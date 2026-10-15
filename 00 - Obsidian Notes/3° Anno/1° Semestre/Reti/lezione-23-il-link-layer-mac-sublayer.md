# Lezione 23 — Il Link Layer: MAC sublayer

## Servizi del link layer (richiamo)

Il link layer offre fino a 4 servizi: **framing**, **link access** (regolato dal MAC), **reliable delivery** (per lo più opzionale) e **rilevazione/correzione degli errori** (parity check, checksum, CRC).

## Tipi di link

Esistono due tipi fondamentali di link:

- **Punto-punto**: un singolo mittente a un estremo e un singolo ricevitore all'altro (es. link Ethernet diretto tra due computer). Un protocollo di riferimento è **PPP** (Point-to-Point Protocol).
- **Broadcast**: più nodi trasmittenti/riceventi collegati allo **stesso canale condiviso**. Il termine *broadcast* deriva dal fatto che quando un nodo trasmette, **tutti** i nodi sul canale ricevono il frame (es. bus Ethernet, half-duplex Ethernet — raro, i cavi sono oggi full-duplex — e LAN wireless).

L'accesso ai link broadcast va **coordinato** (*multiple access problem*): trasmissioni multiple sullo stesso link possono interferire tra loro.

## Collisioni

> [!def] Collisione
> Se più nodi trasmettono simultaneamente sullo stesso canale broadcast, i frame si **sovrappongono** diventando inintelligibili. Tutti i nodi li ricevono e li scartano come errati (nessun danno), ma: **tutti i frame trasmessi sono persi** e l'**intervallo di tempo è sprecato**.

L'accesso al mezzo fisico (insieme al framing) è regolato dal protocollo **MAC** (Medium Access Control).

## Protocolli di multiple access

I protocolmi di multiple access regolano le trasmissioni sui canali broadcast così che:

- le collisioni siano gestite;
- ogni nodo abbia possibilità di trasmettere (nessun nodo monopolizza il link);
- le connessioni stabilite non vengano interrotte (es. controllo che il link sia libero).

Servono per cablate, wireless e reti satellitari, dove centinaia o migliaia di nodi comunicano direttamente su un canale broadcast.

### Approcci principali

1. **Channel partitioning**: la banda viene partizionata tra i nodi.
2. **Random access**: i nodi "scommettono" sull'accesso.
3. **Taking-turns**: i nodi attendono il proprio turno.

### Desiderata

Un protocollo di multiple access per un canale broadcast di $R$ bps dovrebbe:

- **massimizzare l'uso del canale**: se $M$ nodi hanno dati da inviare, ciascuno deve avere in media un throughput di $R/M$ bps (se $M=1$, throughput $R$);
- essere **decentrato**: un nodo master sarebbe un singolo punto di guasto;
- essere **semplice e leggero**: si inviano tantissimi frame, l'overhead dev'essere nullo.

## Protocolli a partizionamento del canale

### TDMA (Time Division Multiple Access)

Data la trasmissione di $R$ bps su un canale con $N$ nodi, TDMA:

- divide il tempo in **time frame** (step), ciascuno a sua volta suddiviso in **$N$ time slot**;
- **ogni slot è assegnato a uno** degli $N$ nodi;
- il nodo attende il proprio slot per trasmettere (dimensione degli slot tipicamente tale da contenere un intero pacchetto).

### FDMA (Frequency Division Multiple Access)

Divide il canale di $R$ bps in **frequenze diverse** (banda $R/N$ ciascuna), assegnandone una per nodo.

**Pro/contro comuni a TDMA e FDMA**:

- ✔ evitano le collisioni e dividono la banda equamente tra gli $N$ nodi;
- ✘ un nodo è limitato a $R/N$ **anche quando è l'unico** a dover trasmettere.

### CDMA (Code Division Multiple Access)

- Assegna a ogni nodo un **codice** diverso, usato per codificare/decodificare i bit inviati.
- Con codici scelti con cura, i nodi possono **trasmettere simultaneamente senza interferire**.
- Funziona soprattutto su canali wireless: usato in ambito militare (proprietà *anti-jamming*) e nella telefonia cellulare (es. 3G).
- ✘ Complesso da implementare.
- ✘ Non scala bene col numero di nodi.

## Protocolli di random access

Nei protocolli random access:

- il nodo trasmittente trasmette **sempre al pieno rate del canale** ($R$ bps);
- in caso di collisione (almeno 2 nodi trasmettono), **ogni nodo attende un ritardo casuale** prima di ritrasmettere;
- la scelta è **indipendente** tra i nodi: due nodi possono scegliere ritardi sufficientemente diversi da permettere a uno dei due di "infilare" il messaggio; se scelgono ritardi simili, **nuova collisione** e si itera.

### Slotted ALOHA

Funzionamento:

- il tempo è diviso in **slot** (come TDMA), ciascuno grande abbastanza da contenere un frame;
- i nodi sono **sincronizzati**: trasmettono solo **all'inizio** di uno slot;
- se **nessuna collisione** è rilevata nello slot, la comunicazione continua;
- in caso di collisione, ogni nodo coinvolto ha **probabilità $p \in [0,1]$** di ritrasmettere il frame in ciascuno degli slot seguenti, finché non riesce.

Caratteristiche:

- ✔ nodo singolo → pieno rate $R$ del canale (no collisioni);
- ✔ decentralizzato (nodi indipendenti, a parte la sincronizzazione);
- ✔ semplice da implementare ed eseguire (la selezione casuale è rapidissima);
- ✔ collisioni multiple consecutive sono improbabili.

### CSMA (Carrier Sense Multiple Access)

**Debolezza di ALOHA**: si può iniziare a trasmettere (produendo una collisione) **anche se il canale è già occupato** — lo si scopre solo attraverso l'effetto della collisione.

Soluzione: **monitorare il canale** e tentare la trasmissione solo se è libero. CSMA e CSMA/CD si basano su due principi:

- **Carrier sensing**: i nodi ascoltano il canale **prima** di trasmettere; se è in corso la trasmissione di un frame altrui, attendono finché non si rileva silenzio;
- **Collision detection**: i nodi ascoltano il canale **mentre trasmettono**; se rilevano una collisione, **interrompono** la trasmissione e attendono un tempo casuale prima di ricominciare.

> [!warning] Se tutti fanno carrier sensing, perché ci sono comunque collisioni?
> Per il **ritardo di propagazione del segnale**: la propagazione, pur vicina alla velocità della luce, impiega tempo a raggiungere gli altri nodi. Un secondo nodo rileva la trasmissione **solo dopo** che è iniziata; nel frattempo può considerare libero un canale in realtà occupato, producendo la collisione. (Approfondito nella lezione successiva.)