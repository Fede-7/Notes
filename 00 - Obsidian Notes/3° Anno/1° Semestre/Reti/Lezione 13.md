# Lezione 13 Il livello di trasporto

## Comunicazione logica tra processi

Il livello di trasporto fornisce **comunicazione logica** tra processi applicativi in esecuzione su host diversi: dal punto di vista dell'applicazione, i processi appaiono connessi direttamente come se fossero sulla stessa macchina, qualunque cosa si frapponga tra loro (router, collegamenti).

- Al **sender**, il livello di trasporto incapsula i dati dell'applicazione: **TCP** organizza il flusso di byte in **segmenti**, mentre **UDP** incapsula i singoli messaggi in **datagram**, preservandone i confini.
- Ogni segmento/datagram riceve un'intestazione di trasporto e viene passato al livello di rete, che lo incapsula in un datagramma IP e tenta una consegna *best-effort*.
- Al **receiver**, il livello di trasporto fa il demultiplexing dei segmenti/datagram in arrivo verso la socket appropriata: TCP consegna un flusso di byte ordinato, UDP consegna i singoli datagram.
- La segmentazione è resa **trasparente all'applicazione**: è il livello di trasporto che spezza lo stream, e la rete provvede eventualmente a una frammentazione ulteriore.
- I protocolli di trasporto sono implementati **solo nei sistemi finali**, mentre il routing segue la topologia e deve girare sui nodi: il trasporto connette processi, la rete connette host.

> [!info] Segmentazione e frammentazione
> La **segmentazione TCP** e la **frammentazione IP** sono meccanismi diversi che operano a livelli diversi. A livello di trasporto lo stream viene diviso in segmenti; a livello di rete i segmenti vengono spezzati in frammenti più o meno piccoli secondo le caratteristiche della linea e i vincoli di rappresentazione, ad esempio l'**MTU**. Proprio per questi vincoli strutturali, qualche informazione dal livello sottostante può emergere verso il trasporto: la separazione dei livelli non è completamente impermeabile.

## Responsabilità del livello di trasporto

I protocolli di trasporto (UDP e TCP) hanno quattro responsabilità principali.

- **Consegna processo-processo**: i messaggi raggiungono i processi destinatari indipendentemente da dove si trovano, a differenza della consegna host-to-host tra due macchine, che è responsabilità del protocollo IP.
- **Controllo di integrità**: campi di rilevamento errori inclusi nelle intestazioni dei segmenti.
- **Trasferimento affidabile dei dati**: i dati arrivano dal processo mittente al processo destinatario corretti e in ordine.
- **Controllo di congestione e di flusso**: evita di sommergere i dispositivi di rete (collegamenti o router) con un traffico eccessivo, con beneficio alle prestazioni e all'intera rete.

UDP, più veloce e semplice, fornisce solo i primi due servizi; TCP fornisce tutti e quattro.

## Multiplexing e demultiplexing

A livello di applicazione più processi accedono alla rete contemporaneamente, e un processo può essere connesso a più processi nello stesso momento (proxy, mail server): non esiste una corrispondenza uno-a-uno tra processi e connessioni. Le **socket** forniscono gli endpoint della comunicazione processo-processo, e non c'è una socket per forza per ogni processo: un server può gestire più connessioni concorrenti.

> [!def] Multiplexing e demultiplexing
> **Operazioni complementari** del livello di trasporto: il **multiplexing** (lato sender) raccoglie i dati da socket diverse, aggiunge le intestazioni di trasporto con i numeri di porta e passa i segmenti/datagram risultanti al livello di rete; il **demultiplexing** (lato receiver) esamina le informazioni nei pacchetti ricevuti e ne consegna i dati alla socket appropriata.

L'apertura di una socket espone un **buffer di ricezione a livello kernel**: è il demultiplexing, gestito dallo stack di rete del kernel, a indirizzare lì i dati in arrivo, e l'applicazione li preleva con `recvfrom()`.

### Demultiplexing senza connessione in UDP

Nel client UDP la socket si crea con `socket(AF_INET, SOCK_DGRAM, 0)` e tipicamente non viene legata a una porta sorgente: è il sistema operativo a sceglierne una libera (es. 46428), benché sia sempre possibile il `bind()` esplicito; la destinazione si imposta nella struttura `sockaddr_in` passata a `sendto()`.

- Nel demultiplexing **connectionless** di UDP, il datagram in arrivo viene consegnato alla socket in base a due soli campi: l'**indirizzo IP di destinazione** e la **porta di destinazione**.
- Per questo una socket UDP è identificata da due numeri, mentre una socket TCP da quattro: è la ragione per cui TCP necessita di `accept()` e UDP no.
- La `recvfrom()` riempie la struttura `cliaddr` con indirizzo e porta del mittente: la stessa socket può così inviare la risposta (`sendto()`) a più porte e indirizzi sorgente, chiunque sia il client.

### Porta di destinazione non raggiungibile

Se un datagram UDP arriva su una porta senza socket in ascolto si verifica la seguente sequenza.

- Il livello UDP della macchina ricevente tenta il demultiplexing con le informazioni di destinazione, non trova socket corrispondenti e **scarta** il datagram.
- L'host genera normalmente un messaggio **ICMP Destination Unreachable (Port Unreachable)** verso il mittente, la cui consegna però non è garantita.
- Il sistema operativo può riportare l'errore all'applicazione (es. `ECONNREFUSED` su Linux); una `recvfrom()` bloccante può comunque attendere indefinitamente se non si configura un timeout.

UDP non garantisce la consegna né offre meccanismi di instaurazione della connessione: le applicazioni devono gestire da sole le risposte mancanti e i timeout.

### Demultiplexing in TCP

Nel TCP la comunicazione parte da una **welcoming socket** del server, in ascolto su una porta nota (es. 19157): il client crea la socket con `socket(AF_INET, SOCK_STREAM, 0)` e con `connect()` invia un **segmento di richiesta di connessione**, cioè un segmento TCP con porta di destinazione 19157 e il bit **SYN** a 1 nell'intestazione.

La connessione si stabilisce con il **three-way handshake**.

> [!aside]
> 
> 1. **SYN**: il client invia un segmento con SYN = 1 per richiedere la connessione.
> 2. **SYN-ACK**: il server risponde con un segmento con SYN = 1 e ACK = 1.
> 3. **ACK**: il client riconosce il SYN del server con un segmento con ACK = 1.
> 
> I tre segmenti portano le porte sorgente e destinazione che identificano gli endpoint; completato l'handshake, `accept()` sulla socket in ascolto restituisce una **nuova socket connessa** e riempie `cliaddr` con indirizzo e porta del client. Il transport layer registra i quattro valori letti nel segmento in arrivo: ogni segmento successivo con gli stessi quattro valori viene consegnato alla nuova socket, e la socket in ascolto può continuare ad ascoltare.
> 
> ---
> 
> ![[Lezione 13-1793554391151.png|160]]
> 

> [!def] 4-tuple
> **Insieme di quattro valori** che identifica una connessione TCP stabilita: indirizzo IP sorgente, porta sorgente, indirizzo IP di destinazione, porta di destinazione. Più connessioni possono condividere la stessa porta del server e restare distinte per le loro 4-tuple.

Host diversi possono riusare lo stesso numero di porta sorgente: nell'esempio del libro l'host C apre due sessioni HTTP verso il server B assegnando alle connessioni le porte sorgente 26145 e 7532, e l'host A può usare la porta 26145 per la propria sessione senza saperlo di C, perché le due connessioni differiscono per l'indirizzo IP sorgente. Il server apre tipicamente un processo (o thread) per ogni connessione in arrivo, assegnandogli la nuova socket; troppi processi o thread possono però comprometterne le prestazioni.

![[Lezione 13-1793554465193.png|200]]

## Porte

I protocolli di trasporto usano i numeri di porta per distinguere gli endpoint di comunicazione e supportare multiplexing e demultiplexing; porta sorgente e destinazione compaiono nelle intestazioni TCP e UDP.

> [!def] Porta
> **Numero intero a 16 bit** (da 0 a 65535) che identifica un endpoint di comunicazione a livello di trasporto; la classificazione è curata dalla IANA (*Internet Assigned Numbers Authority*).

Le porte si distinguono in tre categorie.

- **Well-known** (0–1023): universalmente note e assegnate ai servizi storici.
- **Registered** (1024–49151): assegnate dalla IANA su registrazione, ad es. MySQL su `3306/TCP`; sono una convenzione, non un obbligo, e un servizio può essere configurato su un'altra porta.
- **Dynamic/private** (49152–65535): libere, ad esempio per le porte sorgente scelte dai client.

Le porte ben note assegnate ai servizi principali sono le seguenti.

| Porta | Servizio |
|---|---|
| `20` | FTP data transfer |
| `21` | FTP command control |
| `22` | SSH |
| `23` | Telnet, remote login con messaggi di testo non cifrati |
| `25` | SMTP, instradamento e-mail |
| `53` | DNS |
| `80` | HTTP |
| `110` | POP3, recupero e-mail dal server |
| `119` | NNTP |
| `123` | NTP |
| `143` | IMAP |
| `161` | SNMP |
| `443` | HTTPS (HTTP su TLS/SSL) |

### Ispezione delle porte con nmap e ss

**`nmap`** (*Network Mapper*) opera dalla prospettiva di rete: manda sonde a un host remoto, per nome o indirizzo, per scoprire host e servizi e individuare le porte aperte, cioè quelle su cui un'applicazione è in ascolto.

- `nmap scanme.nmap.org` scansiona le 1000 porte TCP più comuni; `--top-ports N` limita alle N più usate; `-p 22,80,443` specifica le singole porte.
- `-sV` attiva il *service version detection*: interroga le porte aperte per identificare il servizio effettivo e la versione del software; senza `-sV` i nomi dei servizi sono dedotti dalle assegnazioni convenzionali.

Ogni porta può risultare in uno di tre stati.

- **open**: qualcosa è legato a quella porta ed è in ascolto.
- **closed**: l'host ha risposto, ma nulla è in ascolto su quella porta.
- **filtered**: nessuna risposta è tornata: un firewall ha ingoiato la sonda e lo stato resta sconosciuto.

**`ss`** opera invece dalla prospettiva locale del sistema operativo, ispezionando le socket direttamente dal kernel: `ss -tulnp` mostra le socket locali con `-t` (TCP), `-u` (UDP), `-l` (in ascolto), `-n` (indirizzi e porte numerici), `-p` (processi associati). La differenza chiave: `nmap` scopre i servizi accessibili via rete su host remoti, `ss` mostra le socket aperte sulla macchina locale, a un livello più basso.

## UDP

> [!def] UDP
> **Protocollo di trasporto connectionless**, senza handshake tra le entità di trasporto prima dell'invio, che fornisce **consegna processo-processo** (porte, multiplexing e demultiplexing) e **controllo di errori** (checksum), e nient'altro: nessuna garanzia di consegna, nessun controllo di congestione o di flusso. È un protocollo minimalista che aggiunge a IP solo "l'essenziale".

### Perché UDP invece di TCP

Le ragioni per preferire UDP sono le seguenti.

- **Controllo a livello applicativo**: UDP è più diretto e lascia all'applicazione più controllo sulla trasmissione, utile nelle applicazioni real-time dove ritmo di invio e ritardi sono cruciali mentre la perdita di dati è tollerabile.
- **Instaurazione rapida della connessione**: niente handshake, quindi meno ritardo nel stabilire la comunicazione, ad es. per DNS.
- **Nessuno stato di connessione**: niente parametri di controllo della congestione, né numeri di sequenza o di riconoscimento; un server regge tipicamente molti più client attivi su UDP che su TCP.
- **Overhead minimo sui pacchetti**: il segmento TCP aggiunge 20 byte di intestazione, il datagram UDP solo 8.

### Uso di UDP

Le applicazioni che richiedono trasferimento affidabile (e-mail, terminale remoto, Web, file transfer) girano su TCP o su protocolli affidabili basati su UDP come **QUIC**; SNMP usa UDP perché la gestione di rete deve funzionare proprio quando la rete è sotto stress, cioè quando il trasferimento affidabile è difficile; le applicazioni multimediali (telefonia Internet, videoconferenza, streaming) usano spesso sia UDP sia TCP, perché si può tollerare una piccola perdita di pacchetti, mentre le applicazioni real-time reagiscono molto male al controllo di congestione di TCP.

| Servizio | Protocollo applicativo | Trasporto |
|---|---|---|
| E-mail | SMTP | TCP |
| Remote terminal | Telnet | TCP |
| Web | HTTP | TCP o UDP |
| File transfer | FTP | TCP |
| Name translation | DNS | UDP |
| Gestione dispositivi di rete | SNMP | UDP |
| Streaming multimediale | Proprietary | UDP o TCP |
| Telefonia Internet | Proprietary | UDP o TCP |

> [!warning] Multimedia su UDP
> Fare streaming ad alto bitrate su UDP senza controllo di congestione è controverso: se tutti iniziassero a trasmettere selfish senza controllo, i dispositivi di rete andrebbero in overflow causando la perdita di più pacchetti UDP; i tassi di perdita indotti dai sender UDP fuori controllo farebbero abbassare drasticamente i tassi dei sender TCP.

### Formato del datagram

Il datagram UDP è composto da un'intestazione di 8 byte e dai dati dell'applicazione (N byte).

- L'intestazione contiene quattro campi da 16 bit ciascuno: **source port** (porta del processo mittente), **destination port** (porta del processo destinatario), **length** e **checksum**.
- **Length**: lunghezza dell'intero datagram in byte, intestazione + dati (N + 8 byte).
- **Checksum**: usato dal ricevente per verificare che il messaggio sia intatto.

![[Lezione 13-1793554552363.png|200]]

Il campo Length a 16 bit rappresenta valori da 0 a $2^{16}-1 = 65535$, quindi il payload teorico massimo è 65535 − 8 = 65527 byte. Il livello IP impone però vincoli ulteriori: in IPv4 il payload UDP massimo è 65507 byte (con intestazione IP di 20 byte); anche i limiti di rappresentazione del livello di rete vincolano le dimensioni, perché un datagram troppo grande non risulta neanche spezzettabile dal livello sottostante.

### Checksum

> [!info] Calcolo del checksum UDP
> Il sender calcola il **complemento a 1** della somma di tutte le parole da 16 bit del datagram (più la *pseudo-header* IP); l'eventuale bit di overflow viene ri-sommato alla cifra meno significativa (*end-around carry*): il bit che rappresentava $2^{17}$ torna a valere 1. Il risultato va nel campo checksum.
> Con le parole `0110011001100000`, `0101010101010101`, `1000111100001100`: la somma con end-around carry dà `0100101011000010`, il cui complemento a 1 è il checksum `1011010100111101`.
> Il receiver somma tutte le parole del messaggio, checksum incluso: se il risultato è `1111111111111111` (16 uni) il check passa; se anche un solo bit è 0, sono stati introdotti errori nel pacchetto.

Il checksum permette di **rilevare** gli errori, non di correggerli: un datagram con checksum invalido viene scartato silenziosamente, senza alcuna ritrasmissione.

#### Limiti del checksum

Il checksum non può rilevare tutti gli errori di trasmissione, perché contenuti diversi possono produrre lo stesso checksum.

- Un checksum a N bit rileva con certezza l'errore su un **singolo bit**, ma non garantisce la rilevazione di due o più errori.
- **Errori che si compensano**: due bit flip con variazioni opposte si annullano lasciando la somma invariata (es. una parola che passa da `0001` a `0000` e un'altra da `0000` a `0001`).
- **Riordino**: scambiare due parole da 16 bit non cambia la loro somma, quindi l'errore non viene rilevato.
- È computazionalmente economico e cattura molti errori comuni, ma non garantisce l'integrità; meccanismi più robusti come il **CRC** (*Cyclic Redundancy Check*) sono usati al livello data link.

#### Perché un controllo end-to-end

> [!info] Errore end-to-end
> I controlli del livello link non bastano: non tutti i collegamenti offrono gli stessi controlli di integrità, e i dati possono corrompersi dentro i dispositivi intermedi (es. in un router) anche quando i controlli link-by-link sui frame riescono. Per il **principio end-to-end**, i controlli di integrità che devono valere tra gli endpoint non possono affidarsi esclusivamente ai componenti intermedi; i controlli link e quello di trasporto proteggono il dato in punti diversi del percorso e sono complementari, nessuno dei due sostituisce l'altro.

### Consegna, perdita e ordinamento

UDP fornisce un servizio connectionless *best-effort*.

- **Nessuna garanzia di consegna**: i datagram possono perdersi durante la trasmissione.
- **Nessuna ritrasmissione**: i datagram persi o corrotti non vengono rinviati automaticamente.
- **Nessun ordine**: i datagram possono arrivare in un ordine diverso da quello di invio.
- **Nessuna soppressione dei duplicati**: non è garantito che un datagram sia consegnato una sola volta.

Le applicazioni che richiedono affidabilità devono implementare meccanismi aggiuntivi o usare un protocollo di trasporto come TCP.

### Buffer delle socket e perdita dei datagram

I datagram in arrivo vengono smistati dal demultiplexing nel **buffer di ricezione della socket** (spazio kernel) e l'applicazione li preleva uno alla volta con `recvfrom()`.

- Se i datagram arrivano più velocemente di quanto l'applicazione li elabora, il buffer di ricezione si può riempire e i datagram in arrivo possono essere scartati.
- Se il buffer dell'applicazione è troppo piccolo, il datagram viene troncato e i byte rimanenti scartati; il buffer kernel deve invece accoglierlo completo, perché UDP preserva i confini del messaggio.
- Una `sendto()` di successo non garantisce che il datagram abbia raggiunto l'applicazione destinataria; UDP non ha controllo di flusso, quindi il sender non viene rallentato quando il receiver non tiene il passo.

### Percorso di ricezione in Linux

Il percorso di un datagram nello stack di rete del kernel segue questi passi.

1. La scheda di rete riceve il frame e lo memorizza in memoria kernel.
2. Il livello IP elabora il pacchetto e riassembla i frammenti se c'è stata frammentazione.
3. Il livello UDP controlla intestazione e checksum, poi fa il demultiplexing del datagram verso la socket appropriata.
4. Il datagram entra nella coda di ricezione della socket.
5. L'applicazione legge il datagram con `recvfrom()`, che copia i dati nel buffer applicativo.

### Affidabilità a livello applicazione

UDP non fornisce riconoscimenti, ritrasmissioni né consegna in ordine, ma le applicazioni possono implementare questi meccanismi quando servono.

- **Sequence number** per identificare i messaggi e rilevare dati mancanti o duplicati.
- **Acknowledgment** per confermare la ricezione avvenuta.
- **Timeout e ritrasmissioni** per recuperare le risposte mancanti.
- **Controllo della congestione** per regolare il traffico immesso nella rete.

Il client DNS può ritentare le query senza risposta; **QUIC** implementa affidabilità e controllo della congestione sopra UDP e supporta HTTP/3. UDP fornisce il servizio di trasporto minimo, lasciando le funzionalità aggiuntive ai protocolli di livello superiore.