## The Application Layer: The Transport Layer

Lecture 10 

## Transport Layer From Application to Transport

<sup>•</sup> A transport-layer protocol mostly provide logical communication between application processes running on diferent hosts. 

<sup>•</sup> From the application’s perspective, hosts running the processes looks directly connected as if they were on the same machine (even if they are on opposite sides of the planet). 

• The transport layer converts the application-layer messages into one or more transport-layer packets, called segments or datagrams (the later is mainly used for UDP packets): 

<sup>•</sup> If application messages are broken into smaller chunks (segments/datagrams), each chunk is provided with transportlayer header. 

• Segments are passed one by one to the network layer to be transmited. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/04d24ca622758f4a0e48823e6d6c9a95439fa79b05d3c0c0c1e5c5e184a28e68.jpg)


## Transport Layer Responsibilities of Transport Layer

<sup>•</sup> Transport-layer protocols (UDP and TCP) have four main responsibilities: 

1. Process-to-process delivery: messages are delivered independently of where these processes are. 

• Note that this is diferent from host-to-host delivery (i.e., between two diferent machines), which is responsibility of the lower-level IP protocol. 

2. Integrity checking: by including error detection fields into the segments’ headers. 

3. Re<sup>li</sup>ab<sup>l</sup>e data transfer: ensuring that data is delivered from sending process to receiving process, correctly and in order. 

4. Congestion/flow control: it prevents connection from swamping network devices (links or routers) with an excessive amount of trafic. This service is useful to improve performance and is very beneficial to the whole (internet) network. 

<sup>•</sup> In particular, UDP (faster but simpler) provides only the first two services, while TCP provides all the four ones. 

## Transport Layer Process-to-process Delivery

<sup>•</sup> At the application level, several processes can be accessing the network at the same time. 

<sup>•</sup> For example: listening to Spotify music, downloading files, navigating web sites, all together. 

• A process may also be connected to multiple processes at the same time: 

<sup>•</sup> For example: proxy servers, mail servers, etc., all may be connected to multiple remote processes. 

<sup>•</sup> To solve these issues, we use sockets for process-to-process delivery: 

<sup>•</sup> Instead of delivering the message directly to a specific process, we use sockets as endpoints from which processes get the messages. 

<sup>•</sup> This approach somehow decouples the number of processes from the number of connections. 

## Transport Layer Process-to-process Delivery

<sup>•</sup> Since there are multiple sockets in the receiving host, we need: 

• A unique identifier for each socket (port) that must be atached to the received segments. 

• A multiplexing/demultiplexing process on the sender/receiver. 

<sup>•</sup> Demultiplexing: is the process of redirecting a segment to the right socket depending on the associated identifier. 

<sup>•</sup> Multiplexing: is the process of creating segments from diferent processes, assigning to them the right identifier. 

<sup>•</sup> Notice that the problem of redirecting messages to multiple sources is quite common in computer networks, multiplexing and demultiplexing are also present in other layers. 

## Transport Layer

## Ports

• The identifiers of sockets are called source and destination ports (or simply ports): 

• A port is a 16-bit number (port number) ranging from 0 to 65535. 

• The port numbers ranging from 0 to 1023 are ca<sup>ll</sup>ed well-known port numbers and are restricted, which means that they are reserved for use by well-known application protocols. 

• The list of well-known port numbers is updated by IANA (Internet Assigned Numbers Authority), available at htp://www.iana.org. 

• When we develop a new network application, we must assign port numbers to sockets (and therefore to the applications) accordingly. 

<table><tr><td>Port</td><td>Usage</td></tr><tr><td>20</td><td>File Transfer Protocol (FTP) Data Transfer</td></tr><tr><td>21</td><td>File Transfer Protocol (FTP) Command Control</td></tr><tr><td>22</td><td>Secure Shell (SSH)</td></tr><tr><td>23</td><td>Telnet - Remote login service, unencrypted text messages</td></tr><tr><td>25</td><td>Simple Mail Transfer Protocol (SMTP) E-mail Routing</td></tr><tr><td>53</td><td>Domain Name System (DNS) service</td></tr><tr><td>80</td><td>Hypertext Transfer Protocol (HTTP) used in World Wide Web</td></tr><tr><td>110</td><td>Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server</td></tr><tr><td>119</td><td>Network News Transfer Protocol (NNTP)</td></tr><tr><td>123</td><td>Network Time Protocol (NTP)</td></tr><tr><td>143</td><td>Internet Mail Access Protocol (IMAP) Management of Digital Mail</td></tr><tr><td>161</td><td>Simple Network Management Protocol (SNMP)</td></tr><tr><td>443</td><td>HTTP Secure (HTTPS) HTTP over TLS/SSL</td></tr></table>

## Transport Layer

## Ports: Nmap

• To check port usage (and more) on a Linux machines we can use the nmap command. 

• Nmap (Network Mapper) is a network scanning utility basically created to map (discover) hosts and services on a network. 

• It can be used to probe ports of hosts in order to detect open ones (on which an application is listening) and possibly the associated services. 

## • Usage:

• Port-scan of a given target: • $ sudo nmap [target address] 

• Probe port to determine services: • $ sudo nmap –sV [target address] 

• Check first N top used ports: • $ sudo –top-port [N] [target address] 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/d09d636efd314bf4fe213b765e78565df4f87d6373d1486b80b5909ef80952f6.jpg)


Note: state can be open or closed, filtered or unfiltered (which means unable to be scanned). 

## Transport Layer Multiplexing and Demultiplexing

• Assume we have a process in Host A (port 19157) that wants to send a message to a process (port 46428) in Host B. 

## <sup>•</sup> Multiplexing:

<sup>•</sup> The transport layer in Host A creates a segment/datagram that includes the application data, the source port number (19157), the destination port number (46428). 

• The transport layer then passes the resulting segment/datagram to the network layer that encapsulates it in an IP datagram, which will make a best-efort atempt to deliver the segment to the receiving host. 

## <sup>•</sup> Demultiplexing:

<sup>•</sup> If the segment/datagram arrives at the Host B, the transport layer receives and decapsulates it. 

• The transport layer then passes the segment/datagram to the appropriate socket by examining the segment’s destination port number. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/eca28cd5791281b7ac0f394556bde6bbfc114164fde12b010bd2d8db22230b0b.jpg)


## Transport Layer Multiplexing/Demultiplexing in UDP (C/C++)

• In a C UDP client, socket is created as follows: 

sockfd = socket(AF_INET, SOCK_DGRAM, 0); 

<sup>•</sup> The socket is typically not bound to a specific source port, it is the OS that selects a free one (e.g., 46428) but we can always bind it to a specific port. 

<sup>•</sup> Destination port/address is set by passing a suitable sockaddr_in structure to the sendto function: 

```matlab
servaddr.sin_port = htons(19157);
servaddr.sin_addr.s_addr = inet_addr(address_of_B);
...
sendto(sockfd, (const char *)msg, strlen(msg), 0,
(const struct sockaddr *) &destaddr,
sizeof(destaddr); 
```

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/492c9f022a3b3eccec7575dd83fb74123a0e7baef92fbb9749e4e806ff8f67ea.jpg)


## Transport Layer Multiplexing/Demultiplexing in UDP (C/C++)

• In a C UDP server, socket is created and bound as follows: 

```matlab
sockfd = socket(AF_INET, SOCK_DGRAM, 0);
...
servaddr.sin_addr.s_addr = INADDR_ANY;
servaddr.sin_port = htons(19157);
...
bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr)); 
```

• Destination port/address is retrieved through the sockaddr_in structure from the recvfrom function and used in the reply message: 

```c
recvfrom(sockfd, (char *)msg, 1024, 0,
( struct sockaddr *) &cliaddr, &len);
...
sendto(sockfd, (const char *)msg, strlen(msg), 0,
(const struct sockaddr *) &cliaddr, sizeof(cliaddr); 
```

<sup>•</sup> The reply will be sent back whatever the client is. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/fb958f6b453caeb02d6c0827c2727ead6e56e5c51d83e0d0542a830178c4a8ab.jpg)


## Transport Layer Multiplexing/Demultiplexing in UDP

<sup>•</sup> We can say that a UDP socket can be identified by two elements: 

• Destination address (IP). 

<sup>•</sup> Destination port. 

<sup>•</sup> In fact, we can use the same socket to send a return message back to multiple source ports/addresses. 

<sup>•</sup> In the example, the cliaddr structure is filled by the recvfrom function, so we can use it as a destination address for the following sendto function, independently on who the host is. 

## Transport Layer Multiplexing/Demultiplexing in TCP (C/C++)

<sup>•</sup> In TCP communication the server application has a welcoming socket, that waits for connection establishment requests from clients on a specific port number (19157 as before). 

• The TCP client creates a socket and sends a connection establishment request segment to the host specified in the sockaddr_in structure (servaddr in this case): 

sockfd = socket(AF_INET, SOCK_STREAM, 0); 

servaddr.sin_port = htons(19157); 

servaddr.sin_addr.s_addr = inet_addr( address_of_B ); 

connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)); 

• A connection-establishment request is just a TCP segment with a destination port number (19157 here) and a special connectionestablishment bit set in the TCP header (SYN = 1). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/8809d7f5135d1c2a36c81cc3802ec0a33402ca16cc66f7d5462b0962234148cd.jpg)


## Transport Layer Multiplexing/Demultiplexing in TCP (C/C++)

<sup>•</sup> When the server receives the incoming connection-request segment (with destination port 19157), it locates the server process that is waiting to accept a connection. Then a new socket is created: 

new_socket = accept(sockfd, 

(struct sockaddr*)&cliaddr, (socklen_t*)&addrlen) 

• The server-side transport layer fills the structure (cliaddr) by using port numbers and addresses from the incoming segment and creates a new socket (new_socket). 

<sup>•</sup> All future segments having these specific source port, source IP address, destination port, and destination IP address are redirected (demultiplexed) to new_socket. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/635850b4e121ec0564c93a77772f76ea008f5c31f70e222673d0ef174a5bb977.jpg)


## Transport Layer Multiplexing/Demultiplexing in TCP (C/C++)

<sup>•</sup> We can say that a TCP socket can be identified by four elements: 

• Source address (IP). 

<sup>•</sup> Source port. 

• Destination address (IP). 

<sup>•</sup> Destination port. 

• Because of the initial handshake the TCP connection entangles the processes of both sides of the socket. 

<sup>•</sup> Only one source and one destination will use this socket; if the client or the server sides of the communications are interrupted, the socket is closed on both sides (which does not happen in UDP). 

## Transport Layer Multiplexing/Demultiplexing HTTP example

<sup>•</sup> We can then have multiple processes from one machine communicating with multiple processes (or with the same process) on another. 

<sup>•</sup> In this example a host C initiates two HTTP sessions to server B, and host A initiates one HTTP session to B. Hosts A and C and server B each have their own unique IP address (A, C, and B). Host C assigns two diferent source port numbers (26145 and 7532) to its two HTTP connections. 

• Host A may assign a source port of 26145 to its HTTP connection (not aware of C). 

<sup>•</sup> This is not a problem, since the two connections have diferent source IP addresses. 

<sup>•</sup> In this example, the server opens a new process (or a new thread) for each incoming connection by assigning to it the specific socket (new_socket). 

<sup>•</sup> This is quite typical but opening too many processes (or threads) may impair the performance of the server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/deb9bcbba2a3bb33db853830afe96f9ac0b5543c82b0e554d82ff29b7487b656.jpg)


## Transport Layer UDP

<sup>•</sup> As already explained, UDP is useful for simple and rapid connections. It mainly performs 2 tasks: 

<sup>•</sup> Process-to-process delivery (ports, multiplexing and demultiplexing). 

<sup>•</sup> Error Checking. 

<sup>•</sup> UDP is connectionless: t<sup>h</sup>ere <sup>i</sup>s no <sup>h</sup>ands<sup>h</sup>a<sup>ki</sup>ng between sending and receiving transport-layer entities before sending a segment. 

• UDP has no guarantee about delivery of messages (no reliable data transfer implemented) and has no congestion/flow control. 

<sup>•</sup> Roughly speaking, UDP is a minimalistic protocol that just adds <sup>“</sup>the essential” with respect to the lower-level IP protocol. 

## Transport Layer UDP

<sup>•</sup> Why to use UDP instead of TCP? 

<sup>•</sup> Application-level control: UDP is more direct, so the application has more control on the transmission. 

<sup>•</sup> This can be useful for instance in real-time applications, where sending rate or delays are crucial while data loss can be tolerated, so less checking is preferred. 

<sup>•</sup> Fast connection establishment: there is no handshake, so less delay to establish a connection. 

<sup>•</sup> This is good for instance in DNS to not provide additional delays. 

<sup>•</sup> No connection state: there are no congestion-control parameters, no sequence nor acknowledgment numbers. 

<sup>•</sup> A server can typically support many more active clients when the application runs over UDP rather than TCP. 

<sup>•</sup> Minimal packet overhead: The TCP segment adds 20 bytes of header in every segment, whereas UDP only adds 8 bytes. 

## Transport Layer UDP: DNS Example

<sup>•</sup> An example of application using UDP connection is DNS. The DNS client works as follows: 

• In application layer: when the host wants to make a query to a DNS server, it constructs a DNS query message and passes the message to UDP. 

<sup>•</sup> In transport layer: without performing any handshaking with the DNS server, UDP adds header fields to the message and passes the resulting segment to the network layer. 

<sup>•</sup> In network layer: the UDP segment is encapsulated into an IP datagram and sent to the DNS server (through the access layer). 

<sup>•</sup> The client then waits for a reply to its query. If reply is not received (possibly because the underlying network lost the query or the reply), it might try diferent approaches: 

<sup>•</sup> Resending the query. 

<sup>•</sup> Sending the query to another name server. 

<sup>•</sup> Informing the invoking application that a reply is not received. 

## Transport Layer

## UDP: Usage

• Applications needing reliable data transfer such as, e-mail, remote terminal access, the Web, run over TCP (or over reliable UDP-based protocols like QUIC). 

• In this cases we can’t aford packet loss, for instance, mails must be fully delivered we can<sup>’</sup>t have missing elements. 

• SNMP uses UDP to carry out device management. Network management applications must often run when the network is in a stressed state (precisely when reliable data transfer is dificult). 

• Multimedia applications such as Internet phone, video conferencing, streaming, often use both UDP and TCP, because small amount of packet loss can be tolerated. 

• In general, real-time applications react very poorly to TCP congestion control. 

<table><tr><td>Service</td><td>Application Protocol</td><td>Transport Protocol</td></tr><tr><td>E-mails</td><td>SMTP</td><td>TCP</td></tr><tr><td>Remote terminal</td><td>Telnet</td><td>TCP</td></tr><tr><td>Web</td><td>HTTP</td><td>TCP or UDP</td></tr><tr><td>File transfer</td><td>FTP</td><td>TCP</td></tr><tr><td>Name translation</td><td>DNS</td><td>UDP</td></tr><tr><td>Network device management</td><td>SNMP</td><td>UDP</td></tr><tr><td>Multimedia streaming</td><td>Proprietary</td><td>UDP or TCP</td></tr><tr><td>Internet telephony</td><td>Proprietary</td><td>UDP or TCP</td></tr></table>

## Transport Layer

## UDP: Usage

• On the other hand, running multimedia applications over UDP is controvers<sup>i</sup>a<sup>l</sup> because no congestion control is performed. 

• If everyone were to (selfishly) start streaming high-bit-rate video without using any congestion control, network devices would overflow causing more UDP packets to be lost. 

• High loss rates induced by the uncontrolled UDP senders would also cause the TCP senders to dramatically decrease their rates. 

<table><tr><td>Service</td><td>Application Protocol</td><td>Transport Protocol</td></tr><tr><td>E-mails</td><td>SMTP</td><td>TCP</td></tr><tr><td>Remote terminal</td><td>Telnet</td><td>TCP</td></tr><tr><td>Web</td><td>HTTP</td><td>TCP</td></tr><tr><td>File transfer</td><td>FTP</td><td>TCP</td></tr><tr><td>Name translation</td><td>DNS</td><td>UDP</td></tr><tr><td>Network device management</td><td>SNMP</td><td>UDP</td></tr><tr><td>Multimedia streaming</td><td>Proprietary</td><td>UDP or TCP</td></tr><tr><td>Internet telephony</td><td>Proprietary</td><td>UDP or TCP</td></tr></table>

# Transport Layer UDP: Segment Format

• The UDP segment (or datagram to be more precise) is composed by 5 elements: 

• UDP header (64 bits) which includes information related to the UDP protocol and is composed by 4 elements of 16 bits each: 

• Source port: port number of the sending process. 

• Destination port: port number of the receiving process. 

• Lengt<sup>h</sup>: length of the whole datagram (header+data, i.e., N + 64 bits). 

• Checksum: used by the receiver to check if the message is intact. 

• Data (N bits) which is the actual message from the application layer. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/04da3972-dcba-4b7f-b77f-00322e4244f8/6f59d588154c8a7d78a0f59bada1a931462b6180a7ac0b9b3f3203a8cd4417db.jpg)


## Transport Layer

## UDP: Checksum

<sup>•</sup> Integrity checking is performed by using the c<sup>h</sup>ec<sup>k</sup>sum. The UDP checksum is a 16 bits filed used for error detection as follows: 

<sup>•</sup> UDP at the sender side performs the 1s complement of the sum of all the 16-bit words in the datagram, with any overflow bit being summed itself. 

• This result is put in the checksum field of the UDP datagram. 

• When the receiver sums all bits inside the message (checksum included) the sum must be 1111111111111111 (16 ones). 

• If one bit is 0, then we know that errors have been introduced into the packet. 

Example of segment having 3 words 0110011001100000 0101010101010101 1000111100001100 

Sum of the third 16-bit word 

Sum overflow bit 

Sum of first two 16-bit words 

0110011001100000 0101010101010101 1011101110110101 1000111100001100 10100101011000001 0000000000000001 0100101011000010 omplement 

1011010100111101 

Checksum 