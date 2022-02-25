
package rmi;
//Interfaz de tipo remota, cabe resaltar que
// solo tiene el metodo echo ( no hya instrucciones) 
public interface EchoInterface extends java.rmi.Remote 
{
    public String echo(String input)throws java.rmi.RemoteException;
}
