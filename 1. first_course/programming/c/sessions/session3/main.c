/*
    Second session
    @wrstdani
*/

#include <stdio.h>

int first() {
    printf("First example: int bigger or smaller than 0.\n");
    int a;
    scanf("%i", &a);

    if (a > 0) {
        printf("Bigger than 0.\n");
    }
    else {
        printf("Smaller or equal to 0.\n");
    }

    printf("After if expression.");

    return 0;
}

int second() {
    printf("Second example: char equal or not to a.\n");
    char b;
    printf("Give me a char: ");
    scanf("%c", &b);
    if (b == 'A' || b == 'a') {
        printf("ACIERTO");
    }
    else {
        printf("FALSO");
    }

    return 0;
}

int third() {
    printf("Third example: division.\n");
    int a = 0;
    int b = 7;
    if ((a != 0) && (b / a == 0)) {
        printf("Exact.\n");
    } else {
        printf("Division not done.\n");
    }

    return 0;
}

int fourth() {
    printf("Fourth example: switches.\n");
    char x;
    printf("Dame una letra: ");
    scanf("%c", &x);

    switch (x) {
        case 'a':
            printf("Me diste una a.\n");
            break;
        case 'b':
            printf("Me diste una b.\n");
            break;
        default:
            printf("No me diste ni a ni b.\n");
            break;
    }

    return 0;
}

int fifth() {
    int a = 2;
    int x;
    (a > 0) ? (x=1) : (x=2);
    return 0;
}

int sixth() {
    for (int i = 0; i < 5; ++i) {

    }

    return 0;
}

int seventh() {
    int x = 0;
    do {
        printf("Dame un número: ");
        scanf("%i", &x);
    } while (x != 22);
    return 0;
}

int main() {
    char example;
    printf("Choose an example (1/2/3/4/5/6/7): ");
    scanf("%c", &example);

    switch (example) {
        default:
            printf("You gave me an example that doesn't exist.\n");
            break;
        case '1':
            first();
            break;
        case '2':
            second();
            break;
        case '3':
            third();
            break;
        case '4':
            fourth();
            break;
        case '5':
            fifth();
            break;
        case '6':
            sixth();
            break;
        case '7':
            seventh();
            break;
    }
    return 0;
}
