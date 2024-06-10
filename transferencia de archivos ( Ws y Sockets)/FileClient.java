import java.io.*;
import java.net.Socket;

public class FileClient {
    public static void main(String[] args) {
        String serverAddress = "127.0.0.1"; // Dirección IP del servidor
        int serverPort = 12345; // Puerto del servidor

        try (Socket socket = new Socket(serverAddress, serverPort);
             DataInputStream dis = new DataInputStream(socket.getInputStream());
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream())) {

            // Nombre del archivo que deseas descargar
            String fileName = "archivo.txt";
            
            // Enviar el nombre del archivo al servidor
            dos.writeUTF(fileName);

            // Crear un flujo de salida para guardar el archivo
            FileOutputStream fos = new FileOutputStream(fileName);

            // Recibir y guardar el archivo
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = dis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }
            System.out.println("Archivo descargado: " + fileName);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
