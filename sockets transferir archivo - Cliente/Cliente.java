import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 1234);
            
            OutputStream os = socket.getOutputStream();
            PrintWriter pw = new PrintWriter(os, true);
            
            pw.println("archivo.txt");
            System.out.println("Enviando archivo...");
            
            FileInputStream fis = new FileInputStream("archivo.txt");
            byte[] buffer = new byte[1024];
            int count;
            
            while ((count = fis.read(buffer)) > 0) {
                os.write(buffer, 0, count);
            }
            
            fis.close();
            os.close();
            pw.close();
            socket.close();
            
            System.out.println("Archivo enviado correctamente.");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
