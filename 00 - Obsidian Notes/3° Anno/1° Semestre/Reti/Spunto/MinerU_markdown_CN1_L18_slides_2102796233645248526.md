## The Network Layer: DHCP, LANs, IPv6

Lecture 18 

## Network Layer Internet Protocol: IP Assignment

<sup>•</sup> Within a block of addresses, IP addresses must be assigned to individual interfaces. 

<sup>•</sup> A system administrator can configure the IP addresses in two ways: 

<sup>•</sup> Manually: by assigning one-to-one IP addresses to hosts. 

<sup>•</sup> Automatically: the network autonomously assigns free IP to incoming hosts. 

<sup>•</sup> The second approach (most common) can be done by using the Dynamic Host Configuration Protocol (DHCP). 

• In addition to host IP address, DHCP provides a host with the information needed to join the network, such as subnet mask, the address of the default gateway (to go outside of the network), and the address of the local DNS server. 

<sup>•</sup> The DHCP is plug-and-play, and it is typically used in our homes. 

## Network Layer Internet Protocol: DHCP

<sup>•</sup> The DHCP is a client-server protocol: a newly arriving host (client) connects to the DHCP server to receive network information. DHCP service may be provided by a computer or by the router itself. <sup>•</sup> Formally, DHCP is an application-layer protocol. 

<sup>•</sup> Let’s look to the previous example of 3 subnets connected by a single router. 

<sup>•</sup> Here we assume the network on the right (233.1.2.0/24) to be equipped with a DHCP server. 

• When a new host joins the network, it trades the IP address with the DHCP server. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/a1089732fcfe13d7fc95afaccafb04d5ad70048877ca077b5cb003226ed4f22c.jpg)


## Network Layer Internet Protocol: DHCP

<sup>•</sup> Adding a new host is mainly a 4-steps process: 

1. DHCP server discovery: the new host sends in broadcast a DHCP discovery message (UDP on port 67) to find the DHCP server. 

• Destination IP: 255.255.255.255 (broadcast). 

• Source IP: 0.0.0.0 (this host). 

• Random transaction ID. 

2. DHCP server ofer: since multiple DHCP servers may be present, when a discovery message is received, a server responds with a broadcast message (on port 68) ofering a possible network configuration (yiaddr filed – Your Internet ADDRess). 

• Destination IP: 255.255.255.255 (broadcast). 

• Source IP: 223.1.2.5 (DHCP server). 

3. DHCP request: the new client selects the accepted ofer by echoing back the ofer message. 

4. DHCP ACK: final ACK message confirming the transaction. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/302d6c108dddb7c6bad210ef5b3e858c4437527ea28199bae2812f4e482236d8.jpg)


## Network Layer Internet Protocol: DHCP

<sup>•</sup> In this case everything works smoothly because the DHCP and the arriving host are in the same subnet. 

• If a server exists but in a diferent subnet, we need a DHCP relay agent to forward DHCP messages (a router can do that). 

<sup>•</sup> In this example we can configure our router to be a relay agent so that also hosts from subnets 223.1.1.0/24 and 223.1.3.0/24 are served by our DHCP. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/27b8b0073b98eb1ba47baca7e2c958531579403f8c16d4abb8ca0aa4c9a881c7.jpg)


## Network Layer

## Route

<sup>•</sup> In Linux we can use the ip command to see the network configuration provided by the DHCP. 

## <sup>•</sup> Usage:

<sup>•</sup> See our current configuration (IP address, mask): 

<sup>•</sup> $ ip addr 

<sup>•</sup> See our default gateway: 

<sup>•</sup> $ ip route 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/4ef7807e4c014f4b466350eb8ad9bef592a2da5359f509e5138532250efeb976.jpg)


## Network Layer Internet Protocol: Visibility

• In Internet there are billions of connected devices that must be associated with unique IP addresses to be reached by anyone. 

<sup>•</sup> Is it really necessary to have all devices visible to anyone? <sup>•</sup> For example: is it good to have my printer reachable (usable) by anyone on Internet? 

<sup>•</sup> There are clear issues in having all devices reachable from outside local networks: 

• IP addresses are finite. 

• If devices are locally connected it is often unreasonable (or undesirable) to expose all of them on Internet. 

<sup>•</sup> Local administrators should be fully aware of the overlying IP block structure in order to assign unused addresses (which is often not up to them, e.g., in home networks). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/8d89f09d49be920c8ce4bb9a8e983df1c26a8d76e4d6696a54694360d8a4d3a0.jpg)


## Network Layer Internet Protocol: NAT

• The Network Address Translation (NAT) service allows to remap the IP addresses of packets within a network into diferent ones (network masquerading). 

<sup>•</sup> This is performed by using a translation table associating multiple local IPs/ports (of the LAN) into a global IP/port (of the WAN). This service can be ofered by routers. 

• The masqueraded local network is also called private network or realm with private addresses. Private IP addresses are valid only inside the private network. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/5c54f120e7e4a12616ae361244a49000aa7174f9c3bb1976f77114e2f9e34c33.jpg)


## Network Layer Internet Protocol: NAT

<sup>•</sup> This is an example of a NAT-enabled router connecting a network to internet. 

• The four interfaces in the local network have the same subnet address of 10.0.0.0/24. The router behaves as a message passer that overrides the IPs with the one specified in the table: 

<sup>•</sup> Outgoing packets have their source IPs/ports overwriten with a single WAN-side IP (138.76.29.7) and a fresh port (5001). 

<sup>•</sup> Incoming packets have their destination IPs/ports overwriten with the specific LAN-side IP of the host (10.0.0.1) and the initial port (3345) 

<sup>•</sup> It is important to notice that, since hosts are unaware of the other hosts’ trafic, the NAT cannot use the initial port because multiple hosts may select the same port simultaneously. 

• Since the port is 16bits, NATs can manage over 60000 simultaneous connections. 

<table><tr><td colspan="2">NAT translation table</td></tr><tr><td>WAN side</td><td>LAN side</td></tr><tr><td>138.76.29.7, 5001...</td><td>10.0.0.1, 3345...</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/5bde4504437a521bc72c20041fb91dd2facf1f7ce9cea4afcbcb357a78db5543.jpg)


## Network Layer Ping

<sup>•</sup> To check if a host is reachable on a network, we can use the ping command (ping is the same on Linux/Windows machines). 

• Ping (Packet Internet Groper) is a utility based on the ICMP (Internet Control Message Protocol) transport protocol and sends a “echo request” packet to a host that automatically answers with a “echo reply” message. 

<sup>•</sup> Ping also provide the time elapsed between request/reply, measuring the RTT. 

## <sup>•</sup> Usage:

<sup>•</sup> To check the reachability: <sup>•</sup> $ ping [target address] 

<table><tr><td><img src="https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/673cee61e96d3db064e26c233f838b8f95f17462d068a544faebfdd4c5f4aff7.jpg"/></td></tr></table>

## Network Layer Nmap (pt.2)

<sup>•</sup> Besides port scanning, the nmap command can also be used to map/scan the devices on the network. 

• It relies on ping (ICMP) to discover hosts on the network. 

## <sup>•</sup> Usage:

<sup>•</sup> Ping-based hosts discovery: 

• $ sudo nmap -sn [gate address]/[subnet bits] 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/bcd1a2357cf1ec5bfbff2893218fd40afd3270276bd5d0d9081814a7cc408479.jpg)


## Network Layer Internet Protocol: Reserved IP addresses

• Since local administrators should be free to organize a private network without interferences, by convention there are some reserved IP blocks, i.e., that ISPs/ICANN cannot assign to any organization. Some common such blocks are: 

• 10.0.0.0 – 10.255.255.255 (reserved for private networks). 

• 192.168.0.0 – 192.168.255.255 (reserved for private networks). 

• 127.0.0.0 – 127.255.255.255 (indicate this machine, i.e., loopback). <sup>•</sup> Typically, 127.0.0.1 is used. 

• 0.0.0.0 (indicates current network). 

<sup>•</sup> Addresses having 0 in the host-part fall under this definition. 

• 255.255.255.255 (indicates broadcast). 

<sup>•</sup> Addresses having 255 in the host-part fall under this definition.<sup>.</sup> 

<sup>•</sup> The necessity to reserve IPs is given by the fact that private addresses may be the same as public (non-private) ones, so routing within the network would be ambiguous. 

## Network Layer Internet Protocol: LAN Setup Example

<sup>•</sup> Let’s see and example in which we want to create a new local subnetwork (LAN) into a pre-existing network (WAN). 

<sup>•</sup> The network administrator of the WAN provides us the following information: 

• The IP of the WAN: 150.100.0.0/16. 

• The IP of the getaway (leading to external WAN/Internet): 150.100.50.1 

• A free IP for our network: 150.100.50.10 

<sup>•</sup> We have now to configure our router and our devices to setup the new LAN. 

<sup>•</sup> We are considering a NAT-enabled router. 

• We decide that the IP of the new LAN will be: 192.168.1.0/24 (reserved for local networks). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/57cd24119ae346a3146ae479b88b395ac096f807a1938950d07e59e3c0d734a3.jpg)


# Network Layer Internet Protocol: LAN Setup Example

• Our local router has 2 interfaces, one for the WAN-side and another for the LAN-side. 

<sup>•</sup> Let’s start by configuring our local router’s WAN-side setings. 

<sup>•</sup> On the router we have to specify the following parameters: 

• The IP address of the router in the WAN. 

• The subnet of the WAN. 

<sup>•</sup> The gateway. 

• One or more DNS. 

<sup>•</sup> Notice that we can also specify a dynamic IP if the WAN has a DHCP service. 

## Internet Connection

Internet Connection Type: 

150.100.50.10 

255.255.0.0 

150.100.50.1 

Primary DNS: 8.8.8.8 

Secondary DNS: 4.4.4.4 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/ee362601745e39b91fe51a100baf5da30e6c9b3e7f6ab70bc583cffb7fc4074d.jpg)


## Network Layer Internet Protocol: LAN Setup Example

## <sup>•</sup> Now let’s configure the LAN-side setings.

<sup>•</sup> We have to give an IP to the LAN-side interface of the router: 

• Since our network will be addressed as 192.168.1.0/24, we will give 192.168.1.1/24 to the router (it is typical to give .1 to it). 

<sup>•</sup> In this example, our router also provide DHCP service, we can then specify: 

• Address pool (for DHCP hosts). 

• Lease time (timeout of the IP assignment, after that, the IP can be reused). 

• Gateway and DNS to be communicated to the hosts. 

## LAN

MAC Address: 48-22-54-16-18-7D 

IP Address: 

192.168.1.1 

Subnet Mask: 

255.255.255.0 

## DHCP Server

DHCP Server: 

Enable 

IP Address Pool: 

192.168.1.100 

192.168.1.250 

Address Lease Time: 

120 

Default Gateway: 

192.168.1.1 

Primary DNS: 

Secondary DNS: 

## Network Layer Internet Protocol: LAN Setup Example

<sup>•</sup> This is a simple example of how to configure this connection on a new host (Linux Mint). 

• There are diferent methods to choose: 

• Automatic (DHCP): uses DHCP to automatically configure the connection (you will get an IP from 192.168.1.100 to 192.168.1.250). 

<sup>•</sup> Manual: setup the connection by manually seting the configuration. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/4deb13b4bfb3887955b64c1b79da521a91aece167cd162282ce7c96c939c1810.jpg)


## Network Layer Internet Protocol: LAN Setup Example

<sup>•</sup> In a manual seting we need to know the network configuration (and the available IPs). 

## <sup>•</sup> We have to specify the main information for connection setup:

• IP address of the host (static/fixed). 

• Subnet mask. 

<sup>•</sup> Gateway. 

• DNS (one or more). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/5789232e0d0fa6110a7806df38280b9620593e8db8dc0b697e2d4e5afb70b293.jpg)


Routes... 

Cancel 

Save 

## Network Layer Internet Protocol: LAN Setup Example

• In this created LAN we can connect new hosts to the LAN by specifying a manual IP address (outside the DHCP pool) or an automatic IP address (inside the DHCP pool). 

<sup>•</sup> The connected hosts will send their packets to the local router (unaware of the outside WAN). 

<sup>•</sup> We have the local router configured to forward packets to the WAN router (and possibly to the Internet). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/8f06b4de-376c-4b7d-bb39-0b7b031e3eea/c00278dc89e411f8ed89578895e6e0d03cfca7f0524895121e08d8a31bf36685.jpg)


## Network Layer Internet Protocol: IPv6

<sup>•</sup> In the early 1990s, the Internet Engineering Task Force (IETF), which is an ONG founded in 1986, began an efort to develop a successor to the IPv4 protocol to face the 32-bit IPv4 address shortage. 

<sup>•</sup> IPv6 was designed to ensure more addresses available, but it was also an opportunity to update other aspects of IPv4, based on the accumulated operational experience. 

• It is not sure when exactly all the available IPv4 would be exhausted (it was speculated to be 2008 or 2018, but we have still some IPs left). 

<sup>•</sup> But what about IPv5? It was proposed in 1979 and was based on the experimental Internet Stream Protocol (ST). It was still relying on 32bit addresses, so it was dropped mainly because of addresses shortage. 

## Network Layer Internet Protocol: IPv6 Datagram

## <sup>•</sup> IPv6 has the following advantages:

• Expanded addressing capabilities: from 32 to 128 bits (i.e., 3.4028237e+38), which ensures that the world won’t run out of IP addresses, as every grain of sand on the planet can be IP-addressable. 

<sup>•</sup> A fixed-length 40-byte header: some of IPv4 fields have been dropped or made optional. 

<sup>•</sup> Flow labeling: packets from some applications (e.g., audio/video streaming) can be grouped into a unique with flow having specific identification. 

<sup>•</sup> The precise role and usage of flows is still discussed. 

<table><tr><td colspan="5">32 bits</td></tr><tr><td colspan="5"></td></tr><tr><td>Version</td><td>Traffic class</td><td colspan="3">Flow label</td></tr><tr><td colspan="3">Payload length</td><td>Next hdr</td><td>Hop limit</td></tr><tr><td colspan="5">Source address(128 bits)</td></tr><tr><td colspan="5">Destination address(128 bits)</td></tr><tr><td colspan="5">Data</td></tr></table>

## Network Layer Internet Protocol: IPv6 Datagram

<sup>•</sup> IPv6 datagram is composed by the following fields: 

<sup>•</sup> Version (4 bits): identifies the IP version number. Not surprisingly, IPv6 carries a value of 6 in this field. 

• Trafic class (8 bits): like the TOS field in IPv4, can be used to give priority to datagrams (e.g., voice-over-IP over SMTP, etc.). 

• Flow label (20 bits): identify a flow of datagrams. 

• Payload length (16 bits): the number of bytes of the payload (40- bytes header excluded). 

• Next header (8 bits): identifies the upper-level protocol to which the contents (data field) of this datagram will be delivered (for example, to TCP or UDP). Similar to protocol field in the IPv4 header. 

• Hop limit (8 bits): Specifies the time-to-live as in TTL field of IPv4 (decremented every forward). 

• Source and destination addresses (128+128 bits): the IPv6 128-bit addresses. 

• Data (variable): the payload portion of the datagram. 

<table><tr><td colspan="5">32 bits</td></tr><tr><td colspan="5"></td></tr><tr><td>Version</td><td>Traffic class</td><td colspan="3">Flow label</td></tr><tr><td colspan="3">Payload length</td><td>Next hdr</td><td>Hop limit</td></tr><tr><td colspan="5">Source address(128 bits)</td></tr><tr><td colspan="5">Destination address(128 bits)</td></tr><tr><td colspan="5">Data</td></tr></table>

## Network Layer Internet Protocol: IPv6 Datagram

<sup>•</sup> What is missing from IPv4: 

<sup>•</sup> Fragmentation-related fields: IPv6 does not allow fragmentation and reassembly on intermediate routers, but only on hosts. 

<sup>•</sup> If an IPv6 datagram received by a router is too large to be forwarded, the router simply drops the datagram and sends a <sup>“</sup>Packet Too Big<sup>”</sup> error message back to the sender. The sender can then resend the data, using a smaller IP datagram size. 

• Header checksum: it takes time on routers, and it is redundant as link-layer protocols typically perform checksum on the whole packet. 

<sup>•</sup> Options: are no longer a part of the standard IP header, some options can be specified into next header field (along with TCP/UDP identifiers). 


32 bits


<table><tr><td>Version</td><td>Header length</td><td>Type of service</td><td colspan="2">Datagram length (bytes)</td></tr><tr><td colspan="3">16-bit Identifier</td><td>Flags</td><td>13-bit Fragmentation offset</td></tr><tr><td colspan="2">Time-to-live</td><td>Upper-layer protocol</td><td colspan="2">Header checksum</td></tr><tr><td colspan="5">32-bit Source IP address</td></tr><tr><td colspan="5">32-bit Destination IP address</td></tr><tr><td colspan="5">Options (if any)</td></tr><tr><td colspan="5">Data</td></tr></table>

## IPv4


32 bits


<table><tr><td>Version</td><td>Traffic class</td><td colspan="3">Flow label</td></tr><tr><td colspan="3">Payload length</td><td>Next hdr</td><td>Hop limit</td></tr><tr><td colspan="5">Source address(128 bits)</td></tr><tr><td colspan="5">Destination address(128 bits)</td></tr><tr><td colspan="5">Data</td></tr></table>

## Network Layer Internet Protocol: From IPv4 to IPv6

<sup>•</sup> There is one big issue with IPv6: it is not backward-compatible. IPv4-capable systems are unable to handle IPv6 datagrams. 

<sup>•</sup> How will Internet adopt IPv6? 

• The flag day approach: in a given time and date all Internet machines would be turned of and upgraded from IPv4 to IPv6. A similar approach have been used when TCP was introduced but it was a mess (even for the small internet network of the time). A flag day involving billions of devices is even more unthinkable today. 

• The tunneling approach: the use of specific routers (tunnels) in charge of mapping IPv4 datagrams into IPv6 datagrams and vice versa in almost-transparent way. This is probably the most realistic approach, already used in practice. 

<sup>•</sup> While the adoption of IPv6 was initially slow, it is accelerating. 