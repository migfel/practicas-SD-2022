#ifndef _SOCKET_SERVIDOR_H
#define _SOCKET_SERVIDOR_H

int Abre_Socket_Inet (char *Servicio);
int Abre_Socket_Unix (char *Servicio);
int Acepta_Conexion_Cliente (int Descriptor);

#endif
