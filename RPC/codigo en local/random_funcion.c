/* Archivo random_funcion.c que incluye la definición de las funciones a utilizar */
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>#include "random_local.h"

void inicializa_random(long semilla)
{
srandom(semilla);
}
double obtiene_siguiente_random(void)
{
return random();
}
