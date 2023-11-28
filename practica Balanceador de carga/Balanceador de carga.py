from flask import Flask, jsonify
import requests
import threading

app = Flask(__name__)

def redirect_requests():
    while True:
        response = requests.get('http://127.0.0.1:12345/sum', params={'num1': 5, 'num2': 3})
        print(response.json())

@app.route('/redirect', methods=['GET'])
def redirect():
    threading.Thread(target=redirect_requests).start()
    return jsonify({'message': 'Redirección iniciada'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12346)
