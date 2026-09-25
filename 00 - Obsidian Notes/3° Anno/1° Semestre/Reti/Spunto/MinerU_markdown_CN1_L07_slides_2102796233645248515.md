## The Application Layer: More on DNS

Lecture 7 

## Application Layer DNS

• There are two ways to identify a host: by hostname and by IP address. People prefer the more mnemonic hostname identifier, while network devices prefer fixed-length, hierarchically structured IP addresses. 

• Example: www.unina.it -> 143.225.15.50 

• The Domain Name System (DNS) is an application-layer protocol that manages translation from hostnames to IP addresses. 

• It is a client-server protocol in which a DNS-client asks to a DNS-server for a specific hostname-to-address translation. 

• DNS servers are often UNIX machines running the Berkeley Internet Name Domain (BIND) software, typically using UDP connection and port number 53. 

## The Domain Name System (DNS)

<sup></sup> Mechanism to “convert” names to IP addresses 

<sup></sup> Impossible to manage a centralised repository (table) 

<sup></sup> large number of hosts 

<sup></sup> geographical distance of hosts and delays 

<sup></sup> DNS is a distributed, decentralised system 

## DNS (cont’d)

<sup></sup> hierarchical 

<sup></sup> domain-based 

<sup></sup> implemented by means of a distributed database 

Resolver 

<sup></sup> Program that returns the IP address associated to a name 

<sup></sup> queries a local DNS server 

<sup></sup> all messages are UDP packets 

## The DNS name space

<sup></sup> Naming hierarchy organised by ICANN (Internet Corp. for Assigning Names and Numbers) 

<sup></sup> 250 top-level domains 

<sup></sup> Each domain partitioned in sub-domains, and so on 

## Top-level domains

## Two types

<sup></sup> generic (aero, com, edu, . . . ) 

<sup></sup> country (uk, uk, it, tv, . . . ) 

all managed by registrars appointed by ICANN 

## The DNS name space

<sup></sup> The name space is hierarchical from the root down 

<sup></sup> Diferent parts delegated to diferent organisations 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/254eb799-fa42-4cbe-949c-5a21e6034691/cf6abebdda8658935d3b21e5b424aea7dd5cc2fa98f97692f5b47923ee5da255.jpg)



The computer robot.cs.washington.edu


## The DNS name space (cont’d)

Generic top-level domains are controlled by ICANN who appoints registrars to run them 

<table><tr><td>Domain</td><td>Intended use</td><td>Start date</td><td>Restricted?</td></tr><tr><td>com</td><td>Commercial</td><td>1985</td><td>No</td></tr><tr><td>edu</td><td>Educational institutions</td><td>1985</td><td>Yes</td></tr><tr><td>gov</td><td>Government</td><td>1985</td><td>Yes</td></tr><tr><td>int</td><td>International organizations</td><td>1988</td><td>Yes</td></tr><tr><td>mil</td><td>Military</td><td>1985</td><td>Yes</td></tr><tr><td>net</td><td>Network providers</td><td>1985</td><td>No</td></tr><tr><td>org</td><td>Non-profit organizations</td><td>1985</td><td>No</td></tr><tr><td>aero</td><td>Air transport</td><td>2001</td><td>Yes</td></tr><tr><td>biz</td><td>Businesses</td><td>2001</td><td>No</td></tr><tr><td>coop</td><td>Cooperatives</td><td>2001</td><td>Yes</td></tr><tr><td>info</td><td>Informational</td><td>2002</td><td>No</td></tr><tr><td>museum</td><td>Museums</td><td>2002</td><td>Yes</td></tr><tr><td>name</td><td>People</td><td>2002</td><td>No</td></tr><tr><td>pro</td><td>Professionals</td><td>2002</td><td>Yes</td></tr><tr><td>cat</td><td>Catalan</td><td>2005</td><td>Yes</td></tr><tr><td>jobs</td><td>Employment</td><td>2005</td><td>Yes</td></tr><tr><td>mobi</td><td>Mobile devices</td><td>2005</td><td>Yes</td></tr><tr><td>tel</td><td>Contact details</td><td>2005</td><td>Yes</td></tr><tr><td>travel</td><td>Travel industry</td><td>2005</td><td>Yes</td></tr><tr><td>xxx</td><td>Sex industry</td><td>2010</td><td>No</td></tr></table>

## Domain names

<sup></sup> Names are paths upwards from the domain to the root 

<sup></sup> example: eng.mit.edu 

<sup></sup> Absolute paths end with a dot; relative paths are to be interpreted 

<sup></sup> Possibility of registering under more than one top-level domain 

<sup></sup> example: ibm.com, ibm.us 

<sup></sup> cyber-squatting: buying domains only in order to sell them later to interested businesses 

## Domain names (cont’d)

<sup></sup> Each domain controls the allocation of the domains under it 

<sup></sup> The creation of a new domain requires permission from the parent domain 

<sup></sup> Naming does not follow physical/geographical boundaries 

## Domain resource records

## Fields of a resource record

<sup></sup> domain name 

<sup></sup> time to live 

<sup></sup> class 

<sup></sup> type 

<sup></sup> value 

## Resource record fields: Domain name (NAM

<sup></sup> Tells the domain to which the record applies 

<sup></sup> This field is the main search key for DNS queries 

<sup></sup> Normally several records exist for each domain, residing at diferent servers 

## Resource record fields: Time to live (TTL)

<sup></sup> Indicates the life time of the record 

<sup></sup> long for stable hosts (e.g. 86, 400 for 1 day), short for volatile ones (e.g. 60 for 1 min) 

<sup></sup> maximum value 231 − 1, approximately 68 years 

## Resource record fields: Class (CLASS)

<sup></sup> This field is always IN (Internet) for Internet records 

<sup></sup> Other codes are rarely used 

## Resource record fields: Type (cont’d)

## Possible values:

<sup></sup> SOA (Start of Authority): information about the server’s zone (explained later), administrator’s contact etc. 

<sup></sup> A (Address): 32-bit IPv4 address of some interface for the host 

<sup></sup> some hosts have more than one interface 

<sup></sup> equivalent AAAA value for IPv6 addresses 

<sup></sup> MX (Mail eXchange): gives the name of the host which accepts email in the domain 

<sup></sup> [see next slide] 

## Resource record fields: Type (TYPE)

<sup></sup> NS (Name Space): gives the name server for the domain; used as part of name lookup 

<sup></sup> CNAME (Canonical Name): allows for aliases; the DNS lookup proceeds with the new name 

<sup></sup> PTR (Pointer): alias used for reverse lookup: the lookup does not proceed, instead the name is returned. 

## Resource record fields: Type (TYPE)

<table><tr><td>Type</td><td>Meaning</td><td>Value</td></tr><tr><td>SOA</td><td>Start of authority</td><td>Parameters for this zone</td></tr><tr><td>A</td><td>IPv4 address of a host</td><td>32-Bit integer</td></tr><tr><td>AAAA</td><td>IPv6 address of a host</td><td>128-Bit integer</td></tr><tr><td>MX</td><td>Mail exchange</td><td>Priority, domain willing to accept email</td></tr><tr><td>NS</td><td>Name server</td><td>Name of a server for this domain</td></tr><tr><td>CNAME</td><td>Canonical name</td><td>Domain name</td></tr><tr><td>PTR</td><td>Pointer</td><td>Alias for an IP address</td></tr><tr><td>SPF</td><td>Sender policy framework</td><td>Text encoding of mail sending policy</td></tr><tr><td>SRV</td><td>Service</td><td>Host that provides it</td></tr><tr><td>TXT</td><td>Text</td><td>Descriptive ASCII text</td></tr></table>

## Resource record fields: Value (RDATA)

<sup></sup> The value depends on the record type (see table in previous slide) 

<sup></sup> Can contain a domain, a value, or an ASCII string 

## Doma<sup>i</sup>n resource records: examp<sup>l</sup>e

<table><tr><td colspan="5">; Authoritative data for cs.vu.nl</td></tr><tr><td>cs.vu.nl.</td><td>86400</td><td>IN</td><td>SOA</td><td>star boss (9527,7200,7200,241920,86400)</td></tr><tr><td>cs.vu.nl.</td><td>86400</td><td>IN</td><td>MX</td><td>1 zephyr</td></tr><tr><td>cs.vu.nl.</td><td>86400</td><td>IN</td><td>MX</td><td>2 top</td></tr><tr><td>cs.vu.nl.</td><td>86400</td><td>IN</td><td>NS</td><td>star</td></tr><tr><td>Star</td><td>86400</td><td>IN</td><td>A</td><td>130.37.56.205</td></tr><tr><td>zephyr</td><td>86400</td><td>IN</td><td>A</td><td>130.37.20.10</td></tr><tr><td>top</td><td>86400</td><td>IN</td><td>A</td><td>130.37.20.11</td></tr><tr><td>www</td><td>86400</td><td>IN</td><td>CNAME</td><td>star.cs.vu.nl</td></tr><tr><td>ftp</td><td>86400</td><td>IN</td><td>CNAME</td><td>zephyr.cs.vu.nl</td></tr><tr><td>flits</td><td>86400</td><td>IN</td><td>A</td><td>130.37.16.112</td></tr><tr><td>flits</td><td>86400</td><td>IN</td><td>A</td><td>192.31.231.165</td></tr><tr><td>flits</td><td>86400</td><td>IN</td><td>MX</td><td>1 flits</td></tr><tr><td>flits</td><td>86400</td><td>IN</td><td>MX</td><td>2 zephyr</td></tr><tr><td>flits</td><td>86400</td><td>IN</td><td>MX</td><td>3 top</td></tr><tr><td rowspan="3">rowboat</td><td></td><td>IN</td><td>A</td><td>130.37.56.201</td></tr><tr><td></td><td>IN</td><td>MX</td><td>1 rowboat</td></tr><tr><td></td><td>IN</td><td>MX</td><td>2 zephyr</td></tr><tr><td>little-sister</td><td></td><td>IN</td><td>A</td><td>130.37.62.23</td></tr><tr><td>laserjet</td><td></td><td>IN</td><td>A</td><td>192.31.231.216</td></tr></table>

## Name servers

<sup></sup> A single, centralised DNS server makes no sense 

<sup></sup> The DNS name space is divided in non-overlapping zones 

<sup></sup> The partitioning is up to the zone administrator 

<sup></sup> Each zone contains one or more name servers 

<sup></sup> a primary one and secondary one 

## Name servers (cont’d)

<sup></sup> Name servers contain data for portions of the name space called zones (circled) 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/254eb799-fa42-4cbe-949c-5a21e6034691/4639343880e43fa622f6f10809530fc09cb5354d4cee034dae5d4b5718d15fb7.jpg)


## Name resolution

1.Host queries a local name server 

2.If the domain falls under the jurisdicion (zone) of the local server, an authoritative record is returned 

3.otherwise, the local server handles the query recursively and issues remote queries 

<sup></sup> if the DNS server has the address, it returns it 

<sup></sup> otherwise, it returns the name server for a lower zone 

<sup></sup> the process goes on iteratively, until the address is found 

## Name resolution (cont’d)

<sup></sup> these are the ones to start from when no information is available 

<sup></sup> there are 13 of them 

<sup></sup> a.root-servers.net to m.root-servers.net 

<sup></sup> they are highly replicated servers 

<sup></sup> they are busy, therefore they usually return information on lower zones (not on individual records) 

## Name servers: examp<sup>l</sup>e

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/254eb799-fa42-4cbe-949c-5a21e6034691/1584b1eafe45651946e399fad6c344d2eaa6c23118b5cb808653d472b9c714c2.jpg)


## ns<sup>l</sup>oo<sup>k</sup>up examples

<sup></sup> We can perform manually the iterative querying done by a local DNS server 

<sup></sup> Reverse lookup is also possible (get name from address) 

## ns<sup>l</sup>oo<sup>k</sup>up examples

The (default) server is in this case the router: 127.0.0.53 (port 53) 

• The returned records are nonauthoritative (cached) 

• They do not come from the DNS server that manages the zone 

• The local server handles the whole resolution via iterative queries 

• The host issues a recursive query (either the complete answer or an error is returned) 

```txt
andrea@turgia:~$ nslookup www.vatican.va
Server: 127.0.0.53
Address: 127.0.0.53#53 
```

Non-authoritative answer: www.vatican.va canonical name = wcm-disp.spc.va. Name:wcm-disp.spc.va Address: 185.152.70.33 

## Types o<sup>f</sup> DNS quer<sup>i</sup>es

<sup></sup> Local DNS servers manage recursive queries 

<sup></sup> service to their hosts 

<sup></sup> Many DNS servers (the busy ones, e.g. the ones closer to the top) do not handle recursive queries 

## Types o<sup>f</sup> DNS records

<sup></sup> Records are either authoritative or cached 

<sup></sup> Cached records expire (recall TTL) 

<sup></sup> Caching helps performances 

<sup></sup> All answers are cached 

<sup></sup> The address can be returned immediately by the local server if cached 

<sup></sup> If a request for the address of cs.mit.edu comes and the server has the address of the DNS server for mit.edu, such server can be queried. 

<sup></sup> Root servers are only queried in the absence of any information on a certain domain. 

gaia.cs.umass.edu 

## Application Layer DNS: Resolver

• There is another important type of DNS server called the local DNS server (or DNS resolver). 

• A local DNS server does not strictly belong to the hierarchy of servers and is typically managed by ISPs. 

• Google also provides similar servers all around the world (Google Public DNS) on address 8.8.8.8 or 8.8.4.4. 

• When a host connects to an ISP, the ISP provides the host with the IP addresses of one or more of its local DNS servers (that are typically “close to” the host). 

• When a host makes a DNS query, the query is sent to the local DNS server, which acts as a proxy, forwarding the query to the DNS server hierarchy. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-23/254eb799-fa42-4cbe-949c-5a21e6034691/4a1ebf16926347f2607413671a9527dbaf147d4256e55cb70353628f1b32c03e.jpg)


## Application Layer DNS: Aliasing

• DNS provides an aliasing service for servers in which complicated/long names (aka canonical) are associated to a more simple/short ones (aka alias). 

• Host aliasing: hosts with complicated hostnames can be associated to more mnemonic aliases. 

• Example: relay1.west-coast.enterprise.com -> www.enterprise.com 

• Note that DNS can still be invoked by an application to obtain the canonical (original) hostname for a supplied alias as well as the associated IP address. 

## Application Layer DNS: Load Distribution

• A DNS can be used to perform load distribution among replicated servers (aka, round-robin DNS). 

• Typically, busy sites (e.g., google, amazon, CNN, etc.) are replicated over multiple servers, with each server running on a diferent end system and each having a diferent IP address (multiple IP addresses associated with one canonical hostname). 

• The DNS database contains this set of IP addresses. When clients make a DNS query for a name mapped to a set of addresses, the server may rotate the order in which addresses are replied. 