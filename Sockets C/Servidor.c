/*

* Programa Servidor de socket INET, como ejemplo de utilizacion de las
* funciones de sockets.
*/
#include <Socket_Servidor.h>
#include <Socket.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h> // for open sockets
#include <unistd.h> // for close sockets
int main ()
{
	/*
	* Descriptores de socket servidor y de socket con el cliente
	*/
	int Socket_Servidor;
	int Socket_Cliente;
	char Cadena[100];

	/*
	* Se abre el socket servidor, con el servicio "cpp_java" dado de
	* alta en el archivo de /etc/services.
	*/
	Socket_Servidor = Abre_Socket_Inet ("cpp_java");
	if (Socket_Servidor == -1)
	{
		printf ("No se puede abrir socket servidor\n");
		exit (-1);
	}

	/*
	* Se espera un cliente que quiera conectarse
	*/
	Socket_Cliente = Acepta_Conexion_Cliente (Socket_Servidor);
	if (Socket_Servidor == -1)
	{
		printf ("No se puede abrir socket de cliente\n");
		exit (-1);
	}

	/*
	* Se lee la informacion del cliente, suponiendo que va a enviar 
	* 5 caracteres.
	*/
	Lee_Socket (Socket_Cliente, Cadena, 5);

	/*
	* Se escribe en pantalla la informacion que se ha recibido del
	* cliente
	*/
	printf ("Soy Servior, he recibido : %s\n", Cadena);

	/*
	* Se prepara una cadena de texto para enviar al cliente. La longitud
	* de la cadena es 5 letras + \0 al final de la cadena = 6 caracteres
	*/
	strcpy (Cadena, "Adios");
	Escribe_Socket (Socket_Cliente, Cadena, 6);

	/*
	* Se cierran los sockets
	*/
	close (Socket_Cliente);
	close (Socket_Servidor);
}
