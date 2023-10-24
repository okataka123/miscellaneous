#include "UdpClient.h"

UdpClient::UdpClient(std::string address, int port) {
  sock_ = socket(AF_INET, SOCK_DGRAM, 0);
  addr_.sin_family = AF_INET;
  addr_.sin_addr.s_addr = inet_addr(address.c_str());
  addr_.sin_port = htons(port);
}

void UdpClient::send(std::string word) {
  sendto(sock_, word.c_str(), word.length(), 0, (struct sockaddr *)&addr_, sizeof(addr_));
}

void UdpClient::bind(void) {
  ::bind(sock_, (const struct sockaddr *)&addr_, sizeof(addr_));
}

std::string UdpClient::recv(void) {
  const int  BUFFER_MAX = 400;
  char buf[BUFFER_MAX];
  memset(buf, 0, sizeof(buf));
  ::recv(sock_, buf, sizeof(buf), 0);
  return std::string(buf);
}

void UdpClient::recv(char * buf, int size) {
  memset(buf, 0, size);
  ::recv(sock_, buf, size, 0);
}

