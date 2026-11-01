# Lezione 18 — Il Network Layer: DHCP, NAT, IPv6

## Assegnazione degli indirizzi: DHCP

Dentro un blocco di indirizzi, gli IP vanno assegnati alle singole interfacce. L'amministratore può configurarli:

- **manualmente**: assegnazione uno-a-uno agli host;
- **automaticamente**: la rete assegna autonomamente IP liberi agli host che si collegano (approccio più comune).

> [!def] DHCP
> Il **Dynamic Host Configuration Protocol** è il protocollo client-server che assegna automaticamente gli IP. Fornisce inoltre subnet mask, indirizzo del **default gateway** e del **DNS locale**: tutto ciò che serve per entrare nella rete. È **plug-and-play** (tipico delle reti casalinghe); formalmente è un protocollo di **application layer** (usa UDP).

### I 4 passi del DHCP

Un host che si collega scambia messaggi con il server DHCP (che può essere un computer o il router stesso):

1. **DHCP server discovery**: l'host invia in **broadcast** un messaggio di discovery (UDP porta 67) con IP destinazione `255.255.255.255`, IP sorgente `0.0.0.0` (this host) e un ID di transazione casuale.
2. **DHCP server offer**: ogni server risponde in broadcast (porta 68) con un'offerta di configurazione di rete, includendo un possibile IP nel campo *yiaddr* (Your Internet ADDRESS).
3. **DHCP request**: il client seleiona l'offerta accettabile rispondendo (echo) l'offerta al server scelto.
4. **DHCP ACK**: messaggio finale che conferma la transazione.

> [!info] DHCP relay
> Se il server DHCP si trova in una **subnet diversa** da quella dell'host, serve un **DHCP relay agent** (può essere il router stesso) che inoltra i messaggi DHCP: così una sola macchina può servire più subnet.

## Visibilità in Internet e NAT

Non è necessario (né desiderabile) che tutti i dispositivi siano raggiungibili da chiunque: gli indirizzi sono finiti, ed esporre dispositivi locali (es. una stampante) è irragionevole. Inoltre gli amministratori locali non sempre controllano la struttura del blocco IP sovrastante.

> [!def] NAT
> Il **Network Address Translation** (network masquerading) rimappa gli indirizzi IP dei pacchetti attraverso una **tabella di traduzione** che associa coppie IP/porta **locali (LAN)** a una coppia IP/porta **globale (WAN)**. Il servizio è offerto dai router. La rete mascherata si chiama **rete privata**: i suoi IP sono validi solo al suo interno.

### Funzionamento

- I pacchetti **in uscita** hanno IP sorgente e porta sovrascritti con l'IP WAN del router e una **porta nuova** (es. 5001).
- I pacchetti **in entrata** hanno IP destinazione e porta sovrascritti con l'IP locale dell'host e la porta originale.
- La porta iniziale **non può essere riusata** nella traduzione: host diversi, non consapevoli del traffico altrui, potrebbero scegliere la stessa porta simultaneamente.
- Essendo la porta a 16 bit, un NAT può gestire **oltre 60000 connessioni simultanee**.

## Indirizzi IP riservati

Gli amministratori locali devono poter organizzare una rete privata senza interferenze: esistono blocchi **riservati** che ISP/ICANN non possono assegnare.

| Blocco | Significato |
| --- | --- |
| 10.0.0.0 – 10.255.255.255 | Rete privata |
| 192.168.0.0 – 192.168.255.255 | Rete privata |
| 127.0.0.0 – 127.255.255.255 | Loopback (di solito `127.0.0.1`, indica la macchina stessa) |
| 0.0.0.0 | Rete corrente (host-part a 0) |
| 255.255.255.255 | Broadcast (host-part a 255) |

> [!warning] Perché riservare?
> Gli indirizzi privati possono **coincidere** con indirizzi pubblici: senza riserva il routing nella rete sarebbe **ambiguo**.

## Reachability: ping e nmap

- **ping** (Packet Internet Groper): utility basata su **ICMP** (Internet Control Message Protocol); invia un *echo request* a cui l'host risponde con un *echo reply*. Misura anche l'**RTT** tra richiesto e risposta. Uso: `ping [indirizzo]` (identico su Linux/Windows).
- **nmap**: oltre alla port scanning, mappa i dispositivi della rete affidandosi al ping (ICMP) per la *host discovery*: `sudo nmap -sn [gateway]/[bit di subnet]`.

## IPv6

Negli anni '90 l'**IETF** (ONG fondata nel 1986) iniziò a sviluppare il successore di IPv4 per far fronte alla **penuria di indirizzi a 32 bit**. IPv6 garantisce più indirizzi ed è anche l'occasione per aggiornare altri aspetti di IPv4.

> [!info] Che fine ha fatto IPv5?
> Proposto nel 1979, basato sul protocollo sperimentale Internet Stream Protocol (ST): manteneva indirizzi a 32 bit e fu **abbandonato** proprio per la penuria di indirizzi.

### Datagramma IPv6

Vantaggi rispetto a IPv4:

- **Indirizzamento esteso**: da 32 a **128 bit** ($3{,}4 \times 10^{38}$ indirizzi — "ogno granello di sabbia del pianeta può avere un IP");
- **header a lunghezza fissa di 40 byte**: alcuni campi di IPv4 eliminati o resi opzionali;
- **flow labeling**: i pacchetti di certe applicazioni (es. streaming audio/video) possono essere raggruppati in un unico *flusso* identificato (l'uso preciso è ancora in discussione).

Campi del datagramma IPv6:

| Campo | Dimensione | Funzione |
| --- | --- | --- |
| Versione | 4 bit | Numero di versione (6) |
| Traffic class | 8 bit | Come il TOS di IPv4: priorità ai datagrammi (es. VoIP su SMTP) |
| Flow label | 20 bit | Identifica un flusso di datagrammi |
| Payload length | 16 bit | Byte del payload (esclusi i 40 byte di header) |
| Next header | 8 bit | Protocollo di livello superiore destinatario (come *protocol* in IPv4) |
| Hop limit | 8 bit | Come il TTL di IPv4 (decrementato a ogni inoltro) |
| Source / Destination address | 128+128 bit | Indirizzi IPv6 |
| Data | variabile | Payload |

### Cosa manca rispetto a IPv4

- **Frammentazione**: IPv6 **non consente frammentazione sui router intermedi**, ma solo sugli host. Se un datagramma è troppo grande per essere inoltrato, il router lo scarta e invia al mittente un messaggio di errore *"Packet Too Big"*: il mittente reinvia con dimensioni minori.
- **Header checksum**: costa tempo sui router ed è ridondante (il link layer fa già checksum sull'intero pacchetto).
- **Options**: non più parte dell'header standard; alcune opzioni si specificano nel campo *next header*.

### Da IPv4 a IPv6

Il grosso problema: IPv6 **non è retrocompatibile** — i sistemi IPv4 non sanno gestire datagrammi IPv6. Due strade possibili:

- **Flag day**: a una data prefissata tutte le macchine si spengono e si aggiornano. Fu già un disastro quando si introdusse TCP (con una rete piccolissima); impensabile oggi con miliardi di dispositivi.
- **Tunneling** (approccio realistico, già usato): router dedicati (*tunnel*) si occupano di **mappare datagrammi IPv4 in IPv6 e viceversa** in modo quasi trasparente.

> [!info] Adozione
> L'adozione di IPv6, inizialmente lenta, sta accelerando.