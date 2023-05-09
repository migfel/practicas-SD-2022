import requests

url = 'http://127.0.0.1:9005/upload_file'

with open('texto.txt', 'rb') as f:
    files = {'file': ('texto.txt', f)}
    response = requests.post(url, files=files)

print(response.json())
