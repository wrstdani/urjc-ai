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
    int H, P, minplatos = 1;

    scanf("%i %i", &H, &P);

    int count = 0, array[P];

    for (int i = 0; i < P; ++i) {
        scanf("%i", array[i]);
    }

    for (int j = 0; j < P; ++j) {
        count += array[j];
    }

    if (count < H) {
        printf("Sinpa");
    } else {
        for (int x = 0; x < P; ++x) {
            for (int y = 0; y < P; ++y) {
                if (array[x] + array[y] >= H) {
                    minplatos++;
                }
            }
        }
        printf("%i", minplatos);
    }
}