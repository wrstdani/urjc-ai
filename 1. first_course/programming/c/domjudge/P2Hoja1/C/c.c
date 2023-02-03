#include <stdio.h>

int main() {
    int N;
    int horas = 0;
    int minutos = 0;
    int segundos = 0;
    scanf("%i", &N);
    while (N > 0) {
        if (N >= 3600) {
            horas += 1;
            N -= 3600;
        }
        else if (N >= 60) {
            minutos += 1;
            N -= 60;
        }
        else {
            segundos += 1;
            N -= 1;
        }
    }
    printf("%i %i %i", horas, minutos, segundos);
    return 0;
}