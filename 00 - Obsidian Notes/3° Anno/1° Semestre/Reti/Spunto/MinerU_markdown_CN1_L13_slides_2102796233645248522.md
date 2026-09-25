## The Transport Layer: TCP

Lecture 13 

## Transport Layer [Remind] Responsibilities of Transport Layer

• Transport-layer protocols (UDP and TCP) have four main responsibilities: 

1. Process-to-process delivery: messages are delivered independently of where these processes are. 

• Note that this is diferent from host-to-host delivery (i.e., between two diferent machines), which is responsibility of the lower-level IP protocol. 

2. Integrity checking: by including error detection fields into the segments’ headers. 

3. Reliable data transfer: ensuring that data is delivered from sending process to receiving process, correctly and in order. 

4. Congestion/flow control: it prevents connection from swamping network devices (links or routers) with an excessive amount of trafic. This service is useful to improve performance and is very beneficial to the whole (internet) network. 

• In particular, UDP (faster but simpler) provides only the first two services, while TCP provides all the four ones. 

## Transport Layer [Recall] TCP Segment

• The TCP segment consists of header fields and a data field, the later contains some application data of at most MSS size. 

• The header contains several fields: 

• Sequence number (32-bit) for reliable data transfer. 

• Acknowledgment number (32-bit) for reliable data transfer. 

• Receive window (16-bit) used to indicate the number of bytes that a receiver is willing to accept (for flow control). 

• Header length (4-bit) specifies the number of 32-bit words contained into the header. Note that TCP header is variable due to the options field. 

• Options field (K-bit) used for optional processes such as negotiating the MSS, time-stamping, etc. 

• Flags (6/12-bit) including: 

• ACK bit indicates that this segment is an ACK packet (so the acknowledgment number field is in use). 

• RST, SYN, and FIN bits used for connection setup and teardown. 

• CWR and ECE bits used in explicit congestion notification (optional). 

• PSH bit tells the receiver to pass the data to the application immediately. 

• URG bit indicates that the segment contains “urgent” data. 

• Checksum (16-bit): for integrity check. 

• Urgent data pointer field (16-bit) indicates the location of the last byte of the urgent part of the data. 

<table><tr><td colspan="9">32 bits</td></tr><tr><td colspan="7">Source port #</td><td colspan="2">Dest port #</td></tr><tr><td colspan="9">Sequence number</td></tr><tr><td colspan="9">Acknowledgment number</td></tr><tr><td>Header length</td><td>Unused</td><td>CWR</td><td>ECE</td><td>URG</td><td>ACK</td><td>PSH</td><td>RST</td><td>SYN FIN</td></tr><tr><td colspan="8">Internet checksum</td><td>Receive window</td></tr><tr><td colspan="9">Options</td></tr><tr><td colspan="9">Data</td></tr></table>

## Transport Layer TCP Problems in Connection Management

• Since TCP is connection-oriented two hosts must agree during both the opening and the closing procedures. 

• Knowing that messages could be lost or damaged on the network, it is quite dificult for two hosts to find such agreement. 

• If messages are lost during transmission one end of the communication can be open or closed while the other is not. 

• To avoid (or beter to mitigate) this issue TCP implements a procedure called three-way handshake in which open/close connection requests have to be acknowledged by hosts before a connection can be established/released. 

## Transport Layer TCP Problems in Connection Management

## • The two-army problem:

• Imagine a white army encamped in a valley and, on both hillsides, there are 2 enemy blue armies. 

• The white army is larger than either of the blue armies alone, but together the blue armies are larger, they will be victorious only if the atack is simultaneous. 

• To synchronize their atacks, blue armies must send messengers through the valley where they might be captured (unreliable communication). 

• Does a protocol exist that allows the blue armies to win? 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/5a92e7adf3ab61e7a636b295cf4ffa4fb78156f3f989a5773026340d0a9f5ab6.jpg)


## Transport Layer TCP Problems in Connection Management

• Suppose that the commander of blue army #1 sends a message reading: ‘‘I propose we atack today, is it ok?’’ 

• Now suppose that the message arrives, the commander of blue army #2 agrees, and his reply gets safely back to blue army #1. 

• Will the atack happen? Probably not, because commander #2 does not know if his reply got through. If it did not, blue army #1 will not atack. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/6f8643fdc9fc26f52b823aaecf65e72ba0b862f35795dae92b93957457392bd1.jpg)


## Transport Layer TCP Problems in Connection Management

• Let’s make it a three-way handshake: the first commander (of the original proposal) must acknowledge the response. 

• Assuming no messages are lost, blue army #2 will get the acknowledgement, but the commander of blue army #1 will now hesitate (he does not know if his acknowledgement got through). 

• Now we could make it a four-way handshake, but that does not help either. In fact, it can be proven that no protocol exists that works. 

• Three-way handshake is not perfect, but it is usually adequate! 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/92420220025051386d58d6f084ab4f331cf84ab0075e69fe0967da29a7e645da.jpg)


## Transport Layer TCP Connection Establishment

• In TCP three-way handshake is performed to establish connection: 

• Client sends a connection request (SYN segment) to the server. 

• Server responds with a special acknowledgment (SYN-ACK segment). 

• Client sends back a final acknowledgment (ACK segment). 

## • TCP connection establishment is a delicate procedure that can also add significantly delays.

• There is typically a timeout (30-60 secs) to complete the handshake, after that the procedure is aborted. 

• Some atacks (e.g., SYN flood) happen here. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/4e71206f218d4dd8ed5d655413f7a5d8e669552a53ee8421200a978592e72055.jpg)


## Transport Layer TCP Connection Establishment

## • Details of the three-way handshake procedure:

1. The client sends a SYN segment having: 

• No application-layer data (payload). 

• The SYN bit set to 1. 

• A random initial sequence number (client_isn) as sequence number. 

2. When the above SYN segment (hopefully) arrives, the server allocates TCP bufers and variables and sends back a SYNACK segment having: 

• No application-layer data (payload). 

• The SYN and ACK bits set to 1. 

• The acknowledgment number set to client_isn+1. 

• A random initial sequence number (server_isn) as sequence number. 

3. When the SYNACK segment (hopefully) arrives, the client also allocates bufers and variables to the connection and sends to the server a final ACK segment having: 

• Possibly application-layer data. 

• The SYN bit set to 0 (connection is established) and ACK bit set to 1. 

• The acknowledgment number set to server_isn+1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/b328b05dbc26652a8280ab57cac06b7f27ae96e534296bfeadf3273fdb29cb84.jpg)


## Transport Layer TCP Connection Establishment

• Simplified state diagram for TCP connection establishment. 

Passive Open 

listen() invoked 

Closed 

Active Open 

Listen 

SYN received Send SYN+ACK 

SYN Received 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/b7bc4a35ff8d95be894939d390ff0772d1d75a39634828adcfc47f74dfce4cc6.jpg)


ACK received connect() invoked Send SYN 

SYN+ACK received Send ACK 

SYN Sent 

Established 

## Transport Layer TCP Connection Release

• TCP connection release (aka teardown) can be performed by either host. 

• Let’s assume client is closing the connection, the three-way handshake is performed as follow: 

1. The client sends a special shutdown segment (FIN segment) to the server having the FIN bit set to 1. 

2. When the server receives this segment, it sends back an acknowledgment/shutdown segment, having ACK to 1 and FIN bit set to 1. 

• Note: ACK and FIN can be sent in the same segment or in two separated ones. 

3. Finally, the client acknowledges the server’s shutdown segment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/219e6c3204f48cc8f5c7d436c271ac718eae42e6f4eb8b55645d7c6209012544.jpg)


## Transport Layer TCP Connection Release

• Simplified state diagram for TCP connection release. 

First to Close close() invoked Send FIN 

FIN-wait-1 

ACK received 

FIN-wait-2 

FIN received Send ACK 

FIN received Send ACK 

Established 

Closing 

ACK received 

FIN received Send ACK 

ACK received 

Close Wait 

Second to Close 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/c18c92de249f2f776901df8e0b43e9f3a5598b9d2e9640291d8c17fe824ba553.jpg)


close() invoked Send FIN 

Closed 

Last ACK 

Time Wait 

Timeout Elapsed 

## Transport Layer TCP Connection Release

• How do we save ourselves from packet loss? 

• Since three-way handshake is not perfect, TCP rely on timers to eventually close connections or to send again requests. Here some examples during connection release: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/69bffe71734618a13650e2f3b7dc4be411d145f5d50fa5278dfa4f48510f3e0d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/178d646a5f5907b73ce0683f3208f941c393f6d975be813166941f991309ae99.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/0c0477a8-95bb-4d30-9fc7-31323d44383d/014d3c0ab3928ead7ef3b62f444e5769f61ab675188b63a7fe873e6edc7106df.jpg)
