#include <stdio.h>
#include <string.h>
/*este programa realiza operaciones basicas de manipulacion de cadenas utilizando las fun
ciones de la biblioteca string en c. el usuario ingresa dos palabras y el programa realiza las siguientes acciones:
 1. determina la longitud de cada palabra. 
 2. copia la primera palabra en una nueva cadena.
  3. concatena la segunda palabra a la nueva cadena.
   4. compara las dos palabras ingresadas para determinar si son iguales o cual es mayor en orden lexicografico.
    */



int main() {
    char palabra1[100];
    char palabra2[100];
    char nueva_cadena[200];

    printf("Ingrese la primera palabra: ");
    scanf("%s", palabra1);

    printf("Ingrese la segunda palabra: ");
    scanf("%s", palabra2);

    size_t longitud_palabra1 = strlen(palabra1);
    size_t longitud_palabra2 = strlen(palabra2);

    printf("Longitud de la primera palabra: %zu\n", longitud_palabra1);
    printf("Longitud de la segunda palabra: %zu\n", longitud_palabra2);

    strcpy(nueva_cadena, palabra1);
    strcat(nueva_cadena, palabra2);

    printf("La concatenacion de las palabras es: %s\n", nueva_cadena);

    int comparacion = strcmp(palabra1, palabra2);

    if (comparacion == 0) {
        printf("Las dos palabras son iguales.\n");
    } else if (comparacion < 0) {
        printf("La primera palabra es menor que la segunda en orden lexicografico.\n");
    } else {
        printf("La primera palabra es mayor que la segunda en orden lexicografico.\n");
    }

    return 0;
}
