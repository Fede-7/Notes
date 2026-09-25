## The Application Layer: TCP

Lecture 11 

## Transport Layer Reliable Data Transfer Problem

<sup>•</sup> Let’s assume we are at the railway station waiting for the train number 6 which should arrive on platform 5. 

<sup>•</sup> The train changes platform, it will arrive on platform 9 instead of platform 5, a message is sent from station control to communicate it: 

“Train 6 will arrive on platform 9” 

<sup>•</sup> What happens if the communication is unreliable: 

<sup>•</sup> Words could be lost: “Train %&! will arrive on platform 9” 

<sup>•</sup> Words could be altered: “Train 7 will arrive on platform 9” 

• Words could be swapped: “Train 9 will arrive on platform 6” 

<sup>•</sup> Words could be duplicated: “Train 66 will arrive on platform 9” 

<sup>•</sup> It is possible you can understand that the message is wrong (for example in case 1), but you may also take the wrong train or miss the right one. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/f08881f2655b34e7cf0b0b0a9d306433c5d6bd836a8eb4911b8f12bdc3e9e7b8.jpg)


## Transport Layer Reliable Data Transfer

• Error control (e.g., through checksum) allows receiver at least to understand if the message is corrupted, but this is not enough. Reliable data transfer is still one of the main problem of networking. 

<sup>•</sup> The problem is not only addressed at the transport layer, but also at the link layer and (often) at the application layer. 

<sup>•</sup> In a reliable channel 3 elements must be guaranteed: 

1. None of the transmited bits are corrupted (flipped from 0 to 1, or vice versa). 

2. None of the transmited bits are lost or repeated. 

3. All bits are delivered in the exact order in which they were sent. 

<sup>•</sup> In general, we must assume the lower-level network layer to be unreliable. 

<sup>•</sup> This is a realistic assumption, for example, TCP is a reliable data transfer protocol that is implemented on top of an unreliable (IP) end-to-end network layer. 

## Transport Layer Reliable Data Transfer: Packet Corruption and Stop-and-wait

• Let’s assume we have a channel where bits may only be corrupted (not lost). 

<sup>•</sup> Corruption of bits is a typical problem, which is mainly due to the physical components of a network as a packet is transmited, propagated, or bufered several time during the communication. 

<sup>•</sup> Stop-and-wait: a first approach requires each message to be acknowledged before sending a new one: 

• Positive acknowledgments (ACK) means that the message has been received intact. 

• Negative acknowledgments (NCK) means that an error occurred, so the message must be repeated. 

<sup>•</sup> In a computer network, protocols based on retransmission are also known as ARQ (Automatic Repeat reQuest) protocols. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/c49f9806eb8663471e66d3b3ffe31f0001d1facaf36f262446efc5dbc4df8b19.jpg)


## Transport Layer Reliable Data Transfer: Stop-and-wait

<sup>•</sup> There are a couple of issues with this approach: 

<sup>•</sup> What happens if the ACK/NCK message is corrupted itself? 

<sup>•</sup> How can Host B be sure that a message is the repetition instead of a new message? 

• Sequence number: add a new field to the headers of packets which specifies the order in which packages should be received. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/2c1525807511d4574757b4c9e15cf1f4cafbac4e0f2e841ae9d9de6fe619cb4c.jpg)


What if my NCK has been corrupted? 

Is this message new or old? 

## Transport Layer Reliable Data Transfer: Stop-and-wait

<sup>•</sup> In a stop-and wait approach we always have one message on the line. 

<sup>•</sup> There is no need to specify the whole sequence of packets, we just need to diferentiate between the current packet and the previous one. 

• Therefore, in this case, we just need to add one bit (s = 0/1) to the headers of packets. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/06420f3b5b493d8c4bc9175b2c60c7ebe46e586644d2890e864b3dcc40951e6b.jpg)


## Transport Layer Reliable Data Transfer: Packet Loss and Stop-and-wait

• Let’s assume we now have a channel where packets may also be lost. 

<sup>•</sup> This is also quite reasonable as network devices may have bufer overflow in case of intense trafic. 

<sup>•</sup> Here we have a clear problem with stopand-wait approach: the loop. If one message is lost, hosts will never send a new one. 

<sup>•</sup> Notice that this happens whether we lose message or acknowledgment, as in both cases host A will not be triggered to send a new message. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/6bfca5ca2876bbf0b3a4cf51a97029c657a8172f230935b61b192339064437eb.jpg)


## Transport Layer Reliable Data Transfer: Packet Loss and Stop-and-wait

<sup>•</sup> Timeout: a very simple yet efective solution is to add a timeout on the senderside that, once expired, allows the Host to try again. 

<sup>•</sup> A similar approach can be used in UDP-based DNS. 

• This works both in the case of packet loss and in acknowledgment loss. 

<sup>•</sup> In case of duplicate the receive has just to discard the packet. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/f147ecc88785d7c779a2b69a5f9661f748b818c111a60c84213c7ec45a1386cc.jpg)


## Transport Layer Reliable Data Transfer: Packet Loss and Stop-and-wait

<sup>•</sup> The challenge here is how to estimate a suitable timeout (it depends on the RTT). 

<sup>•</sup> Too long timeout causes communication to be slowed. 

<sup>•</sup> Too short timeout causes the packets to overlap. 

<sup>•</sup> We can say that a reasonable timeout should be somehow longer than the RTT. 

<sup>•</sup> Timeout saves stop-and-wait from loop, but the performance are quite bad… 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/8c0bfe60ea0e96621ebab8dfd09b50f192c2fe8650cf4c9e94772a8a00d3c402.jpg)


## Transport Layer Reliable Data Transfer: Water Example

## • We can see data transfer as a water flow problem:

• There is the time (t) to move the water from the tank to the tube. While entering the water is also moving toward the tube. 

• After t all the water from the tank is inside the tube (the initial tank is empty as well as the destination tank). 

• It takes a certain time (RTT/2) for the water to flow into the tube. 

<sup>•</sup> Finally, the water arrives at the destination tank and (by assuming same download/upload time) it takes the same time t to pour out of the tube (RTT/2 + t to receive the last drop). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/3281834abcc043ff1d94c9d8298002ad6b2de595b7fe27ca037e486dd68c2117.jpg)



Tot = RTT/2 + t


## Transport Layer Reliable Data Transfer: Performance of Stop-and-Wait

• Let’s consider the idealized case of two hosts located on the opposite coasts of the United States. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/0d496bbd9c7ae868218c9a0737da87be429819898475a53799691a2856655d05.jpg)


<sup>•</sup> The speed-of-light RTT between these two end systems is approximately 30 milliseconds (0.03 sec.). Let’s assume to have: 

• A channel with a transmission rate (R) of 1 Gbps (10<sup>9</sup> bits per second). 

• A packet size (L) of 1000 bytes (8000 bits). 

• The time (t) needed to transmit the packet to the channel is: 

(8 microseconds) 

## Transport Layer Reliable Data Transfer: Performance of Stop-and-Wait

## • Let’s consider the idealized case of two hosts located on the opposite coasts of the United States.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/de3a36d5435edc1b2a7a3d135140227175718d68cd367aea4c1ed15be86836c0.jpg)


## <sup>•</sup> In a stop-and-wait protocol:

<sup>•</sup> the sender begins sending the packet at $\mathbf { t } _ { 0 } ,$ 

• the last bit enters the channel at $\mathbf { t } _ { \scriptscriptstyle 0 } + 0 . 0 0 0 0 0 8 \mathsf { s e c }$ 

• the packet takes 0.015 sec. to reach the receiver, 

• the last bit is received at $\mathbf { t } = \mathsf { R T T } / 2 + \mathsf { L } / \mathsf { R } = 0 . 0 1 5 0 0 8 \mathsf { s e c } .$ 

<sup>•</sup> assuming that ACK packets are extremely small (their transmission time can be neglected) the ACK emerges back at the sender at $\mathbf { t } = \mathsf { R T T } + \mathsf { L } / \mathsf { R } = 0 . 0 3 0 0 0 8 \mathsf { s e c }$ 

<sup>•</sup> In 0.030008 sec. of total transmission time, the sender was waiting almost all the time (99.973% of the time). 

## Transport Layer Reliable Data Transfer: Performance of Pipelining

• Pipelining: instead of stop-and-wait, the sender is allowed to send multiple packets without waiting for acknowledgments. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/3c4b83c15354a910d31487d3f5636af2cc4e89b4ab89715d04361c6f72c9976e.jpg)


<sup>•</sup> In pipelining approaches (e.g., 3 packets instead of 1): 

<sup>•</sup> the sender begins sending the 3 packets at $\mathbf { t } _ { 0 } ,$ 

<sup>•</sup> the last bit of the last packet enters the channel at $\mathfrak { t } _ { \scriptscriptstyle 0 } + 0 . 0 0 0 0 2 4 \ : \mathfrak { s e c } .$ • 

• the packets take 0.015 sec. to reach the receiver, 

• the last bit is received at $\mathrm { t } = \mathrm { R T T } / 2 + \mathrm { L } / \mathrm { R } = 0 . 0 1 5 0 2 4 \mathrm { s e c } .$ 

<sup>•</sup> assuming that ACK packets are extremely small (their transmission time can be neglected) the ACK emerges back at the sender at $\mathbf { t } = \mathsf { R T T } + \mathsf { L } / \mathsf { R } = 0 . 0 3 0 0 2 4 \mathsf { s e c } .$ 

• In 0.030024 sec. the sender was waiting 0.035% less (99.920% instead of 99.973%). 

## Transport Layer Reliable Data Transfer: Performance of Pipelining

• Pipelining: instead of stop-and-wait, the sender is allowed to send multiple packets without waiting for acknowledgments. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/202ed05cf84454aebbe7f6dd964219b32d4e972600b7e59d1675c19b18c3e5b9.jpg)


## <sup>•</sup> In pipelining approaches:

• The range of sequence numbers must be increased since each in-transit packet (not counting retransmissions) must have a unique sequence number and there may be multiple, in-transit, unacknowledged packets. 

<sup>•</sup> We need bufers to store incoming packets since we don’t know if packets are correct or there are “holes” in the transmission. 

<sup>•</sup> There are 2 basic protocols using pipelining: 

• Go-Back-N. 

• Selective Repeat. 

# Transport Layer Reliable Data Transfer: Go-Back-N

• Go-Back-N (GBN) protocol (aka sliding-window protocol): the sender is allowed to transmit multiple packets (when available) without waiting for an acknowledgment but is constrained to have no more than N unacknowledged packets. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/6a2089b22ca11618966cf789f03a5e9b6dbaad46c9d08cca61ddc5d0a3c4efbc.jpg)


• Base: is the sequence number of the oldest unacknowledged packet. 

• Nextseqnum: is the smallest unused sequence number (next to be sent). 

• We have that: 

• Packets in [0, base-1] have been transmited and acknowledged. 

• Packets in [base, nextseqnum-1] have been sent but not yet acknowledged. 

• Packets in [nextseqnum, base+N-1] can be sent. 

• Packets in [base+N, +inf] cannot be used until a new acknowledgment is received. 

## Transport Layer Reliable Data Transfer: Go-Back-N

<sup>•</sup> What about the receiver? In GBN protocol receiver is quite simple. 

• The receiver has simply to discard out-of-order packets (whether they are damaged or not) and to deliver to the upper level (application) in-order packets only. 

<sup>•</sup> Discarded packets (not acknowledged) will be eventually retransmited by the sender. 

<sup>•</sup> With this approach good packets are also discarded but the overall process is quite simple: 

• the sender must maintain the indices of the window, 

• the receiver only needs to maintain the sequence number of the next in-order packet. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/93f27a3a380712830c620ad2dc4699da72f6546ff7911460e1d942542ffddc56.jpg)



Since pkt2 is lost, all pkt3, pkt4, pkt5, must be discarded even if correct.


## Transport Layer Reliable Data Transfer: Go-Back-N

<sup>•</sup> Of course, the disadvantage of throwing away a correctly received packet is that we need to resend it again. 

<sup>•</sup> This is a chain-reaction, if we are losing packets due to network dificulties many correctly received but out-of-order packets may be discarded forcing the sender to retransmit them. 

<sup>•</sup> The retransmission itself might be lost or damaged and thus even more retransmissions would be required. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/88be9c2bfdade085562e70bfb2407ec6b33c88ea319278d3f4b02aaba30b1442.jpg)



Not only pkt2, but also pkt3, pkt4, pkt5, must be transmited again.


b. Receiver view of sequence numbers 

## Transport Layer Reliable Data Transfer: Selective Repeat

<sup>•</sup> Despite GBN is more efective than stop-and-wait, it may sufer from performance problems. 

• Considering large window size, a single packet error can cause GBN to retransmit a large number of packets, many unnecessarily. 

• In selective-repeat (SR) protocols: the sender retransmit only those packets that were likely received in error (lost or corrupted): 

• As in GBN individual packets are acknowledged. 

• A window size of N is again used to limit the number of unacknowledged packets. 

• Unlike GBN, out-of-order packets are bufered (stored) and acknowledged by the receiver. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/1f727afa8da559aadcf402fe66e64b9480beac8ed3ff31debe9d7da130541c01.jpg)


## Transport Layer Reliable Data Transfer: Selective Repeat

Example of SR operation in the presence of lost packets: the receiver initially bufers pkt3, pkt4, and pkt5, while waiting for pkt2 (lost) to be retransmited. 

<sup>•</sup> Despite the previous example, here we avoid to resend pkt3, pkt4, pkt5, in so avoiding additional transmission loss or errors. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/bf69c809ff376451ba9428b319d4494d3a45745c52d6d3c66aad544529f86b21.jpg)


# Transport Layer Reliable Data Transfer: Selective Repeat

<sup>•</sup> One issue in SR is that the window size is related to the sequence number, and sequence number is finite. 

<sup>•</sup> In this example we have four packets, a max sequence number of 3 and a window size of 3. 

<sup>•</sup> Let’s assume packets 0 to 2 are correctly received and their ACK have been sent (but not yet received). 

• The receiver’s window moves to 6<sup>th</sup> packet (i.e., to [3, 0, 1] ) even if ACK are not received for certain. 

<sup>•</sup> Case a: the ACKs for the first three packets are lost and the sender retransmits these packets. Is packet 0 new or old? 

<sup>•</sup> Case b: the ACKs are received, packets 3 and 0 are sent but packet 3 is lost. Is packet 0 new or old? 

## • To avoid this issue, the sequence number must be at least 2 times the window size.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/7de41027ba56b80ffa6e3acbdfc1ce8f0137109fe2b298746eb9722baca8c211.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/dd2f9997-2e89-4abf-9f6b-a492d03a6fbf/d580a2ebcced928ae190e16cf0134a43a2a1a734276404218028f3c391dbd1c5.jpg)
