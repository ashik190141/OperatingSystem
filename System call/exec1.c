#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[])
{
    printf("PID of exec1.c = %d\n", getpid());
    char *args[] = {"Operating", "System", NULL};
    execv("./exec2", args);
    return 0;
}