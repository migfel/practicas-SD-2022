import java.io.*;
import java.net.*;

public class FileReceiver {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Uso: java FileReceiver <puerto>");
            return;
        }

        int port = Integer.parseInt(args[0]);

        try {
            ServerSocket serverSocket = new ServerSocket(port);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                Thread clientThread = new Thread(new ClientHandler(clientSocket));
                clientThread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class ClientHandler implements Runnable {
    private Socket clientSocket;

    public ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try {
            DataInputStream dis = new DataInputStream(clientSocket.getInputStream());

            // Leer nombre del archivo
            String fileName = dis.readUTF();
            System.out.println("Receiving file: " + fileName);

            // Crear un nuevo archivo
            File file = new File("received_" + fileName);
            FileOutputStream fos = new FileOutputStream(file);

            // Fragmentar y recibir el archivo
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = dis.read(buffer)) != -1) {
                fos.write(buffer, 0, bytesRead);
            }

            System.out.println("File received successfully.");

            fos.close();
            dis.close();
            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
