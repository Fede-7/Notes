# Lezione 17 — Il Network Layer: gestione degli indirizzi

## Ruolo del network layer e protocollo IP

Il network layer fornisce consegna **host-to-host**: incapsula segmenti in datagrammi e li inoltra verso l'host di destinazione attraverso i router (nodi con porte in ingresso/uscita, un modulo di switching che collega le porte e un processore di controllo che crea le tabelle di inoltro).

Il **protocollo IP (Internet Protocol)** è il protocollo di network layer che realizza questa consegna. Esistono due versioni in uso:

- **IPv4**: la più diffusa e comune.
- **IPv6**: versione più recente, proposta per sostituire IPv4.

La funzionalità più importante dell'IP è l'**indirizzamento**: assegnare indirizzi univoci ai dispositivi della rete.

## Indirizzi IPv4

> [!def] Indirizzo IP (IPv4)
> Stringa di **32 bit** (4 byte) che identifica univocamente un'interfaccia nella rete globale. Viene scritto in **notazione decimale puntata**: ogni byte in forma decimale, separato da punti (es. `193.32.216.9`).

Con 32 bit sono possibili $2^{32}$ indirizzi, circa 4 miliardi.

### Interfacce

- L'host è collegato alla rete tramite un **link**; il confine tra host e link fisico è l'**interfaccia**.
- Un host ha tipicamente una sola interfaccia, un router ne ha molteplici.
- Poiché ogni host e router può inviare e ricevere datagrammi IP, **ogni interfaccia deve avere il proprio indirizzo IP**: l'indirizzo è associato tecnicamente all'interfaccia, non al dispositivo.

## Subnetting

Assegnare indirizzi a caso sarebbe insensato:

- gli IP non indicherebbero la posizione degli host;
- servirebbero tabelle di inoltro enormi nei router.

L'indirizzamento ricalca quello telefonico: le reti sono **gerarchicamente** divise in sottoreti (**subnet**) con prefissi diversi. Un indirizzo IP si divide in due parti:

- **parte di subnet** (a sinistra): identifica la sottorete a cui il nodo è collegato;
- **parte di interfaccia** (a destra): identifica la singola interfaccia.

Il numero di bit delle due parti non è fisso.

### Subnet mask

> [!def] Subnet mask
> Maschera che specifica quali bit dell'indirizzo appartengono alla parte di subnet. In notazione **slashed** (CIDR), `193.32.216.0/24` indica che i 24 bit più a sinistra sono dedicati alla subnet.

Le maschere valide hanno tutti gli **1 a sinistra e contigui**:

| Dotted-decimal | Binario | Valida? |
| --- | --- | --- |
| 255.255.255.0 | 11111111 11111111 11111111 00000000 | /24 ✔ |
| 255.255.128.0 | 11111111 11111111 10000000 00000000 | /17 ✔ |
| 255.224.0.0 | 11111111 11100000 00000000 00000000 | /11 ✔ |
| 255.255.10.0 | 11111111 11111111 00001010 00000000 | ✘ (non è una subnet mask) |
| 63.255.255.0 | 00111111 11111111 11111111 00000000 | ✘ (non è una subnet mask) |

Per verificare se due host sono nella stessa subnet basta confrontare i loro prefissi. Host in subnet diverse possono comunque comunicare, ma gli amministratori possono trattare (filtrare/bloccare) i messaggi in ingresso/uscita dalle subnet in modo diverso.

### Router e subnet

Il router è il dispositivo che interconnette subnet diverse: ha più porte fisiche, con interfacce e indirizzi IP diversi, e fa spesso da **gateway** sul bordo di più subnet. Per la sua posizione privilegiata offre spesso servizi aggiuntivi al semplice routing: **NAT**, **DHCP**, **firewall**.

Un classico esempio: un router con tre interfacce collega sette host divisi in 3 subnet — `223.1.1.0/24`, `223.1.2.0/24`, `223.1.3.0/24` — con l'interfaccia del router che appartiene a ciascuna subnet. Con tre router interconnessi da link punto-a-punto, anche i link tra router formano subnet proprie: in un esempio simile si contano **6 subnet** (3 router-host, 3 router-router).

> [!info] ifconfig / ip
> Su Linux si ispeziona la configurazione di rete (indirizzi, maschere, interfacce) con `ifconfig` (equivalente Windows: `ipconfig`), oppure con il comando più moderno `ip`.

## Indirizzamento in Internet

Su Internet miliardi di dispositivi devono essere connessi: gli indirizzi vanno assegnati con cura per evitare:

- tabelle di inoltro troppo grandi nei router;
- interfacce con lo stesso indirizzo;
- esaurimento degli indirizzi.

Gli indirizzi vengono assegnati fornendo **subnet alle organizzazioni** in due modi:

1. **Classful addressing** (storico, non più usato in pratica);
2. **Classless addressing** (attuale).

### Classful addressing (storico)

| Classe | Formato | Esempio | IP per rete |
| --- | --- | --- | --- |
| A | a.b.c.d/8 | 10.X.X.X | > 16 milioni |
| B | a.b.c.d/16 | 10.10.X.X | 65535 |
| C | a.b.c.d/24 | 10.10.10.X | 254 |

Il problema è lo **spreco**: un'organizzazione che necessita di 300 IP riceve un'intera classe B, sprecando oltre 65000 indirizzi.

### Classless addressing (CIDR)

> [!def] CIDR
> **Classless InterDomain Routing**: un'organizzazione riceve un blocco di qualsiasi forma `a.b.c.d/X`, dove i primi X bit sono il **prefisso** (parte di rete) e l'insieme degli IP riservati è il **blocco**.

- Per 300 IP si assegna ad esempio `241.115.2.0/23` → 512 IP, con solo 212 sprecati.
- I blocchi possono **sovrapporsi**: la lunghezza X del prefisso distingue i blocchi (es. `10.10.10.15/16` e `10.10.10.14/24` non sono nello stesso blocco).
- Un blocco CIDR può essere a sua volta suddiviso in **subnet interne** (es. `241.115.0.0/16` in più /24).

### Aggregazione degli indirizzi

Con l'indirizzamento a prefissi, un router può ricordare **solo il prefisso** comune: un blocco grande (es. `200.23.16.0/20`) aggrega i blocchi /23 delle singole organizzazioni, e i router esterni inoltrano tutto verso lo stesso punto.

> [!info] Route summarization
> L'**aggregazione degli indirizzi** (o *route summarization*) è tanto più efficace quanto più i blocchi sono **contigui/raggruppati** (clustered).

### Ottenere un blocco

1. **Contattare un ISP**, che assegna indirizzi da un blocco più grande già allocato, suddiviso in sotto-blocchi di dimensione variabile secondo la sua politica.
2. **Rivolgersi a ICANN**, autorità globale no-profit che gestisce lo spazio di indirizzi IP (allocando blocchi agli ISP) e i root server DNS.

## Datagramma IPv4

Il pacchetto del network layer di Internet si chiama **datagramma**. Campi principali:

| Campo | Dimensione | Funzione |
| --- | --- | --- |
| Versione | 4 bit | Versione IP del datagramma (4 o 6) |
| Header length | 4 bit | Dimensione dell'header (variabile per le opzioni; senza opzioni = 20 byte) |
| Type of Service (TOS) | 8 bit | Proprietà del datagramma (es. real-time/non-real-time), definite dagli amministratori |
| Datagram length | 16 bit | Lunghezza in byte (header + dati); raramente > 1500 byte (max 65535) |
| Identifier | 16 bit | Numero progressivo che identifica il datagramma (usato nella frammentazione) |
| Flags + offset frammentazione | 3+13 bit | Proprietà e offset del frammento |
| Time-to-live (TTL) | 8 bit | Decrementato di 1 a ogni router; a 0 il datagramma viene scartato |
| Upper-layer protocol | 8 bit | Protocollo di trasporto del payload (es. 6 = TCP, 17 = UDP) |
| Header checksum | 16 bit | Rilevamento errori: complemento a 1 della somma a 16 bit dell'header |
| Source / Destination IP | 32+32 bit | Indirizzi sorgente e destinazione |
| Options | variabili | Estensioni dell'header (rimosse in IPv6) |
| Data | variabili | Payload, tipicamente un segmento TCP/UDP |

> [!warning] Checksum ricalcolato a ogni hop
> Poiché **TTL** e **opzioni** cambiano lungo il percorso, il checksum dell'header deve essere **ricalcolato e memorizzato di nuovo a ogni router**; i datagrammi errati vengono tipicamente scartati.

## Frammentazione IPv4

Ogni tecnologia di link trasporta al massimo una certa quantità di dati per frame.

> [!def] MTU
> Il **Maximum Transmission Unit** è la massima quantità di dati che un frame di link layer può trasportare (es. Ethernet: 1500 byte).

Un router che interconnette due link con MTU diverse può ricevere un datagramma che non entra nel link in uscita: deve dividere il payload in due o più **frammenti**, ciascuno incapsulato in un frame e inoltrato.

Quando un router frammenta:

- copia **identico identificatore, indirizzo sorgente e destinazione** in tutti i frammenti;
- imposta l'**offset** dei frammenti con numeri progressivi;
- imposta a 1 il flag dell'**ultimo frammento** (segnala che la sequenza è terminata).

### Riassemblaggio negli end system

I frammenti vanno riassemblati prima di raggiungere il transport layer (TCP e UDP si aspettano segmenti completi). I progettisti di IPv4 hanno scelto di non riassemblare nei router (complicazione e calo di prestazioni): il **riassemblaggio avviene negli host finali**:

- se arrivano più datagrammi con stessi indirizzi e identificatore, il datagramma originale è stato frammentato;
- l'host ricostruisce il datagramma originale dai frammenti.