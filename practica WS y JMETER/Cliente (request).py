import requests
import json

url = 'http://127.0.0.1:5000/sum'

def send_request(num1, num2):
    payload = {'num1': num1, 'num2': num2}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# Ejemplo de uso
result = send_request(3, 5)
print(result)
