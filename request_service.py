import requests

def export_logs(data, token):
    requests.post(url='http://localhost:8080/api/logs', json=data, headers={'Authorization': 'Bearer ' + token.json()['id_token'], "content-type": "application/json"})
