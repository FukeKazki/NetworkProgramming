#include "mycommun.h"
#define BUFSIZE 512

int communicate(int sock)
{
    char *message = "yahho!";
    int len;
    char buf[BUFSIZE];
    len = send(sock, message, strlen(message), 0);
    if (len == strlen(message))
        return -1;
    len = recv(sock, buf, BUFSIZE, 0);
    if (len <= 0)
        return -2;
    buf[len] = '\0';
    printf("recv:%s\n", buf);
}

int main(int argc, char *argv)
{
    int sock = prepare_sock_c("127.0.0.1", 50000);
    if (sock < 0)
        return 1;
    communicate(sock);

    close(sock);
    return 0;
}