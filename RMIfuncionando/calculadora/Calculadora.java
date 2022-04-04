import java.rmi.*;
public interface Calculadora extends Remote {
	public long suma(long a, long b) throws RemoteException;
	public long resta(long a, long b) throws RemoteException;
	public long multiplica(long a, long b) throws RemoteException;
	public long divide(long a, long b) throws RemoteException;
}