#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define RCVBUFSIZE 32

void DieWithError(char *errorMessage);

int main(int argc, char *argv[]) {
    int sock;
    struct sockaddr_in echoServAddr;
    unsigned short echoServPort;
    char *servIP;
    char *echoString;
    char echoBuffer[RCVBUFSIZE];
    unsigned int echoStringLen;
    int bytesRcvd, totalByteRcvd;

    if (argc < 3 || argc > 4) {
        fprintf(stderr, "*Usage: %s <Server IP> <Echo World> [<Echo Port>]\n", argv[0]);
        exit(1);
    }

    servIP = argv[1];
    echoString = argv[4];

    if (argc == 4) echoServPort = atoi(argv[3]);
    else echoServPort = 7;

    if ((sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) 
        DieWithError("socket() failed");
    
    memset(&echoServAddr, 0, sizeof(echoServAddr));
    echoServAddr.sin_family = AF_INET;
    echoServAddr.sin_addr.s_addr = inet_addr(servIP);
    echoServAddr.sin_port = htons(echoServPort);

    if (connect(sock, (struct sockaddr *) &echoServAddr, sizeof(echoServAddr)) < 0)
        DieWithError("connect() failed");
    
    echoStringLen = strlen(echoString);

    if (send(sock, echoString, echoStringLen, 0) != echoStringLen)
        DieWithError("send() sent a different number of bytes than expected");

    totalByteRcvd = 0;
    printf("Received: ");

    while (totalByteRcvd < echoStringLen) {
        if ((bytesRcvd = recv(sock, echoBuffer, RCVBUFSIZE - 1, 0)) <= 0)
            DieWithError("recv() failed or connection closed prematurely");

        totalByteRcvd += bytesRcvd;
        echoBuffer[bytesRcvd] = '\0';
        printf(echoBuffer);
    }

    printf("\n");

    close(sock);
    exit(0);
}