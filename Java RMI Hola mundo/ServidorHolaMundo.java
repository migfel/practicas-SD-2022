import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ServidorHolaMundo extends UnicastRemoteObject implements ServicioHolaMundo {
    public ServidorHolaMundo() throws RemoteException {
        super();
    }

    public String saludar() throws RemoteException {
        return "Hola Mundo desde el servidor RMI!";
    }
}
