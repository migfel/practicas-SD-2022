import java.rmi.Remote;
import java.rmi.RemoteException;

public interface FileTransfer extends Remote {
    public void transferFile(String fileName, byte[] data) throws RemoteException;
}
