#include <stdio.h>

void reverse(char s[]){
    static int i = 0; static int n = 0; 
    int ntmp = n;
    char c = s[n++];
    if(c!='\0'){
        reverse(s);
        s[i++] = c;
    }
    if(ntmp == 0){
        i = 0; n = 0;
    }
}

int main(){
    char s[1024] = "abcd";
    char t[1024] = "fghj";
    reverse(s);
    reverse(t);
    printf("%s\n", s);
    printf("%s", t);
    return 0;
}
