import java.net.*;
import java.io.*;

public class Servidor {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = null;
        boolean listening = true;
        try {
            serverSocket = new ServerSocket(9090);
        } catch (IOException e) {
            System.err.println("No se pudo escuchar en el puerto: 9090.");
            System.exit(-1);
        }
        while (listening) {
            new HiloServidor(serverSocket.accept()).start();
        }
        serverSocket.close();
    }
}

class HiloServidor extends Thread {
    private Socket socket = null;

    public HiloServidor(Socket socket) {
        super("HiloServidor");
        this.socket = socket;
    }

    public void run() {
        try {
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            String inputLine, outputLine;
            outputLine = "Hola, bienvenido al servidor. Escribe 'adios' para salir.";
            out.println(outputLine);

            while ((inputLine = in.readLine()) != null) {
                if (inputLine.equals("adios"))
                    break;
                outputLine = "Respuesta del servidor: " + inputLine;
                out.println(outputLine);
            }
            out.close();
            in.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
