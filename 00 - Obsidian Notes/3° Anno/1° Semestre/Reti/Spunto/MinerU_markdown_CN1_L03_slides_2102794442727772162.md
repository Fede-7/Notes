## The Application Layer

Lecture 3 

## Application Layer Network Applications

<sup>•</sup> A network application is composed by multiple programs that run on diferent end-systems (hosts or endpoints) and communicate with each other over the network. 

<sup>•</sup> Example: a Web application includes two distinct programs: 

<sup>•</sup> the browser program running in the user’s host (desktop, laptop, tablet, smartphone, and so on). 

• the Web server program running in the Web server host. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/8519b9695af966bd4019edf46e460ed71e8d3a42edfbcf3b44d304cb7560545d.jpg)


## Application Layer Some Network Applications

<sup>•</sup> The applications are the programs that runs on the devices and allow users to access to services. 

<sup>•</sup> social networking 

• Web 

<sup>•</sup> text messaging 

• e-mail 

<sup>•</sup> multi-user network games 

• streaming stored video (YouTube, Netflix) 

<sup>•</sup> P2P file sharing 

<sup>•</sup> voice over IP (e.g., Skype) 

<sup>•</sup> real-time video conferencing 

• Internet search 

<sup>•</sup> remote login 

## Application Layer Creating Network Applications

<sup>•</sup> Creating network applications means to write programs that: 

<sup>•</sup> Run on diferent end systems, perhaps using diferent languages or OS. 

• Communicate over network (e.g., via sockets) by means of a specific protocol. 

• No need to write software for network-core devices 

• Network devices do not run user applications. 

• There are specific libraries (e.g., sockets) implementing network functionalities. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/9e9231a4428e0b0c8056de646f6cbabbcc0bdc6853f846402fb468c669993193.jpg)


## Application Layer Creating Network Applications

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/61af43eb47cffabab73346afa20248934392e6fcb5ca5822bc77812845db93bd.jpg)


## Application Layer Creating Network Applications

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/8e7b67a792f28a9f688c8b7832c37c4d97205ba9c07c532f612c6d18ea764b85.jpg)



<sup></sup> The communication between processes occurs via sockets.



<sup></sup> Applications use the transport layer’s services (reliable data stream)


## Application Layer Network Applications

• A (network) application architecture is designed by the application developer and determines how the application is structured over the various end systems: 

• Client-server: the nodes are heterogeneous, there is an always-on host (server), which provides services to be requests from many other hosts (clients). 

• Peer-to-peer (P2P): the nodes are (ideally) homogeneous, the application exploits direct communication between pairs of intermitently connected hosts (peers). 

Client-server 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/d38e9f7c0ac6086a9fe64d46e45bc8966593f24da515721c096e2395098c6db5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/9af956d200442c5794df30cdcb96858d31f26d24e3d41dfcc36c8f54499a87c5.jpg)



Peer-to-peer


## Application Layer Client-server Applications

• In a client-server architecture, clients do not directly communicate with each other. 

• The server has a fixed, well-known address (hostname or IP address) so a client can always contact the server by sending a packet (request) to it. 

<sup>•</sup> In a client-server architecture multiple servers are often involved to keep up with all the requests from clients. The client is typically unaware of that and perceives them as a single server. 

<sup>•</sup> Multiple servers can be: 

<sup>•</sup> Grouped into data centers containing a huge number of servers in a specific location. 

<sup>•</sup> Servers must be powered, maintained, and well connected. 

• Scatered as distributed servers all around the world. 

• Servers must be interconnected and coordinated. 

<sup>•</sup> Organized in distributed data centers. 

## Application Layer Client-server Applications

## <sup>•</sup> A web application is a typical client-server example:

<sup>•</sup> There is an always-on Web server receiving requests from the browsers on the client hosts. 

• When a Web server receives a request for an object from a client host, it responds by sending the requested object to the client host. 

<sup>•</sup> The web server is reachable by the hosts. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/ff12c5db1b25881dd557d5b3396cb9374ae7cdf007c43956b7f4c012703480ce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/f1c3b03717140a654522a01eedfd47eb3aa2482be0ce5798a09bbcc2403461eb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/c61c8a7de47da04a26390c35577187eb5e7c85f53b1ef1b3e5710706223f7681.jpg)


## Application Layer Peer-to-peer Applications

• It is often used for trafic-intensive applications. 

<sup>•</sup> There is no single server with fixed address 

 <sub>Each</sub> <sub>client</sub> <sub>has</sub> <sub>its</sub> <sub>own</sub> <sub>address</sub> 

<sup>•</sup> Pure P2P applications are rare: most applications have hybrid architectures, combining both client-server and P2P elements. 

<sup>•</sup> For example, for many instant messaging applications, servers are used to track the addresses of users, but user-to-user messages are sent directly between user hosts (without passing through intermediate servers). 

• P2P architectures are scalable and distributed. 

<sup>•</sup> For example, in a P2P file-sharing application, although each peer generates workload by requesting files, each peer also adds service capacity to the system by distributing files to other peers. 

• P2P architectures are also cheap (no need for infrastructures or significant bandwidth) but there are security, performance, and reliability issues. 

## Application Layer Peer-to-peer Applications

<sup>•</sup> Typical P2P applications are internet telephony and video conference or file-sharing (e.g., BitTorrent, Napster): 

• Servers are used to track the IP addresses of users, but user-to-user messages/requests are sent directly between user hosts (without passing through intermediate servers). 

<sup>•</sup> In file-sharing applications the server can also trace all available files in order to speed up the search. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/44edbdfc0fff5734442f7c1fe4e14559b3ee9fc54523e20f823c554e1623181d.jpg)


## Application Layer Communication between Processes

<sup>•</sup> In a network application there are processes running on diferent machines (potentially running on diferent operating systems) that communicate through the network. 

<sup>•</sup> In web applications the process of a client’s browser exchanges messages with the process of the web server. 

<sup>•</sup> In P2P file-sharing a file is transferred from a process in one peer to a process in another peer. 

<sup>•</sup> Between a pair of communicating processes there is typically a client process and a server process: 

<sup>•</sup> In Web applications a browser’s process is a client, while the server’s process is a server. 

<sup>•</sup> In P2P file-sharing the peer that is downloading can be seen as a client, while the peer that is uploading as a server. 

<sup>•</sup> In a P2P application processes may “change role”. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/0f402a48fa69c3c49df2609b7a43bede53ae3e5405c2dcaceaef2e7736cc9ea3.jpg)


## Application Layer Communication between Processes

<sup>•</sup> Most network applications consist of pairs of communicating processes sending/receiving messages to/from each other through the underlying network. 

<sup>•</sup> Following the layered model, a socket is the software interface between application and transport layers and allows processes to send/receive messages over the network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/6b0048ca0074357e0ffddfae0c8198f5da6bef379f0754534a0dddcec6e6df2f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/11a7845d31e1268d401c48342154d425b9d6f085c993d3b308bde16d0c38ff9b.jpg)


Toward hardware (low-level) 

## Application Layer Communication between Processes

## <sup>•</sup> A typical analogy is to consider sockets as mailboxes:

<sup>•</sup> When a process wants to send a message to another process on another host, it puts the message into a mailbox. 

<sup>•</sup> This sending process assumes that there is a transportation infrastructure on the other side of its door that will transport the message to the mailbox of the destination process. 

<sup>•</sup> Once the message arrives at the destination host, the message passes through the receiving process’s mailbox (socket). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/546e18cf8d79ca9a3ef5860ed646d869aaec4e39306b2528a946dbd496474ae5.jpg)


## Application Layer Communication between Processes

• Sockets are used as Application Programming Interface (API) between the application and the network. 

<sup>•</sup> The application developer has control of everything on the application-layer side of the socket but has litle control of the transport-layer side of the socket. 

<sup>•</sup> The only control that the application developer has on the transport-layer side is: 

1. The choice of transport protocol (TCP/UDP). 

2. Perhaps the ability to set a few transport-layer parameters (e.g., maximum bufer, maximum segment size, etc.). 

<sup>•</sup> Once the application developer chooses a transport protocol (if a choice is available), the application is built assuming as given the transport-layer services provided by that protocol. 

## Application Layer Communication between Processes

<sup>•</sup> Following the postal mail analogy, processes need an address to send messages. 

• Since multiple network applications can be running on a single host, to identify the receiving process, two pieces of information needed: 

1. An address of the host (to find the right host on the network). 

2. An identifier of the receiving process (to find the right process in the host). 

• The address works at the network level (routing) while identifier works at transport level. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/f9f29135482e772bb83253cc583eba72358415d6d3778a07eb173ec58ef18ff5.jpg)


## Application Layer Communication between Processes

<sup>•</sup> In the Internet, a host is identified by an IP address (32-bit quantity) while the process is identified by a port number. 

<sup>•</sup> Popular applications have been conventionally assigned to specific port numbers. 

<sup>•</sup> For example, a Web server is identified by port number 80, a mail server process (using the SMTP protocol) is identified by port number 25. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/7919f0fa-2689-4f07-8218-65b6814a6038/525f37bb76d417a261d4d504c757fa02b6f5bf38635b351dcfdadee6cf1a04ba.jpg)


• A list of well-known port numbers (and protocols) can be found here: htps://www.iana.org/assignments/service-names-port-numbers/service-names-port-number s.xhtml 

## Application Layer QoS from Transport-layer

<sup>•</sup> The transport-layer (below the application layer) ofers protocols to implement on demand some proprieties, aka Quality of Service (QoS): 

<sup>•</sup> Reliability of data transfer: data sent by one end of the application is delivered correctly and completely to the other end. 

<sup>•</sup> Throughput: the rate at which the sending process can deliver bits to the receiving process (bit/sec). 

<sup>•</sup> Timing: every bit that the sender pumps into the socket arrives at the receiver’s socket within a time range. 

<sup>•</sup> Security: encryption and decryption of the messages. 

<sup>•</sup> Theoretically, security is a transport-layer issue but secure protocols (e.g., TLS - Transport-Layer Security) are often built upon TCP, so it is application-layer in practice. 

• TCP (Transmission Control Protocol): includes a handshake between processes service and a reliable data transfer service (aka connection-oriented). 

• UDP (User Datagram Protocol): is lightweight with minimal services, there is no handshake, no guarantee that messages are received (aka connectionless). 

## Application Layer Application Protocols

• An application-layer protocol defines how network application’s processes, running on diferent end systems, pass messages to each other. 

<sup>•</sup> How are messages structured? What are the meanings of the various fields in the messages? When do the processes send the messages? 

## <sup>•</sup> Specifically, application-layer protocols define:

1. The types of messages exchanged (for example request messages and response messages). 

2. The syntax of the various message types, such as the fields in the message and how the fields are delineated. 

3. The semantics of the fields, i.e., the meaning of the information in the fields. 

4. The rules for determining when and how a process sends messages and responds to messages. 

## Application Layer Some Application Protocols

<sup>•</sup> There are several application-layer protocols that are commonly used on networks (and internet), here some example. 

<table><tr><td>Application</td><td>Description</td></tr><tr><td>DHCP</td><td>Dynamic Host Configuration Protocol, assigns IP addresses</td></tr><tr><td>DNS</td><td>Domain Name System, translate website names to IP addresses</td></tr><tr><td>HTTP/HTTPS</td><td>HyperText Transfer Protocol (Secure), transfer web pages</td></tr><tr><td>SMTP/SMTPS</td><td>Simple Mail Transfer Protocol (Secure), sends email messages</td></tr><tr><td>SNMP</td><td>Simple Network Management Protocol, manages network devices</td></tr><tr><td>Telnet/SSH</td><td>Teletype Network (Secure SHEll), allows command-line interfacing with remote hosts</td></tr><tr><td>FTP/FTPS</td><td>File Transfer Protocol (Secure), used to transfer files</td></tr></table>

## Application Layer Some Application Protocols

• Some application may exchange sensitive information (e.g., user’s credentials, personal data, etc.). 

• On public networks, messages should be secured. 

<table><tr><td>Application</td><td>Description</td></tr><tr><td>DHCP</td><td>Dynamic Host Configuration Protocol, assigns IP addresses</td></tr><tr><td>DNS</td><td>Domain Name System, translate website names to IP addresses</td></tr><tr><td>HTTP/HTTPS</td><td>HyperText Transfer Protocol (Secure), transfer web pages</td></tr><tr><td>SMTP/SMTPS</td><td>Simple Mail Transfer Protocol (Secure), sends email messages</td></tr><tr><td>SNMP</td><td>Simple Network Management Protocol, manages network devices</td></tr><tr><td>Telnet/SSH</td><td>Teletype Network (Secure SHEll), allows command-line interfacing with remote hosts</td></tr><tr><td>FTP/FTPS</td><td>File Transfer Protocol (Secure), used to transfer files</td></tr></table>

## Application Layer FTP and FTPS

• FTP (File Transfer Protocol) is one of the oldest protocols defined in Internet (first version in 1971) and is used to transfer files between hosts over network. 

• In the basic version of FTP data transfer is in clear-text (username, password, and files) so it is best used in local or private applications. 

• The secure version FTPS (FTP Secure) protects username and password and encrypt contents. 

• Both FTP and FTPS have two components: 

• The protocol that specifies commands (show, get, delete files, etc.). 

• A software application implementing the protocol (client-side and a server-side software). 

## Application Layer FTP Example

<sup>•</sup> In Linux we can use ftp and vsftpd (very secure FTP daemon) as client and server applications respectively. 

• On the server machine: 

<sup>•</sup> Install vsftpd: 

• $ sudo apt-get install vsftpd 

<sup>•</sup> Check ftp server running 

• $ service vsftpd status (check if daemon is running) 

## • On the client machine:

<sup>•</sup> Install ftp: 

• $ sudo apt-get install ftp (it is already available in Ubuntu) 

• Connect to server: 

• $ ftp ADDRESS (usr and pass will be asked) 

• Close connection: 

• $ exit 

Note: The server side of this application is implemented as a daemon: a program that runs in background and waits for clients to connects. This is a common approach. 

## Application Layer FTP Common Commands

Common FTP commands: 

help - List all available FTP commands. 

cd - Change directory on remote machine. 

lcd - Change directory on local machine. 

ls - View the names of the files and directories in the current remote directory. 

mkdir - Create a new directory within the remote directory. 

pwd - Print the current working directory on the remote machine. 

delete - Delete a file in the current remote directory. 

rmdir- Remove a directory in the current remote directory. 

get - Copies a file from the remote server to the local machine. 

put - Copies a file from the local machine to the remote machine. 