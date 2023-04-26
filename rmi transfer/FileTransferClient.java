import java.io.File;
import java.io.FileInputStream;
import java.rmi.Naming;
import java.rmi.RemoteException;

public class FileTransferClient {
    public static void main(String[] args) {
        String host = "localhost";
        String fileName = "archivo.txt";

        try {
            FileTransfer fileTransfer = (FileTransfer) Naming.lookup("rmi://" + host + "/FileTransfer");
            File file = new File(fileName);
            byte[] data = new byte[(int) file.length()];
            FileInputStream fileInputStream = new FileInputStream(file);
            fileInputStream.read(data);
            fileInputStream.close();
            fileTransfer.transferFile(fileName, data);
            System.out.println("Archivo " + fileName + " transferido al servidor.");
        } catch (Exception e) {
            System.err.println("Error al transferir archivo: " + e.getMessage());
        }
    }
}

