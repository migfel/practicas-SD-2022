from python:3.6.4-slim-jessie
RUN pip install pandas
RUN pip install CherryPy
COPY myprocessor.py .
COPY ws.py .
EXPOSE 8080
ENTRYPOINT ["python", "ws.py"]