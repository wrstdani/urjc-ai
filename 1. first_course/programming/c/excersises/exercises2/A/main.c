#include <stdio.h>

void isEven_withElse(int x);
void isEven_withoutElse(int x);

int main() {
    int number;

    printf("Give me an integer: ");
    scanf("%i", &number);

    printf("Using the function with the 'else' statement: \n");
    isEven_withElse(number);

    printf("Using the function without the 'else' statement: \n");
    isEven_withoutElse(number);

    return 0;
}

void isEven_withElse(int x) {
    if (x % 2 == 0) {
        printf("EVEN\n");
    } else {
        printf("ODD\n");
    }
}

void isEven_withoutElse(int x) {
    int module = x % 2;
    switch(module) {
        case 0:
            printf("EVEN\n");
            break;
        case 1:
            printf("ODD\n");
            break;
        default:
            printf("That's not an integer.\n");
    }
}