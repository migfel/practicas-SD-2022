import java.io.*;
import java.net.*;

public class Servidor {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            System.out.println("Servidor iniciado en el puerto 1234...");
            
            Socket socket = serverSocket.accept();
            System.out.println("Cliente conectado: " + socket.getInetAddress().getHostName());
            
            InputStream is = socket.getInputStream();
            BufferedReader br = new BufferedReader(new InputStreamReader(is));
            
            String nombreArchivo = br.readLine();
            System.out.println("Recibiendo archivo " + nombreArchivo + "...");
            
            FileOutputStream fos = new FileOutputStream(nombreArchivo);
            byte[] buffer = new byte[1024];
            int count;
            
            while ((count = is.read(buffer)) > 0) {
                fos.write(buffer, 0, count);
            }
            
            fos.close();
            is.close();
            br.close();
            socket.close();
            serverSocket.close();
            
            System.out.println("Archivo recibido y almacenado correctamente.");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
