#include <stdio.h>

int main() {
    double altura;
    printf("Give me the person's height: ");
    scanf("%d", &altura);
    
    if (altura <= 1.50) {
        printf("Low height.");
    } else if (1.51 <= altura <= 1.70) {
        printf("Average height.");
    } else if (1.71 <= altura <= 1.90) {
        printf("High height.");
    } else if (1.91 <= altura) {
        printf("Very high height.");
    }

    return 0;
}