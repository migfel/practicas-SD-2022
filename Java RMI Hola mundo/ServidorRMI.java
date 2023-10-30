import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class ServidorRMI {
    public static void main(String[] args) {
        try {
            ServicioHolaMundo servicio = new ServidorHolaMundo();
            LocateRegistry.createRegistry(1099); // Puerto predeterminado para RMI
            Naming.rebind("ServicioHolaMundo", servicio); // Registra el servicio en el registro RMI
            System.out.println("Servidor RMI iniciado.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
