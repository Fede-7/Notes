# Lezione 23: Livello di collegamento — Sotto-livello MAC

## Richiamo: servizi del livello di collegamento

Il livello di collegamento può offrire fino a quattro servizi, tra loro indipendenti:

1. **Framing**: incapsulare/decapsulare i datagram in/da frame.
2. **Accesso al collegamento**: regolare l'accesso ai collegamenti condivisi (broadcast), compito del protocollo **Medium Access Control (MAC)**.
3. **Consegna affidabile**: garantire che i frame trasmessi sul collegamento vengano ricevuti (per lo più opzionale).
4. **Rilevamento e correzione degli errori**: rilevare gli errori nei frame ed eventualmente correggerli (parity check, checksum, CRC).

## Tipi di collegamento

Esistono fondamentalmente due tipi di collegamento. Nel **collegamento punto-a-punto** vi è un solo mittente a un'estremità e un solo ricevitore all'altra; il **Point-to-Point Protocol (PPP)** è un esempio di protocollo che gestisce tali collegamenti (es. collegamento Ethernet diretto tra due computer). Nel **collegamento broadcast**, invece, più nodi trasmittenti e riceventi sono connessi allo stesso canale condiviso: si dice broadcast perché, quando un nodo trasmette un frame, questo viene ricevuto da tutti i nodi sul canale (bus Ethernet, Ethernet half-duplex — raro, oggi la maggior parte dei cavi è full-duplex — o LAN wireless). Poiché più comunicazioni sullo stesso collegamento possono interferire tra loro, l'accesso ai collegamenti broadcast deve essere coordinato: è il cosiddetto **problema degli accessi multipli**.

## Collisioni

Il problema principale del collegamento broadcast è la **collisione**: se più nodi trasmettono simultaneamente frame sullo stesso canale, tali frame si sovrappongono diventando inintelligibili. I frame collisi vengono ricevuti da tutti i nodi del canale e scartati come errori (nessun danno), però tutti i frame trasmessi sono persi e l'intervallo di tempo è sprecato, poiché il canale è stato usato per trasmettere dati inutili. L'accesso al mezzo fisico, così come il framing, è quindi regolato dal protocollo **MAC (Medium Access Control)**.

## Protocolli di accesso multiplo

Nelle reti di calcolatori i **protocolli di accesso multiplo** (*multiple access*) regolano le trasmissioni sui canali broadcast, così che le collisioni siano gestite, ogni nodo abbia una possibilità di trasmettere — quindi nessun nodo monopolizzi il collegamento — e le connessioni stabilite non vengano interrotte, ad esempio verificando se il collegamento è occupato. Sono necessari in vari contesti, cablati, wireless o satellitari, dove centinaia o migliaia di nodi comunicano direttamente su un canale broadcast.

### Ruolo e approcci

Il ruolo primario di un protocollo di accesso multiplo è in qualche modo **evitare le collisioni**, e ne esistono decine per le diverse tecnologie. Gli approcci principali sono tre:

- **Partizionamento del canale** (*channel partitioning*): la banda è partizionata tra i diversi nodi.
- **Accesso casuale** (*random access*): i nodi "scommettono" per l'accesso.
- **Turni** (*taking-turns*): i nodi aspettano il proprio turno.

### Desiderata

Un protocollo di accesso multiplo per un **canale broadcast di velocità R bps** dovrebbe avere le seguenti proprietà:

- **Massimizzare l'uso del canale**: se M nodi hanno dati da inviare, ciascuno dovrebbe avere in media un throughput di R/M bps (se M=1, il throughput dovrebbe essere R).
- **Essere decentralizzato**: un nodo master sarebbe un singolo punto di guasto.
- **Essere semplice e leggero**: vengono inviati tantissimi frame, quindi non ci deve essere overhead.

## Protocolli a partizionamento del canale

### TDMA (Time Division Multiple Access)

Considerando un canale con N nodi e velocità di trasmissione R bps, il TDMA divide il tempo in **frame temporali** (step) e divide ulteriormente ogni frame temporale in **N slot** temporali. Ogni slot è assegnato a uno degli N nodi, quindi quando un nodo ha un pacchetto da inviare aspetta il proprio slot; tipicamente gli slot sono dimensionati così che un intero pacchetto possa essere trasmesso durante uno slot.

### FDMA (Frequency Division Multiple Access)

Il FDMA divide il canale da R bps in diverse frequenze, ciascuna con banda R/N, e assegna ogni frequenza a uno degli N nodi. FDMA e TDMA condividono pro e contro: evitano le collisioni e dividono equamente la banda tra gli N nodi, però un nodo è limitato alla banda R/N anche quando è l'unico nodo con pacchetti da inviare.

### CDMA (Code Division Multiple Access)

Il CDMA assegna a ogni nodo un **codice diverso** usato per codificare e decodificare i bit dei dati inviati. Se i codici sono scelti con cura, le reti CDMA permettono a nodi diversi di trasmettere simultaneamente senza interferenze. Funziona soprattutto su canali wireless; è stato usato in sistemi militari per le sue proprietà anti-jamming e anche nella telefonia cellulare (es. 3G). Le sue criticità sono la complessità di implementazione e il fatto che non scala bene con il numero di nodi.

## Protocolli ad accesso casuale

Nei protocolli ad accesso casuale un nodo trasmittente **trasmette sempre alla velocità piena** del canale (R bps). Se avviene una collisione, cioè se almeno due nodi stanno trasmettendo, tutti i nodi trasmittenti aspettano un **ritardo casuale** prima di ritentare la ritrasmissione. Poiché la scelta è fatta indipendentemente, è possibile che i due nodi scelgano ritardi sufficientemente diversi, permettendo a uno dei due di far passare il messaggio; se invece viene scelto un ritardo simile, avviene una nuova collisione e il processo è iterato.

### Slotted ALOHA

Il protocollo **slotted ALOHA** si basa su quattro regole:

- Il **tempo è diviso in slot** (come in TDMA), ciascuno abbastanza grande da contenere un frame.
- I nodi sono sincronizzati: ogni nodo trasmette i frame solo all'inizio di uno slot.
- Se nessuna collisione è rilevata nello slot, la comunicazione prosegue.
- Se viene rilevata una collisione, ogni nodo in collisione ha una probabilità $p \in [0,1]$ di reinviare il frame in ciascuno degli slot successivi, finché il frame non è inviato con successo.

Le sue caratteristiche: se c'è un solo nodo, questo usa l'intera velocità R del canale senza collisioni; è **decentralizzato**, poiché i nodi sono totalmente indipendenti (a parte la sincronizzazione); è semplice da implementare ed eseguire, dato che la selezione casuale è rapidissima; ed è improbabile avere collisioni consecutive multiple.

### CSMA e CSMA/CD

Una debolezza di ALOHA è che si può iniziare a trasmettere — producendo una collisione — anche se il canale è già occupato, e lo si capisce solo dall'effetto delle collisioni. Una soluzione è **monitorare il canale** e tentare la trasmissione solo se è inattivo. I protocolli **CSMA (Carrier Sense Multiple Access)** e **CSMA con rilevamento delle collisioni (CSMA/CD)** si basano su due principi:

- **Carrier sensing**: i nodi ascoltano il canale prima di trasmettere; se è in corso la trasmissione di un frame di un altro nodo, aspettano finché non viene rilevata nessuna trasmissione.
- **Collision detection**: i nodi ascoltano il canale mentre trasmettono; se rilevano una collisione, interrompono la trasmissione e aspettano un tempo casuale prima di ripartire.

Resta una domanda chiave: se tutti i nodi fanno carrier sensing, perché le collisioni avvengono comunque? La risposta, legata al ritardo di propagazione, è nella lezione successiva.