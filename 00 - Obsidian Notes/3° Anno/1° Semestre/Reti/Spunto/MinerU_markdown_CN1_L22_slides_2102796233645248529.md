## The Link Layer: Framing and error management

Lecture 22 

## Link Layer From Network to Link & Physical

• We have seen that the network layer basically provides communication layer between two hosts (wherever they are). 

• Link and physical layers provide communication between two connected hosts: 

• The link layer is the portion of the stack dedicated to the transmission of packets over links (transmission channels), from node to node of the network. 

• The physical layer is the portion of the stack that regulates the structure of links (transmission medium, connectors, cable types, etc.) and how bits are represented/transmited along the link. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/ecbeaa851e390da2a2ecdb5b81c99133c2e05da8e2e0c4ac281b85ae8dd953e0.jpg)


## Link Layer From Network to Link & Physical

<sup>•</sup> We have seen that the network layer basically provides communication layer between two hosts (wherever they are). 

<sup>•</sup> Link and physical layers provide communication between two connected hosts: 

<sup>•</sup> The link layer is the portion of the stack dedicated to the transmission of packets over links (transmission channels), from node to node of the network. 

• The physical layer is the portion of the stack that regulates the structure of links (transmission medium, connectors, cable types, etc.) and how bits are represented/transmited along the link. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/986a564f86e9c5a02966f3b84f93194cf9b25749f911b3d60fbd48a28456d059.jpg)


## Link Layer From Network to Link & Physical

• Link and physical layers are strictly intertwined (these are often grouped into a single layer called network access). 

• Some common protocols (e.g., Ethernet) cover both layers. 

<sup>•</sup> Diferently from the previous layers, these 2 layers are present in all pieces of the network infrastructure: 

• Nodes: hosts (PC, servers, etc.), routers, switches, hubs, WiFi access points, etc. 

<sup>•</sup> Links: wired (copper cables, optical-fiber), wireless (radiofrequencies). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/7f57b2472729c8360c740cd166717a50425f6b65ce7456a4b0c3503bade8dc19.jpg)


## Link Layer From Network to Link & Physical

<sup>•</sup> To transmit an IP datagram, we must transfer it from source host to destination host by jumping over each of the individual links/devices along the path. 

<sup>•</sup> To be transferred over a link, datagrams are encapsulated into link-layer frames depending on the specific type of link. 

• This is the last encapsulation, frames are converted into signals and transferred over the link following its specification. Signals can be: 

<sup>•</sup> Electric pulses. 

<sup>•</sup> Light. 

• Radio waves. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/368ed13c0d9d967ee7c505608b80b10363ea5bffbd7a94e04eaf355c07903b2e.jpg)


In order to reach Internet, packets of this host have to cross 4/5 links (wireless and wired), 1 access point, 1 switch and 2/3 routers. 

## Link Layer

## Services

• Link layer may ofer up to 4 services: framing, link access, reliable delivery, error detection and correction. 

1. Framing: to encapsulate datagrams into link-layer frames having the upper-layer datagram as payload and specific header/tailer. The structure of the frame depends on the link-layer/physical-layer protocols. 

2. Link access: to define the rules regulating the access to the link by means of a Medium Access Control (MAC) protocol. Such rules depend on the link architecture: 

• For point-to-point links (single sender and single receiver), the MAC protocol is simple (or nonexistent). The sender can send a frame whenever the link is idle. 

<sup>•</sup> For broadcast links there is the so-called multiple access problem. Here, the MAC protocol serves to coordinate the frame transmissions of the many nodes. 

3. Reliable delivery: it guarantees that frames transmited across the link are received. 

<sup>•</sup> A link-layer reliable delivery service is often used for links that are prone to high error rates, such as a wireless link, with the goal of correcting an error locally. 

<sup>•</sup> It may produce strong overhead. Since other application/transport protocols (e.g., TCP) are reliable, this feature is not always implemented. 

4. Error detection and correction: the link-layer hardware can be afected by the bit flipping problem. Many link-layer protocols implement more sophisticated (and hardware-embedded) checking/correction strategies in addition to the ones from upper layers (e.g., TCP and IP checksums). 

<sup>•</sup> Since there is no further encapsulation, these checks basically cover the whole message. 

• Hardware-embedded checks may be a lot faster. 

## Link Layer Implementation

• In network devices (end-systems, routers, etc.) the link-layer functionalities are implemented both software-side and (mostly) hardware-side. 

<sup>•</sup> In computers (i.e., end-systems) there are network adapters called Network Interface Cards (NICs) having a specialized chip (controller) to implement link-layer functionalities. 

<sup>•</sup> These cards used to be separated from the motherboard (plug-in into PCI slots), but recently this approach is changing (LAN-on-motherboard). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/a4477b703b408085f84b68b2f9b3523008c678eb0b2b98e40fee7b8f899302df.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/06ee03ac55697bd2b434332f046057da115327a0a914a05966fb2eca6e493ecc.jpg)



NIC plugged in a motherboard


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/e53d8262d83372e283cf5e3a1e6af720b3ca0844f519254970344d6a8aa5d5fb.jpg)



Latepanda mini-PC with embedded NIC


## Link Layer Implementation

<sup>•</sup> Software: runs on the CPU and provides high-level functionalities such as addressing, interrupts/hardware management, handling of errors, encapsulation/decapsulation of datagrams. 

<sup>•</sup> At link-layer we have an additional address, the MAC address that is used to identify the NIC. 

• The datagrams must be stored into the memory to be used by the upper-level protocol. They have to be: 

<sup>•</sup> Retrieved the datagram from memory during encapsulation (sender-side). 

<sup>•</sup> Inserted the datagram into the memory during decapsulation (receiverside). 

<sup>•</sup> Hardware: works as a typical I/O device, converting the data into the signal to be transmited depending on the physical protocol (e.g., ethernet, wireless, etc.). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/a699f63414080c26d73ad11764fe97a2657b0fdc97b084ba9fb91267f9fce804.jpg)


## Link Layer Physical Technologies

• The link-layer protocol, hence the resulting frame structure, depends on the technology of the physical link (physical layer). 

## • Here some common technologies:

• Ethernet 802.3: wired connection based on electric pulses over 4 twisted-pairs copper cables (most common) or photons over optic fiber cables. 

• WiFi 802.11: wireless connection based on radiofrequency (2.4GHz, 5GHz, 6GHz). 

• Bluetooth: wireless connection based on radiofrequency (2.4GHz). 

Twisted-pairs 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/088ab2c36b976b32e9b0486bd6df6a5d55cc3b7f79b83dc0c5843df19c2ccb26.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/53f9ac9e5af6447b8a9c62520151e78af03db605c14c3d394b234c0b63645603.jpg)



WiFi extender


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/d6a58e054ae6a55877dab486092244906a619f9fdb4cb44a33a12d8809ad9771.jpg)



Bluetooth Adapter


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/ada7b1d079a16fc548060578a003f56c6df1928dadddcb5dc5a2c85febe999dc.jpg)



Optic Fiber


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/52958ebd6e0c2c92cde98231c84ae10284afbdd39e640d0e3401b147b0a88df3.jpg)


## Link Layer Physical Technologies

• Physical technologies are continuously evolving, their boundaries in term of distance/bandwidth are often updated. 

• Diferent technologies have diferent pros and cons. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/52e15dbdce19bd5b6249ac454d163063f9fc620563ced909baa21884d071245a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/0ba5b5b41b41c2b4613cac5a90b0e3a29639d3d78bc5227edc46f89ac70a2705.jpg)



WiFi extender


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/bef1e88094c4af21bd286b08d96183004e7fc3f9b8607f5f4d9b2a999ef037e7.jpg)



Bluetooth Adapter


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/9a4c493847cb46628273fbbd56719345d45389563c8d5e93284a759caac6b8a4.jpg)



Optic Fiber


<table><tr><td>Type</td><td>Signal</td><td>Distance</td><td>Bandwidth</td></tr><tr><td>Wireless</td><td>Radio</td><td>30-50 m</td><td>1.3 Gbps</td></tr><tr><td>Twisted pair copper cables</td><td>Electricity</td><td>30-100 m</td><td>1-25 Gbps</td></tr><tr><td>Fiber-optic cable</td><td>Light</td><td>100-200 km</td><td>1-400+ Gbps</td></tr></table>

## Frames (recall)

The Data Link layer accepts packets from the network layer, and encapsulates them into frames that it sends using the physical layer; reception is the opposite process 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/00f439d8840c26e30bc0ae642ba240b1e09f5dca4e422bf656198dcb634e129e.jpg)


## Framing methods Logical/physical

<sup>●</sup>Byte count 

<sup>●</sup>Flag bytes with byte stuffing 

<sup>●</sup>Flag bits with bit stuffing 

<sup>●</sup>Physical layer coding violations 

<sup></sup>Use non-data symbol to indicate frame 

## Byte count (never used)

Each frame begins with a count of the number of bytes in it Simple, but difficult to resynchronize after an error 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/12a4dc3adcf11afe218f41272b676c8157872d898dfca3bf390c303c3b0df575.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/ae763d143b4286cd2cc63fedbbb40b4e225ce53e124a7f03ab16ff334e1a6a51.jpg)


## Byte stufing

<sup>●</sup>A special flag byte delimits frames; occurrences of flags in the data must be stuffed (escaped) 

<sup>●</sup>Longer, but easy to resynchronize after error 

Frame format 

Examples 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/07cefc1fbe55d2b9ae3ccac01e7c5be073ee539812a8a2e42c80781c9fda13ef.jpg)


## Bit stufing Physical Technologies

●Frame flag has six consecutive 1s (01111110) 

●On transmit, after five 1s in the data, a 0 is added 

●On receive, a 0 after five 1s is deleted 

Data bits 011011111111111111110010 

Transmitted bits with stuffing 

01 1011111011 111011 1 1 101001 0 

Stuffed bits 

## Physical violation Relies on the physical transmission encoding

A non-data byte (or word) is used at the physical layer. 

• In fact, coding violations delimit frames. 

• No stuffing is needed (delimiter signals cannot appear in the data) 

## Link Layer

## Error Detection and Correction: Problem Formulation

<sup>•</sup> In link-layer is possible to perform bit-level error detection and correction. 

<sup>•</sup> Let’s assume D of size d being our data, to protect it against bit errors we include in the message some error detection and correction bits: EDC. 

• The goal is to find if received D’ and EDC’ difers from the original D and EDC and, if so, to possibly retrieve the initial D and EDC. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/85492f541828a11ff0f790645ae0b05f6055a3591ad1432a3487e4c9eb0a38b1.jpg)


• Note that even with the use of error-detection bits there still may be undetected bit errors (in “pathological” cases). 

## Link Layer Parity Check

<sup>•</sup> Parity check is perhaps the simplest form of error detection: we include only 1 additional parity bit to the message such that the total number of 1s among the d+1 bits of the message is even (even parity scheme) or odd (odd parity scheme). 

<table><tr><td>Message</td><td>Parity bit (even scheme)</td><td>Parity bit (odd scheme)</td></tr><tr><td>10101100</td><td>0</td><td>1</td></tr><tr><td>11010000</td><td>1</td><td>0</td></tr></table>

• The receiver need only to count the number of 1s in the received d + 1 bits. If an odd number of 1-valued bits are found with an even parity scheme (or vice versa), the receiver knows that at least one bit error has occurred. 

## Link Layer Parity Check

• Clearly this approach only works if an odd number of bit errors have occurred, but how likely is that? 

• If the probability of bit errors is small and errors can be assumed to occur independently from one bit to the next, the probability of multiple bit errors in a packet would be extremely small, but this is not the case of computer networks. 

<sup>•</sup> In practice, it has been observed that errors are often clustered together in “bursts” (not independent at all). Under burst error conditions, the probability of undetected errors using single-bit parity can approach 50 percent, so it is not really useful. 

## Link Layer Parity Check (Two-dimensional)

<sup>•</sup> A possible way to improve this approach is to use multiple parity bits. 

<sup>•</sup> The two-dimensional parity is a techniques in which message is divided into n rows and m columns, each of them having a specific parity bit. 

• Here, receiver can detect that an error occurred, and also which bit, therefore atempting a correction. 

• Two-dimensional parity can also detect (but not correct!) any combination of two errors in a packet. 

$$
\begin{array}{c c c c c c} \hline 1 & 0 & 1 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 1 & 1 & 0 & 1 \\ \hline 0 & 0 & 1 & 0 & 1 & 0 \\ \hline \end{array}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/aec2976730db99b753471d4cae65e352281440ca6dbd243f22aa7ec6aa293863.jpg)


<table><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/e7df52ad87ae563777a3ec8306403dffa1207d3b51c8244b12fb0525d47e68ce.jpg)


<table><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr></table>

## Link Layer Cyclic Redundancy Check (CRC)

• Cyclic Redundancy Check (CRC) is a widely used error detection technique. It works as follows: 

• In order to send d bits of data D the sender and the receiver agrees on a patern of r+1 bits called generator (G), having the most significant bit (leftmost) at 1. 

For a given piece of data D, the sender will choose r additional bits (CRC bits) to be appended to the message such that the message M, that is D concatenated with CRC, is modulo-2 divisible by G (remainder=0). 

<sup>•</sup> The receiver divides the message M by G. If the remainder is zero, the message is correct; otherwise, an error is assumed. 

<sup>•</sup> This operation is implemented by shifting G up to the most significant 1-bit of the message and performing a bit-wise XOR. 

## Link Layer Cyclic Redundancy Check (CRC)

<sup>•</sup> Let’s now consider a simple example of a 6-bits message D and a 3-bits CRC where: 

• d = 6 

• D = 1 0 1 1 1 0 

• On the sender-side we have to create the CRC from D and G. This CRC is atached to the message and transmited to the receiver. 

• On the receiver-side we use D, G, and the received CRC to check if the received message is intact. 

## Link Layer Cyclic Redundancy Check (CRC)

Sender-side calculation of CRC with r = 3 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/65394c54c2c343f2ff1bf920f416e1228c3bc3fb66e0469cceb8ff957ba395ff.jpg)


## Link Layer Cyclic Redundancy Check (CRC)

Sender-side calculation of CRC with r = 3 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/a44f266e971756c1155895e513b781cfa9c134637e276d1e955b5d74ef6acd05.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8e2c7af2-3586-46e4-b828-b9b5a8d3781c/d03a1f311c143bc8e8812d5c5b8718960c27898a5de39b66dbaed2047bb00d03.jpg)



The remainder is 0 so the message is intact!


## Link Layer Cyclic Redundancy Check (CRC)

• International standards have been defined for 8-, 12-, 16-, and 32-bit generators (i.e., $\scriptstyle \ r = 8 , \ r = 1 2 , \ r = 1 6 , \ r = 3 2 )$ 

<sup>•</sup> The CRC-32 32-bit standard, which has been adopted in several link-level IEEE protocols, uses the following generator (33 bits): 

$$
G _ {C R C - 3 2} = 1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1
$$

• Each of the CRC standards can detect for sure burst errors of less than r + 1 bits, while for error greater than r + 1 there is a probability P of finding the error which is: 

$$
P = 1 - 0. 5 ^ {r}
$$

• Therefore, the probability of finding the error increases with r. 

## Hamming distance Error correction code

Code turns data of n bits into codewords of n+k bits 

The Hamming distance is the minimum bit flips to turn one valid codeword into any other valid one. 

Example with 4 codewords of 10 bits (n=2, k=8): 0000000000, 0000011111, 1111100000, and 1111111111 The Hamming distance is 5 

Bounds for a code with distance: 

2d+1 – can correct d errors (e.g., 2 errors above) 

d+1 – can detect d errors (e.g., 4 errors above) 

Hamming codes are based on this principle (but are more complicated) 