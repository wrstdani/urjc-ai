#include <stdio.h>

int main() {
    char x;
    int y = 0;
    do {
        scanf("%c", &x);
        if (x == ',') {
            y += 1;
        }
    } while (x != '*');
    printf("%i", y);
    return 0;
}