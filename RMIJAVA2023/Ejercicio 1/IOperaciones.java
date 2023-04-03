import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IOperaciones extends Remote {
    public int sumar(int a, int b) throws RemoteException;
    public int restar(int a, int b) throws RemoteException;
}
