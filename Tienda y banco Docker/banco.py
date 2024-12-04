from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validar', methods=['POST'])
def validar_tarjeta():
    data = request.json
    tarjeta = data.get('tarjeta')

    # Simular validación básica
    if tarjeta and tarjeta.startswith("4"):
        return jsonify({"mensaje": "Tarjeta válida"}), 200
    else:
        return jsonify({"error": "Tarjeta inválida"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
