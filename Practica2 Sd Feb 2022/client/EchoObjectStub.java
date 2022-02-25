
package client;
import java.net.*;
import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import rmi.EchoInterface;
public class EchoObjectStub implements EchoInterface{
    private Socket echoSocket = null;
    private PrintWriter os = null;
    private BufferedReader is = null;
    private String host = "localhost";
    private int port=7;
    private String output = "Error";
    private boolean connected = false;
    public void setHostAndPort(String host, int port) {
        this.host= host; this.port =port;
    }
    public String echo(String input)throws java.rmi.RemoteException {
        try {
            connect();
        } catch (IOException ex) {
            Logger.getLogger(EchoObjectStub.class.getName()).log(Level.SEVERE, null, ex);
        }
        if (echoSocket != null && os != null && is != null) {
            try {
                os.println(input);
                os.flush();
                output= is.readLine();
            } catch (IOException e) {
                System.err.println("I/O failed in reading/writing socket");
                throw new java.rmi.RemoteException("I/O failed in reading/writing socket");
            }
        }
        try {
            disconnect();
        } catch (IOException ex) {
            Logger.getLogger(EchoObjectStub.class.getName()).log(Level.SEVERE, null, ex);
        }
        return output;
    }
    private synchronized void connect() throws
    java.rmi.RemoteException, IOException {
    //EJERCICIO: Implemente el método connect
        echoSocket = new Socket(host, port);
        os=new PrintWriter(echoSocket.getOutputStream());
        is=new BufferedReader( new InputStreamReader(echoSocket.getInputStream()));
    }
    private synchronized void disconnect() throws IOException{
    //EJERCICIO: Implemente el método disconnect
        os.close();
        is.close();
        echoSocket.close();
    }
}
