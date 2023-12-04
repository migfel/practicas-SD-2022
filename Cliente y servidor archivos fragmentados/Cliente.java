import java.io.*;
import java.net.*;

public class Cliente {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 12345);
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            // Lee el archivo a enviar
            File archivo = new File("archivo.txt");
            FileInputStream fis = new FileInputStream(archivo);

            byte[] buffer = new byte[1024];
            int bytesRead;

            // Fragmenta y envía el archivo en 10 partes
            while ((bytesRead = fis.read(buffer)) != -1) {
                for (int i = 0; i < 10; i++) {
                    dos.write(buffer, i * (bytesRead / 10), bytesRead / 10);
                    dos.flush();
                }
            }

            fis.close();
            dos.close();
            socket.close();

            System.out.println("Archivo enviado correctamente.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
