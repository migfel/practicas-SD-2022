import requests

def send_request():
    response = requests.get('http://127.0.0.1:12346/redirect')
    print(response.json())

if __name__ == "__main__":
    send_request()
