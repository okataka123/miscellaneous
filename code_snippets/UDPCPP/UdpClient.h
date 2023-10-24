#ifndef UDPCLIENT_H
#define UDPCLIENT_H

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstring>
#include <string>

class UdpClient {
  int sock_;
  struct sockaddr_in addr_;

public:
  UdpClient(std::string address, int port);
  void send(std::string word);
  void bind(void);
  std::string recv(void);
  void recv(char * buf, int size);
  ~UdpClient() {
    close(sock_);
  }
};

#endif //UDPCLIENT_H
