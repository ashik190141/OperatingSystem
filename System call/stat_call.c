#include <fcntl.h> /* Definition of AT_* constants */
#include <sys/stat.h>
#include<stdio.h>
int main(){
    struct stat sfile;
    stat("stat_file.txt", &sfile);
    printf("Stat mode is: %o\n", sfile.st_mode);
}


// dev_t st_dev;         /* ID of device containing file */
// ino_t st_ino;         /* Inode number */
// mode_t st_mode;       /* File type and mode */
// nlink_t st_nlink;     /* Number of hard links */
// uid_t st_uid;         /* User ID of owner */
// gid_t st_gid;         /* Group ID of owner */
// dev_t st_rdev;        /* Device ID (if special file) */
// off_t st_size;        /* Total size, in bytes */
// blksize_t st_blksize; /* Block size for filesystem I/O */
// blkcnt_t st_blocks;   /* Number of 512B blocks allocated */