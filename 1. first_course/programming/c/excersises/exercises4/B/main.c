#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int nRows, nCols;

    printf("Give me a number of rows and a number of columns:");
    scanf("%i %i", &nRows, &nCols);

    int matrix[nRows][nCols];

    srand(time(NULL));

    for (int i = 0; i < nRows; ++i) {
        for (int j = 0; j < nCols; ++j) {
            matrix[i][j] = rand();
        }
    }

    // Print initial matrix
    for (int i = 0; i < nRows; ++i) {
        for (int j = 0; j < nCols; ++j) {
            printf("%i", matrix[i][j]);
        }
        printf("\n ");
    }

    return 0;
}
