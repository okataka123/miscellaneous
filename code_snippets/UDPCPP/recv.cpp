#include <iostream>
#include <string>
#include "UdpClient.h"

int main(void) {
  UdpClient udp0("0.0.0.0", 4001);
  udp0.bind();
  while (1) {
    std::string rdata = udp0.recv();
    std::cout << "recv : " << rdata.c_str() << std::endl;
  }
  return 0;
}
