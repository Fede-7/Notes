# Lezione 18: Livello di rete — DHCP, LAN, IPv6

## Assegnazione degli IP: DHCP

Dentro un blocco di indirizzi, gli IP **vanno assegnati alle singole interfacce**. Un **amministratore di sistema** può configurarli in due modi: **manualmente**, assegnando gli IP uno a uno agli host, oppure **automaticamente**, lasciando che la rete assegni autonomamente IP liberi agli host in arrivo. Il secondo approccio (il più comune) usa il **Dynamic Host Configuration Protocol (DHCP)**: oltre all'indirizzo, DHCP fornisce all'host le informazioni per entrare nella rete — subnet mask, indirizzo del **gateway di default** (per uscire dalla rete) e indirizzo del **server DNS locale**. DHCP è **plug-and-play** ed è tipicamente usato nelle case.

### Funzionamento

DHCP è client-server: un host che arriva (client) contatta il server DHCP per ricevere le informazioni di rete; il servizio può essere offerto da un computer o dal router stesso. Formalmente DHCP è un protocollo di **livello applicazione**. Nell'esempio delle 3 subnet collegate da un router, la rete a destra (233.1.2.0/24) ha un server DHCP con cui un nuovo host che entra "tratta" l'IP. Aggiungere un host è un processo in 4 passi:

1. **DHCP server discovery**: il nuovo host invia in broadcast un messaggio DHCP discovery (UDP porta 67) per trovare il server, con IP destinazione 255.255.255.255 (broadcast), IP sorgente 0.0.0.0 (*this host*) e un ID di transazione casuale.
2. **DHCP server offer**: potendoci essere più server, quando un server riceve la discovery risponde in broadcast (porta 68) offrendo una possibile configurazione di rete (campo `yiaddr` – *Your Internet ADDRESS*), con IP destinazione 255.255.255.255 e IP sorgente 223.1.2.5 (server DHCP).
3. **DHCP request**: il nuovo client sceglie l'offerta accettata, riecheggiando il messaggio di offerta.
4. **DHCP ACK**: messaggio ACK finale che conferma la transazione.

Se il server è in **un'altra subnet** serve un **DHCP relay agent** che inoltri i messaggi (può farlo un router): configurando il router come relay agent, anche gli host delle subnet 223.1.1.0/24 e 223.1.3.0/24 saranno serviti dal nostro DHCP.

### Comandi Linux

`ip addr` mostra la configurazione corrente (indirizzo IP, mask); `ip route` mostra il gateway di default.

## Visibilità degli IP e NAT

Su Internet ci sono miliardi di dispositivi da associare a IP univoci **per essere raggiungibili da chiunque**. Ma è davvero necessario che **tutti i dispositivi siano visibili a tutti**? Esporre tutti i dispositivi presenta problemi: gli IP sono finiti; per dispositivi connessi localmente è spesso **irragionevole (o indesiderabile) esporli** su Internet; e gli **amministratori locali** dovrebbero conoscere a fondo la struttura del blocco IP per assegnare indirizzi liberi (spesso non dipende da loro, es. reti domestiche).

### Network Address Translation (NAT)

Il servizio **NAT** permette di **rimappare gli indirizzi IP** dei pacchetti in una rete in indirizzi diversi (**network masquerading**). Si usa una **tabella di traduzione** che associa **più IP/porte locali (della LAN)** a un **IP/porta globale (della WAN)**; il servizio può essere offerto dai **router**. La rete locale mascherata si chiama anche **rete privata** (*realm with private addresses*): gli IP privati sono validi solo dentro la rete privata.

Si consideri un router NAT-enabled le cui quattro interfacce della LAN hanno subnet 10.0.0.0/24: il router si comporta da "passa-messaggi" che sovrascrive gli IP come da tabella. I pacchetti in **uscita** hanno IP/porta sorgente sovrascritti con un singolo IP WAN (138.76.29.7) e una porta nuova (es. 5001); i pacchetti in **ingresso** hanno IP/porta destinazione sovrascritti con l'IP LAN specifico dell'host (es. 10.0.0.1) e la porta iniziale (3345). È importante notare che gli host non conoscono il traffico degli altri, quindi il NAT **non può usare la porta iniziale**, perché più host potrebbero scegliere la stessa porta contemporaneamente; essendo la porta a 16 bit, un NAT può gestire **oltre 60000 connessioni simultanee**.

### Ping

Per verificare se un host è raggiungibile si usa `ping` (uguale su Linux/Windows). **Ping** (*Packet Internet Groper*) si basa su **ICMP** (*Internet Control Message Protocol*) e invia un pacchetto "echo request" a un host, che risponde automaticamente con "echo reply"; ping fornisce anche il **tempo trascorso** tra richiesta e risposta, misurando l'RTT. Uso: `$ ping [indirizzo]`

```
$ ping google.com
PING google.com (142.251.209.46) 56(84) bytes of data.
64 bytes from mil04s51-in-f14.1e100.net (142.251.209.46): icmp_seq=1 ttl=117 time=19.8 ms
64 bytes from mil04s51-in-f14.1e100.net (142.251.209.46): icmp_seq=2 ttl=117 time=20.3 ms
...
```

### Nmap (parte 2)

Oltre alla scansione delle porte, `nmap` può **mappare/scansionare i dispositivi** della rete, usando ping (ICMP) per scoprire gli host. Uso: `sudo nmap -sn [indirizzo gateway]/[bit di subnet]`

```
$ sudo nmap -sn 100.103.0.1/16
Nmap scan report for _gateway (100.103.0.1)
Host is up (0.0024s latency).
MAC Address: 10:BD:18:E5:74:80 (Cisco Systems)
Nmap scan report for 100.103.0.3
...
```

### Indirizzi IP riservati

Poiché gli amministratori locali devono poter **organizzare una rete privata senza interferenze**, esistono per convenzione **blocchi IP riservati**, che ISP/ICANN non possono assegnare:

- 10.0.0.0 – 10.255.255.255 (riservato alle **reti private**).
- 192.168.0.0 – 192.168.255.255 (riservato alle **reti private**).
- 127.0.0.0 – 127.255.255.255 (indica questa macchina, **loopback**; tipicamente si usa 127.0.0.1).
- 0.0.0.0 (indica la **rete corrente**; anche tutti gli indirizzi con 0 nella parte host).
- 255.255.255.255 (**broadcast**; anche tutti gli indirizzi con 255 nella parte host).

La necessità di riservare IP nasce dal fatto che **gli indirizzi privati possono coincidere con quelli pubblici**: il routing dentro la rete sarebbe **ambiguo**.

## Esempio: setup di una LAN

Si vuole creare **una nuova sottorete locale (LAN) dentro una rete preesistente (WAN)**. L'amministratore del WAN fornisce: l'IP del WAN (150.100.0.0/16), l'IP del gateway verso la WAN esterna/Internet (150.100.50.1) e un IP libero per la nostra rete (150.100.50.10). Configuriamo router e dispositivi con un **router NAT-enabled**; l'IP della nuova LAN sarà 192.168.1.0/24 (riservato alle reti locali).

### Configurazione lato WAN

Il router locale ha **2 interfacce** (WAN e LAN). Lato WAN si specificano: l'indirizzo IP del router nel WAN, la subnet del WAN, il gateway e uno o più DNS:

```
Internet Connection Type: Static IP
IP Address:      150.100.50.10
Subnet Mask:      255.255.0.0
Default Gateway:  150.100.50.1
Primary DNS:      8.8.8.8
Secondary DNS:    4.4.4.4 (opzionale)
```

Si può indicare un **IP dinamico** se il WAN ha un servizio DHCP.

### Configurazione lato LAN

Si dà un IP all'interfaccia LAN del router: essendo la rete 192.168.1.0/24, si assegna 192.168.1.1/24 (è tipico dargli il .1). Il router fornisce anche **DHCP**, quindi si specificano l'**address pool** (per gli host DHCP), il **lease time** (durata dell'assegnazione, dopo la quale l'IP può essere riusato) e **gateway/DNS** da comunicare agli host:

```
MAC Address: 48-22-54-16-18-7D
IP Address: 192.168.1.1
Subnet Mask: 255.255.255.0

DHCP Server: [x] Enable
IP Address Pool: 192.168.1.100 - 192.168.1.250
Address Lease Time: 120 minutes
Default Gateway: 192.168.1.1
```

### Configurazione di un host

L'host può essere configurato in modo **automatico (DHCP)**, usando DHCP per configurare la connessione (IP da 192.168.1.100 a 192.168.1.250), oppure **manuale**, impostando a mano (serve conoscere la configurazione e gli IP disponibili) l'indirizzo IP statico dell'host, la subnet mask, il gateway e i DNS. Gli host connessi **inviano i pacchetti al router locale** (ignari del WAN esterno), e il router locale **inoltra i pacchetti al router WAN** (e possibilmente a Internet). Un nuovo host può usare un IP manuale **fuori dal pool DHCP** o automatico **dentro il pool**.

## IPv6

Nei primi anni '90 l'**IETF** iniziò a sviluppare un successore di IPv4, per far fronte alla **penuria di indirizzi a 32 bit**. IPv6 fu progettato per **garantire più indirizzi**, ma anche per **aggiornare altri aspetti di IPv4** sulla base dell'esperienza operativa maturata. Non è certo quando gli IPv4 si esauriranno (si speculava 2008 o 2018, ma ne restano ancora). Quanto ad **IPv5**, fu proposto nel 1979, basato sul protocollo sperimentale *Internet Stream Protocol* (ST); usava ancora indirizzi a 32 bit, quindi fu **abbandonato proprio per la scarsità di indirizzi**.

### Il datagram IPv6

I vantaggi principali di IPv6 sono:

- **Indirizzamento ampliato**: da 32 a **128 bit** ($3{,}4028237\times10^{38}$ indirizzi): non si esauriranno mai — ogni granello di sabbia del pianeta può avere un IP.
- **Header a lunghezza fissa di 40 byte**: alcuni campi di IPv4 sono stati eliminati o resi opzionali.
- **Flow labeling**: i pacchetti di alcune applicazioni (es. streaming audio/video) possono essere raggruppati in un **flusso** con identificazione specifica; il ruolo preciso dei flow è ancora in discussione.

I campi del datagram IPv6 sono:

- **Version** (4 bit): numero di versione (in IPv6 vale 6).
- **Traffic class** (8 bit): come il TOS di IPv4, dà priorità ai datagram (es. VoIP su SMTP).
- **Flow label** (20 bit): identifica un flusso di datagram.
- **Payload length** (16 bit): byte del payload (header di 40 byte escluso).
- **Next header** (8 bit): protocollo di livello superiore cui consegnare i dati (es. TCP o UDP); simile al campo protocol di IPv4.
- **Hop limit** (8 bit): il time-to-live come in IPv4 (decrementato a ogni inoltro).
- **Indirizzi sorgente e destinazione** (128+128 bit).
- **Data** (variabile): il payload del datagram.

### Cosa manca rispetto a IPv4

- **Campi di frammentazione**: IPv6 **non consente frammentazione/riassemblaggio sui router intermedi**, solo sugli host. Se un datagram è troppo grande per essere inoltrato, il router lo **scarta** e invia al mittente un errore "Packet Too Big"; il mittente può rispedire con un datagram più piccolo.
- **Header checksum**: costa tempo sui router ed è ridondante, perché i protocolli di livello link fanno tipicamente checksum sull'intero pacchetto.
- **Options**: non fanno più parte dell'header standard; alcune opzioni si specificano nel campo next header (insieme agli identificatori TCP/UDP).

### Da IPv4 a IPv6

Il grande problema è che **IPv6 non è retrocompatibile**: i sistemi IPv4 non sanno gestire datagram IPv6. Come adotterà IPv6 Internet? Con l'approccio **"flag day"**, a una certa data **tutte le macchine di Internet verrebbero spente e aggiornate** da IPv4 a IPv6 — un approccio simile fu usato quando fu introdotto TCP, ma fu un disastro (anche per la piccola rete di allora), e con miliardi di dispositivi è impensabile. L'alternativa è l'approccio **tunneling**: router dedicati (**tunnel**) incaricati di **mappare datagram IPv4 in IPv6** e viceversa, in modo quasi trasparente; è probabilmente l'approccio più realistico ed è **già usato in pratica**. L'adozione di IPv6, inizialmente lenta, sta accelerando.