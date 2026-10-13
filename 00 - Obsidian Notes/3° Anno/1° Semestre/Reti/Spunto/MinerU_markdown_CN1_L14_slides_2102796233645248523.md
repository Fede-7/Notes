## Transport Layer Congestion and Flow Control Problem

<sup>•</sup> Additional features of TCP with respect to UDP are the congestion and flow control. 

• We mentioned that packet loss is often a result of bufers’ overflow: 

• From receiver bufer, if receiving application is not fast enough in reading the data. 

• From network devices (e.g., routers), if nodes are congested. 

<sup>•</sup> Following our previous water-flowing analogy, we can see bufers as intermediate buckets that overflows in case water exceeds. 

<sup>•</sup> If packets are lost, hosts are forced to rely on retransmission and timeouts that drastically impair the network performance. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/94dfd6c71aeda6dd3e636a20fd180c54a8db91a41dd8513d4204297950e8787c.jpg)


## Transport Layer

## Flow Control

• When the TCP connection receives bytes that are correct and in sequence, it places the data in the receive bufer. The receiving application will read data from this bufer, but not necessarily at the instant the data arrive (application may be busy). 

• If the application is relatively slow at reading the data, the sender can very easily overflow the receiver bufer by sending too much data too quickly. 

• TCP flow control is a speed-matching service: it atempts to match (reduce) the rate at which the sender is sending against the rate at which the receiving application is reading. 

• In this case we rely on a receive window to inform the sender how many segments we can receive without producing overflows. 

• Remind: TCP segment allow receiver to tell the sender how much bufer has left through the receive window field (free bufer space). 

## Transport Layer Flow Control

<sup>•</sup> Let’s assume for simplicity that the TCP receiver discards outof-order segments, so all segments in the bufer are ordered. 

• On the receiver side (host B) we have: 

• RcvBufer: size of the receiver bufer (in bytes) 

<sup>•</sup> LastByteRead: the last byte of the stream retrieved by the application. 

<sup>•</sup> LastByteRead:the last byte of the stream that is received. 

• We may define the size of the receive window (rwnd) as: rwnd = RcvBufer – (LastByteRcvd - LastByteRead) 

• On the sender side (host A) we have: 

<sup>•</sup> the last byte of the stream to be sent. 

<sup>•</sup> the last byte of the stream that is acknowledged by the receiver. 

• Knowing the receive window, the sender guarantees anytime that: 

LastByteSent – LastByteAckd ≤ rwnd 

Receiver: 

Sender: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/be73297fd2fdb7ecf602156d8f898b5bd28b054f8082eb4bfc7b7d0dcadb0176.jpg)


## Transport Layer Congestion Problem

• The congestion control problem is similar to flow control, but it is related to the network infrastructure. 

• Example: two hosts (A and B) have a connection that shares a single router and a single outgoing link of capacity between source and destination. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/568f9d221ed16cc50f7afa210de695a4b7d269a728bdb6ff1e15d7de7225c502.jpg)


<sup>•</sup> The router has bufers that allow it to store incoming packets when the packetarrival rate exceeds the outgoing link’s capacity. 

• Link capacity: R 

Let’s assume for simplicity that both applications (in A and B) are sending data into the connection at the same average rate of λin bytes/s. 

## Transport Layer Congestion Problem – simplified view

<sup>•</sup> If λin<R/2, everything sent by the sender is received by the receiver with a finite delay. 

• If λin=R/2, the link reaches its full capacity (R), and the exceeding packets are stored into the bufer. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/71ff4b95c0ab5212f0706a26d8258393bca52e1e68b00e70b584a60149349730.jpg)



Router


<sup>•</sup> As long as we exceed the maximum capacity the packets will be accumulating into the router<sup>’</sup>s bufer waiting for their turn to be sent into the link. 

<sup>•</sup> Since the bufer is finite, accumulated packets will eventually be discarded, and hosts will be forced to retransmit them (even more trafic). 

<sup>•</sup> An infinite bufer doesn’t work either: packets will not be lost but the delay would constantly increase: if we exceed the capacity forever, the delay will reach infinity (so packets are as good as lost). 

## Transport Layer Congestion Control

• There are mainly two approaches to congestion control: 

1. End-to-end congestion control: this is the standard TCP approach where congestion is inferred by the end systems based only on observed network behavior (for example, packet loss and delay). 

<sup>•</sup> TCP segment loss (due to timeouts or the receipt of 3 duplicate ACKs) is taken as an indication of network congestion, and TCP decreases sending rate accordingly. 

2. Network-assisted congestion control: this is a recent (optional) approach where transport-layer works in synergy with network-layer. Routers provide explicit feedback to the sender and/or receiver regarding the congestion state of the network. 

<sup>•</sup> The CWR and ECE flags are used to this end. 

<sup>•</sup> The feedback may be as simple as a single bit indicating congestion at a link, but more sophisticated feedback is also possible. 

## Transport Layer TCP Congestion Control

• TCP mostly relies on end-to-end congestion control. 

<sup>•</sup> The approach is to have each sender to adapt their sending rate depending on the perceived network congestion. 

<sup>•</sup> Here there are 3 main problems to be considered: 

<sup>•</sup> Rate regulation: how does a TCP sender regulate the rate at which it sends trafic into its connection? 

<sup>•</sup> Congestion detection: how does a TCP sender detect the congestion on the path between itself and the destination? 

<sup>•</sup> Rate adjustment: what algorithm should the sender use to change its send rate as a function of perceived end-to-end congestion? 

## Transport Layer TCP Congestion Control – Rate Regulation

• Reminder: in TCP flow control the sending rate is regulated by considering the bufer space on the receiver side (receiver window, rwnd): 

LastByteSend – LastByteAcked ≤ rwnd 

• In TCP congestion-control the sender also keeps track of a congestion window (cwnd): 

LastByteSent – LastByteAcked ≤ min{cwnd, rwnd} 

<sup>•</sup> So, the rate is regulated by increasing/decreasing . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/f854de5a627ce2124003173b64347a51cde01ce485db9ad58703b6ba5df3a90b.jpg)



Receive Window


Sent and ACKed 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/575b6fca950308b7683b4f2fb054b32fee1f33ff67442e2e30091eb4a845a7e0.jpg)


Sent, not ACKed 

_ Send Can 

## Transport Layer TCP Congestion Control – Congestion Detection

<sup>•</sup> A TCP sender perceives that there is congestion on the path between itself and the destination in two ways by checking loss events. 

<sup>•</sup> A loss event happens when either a timeout is reached or 3 duplicate/wrong ACKs are received. 

<sup>•</sup> Both events mean that a previous packet is not arrived at the destination probably because of network devices overflow. 

<sup>•</sup> If loss events do not occur, i.e., ACKs of segments arrive as expected, TCP will assume that network is not congested, so the congestion window can be increased. 

<sup>•</sup> If, on the other hand, loss events occur, the congestion window must be decreased. 

## Transport Layer TCP Congestion Control – Rate Adjustment

• TCP rate adjustment is then performed through bandwidth probing: rate is increased as long as ACKs arrive correctly (probing the network), when congestion is detected (loss events) the rate is decreased. This process is continuously repeated. 

• TCP uses Jacobson congestion-control algorithm [Jacobson 1988] to regulate the rate, it includes 3 phases: 

1. Slow start: start from 1 MSS/RRT increase rate exponentially. 

2. Additive Increase (or congestion avoidance): increase rate linearly. 

3. Fast Recovery (optional): halves the rate instead of slow-starting again and proceed with additive increment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/9d2283df-2416-4ca1-bdff-ab083f5235cb/454bf6f4a4e4ff625e7e4b9a7a0fb1d46530e0f1a9a04456a15df5ae7ec8dd87.jpg)



Typical sawtooth behavior of the Jacobsen algorithm
