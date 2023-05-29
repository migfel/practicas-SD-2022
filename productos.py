#para ejecutar seguir estos pasos en widnows
#pip install flask
#crea el ambiente
#python -m venv env
#env\Scripts\activate
#set FLASK_APP=productos.py
#cambia el puerto
#flask run --port=8081
#por ultimo recuerda debes invocarlo con la ruta y parametros ( el endpoint)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto(producto_id):
    # Lógica para obtener información del producto desde una base de datos
    producto = {
        'id': producto_id,
        'nombre': 'Laptop',
        'precio': 1999.99
    }
    return jsonify(producto)

if __name__ == '__main__':
    app.run()
