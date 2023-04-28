import java.io.*;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class FileTransferClient {
    public static void main(String[] args) throws RemoteException, NotBoundException, IOException {
        String filename = "archivotransferir.txt";
        File file = new File(filename);
        long fileSize = file.length();
        long chunkSize = fileSize / 10;
        
        Registry registry = LocateRegistry.getRegistry("localhost", 1099);
        FileTransfer stub = (FileTransfer) registry.lookup("FileTransfer");
        
        try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file))) {
            byte[] buffer = new byte[(int) chunkSize];
            int bytesRead = 0;
            while ((bytesRead = bis.read(buffer)) != -1) {
                stub.transferFile(buffer, file.getName());
            }
        }
    }
}
