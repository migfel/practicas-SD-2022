from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simular el estado del sensor
def get_sensor_status():
    # Genera un estado aleatorio: 1 (presencia detectada) o 0 (sin presencia)
    return random.choice([0, 1])

@app.route('/sensor/status', methods=['GET'])
def sensor_status():
    # Devuelve el estado actual del sensor
    status = get_sensor_status()
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)







