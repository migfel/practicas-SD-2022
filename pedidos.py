#para ejecutar seguir estos pasos en widnows
#pip install flask
#crea el ambiente
#python -m venv env
#env\Scripts\activate
#set FLASK_APP=pedidos.py
#cambia el puerto
#flask run --port=8082
#por ultimo recuerda debes invocarlo con la ruta y parametros ( el endpoint)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/pedidos/', methods=['POST'])
def crear_pedido():
    # Lógica para crear un nuevo pedido
    datos_pedido = request.get_json()
    # Procesar los datos del pedido y realizar acciones necesarias
    # ...

    return jsonify({'mensaje': 'Pedido creado correctamente'}, datos_pedido)

if __name__ == '__main__':
    app.run()
