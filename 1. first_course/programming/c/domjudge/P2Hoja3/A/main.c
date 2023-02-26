#include <stdio.h>
#define NUM 10

int main() {
    int N, count1 = 0, array[NUM] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, arrayCount[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    do {
        scanf("%i", &N);
        for (int i = 0; i < NUM; ++i) {
            if (array[i] == N) {
                arrayCount[i] += 1;
            }
        }
    } while (N != -1);

    for (int j = 0; j < NUM; ++j) {
        if (arrayCount[j] >= 3) {
            printf("%i ", array[j]);
        }
    }

    return 0;
}
