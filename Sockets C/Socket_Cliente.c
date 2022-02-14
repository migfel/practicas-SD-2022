
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/*
* Conecta con un servidor Unix, en la misma máquina.
*	Devuelve descriptor de socket si todo es correcto, -1 si hay error.
*/
int Abre_Conexion_Unix (char *Servicio)
{
	struct sockaddr_un Direccion;
	int Descriptor;

	strcpy (Direccion.sun_path, Servicio);
	Direccion.sun_family = AF_UNIX;

	Descriptor = socket (AF_UNIX, SOCK_STREAM, 0);
	if (Descriptor == -1)
		return -1;

	/*
	* Devuelve 0 si todo va bien, -1 en caso de error
	*/
	if (connect (
			Descriptor, 
			(struct sockaddr *)&Direccion, 
			strlen (Direccion.sun_path) + sizeof (Direccion.sun_family)) == -1)
	{
		return -1;
	}
	else
	{
		return Descriptor;
	}
}

/*
/ Conecta con un servidor remoto a traves de socket INET
*/
int Abre_Conexion_Inet (
	char *Host_Servidor, 
	char *Servicio)
{
	struct sockaddr_in Direccion;
	struct servent *Puerto;
	struct hostent *Host;
	int Descriptor;

	Puerto = getservbyname (Servicio, "tcp");
	if (Puerto == NULL)
		return -1;

	Host = gethostbyname (Host_Servidor);
	if (Host == NULL)
		return -1;

	Direccion.sin_family = AF_INET;
	Direccion.sin_addr.s_addr = ((struct in_addr *)(Host->h_addr))->s_addr;
	Direccion.sin_port = Puerto->s_port;
	
	Descriptor = socket (AF_INET, SOCK_STREAM, 0);
	if (Descriptor == -1)
		return -1;

	if (connect (
			Descriptor, 
			(struct sockaddr *)&Direccion, 
			sizeof (Direccion)) == -1)
	{
		return -1;
	}

	return Descriptor;
}
