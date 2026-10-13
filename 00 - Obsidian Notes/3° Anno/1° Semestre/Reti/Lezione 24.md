# Lezione 24: Sotto-livello MAC, accesso casuale, protocolli senza collisioni, switch e ARP

## Protocolli ad accesso casuale: CSMA

### Perché le collisioni avvengono nonostante il carrier sensing?

La causa è il **ritardo nella trasmissione del segnale**. Anche se la propagazione dei segnali nel canale avviene tipicamente vicino alla velocità della luce, serve tempo per raggiungere tutti gli altri nodi: un secondo nodo rileva la trasmissione solo dopo che è iniziata. Per questo ritardo tra inizio della trasmissione e rilevamento, un nodo può ritenere libero un canale in realtà già in uso, producendo una collisione.

### CSMA puro

1. Il nodo verifica se il canale è occupato.
2. Se il canale è inattivo, invia un frame.

Nel CSMA puro le collisioni non vengono rilevate ma restano possibili: si capisce che un frame è perso solo perché l'**ACK non arriva**.

### CSMA/CD (implementato attualmente su Ethernet)

1. Il nodo verifica se il canale è occupato.
2. Se il canale è inattivo, invia un frame.
3. Mentre trasmette, controlla eventuali collisioni.
4. Se rileva una collisione, interrompe la trasmissione e aspetta un periodo casuale $K \in \{0, \dots, 2^n-1\}$, dove $n$ è il numero di collisioni rilevate sul frame corrente (**binary exponential backoff**).

Grazie al backoff, la probabilità di inviare con successo il frame cresce con il numero di collisioni.

## Protocolli a turni (taking-turns)

### Protocollo di polling

Esiste un **nodo master che seleziona, in modalità round-robin, un nodo alla volta** autorizzato a trasmettere (fino al throughput massimo); il processo è iterato ogni volta che la trasmissione si ferma (es. Bluetooth). Il pro è l'assenza di collisioni; i contro sono il **ritardo di polling** (il tempo per selezionare i nodi) e l'approccio **centralizzato**, che introduce un singolo punto di guasto.

### Protocollo token-passing

Non c'è un nodo master: i nodi si scambiano un **frame speciale chiamato token**, e chi lo riceve è autorizzato a trasmettere, per poi passarlo a un altro nodo. I pro sono l'assenza di collisioni e l'approccio **decentralizzato**; il contro è che sorgono problemi se un nodo dimentica di rilasciare il token, monopolizzando il collegamento.

## Indirizzi MAC

A livello di collegamento i dispositivi sono identificati dagli **indirizzi MAC**: ogni interfaccia di rete ha un MAC specifico (progettato per essere fisso, ma cambiabile) e ogni produttore possiede il proprio insieme di MAC. L'**indirizzo MAC** (o indirizzo fisico) è un indirizzo di livello collegamento composto da **6 byte** ($2^{48}$ indirizzi possibili), spesso in notazione esadecimale:

```
1A:23:F9:CD:06:9B   oppure   1A-23-F9-CD-06-9B
```

Gli indirizzi MAC sono **locali**, mentre gli IP, fuori dalle LAN, sono globali: tutte le interfacce hanno un MAC, ma questo viene usato solo all'interno di una LAN.

### Comunicazione in una LAN

In una LAN, due interfacce A e B comunicano così: A inserisce il MAC di B nel frame e lo trasmette; B riceve il frame e confronta il proprio MAC con il MAC di destinazione del frame; se i due MAC coincidono, il frame è accettato, altrimenti è **scartato** senza coinvolgere il resto dello stack. Esiste anche la possibilità di inviare **messaggi broadcast**, accettati da qualunque MAC: per le LAN con indirizzi da 6 byte (es. Ethernet e 802.11) l'indirizzo broadcast è una stringa di 48 uno consecutivi, cioè `FF-FF-FF-FF-FF-FF`. Poiché in una LAN è tutt'altro che raro che un'interfaccia riceva frame diretti ad altre, il ruolo dell'indirizzo MAC è di **filtrare i frame non intesi** senza disturbare l'host.

## Switch

Gli switch sono l'**equivalente di livello collegamento dei router**: non implementano alcun algoritmo di routing e usano **solo indirizzi MAC**, non gli IP. Il loro ruolo è ricevere i frame in arrivo sui collegamenti in ingresso e inoltrarli sui collegamenti in uscita. Lo switch è **trasparente** agli host e ai router della sottorete, ha **buffer sulle interfacce** e possiede **tabelle di inoltro** che associano indirizzi MAC a interfacce; la tabella viene aggiornata **automaticamente e dinamicamente** (*self-learning*) man mano che si scoprono nuovi dispositivi.

### LAN con switch

Le LAN usano in genere uno o più switch per collegare più dispositivi locali. A differenza dei router, gli switch sono **veloci e plug-and-play**, poiché non esegono alcun algoritmo di routing e coinvolgono solo due livelli dello stack. D'altro canto, le LAN con switch sono **limitate in dimensione** e devono avere **struttura ad albero**: i MAC sono difficili da raggruppare (le tabelle di inoltro possono crescere rapidamente) e, non essendoci routing, i loop sono difficili da evitare.

## ARP (Address Resolution Protocol)

Poiché i protocolli dei livelli superiori lavorano con indirizzi IP, è necessario tradurre IP in MAC: se ne occupa l'**Address Resolution Protocol (ARP)**. Ogni interfaccia ha un **modulo ARP** con una **tabella ARP** che associa ogni IP della LAN a un MAC, con un **tempo di vita (TTL)** dopo il quale la voce viene eliminata (tipicamente 5–20 minuti).

Esempio di tabella ARP:

| Indirizzo IP | Indirizzo MAC | TTL |
| --- | --- | --- |
| 222.222.222.221 | 88-B2-2F-54-1A-0F | 13:45:00 |
| 222.222.222.223 | 5C-66-AB-90-75-B1 | 13:52:00 |

Poiché i MAC sono locali, anche ARP funziona solo su reti locali (LAN).

### Esempio: da C verso A

L'host C (222.222.222.220) vuole inviare un messaggio all'host A (222.222.222.222) e gli serve conoscere anche il MAC associato. Prima di inviare, se A non è presente in tabella, C invia un pacchetto di **ARP request in broadcast** a tutti i dispositivi della rete, cercando l'IP giusto. Tutti i nodi ricevono il pacchetto, ma **solo l'IP cercato risponde** con un messaggio diretto di **ARP reply** (unicast). Un host malevolo può intercettare la richiesta e rispondere con una risposta "contraffatta" (**ARP poisoning**), uno degli attacchi più comuni sulle LAN.

### ARP e gateway (IP non locale)

Se l'IP è fuori dalla rete, il meccanismo passa dal router: il router che collega le due reti deve avere **almeno due interfacce** (2 IP, 2 MAC e 2 tabelle ARP), una dentro ciascuna sottorete. I frame diretti fuori dalla sottorete vengono quindi inviati alla prima interfaccia del router, spostati alla seconda interfaccia e dirottati verso l'host giusto usando la seconda tabella ARP.

## Frame Ethernet

Il frame **Ethernet** è composto dai seguenti campi:

| Campo | Dimensione | Descrizione |
| --- | --- | --- |
| Preamble | 8 byte | Blocco di bit di "sveglia" usato per sincronizzare gli orologi degli adattatori sorgente e destinazione |
| Destination address | 6 byte | MAC dell'adattatore di destinazione |
| Source address | 6 byte | MAC dell'adattatore sorgente che trasmette il frame sulla LAN |
| Type field | 2 byte | Specifica il protocollo di livello rete usato nel frame (potrebbero esserci alternative a IP: ad es. i pacchetti ARP hanno un tipo specifico — 0x0806) |
| Data field | 46–1500 byte | Contiene il datagram IP; il limite massimo è dato dalla MTU di Ethernet: se il datagram la supera, viene frammentato |
| CRC | 4 byte | Contiene il numero di CRC |