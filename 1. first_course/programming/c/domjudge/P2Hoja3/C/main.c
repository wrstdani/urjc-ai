#include <stdio.h>

void Tim();

int main() {
    int R;

    scanf("%i", &R);

    for (int i = 0; i < R; ++i) {
        Tim();
    }

    return 0;
}

void Tim() {
    int H, P, Hplatos;

    scanf("%i %i", &H, &P);

    for (int i = 0; i < P; ++i) {
        scanf("%i", &Hplatos);
    }

    if (Hplatos < H) {
        printf("Sinpa");
    } else {

        }
    }
