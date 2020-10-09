#include "mycommun.h"

#define BUFSIZE 512

int communicate(int sock)
{
    int len;
    char buf[BUFSIZE];
    len = recv(sock, buf, BUFSIZE, 0);
    if (len <= 0)
        return -2;
    buf[len] = '\0';
    len = send(sock, buf, strlen(buf), 0);
    if (len < strlen(buf))
        return -1;
    return 0;
}

int main(int argc, char **argv)
{
    int sock = prepare_sock_s(50000);
    if (sock < 0)
        return 1;
    listen(sock, 5);

    while (1)
    {
        struct sockaddr_in cinfo;
        unsigned int len_cinfo = sizeof(cinfo);
        int sock_c = accept(sock, (struct sockaddr *)&cinfo, &len_cinfo);
        communicate(sock_c);
        close(sock_c);
    }
    close(sock);
    return 0;
}