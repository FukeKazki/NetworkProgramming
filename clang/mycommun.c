#include "mycommun.h"

int prepare_sock_s(int port)
{
    int sock = socket(PF_INET, SOCK_STREAM, 0);
    if (sock < 0)
        return -1;
    struct sockaddr_in selfinfo;
    selfinfo.sin_family = AF_INET;
    selfinfo.sin_addr.s_addr = htonl(INADDR_ANY);
    selfinfo.sin_port = htons(port);
    int is_bound = bind(sock, (struct sockaddr *)&selfinfo, sizeof(selfinfo));
    if (is_bound < 0)
        return -2;
    return sock;
}

int prepare_sock_c(char *host, int port)
{
    int sock = socket(PF_INET, SOCK_STREAM, 0);
    if (sock < 0)
        return -1;
    struct sockaddr_in target;
    target.sin_family = AF_INET;
    target.sin_addr.s_addr = inet_addr(host);
    target.sin_port = htons(port);
    int connected = connect(sock, (struct sockaddr *)&target, sizeof(target));
    if (connected < 0)
        return -2;
    return sock;
}
