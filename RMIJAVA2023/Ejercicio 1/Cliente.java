import java.rmi.Naming;

public class Cliente {

    public static void main(String[] args) {
        try {
            IOperaciones operaciones = (IOperaciones) Naming.lookup("//localhost/Operaciones");
            int resultadoSuma = operaciones.sumar(5, 3);
            int resultadoResta = operaciones.restar(5, 3);
            System.out.println("5 + 3 = " + resultadoSuma);
            System.out.println("5 - 3 = " + resultadoResta);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
