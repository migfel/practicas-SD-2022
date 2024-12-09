from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS

@app.route('/validar', methods=['POST'])
def validar():
    data = request.json
    nombre = data.get('nombre')
    numero = data.get('numero')
    cvc = data.get('cvc')

    # Validar datos de la tarjeta
    if not nombre or not numero or not cvc:
        return jsonify({"mensaje": "Datos de tarjeta incompletos"}), 400

    if cvc.startswith("4"):  # El CVC inicia con 4
        return jsonify({"mensaje": "Tarjeta aprobada"}), 200
    else:
        return jsonify({"mensaje": "Tarjeta rechazada"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
