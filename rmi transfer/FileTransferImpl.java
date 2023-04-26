import java.io.FileOutputStream;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class FileTransferImpl extends UnicastRemoteObject implements FileTransfer {
    public FileTransferImpl() throws RemoteException {
        super();
    }

    public void transferFile(String fileName, byte[] data) throws RemoteException {
        try {
            FileOutputStream file = new FileOutputStream(fileName);
            file.write(data);
            file.close();
            System.out.println("Archivo " + fileName + " transferido con éxito.");
        } catch (Exception e) {
            System.err.println("Error al transferir archivo: " + e.getMessage());
        }








    }
}
