# Lezione 1: Introduzione alle reti di calcolatori

## Cosa sono le reti di calcolatori

Il networking è il processo di collegare tra loro calcolatori affinché possano condividere informazioni. Una **rete di calcolatori** è un insieme di dispositivi di calcolo interconnessi e autonomi: un numero elevato di calcolatori separati ma connessi svolge un lavoro comune e può scambiarsi informazioni.

**Internet** è la rete di calcolatori più importante al mondo e, anzi, è una **rete di reti**: tecnicamente si tratta di un'enorme *Wide Area Network* (WAN) che connette sotto-reti e dispositivi tra nazioni e continenti diversi. Comprende centinaia di milioni di dispositivi di rete, collegamenti e calcolatori che offrono centinaia di servizi agli utenti; esistono comunque anche reti più piccole, locali o disconnesse da Internet.

### Usi delle reti

Le reti servono per accedere alle informazioni, per la comunicazione da persona a persona, per il commercio elettronico, per l'intrattenimento e per l'**Internet delle cose** (IoT).

### Storia di Internet

L'idea di una rete "universale" fu teorizzata dai ricercatori (in particolare J.C.R. Licklider) intorno al 1950 e iniziò a diventare realtà quasi dieci anni dopo. Le tappe fondamentali sono:

- L'**Advanced Research Projects Agency** (ARPA) del Dipartimento della Difesa statunitense assegnò contratti per lo sviluppo del progetto **ARPANET** (1969).
- R. Kahn (ARPA) e V. Cerf (Stanford) progettarono il Transmission Control Protocol (TCP) e l'Internet Protocol (IP), due protocolli della **suite di protocolli Internet** (1974).
- La National Science Foundation (NSF) finanziò il progetto **NSFNET**, una rete basata su TCP/IP (1986).
- **ARPANET fu dismesso** nel 1990; **NSFNET fu dismesso** nel 1995, rimuovendo le ultime restrizioni all'uso di Internet per il traffico commerciale.

L'ARPANET iniziale aveva quattro nodi (SRI, UCLA, UCSB e UTAH, 1969) e nasceva come rete chiusa, pensata per università e centri di ricerca; reti simili furono create indipendentemente in tutta Europa e negli USA. NSFNET e il protocollo TCP/IP realizzarono l'idea di *rete di reti*, ma sia ARPANET che NSFNET presentavano **restrizioni commerciali**.

## Componenti della rete

I dispositivi di rete e i collegamenti (*link*) costituiscono l'infrastruttura che permette agli host di connettersi: router, access point, switch e hub. Gli **host** sono invece i dispositivi su cui girano le applicazioni, come laptop, server, smartphone e PC.

### Reti e grafi

Le reti di calcolatori condividono la terminologia con la teoria dei grafi. I dispositivi connessi tramite la rete sono chiamati **nodi**, mentre le connessioni tra nodi sono chiamate **collegamenti** (o **canali**) di comunicazione. Una sequenza di nodi e collegamenti forma un **cammino** (*path*). I punti terminali della rete, che forniscono o usano **servizi**, sono nodi speciali chiamati **host**: idealmente sono le foglie della rete (anche se spesso non è vero), mentre i nodi intermedi sono dispositivi di routing come router e switch.

![[Lezione 1-1790182515582.png|309]]

### Comunicazione dei dati

La comunicazione dati coinvolge cinque componenti principali:

- Il **messaggio**, che contiene i dati da trasmettere.
- Il **mittente**, l'entità che invia il messaggio.
- Il **destinatario**, l'entità che dovrebbe riceverlo.
- Il **mezzo**, il canale tra mittente e destinatario in cui viaggia il messaggio.
- Il **protocollo**, un insieme di regole di comunicazione note a mittente e destinatario.

![[Lezione 1-1790182376439.png|420|420x115]]

I dati da scambiare possono essere rappresentati in forme diverse (testo, numeri, immagini, audio, video). A seconda del tipo e dello scopo della comunicazione, il **flusso dei dati** può essere **simplex** (monodirezionale), **half-duplex** (bidirezionale a turni) o **full-duplex** (bidirezionale simultaneo).

### Velocità di trasmissione, banda e throughput

Questi tre termini si distinguono per ciò che misurano. 
- La **velocità di trasmissione** è la quantità **massima** di informazione che un **dispositivo** può trasmettere, misurata in bit/s (o byte/s). 
- La **banda** (*bandwidth*) è la quantità **massima** di informazione che un **cammino** (link + nodi) può trasmettere, sempre in bit/s. 
- Il **throughput**, infine, è la quantità **effettiva** (istantanea) di informazione che viene realmente trasmessa su un cammino.

### Tipi di connessione

Gli host di una rete possono essere connessi in modi diversi: **punto-punto**, quando viene fornito un collegamento dedicato tra due dispositivi (wireless o cablato), oppure **multipunto** (broadcast), quando più di due dispositivi condividono un singolo collegamento.

### Architetture di comunicazione

Nel modello **client-server**, un client richiede esplicitamente informazioni a un server che le ospita: il processo client invia un messaggio attraverso la rete al processo server e attende un messaggio di risposta. In un sistema **peer-to-peer**, invece, non esistono client e server fissi.

## Topologie di rete

La **topologia di rete** è la disposizione degli elementi (link, nodi, ecc.) di una rete di comunicazione. Le topologie principali sono:

### Bus

Nella topologia **bus** gli host sono connessi a un cavo dorsale centrale, e quindi sono possibili **collisioni**. È una soluzione semplice ed economica, adatta a reti piccole; il difetto principale è che il bus è un singolo punto di guasto, anche se le sotto-reti possono rimanere disponibili. Una rete bus ha un collegamento fisico duplex (una dorsale più n link).

![[Lezione 1-1790195672276.png|207]]
### Ring

Nella topologia **ring** ogni host è connesso punto-punto esattamente ad altri due, e il segnale viene **inoltrato** lungo l'anello, da dispositivo a dispositivo, fino a raggiungere la destinazione. È semplice ed economica, con prestazioni migliori del bus; tuttavia aggiungere nuovi nodi è più difficile e i nodi guasti possono compromettere la rete. Una rete ring ha $n$ collegamenti duplex.

![[Lezione 1-1790195640079.png|146]]
### Star

Nella topologia **star** gli host sono collegati a un controllore centrale (hub, switch o router), senza collegamenti diretti tra host: è il controllore a reindirizzare i messaggi. È meno costosa, semplice, robusta e più scalabile delle precedenti, ma il controllore deve essere raggiungibile da tutti gli host e rappresenta un singolo punto di guasto. Una rete star ha un controllore e $n$ collegamenti fisici duplex.

![[Lezione 1-1790195698195.png|133]]
### Tree

La topologia **tree** integra più topologie star, tipicamente tramite un cavo bus. È versatile, scalabile e robusta, ed è ben supportata dai fornitori di hardware e software; in compenso è difficile da configurare ed eredita la debolezza del bus.

![[Lezione 1-1790195701360.png|200]]
### Mesh

Nella topologia **mesh** gli host sono collegati punto-punto in modo non gerarchico. Si distingue tra **full mesh**, in cui tutti i nodi sono pienamente connessi, e **partial mesh**, in cui i nodi sono connessi solo ad alcuni altri. Offre traffico ridotto, robustezza, sicurezza e collegamenti dedicati, ma è difficilmente scalabile e costosa, perché richiede dispositivi con più porte. Una rete full mesh ha $n(n-1)/2$ collegamenti fisici duplex.

![[Lezione 1-1790195717867.png|230]]![[Lezione 1-1790195745017.png|196]]
### Ibrida

Le topologie possono essere **combinate** in una rete ibrida, per esempio una dorsale star con tre reti bus.

![[Lezione 1-1790195783748.png|391]]
## Categorie di reti

Le reti si classificano per dimensione, numero di host e banda in **PAN** (Personal Area Network), **LAN** (Local Area Network) o **WLAN** (Wireless LAN), **MAN** (Metropolitan Area Network) e **WAN** (Wide Area Network).
#### PAN

Le PAN permettono ai dispositivi di comunicare entro il raggio di una persona. **Bluetooth** è una rete wireless a corto raggio usata per connettere componenti senza cavi.

#### LAN e rete casalinga

Una LAN domestica connette una gamma ampia e diversificata di dispositivi a Internet, e deve essere gestibile, affidabile e sicura; l'IoT permette di connettere quasi qualsiasi dispositivo. Le proprietà richieste a una rete domestica sono: facile da installare, sicura e affidabile, con interfacce compatibili tra tutti i prodotti e costi ridotti dei dispositivi.

#### MAN

In una MAN sia i segnali televisivi che Internet vengono immessi nel centralino via cavo (*cable head-end*, o cable modem termination system) per la successiva distribuzione alle abitazioni.

#### WAN

Le WAN mostrano come host in città diverse possano comunicare tramite linee dedicate (*leased line*), via Internet o tramite un ISP. La complessità della topologia cresce con le dimensioni della rete: le WAN che connettono nazioni o continenti possono essere molto complesse ed eterogenee.

## Internet Service Provider (ISP)

L'accesso a Internet è il servizio base. Un **Internet Service Provider** (ISP) è un'organizzazione che fornisce servizi per accedere, utilizzare o partecipare a Internet; può essere commerciale, comunitario, no-profit o privato (per esempio un'azienda o un'università). Diversi ISP si scambiano dati tramite Network Access Point (NAP) neutri o Internet Exchange Point (IXP).

La rete di un ISP è definita gerarchicamente:

- Un punto di presenza (**PoP**) è un gruppo di uno o più router usati dall'ISP per raggiungere i clienti.
- Gli **access ISP** coprono aree locali.
- I **regional ISP** coprono aree più ampie.
- I **national ISP** coprono intere nazioni.
- Un **Internet Exchange Point** (IXP) funge da punto d'incontro tra più ISP, spesso non gestito dagli ISP coinvolti.

![[Lezione 1-1790196095424.png|391]]
Structure of a national ISP

![[Lezione 1-1790196285957.png|389]]
Interconnection of national ISPs

## Connessione a Internet

Le connessioni private a Internet si stabiliscono tramite modem o ONT collegato alla rete telefonica. Le tecnologie, in ordine cronologico e di capacità, sono:

- Analogica (56 kbps).
- ISDN (Integrated Services Digital Network, 128 kbps).
- ADSL (Asymmetric Digital Subscriber Line, da 1 a 20 Mbps).
- Doppino in rame (da 10 a 100 Mbps).
- Fibra ottica (da 50 Mbps a 40 Gbps), tramite ottico di rete (ONT), senza (de)modulazione.

Le aziende, soprattutto medie e grandi, possono invece avere un collegamento diretto o dedicato all'ISP.
![[Lezione 1-1790196393884.png|289]]