#include <stdio.h>
#include <strings.h>
#define N 100

int main() {
    char sentence[N];
    int count = 0;

    printf("Enter a sentence: ");
    fgets(sentence, N, stdin);

    for (int i = 0; i < strlen(sentence); ++i) {
        if (i > 0 && sentence[i] == ' ' && sentence[(i - 1)] != ' ') {
            count++;
        }
    }

    printf("The sentence written is: %s" "It has %i words.", sentence, ++count);

    return 0;
}
