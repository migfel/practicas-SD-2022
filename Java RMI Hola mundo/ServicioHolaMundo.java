import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ServicioHolaMundo extends Remote {
    String saludar() throws RemoteException;
}
