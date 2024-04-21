#define FILAS 5
#define COLUMNAS 5

// Función para imprimir el tablero
void imprimirTablero(char tablero[FILAS][COLUMNAS]) {
    printf("\n");
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            printf("%c ", tablero[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Función para verificar si el juego ha terminado
int juegoTerminado(char tablero[FILAS][COLUMNAS]) {
    // Verificar si el ratón ha llegado a la esquina superior izquierda
    if (tablero[0][0] == 'R') {
        return 1; // El ratón ganó
    }

    // Verificar si el gato ha atrapado al ratón
    int contadorGatos = 0;
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            if (tablero[i][j] == 'G') {
                contadorGatos++;
            }
        }
    }
    if (contadorGatos == 0) {
        return -1; // El ratón escapó y ganó
    }

    return 0; // El juego aún no ha terminado
}

int main() {
    char tablero[FILAS][COLUMNAS] = {
        {'R', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.'},
        {'.', '.', '.', '.', '.'},
        {'.', '.', '.', '.', 'G'}
    };

    int opcion;
    do {
        printf("JUEGO\n");
        printf("1. JUGAR\n");
        printf("2. ESTADÍSTICAS\n");
        printf("3. INDICACIONES\n");
        printf("4. SALIR\n");
        printf("SELECCIONA OPCIÓN: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                imprimirTablero(tablero);
                while (1) {
                    // Movimiento del ratón
                    int filaRaton, columnaRaton;
                    printf("Ingrese la fila y columna del ratón: ");
                    scanf("%d %d", &filaRaton, &columnaRaton);
                    tablero[filaRaton][columnaRaton] = '.';

                    // Movimiento de los gatos
                    for (int i = 0; i < FILAS; i++) {
                        for (int j = 0; j < COLUMNAS; j++) {
                            if (tablero[i][j] == 'G') {
                                // Lógica de movimiento de los gatos
                                // ...

                                // Actualizar posición del gato en el tablero
                                tablero[i][j] = '.';
                            }
                        }
                    }

                    // Verificar si el juego ha terminado
                    int resultado = juegoTerminado(tablero);
                    if (resultado == 1) {
                        printf("¡El ratón ganó!\n");
                        break;
                    } else if (resultado == -1) {
                        printf("¡El ratón fue atrapado por los gatos!\n");
                        break;
                    }

                    imprimirTablero(tablero);
                }
                break;
            case 2:
                // Lógica para mostrar las estadísticas
                // ...
                break;
            case 3:
                // Lógica para mostrar las indicaciones
                // ...
                break;
            case 4:
                printf("¡Hasta luego!\n");
                break;
            default:
                printf("Opción inválida. Por favor, seleccione una opción válida.\n");
                break;
        }
    } while (opcion != 4);

    return 0;
}
