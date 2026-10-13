## The Application Layer: Network programming

Lecture 8 

## Application Layer Creating Network Applications

<sup>•</sup> So far, we have looked at several network applications and protocols, we will now see how to create network applications. 

<sup>•</sup> Most network applications include a client-side program and a server-side program that communicate through the network. 

• When these two programs are executed, a client process and a server process are created, and these processes communicate with each other by reading from, and writing to, sockets. 

## Application Layer Creating Network Applications

## <sup>•</sup> Choice of protocols:

• Open protocols. Protocols whose rules are public. 

• Proprietary protocols. “Custom” protocols (not been openly published in an RFC or elsewhere). 

## <sup>•</sup> There are two transport protocols that can be used:

• TCP (Transmission Control Protocol), which is connection oriented and provides a reliable byte-stream channel through which data flows between two end systems. 

• UDP (User Datagram Protocol), which is connectionless and sends independent packets of data from one end system to the other, without any guarantees about delivery. 

## Application Layer Creating Network Applications

• Sockets are a central element for the creation of network applications. 

<sup>•</sup> They typically implement (black-box) the transport (UDP/TCP) and the network (IP) layers functionalities. 

<sup>•</sup> Note that there are several applications (middleware) that may wrap sockets simplifying their creation and providing more complex functionalities. 

• However, basic API are still widely used. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/70608032-3061-415a-bdae-165ab85bb5e2/ed003c0a369779e6322e28ec66a5e94a75182dfc4d921c60c6602e0844708a5a.jpg)



Where layers are implemented


## Application Layer Connection-oriented vs. Connectionless

Client 

Server 

Create Socket 

Create Socket 

Connectionless (UDP) 

Connection Oriented (TCP) 

Creation 

Read Message 

Connect 

Send Reply 

Connection 

Create Socket 

Send Message 

Client 

Messaging 

Send Message 

Wait Connections 

Destruction 

Read Message 

Create Socket 

Read Reply 

Read Reply 

Server 

Close Socket 

Close Socket 

Send Reply 

Close Client-specific Socket 

## Application Layer UDP and TCP

<sup>•</sup> UDP and TCP sockets implement the previous procedure to allow connectionless and connection-oriented communication, respectively. 

<sup>•</sup> The basic APIs providing UDP and TCP sockets are typically available in almost all programming languages and operating systems: 

• C, C++, C#, Java, Perl, Python, Matlab, etc. 

<sup>•</sup> The underlying implementation and the usage depends on the configuration of the machines. 

• In Unix domain we use Berkeley sockets (aka BSD or POSIX sockets) for both TCP and UDP connections. These are native C APIs. 

## Application Layer Sockets: Definitions

## <sup>•</sup> Internet-domain sockets in C rely on some structure to define the addresses and ports of the sending/receiving hosts:

```c
#include <netinet/in.h>
#include <arpa/inet.h>    // for inet_addr()
#include <sys/types.h>    // some custom types are defined here

struct sockaddr_in {
    short    sin_family;    // family of the address, typically set to AF_INET (IPv4)
    unsigned short  sin_port;    // port number, e.g. htons(3490)
    struct in_addr  sin_addr;    // see struct in_addr below
    char    sin_zero[8];    // typically zeros, now this structure has same size as sockaddr and can be casted to it
};

struct in_addr {
    unsigned long s_addr; // IP address, can be loaded with inet_addr() or set to INADDR_ANY for localhost
}; 
```

## Application Layer Sockets: Creation

• Sockets are created in C by using the socket() function: 

#include <sys/socket.h> 

int sockfd = socket(int domain, int type, int protocol); 

## Where:

<sup>•</sup> domain: specifies the family as in previous structure (AF_INET). 

<sup>•</sup> type: specifies the type of socket to be created. 

• SOCK_STREAM -> TCP socket 

• SOCK_DGRAM -> UDP socket 

<sup>•</sup> protocol: specifies a particular protocol to be used within the socket. 

<sup>•</sup> This is often 0, so no specific protocol is used. 

<sup>•</sup> sockfd: is the file descriptor that identifies the newly created socket. 

<sup>•</sup> Notice that sockets adhere to the Unix philosophy that “everything is a file” where I/O sources are treated as files (and associated to a file descriptor). 

## Application Layer Sockets: Binding

• We can associate a socket to local address and port by using the bind() function: 

```c
#include <sys/socket.h>
int val = bind(int socket, const struct sockaddr *address, socklen_t address_len); 
```

## Where:

<sup>•</sup> socket: is the file descriptor of the socket we want to bind. 

<sup>•</sup> address: pointer to a sockaddr structure specifying on which port and address to bind. 

• address.sin_addr often set to INADDR_ANY so connections from all addresses are listened (multiple IPs). 

<sup>•</sup> address_len: specifies the length of the sockaddr structure pointed to by the address argument (we can use sizeof() to get it). 

• val: return value which is 0 on success, and -1 otherwise. 

<sup>•</sup> Notice that this function is used on servers as we must bind the socket to a specific port but is optional on clients (the OS assigns a free port automatically). 

## Application Layer Sockets: Send and Receive (UDP)

<sup>•</sup> Processes of sending or receiving messages in UDP are performed by the sendto() and recvfrom() functions: 

#include <sys/socket.h> 

int ob = sendto(int osock, const void *obuf, size_t olen, int oflags, const struct sockaddr *oaddr, socklen_t oaddr_len); 

#include <sys/socket.h> 

int ib = recvfrom(int isock, void *ibuf, size_t ilen, int iflags, struct sockaddr *iaddr, socklen_t *iaddr_len); 

## Where:

<sup>•</sup> osock/isock: are the file descriptors on which to send/receive a message. 

<sup>•</sup> obuf/ibuf: are pointers to the bufers containing a message to send/receive. 

<sup>•</sup> olen/ilen: are lengths of the messages in bytes. 

<sup>•</sup> oflags/iflags: specifies flags (typical values are 0 or MSG_WAITALL to wait until all olen/ilen bytes are sent/received). 

<sup>•</sup> oaddr/iaddr: pointers to sockaddr structures containing the receiving/sending address. 

• oaddr_len/iaddr_len: length in bytes of the sockaddr structure. 

• ob/ib: number of bytes that are actually sent/received. 

## Application Layer Sockets: Closing

• Sockets can be closed by using the close() function: 

#include <unistd.h> 

int val = close(int socket); 

## Where:

<sup>•</sup> socket: is the file descriptor of the socket to close 

• val: return value which is 0 on success, and -1 otherwise. 

## Application Layer UDP Socket Programming (Simple Example C/C++)

## // client-side (includes omited)

int main() { int sockfd; char bufer[1024]; const char *hello = "Hello from client"; struct sockaddr_in servaddr; 

if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) { perror("socket creation failed"); exit(EXIT_FAILURE); 

## memset(&servaddr, 0, sizeof(servaddr));

servaddr.sin_family = AF_INET; servaddr.sin_port = htons(8080); servaddr.sin_addr.s_addr = INADDR_ANY; 

int n; socklen_t len; 

sendto(sockfd, (const char *)hello, strlen(hello), 0, (const struct sockaddr *) &servaddr, sizeof(servaddr)); std::cout<<"Hello message sent."<<std::endl; 

n = recvfrom(sockfd, (char *)bufer, 1024, MSG_WAITALL, (struct sockaddr *) &servaddr, &len); bufer[n] = '\0'; std::cout<<"Received \""<<bufer<<"\""<<std::endl; 

close(sockfd); 

return 0; 

Note: to talk to another computer use inet_addr() instead of INADDR_ANY (e.g., inet_addr(“192.168.1.10”) ) 

UDP Client 

Create UDP Socket 

UDP Server 

Create UDP Socket 

Send Message 

Read Reply 

Read Message 

Send Reply 

Close Socket 

## //server-side (includes omited)

int main() { int sockfd; char bufer[1024]; const char *hello = "Hello from server"; struct sockaddr_in servaddr, cliaddr; 

if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) { perror("socket creation failed"); exit(EXIT_FAILURE); 

memset(&servaddr, 0, sizeof(servaddr)); memset(&cliaddr, 0, sizeof(cliaddr)); 

servaddr.sin_family = AF_INET; servaddr.sin_addr.s_addr = INADDR_ANY; servaddr.sin_port = htons(8080); 

if ( bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0 ) { perror("bind failed"); exit(EXIT_FAILURE); 

socklen_t len = sizeof(cliaddr); int n; 

n = recvfrom(sockfd, (char *)bufer, 1024, MSG_WAITALL, ( struct sockaddr *) &cliaddr, &len); bufer[n] = '\0'; std::cout<<"Received \""<<bufer<<"\""<<std::endl; 

sendto(sockfd, (const char *)hello, strlen(hello), 0, (const struct sockaddr *) &cliaddr, len); std::cout<<"Hello message sent."<<std::endl; 

close(sockfd); return 0; 

## Application Layer From UDP to TCP

• Unlike UDP, in TCP client and server need to handshake before messages can be transmited. 

## • We use two sockets on the server-side:

• A welcoming socket, which is always on, and allows clients to perform handshakes with the server. 

• A client-specific socket, which is created after the handshake, and is used by client and server to communicate. 

<sup>•</sup> The three-way handshake, which takes place within the transport layer, is completely invisible to the client and the server programs. 

<sup>•</sup> Once the connection is accepted by the server (handshake success) the communication moves to the newly created socket. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/70608032-3061-415a-bdae-165ab85bb5e2/344372fc7df20ea8e711bae342216055e5b1309c20805ff0b3343c7c83642291.jpg)


## Application Layer Sockets: Connection (TCP only)

<sup>•</sup> Client-side TCP connection is performed by using the connect() function: 

```c
#include <sys/socket.h>
int val = connect(int socket, const struct sockaddr *address, socklen_t address_len); 
```

## Where:

<sup>•</sup> socket: is the file descriptor of the socket we use to connect. 

<sup>•</sup> address: pointer to a sockaddr structure containing the server address. 

<sup>•</sup> address_len: specifies the length of the sockaddr structure pointed to by the address argument (we can use sizeof() to get it). 

• val: return value which is 0 on success, and -1 otherwise. 

## Application Layer Sockets: Wait-for-connection (TCP only)

<sup>•</sup> Server-side TCP wait-for-connection is performed through two functions: listen() and accept(), which works in combination with the clients connect(). 

• The listen() opens a queue where incoming connections are stored. 

• The accept() opens the client-specific socket. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/70608032-3061-415a-bdae-165ab85bb5e2/eade4b6d9d5510e4a5840318db6682d3b24bb0e5a946ec785a495f30d7faaef9.jpg)


# Application Layer Sockets: Wait-for-connection (TCP only)

## • Server-side TCP wait-for-connection is performed by the listen() and accept() functions:

```c
#include <sys/socket.h>

int val = listen(int socket, int backlog);
int new_sockfd = accept(int socket, struct sockaddr *address, socklen_t *address_len); 
```

## Where:

• socket: is the file descriptor of the socket on which to wait for connections (must be bound to address/port). 

<sup>•</sup> backlog: maximum length of the queue of pending connections. 

<sup>•</sup> address: can be a null pointer, or a pointer to a sockaddr structure where the address of the connecting socket shall be returned. 

<sup>•</sup> address_len: length of the address. 

<sup>•</sup> new_sockfd: new socket descriptor on which the client and the server will communicate. 

• val: return value which is 0 on success, and -1 otherwise. 

```c
#include <sys/socket.h>
int ob = send(int osock, const void *obuf, size_t olen, int flags); 
```

## Application Layer Sockets: Send and Receive (TCP)

<sup>•</sup> Processes of sending or receiving messages in TCP are performed by the send() and read() functions (simpler than UDP ones): 

#include <unistd.h> 

```c
int ib = read(int isock, void *ibuf, size_t ilen); 
```

## Where:

• osock/isock: are the file descriptors on which to send/receive a message. 

<sup>•</sup> obuf/ibuf: are pointers to the bufers containing a message to send/receive. 

<sup>•</sup> olen/ilen: are lengths of the messages in bytes. 

• flags: specifies the type of message transmission (depends on protocol, typically 0). 

• ob/ib: number of bytes that are actually sent/received. 

<sup>•</sup> Notice that we have already specified client and server addresses during the connection phase, we no need to do it here as in sendto/recvfrom. 

## Application Layer TCP Socket Programming (Simple Example C/C++)

## // client-side (includes omited)

int main() { int sockfd, status; char bufer[1024]; const char *hello = "Hello from client"; struct sockaddr_in servaddr; 

if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) { perror("socket creation failed"); exit(EXIT_FAILURE); 

## memset(&servaddr, 0, sizeof(servaddr));

servaddr.sin_family = AF_INET; servaddr.sin_port = htons(8080); servaddr.sin_addr.s_addr = INADDR_ANY; 

if ((status = connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr))) < 0) { printf("\nConnection Failed \n"); return -1; 

send(sockfd, hello, strlen(hello), 0); std::cout<<"Hello message sent."<<std::endl; 

n = read(sockfd, bufer, 1024); std::cout<<"Received \""<<bufer<<"\""<<std::endl; 

close(sockfd); 

return 0; 

TCP Client 

Note: to talk to another computer use inet_addr() instead of INADDR_ANY (e.g., inet_addr(“192.168.1.10”) ) 

Create TCP Socket 

TCP Server 

Create TCP Socket 

Connect 

Send Message 

Read Reply 

Wait Connections 

Read Message 

Send Reply 

Close Socket 

Close Client Socket 

## //server-side (includes omited)

int main() { int sockfd, new_socket; char bufer[1024]; const char *hello = "Hello from server"; struct sockaddr_in servaddr, cliaddr; 

if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0 ) { perror("socket creation failed"); exit(EXIT_FAILURE); } 

memset(&servaddr, 0, sizeof(servaddr)); memset(&cliaddr, 0, sizeof(cliaddr)); 

servaddr.sin_family = AF_INET; servaddr.sin_addr.s_addr = INADDR_ANY; servaddr.sin_port = htons(8080); 

if ( bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)) < 0 ) { perror("bind failed"); exit(EXIT_FAILURE); 

if (listen(sockfd, 3) < 0) { perror("listen"); exit(EXIT_FAILURE); 

if ((new_socket = accept(sockfd, (struct sockaddr*)&cliaddr, (socklen_t*)&addrlen)) < 0) { perror("accept"); exit(EXIT_FAILURE); 

int n = read(new_socket, bufer, 1024); std::cout<<"Received \""<<bufer<<"\""<<std::endl; 

send(new_socket, hello, strlen(hello), 0); std::cout<<"Hello message sent."<<std::endl; 

close(new_socket); close(sockfd); return 0; 