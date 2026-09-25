# Lezione 2: HTTP: The Hypertext Transfer Protocol

## Il Contesto: Web Technologies

**Internet** è una rete globale di computer interconnessi che condividono informazioni tramite i protocolli Internet; le sue origini risalgono ad **ARPANET** (1969). La **World Wide Web** (WWW, o semplicemente "il Web") non coincide con Internet: ne è un sottoinsieme. Fu inventata da Sir Tim Berners-Lee all'inizio degli anni '90 come sistema di **documenti ipertestuali** interconnessi tramite **hyperlink**, e i suoi componenti fondamentali sono **HTTP** e **HTML**.

### Ipertesti

I documenti tradizionali sono semplici sequenze di caratteri. Un **ipertesto**, invece, è un documento che contiene anche collegamenti ad altri contenuti, come altri ipertesti, documenti o media.

## HTTP: Hypertext Transfer Protocol

### Caratteristiche e Ruolo

**HTTP** è un **protocollo applicativo** costruito sopra **TCP/IP** e rappresenta la fondazione e la spina dorsale della World Wide Web. Sviluppato originariamente per la trasmissione di ipertesti, è oggi utilizzato anche per la trasmissione di altre tipologie di risorse. Nel modello HTTP, il **client invia una richiesta** al server per interagire con una risorsa, e il **server risponde** alla richiesta. Le risorse sono identificate da **URL (Uniform Resource Locator)**.

### URL: Uniform Resource Locator

Un URL completo ha la forma: 

![[Lezione 2 - HTTP - The Hypertext Transfer Protocol-1790354892063.png]]
### Intestazioni delle Richieste

Le intestazioni HTTP sono meccanismi per passare informazioni aggiuntive nelle richieste e nelle risposte. Un'intestazione è composta da un nome (case-insensitive) seguito da un due-punti e dal valore: `HEADER_NAME: value`. 

> [!faq] nota: 
> L'**Internet Assigned Numbers Authority (IANA)** mantiene un elenco ufficiale di intestazioni permanenti e provvisorie. È inoltre possibile definire intestazioni personalizzate. 
> Consulta il [riferimento MDN sulle intestazioni HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) per ulteriori dettagli.

## Risposte HTTP

### Struttura di una Risposta

Una risposta HTTP è composta da:

- **Linea di Stato**: contiene la versione del protocollo, il codice di stato, e un messaggio descrittivo.
- **Intestazioni (Headers)**: metadati che descrivono la risposta.
- **Linea Vuota**: separa le intestazioni dal corpo della risposta.
- **Corpo della Risposta (facoltativo)**: contiene la risorsa richiesta o ulteriori informazioni.

> [!example] Esempio di una Risposta
> 
> ```http
> HTTP/1.1 200 OK
> Content-Type: text/plain
> Content-Length: 153
> ```

### Codici di Stato HTTP

I codici di stato indicano se una richiesta è stata completata con successo. Sono organizzati in cinque classi:

- **1xx (Informazionale)**: Lo scambio richiesta-risposta è in corso.
- **2xx (Successo)**: La richiesta è stata elaborata con successo.
- **3xx (Reindirizzamento)**: Il client deve intraprendere un'azione aggiuntiva, ad esempio un reindirizzamento.
- **4xx (Errore della Richiesta)**: La richiesta non può essere elaborata come presentata (errore nel client).
- **5xx (Errore del Server)**: Il server, o un componente intermedio come un database, ha fallito.

> [!example] Esempi comuni
>  **200 OK** (successo), 
>  **301 Moved** (reindirizzamento permanente), 
>  **400 Bad Request** (richiesta malformata),
>   **403 Forbidden** (accesso negato), 
>   **404 Not Found** (risorsa non trovata),
>    **500 Application Error** (errore interno del server),
>    **503 Service Unavailable** (servizio temporaneamente non disponibile). 
>    
> Consulta la [documentazione dettagliata](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) per un elenco completo.

### L'Intestazione Host

Una questione che sorge naturalmente è: perché le richieste HTTP includono un'intestazione **Host** quando il nome di dominio è già stato risolto in indirizzo IP dal DNS?

In realtà **più nomi di host possono risolvere allo stesso IP** — ad esempio `www`, `informatica`, `biblioteca` ed `erasmus.dieti.unina.it` puntano tutti a 143.225.97.81. 
Poiché un server HTTP può essere configurato per gestire più **virtual host**, ciascuno con la propria document root, è proprio l'header **Host** a permettergli di selezionare il virtual host corretto, poiché il server non conosce automaticamente quale dominio il client ha digitato nel browser; conosce solo l'indirizzo IP verso cui la connessione è stata stabilita.

![[Lezione 2 - HTTP - The Hypertext Transfer Protocol-1790354846207.png]]

## Caratteristica Statelessness

**HTTP è un protocollo stateless**, il che significa che ogni richiesta è indipendente dalle precedenti e il server non mantiene informazioni sui progressi delle richieste precedenti di un client. 

Questa semplicità è un vantaggio architetturale, ma per implementare conversazioni "statefull" (con memória del contesto) è necessario ricorrere a meccanismi specifici, come i **cookie**.

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

Quando un server gestisce una richiesta, può costruire la risposta in modi diversi. 
- Può recuperare un file dal proprio file system (servendo **file statici**) e includerne il contenuto nel corpo della risposta. 
- Può **eseguire codice per generare una risposta dinamicamente**, il che può coinvolgere interrogazioni di database e interazioni con altri sistemi, con complessità arbitraria.

Tra i server HTTP statici più noti figurano **nginx** e **Apache httpd**.

### Server HTTP Statici

I server statici mappano le risorse richieste a file nel filesystem, secondo una configurazione decisa dal server. Tipicamente si servono i file a partire da una directory specifica, la **document root**: se questa è `/var/www/`, la richiesta `GET /webtech/hello.txt` restituisce `/var/www/webtech/hello.txt`. La root e molte altre impostazioni si definiscono nei file di configurazione dedicati del server.

> [!example] Esempio: nginx in Docker
> 
> ```nginx
> services:
>   nginx:
>     image: nginx:1.31.3
>     ports:
>       - "80:80"
>     volumes:
>       - ./website-book-of-programming:/usr/share/nginx/html/book-of-programming
>       - ./website-web-technologies:/usr/share/nginx/html/web-technologies
>       - ./nginx.conf:/etc/nginx/nginx.conf:ro
> ```
> 
> Il file `nginx.conf` definisce due blocchi `server`, cioè due virtual host (`book-of-programming.local` e `web-technologies.local`), ciascuno con una document root diversa:
> 
> ```nginx
> events {}
> http {
>     server {
>         listen 80;
>         server_name book-of-programming.local;
>         root /usr/share/nginx/html/book-of-programming;
>     }
>     server {
>         listen 80;
>         server_name web-technologies.local;
>         root /usr/share/nginx/html/web-technologies;
>     }
> }
> ```
> 

## Risoluzione DNS per Siti Web Locali

Il suffisso `.local` non è un **Top-Level Domain (TLD)** che può essere acquistato pubblicamente. Per fare in modo che i nomi di dominio `book-of-programming.local` e `web-technologies.local` vengano risolti all'indirizzo IP corretto (127.0.0.1), è necessario ricorrere a un meccanismo locale. Nei sistemi operativi moderni, è possibile utilizzare il **file hosts** per ottenere questo risultato. Su Windows il file si trova in `C:\Windows\System32\drivers\etc\hosts`, mentre su Linux e macOS in `/etc/hosts`.

I **risolutori DNS stub** (le componenti locali del sistema di risoluzione dei nomi) consultano questo file prima di inviare la richiesta a un risolutore ricorsivo remoto. Aggiungendo al file hosts una voce come `127.0.0.1 book-of-programming.local`, le richieste DNS per questo dominio verranno automaticamente risolte a 127.0.0.1 (localhost).

> [!example]
> 
> #### Esempio di Configurazione del File Hosts
>
> | Indirizzo IP | Hostname |
> |--------------|----------|
> | 127.0.0.1 | localhost (IPv4) |
> | ::1 | localhost (IPv6) |
> | 127.0.0.1 | web-technologies.local |
> | 127.0.0.1 | book-of-programming.local |

## Strumenti per fare richieste HTTP

### Dev tools del browser

I dev tools del browser sono strumenti integrati, accessibili con **F12** o con *tasto destro → Ispeziona*, ed equivalenti tra i browser moderni. La scheda **Network** mostra le richieste HTTP effettuate: header e body di richiesta e risposta, metodo e percorso, codici di stato e un'analisi dettagliata dei tempi, dalla risoluzione DNS alla connessione, dall'invio della richiesta alla ricezione della risposta.

### REST Client in VS Code

L'estensione REST Client per VS Code permette di scrivere richieste HTTP in file di testo con estensione `.http` e di inviarle al volo dall'editor: un modo pratico per richieste rapide e molto utile per imparare HTTP.

### Client HTTP dedicati

Esistono anche client HTTP dedicati, come **Postman**, **Bruno** e **Insomnia**, che offrono una GUI per definire richieste e ispezionare risposte. Tipicamente includono funzioni avanzate per gestire collezioni di richieste e per il testing, e si rivelano utili quando si sviluppano API web.
