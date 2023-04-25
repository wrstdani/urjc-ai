#include <stdio.h>
#define N 10
#define FICHERO "prueba.dat"
// los ficheros se abren con fopen y se cierran con fclose
// feof nos dice si hemos llegado o no al final del archivo
// fprintf y fscanf / fputs y fgets / fputc y fgetc (permite leer caracter a caracter)
// rewind(f) rebobina el fichero
/* FICHEROS BINARIOS: escriben la informacion en binario. son incompatibles con otros lenguajes. permiten el acceso
directo a los datos */
/* en ficheros binarios se usa fwrite y fread */
/* fseek busca el situa el puntero del fichero en una posicion concreta del mismo */
int main() {
    FILE *f = fopen(FICHERO, "wb");

    if (f == NULL) {
        perror("Problema de apertura");
        return -1;
    }

    for (int i = 0; i < N; ++i) {
        fwrite(&i, sizeof(int), 1, f);
    }

    if (fclose(f) != 0) {
        perror("Error en clausura.");
    }

    f = fopen(FICHERO, "rb");

    if (f == NULL) {
        perror("Problema de apertura");
        return -1;
    }

    // fseek(f, (3 * sizeof(int)), SEEK_CUR);

    int x;
    while(!feof(f)) {
        fread(&x, sizeof(int), 1, f);
        if ((!feof(f)) && (x % 2 != 0)) printf("%i\t", x);
    }

    if(fclose(f) != 0) {
        perror("Error de clausura.");
    }

    return 0;
}
