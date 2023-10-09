#include <stdio.h>
#include "Bitmap.h"
int main() {
    int i, j;
    int ancho = 640;
    int alto = 480;
    Bitmap gradiente = createBitmap("gradiente.bmp", ancho, alto, 3);
    for (i = 0; i < ancho; i++) {
        for (j = 0; j < alto; j++) {
            putPixel(&gradiente, i, j, (i / 10) % 64);
        }
    }
    saveBitmap(&gradiente);
}