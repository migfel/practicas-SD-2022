
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Server implements Hello {

    public Server() {}

    public String sayHello() {
        return "Hola, Mundo en sistemas distribuidos desde el Servidor, esto podria ser Amazon respondiendo un proceso de pago!";
    }

    public static void main(String args[]) {

        try {
            Server obj = new Server();
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            // Enlazar el stub del objeto remoto en el registro
        //Naming proporciona métodos para almacenar y obtener referencias a objetos remotos en un registro de objetos remotos.
            java.rmi.Naming.rebind("//" +java.net.InetAddress.getLocalHost().getHostAddress()+ ":1099/Hello", stub);
       

            System.err.println("el servidor esta listo y acepta conexiones");
        } catch (Exception e) {
            System.err.println("Excepcion del Servidor : " + e.toString());
            e.printStackTrace();
        }
    }
}