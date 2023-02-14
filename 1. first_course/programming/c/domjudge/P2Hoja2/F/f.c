#include <stdio.h>

int main() {
    int c, i, s;
    int id1, id2, punt1 = 0, punt2 = 0;
    scanf("%i", &c);
    
    for (int j = 0; j < c; j++) {
        scanf("%i %i", &i, &s);
        
        if (s > punt1) {
            punt2 = punt1;
            id2 = id1;
            punt1 = s;
            id1 = i;
        } 
        
        else if (punt2 < s < punt1) {
            punt2 = s;
            id2 = i;
        }
    }

    int resultado = punt1 + punt2;
    printf("%i %i %i", id1, id2, resultado);
    return 0;
}