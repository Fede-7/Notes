## The Transport Layer: TCP

Lecture 12 

## Transport Layer

## <sup>•</sup> TCP with respect to UDP is:

<sup>•</sup> Connection-oriented: there is a “handshake” phase before the transmission that ensures the two processes (sender and receiver) to be “connected”. 

<sup>•</sup> Reliable: error detection, retransmissions, acknowledgments, timers, sequence numbers are implemented. 

<sup>•</sup> Congestion and flow aware: there is a regulation of the transmission rate depending on the receiver performance (flow) and the network performance (congestion). 

## <sup>•</sup> Connection orientation makes TCP full-duplex and point-to-point:

• Full-duplex: if host A is connected with B, then B is connected with A. 

<sup>•</sup> Point-to-point: single sender and single receiver, i.e., the transfer of data from one sender to many receivers is not possible. 

<sup>•</sup> Note: UDP allows multicasting 

## <sup>•</sup> TCP is also oriented on sending/receiving data streams:

<sup>•</sup> Multiple TCP segments may be part of a bigger data stream (ordered sequence of data). 

<sup>•</sup> Single UDP datagrams are considered mostly decoupled. 

## Transport Layer TCP Bufers

<sup>•</sup> In TCP connection sending and receiving operations strongly rely on bufers to be performed. 

• Bufers allow us to partially decouple transmission times from: 

<sup>•</sup> Application delays. 

<sup>•</sup> OS delays in multiplexing demultiplexing packets. 

• Network delays (oscillations of network performance). 

<sup>•</sup> There is also the limit of the transmission rate, so long messages could be broken into smaller segments that may be collected in bufers before being disassembled (sender-side) or reassembled (sender-side). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/10974b66d820a4d42b59015012ee721d93fdbb611a9785bbd81f36f400b255d0.jpg)


## Transport Layer TCP Maximum Segment Size

• The amount of data inside a segment is limited by the Maximum Segment Size (MSS): 

$$
\mathrm{MSS} + 4 0 = \mathrm{MTU}
$$

• Where: 

<sup>•</sup> The Maximum Transmission Unit (MTU) is the maximum length of a frame acceptable by the link-layer (e.g., in Ethernet it is 1500 bytes). 

<sup>•</sup> The combined header size of TCP and IP headers (typically 20+20 bytes). 

<sup>•</sup> On sending: the segments are created from the application data and passed down to the network layer, where they are separately encapsulated within network-layer IP datagrams to be sent. 

<sup>•</sup> On receiving: the data is placed into the receive-bufer, the application grabs data from the bufer when ready. 

## Transport Layer

## TCP Segment

<sup>•</sup> The TCP segment consists of header fields and a data field, the later contains some application data of at most MSS size. 

• The header contains several fields: 

• Sequence number (32-bit) for reliable data transfer. 

• Acknowledgment number (32-bit) for reliable data transfer. 

• Receive window (16-bit) used to indicate the number of bytes that a receiver is willing to accept (for flow control). 

• Header length (4-bit) specifies the number of 32-bit words contained into the header. Note that TCP header is variable due to the options field. 

<sup>•</sup> Options field (K-bit) used for optional processes such as negotiating the MSS, time-stamping, etc. 

• Flags (6/12-bit) including: 

<sup>•</sup> ACK bit indicates that this segment is an ACK packet (so the acknowledgment number field is in use). 

• RST, SYN, and FIN bits used for connection setup and teardown. 

<sup>•</sup> CWR and ECE bits used in explicit congestion notification (optional). 

<sup>•</sup> PSH bit tells the receiver to pass the data to the application immediately. (RARE) 

• URG bit indicates that the segment contains “urgent” data. (RARE) 

• Checksum (16-bit): for integrity check. 

• Urgent data pointer field (16-bit) indicates the location of the last byte of the urgent part of the data. (RARE) 

<table><tr><td colspan="9">32 bits</td></tr><tr><td colspan="7">Source port #</td><td colspan="2">Dest port #</td></tr><tr><td colspan="9">Sequence number</td></tr><tr><td colspan="9">Acknowledgment number</td></tr><tr><td>Header length</td><td>Unused</td><td>CWR</td><td>ECE</td><td>URG</td><td>ACK</td><td>PSH</td><td>RST</td><td>SYN FIN</td></tr><tr><td colspan="8">Internet checksum</td><td>Receive window</td></tr><tr><td colspan="9">Options</td></tr><tr><td colspan="9">Data</td></tr></table>

## Transport Layer TCP Sequence and Acknowledgment Numbers

<sup>•</sup> Sequence numbers are used not only for reliable data transfer but also to manage segmentation. 

<sup>•</sup> If a large data stream is transmited, we need to break it into smaller <sup>“</sup>pieces” depending on the MSS. 

<sup>•</sup> Each “piece” of the stream is put into a TCP segment. 

## <sup>•</sup> Sequence numbers and acknowledge numbers are strictly related.

<sup>•</sup> The sequence number of a segment is conventionally the position that the first byte of the segment’s data has into the data stream. 

<sup>•</sup> The acknowledgment number is conventionally the next piece of the data stream we are expecting (calculated from the sequence number of the previous segment). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/b339b5e754196df6ab442bab1146eb3263110b1708b4c73abeef650a533fdcee.jpg)


## Transport Layer TCP Sequence and Acknowledgment Numbers

<sup>•</sup> Notice that TCP is a general-purpose transport protocol, it has no information about the data to be transmited. From TCP’s viewpoint data are just an ordered stream of bytes. 

<sup>•</sup> The sequence number for a segment is then the byte-stream number of the first byte of the data in the segment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/293185513043286d149c691f7fd7b17d9d89180f6adef8d99e0b1d3c1b06a47b.jpg)


• In the example, assuming a data stream of 500,000 bytes (~500KB), and a MSS of 1,000 bytes. 

<sup>•</sup> The TCP constructs 500 segments where the first segment has sequence number 0, the second segment has sequence number 1000, the third segment has sequence number 2000, and so on. 

## Transport Layer TCP Sequence and Acknowledgment Numbers

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/99d22eb9aa9617d646429d42038f1ee2bdfa3b43226a4820805d8a1902f66f63.jpg)


• Let’s assume this data stream to be passed from host A to host B. 

<sup>•</sup> For simplicity, let’s neglect previous interaction (data exchange from connection establishment), so we are starting from sequence number 0: 

• The receiver will get a first segment of 1,000 bytes, i.e., from sequence number 0 to sequence number 999. 

<sup>•</sup> The receiver will then acknowledge the transmission by seting an acknowledgment number of 1,000 (next expected byte in the stream). 

<sup>•</sup> The receiver will get the next segment of 1000 bytes, i.e., from sequence number 1,000 to sequence number 1,999 and so on… 

## Transport Layer TCP Sequence and Acknowledgment Numbers

## <sup>•</sup> What happens if the receiver is sending data in return?

<sup>•</sup> Remind: TCP communication is full-duplex, if 2 hosts, A and B, communicate there are also 2 flows of data to be considered for reliable data transfer: A-to-B and B-to-A. 

## <sup>•</sup> In this case we can use sequence numbers and acknowledgment numbers at the same time:

<sup>•</sup> Segments from A have sequence numbers related to Ato-B data stream and acknowledge numbers related to the B-to-A data stream. 

<sup>•</sup> Segments from B have sequence numbers related to Bto-A data stream, and acknowledge numbers related to the A-to-B data stream. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/054d0a4875da8e2f2f9a01a3be1eae051c4ed3224800b4c192fa5d2c70ebb8c2.jpg)


## Transport Layer TCP Sequence and Acknowledgment Numbers

<sup>•</sup> This is a simplified example of two hosts sending data each other. 

• We are considering 2 messages of just 1 byte (1 char) form A to B and vice versa. 

<sup>•</sup> Specifically, host A transmits a ‘c’ that is echoed back by B. 

<sup>•</sup> Here that segments provide ACK and DATA at the same time (so the ACK flag is 1). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/b2a380ca56b68d07afbca18d49f606cfc0dcf6b7c03bd63a1427948b634660e3.jpg)


A-to-B info are in green. B-to-A info are in red. 

## Transport Layer TCP Sequence and Acknowledgment Numbers

## 1. From A to B:

• The ack number as the seq number of the next expected packet in the B-to-A flow (byte 79). 

<sup>•</sup> The seq number as the position of the single byte we are transmiting (byte 42). 

## 2. From B to A:

<sup>•</sup> The ack number as the seq number of the next expected packet in the A-to-B flow (i.e., seq + 1 byte of the ‘c’ char). 

• The seq number as the position of the byte we are transmiting (byte 79). 

## 3. From A to B:

<sup>•</sup> Pure ACK segment is sent, having seq number 43 (as expected by B) and ack number 80 (next expected). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/ea4b98a145df8ea17fb729f00a5bf9c187865da5a1fca23124c6656df4187e3d.jpg)


## Transport Layer Retransmission Timeout

<sup>•</sup> Previously we have emphasized that TCP reliable data transfer mechanism makes extensive use of timeouts. 

<sup>•</sup> The default approach in pipelining-based TCP transmission is to retransmit segments only if the associated ACKs are not received before the timeout. 

<sup>•</sup> Therefor, timeout estimation is critical as it strongly afects the performance of the transmission. 

<sup>•</sup> Too long timeout causes communication to be slowed. 

<sup>•</sup> Too short timeout causes the packets to overlap (and unnecessary packets to be retransmited, producing useless trafic on the network). 

## Transport Layer RTT Estimation

• To suitably set timeouts we need a round-trip time (RTT) estimation. 

• The timeout, i.e., the time to wait for a segment’s ACK, should be larger than RTT otherwise unnecessary retransmissions would be sent. 

<sup>•</sup> TCP estimates this value by sampling the RTT of successfully acknowledged segments that have not been retransmited (one-shot). 

• Since the time of a sampled RTT (SampleRTT) may fluctuate (due to trafic congestion, load of the receiver, etc.) the RTT estimation (EstimatedRTT) is given by the exponential weighted moving average (EWMA): 

EstimatedRTT = (1-α) EstimatedRTT + α SampleRTT⋅ ⋅ 

Where α is a parameter which is usually 0.125 (i.e., 1/8). 

## Transport Layer RTT Estimation

• We can also consider the variability of the RRT in our timeout calculation. 

• The variability of the RTT (DevRTT) can be given by the diference between the sample (SampleRTT) and the estimation (EstimatedRTT): 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/1f907bdca17f25553a157891721b57407b7fae822fd4f2ae150ae78ad9ab3260.jpg)


DevRTT = (1-β) DevRTT + β | SampleRTT – EstimatedRTT⋅ ⋅ 

Where β is a parameter which is usually 0.25 (i.e., 1/4). 

## Transport Layer Retransmission Timeout

<sup>•</sup> Having these estimations, it is possible to define a retransmission timeout for TCP that is not too much lower or higher than the estimated RTT: 

$$
\text {TimeoutInterval} = \text {EstimatedRTT} + 4 \cdot \text {DevRTT}
$$

• Here, the deviation of the RTT is used to set a reasonable and adaptive margin from the estimated RTT. 

<sup>•</sup> It increases when RTT oscillates, so the timeout window is larger when we are uncertain about our current RTT. 

• By default, the initial value of the RTT (at t=0) is 1 second. 

## Transport Layer

## Fast Retransmit

<sup>•</sup> Timeout-triggered retransmission is quite efective, but the timeout period can be relatively long. 

<sup>•</sup> Fast retransmit is an approach in which the receiver signals the sender that one packet might be lost by sending duplicate ACKs. 

<sup>•</sup> When a TCP receiver receives a segment with a sequence number that is larger than the expected one it means that a segment has been reasonably missed. 

• The receiver resends the old ACK (duplicate ACK) having as ACK number the one of the expected segment. 

<sup>•</sup> If the sender receives N duplicates (typically 3 duplicates), it assumes that the previous segment has been lost so it is (fast) retransmited well before the deadline. 

## Transport Layer

## Fast Retransmit

<sup>•</sup> In this example we have a lost segment with sequence number 100. 

<sup>•</sup> Every time host B receives an out-of-order segment it sends back a duplicated ACK (ack=100). 

<sup>•</sup> When host A receives 3 duplicates, it assumes segment 100 to be lost and resends it (fast retransmit). 

<sup>•</sup> When host B finally receives the lost segment, it will send the ACK of the next expected segment depending on its own policy (go-back-N or selective repeat). 

<sup>•</sup> But why don’t we retransmit segments directly when the first duplicated ACK is received? 

<sup>•</sup> Because we may receive wrong ACKs for diferent reasons (not only if segments are lost). 

<sup>•</sup> For example, if 2 segments are received in the wrong order (swapped during transmission), the receiver will send 1 duplicate ACK (for the first segment) before detecting the swap. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/c185b446-d56b-49aa-91a6-32f8e86330bf/c133b75d8386cd7ba80df68ab8b54c27fd5dfe9ea57f3c6095e27575ac2b1589.jpg)
