#include <stdio.h> // printf and scanf
#include <stdlib.h> //malloc

//Prototypes
void StringsTest();
void UsingMalloc();

int main()
{
    StringsTest();
    UsingMalloc();
    return 0;
}

void StringsTest(){
    unsigned char i;
    char Words[2][10];
    unsigned int arrayLength = sizeof(Words)/sizeof(Words[0]);

    printf("Say something I'm giving up on you...\n");

    for(i=0; i<2 ; i++){
        scanf("%s",Words[i]); //string so no address b/ already an address
    }

    printf("you entered %s and %s\n",Words[0],Words[1]); // if gives weird results check your index
    printf("length of the matrix is %d", arrayLength);
}

void UsingMalloc(){

    // First make sure you got the library <stdlib.h>
}
