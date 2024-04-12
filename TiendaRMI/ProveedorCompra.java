import java.rmi.*;
import java.rmi.server.*;

class ProveedorCompra extends UnicastRemoteObject implements TiendaOnline {
    public ProveedorCompra() throws RemoteException {
        super();
    }

    public String comprar(String producto) throws RemoteException {
        return "Compra exitosa de " + producto;
    }

    public String agregarAlCarrito(String producto) throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String verCarrito() throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String pagar() throws RemoteException {
        return "Operación no disponible en este proveedor";
    }
}
