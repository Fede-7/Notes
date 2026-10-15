# Lezione 26 — Sicurezza di rete: autenticazione, SSL, firewall

## Proprietà di una comunicazione sicura (richiamo)

Una comunicazione sicura deve garantire:

- **Confidenzialità**: solo mittente e destinatario comprendono il contenuto (anti-sniffing);
- **Integrità dei messaggi**: il contenuto non va alterato, né maliziosamente né accidentalmente;
- **Autenticazione degli endpoint**: mittente e destinatario confermano l'identità reciproca (anti-spoofing);
- **Operational security**: un'infrastruttura che impedisca a host malevoli di intrufolarsi.

Le prime 3 sono software-based; l'ultima tipicamente hardware (firewall, intrusion detection systems).

## End-point authentication

> [!def] End-point authentication
> Processo con cui un'entità **dimostra la propria identità** a un'altra su una rete. Un **authentication protocol (AP)** gira **prima** che le parti eseguano altri protocolli (trasferimento affidabile su TCP, scambio di informazioni di routing, e-mail/SMTP, ecc.), per stabilire le identità di entrambe.

Ci si può appoggiare alla **certification authority (CA)**, ma non basta.

### Autenticazione tramite IP

Se A e B hanno già comunicato e l'IP di A non è cambiato, B potrebbe autenticare A controllando **l'indirizzo IP nel datagramma**: se è quello noto, si assume sia A. Funziona con intrusi "ingenui", ma un intruso meno ingenuo può **forgiare l'indirizzo sorgente** (spoofing).

Una contromisura via router: il router inoltra solo datagrammi "legittimi" (con IP sorgenti coerenti con i propri host) e scarta i forgiati — ma questa capacità **non è universalmente dispiegata**, quindi lo spoofing va considerato possibile.

### Autenticazione tramite password

Approccio più comune: la password come **segreto condiviso** tra autenticatore e autenticato (Gmail, Facebook, telnet, FTP...). Il segreto serve anche per il controllo di integrità.

- **Problema 1**: l'intruso può fare **eavesdropping** e rubare la password. → Si risolve **cifrando** la password; con cifratura simmetrica non serve nemmeno una password aggiuntiva: la chiave condivisa fa già da password.
- **Problema 2**: **playback (replay) attack** — un intruso "molto smart" sniffera i pacchetti da A a B, ottiene la **versione cifrata** della password e la **riutilizza** in una nuova sessione (senza comprenderla). Diversamente dai MiM (in tempo reale), sniffing e playback avvengono **separatamente**. B non può capire se A è "vivo" (sessione attiva tra il vero A e B).

### Nonce

> [!def] Nonce
> Numero **casuale o pseudo-casuale** che un protocollo usa **una sola volta** nella sua vita (analogo ai numeri di sequenza iniziali casuali del three-way handshake TCP, usati per evitare che vecchie ritrasmissioni vengano interpretate come SYN/ACK).

Protocollo (A e B condividono una chiave simmetrica):

1. A invia a B: *"Io sono A"*;
2. B sceglie un nonce $R$ e lo invia ad A;
3. A cifra **nonce + password** con la chiave simmetrica A–B e la rimanda a B;
4. B decifra: se il nonce ricevuto **uguaglia quello inviato**, A è autenticato.

La password diventa di fatto una **one-time password**: ogni versione cifrata contiene il nonce e **non è riusabile** in altre sessioni; se il pacchetto risponde correttamente al nonce, si può assumere ragionevolmente che dietro ci sia A vivo.

## SSL/TLS

> [!def] SSL
> Il **Secure Socket Layer** è una versione "potenziata" di TCP con servizi di sicurezza: integra confidenzialità, integrità dei dati e autenticazione degli endpoint per le connessioni TCP. TLS è la versione leggermente modificata di SSL v3; per UDP esiste il **DTLS**. Usato da Web, e-mail, messaggistica, VoIP (es. **HTTPS** = HTTP + SSL/TLS).

Poiché SSL protegge TCP, **qualsiasi applicazione su TCP** può usarlo; offre una API con socket simile a quella TCP (basta includere le classi/librerie SSL). Tecnicamente risiede nell'application layer, ma **dalla prospettiva dello sviluppatore** sembra un protocollo di trasporto che fornisce i servizi TCP + sicurezza.

Le 3 fasi principali: **handshake**, **key derivation**, **data transfer**.

### Fase 1: handshake

Obiettivi del client B verso il server A: stabilire la connessione TCP, verificare che A sia davvero A, inviare il **master secret** (segreto condiviso).

```text
1. Stabilita la connessione TCP, B invia un messaggio "hello" ad A.
2. A risponde con un certificato contenente la propria chiave pubblica
   (asimmetrica).
3. Il certificato è certificato da una CA → B si fida che la chiave
   pubblica appartenga ad A.
4. B genera un Master Secret (MS) valido solo per questa sessione SSL
   (nonce), lo cifra con la chiave pubblica di A e lo invia.
5. A decifra con la propria chiave privata e ottiene l'MS.
   Ora solo A e B conoscono il master secret della sessione.
```

### Fase 2: key derivation

Usare l'MS come chiave per tutto sarebbe rischioso: è più sicuro usare **chiavi diverse** per cifratura e integrità nei **due sensi** del flusso. Dall'MS si derivano **4 chiavi**:

- $E_{B\to A}$: chiave di cifratura per i dati da B verso A;
- $M_{B\to A}$: chiave MAC per i dati da B verso A;
- $E_{A\to B}$: chiave di cifratura per i dati da A verso B;
- $M_{A\to B}$: chiave MAC per i dati da A verso B.

### Fase 3: data transfer

SSL spezza il flusso applicativo in **record**; per ogni record:

1. si aggiunge un **MAC** per il controllo di integrità ($record_i + \text{MAC}$);
2. il record modificato viene **cifrato**;
3. il record cifrato è passato a TCP per la trasmissione.

> [!warning] Riordino dei segmenti
> Solo il payload è cifrato: un MiM tra A e B può **invertire o rimuovere segmenti** (es. catturare due segmenti consecutivi e scambiarli insieme ai numeri di sequenza TCP) — il destinatario non se ne accorgerebbe finché i dati non raggiungono l'applicazione. SSL integra quindi anche un **numero di sequenza nel messaggio prima della cifratura**: il record reale cifrato è `record + MAC + sequenceNumber`, così il destinatario può certificare l'integrità dell'intero flusso.

## Firewall

> [!def] Firewall
> Combinazione di hardware e software che **isola (protegge) una rete da Internet** permettendo/negando il passaggio dei pacchetti. Tutto il traffico in entrata/uscita deve passare dal firewall; è autorizzato solo il traffico consentito dalla **politica di sicurezza locale**. È un **singolo punto d'accesso** alla rete pubblica (le grandi organizzazioni possono avere livelli multipli o firewall distribuiti) e **deve essere immune alla penetrazione**: se compromesso, darebbe un falso senso di sicurezza.

Tre approcci: **packet filtering** tradizionale, **stateful filtering**, **application gateway**.

### Traditional packet filtering

- Implementato tipicamente sul **gateway** (router che connette la LAN all'ISP).
- Esamina **ogni singolo datagramma** e decide accettazione/scarto secondo **regole dell'amministratore** (distinte per datagrammi in entrata/uscita e per singola interfaccia).
- Le regole si basano su: IP sorgente/destinazione, tipo di protocollo nel campo IP (TCP, UDP, ICMP...), porte sorgente/destinazione, flag TCP (SYN, ACK, ...).

Esempi di politiche:

- solo traffico Web: bloccare i segmenti TCP SYN con porta destinazione ≠ 80;
- negare servizi di streaming: bloccare il traffico UDP non critico;
- negare ping in entrata: bloccare le **risposte ICMP** in uscita;
- politiche combinate IP+porta: inoltrare tutti i datagrammi Telnet (porta 23) **tranne** quelli verso/da specifici IP.

> [!warning] Niente anti-spoofing
> Queste politiche **non proteggono dallo spoofing**.

Esempio di **access control list** sull'interfaccia verso l'ISP (rete 222.22/16, solo web + DNS):

| action | source | dest | protocol | src port | dst port | flag |
| --- | --- | --- | --- | --- | --- | --- |
| allow | 222.22/16 | fuori 222.22/16 | TCP | >1023 | 80 | any |
| allow | fuori 222.22/16 | 222.22/16 | TCP | 80 | >1023 | ACK |
| allow | 222.22/16 | fuori 222.22/16 | UDP | >1023 | 53 | — |
| allow | fuori 222.22/16 | 222.22/16 | UDP | 53 | >1023 | — |
| deny | all | all | all | all | all | all |

Problema: il filtering tradizionale è **stateless** — la seconda regola fa passare **qualsiasi** pacchetto esterno con ACK=1 e porta sorgente 80, e tali pacchetti sono noti strumenti di attacchi **DoS**. Bloccare anche i TCP ACK impedirebbe però agli utenti interni di navigare.

### Stateful packet filtering

Il filtro **stateful** tiene traccia delle connessioni TCP in corso in una **connection table**, per capire se il traffico appartiene a una connessione legittima:

- riconosce l'**inizio** di una connessione (SYN–SYNACK–ACK) e la **fine** (FIN);
- assume (conservativamente) la fine anche dopo un **timeout di inattività** (es. 60 s);
- la tabella ha una colonna **"check connection"** che verifica se i pacchetti rientrano in una connessione già stabilita (la regola ACK+porta 80 vale solo con `X`).

### Application gateway

Filtrare per IP/porta non basta quando si vuole permettere/negare funzionalità **per utente o per applicazione**:

- solo i tecnici possono usare certi protocolli (es. Telnet col mondo esterno);
- solo certi tipi di messaggi/comandi sono ammessi dentro un protocollo.

Sono informazioni di **livello applicativo** (identità dell'utente) non presenti negli header IP/TCP/UDP: servono un **application gateway** (o application-level gateway), un server separato che opera in combinazione col firewall e filtra in base ai dati applicativi.

Funzionamento:

1. si nega **ogni** connessione del protocollo (es. Telnet), tranne quelle da/verso l'application gateway;
2. l'utente deve **autenticarsi** al gateway (user ID e password);
3. il gateway controlla se l'utente ha il permesso per quel protocollo; in tal caso tutte le richieste/risposte passano da lui (**proxy**).

Le reti interne hanno spesso **gateway multipli** per protocolli diversi (Telnet, HTTP, FTP, e-mail...). Svantaggi:

- serve un **gateway diverso per ogni applicazione**;
- **penalità di prestazioni** per il proxying (specie con molti utenti);
- il software degli host deve sapere usare l'application gateway.

## Intrusion Detection Systems

> [!def] IDS
> L'**Intrusion Detection System** è un insieme di dispositivi specializzati che monitorano la rete cercando pacchetti sospetti, tramite **deep packet inspection** (pattern d'attacco noti o traffico sospetto). Ruolo primario: riconoscere pacchetti potenzialmente malevoli e **allertare l'amministratore**. La variante che **blocca/filtra** i pacchetti malevoli è l'**IPS** (Intrusion *Prevention* System).

Gli IDS rilevano un ampio spettro di attacchi: **port/network scan** (es. nmap), **DoS flooding**, **worm e virus**.

Architettura: uno o più **sensori IDS** + un **processore centrale** che colleziona e integra le informazioni e invia gli allarmi. Tipologie:

- **Signature-based**: mantiene un database esteso di **firme d'attacco** (regole legate a un'attività di intrusione) — il più comune;
- **Anomaly-based**: crea un **profilo del traffico** e segnala flussi statisticamente insoliti.

## DMZ

Nelle grandi reti servono **due livelli di sicurezza** diversi: i server che comunicano col mondo esterno possono usare un filtering più soft.

> [!def] DMZ
> La **demilitarized zone** è una regione a **bassa sicurezza** in cui le restrizioni sono limitate e si possono ospitare i server. Si colloca tipicamente **tra due firewall**: uno esterno (meno restrittivo) e uno interno (più restrittivo).

Esempio di DMZ con IDS:

- la regione **ad alta sicurezza** è protetta da un packet filter + application gateway e monitorata da sensori IDS;
- la regione a bassa sicurezza (la DMZ) è protetta solo dal filter e monitorata dai sensori.