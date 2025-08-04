#include <stdio.h>
#include <string.h>

void vulnerable(char *input) {
    char buffer[100];
    strcpy(buffer, input); // No bounds checking
    printf("You entered: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    printf("Content-Type: text/plain\n\n");
    vulnerable(getenv("QUERY_STRING")); // Buffer overflow if input > 100 chars
    return 0;
}
hhk
