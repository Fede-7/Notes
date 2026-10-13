## Computer Networks I Reti di Calcolatori I

## The Network Layer

Lecture 15 

## Network Layer From Transport to Network

<sup>•</sup> The job of the network layer is mainly to allow remote hosts to communicate: 

<sup>•</sup> At the sending host: to take segments from the transport layer, to encapsulate each segment into a datagram, and to send the datagrams into the network. 

<sup>•</sup> At the receiving host: to receive the datagrams from the network, extracts the transport-layer segments from datagrams, and delivers the segments up to the transport layer. 

<sup>•</sup> At this level, some of the most important protocols of computer networks works: 

• IP, DHCP, NAT, etc. 

• There are special devices (routers) that works at this level. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/b77a317c552d1b0022f3bda0db533a1a524801dbde5146266471290e6b046840.jpg)


## Network Layer From Transport to Network

• Inside the network there are nodes that forward datagrams to the adjacent nodes (routers) up to the destination host. 

• The routers are shown with a truncated protocol stack. Potentially routers do not run applications nor transport-layer protocols. 

<sup>•</sup> The act of a datagram being redirected by a router is also called hop. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/27fbaf0ccfa86b6f783560081ebd1949b3fa36100c63dc877aa3dc6e8d4ae418.jpg)


## Network Layer Network Layer in Internet

<sup>•</sup> The network layer is mainly responsible for host-to-host delivery. 

<sup>•</sup> What services could be ofered along with delivery: 

<sup>•</sup> Guaranteed delivery: a packet sent by a source host will eventually arrive at the destination host. 

<sup>•</sup> Guaranteed delivery with bounded delay: packets will be delivered and within a specified host-to-host delay bound (for example, within 100 msec). 

<sup>•</sup> In-order packet delivery: packets will arrive at the destination in the order that they were sent. 

<sup>•</sup> Guaranteed minimal bandwidth: possibility to specify a minimal bit rate (for example, 1 Mbps) such that, if the rate of the sending host is within it, then all packets are eventually delivered to the destination host. 

<sup>•</sup> Security: encryption/decryption of all datagrams at the source/destination. 

<sup>•</sup> Actually, none of these services is generally ofered by networks. 

## Network Layer Network Layer in Internet

<sup>•</sup> Conversely, Internet’s network layer provides just one service, the so called best-efort service. 

• Best-efort service (or best-efort delivery): the network tries its best to deliver a packet from its source to its destination. 

<sup>•</sup> Packets are neither guaranteed to be received in the order in which they were sent, nor to be received at all. 

<sup>•</sup> There is no guarantee about delays or minimal bandwidth. 

<sup>•</sup> Despite its simplicity, the best-efort service model, in combination with good bandwidth have proven to be adequate. 

<sup>•</sup> For example, applications, such as Netflix and voice-and-video-over-IP, real-time conferencing, Matrix, etc. all works with it. 

## Network Layer Routers in the Network

<sup>•</sup> The primary role of the network layer is to perform host-to-host delivery, i.e., to move packets from a sending host to a receiving host. 

• This process is performed by routers (network nodes) that are special nodes having multiple incoming/outgoing links. Routers provide two network-layer functions: 

Forwarding: when a packet arrives at a router’s input link, the router must move the packet to the appropriate output link. It is also possible to: 

a. Block a packet from exiting a router (e.g., if originated from a known malicious host, or destined to a forbidden host). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/72cf60e05962c448bccdfc543236e7d47003345b839eef8085ec5b954e723db2.jpg)


b. Drop a packet if it is expired. 

c. Duplicate a packet and sent it over multiple outgoing links. 

d. Modify a packet (e.g., to notify congestion, etc.). 

<sup>•</sup> Routing: to decide the route or path to be taken by packets as they flow from a sender to a receiver. The algorithms that calculate these paths are referred to as routing algorithms. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/668def0913d091240fd010e72bb63f51625a88a8c7404f24b0e0ee0180930514.jpg)


## Network Layer

## Routers

## <sup>•</sup> Routers may be very diferent depending on the usage/technology:

<sup>•</sup> Home or business usage. 

• Wireless or wired connections. 

<sup>•</sup> One important distinction is between edge and core routers: 

• Edge routers: a router that distributes data packets between one or more networks (e.g., connecting a network with the ISP). 

<sup>•</sup> This is the most common typology. 

<sup>•</sup> Core routers: used to distribute packets within the same network rather than across multiple networks. 

• These are also used on the backbone of the Internet and its job is to carry out heavy data transfers. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/0f666ab9a8689af5cf0b8ff24c19226ff7707fd8a8656f34e42ac90dc8e9e339.jpg)



Cisco RV016-G5 business router


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/c3808d997aad6c67ead56f1b87729a3a50025452931a5e79b16ee0989fc6e772.jpg)



Juniper MX2020, edge router


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/076f22a2f6263c72fd91496a680eae6c6af274dd8d0cc22656f3fad040cf7bc6.jpg)



Tp-link AX6600 home router


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/c2c44ce9df0fd1871d69691d7da2e607e6f819184373be7f2f0658a5390e6451.jpg)



Cisco CRS-1 backbone core router


## Network Layer Routers: Data and Control Planes

• The job of routers is typically implemented as a two-step (or two-plane) process: 

<sup>•</sup> Forwarding (data or forwarding plane) refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface. 

<sup>•</sup> This is a fast operation (typically a few nanoseconds), and thus is typically implemented in hardware. 

• Routing (control plane) refers to the network-wide process that determines the end-toend paths that packets take from source to destination. 

<sup>•</sup> This is a slower process (typically seconds), and it is often implemented via software. 

<sup>•</sup> At the data plane we have the forwarding table: a table that associates output links with possible destination addresses. 

<sup>•</sup> A router forwards a packet by examining the value of one or more fields in the packet’s header. 

• The value stored in the forwarding table indicates the outgoing link interface to which that packet is to be forwarded. 

## Network Layer Routers: Data and Control Planes

<sup>•</sup> Since multiple routers can be encountered before to reach a destination, the content of a forwarding table must be determined by collecting information from diferent routers. 

<sup>•</sup> This process is implemented using one or more routing tables (control plane) that eventually lead to the creation of the forwarding table (data plane). 

<sup>•</sup> Creation of routing and (eventually) forwarding tables can be performed in two ways: 

• Decentralised (or distributed): we can have each router endowed with a routing component that communicates with the routing component of other routers (this was the mainstream approach). 

<sup>•</sup> Centralised: we can have a physically separated (from the routers) remote controller computes that distributes the forwarding tables to be used by routers. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/f01c4369f418171c277b70672fc139228e4e017a5503f80fcc8fd92d861b0e1b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/18d19adce981ea4775fc685399b3ca3bb1480deb0c04d1a545fb328eee1ab121.jpg)


## Network Layer Routers: Data and Control Planes

<sup>•</sup> In the centralised case, the remote controller might be implemented in a remote data center (with high reliability and redundancy) and might be managed by the ISP or some third party. 

• This approach is at the basis of software-defined networking (SDN), where the network is “software-defined” because the controller that computes forwarding tables and interacts with routers is a centralized software. 

<sup>•</sup> Some of these software are also open. 

## Network Layer Routers: Main Components

## • A router’s main components are:

• Input ports (diferent from transport-layer ports): are the physical input interfaces that operate with the lower linklayer of the connected link, their job is: 

• To consult the forwarding table (aka lookup) and to prepare the switching fabric for the output port to choose. 

<sup>•</sup> To forward control packets (e.g., packets carrying routing information) to the routing processor. 

• The number of input ports may range from dozens to hundreds (e.g., the Juniper MX2020 edge router supports up to 960 of 10 Gbps Ethernet ports). 

<sup>•</sup> Switching fabric: connects input ports to its output ports. 

<sup>•</sup> Output ports: store packets received from the switching fabric and transmits these packets on the outgoing link. 

<sup>•</sup> Ports may be bidirectional (i.e., input/output ports are coupled). 

<sup>•</sup> Routing processor: executes the routing protocols, maintains state-information about links, and computes/updates the forwarding table. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/3260054f63d0dc9e5a438b979ccced666268c050c1196071b76c2c90f6bd6948.jpg)


## Network Layer Routers: Forwarding

• The role of the forwarding table is to associate IP addresses to output ports, so that packets can be forwarded to the right output link in order to be transmited to the next node (and possibly be forwarded again). 

• An IP address is a 4-bytes (32-bits) number that we usually see in decimal notation, but we can also see it in its binary form: 

192.168.1.1 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/fefeeec1a23af0e85597dc8e8f2e1561941535c3e87d18a068efd95b6596f952.jpg)


11000000 10101000 00000001 00000001 

• Inside a forwarding table, IPs are associated to output port numbers for actual redirection. 

## Network Layer Routers: Forwarding

<sup>•</sup> When a packet is received from the link into an input port a lookup operation is performed. 

• Each port has a copy of the forwarding table from the routing processor (received on a dedicated bus, e.g., a PCI bus) to avoid botleneck due to continuous invoking of the centralized routing processor on a per-packet basis. 

• Multiple addresses may be associated to the same port. 

<table><tr><td>Prefix of IP addresses</td><td>Link Interface</td></tr><tr><td>11001000 00010111 00010*** *******</td><td>0</td></tr><tr><td>11001000 00010111 00011000 *******</td><td>1</td></tr><tr><td>11001000 00010111 00011*** *******</td><td>2</td></tr><tr><td>otherwise</td><td>3</td></tr></table>

## Network Layer Routers: Forwarding

<sup>•</sup> Notice that entries may not be mutually exclusive (for example, IP 11001000 00010111 00011000 10101010 matches links 1 and 2) if so, the router forwards it to the longest matching entry (longest prefix matching rule): 

Match with Link 1 = 24 bits 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/d02c43df8eaf4f568e0287c479be17dba21f296da70ec4f3debd98851389b199.jpg)


Match with Link 2 = 21 bits 

## Network Layer Routers: Forwarding

• This lookup procedure is typically performed on the hardware to be executed as fast as possible (e.g., in nanoseconds for Gigabit transmissions). 

<sup>•</sup> Embedded memories and advanced table-search algorithms are also involved. 

<sup>•</sup> Once a packet’s output port has been determined (after lookup), the packet can be sent into the switching fabric. In some devices, packets may also be temporarily queued (bufered) if other input ports are using the fabric. 

• This two-steps operation of looking up a destination IP address (match) and forwarding (action) is called match-plus-action and is performed in many networked devices, such as: 

• Switches: similar action as routers. 

• Firewalls: where the action is to filter out specific incoming packets. 

• Network address translators (NATs): where the action is to rewrite port number of specific incoming packets before forwarding. 

## Network Layer Routers: Switching Fabric

<sup>•</sup> In a switching fabric, switching can be performed in 3 ways: 

1. Switching via memory: ports are considered as I/O devices that write packets on memory cells then the routing process copies the message on the output port as specified by the forwarding table. 

<sup>•</sup> This approach is a bit slow (need for memory access) and was more common in early routers (which were standard computers). 

2. Switching via a bus: input port transfers a packet directly to the output port over a shared bus, without intervention by the routing processor. 

<sup>•</sup> Only one port per time can be served, but this method is often suficient for routers that operate in small local area. 

3. Switching via an interconnection network: input/output ports connected by a network having cross-points which can be open/close and then redirect the packets. 

<sup>•</sup> Here multiple packets can be forwarded in parallel. This method is used in several modern routers. 

## Memory

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/0c23e964300c355652aaa51da65d758a5df6ae9eebdb1f42dd6ad11e6c5e577a.jpg)



Bus


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/8881b8d1f054cbce6a10fa8bbbd2d2350fb639b215284815600e0cfb43a72864.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/549908f83aab160a03587dad7cf3dcef7347bfd590f31aee00632a29e3a66f4c.jpg)


## Network Layer Routers: Ports

<sup>•</sup> Since switching takes time, input and output ports have queues to temporarily store packets (as cars waiting for semaphores). 

• The extent of queueing is not fixed, it may depend on trafic load, the speed of the switching fabric, or the line speed. 

• In general, packets may be received/sent faster/slower than switching, so they may be accumulating into the input/output bufer (that may overflow). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/b651c9e8be30f1369ebc062490a6f9f1f79d5ffdf7192ec1de70c3cfc1b64fd6.jpg)


## Network Layer

## Routers: Ports

• Example: let’s assume to have (1) a router with N input and N output ports, (2) that each port is receiving packets at the same time, and (3) that all input and output lines have the same speed Rline packets per second. 

• Let’s now consider a worst-case scenario in which all packets have to be forwarded to the same port. 

If the switching fabric have a rate (Rswitch) we have: 

<sup>•</sup> If Rswitch ≅ N Rline, queuing on input ports is negligible as all packets are forwarded in time by the forward fabric, but queuing on the output port is significant as the incoming packets are N time more than the rate of the output link. 

<sup>•</sup> if Rline < Rswitch < N Rline, there is queuing on both ports as input port must wait for the switch fabric while output port must wait for the link. 

<sup>•</sup> if Rswitch ≅ Rline, there is negligible queueing on output port but significant queuing on the input ports. 

# Network Layer Routers: Packet Scheduling

<sup>•</sup> It is reasonable to have multiple packets (potentially from multiple input ports) to be forwarded to a single output port. 

<sup>•</sup> The access of queued packets from bufer to the output link needs to be scheduled. 

<sup>•</sup> There are basically 3 (famous) approaches: 

• First-come-first-served (FCFS, aka first-in-first-out, FIFO), which is simple time-based approach. 

• Priority queuing, which is based on the importance of the packets. 

• Round-robin queueing, where packets are divided into classes (based on priority) and each class is served in turn. 

## Network Layer Routers: Packet Scheduling - FIFO

• If the output link is busy (transmiting something) the packets arriving at the output port must be bufered. 

• If there is no suficient bufering space to hold the arriving packet, we must rely on a packet-discarding policy. 

• A typical policy is to drop the recently arrived packets (drop-tail) but in more sophisticated approaches also already bufered packets can be removed to make space for the arriving ones. 

<sup>•</sup> A packet is removed from the queue only if it has been completely transmited over the outgoing link (served). 

<sup>•</sup> In FIFO scheduling packets are selected for transmission in the same order in which they have arrived at the output port. 

Switch Fabric 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/1bd28b7e11ff4231223024813656fa8de27d227b07434b81fb8d18d24c63ced4.jpg)


Output Port 

## Output Bufer

Output Link 

## Network Layer Routers: Packet Scheduling - Priority

• In priority queuing, packets arriving at the output link are classified (e.g., through TCP/UDP port numbers) into priority classes upon arrival at the queue. 

• A network operator may configure a queue so that specific packets (e.g., carrying network management information, real-time voice-over-IP, etc.) may receive priority over user trafic or non-real-time packets. 

## • Each priority class may have its own queue:

<sup>•</sup> Packets from the most prioritized non-empty class are transmited first. 

<sup>•</sup> The choice among packets in the same priority class is typically done in a FIFO manner. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/1ee593c3a989f60b538476f2665ccb937f3a7838ddf7bfaff17e77fcf8505f44.jpg)


## Network Layer Routers: Packet Scheduling – Round-robin

• In round robin queuing, packets are still sorted into classes, but classes are alternated rather than selected by priority. 

<sup>•</sup> A common implementation is called weighted fair queuing (WFQ) where arriving packets are classified and queued in the appropriate waiting area. 

<sup>•</sup> Each class is then associated to a specific weight that dictates the rate with which the class is selected over the others. 

Switch Fabric 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/141a6658-95b7-4f64-bbb1-9a52865e8320/6a4c57e890cb149bf17d830f7c1a4a99fb34bbd5e7ba85a9536e978065dd000b.jpg)


Output Port 