import requests
import json

def export_logs(data):
    token = requests.post(url='http://localhost:8080/api/authenticate', json=json.loads('{"password": "admin","username": "admin"}'), headers={"content-type": "application/json"})
    requests.post(url='http://localhost:8080/api/logs', json=data, headers={'Authorization': 'Bearer ' + token.json()['id_token'], "content-type": "application/json"})
