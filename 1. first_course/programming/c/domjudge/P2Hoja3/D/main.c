#include <stdio.h>

int main() {
    int N;

    scanf("%i", &N);

    int board[N][N], dim = N*N, count = 1, rows, cols;

    while (count <= dim) {
        // cols right
        for (cols = 0; cols < N; ++cols) {
            
            count++;
        }

        // rows down
        for (rows = 0; rows < N; ++rows) {

            count++;
        }

        // rows up
        for (rows = 0; rows < N; --rows) {

            count++;
        }

        // cols left
        for (cols = 0; cols < N; --cols) {

            count++;
        }

        count++;
    }


    // print board
    for (rows = 0; rows < N; ++rows) {
        for (cols = 0; cols < N; ++cols) {
            printf("%i ", board[rows][cols]);
        }
        printf("\n");
    }


    return 0;
}
