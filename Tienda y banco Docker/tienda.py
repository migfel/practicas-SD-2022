from flask import Flask, request, jsonify

app = Flask(__name__)

# Productos disponibles en la tienda
productos = [
    {"id": 1, "nombre": "Laptop", "precio": 1000},
    {"id": 2, "nombre": "Smartphone", "precio": 700},
    {"id": 3, "nombre": "Auriculares", "precio": 100},
    {"id": 4, "nombre": "Monitor", "precio": 300},
    {"id": 5, "nombre": "Teclado", "precio": 50},
]

@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(productos)

@app.route('/comprar', methods=['POST'])
def comprar_producto():
    data = request.json
    producto_id = data.get('producto_id')
    tarjeta = data.get('tarjeta')

    # Simular validación con el banco (BVVA)
    if not tarjeta:
        return jsonify({"error": "Tarjeta no proporcionada"}), 400
    
    # Supongamos que el banco está en localhost:5001
    import requests
    respuesta = requests.post("http://localhost:5001/validar", json={"tarjeta": tarjeta})
    if respuesta.status_code == 200:
        return jsonify({"mensaje": "Compra exitosa"}), 200
    else:
        return jsonify({"error": "Compra fallida"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
