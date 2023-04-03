import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class Servidor {

    public static void main(String[] args) throws RemoteException {
        try {
            LocateRegistry.createRegistry(1099);
            Naming.rebind("//localhost/Operaciones", new OperacionesImpl());
            System.out.println("Servidor listo...");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
