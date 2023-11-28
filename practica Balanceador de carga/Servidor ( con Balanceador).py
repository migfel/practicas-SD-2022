from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

def handle_request():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/sum', methods=['GET'])
def sum_numbers():
    return handle_request()

def start_server():
    app.run(host='0.0.0.0', port=12345)

if __name__ == "__main__":
    threading.Thread(target=start_server).start()
