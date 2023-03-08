

/**
 *
*/
public class AppHilos {

    /**
     * @los parametros de args recuerden que los recibimos de lo que escribimso en consola 
     */
    public static void main(String[] args) {
        
        animal conejo= new animal("conejo", 100);
        animal tortuga= new animal("tortuga", 100);
        animal perro=new animal("perro", 100);
    
    conejo.start();
    tortuga.start();
    perro.start();
    
    //System.out.println("La carrera ha terminado");
    
    
    }
}

