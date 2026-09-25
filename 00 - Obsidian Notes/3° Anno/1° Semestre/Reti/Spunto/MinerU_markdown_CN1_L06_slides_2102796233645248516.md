## The Application Layer: More on HTTP

Lecture 6 

## Application Layer Mails and SMTP

• Electronic mailing (e-mail) is one of the oldest and most important internet applications. 

<sup>•</sup> Mailing is typically implemented in a client-server fashion, having 2 types of hosts: 

<sup>•</sup> User agent: application allowing mail management (e.g., Pine, K-9 Mail etc.). 

• Mail Server: a server that stores mails and maintain userspecific mailboxes. 

<sup>•</sup> Diferently from HTTP, here communication also occurs between servers. We need 2 applications/protocols: 

• One between user agent and mail server. 

• One between mail server and mail server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/fecffe90-f748-4b68-8a9d-ae87432501c6/bb3ac61f8748e4fcba8c59c4171807d18223f6310339d247a87000e701ca4e84.jpg)


## Application Layer Mails and SMTP

• Users do not exchange mails directly (as in instant messaging). It is preferred to use the more reliable and specialized mail servers. 

• The Simple Mail Transfer Protocol (SMTP) is the main application-layer protocol working between mail servers. 

<sup>•</sup> It allows servers to exchange mails, user agents do not use SMTP. 

Once a new mail arrives on the server, it is stored inside the user-specific mailboxes, waiting to be download locally by the user agent. 

• In SMTP there are a client-side (sender) and a serverside (receiver) that run on mail servers, both using the reliable TCP to transfer mail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/fecffe90-f748-4b68-8a9d-ae87432501c6/1467bdc5b21a0ece4b59a24590bec874e9c6c9e3df63b7a45f1bce41f41cdd11.jpg)


## Application Layer SMTP

• Let’s assume to have host A (Alice) that is sending an e-mail to host B (Bob), we have 4 elements involved: 

<sup>•</sup> Alice’s agent. 

• Alice’s mail server. 

<sup>•</sup> Bob’s agent. 

• Bob’s mail server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/fecffe90-f748-4b68-8a9d-ae87432501c6/cff213030e715ea581b952c141dca7c53801d2feaf52395e158a266cb824f5c2.jpg)


## <sup>•</sup> The process works as follows:

1. Alice invokes her user agent for e-mail, provides Bob’s e-mail address (e.g., bob@someschool.edu), composes a message, and instructs the user agent to send the message. 

2. Alice’s user agent sends the message to her mail server, where it is placed in a message queue. 

3. The client side of SMTP, running on Alice’s mail server, sees the message in the message queue. It opens a TCP connection to an SMTP server, running on Bob’s mail server. 

4. After some initial SMTP handshaking, the SMTP client sends Alice’s message into the TCP connection. 

5. At Bob’s mail server, the server side of SMTP receives the message. Bob’s mail server then places the message in Bob<sup>’</sup>s mailbox. 

6. Bob invokes his user agent to read the message at his convenience. 

## Application Layer SMTP

• First, the client SMTP (running on the sending mail server host) establishes a TCP a connection to port 25 at the server SMTP (running on the receiving mail server host). 

<sup>•</sup> If the server is down, the client tries again later. Once this connection is established, the server and client perform some application-layer handshaking: SMTP clients and servers introduce themselves before transferring information. 

<sup>•</sup> During this SMTP handshaking phase, the SMTP client indicates the e-mail address of the sender (the person who generated the message) and the e-mail address of the receiver. 

<sup>•</sup> SMTP can count on the reliable data transfer service of TCP to get the message to the server without errors. 

## Application Layer Accessing mails

<sup>•</sup> Deployment of SMTP servers is more reliable with respect to direct user-touser mailing: 

<sup>•</sup> Servers are, by definition, always on and visible to all devices of the network. 

• Servers are certified. 

<sup>•</sup> The server may continuously try to re-send mails if delivery fails (which is a quite computationally expansive process). 

• On the other hand, to access the mails from the server an additional clientserver application is needed (and a diferent protocol), most popular are: 

• Post Ofice Protocol—Version 3 (POP3). 

• Internet Mail Access Protocol (IMAP). 

• HTTP. 

## Application Layer Accessing mails: POP3

• The Post Ofice Protocol - Version 3 (POP3) is an extremely simple mail access protocol. 

• The user agent (the client) opens a TCP connection to the mail server (the server) on port 110. 

<sup>•</sup> With the TCP connection established, POP3 progresses through three phases: 

1. Authorization: the user agent sends a username and a password to authenticate the user. 

2. Transaction: the user agent can retrieve messages, mark messages for deletion, remove deletion marks, and obtain mail statistics. 

3. Update: after the client has issued the quit command, ending the POP3 session, the mail server deletes the messages that were marked for deletion. 

## Application Layer Accessing mails: IMAP

<sup>•</sup> With POP3 access, messages can just be downloaded or deleted. Action like searching or organizing mails into folders are not considered (these must be done on the local machine). 

## • The Internet Mail Access Protocol (IMAP) allow servers to provide additional features:

<sup>•</sup> Managing and creating folders. 

<sup>•</sup> Perform search into remote folders for messages matching specific criteria. 

<sup>•</sup> Allow user agent to obtain just parts of messages (e.g., header only, atachments only, etc.). 

• Allow multiple clients to be connected to the same server. 

## Application Layer Accessing mails: HTTP

<sup>•</sup> More and more users today are sending and accessing their e-mails through their Web browsers. 

<sup>•</sup> HTTP Web-based access was introduced by Hotmail in the mid 1990 an is now the mainstream approach (Google, Yahoo!, Virgilio, etc.) and it is used by almost every major university and corporation (UniNA included). 

<sup>•</sup> With this service, the user agent is an ordinary Web browser, and the user communicates with its remote mailbox via HTTP rather than through the POP3 or IMAP protocols. 

<sup>•</sup> This works for user-agents, while mail servers still rely on the standard SMTP to exchange messages. 

## Application Layer Peer-to-Peer

• Diferently from client-server, P2P architecture makes minimal (if none) use of servers, here we have pairs of intermitently connected hosts (peers) that communicate directly with each other. 

<sup>•</sup> The peers are not owned by a service provider but are instead desktops and laptops controlled by users. 

<sup>•</sup> One natural application of P2P is file sharing: 

• In a client-server architecture, the server must share files to all clients (which is a serious burden on the server and requires large bandwidth). 

<sup>•</sup> In a P2P architecture, the peers that receive the file may also share it to other peers. Somehow, peers are clients and servers at the same time. 

## Application Layer Peer-to-Peer

<sup>•</sup> In file sharing, the P2P approach typically scales beter than client-server one. 

• On the other hand, P2P approaches can be quite complex to implement. 

<sup>•</sup> There may also be security issues in having all this clients in direct communication. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/fecffe90-f748-4b68-8a9d-ae87432501c6/323c6f59494d841dde9a2f130119f53da2af37ea01c719b63898ec42dccdf180.jpg)


## Application Layer BitTorrent

<sup>•</sup> A popular P2P protocol for file sharing/distribution is BitTorrent. • BitTorrent estimated users are 150-170 million (in 2023). 

<sup>•</sup> A torrent is the collection of all peers participating in the distribution of a particular file. Peers in a torrent download equal-size chunks of the file from one another (typical chunk size is 256 kbytes). 

• When a peer joins a torrent (having no chunks): 

<sup>•</sup> It starts by accumulating chunks. 

<sup>•</sup> While the peer downloads chunks it also uploads chunks to other peers. 

• Once the peer acquires the entire file, it may (selfishly) leave the torrent, or (altruistically) stay in the torrent and continue to upload chunks to other peers. 

<sup>•</sup> Peers may leave the torrent at any time with only a subset of chunks, and later rejoin the torrent. 

## Application Layer BitTorrent: tracker

<sup>•</sup> Each torrent has an infrastructure node called tracker that takes track of the peers participating to the torrent (trackers are basically servers). 

• When a new peer joins a torrent: 

• It registers itself with the tracker and periodically informs the tracker about its status. 

<sup>•</sup> The tracker provides the IP addresses of a randomly selected subset of peers from the torrent. 

<sup>•</sup> Having the list of peers, the new host atempts to establish concurrent TCP connections with all the peers on this list (neighbors). 

<sup>•</sup> During the execution, some of the connected peers may leave while other peers (outside the initial list) may atempt to establish new connections. 

<sup>•</sup> At any given time, each peer will have a subset of chunks from the file, with diferent peers having diferent subsets. Periodically, a host will ask each connected peers (over the TCP connections) for the list of the chunks they have. 

## Application Layer BitTorrent: client

• The downloading client decides which chunks to request (and to whom) following a rarest-first principle: 

<sup>•</sup> Rarest-first: the chunks with fewest repeated copies among the neighbors are prioritized. In this way, the rarest chunks get more quickly redistributed, so to (roughly) equalize the numbers of copies in the torrent. 

## <sup>•</sup> The uploading client decides which requests are served following two intertwined principles:

<sup>•</sup> Trading: hosts give priority to the best 4 neighbors that are currently supplying data at the highest rate. This check is periodically performed (10 seconds) and the list of 4-best neighbors is updated. 

<sup>•</sup> Random selection: every 30 seconds, a host also picks one additional neighbor at random and sends it chunks. If this random exchange is good (the 2 hosts are good partners) they will enter the respective best lists. This process also allows peers with compatible upload rates to find each other. 