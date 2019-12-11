#include <stdio.h>

int getlowbit(int x, int n){
    return x & (2**n-1);
}

int main(){
    printf("%d", getlowbit(12, 2));
    return 0;
}
