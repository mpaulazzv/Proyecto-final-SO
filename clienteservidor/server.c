#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

int main()
{
    int server_fd, new_socket, val_read;
    struct sockaddr_in address;
    char buffer[1024] = {0};

    server_fd = socket(AF_INET, SOCK_STREAM, 0);

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(5000);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 1);

    new_socket = accept(server_fd, (struct sockaddr *)NULL, NULL);

    while (1)
    {
        val_read = read(new_socket, buffer, 1024);
        printf("%s\n", buffer);
    }

    return 0;
}