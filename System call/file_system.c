#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
int main()
{
    int fd;
    char buffer[40];
    char msg[18] = "Operating system";
    fd = open("lab.txt", O_RDWR);
    printf("fd=%d\n", fd);
    if(fd!=-1){
        printf("lab.txt open with read and write access\n");
        write(fd, msg, sizeof(msg));
        lseek(fd, 0, SEEK_SET);
        read(fd, buffer, sizeof(msg));
        printf("%s was written in lab.txt file\n", buffer);
        close(fd);
    }
    return 0;
}