# Lezione 26: Sicurezza di rete — Autenticazione, SSL, firewall

## Richiamo: fondamenti della sicurezza di rete

Una **comunicazione sicura** dovrebbe garantire quattro proprietà:

- **Riservatezza**: solo mittente e destinatario previsto devono poter comprendere il contenuto del messaggio (contro lo sniffing).
- **Integrità dei messaggi**: il contenuto della comunicazione non deve essere alterato, né dolosamente né accidentalmente.
- **Autenticazione degli endpoint**: mittente e destinatario devono poter confermare l'identità dell'altra parte (contro lo spoofing).
- **Sicurezza operativa**: poter contare su un'infrastruttura di rete che impedisce a host malevoli di intrufolarsi nella comunicazione.

Le prime tre proprietà sono **software-based**, mentre la sicurezza operativa si basa tipicamente su **hardware dedicato** (firewall, intrusion detection systems).

## Autenticazione degli endpoint

L'autenticazione degli endpoint è il processo con cui **un'entità prova la propria identità a un'altra entità** su una rete di calcolatori. Tipicamente un **protocollo di autenticazione (AP)** viene eseguito prima che le due parti eseguano un altro protocollo (trasferimento dati affidabile su TCP, scambio di informazioni di routing DV/LS, e-mail con SMTP, ecc.), così da stabilire le identità prima di iniziare a lavorare. Si può fare affidamento sulla **Certification Authority (CA)**, ma non basta.

### Autenticazione tramite indirizzo IP

Se A e B hanno già comunicato e l'IP di A non è cambiato, B può autenticare A controllando l'**indirizzo IP** nel datagram: se è quello "noto", si assume che sia A a inviare il messaggio. Questo funziona con intrusi "ingenui", ma è chiaramente insufficiente, poiché un intruso "meno ingenuo" può falsificare l'indirizzo nel pacchetto (spoofing). Un modo per evitare l'IP spoofing è agire sui router: un router può essere configurato per inoltrare solo datagram legittimi, cioè con IP sorgenti che appartengono davvero agli host della rete, scartando i datagram falsificati. Purtroppo questa capacità non è diffusa ovunque né imposta, quindi bisogna assumere lo spoofing come possibile.

### Autenticazione tramite password

L'approccio più comune è usare una **password segreta**, che funziona come **segreto condiviso** tra autenticatore e autenticando (Gmail, Facebook, telnet, FTP e molti altri servizi la usano); il segreto condiviso può servire anche al controllo di integrità. Il primo problema è che l'intruso può **intercettare (eavesdropping) la password** dai messaggi, usando poi password e IP falsificato. La soluzione è **cifrare la password**, rendendola illeggibile all'intruso; con la cifratura simmetrica, peraltro, non serve una password aggiuntiva, poiché la chiave condivisa stessa può fare da password.

### Attacco playback (replay)

Anche cifrando, un intruso "molto astuto" può intrufolarsi nella comunicazione spacciandosi per A con un **attacco playback**: sniffa i pacchetti da A a B per ottenere la **versione cifrata della password di A** e, se ci riesce, può "riprodurre" (ri-trasmettere) la password cifrata a B in una nuova sessione, usando anche senza comprenderla. A differenza degli attacchi MiM, che avvengono in tempo reale, sniffing e playback avvengono separatamente. Il problema è che B non può dire se A "era vivo", cioè se esiste una sessione attiva tra il vero A e B. È una situazione simile all'instaurazione di connessione TCP, dove il three-way handshake assicura che entrambi gli endpoint siano vivi e TCP usa **numeri di sequenza iniziali casuali** per evitare che vecchie ritrasmissioni vengano interpretate come SYN/ACK; un'idea analoga vale per l'autenticazione.

### Nonce

Si usa quindi un **nonce**: un numero casuale o pseudo-casuale che un protocollo usa **una sola volta nella sua vita**. Esempio con A e B che condividono una chiave simmetrica:

1. A invia a B il messaggio "Io sono A".
2. B sceglie un **nonce R** e lo invia ad A.
3. A cifra il nonce insieme alla password usando la chiave simmetrica segreta A-B e rimanda il nonce cifrato a B.
4. B decifra il messaggio: se il nonce decifrato è uguale a quello inviato, A è autenticato.

In questo modo la password diventa di fatto una **one-time password**: poiché ogni password cifrata contiene quel numero di nonce, non può essere riutilizzata in altre sessioni da altri. Se B riceve correttamente password e nonce, si può ragionevolmente assumere che dietro c'è un A "vivo".

## SSL (Secure Socket Layer)

Le tecniche crittografiche viste si integrano per fornire riservatezza, integrità dei dati e autenticazione degli endpoint sulle connessioni TCP: sono implementate nel **Secure Socket Layer (SSL)**, una **versione potenziata di TCP** con servizi di sicurezza. Esiste una versione leggermente modificata di SSL v3 detta **Transport Layer Security (TLS)**, e l'equivalente per UDP è il **Datagram TLS (DTLS)**. SSL è usato da molti protocolli applicativi — web, e-mail, messaggistica istantanea, VoIP — e il browser spesso usa **HTTPS (HTTP + SSL/TLS)** invece di HTTP. Poiché SSL protegge TCP, può essere usato da qualsiasi applicazione che gira su TCP, fornendo un'API con socket simile a quella di TCP (l'applicazione include le classi e le librerie SSL). Tecnicamente risiede nel livello applicativo, ma allo sviluppatore sembra un protocollo di trasporto, con i servizi di TCP più quelli di sicurezza. Le sue **tre fasi principali** sono handshake, derivazione delle chiavi (*key derivation*) e trasferimento dati.

### Fase 1: Handshake

Un client B vuole comunicare via SSL con un server A: deve stabilire una connessione TCP con A, verificare che A sia davvero A e inviare ad A un master secret (segreto condiviso). La procedura è la seguente:

1. Stabilita la connessione TCP, B invia un messaggio di **hello** ad A.
2. Il server A risponde con un **certificato** contenente la sua chiave pubblica (asimmetrica).
3. Poiché il certificato è certificato da una CA, B si fida che la chiave pubblica nel certificato sia di A.
4. B genera un **Master Secret (MS)**, valido solo per questa sessione SSL (funge da nonce), lo cifra con la chiave pubblica di A e lo invia.
5. A decifra con la chiave privata e ottiene l'MS: al termine, solo B e A conoscono il master secret della sessione.

### Fase 2: Key Derivation

L'MS è un segreto condiviso tra B e A, quindi potrebbe essere usato come chiave simmetrica per tutta la cifratura e la verifica di integrità della sessione. Tuttavia è più sicuro usare chiavi diverse per cifratura e controllo di integrità nei due flussi (A→B e B→A), quindi dall'MS si creano **quattro chiavi**:

- $E_{B \to A}$ = chiave di **cifratura** di sessione per i dati da B verso A.
- $M_{B \to A}$ = chiave di **MAC** di sessione per i dati da B verso A.
- $E_{A \to B}$ = chiave di **cifratura** di sessione per i dati da A verso B.
- $M_{A \to B}$ = chiave di **MAC** di sessione per i dati da A verso B.

### Fase 3: Trasferimento dati

SSL protegge TCP spezzando il flusso di dati dell'applicazione in **record**. Per ogni record:

1. SSL appende un **MAC** per il controllo di integrità (recordᵢ + MAC).
2. Il record modificato viene **cifrato**.
3. Il record cifrato è passato a TCP per la trasmissione.

Questo garantisce l'integrità dei singoli record, ma non dello stream intero: poiché si cifra solo il payload, un MiM tra A e B può ancora danneggiare lo stream invertendo o rimuovendo segmenti — ad esempio cattura due segmenti consecutivi, inverte il loro ordine insieme ai numeri di sequenza TCP e li invia così al ricevente, che se ne accorge solo quando i dati arrivano all'applicazione. La soluzione è integrare anche un **numero di sequenza** nel messaggio prima della cifratura: il messaggio cifrato è recordᵢ + MAC + sequenceNumberᵢ, quindi conoscendo la procedura e il MAC, il ricevente può certificare l'integrità del messaggio.

## Firewall

Un **firewall** è una combinazione di hardware e software che isola (protegge) una rete da Internet consentendo o negando il passaggio dei pacchetti. Tutto il traffico in ingresso e in uscita deve passare dal firewall, e solo il traffico autorizzato — definito dalla policy di sicurezza locale — può passare. Il firewall è quindi il **singolo punto di accesso alla rete pubblica**, anche se le grandi organizzazioni possono avere più livelli o firewall distribuiti. Il firewall stesso deve essere **immune alle penetrazioni**: se compromesso, dà un falso senso di sicurezza. Gli approcci sono tre: filtraggio tradizionale dei pacchetti, filtraggio stateful e application gateway.

### Filtraggio tradizionale dei pacchetti

Un **packet filter** è tipicamente implementato sul **gateway**, cioè il router che connette la rete locale all'ISP. Esamina ogni singolo datagram e decide se accettarlo o scartarlo in base a regole definite dall'amministratore, specifiche per datagram in ingresso/uscita o per singola interfaccia. Le regole si basano tipicamente su:

- Indirizzo IP sorgente o destinazione.
- Tipo di protocollo nel campo del datagram IP (TCP, UDP, ICMP, ecc.).
- Porta sorgente e destinazione.
- Flag TCP: SYN, ACK, ecc.

Esempi di policy: per consentire solo traffico web si bloccano tutti i segmenti TCP SYN con porta di destinazione diversa da 80; per negare alcuni servizi di streaming si blocca il traffico UDP non critico, spesso usato per lo streaming; per negare i ping in ingresso si bloccano le risposte ICMP ping in uscita. Le policy possono inoltre combinare indirizzi e numeri di porta, ad esempio inoltrando tutti i datagram Telnet (porta 23) tranne quelli verso o da un elenco di IP specifici; tali policy però non proteggono dallo spoofing.

#### Access Control List (ACL)

Le regole si implementano nei router tramite **access control list**. Esempio per far passare solo traffico web (interfaccia router-ISP):

| Azione | Indirizzo sorgente | Indirizzo dest. | Protocollo | Porta src | Porta dest | Flag |
| --- | --- | --- | --- | --- | --- | --- |
| allow | 222.22/16 | fuori da 222.22/16 | TCP | > 1023 | 80 | any |
| allow | fuori da 222.22/16 | 222.22/16 | TCP | 80 | > 1023 | ACK |
| allow | 222.22/16 | fuori da 222.22/16 | UDP | > 1023 | 53 | — |
| allow | fuori da 222.22/16 | 222.22/16 | UDP | 53 | > 1023 | — |
| deny | all | all | all | all | all | all |

Con la regola 1 i pacchetti TCP con porta destinazione 80 possono uscire; con la regola 2 i pacchetti TCP con porta sorgente 80 e ACK=1 possono entrare, poiché tutti i messaggi web portano numeri ACK; con le regole 3–4 i pacchetti DNS (UDP porta 53) entrano ed escono.

#### Problema: filtraggio stateless

Il filtraggio tradizionale è **stateless**: la tabella, pur restrittiva, lascia passare qualsiasi pacchetto dall'esterno con ACK=1 e porta sorgente 80 — e tali pacchetti sono noti per essere usati in **attacchi DoS**. La soluzione ingenua sarebbe bloccare anche i pacchetti TCP ACK, ma ciò impedirebbe agli utenti interni di navigare sul Web.

### Filtraggio stateful

I filtri **stateful** risolvono il problema tracciando **tutte le connessioni TCP attive** in una tabella delle connessioni, per capire se il traffico appartiene a una connessione legittima. Il firewall riconosce l'inizio di una nuova connessione (la sequenza SYN–SYNACK–ACK del three-way handshake) e la fine (il pacchetto FIN); può anche assumere, conservativamente, che la connessione sia terminata quando non vede attività per un certo tempo (es. 60 secondi). La tabella stateful include tipicamente una colonna **"check connection"** che specifica se i pacchetti rientrano in una connessione già stabilita: solo i pacchetti ACK dentro connessioni stabilite vengono ammessi.

| Azione | Ind. sorgente | Ind. dest. | Protocollo | Porta src | Porta dest | Flag | Check connessione |
| --- | --- | --- | --- | --- | --- | --- | --- |
| allow | 222.22/16 | fuori da 222.22/16 | TCP | > 1023 | 80 | any | |
| allow | fuori da 222.22/16 | 222.22/16 | TCP | 80 | > 1023 | ACK | X |
| allow | 222.22/16 | fuori da 222.22/16 | UDP | > 1023 | 53 | — | |
| allow | fuori da 222.22/16 | 222.22/16 | UDP | 53 | > 1023 | — | |
| deny | all | all | all | all | all | all | |

### Application Gateway

I metodi di filtraggio fin qui visti controllano soprattutto IP e porte, ma può servire consentire o negare funzionalità **in base all'utente o all'applicazione**: ad esempio, solo i tecnici potrebbero usare certi protocolli (es. Telnet verso l'esterno), negati agli utenti normali, oppure solo certi tipi di messaggi o comandi sono ammessi dentro un protocollo. Questo va oltre le capacità dei filtri tradizionali e stateful, poiché l'identità degli utenti interni è un dato del **livello applicativo**, non presente negli header IP/TCP/UDP. Un **application gateway** (o application-level gateway) filtra i pacchetti in base ai dati del livello applicativo ed è tipicamente un server separato che lavora insieme al firewall. Il suo funzionamento prevede che si neghi ogni connessione di un protocollo specifico (es. Telnet) tranne quelle da o verso l'application gateway; chi vuole usare il gateway — e quindi il protocollo riservato — deve autenticarsi su di esso (user ID e password); il server verifica se l'utente ha il permesso per quel protocollo e, in tal caso, tutte le richieste e risposte passano dal gateway (proxy). Le reti interne hanno spesso più gateway per applicazioni diverse (Telnet, HTTP, FTP, e-mail). Gli svantaggi sono tre:

- Serve un **gateway diverso per ogni applicazione**.
- C'è una **penalizzazione delle prestazioni** dovuta al proxying, soprattutto con molti utenti.
- Il software sugli host deve **sapere usare l'application gateway**.

## Intrusion Detection Systems (IDS)

Per rilevare certi tipi di attacchi serve il **deep packet inspection**, cercando pattern di attacco noti o traffico sospetto. L'**Intrusion Detection System (IDS)** è un insieme di dispositivi specializzati che monitorano la rete cercando pacchetti sospetti; il suo ruolo primario è riconoscere i pacchetti potenzialmente malevoli e avvisare l'amministratore di rete, che poi deve agire. Se può anche bloccare (filtrare) i pacchetti potenzialmente malevoli, si parla di **Intrusion Prevention System (IPS)**. Le organizzazioni si affidano agli IDS per rilevare un'ampia gamma di attacchi: network/port scan (es. nmap), flooding DoS, worm e virus. L'architettura tipica prevede uno o più **sensori IDS** e un **processore IDS centrale** che raccoglie e integra le informazioni e invia gli allarmi. Esistono due tipi di IDS:

- **Signature-based**: mantiene un'ampia banca dati di **firme di attacco**, cioè insiemi di regole legate a un'attività di intrusione (il più comune).
- **Anomaly-based**: crea un **profilo del traffico** e segnala i flussi statisticamente anomali.

## Demilitarized Zone (DMZ)

Nelle grandi reti esiste spesso il problema di avere due livelli di sicurezza diversi per dispositivi diversi: ad esempio, i server che devono comunicare con l'esterno possono usare un filtraggio più morbido. Una **demilitarized zone (DMZ)** è una regione a bassa sicurezza in cui le restrizioni sono limitate e si possono ospitare i server. L'approccio tipico è porre la DMZ tra due firewall: uno esterno, meno restrittivo, e uno interno, più restrittivo. In una DMZ con IDS, la **regione ad alta sicurezza** è protetta da un packet filter e da un application gateway e monitorata dai sensori IDS, mentre la **regione a bassa sicurezza** (la DMZ) è protetta solo dal filtro e monitorata dai sensori.