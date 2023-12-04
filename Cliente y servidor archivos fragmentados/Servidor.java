import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Servidor esperando conexiones...");

            Socket socket = serverSocket.accept();
            System.out.println("Cliente conectado.");

            DataInputStream dis = new DataInputStream(socket.getInputStream());

            // Recibe y concatena los fragmentos
            byte[] archivoIntegrado = new byte[10 * 1024]; // 10 fragmentos de 1 KB cada uno
            for (int i = 0; i < 10; i++) {
                dis.readFully(archivoIntegrado, i * 1024, 1024);
            }

            // Guarda el archivo integrado
            FileOutputStream fos = new FileOutputStream("archivoIntegrado.txt");
            fos.write(archivoIntegrado);
            fos.close();

            System.out.println("Archivo integrado correctamente.");

            serverSocket.close();
            socket.close();
            dis.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
