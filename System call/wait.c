#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include<sys/wait.h>
int main()
{
    gid_t q;
    printf("Before Fork\n");
    q = fork();
    printf("Fork value is %d\n", q);
    if (q == 0) // child
    {
        printf("I am child having ID %d\n", getpid());
        printf("My parent's id is %d\n", getppid());
    }
    else
    {//parent
        wait(NULL);
        printf("My child's id is %d\n", q);
        printf("I am parent having ID %d\n", getpid());
    }
}