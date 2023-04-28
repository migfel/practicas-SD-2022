import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class FileTransferServer extends UnicastRemoteObject implements FileTransfer {
    public FileTransferServer() throws RemoteException {
        super();
    }

    @Override
    public void transferFile(byte[] data, String filename) throws RemoteException {
        try (FileOutputStream fos = new FileOutputStream(filename, true)) {
            fos.write(data);
        } catch (IOException e) {
            System.err.println("Error writing file: " + e.getMessage());
        }
    }

    public static void main(String[] args) throws RemoteException {
        try {
            FileTransferServer server = new FileTransferServer();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.bind("FileTransfer", server);
            System.out.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
