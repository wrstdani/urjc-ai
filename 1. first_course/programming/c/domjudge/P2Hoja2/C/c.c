#include <stdio.h>

int main() {
    int n;
    scanf("%i", &n);
    if (n > 46) {
        printf("MUY BUENA");
    }
    else if (n >= 36 && n <= 46) {
        printf("BUENA");
    }
    else if (n >= 21 && n <= 35) {
        printf("REGULAR");
    }
    else if (n >= 11 && n <= 20) {
        printf("MALA");
    }
    else {
        printf("CRUZCAMPO");
    }
    return 0;
}