#include <stdio.h>

int main() {
    int t;
    int g;
    double s;
    scanf("%i", &t);
    scanf("%i", &g);
    scanf("%lf", &s);
    if ((t > 5) || ((g > 1500) && (s > 1.2)) || ((t > 5) && ((g > 1500) && (s > 1.2)))) {
        printf("1");
    } else {
        printf("0");
    }
    return 0;
}