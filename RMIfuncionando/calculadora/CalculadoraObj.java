import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.net.*;

public class CalculadoraObj extends UnicastRemoteObject implements Calculadora {
	// hace falta un constructor explicito
	public CalculadoraObj() throws RemoteException {
		super();
	}
	public long suma(long a, long b) throws RemoteException {
		return a + b;
	}
	public long resta(long a, long b) throws RemoteException {
		return a - b;
	}
	public long multiplica(long a, long b) throws RemoteException {
		return a * b;
	}
	public long divide(long a, long b) throws RemoteException {
		return a / b;
	}
}