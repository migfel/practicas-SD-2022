from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/comprar', methods=['POST'])
def comprar():
    data = request.json  # Datos enviados desde el formulario
    tarjeta = data.get('tarjeta')

    # Enviar datos al microservicio BBVA
    bbva_url = "http://127.0.0.1:5001/validar"
    response = requests.post(bbva_url, json=tarjeta)

    if response.status_code == 200:
        return jsonify({"mensaje": "Compra aprobada y pagada"}), 200
    else:
        return jsonify({"mensaje": "Compra rechazada"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
