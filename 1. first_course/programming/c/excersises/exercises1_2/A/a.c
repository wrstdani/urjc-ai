#include <stdio.h>

int isEven_withelse(int x) {
    if (x % 2 != 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int number;
    printf("Give me a number: ");
    scanf("%i", &number);

    if (isEven(number) == 1) {
        printf("EVEN");
    } else {
        printf("ODD");
    }

    return 0;
}