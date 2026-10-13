## Networ<sup>k</sup> Secur<sup>i</sup>ty: Fundamentals

Lecture 25 

## Network Security Some Application Protocols (remind)

• Some application may exchange sensitive information (e.g., user’s credentials, personal data, etc.). 

• On public networks, messages should be secured. 

<table><tr><td>Application</td><td>Description</td></tr><tr><td>DHCP</td><td>Dynamic Host Configuration Protocol, assigns IP addresses</td></tr><tr><td>DNS</td><td>Domain Name System, translate website names to IP addresses</td></tr><tr><td>HTTP/HTTPS</td><td>HyperText Transfer Protocol (Secure), transfer web pages</td></tr><tr><td>SMTP/SMTPS</td><td>Simple Mail Transfer Protocol (Secure), sends email messages</td></tr><tr><td>SNMP</td><td>Simple Network Management Protocol, manages network devices</td></tr><tr><td>Telnet/SSH</td><td>Teletype Network (Secure SHEll), allows command-line interfacing with remote hosts</td></tr><tr><td>FTP/FTPS</td><td>File Transfer Protocol (Secure), used to transfer files</td></tr></table>

## Network Security Introduction

• The network securit<sub>y</sub> is the field that studies <sub>p</sub>ossible atacks to networks and <sub>p</sub>ossible wa<sub>y</sub>s to <sub>p</sub>revent them. 

• Networking is part of our lives (Internet connection is considered almost as water or power supply) and a large quantity of our sensible data travels on networks. 

• There are several types of atacks having diferent purposes and diferent mechanics. 

• Atacks evolve along with the technology and the networks’ audience. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/de74c9eb82a54a04ed0589f53306255a9031b2cddd319ee9f1e5690f3e594ff7.jpg)


## Network Security Atacks: Malwares

• A malware is malicious software that can be transferred to a computer through the network (e.g., downloaded file, e-mail atachment, etc.). 

• Once malware infects our device it can harm in diferent ways: 

• Forcing a system to show commercial advertisements (adware). 

• Showing false alarm messages to induce users to download malwares (scareware). 

• Deleting (wiper) or encrypting (ransomware) our files. 

• Collecting private information such as passwords, security numbers, etc. (spyware). • For example, keyloggers are software recording (logging) the keys struck on a keyboard. 

• Geting root privileges of our system (rootkits). 

• Turn a device into a slave or foothold to atack other devices (zombie or botnet). 

## Network Security

## Atacks: Malwares

• Todays malware are often self-replicating: once it infects one host, from that host it seeks entry into other hosts over the Internet, and from the newly infected hosts, it seeks entry into yet more hosts. 

• Malware can spread in the form of a virus or a worm: 

• Viruses are malware that re<sub>q</sub>uire some form of user interaction to infect the user’s device. 

• For example, an e-mail atachment containing malicious executable code that self-replicates by sending similar mails to users’ contacts. 

• These are typically disguised as legitimate software components (trojan horses). 

• Worms are malware that can enter a device without an<sub>y</sub> ex<sub>p</sub>licit user interaction. 

• For example, a user may be running a vulnerable network application which accepts the worm without intervention. The worm than scans the network for hosts running a similar application. 

## Network Security Atacks: DoS

• Denial-of-Service (DoS) atacks are quite common and are designed to render a network, a host, or other piece of infrastructure (e.g., Web servers, DNS, etc.) unusable by legitimate users. 

• There are 3 types of DoS atacks: 

1. Vulnerability atack: sending suitable messages to vulnerable applications or OSs in order to let them stop or crash. 

2. Bandwidth flooding: sending a large quantity of packets to the targeted host, preventing legitimate packets from reaching the server. 

3. Connection flooding: establishing a large number of half-open or fully open TCP connections at the target host, so it stops accepting legitimate connections. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/e7ef5e0640f8bc4f13bb676323e9704e7bdb1ed96e618fbcf1499175d7edadea.jpg)



Example of a DDoS (Distributed DoS) atack using a botnet of zombies (or slaves).


## Network Security Atacks: Packets Snifing

• Packets snifing involves a passive receiver (snifer) that records a copy of relevant packets from a target host trying to steal sensitive information (aka eavesdropping). 

• Snifers can be deployed in all kind of broadcast networks (wired or wireless) simply by copying packets that are meant for diferent destinations instead of discarding them. 

• As for non-broadcast networks, a snifer can be put into a malware (spyware) and used to infect network devices (e.g., routers) so that all forwarded trafic is also copied. 

• Since snifers are passive (no additional trafic is injected into the network) these are ver<sub>y</sub> dificult to detect. 

• To prevent snifing cryptography approaches can be used. 

## Network Security Atacks: Packets Snifing

• There are several snifers freely available on Internet. A notable example of packet snifer is Wireshark (ex Ethereal). 

• As seen in our lab sessions. 

<table><tr><td>53 6.916738 207.142.131.235 192.168.1.30 TCP 80 &gt; 65155 [ACK] Seq=1 Ack=450 Win=6864 Len=0 TSV=3117138150 TSER=710995743
54 6.961542 207.142.131.235 192.168.1.30 HTTP HTTP/1.0 304 Not Modified
55 6.961666 192.168.1.30 207.142.131.235 TCP 65155 &gt; 80 [ACK] Seq=450 Ack=422 Win=65535 Len=0 TSV=710995744 TSER=3117138194
56 6.972635 192.168.1.30 207.142.131.235 TCP 65155 &gt; 80 [FIN, ACK] Seq=450 Ack=422 Win=65535 Len=0 TSV=710995744 TSER=3117138194
59 7.239480 207.142.131.235 192.168.1.30 TCP 80 &gt; 65155 [FIN, ACK] Seq=422 Ack=451 Win=6864 Len=0 TSV=3117138473 TSER=710995744
60 7.254723 192.168.1.30 207.142.131.228 TCP 65156 &gt; 80 [SYN] Seq=0 Len=0 MSS=1460 WS=0 TSV=710995745 TSER=0
61 7.522182 207.142.131.228 192.168.1.30 TCP 80 &gt; 65156 [SYN, ACK] Seq=0 Ack=1 Win=5792 Len=0 MSS=1420 TSV=187437131 TSER=71099574
62 7.522345 192.168.1.30 207.142.131.228 TCP 65156 &gt; 80 [ACK] Seq=1 Ack=1 Win=65535 Len=0 TSV=710995745 TSER=187437131
63 7.523120 192.168.1.30 207.142.131.228 HTTP GET /wikipedia/en/f/fb/Wsicon48.png HTTP/1.1
64 7.794383 207.142.131.228 192.168.1.30 TCP 80 &gt; 65156 [ACK] Seq=1 Ack=375 Win=6864 Len=0 TSV=187437403 TSER=710995745
65 7.796209 207.142.131.228 192.168.1.30 HTTP HTTP/1.0 304 Not Modified
66 7.796322 192.168.1.30 207.142.131.228 TCP 65156 &gt; 80 [ACK] Seq=375 Ack=338 Win=65535 Len=0 TSV=710995746 TSER=187437404
67 7.797664 192.168.1.30 207.142.131.228 TCP 65156 &gt; 80 [FIN, ACK] Seq=375 Ack=338 Win=65535 Len=0 TSV=710995746 TSER=187437404
68 8.039561 207.142.131.235 192.168.1.30 TCP 80 &gt; 65155 [FIN, ACK] Seq=422 Ack=451 Win=6864 Len=0 TSV=3117139274 TSER=710995744
69 8.039704 192.168.1.30 207.142.131.235 TCP 65155 &gt; 80 [ACK] Seq=451 Ack=423 Win=65535 Len=0 TSV=710995746 TSER=3117139274
70 8.065048 207.142.131.228 192.168.1.30 TCP 80 &gt; 65156 [FIN, ACK] Seq=338 Ack=376 Win=6864 Len=0 TSV=187437674 TSER=710995746
71 8.868153 207.142.131.228 192.168.1.30 TCP 80 &gt; 65156 [FIN, ACK] Seq=338 Ack=376 Win=6864 Len=0 TSV=187438478 TSER=710995746
72 8.868306 192.168.1.30 207.142.131.228 TCP 65156 &gt; 80 [ACK] Seq=376 Ack=339 Win=65535 Len=0 TSV=710995748 TSER=187438478</td></tr></table>


GUI of Wireshark from Wikipedia 


## Network Security Atacks: IP Spoofing

• IP spoofing is a technique that allow malevolent hosts to inject into a network packets with false source addresses (forged). 

• It can be used in combination with applications vulnerability to atack specific hosts being masqueraded as another user. 

• It can also be used for DoS atacks (alternative to botnets) as messages from diferent source IPs are more dificult to filter. 

• Spoofing (and snifing) can also be used for man-in-the-middle (MitM or MiM) atacks, in which the atacker is placed in between 2 communicating hosts disguised as both. 

• The 2 hosts think they are communicating each other, while they are actually communicating with the atacker. 

• To prevent spoofing, we can use message integrity checks and end-point authentication, allowing us to determine if the message has not been modified or if the message originates from the right source. 

## Network Security Basics of Network Security

• Given the previous atack types, we can now define the set of proprieties that a secure communication should guarantee: 

• Confidentiality: only the sender and intended receiver should be able to understand the contents of the transmited message (snifing avoidance). 

• Message integrity: the content of the communication must not be altered, either maliciously or by accident. 

• End-<sub>p</sub>oint authentication: both the sender and receiver should be able to confirm the identity of the other party involved in the communication (spoofing avoidance). 

• Operational security: to rely on a network infrastructure that prevents malicious hosts to sneak into the communication. 

• The first 3 proprieties are software-based the last one (operational security) typically relies on specific hardware (firewalls, intrusion detection systems). 

## Network Security Cryptography

• A cr<sub>yp</sub>to<sub>g</sub>ra<sub>p</sub>hic techni<sub>q</sub>ue allows a sender to dis<sub>g</sub>uise data so that it becomes incomprehensible for an intruder. 

• Intruders can gain no information from the intercepted data, but the receiver must be able to recover the original data from the disguised data. 

• In its initial form the message is called plaintext (or cleartext) and is readable for everyone. 

• Before to inject the message into the channel a host uses an encryption algorithm to transform the message into a non-readable form called ciphertext which must be decrypted when received. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/f047ac0daec6365b7d89e68cbc39bf9e6d32141798e551ae77c3a9527c57d65e.jpg)


## Network Security Cryptography: Keys

• In many modern cryptographic systems, including those used on the Internet, the encryption techni<sub>q</sub>ue is known and standard for ever<sub>y</sub>one (including the intruder). The unknown part of the algorithm are the encryption/decryption keys. 

• A key is an alphanumerical string that must be provided to the encryption/decryption algorithm in order to encrypt/decrypt the messages. 

• Encryption and decryption keys can be identical (symmetric) or diferent (asymmetric). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/574ec27b57c476f9751dc308b703713a0602c9f13334b0cabff81b09503fb339.jpg)


## Network Security Cryptography: Symmetric

• In s<sub>y</sub>mmetric cr<sub>yp</sub>to<sub>g</sub>ra<sub>p</sub>h<sub>y</sub> there is onl<sub>y</sub> one ke<sub>y</sub> that is used for both encryption and decryption. 

• Encryption: the plaintext message along with the key is passed to the encryption algorithm to generate a ciphertext that can be safely sent through the network. 

• Decryption: the cyphertext message along with the key is passed to the decryption algorithm to recreate the initial plaintext message (readable). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/9e2a43b1487c5da47daaa57eb44e333878c36faa524d8962bcfc82ea4dbe95b1.jpg)


## Network Security Cryptography: Key Exchange

• The problem with symmetric cryptography, or single-key cryptography, is that it requires the secret key to be communicated (key exchange problem). 

• Hosts can use a secure channel to exchange the key. 

• Hosts can use some <sub>p</sub>rotocol that allows them to “converge” on a shared key. 

• If two parties cannot establish a secure initial key exchange, they won't be able to communicate securely without the risk of messages being intercepted and decrypted by a third party who acquired the key during the initial key exchange. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/24d8100f7a6cd14c97720f660f26a216c00b6c1c4c26fa950a43c5decf3c1e1f.jpg)


## Network Security Cryptography: Asymmetric

• In as<sub>y</sub>mmetric cr<sub>yp</sub>to<sub>g</sub>ra<sub>p</sub>h<sub>y</sub> there is a two-ke<sub>y</sub> s<sub>y</sub>stem (public and private keys). 

• A message that is encrypted with one key must be decrypted with the other and vice versa. 

• The idea is that the <sub>p</sub>ublic ke<sub>y</sub> can be sent over nonsecure channels or shared in public, while the private key is only available to its owner. 

• A typical approach is to use public key for encryption and <sub>p</sub>rivate ke<sub>y</sub> for decr<sub>yp</sub>tion: 

• If the intruder snifs the public key, it is still impossible for him/her to decrypt messages. 

• Host A will use B-key-public to encrypt messages that can only be seen through B-key-private, which is only into B’s hands. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/bb8fe2f837b48e8d91b3dfae9eb7b9ed7acfb62e3b7f4f9e081a8a41eb968e10.jpg)


## Network Security Certification Authority

• In public key cryptography it could be useful to verify if a public key really belong to the entity with whom you want to communicate. 

• Otherwise, we could have someone’s else key (atacker) and we could encrypt messages that are readable by illegitimate entities. 

• Binding a public key to a particular entity is typically done by a Certification Authority (CA), whose job is to validate identities and issue certificates. A CA has the following roles: 

1. A CA verifies that an entity is who it says it is. There is no protocol for that, one must trust the CA to have performed a suitably rigorous identity verification. 

• It works like a natural selection process: if a CA is unreliable no on will trust it. 

• There are several federal or statal CA that provide a reasonable reliability, but we still have to trust them. 

2. Once the CA verifies the identity of the entity, the CA creates a certificate that binds the public key of the entity to the identity. The certificate contains the public key and a globally unique identifier of the owner (for example, a name or an IP address). 

## Network Security Message Integrity

• Message integrity (also known as message authentication) is the problem of checking if: 

1. The message has not been tempered with. 

2. The message has been indeed originated by the expected host. 

• We can create a check-item similarly as the checksum or CRC. Typically, a hash function is used to create such item. 

• Remind: a hash function is any function that can be used to map data of arbitrary size into fixed-size values. 

• A cryptographic hash function is a function H that converts a message x into a fixed-size string H(x) so that it is very hard (computationally infeasible) to find another message y such that $H ( y ) = H ( x )$ 

## Network Security Message Integrity

• As in checksum or CRC, a first strategy can be to atach this hash into the messa<sub>g</sub>e: 

1. Host A creates messa<sub>g</sub>e m and calculates the hash h = H(m). 

2. Host A appends h to the message m, creating an extended message (m, h), and sends the extended message to B. 

3. Host B receives the message (m, h) and calculates H(m). If H(m) = h, the message is intact. 

• This a<sub>pp</sub>roach is obviousl<sub>y</sub> flawed. An intruder may spoof the whole message (m,h), creating a new “ad hoc” one (m’,h’) that is still consistent with the hashing function H. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/0e8e228c76e644ee664cf2d5562ea713eebefbefe18667769a400ec6d66e6623.jpg)


## Network Security Message Integrity

• To avoid this, A and B need a shared secret s (a shared key or a password) which is a string known only to them. 

• This basically works as a symmetric encryption where s is the unique private key. 

## • Assuming such s exists then:

1. Host A creates a message m + s (as a concatenation of message and secret) and calculates the hash h = H(m + s) aka a message authentication code (MAC). 

2. Host A appends the MAC to the message m, creating an extended message (m, H(m + s)), and sends the extended message to B. 

3. Host B receives the extended message (m, h) and knowing s, calculates the MAC H(m + s). If H(m + s) = h, the message is intact. 

• As in all symmetric approaches, also here we need to exchange such secret. 

• This secret can be exchan<sub>g</sub>ed combinin<sub>g</sub> as<sub>y</sub>mmetric cr<sub>yp</sub>to<sub>g</sub>ra<sub>p</sub>h<sub>y</sub> and certificates. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/61b07f1e-d5ac-4722-ac5b-4514e646c942/7c63333e13ff7ee7cd9efe142f3054224d49de4e35c37e07bc23f7bffb2ace51.jpg)
