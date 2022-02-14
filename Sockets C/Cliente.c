/*
* Programa Cliente de un socket INET, como ejemplo de utilizacion
* de las funciones de sockets
*/
#include <stdio.h>
#include <Socket_Cliente.h>
#include <Socket.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h> // for open sockets
#include <unistd.h> // for close sockets


int  main ()
{
	/*
	* Descriptor del socket y buffer para datos
	*/
	int Socket_Con_Servidor;
	char Cadena[100];

	/*
	* Se abre la conexion con el servidor, pasando el nombre del ordenador
	* y el servicio solicitado.
	* "localhost" corresponde al nombre de la computadoras en la que
	* estamos ejecutando. Esta dado de alta en /etc/hosts
	* "cpp_java" es un servicio dado de alta en /etc/services
	*/
	Socket_Con_Servidor = Abre_Conexion_Inet ("localhost", "cpp_java");
	if (Socket_Con_Servidor == 1)
	{
		printf ("No puedo establecer conexion con el servidor\n");
		exit (-1);
	}

	/*
	* Se prepara una cadena con 5 caracteres y se envia, 4 letras mas
	* el \0 que indica fin de cadena en C
	*/
	strcpy (Cadena, "Hola");
	Escribe_Socket (Socket_Con_Servidor, Cadena, 5);

	/*
	* Se lee la informacion enviada por el servidor, que se supone es
	* una cadena de 6 caracteres.
	*/
	Lee_Socket (Socket_Con_Servidor, Cadena, 6);

	/*
	* Se escribe en pantalla la informacion recibida del servidor
	*/
	printf ("Soy cliente, He recibido : %s\n", Cadena);

	/*
	* Se cierra el socket con el servidor
	*/
	close (Socket_Con_Servidor);
}
