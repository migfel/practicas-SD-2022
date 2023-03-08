// Definimos unos hilos simples. Se detendrán un momento
// antes de imprimir sus nombres y retardos
// considera que este archivo podria separarse en un archivo ProbarHilo y en otro que se llame MultiHola
// entonces es susceptible de que los podamos alojar en maquinas diferentes
// la pregunta seria , sera codigo remoto o codigo distribuido?

class ProbarHilo extends Thread {
    private String nombre;
    private int retardo;

    // Constructor para almacenar nuestro nombre
    // y el tiempo de retardo
    public ProbarHilo( String s,int d ) {
        nombre = s;
        retardo = d;
        }

    // El metodo run() es similar al main(), pero para threads. 
        // Cuando run() termina el thread muere , es decir termina y no se ejecuta mas
    public void run() {
        // Retrasamos la ejecución el tiempo especificado
        try {
            sleep( retardo );
        } catch( InterruptedException e ) {
            ;
        }

        // Ahora imprimimos el nombre
        System.out.println( "Hola Mundo! "+nombre+" "+retardo );
        }
    }

public class MultiHola {
    public static void main( String args[] ) {
      
      // definimos 3 hilos 
        ProbarHilo t1,t2,t3;

        // Creamos los threads y en el constructor indicamos el tiempo de retardo de forma aleatoria 
        t1 = new ProbarHilo( "Hilo 1",(int)(Math.random()*2000) );
        t2 = new ProbarHilo( "Hilo  2",(int)(Math.random()*2000) );
        t3 = new ProbarHilo( "Hilo 3",(int)(Math.random()*2000) );

        // Arrancamos los threads
        t1.start();
        t2.start();
        t3.start();
        }
    }
