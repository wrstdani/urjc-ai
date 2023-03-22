#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
    int nRows, nCols;

    printf("Give me a number of rows and a number of columns:");
    scanf("%i %i", &nRows, &nCols);

    srand(time(NULL));

    int matrix[nRows][nCols];

    for (int i = 0; i < nRows; ++i) {
        for (int j = 0; j < nCols; ++j) {
            matrix[i][j] = rand();
        }
    }

    for (int i = 0; i < nRows; ++i) {
        for (int j = 0; j < nCols; ++j) {
            printf("%i ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
