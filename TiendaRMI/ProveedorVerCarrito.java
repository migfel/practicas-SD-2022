import java.rmi.*;
import java.rmi.server.*;

class ProveedorVerCarrito extends UnicastRemoteObject implements TiendaOnline {
    public ProveedorVerCarrito() throws RemoteException {
        super();
    }

    public String comprar(String producto) throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String agregarAlCarrito(String producto) throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String verCarrito() throws RemoteException {
        return "Carrito vacío";
    }

    public String pagar() throws RemoteException {
        return "Operación no disponible en este proveedor";
    }
}
