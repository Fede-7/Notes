# Lezione 13 Transport Layer porte multiplexing e UDP

## Dal livello applicazione al livello trasporto

Un protocollo di trasporto fornisce **comunicazione logica tra processi** su host diversi: dalla prospettiva dell'applicazione, gli host sembrano direttamente connessi, come sulla stessa macchina.

Il trasporto converte i messaggi applicativi in uno o più pacchetti di livello trasporto, detti **segmenti** (o **datagram**, termine usato soprattutto per i pacchetti UDP):

- Se i messaggi sono spezzati in blocchi più piccoli, ogni blocco riceve una **header** di livello trasporto.
- I segmenti sono passati uno alla volta al livello rete per la trasmissione; all'arrivo sono decapsulati e risalgono al destinatario corretto.

## Responsabilità del livello trasporto

I protocolli di trasporto (UDP e TCP) hanno quattro responsabilità principali:

1. **Consegna processo-a-processo**: i messaggi arrivano indipendentemente da dove si trovano i processi; diversa dalla consegna **host-to-host**, che è responsabilità del protocollo IP di livello inferiore.
2. **Controllo di integrità**: campi di rilevamento errori nelle header dei segmenti.
3. **Trasferimento affidibile dei dati**: consegna corretta e **in ordine** dal processo mittente al ricevente.
4. **Controllo di congestione/flusso**: evita di saturare i dispositivi di rete (link o router) con traffico eccessivo; migliora le prestazioni e giova all'intera rete.

**UDP** (più veloce e semplice) fornisce solo i primi due servizi; **TCP** li fornisce tutti e quattro.

## Consegna processo-a-processo e porte

Al livello applicazione più processi accedono contemporaneamente alla rete (musica, download, navigazione insieme) e un processo può essere connesso a più processi remoti (proxy, mail server).

- La consegna processo-a-processo usa le **socket** come endpoint da cui i processi prendono i messaggi, invece di consegnare direttamente ai processi: così si **disaccoppia** il numero di processi dal numero di connessioni.
- Con più socket sull'host ricevente servono: un **identificatore univoco per socket** (la **porta**) allegato ai segmenti ricevuti, e un processo di **multiplexing/demultiplexing**.
- **Demultiplexing**: reindirizzare un segmento alla socket giusta in base all'identificatore.
- **Multiplexing**: creare segmenti da processi diversi, assegnando a ciascuno l'identificatore giusto.

> [!def] Porta
> **Identificatore delle socket**: numero a 16 bit da 0 a 65535.

- Le porte da 0 a 1023 sono le **well-known port**, riservate ai protocolli applicativi più diffusi; la lista è aggiornata da **IANA** (*Internet Assigned Numbers Authority*).
- Chi sviluppa una nuova applicazione di rete deve assegnare porte alle socket di conseguenza.

| Porta | Uso |
|---|---|
| 20 | FTP — data transfer |
| 21 | FTP — command control |
| 22 | SSH |
| 23 | Telnet (remote login, messaggi in chiaro) |
| 25 | SMTP — routing e-mail |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 — recupero e-mail dal server |
| 119 | NNTP |
| 123 | NTP |
| 143 | IMAP — gestione della posta digitale |
| 161 | SNMP |
| 443 | HTTPS (HTTP su TLS/SSL) |

Per controllare l'uso delle porte su Linux esiste **`nmap`** (*Network Mapper*), utility di scansione che mappa host e servizi di una rete: può sondare le porte di un host per individuare quelle aperte (con un'applicazione in ascolto) e i servizi associati; lo stato di una porta può essere `open`, `closed`, `filtered` o `unfiltered` (non sondabile).

## Multiplexing e demultiplexing

Trasmissione da un processo (porta 19157) sull'host A a un processo (porta 46428) sull'host B:

- **Multiplexing** (lato A): il trasporto crea un segmento con i dati applicativi, la **porta sorgente** (19157) e la **porta destinazione** (46428), e lo passa al livello rete che lo incapsula in un datagram IP (consegna best-effort all'host ricevente).
- **Demultiplexing** (lato B): il trasporto riceve il segmento, lo decapsula e lo instrada alla socket giusta **esaminando la porta destinazione**.

Identificazione delle socket nei due protocolli:

- Una socket **UDP** è identificata da **due elementi**: indirizzo (IP) e porta di **destinazione**. Con la stessa socket si può quindi rispondere a più porte/indirizzi sorgente diversi: la struttura `cliaddr` riempita da `recvfrom` viene usata come destinazione della `sendto` successiva, chiunque sia l'host.
- Una socket **TCP** è identificata da **quattro elementi**: IP e porta sorgente, IP e porta destinazione. Per il handshake iniziale, la connessione TCP **vincola** i processi dei due lati: una sola sorgente e una sola destinazione usano quella socket; se la comunicazione si interrompe, la socket si chiude **da entrambi i lati** (a differenza di UDP).
- Sul server TCP: la **welcoming socket** attende richieste sulla porta del servizio; arrivata la richiesta (segmento SYN con porta destinazione nota), la `accept` crea la socket client-specifica, e tutti i segmenti futuri con quella specifica quadrupla vengono demultiplexati su `new_socket`.

Conseguenze (caso HTTP): più processi di una macchina possono comunicare con più processi (anche lo stesso) di un'altra. Un host C apre due sessioni HTTP verso il server B usando **due porte sorgente diverse**; l'host A può usare una porta sorgente uguale a una di C senza conflitto, perché le due connessioni differiscono per **IP sorgente**. Il server apre tipicamente un processo (o thread) per connessione in arrivo, assegnandogli la socket dedicata; aprire troppi processi/thread può però penalizzare le prestazioni.

## UDP

> [!def] UDP
> **User Datagram Protocol**: protocollo minimalista, connectionless, che aggiunge "l'essenziale" rispetto a IP; fornisce solo **consegna processo-a-processo** (porte, multiplexing/demultiplexing) e **controllo errori**; nessun handshake, nessuna garanzia di consegna, nessun controllo di congestione/flusso.

Perché usare UDP invece di TCP:

- **Controllo a livello applicativo**: UDP è più diretto, l'applicazione controlla la trasmissione; utile per le applicazioni real-time, dove ritmo di invio e ritardi sono cruciali e si tollera la perdita di dati (meno controlli).
- **Stabilimento della connessione rapido**: niente handshake, meno ritardo; opportuno ad esempio nel DNS.
- **Nessuno stato di connessione**: niente parametri di controllo della congestione, niente numeri di sequenza o acknowledgment; un server supporta tipicamente molti più client attivi con UDP che con TCP.
- **Overhead minimo del pacchetto**: la header TCP aggiunge 20 byte a segmento, UDP solo 8.

Esempio DNS su UDP:

- **Applicazione**: l'host costruisce il messaggio di query e lo passa a UDP.
- **Trasporto**: senza handshake col server DNS, UDP aggiunge i campi di header e passa il segmento al livello rete.
- **Rete**: il segmento è incapsulato in un datagram IP e spedito al server DNS.
- Il client attende la risposta; se non arriva (rete che ha perso query o risposta) può: **rinviare la query**, **interrogare un altro name server**, o **notificare all'applicazione** l'assenza di risposta.

Uso dei due trasporti per servizio:

| Servizio | Protocollo applicativo | Trasporto |
|---|---|---|
| E-mail | SMTP | TCP |
| Terminale remoto | Telnet | TCP |
| Web | HTTP | TCP o UDP |
| Trasferimento file | FTP | TCP |
| Traduzione nomi | DNS | UDP |
| Gestione dispositivi di rete | SNMP | UDP |
| Streaming multimediale | Proprietari | UDP o TCP |
| Telefonia Internet | Proprietari | UDP o TCP |

> [!warning] UDP e congestione
> Eseguire applicazioni multimediali su UDP è **controverso**: senza controllo di congestione, se tutti inviassero video ad alto bit-rate senza controllo, i dispositivi di rete andrebbero in overflow perdendo pacchetti UDP; le alte perdite indotte dai mittenti UDP incontrollati costringerebbero anche i mittenti TCP a ridurre drasticamente i loro ritmi.

## Formato del segmento UDP

Il datagram UDP è composto da 5 elementi: una **header** di 64 bit (4 campi da 16 bit) e i dati (N bit, il messaggio applicativo).

Campi della header:

- **Source port**: numero di porta del processo mittente.
- **Destination port**: numero di porta del processo ricevente.
- **Length**: lunghezza dell'intero datagram (header + dati, cioè N + 64 bit).
- **Checksum**: usato dal ricevente per verificare l'integrità del messaggio.

### Checksum UDP

Il controllo di integrità è affidato al **checksum**, campo a 16 bit per il rilevamento errori:

- Lato mittente, UDP calcola il **complemento a 1 della somma** di tutte le parole a 16 bit del datagram, con l'eventuale bit di **overflow** ri-sommato; il risultato va nel campo checksum.
- Il ricevente somma tutte le parole del messaggio **checksum incluso**: se il messaggio è integro la somma deve dare 16 uni (`1111111111111111`); se anche un solo bit vale 0, sono stati introdotti errori.