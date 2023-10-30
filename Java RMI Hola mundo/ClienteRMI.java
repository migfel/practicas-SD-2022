import java.rmi.Naming;

public class ClienteRMI {
    public static void main(String[] args) {
        try {
            ServicioHolaMundo servicio = (ServicioHolaMundo) Naming.lookup("rmi://localhost/ServicioHolaMundo");
            String saludo = servicio.saludar();
            System.out.println(saludo);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
