#include <stdio.h>

int main() {
    FILE *f = fopen("fichero.txt", "rb");
    
    if (f == NULL) {
        perror("\nError de apertura\n");
        return -1;
    }

    for (int i = 0; i < N; ++i) {
        
    }
    
    return 0;
}
