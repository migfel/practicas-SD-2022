all : Socket.o Socket_Servidor.o Socket_Cliente.o Servidor Cliente

CPPFLAGS = -g -I.

Servidor : Servidor.c
	cc -g -I. Socket.o Socket_Servidor.o Servidor.c -o Servidor

Cliente : Cliente.c
	cc -g -I. Socket.o Socket_Cliente.o Cliente.c -o Cliente

clean :
	rm *.o Cliente Servidor
