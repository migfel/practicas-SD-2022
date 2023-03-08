
/** muy importante recuerden que aquino hay main, porque este es un hilo que alguien mas debe mandar ejecutar 
*/
public class animal extends Thread {
    String nombre;
    int limite;
    
    public animal(String nombre, int limite)
    {
        this.nombre = nombre;
        this.limite = limite;
        }
    
    
    @Override
    public void run()
        {
        for (int n=0; n<limite;n++) 
            {
            System.out.println(nombre+"  avanza");
            }
           System.out.println(nombre+"   ha llegado a la meta");
    this.yield();
     }
}

