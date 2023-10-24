#include <iostream>
#include "UdpClient.h"

int main(void) {
  UdpClient udp0("127.0.0.1", 4001);
  for(;;) {
    std::string s;
    std::cin >> s;
    udp0.send(s);
  }
  return 0;
}
