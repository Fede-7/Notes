# Application Layer

## Applicazioni di rete

> [!def] Applicazione di rete
> **Insieme di più programmi** che girano su sistemi finali diversi (host) e comunicano tra loro tramite la rete.

Le **applicazioni** sono i programmi in esecuzione sui dispositivi che permettono all'utente di accedere ai **servizi**: social network, Web, messaggistica, e-mail, giochi multiutente, streaming video, file sharing P2P, voice over IP, videoconferenza, motori di ricerca, remote login.

Creare un'applicazione di rete significa scrivere programmi che:

- **Girano su sistemi finali diversi**, anche con linguaggi o sistemi operativi diversi.
- **Comunicano sulla rete** (tipicamente via socket) mediante un protocollo specifico.

Non serve scrivere software per i dispositivi del nucleo della rete: i network device **non eseguono applicazioni utente**, e esistono **librerie specifiche** (es. socket) che implementano le funzionalità di rete.

## Architetture delle applicazioni

> [!def] Architettura dell'applicazione
> **Struttura** dell'applicazione sui vari sistemi finali, decisa dallo sviluppatore al momento della progettazione.

Le due architetture fondamentali sono:

- **Client-server**: nodi eterogenei; un host sempre attivo (il **server**) fornisce servizi richiesti da molti altri host (i client).
- **Peer-to-peer (P2P)**: nodi idealmente omogenei; l'applicazione sfrutta la comunicazione **diretta** tra coppie di host connessi intermittentemente (peer).

Nel client-server valgono le seguenti proprietà:

- I client **non comunicano direttamente** tra loro.
- Il server ha un **indirizzo fisso e noto** (hostname o IP), così un client può sempre contattarlo inviando un pacchetto di richiesta.
- Spesso sono coinvolti **più server** per reggere il carico; il client in genere **non se ne accorge** e li percepisce come un unico server.
- I server multipli possono essere raggruppati in **data center** (grande numero di server in una sede, da alimentare, mantenere e connettere), sparsi come **server distribuiti** nel mondo (da interconnettere e coordinare) o organizzati in **data center distribuiti**.

Nel peer-to-peer valgono le seguenti proprietà:

- Usato per applicazioni **traffic-intensive**; non esiste un server singolo con indirizzo fisso: ogni client ha il proprio indirizzo.
- Le applicazioni P2P pure sono rare: la maggior parte è **ibrida**, combinando client-server e P2P (es. server che tracciano gli indirizzi degli utenti, con messaggi scambiati direttamente tra host).
- P2P è **scalabile e distribuito**: ogni peer genera carico ma aggiunge anche capacità di servizio distribuendo file agli altri peer.
- P2P è **economico** (niente infrastrutture o banda significativa) ma ha problemi di **sicurezza, prestazioni e affidabilità**.

## Comunicazione tra processi

In un'applicazione di rete i **processi** comunicano attraverso la rete, anche su sistemi operativi diversi; tra una coppia di processi comunicanti si identifica tipicamente un **processo client** e un **processo server**, e nelle applicazioni P2P i processi possono **cambiare ruolo**.

> [!def] Socket
> **Interfaccia software** tra livello applicazione e livello trasporto: è la "cassetta delle lettere" tramite cui un processo invia e riceve messaggi, assumendo che lato trasporto esista un'infrastruttura che recapita il messaggio alla socket del processo destinatario.

- Le socket costituiscono l'**API** (*Application Programming Interface*) tra applicazione e rete.
- Lo sviluppatore controlla tutto lato applicazione, ma ha **poco controllo** del lato trasporto: solo la **scelta del protocollo di trasporto** (TCP/UDP) e pochi parametri (dimensione massima del buffer, maximum segment size, ecc.).
- Scelto il protocollo, l'applicazione assume come dati i servizi di trasporto che quel protocollo fornisce.

Per recapitare un messaggio servono due informazioni, dato che più applicazioni girano su uno stesso host:

1. Un **indirizzo** dell'host (per trovare l'host giusto in rete).
2. Un **identificatore** del processo destinatario (per trovare il processo giusto nell'host).

L'indirizzo lavora a livello **rete** (routing), l'identificatore a livello **trasporto**:

- In Internet l'host è identificato da un **indirizzo IP** (quantità a 32 bit).
- Il processo è identificato da un **numero di porta**; le applicazioni popolari hanno porte convenzionali (es. Web server su porta 80, mail server con SMTP su porta 25); la lista dei numeri di porta noti è mantenuta da IANA.

## Servizi di trasporto

> [!def] Quality of Service
> **Insieme di proprietà** che il livello trasporto può implementare su richiesta dell'applicazione.

- **Affidabilità** del trasferimento: i dati inviati da un capo giungono corretti e completi all'altro capo.
- **Throughput**: ritmo a cui il processo mittente può consegnare bit al ricevente (bit/s).
- **Timing**: ogni bit immesso nella socket arriva alla socket del ricevente entro un intervallo di tempo.
- **Sicurezza**: cifratura e decifratura dei messaggi; teoricamente è un problema di trasporto, ma i protocolli sicuri (es. **TLS**) sono costruiti su TCP, quindi in pratica sta a livello applicazione.

I due protocolli di trasporto si collocano così:

- **TCP** (*Transmission Control Protocol*): prevede un **handshake** tra i processi e un servizio di trasferimento affidabile; per questo è detto **connection-oriented**.
- **UDP** (*User Datagram Protocol*): **leggero**, con servizi minimi; nessun handshake, nessuna garanzia di consegna; per questo è detto **connectionless**.

## Protocolli applicativi

> [!def] Protocollo applicativo
> **Insieme di regole** che definisce come i processi di un'applicazione, su sistemi finali diversi, si scambiano messaggi.

Un protocollo applicativo definisce quattro cose:

1. I **tipi** di messaggi scambiati (es. richieste e risposte).
2. La **sintassi** dei tipi di messaggio: campi presenti e loro delimitazione.
3. La **semantica** dei campi, cioè il significato dell'informazione contenuta.
4. Le **regole** che stabiliscono quando e come un processo invia e risponde ai messaggi.

I protocolli applicativi più comuni sono i seguenti.

| Applicazione | Descrizione |
|---|---|
| `DHCP` | Dynamic Host Configuration Protocol, assegna indirizzi IP |
| `DNS` | Domain Name System, traduce nomi di siti in indirizzi IP |
| `HTTP`/`HTTPS` | HyperText Transfer Protocol (Secure), trasferisce pagine web |
| `SMTP`/`SMTPS` | Simple Mail Transfer Protocol (Secure), invia messaggi e-mail |
| `SNMP` | Simple Network Management Protocol, gestisce dispositivi di rete |
| `Telnet`/`SSH` | Teletype Network (Secure SHell), interfaccia a riga di comando con host remoti |
| `FTP`/`FTPS` | File Transfer Protocol (Secure), usato per trasferire file |

Alcune applicazioni scambiano **informazioni sensibili** (credenziali, dati personali): sulle reti pubbliche i messaggi vanno protetti, da qui le varianti *secure* dei protocolli.

## FTP e FTPS

> [!def] FTP
> **File Transfer Protocol**: uno dei protocolli più antichi di Internet (prima versione 1971), usato per trasferire file tra host tramite rete.

- Nella versione base il trasferimento è in **clear-text** (username, password e file leggibili), quindi è adatto ad applicazioni locali o private.
- La versione sicura **FTPS** protegge username e password e cifra i contenuti.
- FTP e FTPS hanno due componenti: il **protocollo** (comandi per mostrare, scaricare, eliminare file, ecc.) e l'**applicazione software** che lo implementa (lato client e lato server, es. `ftp` e `vsftpd` su Linux).

Comandi FTP più comuni (client connesso al server):

- `help`: elenca i comandi disponibili.
- `cd` / `lcd`: cambia directory sulla macchina remota / locale.
- `ls` / `pwd`: elenca file e directory / stampa la directory di lavoro remota.
- `mkdir` / `rmdir` / `delete`: crea directory, rimuove directory, elimina file sulla macchina remota.
- `get` / `put`: copia un file dal server al client / dal client al server.
- `exit`: chiude la connessione.