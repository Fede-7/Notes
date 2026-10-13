# Lezione 4: Il livello applicazione: HTTP

## Web e HTTP

Fino ai primi anni '90 Internet era usato principalmente da ricercatori, accademici e studenti universitari, per accedere a host remoti (Telnet), trasferire file (FTP), ricevere e inviare notizie ed e-mail. Queste applicazioni erano (e restano) utilissime, ma Internet restava essenzialmente sconosciuto fuori dalla comunità accademica. Nei primi anni '90 il **World Wide Web** fu la **prima applicazione di Internet** a conquistare il grande pubblico.

Il **World Wide Web** (WWW, o semplicemente Web) è una **raccolta di informazioni** — documenti, immagini, video, audio, ecc. — accessibile su Internet tramite un protocollo specifico: l'**HyperText Transfer Protocol** (HTTP). La comunicazione basata su HTTP è tipicamente **client-server**: un **programma client** traduce le richieste dell'utente in messaggi HTTP (è implementato nei **browser**, come Chrome, Firefox, Edge e Safari), mentre un **programma server** esegue la richiesta HTTP e restituisce una risposta HTTP. HTTP definisce principalmente la **struttura dei messaggi** e come client e server li scambiano; il Web e i suoi protocolli **fanno da piattaforma** per le applicazioni web: YouTube, webmail, gran parte delle app mobile e i social network.

## URL

Le informazioni sul Web si chiamano **risorse** (o oggetti) e sono identificate da un **Uniform Resource Locator** (URL), una stringa così composta:

```
[protocollo]://[usrinfo@][host][:porta][/percorso][?query][#frammento]
```

Dove `[protocollo]` è il protocollo da usare per accedere alla risorsa (HTTP, HTTPS, FTP, ecc.); `[usrinfo]` (opzionale) sono le credenziali utente (username e password seguiti da @), **largamente deprecato** per motivi di sicurezza; `[host]` è il nome o l'indirizzo IP del server; `[porta]` (opzionale) è la porta da usare, spesso dedotta dal protocollo; `[percorso]` è il percorso della risorsa sul server; `[query]`, preceduta da `?`, specifica eventuali richieste; `[frammento]`, preceduto da `#`, identifica un elemento nella risorsa (es. una sezione).

### Esempi

La maggior parte delle pagine Web è costituita da un file **HTML base** e riferimenti ad altri **oggetti** (immagini, video, ecc.): una pagina con testo HTML e cinque immagini JPEG, ad esempio, ha sei oggetti — il file HTML base più le cinque immagini.

```
http://www.someSchool.edu/someDepartment/picture1.gif
```

Qui `http` è il **protocollo**, `www.someSchool.edu` l'**hostname** e `/someDepartment/picture1.gif` il **percorso** dell'oggetto. Un esempio reale di query:

```
https://en.wikipedia.org/w/index.php?title=SSC_Napoli
```

dove `https` è il protocollo, `en.wikipedia.org` l'hostname, `/w/index.php` il percorso della pagina e `?title=SSC_Napoli` la query; in questo caso equivale a chiedere la pagina `https://en.wikipedia.org/wiki/SSC_Napoli`.

## HTTP

HTTP definisce come i client Web chiedono oggetti (es. pagine) ai server Web e come i server li trasferiscono ai client. Quando l'utente chiede un oggetto (es. cliccando su un hyperlink), il **browser** invia messaggi di richiesta HTTP per gli oggetti della pagina al server, che riceve le richieste e risponde con messaggi HTTP contenenti gli oggetti. HTTP **evolve continuamente** per soddisfare i requisiti (affidabilità vs prestazioni) del networking moderno: HTTP/1.0 (1996), HTTP/1.1 (1997), HTTP/2 (2015), HTTP/3 (2022).

### Protocollo di trasporto

HTTP usa principalmente **TCP** come trasporto, ma dal 2022 (HTTP/3) può usare anche UDP: circa il 30% del traffico HTTP complessivo è oggi su UDP. Il client HTTP **per prima cosa apre una connessione** con il server; stabilita la connessione, browser e server comunicano tramite le proprie **interfacce socket**: il client invia richieste HTTP nel suo socket e riceve risposte dal suo socket, mentre il server fa viceversa.

Storicamente HTTP usava TCP per i suoi servizi utili, in particolare il **trasferimento affidabile dei dati**: TCP garantisce che richiesta e risposta arrivino integre a destinazione (se possibile). Tuttavia i servizi TCP possono rallentare la comunicazione, quindi le versioni recenti usano anche UDP, con una stima di circa il 30% di velocità in più rispetto alla sola comunicazione TCP; questo si basa sul protocollo **QUIC** (*Quick UDP Internet Connection*), che **implementa l'affidabilità sopra UDP**. Qui si vede uno dei **grandi vantaggi dell'architettura a livelli**: le applicazioni HTTP non devono preoccuparsi di raggiungibilità o perdita di dati, quindi possono essere **più semplici** (logicamente e computazionalmente), delegando gran parte del lavoro allo stack inferiore.

### Assenza di stato (statelessness)

La semplicità è fondamentale per server HTTP che gestiscono migliaia di richieste al secondo: in media un server esegue circa 1000 richieste HTTP al secondo, e i grandi motori di ricerca ricevono centinaia di migliaia di query al secondo. Le applicazioni HTTP sono tipicamente **stateless**: il server non mantiene informazioni sull'interazione (sequenza di richieste/risposte) con un client specifico. Se un client chiede due volte di seguito lo stesso oggetto, il server non considera la richiesta ridondante: **reinvia semplicemente l'oggetto**, avendo completamente dimenticato il passato. Non tutte le applicazioni sono però senza stato: diverse sono **stateful**.

## Connessioni persistenti e non persistenti

In molte applicazioni client e server comunicano per un periodo esteso, scambiando coppie richiesta-risposta multiple (una dietro l'altra, a intervalli regolari o intermittenti). Con un protocollo orientato alla connessione (TCP o QUIC) si possono usare **connessioni persistenti**, in cui tutte le richieste e le risposte corrispondenti passano sulla stessa connessione, oppure **connessioni non persistenti**, in cui per ogni coppia richiesta-risposta si stabilisce una nuova connessione. Oggi le applicazioni HTTP usano di default connessioni persistenti, ma client e server possono essere configurati diversamente; le prime versioni (HTTP 1.0) usavano non-persistenti di default.

### Esempio di connessione non persistente

Nella connessione non persistente la connessione si chiude ogni volta che una richiesta è servita (es. un oggetto inviato). Si consideri, su TCP, una pagina composta da un file HTML base e 10 immagini JPEG, tutti e 11 gli oggetti sullo stesso server, all'URL `http://www.someschool.edu/someDepartment/home.index`. La connessione avviene così:

1. Il **processo client HTTP apre una connessione TCP** verso il server sulla porta 80 (porta di default di HTTP); si avranno due socket, uno al client e uno al server.
2. Il **client invia un messaggio di richiesta HTTP** tramite il proprio socket, includendo il percorso `/someDepartment/home.index`.
3. Il **processo server riceve la richiesta**, **recupera** l'oggetto (da RAM o disco), lo **incapsula** in un messaggio di risposta HTTP e lo **rimanda** al client tramite il proprio socket.
4. Il **server chiede a TCP di chiudere** la connessione; TCP la terminerà (più tardi) solo quando sarà certo che il client ha ricevuto la risposta integra (affidabilità).
5. Il **client riceve la risposta**; la **connessione TCP termina**. Il messaggio indica che l'oggetto è un file HTML: il client lo estrae, esamina il file e **trova i riferimenti alle 10 immagini JPEG**.
6. I primi quattro passi **si ripetono** per ciascuno degli oggetti JPEG referenziati.

Poiché la connessione non persiste tra oggetti diversi, servono **11 connessioni TCP** (e 11 coppie di socket) per l'intera pagina, e gli elementi possono arrivare in momenti diversi. Si noti che HTTP **definisce solo il protocollo di comunicazione** tra programma client e programma server, non come i contenuti sono visualizzati: la visualizzazione **dipende dal browser**, e due browser possono interpretare (e mostrare) la stessa pagina in modo diverso, ad esempio attendendo il caricamento completo o mostrandola progressivamente.

Le connessioni multiple possono stabilirsi in **sequenza** o in **parallelo**: nell'esempio, noto che servono 10 JPEG, possiamo scaricarle tutte in parallelo. I browser moderni permettono di **configurare** il grado di parallelismo: la maggior parte apre 5-10 connessioni TCP parallele, ognuna per una transazione richiesta-risposta. Il parallelismo **riduce il tempo di risposta ma aumenta il costo computazionale**; nonostante il parallelismo, stabilire più connessioni TCP induce comunque un significativo **overhead di tempo**.

### RTT (Round-Trip Time)

È difficile stimare i tempi con precisione su Internet; possiamo però stimare l'overhead per completare una richiesta HTML in termini di **round-trip time** (RTT), cioè il tempo che un piccolo pacchetto impiega per andare dal client al server e tornare al client. Quando l'utente clicca su un hyperlink, il browser apre una connessione con il server. Con una richiesta TCP (orientata alla connessione), per stabilire la connessione si esegue un **three-way handshake**: il client invia un piccolo segmento TCP al server per richiedere la connessione, il server conferma e risponde con un piccolo segmento TCP, e il client conferma a sua volta.

Le prime due parti dell'handshake richiedono **un RTT**; in HTTP il client invia il messaggio di richiesta insieme alla terza parte dell'handshake (l'acknowledgment). Arrivata la richiesta, il server invia il file HTML: questa richiesta/risposta consuma **un altro RTT**. In grossolanità, il tempo di risposta totale è quindi **2 RTT più il tempo di trasmissione** del file HTML da parte del server. Un handshake simile avviene anche alla **chiusura** della connessione.

### Connessioni persistenti

Nelle connessioni persistenti il server **lascia aperta** la connessione TCP dopo aver inviato una risposta: richieste e risposte tra lo stesso client e server passano sulla stessa connessione, quindi un'intera pagina Web (file HTML + 10 immagini dell'esempio) può essere inviata su **una sola connessione TCP persistente**. Anche **più pagine Web** sullo stesso server possono essere inviate allo stesso client su una sola connessione persistente. Così si risparmiano grossolanamente **2-4 RTT per oggetto**.

### Pipelining

Con il **pipelining** le richieste di oggetti possono essere fatte una dietro l'altra, senza attendere le risposte alle richieste pendenti. Dagli ultimi anni (da HTTP/2) richieste e risposte multiple possono essere intervallate nella stessa connessione, ed esiste anche un meccanismo per dare priorità a richieste e risposte nella connessione. Le connessioni persistenti **con pipelining sono la modalità di default** di HTTP.

### Confronto: persistenti vs non persistenti

Le connessioni **persistenti** sono più veloci (soprattutto con il pipelining) e richiedono meno risorse (soprattutto memoria), ma sono più complesse da implementare; inoltre la connessione può restare aperta inutilizzata, quindi tipicamente il server HTTP la chiude dopo un certo tempo di inattività (*timeout*). Le connessioni **non persistenti** sono facili da implementare e coerenti con la statelessness di HTTP, ma richiedono più risorse — per ogni connessione vanno allocati buffer TCP e mantenute variabili TCP sia nel client che nel server — e sono più lente, con 1-2 RTT aggiuntivi per richiesta; le connessioni, infine, non possono restare aperte.