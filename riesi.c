/* gcc -std=c89 riesi.c -o riesi_c -pedantic -Wall -Wextra -Werror */
#include <stdio.h> /* getchar */
#include <ctype.h> /* tolower */

int main(void)
{
    int  riesi = 0;
    char input;

    printf("Riesi: False\n");
    printf("Riesi?");

    input = getchar();
    input = tolower(input);
    
    riesi = (input == 'y');

    if (riesi == 0)
        printf("Riesi: False\n");
    else
        printf("Riesi: True\n");

    return 0;
}

