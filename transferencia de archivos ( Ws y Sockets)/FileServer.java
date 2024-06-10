import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class FileServer {
    public static void main(String[] args) {
        int port = 12345; // Puerto del servidor
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("El servidor está escuchando en el puerto " + port);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado desde " + clientSocket.getInetAddress().getHostAddress());

                try (DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                     DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {

                    // Recibir el nombre del archivo del cliente
                    String fileName = dis.readUTF();

                    // Crear un flujo de entrada para el archivo
                    FileInputStream fis = new FileInputStream(fileName);

                    // Enviar el archivo al cliente
                    byte[] buffer = new byte[4096];
                    int bytesRead;
                    while ((bytesRead = fis.read(buffer)) != -1) {
                        dos.write(buffer, 0, bytesRead);
                    }
                    System.out.println("Archivo enviado: " + fileName);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
