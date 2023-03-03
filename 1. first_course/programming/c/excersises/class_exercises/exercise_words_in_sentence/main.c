#include <stdio.h>
#define MAX_CHAR 1000

int main() {
    char sentence[MAX_CHAR];
    int words = 0, index = 0, space = 1;

    printf("Enter a sentence:");
    gets(sentence);

    while (sentence[index] != '\0') {
        if (sentence[index] != ' ' && space) {
            words ++;
            space = 0;
        } else {
            if (sentence[index] == ' ') space = 1;
        }
        index++;
    }

    printf("There are %i words in the sentence", words);

    return 0;
}
