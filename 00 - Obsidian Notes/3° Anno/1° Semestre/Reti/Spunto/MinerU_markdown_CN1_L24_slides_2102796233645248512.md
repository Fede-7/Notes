## The Link Layer: MAC sublayer, Random Access Procols, Collision-Free Protocols, Switches, ARP

Lecture 24 

## Link Layer Random Access Protocols: CSMA

• Because of the delay in the signal transmission! 

<sup>•</sup> Even if the propagation of signals in the channel is typically near the speed of light, it takes time to reach all other nodes. Therefore, a second node detect the transmission only after it has started. 

<sup>•</sup> Because of this delay between transmission start and detection, a node may consider as free a channel that is actually in use, producing a collision. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/7dd54ac865179318ca85d9f6da2a69bb3418c5705bb727807ab17376bce01e78.jpg)


## Link Layer Random Access Protocols: CSMA

<sup>•</sup> The pure CSMA is very simple: 

1. Check if the channel is busy. 

2. If channel is idle, send a frame. 

• In pure CSMA collisions are not detected but are still possible. We understand that a frame is lost just because the ACK is not received. 

## • The CSMA/CD is more sophisticated (currently implemented on Ethernet):

1. Check if the channel is busy. 

2. If channel is idle, send a frame. 

3. While transmiting, check for possible collisions. 

4. If collision is detected, stop transmiting and wait for a random period $K \in \{ 0 , . . . , 2 ^ { n _ { - } } 1 \}$ where n is the number of detected collisions on the current frame (binary exponential backoff). 

• The probability of successfully sending the frame increases with the number of collisions. 

## Link Layer Taking-turns

• Polling protocol: there is one master node that selects in a round-robin way one node per time allowed to transmit (up to the max throughput). This process is iterated every time transmission stops (e.g., Bluetooth). 

• There are no collisions. 

• There is a polling delay (time to select nodes). 

<sup>•</sup> The approach is centralized, there is a single-point-of-failure. 

• Token-passing protocol: there is no master node, nodes exchange a special frame called token, if a node receive the token it is allowed to transmit, then the token is passed to another node. 

• There are no collisions. 

<sup>•</sup> The approach is decentralized. 

• There are problems if some node forgets to release the token (monopolizing the link). 

## Link Layer MAC Addresses

• At the link-layer, devices are identified by MAC addresses: 

• Each network interface has a specific MAC address (it was designed to be fixed but it can be changed). 

• Each manufacturer has its own set of MAC addresses. 

• The MAC address (or physical address) is a link-layer address composed by 6 bytes (2^48 possible addresses) often represented in hexadecimal notation: 

1A:23:F9:CD:06:9B or 1A-23-F9-CD-06-9B 

• MAC addresses are local (while IPs outside LANs are global): 

<sup>•</sup> All interfaces are associated to a MAC address, but this is only used inside a LAN. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/081abb457364fe46301fadd8e1a6eff71e176b57f3d109e3a5b4313c5cde9fa8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/a4e7987bc903907cc581c53a4bfae846c3ef966efdf80011bd760078cf02d47b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/bfb6b3b1f89152bf65632e0cf6fc57db10133c57977bd87306a69a12b6786bb9.jpg)


## Link Layer MAC Addresses

• In a LAN, 2 interfaces (A and B) communicate as follows: 

• A includes B’s MAC address into the frame and transmits it. 

• B receives the frame and compares its own MAC with the destination MAC of the frame. 

• If the 2 MACs are equal, the frame is accepted, otherwise the frame is rejected (the rest of the stack is not involved). 

<sup>•</sup> There is also the possibility to send broadcast messages (that are accepted regardless of the MAC), for LANs that use 6-byte addresses (such as Ethernet and 802.11), the broadcast address is a string of 48 consecutive 1s (that is, FF-FF-FF-FF-FF-FF in hexadecimal notation). 

<sup>•</sup> In a LAN it is quite possible (if not frequent) for an interface to receive frames directed to another interface, the role of the MAC address is to filter out unintended frames without disturbing the host. 

## Link Layer

## Switches

## • Switches are the link-layer equivalent of the routers:

• There is no routing algorithm implemented. 

• Only MAC addresses are used. IP addresses are not. 

• The role of the switch is to receive incoming linklayer frames and forward them onto outgoing links: 

• The switch is transparent to the hosts and routers in the subnet. 

• A switch also has bufers on interfaces. 

## • Switches have forwarding tables that associate MAC addresses to interfaces.

• The table is updated automatically and dynamically (selflearning) as new devices are discovered. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/b1ce9627449ce729c5c4c8e23b936af7503972b27505652960a17c9c31ab648c.jpg)


## Link Layer Switched LAN

• It is usual for LANs to use one or more switches connecting multiple local devices. 

<sup>•</sup> Diferently from routers, switches are fast and plug-and-play: 

<sup>•</sup> There is no routing algorithm involved. 

• Only 2 layers of the stack are considered. 

• On the other hand, switched LANs are limited in size and must be tree-structured: 

• MAC addresses are hard to group (forwarding tables in switches may grow rapidly). 

• There is no routing. Loops are dificult to avoid. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/09d0b4189c1c7990c5b48ab9c2f63d3010a5e4c319367de41f2bbcbe48791316.jpg)


## Link Layer

## ARP

<sup>•</sup> Since upper-layer protocol works with IP addresses w need to translate IP into MAC. 

• The Address Resolution Protocol (ARP) manages conversion between IP and MAC addresses. 

• Each interface is endowed with an ARP module having an ARP table that associates each IP in the LAN to a MAC address with a specific time to live (TTL) value after which the entry is delated (typically 5-20 minutes). 

• Since MAC addresses are local, also ARP works only on local networks (LANs). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/5e9f14bb646353f2a500ceb5750e8a5e33b015663ff6a0e1e0c9987143432e29.jpg)


<table><tr><td>IP Address</td><td>MAC Address</td><td>TTL</td></tr><tr><td>222.222.222.221</td><td>88-B2-2F-54-1A-0F</td><td>13:45:00</td></tr><tr><td>222.222.222.223</td><td>5C-66-AB-90-75-B1</td><td>13:52:00</td></tr></table>

## Link Layer ARP: Example

• Assume that host C (222.222.222.220) wants to send messages to host A (222.222.222.222). To do so, we need to know also the associated MAC: 

• Before to send the message, if A is not present into the table an “ARP request” packet is sent in broadcast to all devices of the network searching for the right IP. 

• All nodes receive this packet but only the searched IP (222.222.222.222) answers with a direct “ARP reply” message (unicast). 

<sup>•</sup> A malevolent host may intercept the message, sending back a “forged” reply (ARP poisoning). 

<sup>•</sup> ARP poisoning is one of the most common atacks on LANs. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/2b8a805a300b01de6be1bd261d10e3e7e9bcdf6359a5c56c06b7109d0b3b7e00.jpg)


<table><tr><td>IP Address</td><td>MAC Address</td><td>TTL</td></tr><tr><td>222.222.222.221</td><td>88-B2-2F-54-1A-0F</td><td>13:45:00</td></tr><tr><td>222.222.222.223</td><td>5C-66-AB-90-75-B1</td><td>13:52:00</td></tr></table>

## Link Layer ARP: Gateway

• What happens if the IP is outside the network (non-local)? 

• The router connecting the 2 networks must have at least 2 interfaces (2 IP, MAC and ARP tables) each one inside the specific subnets. 

• Frames headed outside the subnet are sent to the first interface of the router, moved to the second interface, and headed toward the right host by using the second ARP table. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/9c4cb1c64b094d021a902d13b0ffc25983bb6ffc83ef392ea6d00e7d5a39bd91.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/6cac67df-a909-49ab-b06c-7ebae018c91c/73e8068fd8cdc83f3e101d7d3d791dd8508ef4534a4420d619217219fe7ab28a.jpg)


<sup>•</sup> Ethernet frame is composed by the following fields: 

<sup>•</sup> Data field (46 to 1500 bytes): contains the IP datagram. The maximum limit is given by the maximum transmission unit (MTU) of Ethernet, if datagram exceeds this size it is fragmented. 

• Destination address (6 bytes): contains the MAC address of the destination adapter. 

• Source address (6 bytes): contains the MAC address of the source adapter that transmits the frame onto the LAN. 

• Type field (2 bytes): specifies the network-layer protocol used for in this frame (there could be alternative to IP, for example, ARP packets have a specific type - 0x0806). 

• CRC (4 bytes): contains the CRC number. 

• Preamble (8 bytes): is a “wake up” block of bits used to synchronize the clocks of destination and source adapters. 