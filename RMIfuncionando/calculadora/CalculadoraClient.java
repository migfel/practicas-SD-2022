import java.rmi.*;
import java.net.*;

public class CalculadoraClient {
	
	public static void main(String[] args) {
		
		if( args.length < 3 ) {
			System.out.println("Uso: java CalculadoraClient <ip> <a> <b>");
			return;
		}
		
		String ip = args[0];
		long a = Long.parseLong(args[1]);
		long b = Long.parseLong(args[2]);

		try {
			Calculadora c = (Calculadora) Naming.lookup("//"+ip+"/ServicioDeCalculadora");
			System.out.println(a+" - "+b+" = " + c.resta(a, b));
			System.out.println(a+" + "+b+" = " + c.suma(a, b));
			System.out.println(a+" * "+b+" = " + c.multiplica(a, b));
			System.out.println(a+" / "+b+" = " + c.divide(a, b));
		} catch (Exception e) {
			System.out.println(e);
		}
	}

}