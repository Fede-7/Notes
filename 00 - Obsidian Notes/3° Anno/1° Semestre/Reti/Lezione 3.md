# Lezione 3: Il livello applicazione

## Applicazioni di rete

Un'**applicazione di rete** è composta da più programmi che girano su sistemi finali (host o endpoint) diversi e comunicano tra loro attraverso la rete. Un esempio è un'applicazione Web, che include due programmi distinti: il **programma browser** in esecuzione sull'host dell'utente e il **programma Web server** in esecuzione sull'host server. Le **applicazioni** sono i programmi che girano sui dispositivi e permettono agli utenti di accedere ai **servizi**: social network, Web, messaggistica, e-mail, giochi multiutente, video in streaming, file-sharing P2P, voice over IP, videoconferenze in tempo reale, ricerca su Internet, accesso remoto e altri.

Creare un'applicazione di rete significa scrivere programmi che **girano su sistemi finali diversi** (potenzialmente con linguaggi o sistemi operativi diversi) e **comunicano attraverso la rete** tramite un protocollo specifico, ad esempio via socket. Non serve invece scrivere software per i dispositivi del nucleo della rete, poiché i dispositivi di rete **non eseguono applicazioni utente** e le funzionalità di rete sono implementate da **librerie dedicate** (come i socket). La comunicazione tra processi avviene dunque tramite socket, e le applicazioni usano i servizi del livello di trasporto (flusso di dati affidabile).

## Architetture delle applicazioni

L'architettura di un'applicazione è progettata dallo sviluppatore e determina come l'applicazione è strutturata sui vari sistemi finali. Le due architetture fondamentali sono **client-server**, dove i nodi sono eterogenei ed esiste un host sempre attivo (il server) che fornisce servizi su richiesta di molti altri host (i client), e **peer-to-peer (P2P)**, dove i nodi sono idealmente omogenei e l'applicazione sfrutta la comunicazione diretta tra coppie di host connessi intermittentemente (i peer).

### Applicazioni client-server

In un'architettura client-server **i client non comunicano direttamente tra loro**. Poiché il server ha un **indirizzo fisso e noto** (hostname o indirizzo IP), un client può sempre contattarlo inviandogli un pacchetto di richiesta. Per reggere il volume di richieste sono spesso coinvolti **più server**, ma il client tipicamente non se ne accorge e li percepisce come un unico server. I server multipli possono essere organizzati in modi diversi:

- Raggruppati in **data center**, con un numero enorme di server in una sede specifica (da alimentare, manutenere e ben connettere).
- Sparsi come **server distribuiti** in tutto il mondo, da interconnettere e coordinare.
- Organizzati in **data center distribuiti**.

La **web application** è l'esempio tipico: un Web server sempre attivo riceve richieste dai browser sugli host client e, quando riceve una **richiesta** di un oggetto, **risponde** inviando l'oggetto richiesto.

### Applicazioni peer-to-peer

Le architetture P2P sono spesso usate per applicazioni a **traffico intenso** e non prevedono un server unico con indirizzo fisso: ogni client ha il proprio indirizzo. Le applicazioni P2P pure sono rare, poiché la maggior parte adotta **architetture ibride** che combinano client-server e P2P: ad esempio, in molte app di messaggistica istantanea i **server tracciano gli indirizzi degli utenti**, ma i messaggi utente-utente partono direttamente dagli host. Le architetture P2P sono **scalabili e distribuite**: nel file-sharing ogni peer genera carico richiedendo file, ma aggiunge anche **capacità di servizio** distribuendo file agli altri peer. Sono anche **economiche** (niente infrastrutture o banda costosi), ma presentano **problemi di sicurezza, prestazioni e affidabilità**. Applicazioni P2P tipiche sono la telefonia e la videoconferenza su Internet e il file-sharing (BitTorrent, Napster); nel file-sharing il server può anche **tracciare i file disponibili** per velocizzare la ricerca.

## Comunicazione tra processi

In un'applicazione di rete ci sono **processi** su macchine diverse, potenzialmente con sistemi operativi diversi, che comunicano tramite la rete: nelle applicazioni web il processo del browser scambia messaggi con il processo del server, mentre nel file-sharing P2P un file è trasferito da un processo di un peer a un processo di un altro peer. In una coppia di processi che comunicano ci sono tipicamente un **processo client** e un **processo server**: nelle app web il browser è client e il server è server; nel file-sharing P2P il peer che scarica è visto come client e quello che carica come server. In un'applicazione P2P i processi possono "cambiare ruolo", e la maggior parte delle applicazioni di rete consiste proprio in **coppie di processi comunicanti** che si scambiano messaggi tramite la rete sottostante.

### Socket

Seguendo il modello a livelli, un **socket** è l'**interfaccia software** tra livello applicazione e livello di trasporto, e permette ai processi di inviare e ricevere messaggi sulla rete. L'analogia tipica è quella delle **cassette della posta**: un processo che vuole inviare un messaggio a un processo su un altro host lo **mette nella propria cassetta**, presumendo che esista un'**infrastruttura di trasporto** che porterà il messaggio alla cassetta del destinatario; all'arrivo sull'host di destinazione, il messaggio passa per la cassetta (socket) del processo ricevente. I socket sono usati come **Application Programming Interface** (API) tra applicazione e rete. Lo sviluppatore controlla tutto sul lato applicazione del socket, ma sul lato trasporto ha poco controllo, limitato a:

1. La **scelta** del protocollo di trasporto (TCP/UDP).
2. Eventualmente l'impostazione di alcuni **parametri di trasporto** (buffer massimo, dimensione massima del segmento, ecc.).

Scelto il protocollo di trasporto, l'applicazione è costruita assumendo come dati i servizi forniti da quel protocollo.

### Indirizzamento dei processi

Proseguendo l'analogia postale, i processi hanno bisogno di un **indirizzo** per inviare messaggi. Poiché su un singolo host possono girare più applicazioni di rete, per identificare il processo ricevente servono due informazioni: l'**indirizzo** dell'host, che lavora a livello di **rete** (routing), e un **identificatore** del processo ricevente, che lavora a livello di **trasporto**. Su Internet l'host è identificato da un **indirizzo IP** (quantità a 32 bit) e il processo da un **numero di porta**. Alle applicazioni popolari sono state assegnate convenzionalmente porte specifiche: ad esempio un Web server usa la porta 80, un server di posta (SMTP) la porta 25.

## Qualità del servizio (QoS) dal livello di trasporto

Il **livello di trasporto** offre protocolli per implementare su richiesta alcune proprietà, dette **Quality of Service (QoS)**:

- **Affidabilità** del trasferimento: i dati inviati da un capo sono consegnati correttamente e completamente all'altro capo.
- **Throughput**: la velocità con cui il processo mittente consegna bit al processo ricevente (bit/s).
- **Temporizzazione** (*timing*): ogni bit immesso nel socket del mittente arriva al socket del ricevente entro un intervallo di tempo.
- **Sicurezza**: cifratura e decifratura dei messaggi. Teoricamente è un problema del livello di trasporto, ma i protocolli sicuri (es. TLS, *Transport-Layer Security*) sono spesso costruiti sopra TCP, quindi in pratica sta a livello applicazione.

I due protocolli di trasporto principali sono **TCP** (*Transmission Control Protocol*), che prevede un **handshake** tra i processi e un servizio di trasferimento dati affidabile (detto **orientato alla connessione**), e **UDP** (*User Datagram Protocol*), **leggero** e con servizi minimi, senza handshake e senza garanzia di ricezione dei messaggi (detto **senza connessione**).

## Protocolli applicativi

Un **protocollo di livello applicazione** definisce come i processi di un'applicazione di rete, in esecuzione su sistemi finali diversi, si scambiano messaggi. In particolare definisce:

1. I **tipi** di messaggi scambiati (es. messaggi di richiesta e di risposta).
2. La **sintassi** dei vari tipi di messaggio (campi e loro delimitazione).
3. La **semantica** dei campi, cioè il significato dell'informazione.
4. Le **regole** che determinano quando e come un processo invia messaggi e risponde.

### Alcuni protocolli applicativi

| Applicazione | Descrizione |
| --- | --- |
| DHCP | Dynamic Host Configuration Protocol, assegna indirizzi IP |
| DNS | Domain Name System, traduce i nomi dei siti in indirizzi IP |
| HTTP/HTTPS | HyperText Transfer Protocol (Secure), trasferisce pagine web |
| SMTP/SMTPS | Simple Mail Transfer Protocol (Secure), invia messaggi e-mail |
| SNMP | Simple Network Management Protocol, gestisce dispositivi di rete |
| Telnet/SSH | Teletype Network (Secure SHell), interfaccia a riga di comando con host remoti |
| FTP/FTPS | File Transfer Protocol (Secure), usato per trasferire file |

Poiché alcune applicazioni scambiano **informazioni sensibili** (credenziali, dati personali, ecc.), sulle reti pubbliche i messaggi vanno protetti.

## FTP e FTPS

**FTP** (*File Transfer Protocol*) è uno dei protocolli **più antichi** di Internet (prima versione nel 1971) e serve a trasferire file tra host sulla rete. Nella versione base il trasferimento avviene **in chiaro** (username, password e file), quindi è adatto ad usi locali o privati; la versione sicura **FTPS** (*FTP Secure*) protegge username e password e cifra i contenuti. Sia FTP che FTPS hanno due componenti: il **protocollo**, che specifica i comandi (mostrare, scaricare, cancellare file, ecc.), e un'**applicazione software** che lo implementa lato client e lato server.

### Esempio FTP

Su Linux si possono usare `ftp` e `vsftpd` (*very secure FTP daemon*) rispettivamente come client e server.

Sul server:

```bash
$ sudo apt-get install vsftpd
$ service vsftpd status   # verifica che il demone sia in esecuzione
```

Sul client:

```bash
$ sudo apt-get install ftp   # spesso già disponibile in Ubuntu
$ ftp ADDRESS                 # chiederà utente e password
$ exit                        # chiude la connessione
```

### Comandi FTP comuni

| Comando | Funzione |
| --- | --- |
| `help` | Elenca tutti i comandi FTP disponibili |
| `cd` | Cambia directory sulla macchina remota |
| `lcd` | Cambia directory sulla macchina locale |
| `ls` | Mostra file e directory della directory remota corrente |
| `mkdir` | Crea una nuova directory remota |
| `pwd` | Stampa la directory di lavoro corrente sulla macchina remota |
| `delete` | Elimina un file nella directory remota corrente |
| `rmdir` | Rimuove una directory remota |
| `get` | Copia un file dal server remoto alla macchina locale |
| `put` | Copia un file dalla macchina locale al server remoto |