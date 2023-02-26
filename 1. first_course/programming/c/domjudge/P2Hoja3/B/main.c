#include <stdio.h>

int main() {
    int N, M;

    scanf("%i", &N);

    int array[N];

    for (int i = 0; i < N; ++i) {
        scanf("%i", &M);

        array[i] = M;
    }

    int minimum = array[0];

    for (int j = 0; j < N; ++j) {
        if (minimum > array[j]) {
            minimum = array[j];
        }
    }

    for (int a = 0; a < N; ++a) {
        int result = array[a] - minimum;
        if (result != 0) {
            printf("%i\n", result);
        }
    }
    return 0;
}
