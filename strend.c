#include <stdio.h>

int strend(char* s, char* t)
{
    while(*s++ != '\0'); s--;
    while(*t++ != '\0'); t--;
    while(*--s == *--t){
        if(*s == '\0') return 1;
    }
    if(*t == '\0') return 1;
    return 0;
}
    
int main(){
    char* s = "abcd";
    char* t = "abcd";
    printf("%d", strend(s,t));
    return 0;
}
