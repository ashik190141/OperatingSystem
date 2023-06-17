#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
int main()
{
    gid_t pid = getpid();
    printf("Current Process Id: %d\n", pid);
    gid_t child_process = fork();
    if(child_process==-1){
        printf("Failed to create child process\n");
    }else if(child_process==0){
        printf("Child Process is: %d\n", getpid());
        printf("Parent Process is: %d\n", getppid());
    }else{
        printf("Parent Process is: %d\n", getpid());
        printf("Child Process is: %d\n", pid);
    }
}