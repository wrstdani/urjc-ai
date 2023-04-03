// sesion 31 de marzo

#include <stdio.h>
#include <string.h>

int main() {
    FILE *fichero = fopen("texto.txt", "w");

    if (fichero == NULL) {
        perror("Error de apertura.\n");
        return -1;
    }

    fprintf(fichero, "Hello world!\n"); // escribimos "Hello world!" y salto de línea (línea nueva) en texto.txt

    if (fclose(fichero) != 0) {
        perror("Error de clausura.\n");
    }

    return 0;
}
