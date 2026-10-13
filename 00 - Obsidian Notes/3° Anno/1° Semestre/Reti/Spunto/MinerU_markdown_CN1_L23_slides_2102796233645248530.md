## The Link Layer: MAC sublayer

Lecture 23 

## Link Layer

## Services

• Link layer may ofer up to 4 services: framing, link access, reliable delivery, error detection and correction. 

1. Framing: to encapsulate/decapsulate datagrams into/from frames. 

2. Link access: to regulate access to shared links (broadcast) 

• Done by the Medium Access Control (MAC) protocol. 

3. Reliable delivery: to guarantee that frames transmited across the link are received (mostly optional). 

4. Error detection and correction: to detect frame’s errors and possibly correct them. 

• Parity check, checksum, CRC. 

## Link Layer Link Types

• There are basically 2 types of links that can be managed: 

• Point-to-point link: consists of a single sender at one end and a single receiver at the other end. The point-to-point protocol (PPP) is one example of protocol managing such links. 

• E.g., direct ethernet link between 2 computers. 

Broadcast link: multiple sending and receiving nodes all connected to the same shared channel. The term broadcast is used because when one node transmits a frame it is received by all nodes on the channel. 

• E.g., Ethernet bus, half-duplex Ethernet (rare, as most cables are todays full-duplex) or wireless LANs. 

• The access to broadcast links have to be coordinated (multiple access problem) as multiple communication on a single link may interfere each other. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/3c57914bc5bb827432eef6b91c178690794b66ebca1d420dad0da757b036e28e.jpg)


## Link Layer

## Collisions

• The main problem of broadcast link is the collision: if multiple nodes are simultaneously transmiting frames on the same channel, all such frames overlap becoming unintelligible. 

• These collided frames are then received by all nodes on the channel and dismissed as errors (no harm is done), but: 

• All transmited frames are lost. 

• The time-interval is wasted, as the channel has been used to transmit useless data. 

• The access to the physical medium (as well as framing) is regulated by the MAC (Medium Access Control) protocol. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/0bc542e8c21796fe0a8d0485e15b5f4c7cec7bdfe9358f83d8e85ca5cdab5abc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/0e986795f31156938c226dc30dd62dff44396fe2258164c672b3646257f77113.jpg)


## Link Layer Multiple Access Protocol

• In computer networks multiple access protocols are used to regulate transmissions via broadcast channels, so that: 

• Collisions are managed. 

• Each node has a chance to transmit, so nodes do not monopolize the link. 

• Established connections are not interrupted (e.g., checking if link is busy). 

• Such protocols are needed for a variety of network setings, including both wired, wireless or satellite networks, where hundreds or thousands of nodes can directly communicate over a broadcast channel. 

Shared wire (for example, cable access network) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/2364044efae5bbeeacccbec52ad7e263ceddf255160e0033690a6553ac5b7089.jpg)


## Link Layer Multiple Access Protocol

• The primary role of a multiple access protocol is to somehow avoid collisions (there are dozens of protocols over diferent link-layer technologies). Main approaches are: 

• Channel partitioning: the bandwidth is partitioned for diferent nodes. 

• Random access: the nodes “gamble” for the access. 

• Taking-turns: the nodes waits for their turn. 

## • Desiderata: a multiple access protocol for a broadcast channel of rate R bps should also provide the following characteristics:

• To maximize the usage of the channel: if M nodes have data to send, each one should have, in average, a throughput of R/M bps (if M=1 then throughput should be R). 

• To be decentralized: a master node may be a single point of failure. 

• To be simple and lightweight: tons of frames are sent, there must be no overhead. 

## Link Layer Channel Partitioning Protocols: TDMA

• Time division multiple access (TDMA): let’s consider a channel with N nodes having transmission rate of R bps, TDMA divides time into time frames (steps) and further divides each time frame into N time slots. 

• Each time slot is assigned to one of the N nodes. Whenever a node has a packet to send, it waits for the assigned time slot. 

• Typically, slot sizes are chosen so that a whole packet can be transmited during a slot time. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/9b9952cf21f7aed9ec255fc4c5e1edb3b34d751ce22685252d5857bfdd74befd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/24a27e26966b80ef856a785f4bbc9d69693766c0e2d120a72d8a6302c8a2ebaa.jpg)


## Link Layer Channel Partitioning Protocols: FDMA

• Frequency division multiple-access (FDMA): divides the R bps channel into diferent frequencies (each with a bandwidth of R/N) and assigns each frequency to one of the N nodes. 

• FDMA and TDMA share pros and cons: 

• They avoids collisions and divide the bandwidth fairly among the N nodes. 

• A node is limited to a bandwidth of R/N, even when it is the only node with packets to send. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/a9e8c31a87e55a086476cd8cffc763fdf5cc377a90f8fc2b140466220cf5cd3f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/2c751bed0fc3dab2a2bae5b25c23ec23dcd0358646a70c161a7bb67f7c6eb671.jpg)


## Link Layer Channel Partitioning Protocols: CDMA

• Code division multiple access (CDMA): assigns a diferent code to each node which is used to encode/decode the data bits it sends. 

• If the codes are chosen carefully, CDMA networks allows diferent nodes to transmit simultaneously without causing interference. 

• CDMA works mainly on wireless channels; it has been used in military systems for some time (due to its anti-jamming properties) and also in cellular telephony (e.g., 3G). 

• Complex to implement. 

• It does not scale well with the number of nodes. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/e9a5fb3fd4c70d3dfba3a07fea37885d5802c6406d42c0d3c301ffe11efa6485.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/81374caa6a9a564cf9eff918f2421954c92f727b4ca6245fa25c9328c5557107.jpg)


## Link Layer Random Access Protocols

• In random access protocols, a transmiting node always transmits at the full rate of the channel (at R bps). 

• If a collision occurs (i.e., at least 2 nodes are transmiting) all transmiting nodes waits a random delay before atempting again the retransmission. 

• Since this selection is performed independently, it is possible for the 2 nodes to choose a delay which is diferent enough to allow one of the two contenders to sneak the message in. 

• If, otherwise, a similar delay is chosen, a new collision occurs, and the process is iterated. 

## Link Layer Random Access Protocols: Sloted ALOHA

• The sloted ALOHA protocol works as follows: 

• The time is divided into slots (as in TDMA) where each slot is large enough to contain one frame. 

• The nodes are synchronized, so each node transmit frames only at the beginnings of a slots. 

• If no collision is detected within the slot, the communication continues. 

• Otherwise, if a collision is detected within a slot, each colliding node have a probability p ϵ [0,1] of resending this frame in each one of the following slots, until the frame is successfully sent. 

## • Features:

• If there is only one node, it will use the full rate R of the channel (no collisions). 

• Is decentralized as nodes are totally independent from the others besides the synchronization. 

• Is simple to implement and to execute (random selection is quite fast). 

• Having multiple consecutive collisions is unlikely. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/ab8669de-f470-4a79-8b00-748dcbf306e2/3bed56162ab1386d0ee461b2b2ec67c6aeff2d055992ce274dc1c087f2f07e01.jpg)


## Link Layer Random Access Protocols: CSMA

• One weakness of ALOHA is that we may start transmiting (producing a collision) even if the channel is already busy. We understand it just through the efect of collisions. 

• A solution is to monitor the channel and to atempt transmission only if the channel is idle. 

• Carrier sense multiple access (CSMA) and CSMA with collision detection (CSMA/CD) protocols are based on 2 principles: 

• Carrier sensing: nodes listen to the channel before transmiting. If a frame from another node is currently being transmited, it waits until no transmission is detected. 

• Collision detection: nodes listens to the channel while it is transmiting. If a collision is detected, it stops transmiting and waits a random amount of time before restarting. 

• If all nodes perform carrier sensing, why do collisions occur in the first place? 