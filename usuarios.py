#para ejecutar seguir estos pasos en widnows
#pip install flask
#crea el ambiente
#python -m venv env
#env\Scripts\activate
#set FLASK_APP=usuarios.py
#cambia el puerto
#flask run --port=8080
#por ultimo recuerda debes invocarlo con la ruta y parametros ( el endpoint)


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obtener_usuario(usuario_id):
    # Lógica para obtener información del usuario desde una base de datos
    usuario = {
        'id': usuario_id,
        'nombre': 'Felix Mata',
        'correo': 'migfel@gmail.com'
    }
    return jsonify(usuario)

if __name__ == '__main__':
    app.run()
