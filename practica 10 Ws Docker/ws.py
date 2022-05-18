import cherrypy
import pandas as pd
import myprocessor
p = myprocessor.MyProcessor()

class MyWebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def process(self):
      data = cherrypy.request.json
      df = pd.DataFrame(data)
      output = p.run(df)
      return output.to_json()
if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())