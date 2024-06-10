from flask import Flask, request, jsonify, send_file
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

app = Flask(__name__)

# Ruta para cargar un archivo en el servidor
@app.route('/upload', methods=['POST'])
def cargar_archivo():
    archivo_cargado = request.files['file']
    if archivo_cargado.filename != '':
        # Establece la ubicación donde se almacenarán los archivos cargados
        carpeta_carga = 'cargas'
        os.makedirs(carpeta_carga, exist_ok=True)
        ruta_archivo = os.path.join(carpeta_carga, archivo_cargado.filename)
        archivo_cargado.save(ruta_archivo)
        return jsonify({'mensaje': 'Archivo cargado exitosamente'})

# Ruta para descargar un archivo desde el servidor
@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    ruta_archivo = os.path.join('cargas', nombre_archivo)
    if os.path.exists(ruta_archivo):
        return send_file(ruta_archivo, as_attachment=True)
    return jsonify({'mensaje': 'Archivo no encontrado'})

if __name__ == '__main__':
    # Abre un cuadro de diálogo en el servidor para seleccionar el puerto
    Tk().withdraw()
    puerto = int(input("Ingresa el número de puerto para ejecutar el servidor: "))

    app.run(port=puerto)
