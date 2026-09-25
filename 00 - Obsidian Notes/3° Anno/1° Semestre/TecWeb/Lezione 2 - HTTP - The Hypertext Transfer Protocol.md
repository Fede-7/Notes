# Lezione 2: HTTP: The Hypertext Transfer Protocol

## Il Contesto: Web Technologies

Nel percorso dello studio del web, sono stati già affrontati i fondamenti della **World Wide Web** come sistema distribuito di risorse identificate da URL, e il **Domain Name System (DNS)** come meccanismo di risoluzione dei nomi di dominio in indirizzi IP. A questo punto, la domanda naturale è: cosa accade dopo che un client ottiene l'indirizzo IP del server? Come comunica il client con il server per richiedere una risorsa specifica, e come si sviluppa concretamente questo scambio di informazioni?

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-24/1c1f3f0c-3c72-49eb-9b4b-09d84679c1af/5ff05608f6d8575ea9ffd9fda6a08c2fef7493fb5ca51453250c863c5524d159.jpg)

## Il Web e il Protocollo HTTP

### Fondamenti della World Wide Web

L'**Internet** è una rete globale di computer interconnessi che condividono informazioni attraverso i protocolli Internet. Le sue origini risalgono ad **ARPANET nel 1969**.

La **World Wide Web**, comunemente denominata WWW o semplicemente "il Web", è un sottoinsieme dell'Internet più ampio. È stata inventata da **Sir Tim Berners-Lee nei primi anni Novanta** come un sistema di documenti ipertestuali interconnessi, dove ciascun documento contiene link (detti **iperlink**) a altri contenuti — altri ipertesti, documenti, o media. I componenti fondamentali del Web sono **HTTP** e **HTML**.

### I Documenti Ipertestuali

I documenti tradizionali sono semplicemente sequenze di caratteri. I **documenti ipertestuali**, invece, includono anche link (iperlink) che collegano il contenuto ad altri materiali, creando una struttura reticolare di informazioni interconesse.

### Il Flusso di una Richiesta Web

Quando un utente digita un indirizzo come `http://squids.unina.it` nel browser, avviene una sequenza di operazioni ben definita: il browser effettua una richiesta DNS per risolvere il nome di dominio `squids.unina.it` in un indirizzo IP (ad esempio `143.225.131.206`). Una volta ottenuto l'IP, il client stabilisce un canale di comunicazione TCP con il server su quella destinazione. Attraverso questo canale, il browser invia una richiesta HTTP specificando quale risorsa desidera. Il server riceve la richiesta, la elabora e invia indietro una risposta HTTP contenente la risorsa richiesta o un messaggio di errore appropriato.

## HTTP: Hypertext Transfer Protocol

### Caratteristiche e Ruolo

**HTTP** è un **protocollo applicativo** costruito sopra **TCP/IP** e rappresenta la fondazione e la spina dorsale della World Wide Web. Sviluppato originariamente per la trasmissione di ipertesti, è oggi utilizzato anche per la trasmissione di altre tipologie di risorse. Nel modello HTTP, il **client invia una richiesta** al server per interagire con una risorsa, e il **server risponde** alla richiesta. Le risorse sono identificate da **URL (Uniform Resource Locator)**.

## URL: Uniform Resource Locator

Un URL completo ha la forma: `https://www.informatica.it:4242/corsi/tecweb.html`

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-24/1c1f3f0c-3c72-49eb-9b4b-09d84679c1af/cfd3bbb7b91b1a8bb97efc0c008318034f036e36710e2f8bd2d27f9ecbed6eef.jpg)
### Componenti di un URL

**Schema (Protocollo)**: specifica il protocollo utilizzato per accedere alla risorsa. I protocolli web più comuni sono **http** e **https**. **HTTPS (HTTP Secure)** rappresenta HTTP su una connessione crittografata tramite **Transport Layer Security (TLS)**, che svolge un ruolo cruciale nel mitigare diversi tipi di attacchi alle applicazioni web.

**Nome di Dominio (Host)**: è il nome del server web che ospita la risorsa. Questo nome viene risolto a un indirizzo IP attraverso il DNS.

**Porta**: è il numero della porta sulla quale il server è in ascolto per le connessioni. Se il server utilizza le porte standard (80 per HTTP, 443 per HTTPS), la porta può essere omessa dall'URL; altrimenti deve essere esplicitamente specificata.

**Percorso (Path)**: indica la posizione specifica della risorsa sul server, tipicamente relativa a una **directory radice (document root)**. I server sono configurati per servire solo i file presenti all'interno di questa directory, poiché non si desidera che tutti i file del sistema siano accessibili via web.

Gli URL possono inoltre contenere **parametri di query** e **ancoraggi**, argomenti che verranno affrontati nelle lezioni successive.

## Lo Scambio Richiesta-Risposta HTTP

Nel modello HTTP, il client invia una **richiesta** che specifica: quale operazione eseguire sulla risorsa, quale risorsa è destinataria della richiesta, under quali condizioni o preferenze di accesso, e se vi è contenuto allegato alla richiesta. A sua volta, il server invia una **risposta** che comunica: quale è stato l'esito dell'elaborazione, quali metadati descrivono il risultato, e se vi è contenuto allegato alla risposta.

## Richieste HTTP

### Struttura di una Richiesta

Una richiesta HTTP è composta da:

- **Linea di Richiesta**: contiene il verbo HTTP, il percorso della risorsa, e la versione del protocollo.
- **Intestazioni (Headers)**: metadata aggiuntivi che forniscono informazioni sulla richiesta.
- **Linea Vuota**: separa le intestazioni dal corpo della richiesta.
- **Corpo della Richiesta (facoltativo)**: contiene dati, se necessari.

#### Esempio di una Richiesta

```
GET /wisdom/grain.txt HTTP/1.1
Host: bookofprogramming.com
User-Agent: Mozilla/5.0
Accept: text/plain
Accept-Language: en-us
Connection: keep-alive
```

### Metodi HTTP (Verbi)

I metodi HTTP indicano lo scopo della richiesta rispetto alla risorsa:

- **GET**: Recupera una rappresentazione della risorsa.
- **POST**: Invia nuovi dati alla risorsa specificata, con effetti collaterali (mutamento dello stato del server).
- **PUT**: Sostituisce la risorsa corrente con il payload fornito.
- **DELETE**: Elimina la risorsa specificata.
- **HEAD**: Recupera gli stessi metadati di GET, senza il corpo della risposta.
- **PATCH**: Applica una modifica parziale a una risorsa.
- **OPTIONS**: Chiede informazioni sulle opzioni di comunicazione disponibili.
- **QUERY** : 

Consulta la [documentazione ufficiale su MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) per il riferimento completo.

### Semantica dei Metodi: Sicurezza e Idempotenza

◇ Un metodo è **sicuro** se non modifica lo stato del server, poiché comporta solo operazioni di lettura. Logging e audit non interferiscono con questa proprietà, quindi le richieste sicure possono comunque essere registrate. I metodi **GET, HEAD, QUERY e OPTIONS** sono sicuri.

◇ Un metodo è **idempotente** se l'effetto desiderato sul server di una singola richiesta è equivalente a quello di molteplici richieste identiche consecutive. Tutti i metodi sicuri sono anche idempotenti. **PUT e DELETE** sono idempotenti, mentre **POST e PATCH** non lo sono necessariamente.

#### Tabella Sintetica di Sicurezza e Idempotenza

| Metodo  | Sicuro | Idempotente                    |
| ------- | ------ | ------------------------------ |
| GET     | Sì     | Sì                             |
| HEAD    | Sì     | Sì                             |
| OPTIONS | Sì     | Sì                             |
| PUT     | No     | Sì                             |
| DELETE  | No     | Sì                             |
| POST    | No     | Non garantito (solitamente no) |
| PATCH   | No     | Non garantito (solitamente no) |
| QUERY   | Si     | Si                             |

### Intestazioni delle Richieste

Le intestazioni HTTP sono meccanismi per passare informazioni aggiuntive nelle richieste e nelle risposte. Un'intestazione è composta da un nome (case-insensitive) seguito da un due-punti e dal valore: `HEADER_NAME: value`. L'**Internet Assigned Numbers Authority (IANA)** mantiene un elenco ufficiale di intestazioni permanenti e provvisorie. È inoltre possibile definire intestazioni personalizzate. Consulta il [riferimento MDN sulle intestazioni HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) per ulteriori dettagli.

## Risposte HTTP

### Struttura di una Risposta

Una risposta HTTP è composta da:

- **Linea di Stato**: contiene la versione del protocollo, il codice di stato, e un messaggio descrittivo.
- **Intestazioni (Headers)**: metadati che descrivono la risposta.
- **Linea Vuota**: separa le intestazioni dal corpo della risposta.
- **Corpo della Risposta (facoltativo)**: contiene la risorsa richiesta o ulteriori informazioni.

#### Esempio di una Risposta

```
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 153

Fu-Tzu said: 'When you cut against the grain of the wood, much strength is needed. When you program against the grain of a problem, much code is needed.'
```

### Codici di Stato HTTP

I codici di stato indicano se una richiesta è stata completata con successo. Sono organizzati in cinque classi:

- **1xx (Informazionale)**: Lo scambio richiesta-risposta è in corso.
- **2xx (Successo)**: La richiesta è stata elaborata con successo.
- **3xx (Reindirizzamento)**: Il client deve intraprendere un'azione aggiuntiva, ad esempio un reindirizzamento.
- **4xx (Errore della Richiesta)**: La richiesta non può essere elaborata come presentata (errore nel client).
- **5xx (Errore del Server)**: Il server, o un componente intermedio come un database, ha fallito.

Esempi comuni includono **200 OK** (successo), **301 Moved** (reindirizzamento permanente), **400 Bad Request** (richiesta malformata), **403 Forbidden** (accesso negato), **404 Not Found** (risorsa non trovata), **500 Application Error** (errore interno del server), e **503 Service Unavailable** (servizio temporaneamente non disponibile). Consulta la [documentazione dettagliata](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) per un elenco completo.

## L'Intestazione Host

Una questione che sorge naturalmente è: perché le richieste HTTP includono un'intestazione **Host** quando il nome di dominio è già stato risolto in indirizzo IP dal DNS?

La risposta risiede nel fatto che **più nomi di dominio possono risolvere allo stesso indirizzo IP**. Ad esempio, i nomi `www.dieti.unina.it`, `informatica.dieti.unina.it`, `biblioteca.dieti.unina.it` e `erasmus.dieti.unina.it` possono tutti risolvere allo stesso indirizzo IP `143.225.97.81`. Un server HTTP può essere configurato per servire **più host virtuali** (siti web distinti) su una singola macchina. L'**intestazione Host** consente al server di selezionare il host virtuale corretto in base al nome di dominio richiesto, poiché il server non conosce automaticamente quale dominio il client ha digitato nel browser; conosce solo l'indirizzo IP verso cui la connessione è stata stabilita.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-09-24/1c1f3f0c-3c72-49eb-9b4b-09d84679c1af/b0f0bacd2080e64df5c731eff4d7c62b1d4d3ec292345f463bc7aa9f6f46aabf.jpg)

## La Natura Stateless di HTTP

**HTTP è un protocollo stateless**, il che significa che ogni richiesta è indipendente dalle precedenti e il server non mantiene informazioni sui progressi delle richieste precedenti di un client. Questa semplicità è un vantaggio architetturale, ma per implementare conversazioni "statefull" (con memória del contesto) è necessario ricorrere a meccanismi specifici, come i **cookie**, che verranno approfonditi nelle lezioni successive.

## Server HTTP

### Definizione e Ruoli

Un **server HTTP** è un software in esecuzione su una macchina host che:
- è in ascolto su una porta specifica (ad esempio 80 per HTTP, 443 per HTTPS);
- riceve richieste HTTP;
- interpreta il metodo, la destinazione e le intestazioni della richiesta;
- produce una risposta HTTP.

Il termine "server" può riferirsi a più entità: 
- il **ruolo** del server come partecipante che risponde alle richieste; 
- il **software** server che ascolta le richieste HTTP e risponde; 
- il **processo** come istanza esecutiva del software;
- la **macchina** su cui il software è in esecuzione.

### Modalità di Elaborazione delle Richieste

Quando un server gestisce una richiesta, può costruire la risposta in modi diversi. Può recuperare un file dal proprio file system (servendo **file statici**) e includerne il contenuto nel corpo della risposta. Alternativamente, può **eseguire codice per generare una risposta dinamicamente**, il che può coinvolgere interrogazioni di database e interazioni con altri sistemi, con complessità arbitraria.

Tra i server HTTP statici più noti figurano **nginx** e **Apache httpd**.

### Server HTTP Statici

Un server statico mappa le risorse richieste a file nel file system. Questa mappatura è configurata dal server. Tipicamente, i server sono configurati per servire file da una directory specifica, denominata **document root**. Ad esempio, con una document root impostata a `/var/www/`, una richiesta `GET /webtech/hello.txt` potrebbe essere mappata al file `/var/www/webtech/hello.txt`. La directory root (e molte altre configurazioni) può generalmente essere specificata in file di configurazione dedicati. Consulta la documentazione dei server specifici, come [nginx](https://nginx.org) e [httpd](https://httpd.apache.org), per ulteriori dettagli.

---

> [!note]
> ### Configurazione di NGINX con Docker
>
> Per il setup di NGINX tramite Docker, le directory locali che contengono i dati dei siti web vengono montate (bind-mount) nelle corrispondenti directory del container. Analogamente, il file di configurazione locale `nginx.conf` viene montato nel percorso dove NGINX cerca i file di configurazione (`/etc/nginx/nginx.conf`).
>
> #### Composizione Docker
>
> ```yaml
> services:
>   nginx:
>     image: nginx:1.31.3
>     ports:
>       - "80:80"
>     volumes:
>       # Bind-mount the website directories
>       - ./website-book-of-programming:/usr/share/nginx/html/book-of-programming
>       - ./website-web-technologies:/usr/share/nginx/html/web-technologies
>       # Bind-mount the custom nginx configuration file
>       - ./nginx.conf:/etc/nginx/nginx.conf:ro
> ```
>
> #### Configurazione di NGINX
>
> Il file `nginx.conf` definisce due virtual host distinti: `book-of-programming.local` e `web-technologies.local`, ciascuno con una propria document root diversa.
>
> ```hcl
> events {}
> http {
>     # Other config details omitted (for now)
>     # Define two server blocks, one for each website.
>     server {
>         listen 80;
>         server_name book-of-programming.local;
>         root /usr/share/nginx/html/book-of-programming;
>     }
>
>     server {
>         listen 80;
>         server_name web-technologies.local;
>         root /usr/share/nginx/html/web-technologies;
>     }
> }
> ```
>
> Questa configurazione consente a NGINX di servire due siti web completamente distinti sulla medesima porta (80), discriminando tra essi sulla base del nome di dominio indicato nell'intestazione **Host** della richiesta HTTP.

---

## Risoluzione DNS per Siti Web Locali

Il suffisso `.local` non è un **Top-Level Domain (TLD)** che può essere acquistato pubblicamente. Per fare in modo che i nomi di dominio `book-of-programming.local` e `web-technologies.local` vengano risolti all'indirizzo IP corretto (127.0.0.1), è necessario ricorrere a un meccanismo locale. Nei sistemi operativi moderni, è possibile utilizzare il **file hosts** per ottenere questo risultato. Su Windows il file si trova in `C:\Windows\System32\drivers\etc\hosts`, mentre su Linux e macOS in `/etc/hosts`.

I **risolutori DNS stub** (le componenti locali del sistema di risoluzione dei nomi) consultano questo file prima di inviare la richiesta a un risolutore ricorsivo remoto. Aggiungendo al file hosts una voce come `127.0.0.1 book-of-programming.local`, le richieste DNS per questo dominio verranno automaticamente risolte a 127.0.0.1 (localhost).

> [!example]
> 
> #### Esempio di Configurazione del File Hosts
>
> | Indirizzo IP | Hostname |
> |--------------|----------|
> | 127.0.0.1 | localhost |
> | ::1 | localhost |
> | 127.0.0.1 | web-technologies.local |
> | 127.0.0.1 | book-of-programming.local |

## Analisi delle Richieste HTTP negli Strumenti del Browser

Gli **strumenti di sviluppo del browser** rappresentano risorse indispensabili durante lo studio del web. Non richiedono alcuna installazione, in quanto sono integrati in tutti i browser moderni. Generalmente è possibile accedervi premendo **F12** o selezionando **Inspect** dal menu contestuale delle pagine web. Sebbene gli strumenti siano essenzialmente equivalenti tra i vari browser, possono esistere minori differenze nell'interfaccia. Includono una vasta gamma di utility dedicate al debugging, alla risoluzione dei problemi e all'analisi delle applicazioni web.

### La Scheda Network

Tramite la scheda **Network**, è possibile visualizzare tutte le richieste HTTP effettuate dal browser e accedere a informazioni dettagliate su ciascuna richiesta:

- Le **intestazioni di richiesta e di risposta** forniscono metadati essenziali.
- I **corpi di richiesta e di risposta** contengono i dati effettivi scambiati.
- Il **metodo della richiesta** e il **percorso** specificano l'operazione e la risorsa target.
- I **codici di stato della risposta** indicano l'esito dell'elaborazione.

Inoltre, è disponibile un'**analisi temporale dettagliata** che misura il tempo impiegato per risolvere il DNS, stabilire la connessione TCP, inviare la richiesta e ricevere la risposta. Queste informazioni sono preziose per diagnosticare problemi di performance e comprendere il flusso di una comunicazione HTTP completa.

## REST Client in VS Code

L'estensione **REST Client** per VS Code consente di scrivere richieste HTTP in file di testo con estensione `.http` e di inviarle direttamente dall'editor. Questo rappresenta un metodo pratico per inviare richieste HTTP rapide e, soprattutto, è particolarmente utile quando si sta imparando il protocollo HTTP. È possibile comporre richieste complesse, visualizzare le risposte e sperimentare diversi scenari senza abbandonare l'ambiente di sviluppo.

## Client HTTP Dedicati

Esistono applicazioni client HTTP specializzate, come **Postman**, **Bruno** e **Insomnia**, che forniscono un'interfaccia grafica intuitiva per definire richieste HTTP e ispezionare le risposte. Questi strumenti includono generalmente funzionalità avanzate per la gestione di collezioni di richieste, l'automazione di test, la generazione di molteplici richieste e altro ancora. Diventeranno particolarmente utili quando verrà affrontato lo sviluppo di API web-based nelle lezioni successive.