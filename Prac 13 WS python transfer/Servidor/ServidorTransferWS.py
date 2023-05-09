import cherrypy

class FileTransferService(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def upload_file(self, file):
        with open(file.filename, 'wb') as f:
            data = file.file.read()
            f.write(data)
        return {'message': 'Archivo recibido con éxito'}

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '127.0.0.1'})
    cherrypy.config.update({'server.socket_port': 9005})
    cherrypy.quickstart(FileTransferService())
