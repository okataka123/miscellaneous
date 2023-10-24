send: send.o UdpClient.o
			g++ -o send send.o UdpClient.o
recv: recv.o UdpClient.o
			g++ -o recv recv.o UdpClient.o
send.o: send.cpp
				g++ -c send.cpp
recv.o: recv.cpp
				g++ -c recv.cpp
UdpClient.o: UdpClient.cpp
				g++ -c UdpClient.cpp
clean:; rm -f *.o send recv

