import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class OperacionesImpl extends UnicastRemoteObject implements IOperaciones {

    public OperacionesImpl() throws RemoteException {
        super();
    }

    @Override
    public int sumar(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int restar(int a, int b) throws RemoteException {
        return a - b;
    }
}
