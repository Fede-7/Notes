## Introduction to Computer Networks

Lecture 1 

## Overview

## Syllabus

<sup>•</sup> Introduction to computer networks: goals and applications, main notions, network topologies and types, services (ISPs, grid, cloud, IoT), standards (layered models, IOS/OSI and reference models, protocols). 

<sup>•</sup> Application layer: client-server ad peer-to-peer architectures, FTP and SSH protocols (basis), structure of URL, HTTP protocol, mailing protocols (STMP, POP3, IMAP), DNS, BitTorrent protocol. 

<sup>•</sup> Transport layer: fundamentals, UDP protocol, reliable data transfer, TCP protocol. 

<sup>•</sup> Network layer: fundamentals, routers, IPv4 protocol, DHCP, NAT, IPv6, families of routing algorithms. 

<sup>•</sup> Access layer (data link + physical): network interfaces, parity check and CRC, collisions, ARP protocol, Ethernet protocol (basis). 

<sup>•</sup> Introduction to network security: atacks on networks, introduction to cryptography, message integrity, AP and TLS/SSL, operational security (firewall, IDS). 

<sup>•</sup> Network programming: UDP and TCP sockets, REST applications, data exchange formats. 

## Uses of computer networks

## Computer network

<sup>●</sup> Large number of separate but interconnected computers do a job 

<sup>●</sup> Collection of interconnected, autonomous computing devices 

<sup>●</sup> Interconnected computers can exchange information 

## Example: the Internet

## Network uses

● Access to information 

<sup>●</sup> Person-to-person communication 

● Electronic commerce 

● Entertainment 

<sup>●</sup> The Internet of Things 

## Access to Information

![image|603x288](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/5082de50c2d27439252d83bc951ec6a97534753c5ee1aead893dbe97a0c8a062.jpg)



In the client-server model, a client explicitly requests information from a server that hosts that information.


## Access to information Client-server

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/cee04c13de250e1be1affc2b299aa4223dcc1459f42a9755c134a92a08bbdd91.jpg)


Communication takes the form of the client process sending a message over the network to the server process. The client process then waits for a reply message. 

## Access to information

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/63a296e72fbc78fb4612c55dcd58b1f568ed0c9a8170210f871b67ea673c11ba.jpg)


In a peer-to-peer system, there are no fixed clients and servers. 

## Introduction Computer Networks and Internet

Computer networking: the process of connecting computer together so that they can share information. 

[Cambridge Dictionary] 

<sup>•</sup> Internet (the most important computer network in the world) 

• The Internet includes hundreds of millions of network devices, links, computers, etc. ofering hundreds of services for the users. 

• There are also smaller networks (local or detached from internet). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/3c4625c4df3358f9b730a7fd6de6f53d987ae347adc97c3ff4661cb8a4d25ec7.jpg)


## Introduction History of Internet

<sup>•</sup> The Internet is the largest computer network, connecting devices all around the globe. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/617a72b2ac9d769b35f862800ecdf430707bd3182cbbf135f477a38c84d68d6b.jpg)


Internet is a network of networks. It is technically a huge Wide Area Network (WAN) that allows sub-networks and devices to be connected over diferent nations and continents. 

The idea of such “universal” big network was initially theorized by researchers (most notably J.C.R. Licklider) around 1950 and started to become reality almost 10 years later. 

## Introduction History of Internet

<sup>•</sup> The Internet is the largest computer network, connecting devices all around the globe. 

## <sup>•</sup> Brief history of Internet:

• The Advanced Research Projects Agency (ARPA) of the U.S. Department of Defense awarded contracts for the development of the ARPANET project (1969). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/7f840c74846a8dc0d5675d0347cb236be2c9c7541b1e6e99c23e9ae6d0f8f4aa.jpg)



Initial ARPANET having 3+1 nodes: SRI, UCLA, UCSB, and UTAH (1969)


The initial ARPANET was mainly a closed network designed to include universities and research centers. Similar networks were independently created all around US and Europe. 

## Introduction History of Internet

<sup>•</sup> The Internet is the largest computer network, connecting devices all around the globe. 

## <sup>•</sup> Brief history of Internet:

• The Advanced Research Projects Agency (ARPA) of the U.S. Department of Defense awarded contracts for the development of the ARPANET project (1969). 

• R. Kahn (ARPA) and V. Cerf (Stanford) designed the Transmission Control Protocol (TCP) and Internet Protocol (IP), two protocols of the Internet protocol suite (1974). 

• The National Science Foundation (NSF) awarded contracts for the NSFNET project, a TCP-IP based network (1986). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/e0f532223db8ecca055f38a61e9dda14173a997cba20d5479a550d6ac8f21fa4.jpg)



NSFNET in 1992 (Wikipedia).


The NSFNET and the TCP/IP protocol went toward the idea of a network of networks, but both ARPANET and NSFNET carried commercial restrictions. 

## Introduction History of Internet

## <sup>•</sup> The Internet is the largest computer network, connecting devices all around the globe.

## <sup>•</sup> Brief history of Internet:

• The Advanced Research Projects Agency (ARPA) of the U.S. Department of Defense awarded contracts for the development of the ARPANET project (1969). 

• R. Kahn (ARPA) and V. Cerf (Stanford) designed the Transmission Control Protocol (TCP) and Internet Protocol (IP), two protocols of the Internet protocol suite (1974). 

• The National Science Foundation (NSF) awarded contracts for the NSFNET project, a TCP-IP based network (1986). 

• The ARPANET decommissioned (1990). 

<sup>•</sup> The NSFNET decommissioned, removing the last restrictions on the use of the Internet for commercial trafic (1995). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/62a0ec9e2fb05617d8f45a97ab2aaefbabbaf76dde6a7ca83e868ea93abb06f8.jpg)



Graphical representation of routing paths for a portion of Internet (Wikipedia).


## Introduction Networks Components: Devices, Links, Hosts

• Network devices and links are the infrastructure that allow hosts to connect: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/a90f892a75832b42a9850b35d4cc881eaad8d9475a7d630dbda25a8981238a03.jpg)



Router


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/fb873e10a4dfb9322ac8d3dcdb50d03a3769c9ad1da2a821cc6ecbfae485143c.jpg)



Access Point


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/baf23429f1dc86896cd0a9b0082f739f67f3c270fc1b6c8eb2b07e72c0c94a5c.jpg)



Switch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/fc1f856f68160abc8b9e3930d110b7bd96529dd7b0677b33dffa4a8f90f46a52.jpg)



Hub


• Hosts are devices on which applications (or programs) runs: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/75a283f8e7a4351098079a9ca30964872e50040c8411719f88a44bd80027b5bf.jpg)



Laptop


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/b7792ffde4d8ca96978be6d4fd65b25cefc5a5afce259e620eb09c647bb08593.jpg)



Server


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/8a37111d79791341acecb084b0d1ddb9c72e314f6d67d35039598d9dc23326ab.jpg)



Smartphone


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/4165793f53d57313adcc6120bdf419303c2846678e2dde611ffcae69ad340c43.jpg)



PC


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/278bf5db4d534e7b4b6ef5a0f3aa0b6c48811c71426b640d1d0ce1d2cd1e022d.jpg)



home network



datacenter network


## Introduction Computer Networks and graphs

<sup>•</sup> Computer networks share terminologies with graph theory: 

<sup>•</sup> The devices connected through the network are called nodes while the connections between nodes are called communication links (or channels). 

• A sequence of nodes/links is called path. 

<sup>•</sup> The end-points (or end-systems) of the network, which provide or use services, are special nodes called hosts. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/4dafd5349e801c9191d65e5af99499bde6625516b94da540daaee12dfd9aa21c.jpg)


Ideally hosts are the leaves of the network (often it is not true) while intermediate nodes are routing devices (routers, switches). 

## Introduction Data Communication

<sup>•</sup> Data communication main components: 

1. Message: contains the data to be transmited. 

2. Sender: the entity which is sending the message. 

3. Receiver: the entity which is supposed to receive the message. 

4. Medium: the channel between sender and receiver where the message travels. 

5. Protocol: a set of communication rules, known to sender and receiver. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/3a826647dd045e53d4d50ab2f6d2a3dcdf0243f14775a05d0fa2b38d05493299.jpg)


## Introduction Data Representation and Flow

<sup>•</sup> The data we want to exchange can be represented in diferent forms. <sup>•</sup> Text, numbers, images, audio, video, etc. 

<sup>•</sup> Depending on the type and the purpose of the communication, the data flow can be: 

• Simplex: monodirectional. 

• Half-duplex: bidirectional (taking turns). 

• Full-duplex: bidirectional (simultaneous). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/3ed95cc529dae1463ea7e155487dde59c0923be8a7140bba6f7140800a12cbd3.jpg)



a. Simplex


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/ce4411438d93d2a1742ad93db2a4f126bf2d00c7fe653e76606b37611b2ec09a.jpg)



b. Half-duplex


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/2609aadb2bb44df81bc810700cc5321a035b6a1de97f7ae5d59e0285f103d1bd.jpg)



c. Full-duplex


## Introduction Data Representation and Flow

<sup>•</sup> Transmission rate typically refers to the maximum amount of information that a device can transmit, measured in bit/s (or byte/s). 

• The bandwidth is the maximum amount of information that a path (links + nodes) can transmit, measured in bit/s (or byte/s). 

• The throughput is the actual (instantaneous) amount of information that is being transmited over a path, measured in bit/s (or byte/s). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/b1fde6201b496b58392f6a068dc72f0ff41e6962d7b091250514fecdc5ca4e52.jpg)


## Introduction Types of Connections

<sup>•</sup> The hosts of a network can be connected in diferent ways. 

• Point-to-point: a dedicated link is provided between two devices (wireless or wired). 

• Multipoint (broadcast): more than two specific devices share a single link (wireless or wired). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/568ae23276d667bd6fed8a05d1abe0f7e5269036edcbbaac0078b66a49887036.jpg)


## Introduction Network Topologies

<sup>•</sup> There are diferent ways of connecting devices. 

• The network topology is the arrangement of the elements (links, nodes, etc.) of a communication network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/4ed373b4aeca1802a0cde76220c4ed919357b40af65f6aa49eac9968e7d39816.jpg)



Ring


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/f73a1b5dcc154d91bbcf4522bb3737ef527b53943bd3b27e967f67d48fd3c7d5.jpg)



Mesh


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/b05645362d63e457123eb98ed9c0e5040105e6c964d5bec033b393364416a1d6.jpg)



Star


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/165205783225e040df716eb6308d0b2d0c7309a07da8f6dc85766b1a9ada923d.jpg)



Fully Connected


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/02ec0b22bc8909977dc4ee07b41cd76c525939ec0f6ade9824e43162b4493d2a.jpg)



Line


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/828c9fb17b8489ad8bd1ea999c1f163728b615297b357ac79238f27bd88db930.jpg)



Tree


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/a43d30de636d138bbb944098aa9613a1e2b96f6ee6b52117360f8777dc997c70.jpg)



Bus


## Introduction Network Topologies: Bus

<sup>•</sup> In the Bus topology hosts are connected to a central backbone (bus) cable. <sup>•</sup> Collisions are possible. 

## • Pros:

<sup>•</sup> Simple and cheap. 

• Good for small networks. 

## • Cons:

• Single point of failure (broken bus) but sub networks may still be available. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/f663a3d2e05b7b24df10c7ff6ccd896f0218cfc83103fe90f752574f50cd3560.jpg)



Bus networks have 1 physical duplex link (or 1 backbone and n links).


## Introduction Network Topologies: Ring

<sup>•</sup> In the Ring topology hosts are point-to-point connected to exactly two other ones. The signal is forwarded along the ring, from device to device, until it reaches its destination. 

• Pros: 

<sup>•</sup> Simple and cheap. 

• Performs beter than the bus. 

## • Cons:

<sup>•</sup> Adding new nodes is harder. 

<sup>•</sup> Nodes malfunctioning may impair the network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/b05286763145624a5397d3c712bb29eb5d190b81c2a3895f1b7c89bdb634f79d.jpg)



Ring networks have n duplex links.


## Introduction Network Topologies: Star

<sup>•</sup> In the Star topology hosts are linked to a central controller (hub, switch or router), there is no direct link between hosts. 

<sup>•</sup> The central controller redirects messages. 

• Pros: 

<sup>•</sup> Less expensive, simple, robust, more scalable. 

• Cons: 

<sup>•</sup> The controller must be reachable by all hosts. 

<sup>•</sup> Single point of failure. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/02851f7cc0299ac140f398803b8910e64eacc49f3729258366c436bf24c22264.jpg)


Star networks have 1 controller and n physical duplex links! 

## Introduction Network Topologies: Tree

<sup>•</sup> In the Tree topology multiple star topologies are integrated typically through a bus cable. 

## • Pros:

• Versatile, scalable, robust. 

<sup>•</sup> Well supported by HW and SW providers. 

## • Cons:

<sup>•</sup> Hard to configure. 

• Weakness of the bus. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/612b32f4debc89e440305d5bc590db9e016e5b6017caada3f54d383b65218bd3.jpg)


## Introduction Network Topologies: Mesh

<sup>•</sup> In the Mesh topology hosts are point-to-point linked in a non-hierarchical way. 

• Full mesh: all nodes connected (full-connected). 

• Partial mesh: nodes connected with some others. 

## • Pros:

• Low trafic, robust, secure, dedicated. 

• Cons: 

<sup>•</sup> Hardly scalable. 

<sup>•</sup> Expansive (need for devices with multiple ports). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/4eb5866eac71a3735a512b99001f6bfa9c3dc82bd0f0ad4935103b7ac0ef94e2.jpg)



Full mesh networks have n(n-1)/2 physical duplex links!


## Introduction Network Topologies: Hybrid

<sup>•</sup> Topologies can be mixed into a hybrid network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/bdacb0701b89241552fb0921fc6a469169a9f87bcb21cb36fa0c55ef60ac7345.jpg)



Star-backbone with 3 bus networks


## Introduction Categories of Networks

<sup>•</sup> Networks are categorized by size, number of hosts, bandwidth. 

• Personal Area Network (PAN) 

• Local Area Network (LAN) or Wireless Local Area Network (WLAN). 

• Metropolitan Area Network (MAN). 

• Wide Area Network (WAN) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/ce60f3d04f366755847e1badd2eb640e4dfa6ae6f617eb0463f59e077aaad015.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/b9521f09dd0a688946c7bfdc76353ff272f73a589d963c6686cb29303d2c7481.jpg)



Example of LAN connecting 12 computers to a switch


## Personal Area Network Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/7bb610ea03dee45887b582fa1a061129af1c9872ec2d698fc9e3d685b4a3e04e.jpg)


PANs (Personal Area Networks) let devices communicate over the range of a person. Bluetooth is a short-range wireless network used to connect components without wires. 

## Local Area Network Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/9d704f9e7d68da8b3d0db1a0479b0afe7071dcff3f039952637e1e4210cd8594.jpg)


The configuration on the left represents a wireless 802.11 network. The configuration on the right represents a wired switched Ethernet network. 

## Home Network Categories of Networks

## • Home network LAN

<sup>–</sup> Broad, diverse range of Internet-connected devices 

<sup>–</sup> Characteristics: manageable, dependable, and secure 

## <sup>•</sup> Internet of things

<sup>–</sup> Allows almost any device to connect 

## <sup>•</sup> Required home network properties

<sup>–</sup> Easy to install 

– Secure and reliable 

<sup>–</sup> Interfaces work between all products 

– Reduced consumer device costs 

## Metropolitan Area Network Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/030540122de8298b0d90f019fc7b1bb76302b62778797df20ccb4d0c61a7d8e0.jpg)


A MAN (metropolitan area network) where both television signals and the Internet are being fed into the centralized cable head-end (or cable modem termination system) for subsequent distribution to people’s homes. 

## Wide Area Network (1/3) Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/c4e4ed9e7939abd36640fb4652453f795410ee3a7f6e56f6dc040c261f05bff0.jpg)



This wide area network illustrates how hosts in Perth, Brisbane, and Melbourne can communicate using leased lines.


## Wide Area Network (2/3) Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/8cc247d1e276ec0810ff9622e7c326d5c2f9357babe5ee8f5a44dd1095749f46.jpg)


This wide area network illustrates how hosts in Perth, Brisbane, and Melbourne can communicate via the Internet. 

## Wide Area Network (3/3) Categories of Networks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/8b67ca10cfedce3a384b86c9f2b472f057a07dcecb521ff52d8fdc956f9f1271.jpg)


This wide area network illustrates how hosts in Perth, Brisbane, and Melbourne can communicate via an ISP. 

## Introduction Complexity of WANs

<sup>•</sup> The complexity of the topology may increase with the size of the network. 

<sup>•</sup> WANs connecting nations or continents can obviously be very complex and heterogeneous. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/dc921d9fe05255e3fd4763690457460e2461f70a202ee852b382669f713c732a.jpg)



Example of heterogeneous WAN


## Introduction Internet Service Providers

• Internet access is the basic service. 

• An Internet Service Provider (ISP) is an organisation that provides services for accessing, using, or participating the Internet. 

<sup>•</sup> ISPs can be organized as commercial, community-owned, non-profit, or privately owned (e.g., by private companies or universities). 

<sup>•</sup> Diferent ISPs exchange data through Network (neutral) Access Points (NAPs) or Internet Exchange Points (IXPs). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/9a588c43498b554898944cefc06646fd256a1fe116fee2f07b40467d26eb2c4d.jpg)



a. Structure of a national ISP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/f4fcdfe027a840ff69fa8bacaea90b479e6e09ece1c2138f1bd1536def00ab0d.jpg)



b. Interconnection of national ISPs


## Introduction Internet Service Providers

## <sup>•</sup> An ISP network is hierarchically defined:

• A point of presence (PoP) is a group of one or more routers used by ISPs to reach the customers. 

• Access ISPs for local areas. 

<sup>•</sup> Regional ISPs for larger areas. 

• National ISPs for nations. 

## • An Internet exchange point (IXP) works as a meeting point between multiple ISPs (often not managed by the ISPs involved).

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/2a7abe31cebdebe119fb0607485582d09ed251f24d969d08d8ea345a3676ba1e.jpg)



a. Structure of a national ISP


![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/82386c7995ef1072bb9d3052f40f024001e193757654524d1d598eec783373d1.jpg)



b. Interconnection of national ISPs


## Introduction Internet Connection

• Private internet connections are established via Modem/ONT connected to the telephone network. 

• Analogic (56kbps). 

<sup>•</sup> Integrated Services Digital Network ISDN (128kbps). 

<sup>•</sup> Asymmetric Digital Subscriber Line ADSL (1Mbps to 20Mbps). 

<sup>•</sup> Twisted-Pair Copper Wire (10Mbps to 100Mbps). 

<sup>•</sup> Optical Fiber (50Mbps to 40Gbps), via optical network terminal - ONT, no (de)modulation. 

<sup>•</sup> Companies (especially medium/large ones) can have a direct/dedicated connection to the ISP. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/213311d8-6447-4096-90d9-d6d872fa28b4/405a5e01c429992ef3c02d6405b5d1837d3798bbcbac34af7c3eb66f502f9108.jpg)



Company
