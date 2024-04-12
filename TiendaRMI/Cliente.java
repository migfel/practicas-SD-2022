import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Cliente {
    public static void main(String[] args) {
        try {
            // Localizar el registro RMI en el servidor
            Registry registry = LocateRegistry.getRegistry("localhost");

            // Buscar los proveedores en el registro RMI
            TiendaOnline proveedorCompra = (TiendaOnline) registry.lookup("Compra");
            TiendaOnline proveedorCarrito = (TiendaOnline) registry.lookup("Carrito");
            TiendaOnline proveedorVerCarrito = (TiendaOnline) registry.lookup("VerCarrito");
            TiendaOnline proveedorPagar = (TiendaOnline) registry.lookup("Pagar");

            // Realizar operaciones con los proveedores
            System.out.println("Resultado del proveedor de compra: " + proveedorCompra.comprar("Producto1"));
            System.out.println("Resultado del proveedor de carrito: " + proveedorCarrito.agregarAlCarrito("Producto2"));
            System.out.println("Resultado del proveedor de ver carrito: " + proveedorVerCarrito.verCarrito());
            System.out.println("Resultado del proveedor de pagar: " + proveedorPagar.pagar());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
