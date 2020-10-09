#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>

#define BUFSIZE 512

int prepare_sock_c(char *host, int port) {
    int sock = socket(PF_INET, SOCK_STREAM, 0);
    if (sock < 0) return -1;
    struct sockaddr_in target;
    target.sin_family = AF_INET;
    target.sin_addr.s_addr = inet_addr(host);
    target.sin_port = htons(port);
    int connected = connect(sock, (struct sockaddr *)&target, sizeof(target));
    if (connected < 0) return -2;
    return sock;
}

void communicate(int sock) {
    char *message = "yahho!";
    int len;
    char buf[BUFSIZE];
    len = send(sock, message, strlen(message), 0);
    if (len == strlen(message)) return -1;
    len = recv(sock, buf, BUFSIZE, 0);
    if (len <= 0) return -2;
    buf[len] = '\0';
    printf("recv:%s\n", buf);
}

int main(int argc, char *argv) {
    int sock = prepare_sock_c("10.13.64.100", 50000);
    if (sock < 0) return 1;
    communicate(sock);

    close(sock);
    return 0;
}