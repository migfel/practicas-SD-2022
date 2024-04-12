import java.rmi.*;

public class Cliente2 {
    public static void main(String[] args) {
        try {
            // Conectar con el servidor RMI
            TiendaOnline proveedorCompra = (TiendaOnline) Naming.lookup("rmi://localhost/Compra");
            TiendaOnline proveedorCarrito = (TiendaOnline) Naming.lookup("rmi://localhost/Carrito");
            TiendaOnline proveedorVerCarrito = (TiendaOnline) Naming.lookup("rmi://localhost/VerCarrito");
            TiendaOnline proveedorPagar = (TiendaOnline) Naming.lookup("rmi://localhost/Pagar");

            // Realizar operaciones con los proveedores
            System.out.println("Resultado del proveedor de compra: " + proveedorCompra.comprar("Producto3"));
            System.out.println("Resultado del proveedor de carrito: " + proveedorCarrito.agregarAlCarrito("Producto4"));
            System.out.println("Resultado del proveedor de ver carrito: " + proveedorVerCarrito.verCarrito());
            System.out.println("Resultado del proveedor de pagar: " + proveedorPagar.pagar());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
