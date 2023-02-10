#include <stdio.h>

int main() {
    int A;
    scanf("%i", &A);
    int limite = A;
    
    for (int j = 1; j <= (A*A); j++) {
        printf("%i ", j);
        if (limite == j) {
            printf("\n");
            limite += A;
        }
    }
    
    return 0;
}