import java.rmi.*;
import java.rmi.server.*;

class ProveedorPagar extends UnicastRemoteObject implements TiendaOnline {
    public ProveedorPagar() throws RemoteException {
        super();
    }

    public String comprar(String producto) throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String agregarAlCarrito(String producto) throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String verCarrito() throws RemoteException {
        return "Operación no disponible en este proveedor";
    }

    public String pagar() throws RemoteException {
        return "Pago realizado con éxito";
    }
}
