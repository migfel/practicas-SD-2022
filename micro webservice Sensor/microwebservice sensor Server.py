from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/microsensor', methods=['GET'])
def sensor_status():
    """Simula el estado del sensor de presencia"""
    status = random.choice([0, 1])
    return jsonify({"sensor_status": status})

if __name__ == '__main__':
    # Corre en un puerto típico para microservicios
    app.run(host='0.0.0.0', port=8080, debug=True)
