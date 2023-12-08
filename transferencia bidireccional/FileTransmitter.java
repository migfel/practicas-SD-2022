import java.io.*;
import java.net.*;

public class FileTransmitter {
    public static void main(String[] args) {
        if (args.length != 3) {
            System.out.println("Uso: java FileTransmitter <host> <puerto> <archivo>");
            return;
        }

        String host = args[0];
        int port = Integer.parseInt(args[1]);
        String fileName = args[2];

        try {
            Socket socket = new Socket(host, port);
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            // Enviar nombre del archivo
            dos.writeUTF(fileName);

            // Enviar archivo en binario
            FileInputStream fis = new FileInputStream(fileName);
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                dos.write(buffer, 0, bytesRead);
            }

            System.out.println("File sent successfully.");

            fis.close();
            dos.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
