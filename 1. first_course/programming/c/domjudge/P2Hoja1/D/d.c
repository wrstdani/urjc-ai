/*
    César V1 en C
    @wrstdani
*/

#include <stdio.h>
#include <string.h>

int main() {
    char *abc = "abcdefghijklmnopqrstuvwxyz";
    char C;
    int N;
    scanf(" %c", &C);
    scanf(" %i", &N);
    for (int i = 0; i < strlen(abc); i++) {
        if (abc[i] == C) {
            printf("%c", abc[(i + N) % 26]);
        }
    }
    return 0;
}