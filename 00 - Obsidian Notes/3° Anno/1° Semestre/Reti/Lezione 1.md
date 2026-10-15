# Introduzione alle reti di calcolatori

## Rete di calcolatori

> [!def] Rete di calcolatori
> **Insieme di dispositivi di calcolo autonomi ma interconnessi**: un numero elevato di computer separati che, grazie ai collegamenti, possono **scambiarsi informazioni** per svolgere un lavoro comune.

Gli usi principali delle reti di calcolatori sono:

- **Accesso all'informazione**, tipicamente secondo il modello client-server o peer-to-peer.
- **Comunicazione persona-persona** ed e-commerce.
- **Intrattenimento** e *Internet of Things* (quasi qualsiasi dispositivo può connettersi).

Nel **modello client-server** un client richiede esplicitamente informazioni a un server che le ospita; il processo client invia una richiesta in rete e attende la risposta. In un sistema **peer-to-peer** non esistono client e server fissi.

## Internet

> [!def] Internet
> **Rete di reti**: la più grande rete di calcolatori, tecnicamente un enorme **WAN** che collega sotto-reti e dispositivi su nazioni e continenti.

Cronologia essenziale:

- **1950 ca.**: l'idea di una rete "universale" viene teorizzata (J.C.R. Licklider).
- **1969**: l'ARPA (U.S. Dept. of Defense) finanzia **ARPANET**, inizialmente una rete chiusa di università e centri di ricerca (primi nodi: SRI, UCLA, UCSB, Utah).
- **1974**: R. Kahn e V. Cerf progettano **TCP** e **IP**, i due protocolli della *Internet protocol suite*.
- **1986**: la NSF finanzia **NSFNET**, rete basata su TCP/IP; essa e TCP/IP avviano l'idea di *network of networks*, ma entrambe le reti hanno restrizioni commerciali.
- **1990**: ARPANET viene dismessa; **1995**: NSFNET viene dismessa, rimuovendo le ultime restrizioni al traffico commerciale.

## Componenti di una rete

La rete distingue l'infrastruttura dai sistemi finali:

- **Dispositivi di rete** (*network devices*): router, switch, access point, hub, insieme ai **link** (canali di comunicazione), formano l'infrastruttura che permette ai host di connettersi.
- **Host**: i dispositivi su cui girano applicazioni o programmi (PC, laptop, smartphone, server).

> [!aside]
> Le reti condividono la terminologia della teoria dei grafi:
> 
> - I dispositivi connessi sono i **nodi**, le connessioni sono i **link** (o canali).
> - Una **sequenza** di nodi e link è un **cammino** (*path*).
> - I **host** (o sistemi finali) sono i nodi che producono o usano i **servizi**; idealmente sono le foglie della rete, mentre i nodi intermedi sono dispositivi di instradamento.
> 
> ---
> 
> ![[Lezione 1-1790182515582.png|250]]

## Comunicazione dei dati

> [!def] Comunicazione dei dati
> Scambio che coinvolge cinque componenti: **messaggio** (i dati da trasmettere), **mittente**, **destinatario**, **mezzo** (canale tra mittente e destinatario) e **protocollo** (regole di comunicazione note a entrambi).

![[Lezione 1-1790182376439.png|300]]

I dati si rappresentano in forme diverse: testo, numeri, immagini, audio, video. Il **flusso** dipende dal tipo e dallo scopo della comunicazione:

- **Simplex**: monodirezionale.
- **Half-duplex**: bidirezionale, ma a turni alterni.
- **Full-duplex**: bidirezionale simultaneo.

Tre grandezze misurano il flusso, in bit/s (o byte/s):

- **Transmission rate**: quantità *massima* di informazione trasmissibile da un *dispositivo*.
- **Banda (bandwidth)**: quantità *massima* trasmissibile da un *cammino* (link e nodi).
- **Throughput**: quantità *effettiva* (istantanea) trasmessa su un cammino.

Le connessioni tra host possono essere di due tipi:

- **Point-to-point**: link dedicato tra due soli dispositivi (cablato o wireless).
- **Multipoint (broadcast)**: più di due dispositivi condividono lo stesso link.

## Topologie di rete

> [!def] Topologia di rete
> **Disposizione** degli elementi (nodi, link) di una rete di comunicazione.

> [!aside]
> - **Bus**: gli host sono collegati a un cavo dorsale centrale; possibili **collisioni**; semplice ed economica, adatta a reti piccole, ma la dorsale è un punto singolo di guasto. Ha 1 link fisico duplex (o 1 dorsale e `n` link).
> 
> ---
> 
> ![[Lezione 1-1790195672276.png|100]]
> 

> [!aside]
> - **Ring**: ogni host è connesso point-to-point a esattamente altri due; il segnale è **inoltrato** lungo l'anello fino alla destinazione; semplice ed economica, con prestazioni migliori del bus, ma aggiungere nodi è più difficile e un guasto di un nodo può compromettere la rete; ha `n` link duplex.
> 
> ---
> 
> ![[Lezione 1-1790195640079.png|100]]

> [!aside]
> - **Star**: gli host sono collegati a un controllore centrale (hub, switch o router) che reindirizza i messaggi, senza link diretti tra host; economica, semplice, robusta e scalabile, ma il controllore deve essere raggiungibile da tutti ed è un punto singolo di guasto; ha `n` link duplex.
> 
> ---
> 
> ![[Lezione 1-1790195698195.png|100]]

> [!aside]
> - **Tree**: più topologie a stella integrate, tipicamente tramite un cavo bus; versatile, scalabile, robusta e ben supportata, ma difficile da configurare ed eredita la debolezza del bus.
> 
> ---
> 
> ![[Lezione 1-1790195701360.png|100]]

> [!aside]
> - **Mesh**: host collegati point-to-point in modo non gerarchico; nella **full mesh** tutti i nodi sono tra loro connessi ($n(n-1)/2$ link duplex), nella **partial mesh** solo alcuni; poco traffico, robusta, sicura, con link dedicati, ma difficilmente scalabile e costosa.
>
>---
>
![[Lezione 1-1790195717867.png|100]]
![[Lezione 1-1790195745017.png|100]]
>

> [!aside]
> - **Hybrid**: topologie diverse possono essere **mixate** in una rete ibrida.
> 
> ---
> 
> ![[Lezione 1-1790195783748.png|200]]
> 

## Categorie di reti

Le reti si classificano per dimensione, numero di host e banda:

- **PAN** (*Personal Area Network*): dispositivi nel raggio di una persona (es. Bluetooth).
- **LAN/WLAN** (*Local/Wireless Area Network*): rete locale cablata (es. Ethernet switchata) o wireless (es. 802.11).
- **MAN** (*Metropolitan Area Network*): copertura metropolitana (es. distribuzione di TV e Internet tramite *cable head-end*).
- **WAN** (*Wide Area Network*): copertura di nazioni/continenti, tipicamente molto complessa ed eterogenea; la complessità della topologia cresce con la dimensione della rete.

La **rete casalinga** (home LAN) ospita una gamma ampia e diversificata di dispositivi connessi a Internet (IoT): deve essere facile da installare, sicura e affidabile, con interfacce compatibili tra tutti i prodotti.

## ISP e accesso a Internet

> [!def] ISP
> **Internet Service Provider**: organizzazione (commerciale, comunitaria, non-profit, privata) che fornisce servizi di accesso, uso e partecipazione a Internet.

- Le connessioni private avvengono tramite modem/ONT collegato alla rete telefonica; le aziende (medie/grandi) possono avere un collegamento diretto/dedicato all'ISP.
- Differenti ISP si scambiano dati tramite **NAP** (*Network Access Point*) o **IXP** (*Internet Exchange Point*), punti di incontro tra più ISP spesso non gestiti dagli ISP coinvolti.

> [!aside]
> La rete di un ISP è gerarchica:
> 
> - **PoP** (*Point of Presence*): gruppo di uno o più router con cui l'ISP raggiunge i clienti.
> - **Access ISP** per aree locali, **regional ISP** per aree più ampie, **national ISP** a livello di nazione.
> 
> ---
> 
> ![[Lezione 1-1790196095424.png|200]]

> [!aside]
>Tecnologie di connessione privata (in ordine di banda):
>
> - Modem analogico (56 kbps), **ISDN** (128 kbps), **ADSL** (1–20 Mbps), doppino in rame (10–100 Mbps), fibra ottica (50 Mbps–40 Gbps, tramite **ONT** senza (de)modulazione).
> 
> ---
> 
> ![[Lezione 1-1790196393884.png|200]]