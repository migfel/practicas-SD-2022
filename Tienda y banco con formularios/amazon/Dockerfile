# Usar una imagen base de Python
FROM python:3.9-slim
# Establecer el directorio de trabajo
WORKDIR /app
# Copiar los archivos necesarios al contenedor
COPY amazon.py /app/
COPY templates /app/templates/
COPY requirements.txt /app/
# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt
# Exponer el puerto en el que correrá el servicio
EXPOSE 5000
# Comando para ejecutar la aplicación
CMD ["python", "amazon.py"]
