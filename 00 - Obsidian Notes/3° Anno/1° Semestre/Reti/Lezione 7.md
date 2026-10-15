# Application Layer DNS

## Identificazione degli host

Ci sono due modi per identificare un host:

- **Hostname**: identificatore mnemonico, preferito dalle persone.
- **Indirizzo IP**: identificatore a lunghezza fissa e struttura gerarchica, preferito dai dispositivi di rete.

> [!def] DNS
> **Domain Name System**: protocollo di livello applicativo che gestisce la **traduzione da hostname a indirizzo IP**; è un protocollo **client-server** in cui un client DNS chiede a un server DNS una traduzione specifica nome-indirizzo.

- Il DNS è un **database distribuito**, implementato in una gerarchia di server, più il protocollo applicativo che permette agli host di interrogarlo; query e risposte viaggiano in datagrammi **UDP sulla porta 53** (può usare anche TCP porta 53).
- I server DNS sono spesso macchine UNIX con il software **BIND** (*Berkeley Internet Name Domain*), il più diffuso su Linux e sistemi Unix-like.
- È l'unica applicazione che nessuno usa di proposito: lavora per le altre applicazioni e si vede solo quando fallisce.

Un repository centralizzato (tabella unica) è impossibile da gestire per il grande numero di host e per la distanza geografica (e i relativi ritardi): il DNS è quindi un sistema **distribuito e decentralizzato**, ovvero **gerarchico**, **basato su domini** e **implementato tramite un database distribuito**.

- **Singolo punto di guasto**: se crasha, ogni applicazione che risolve un nome si ferma con lui.
- **Traffico**: risponderebbe per ogni richiesta Web e ogni mail inviata sul pianeta.
- **Distanza**: non può essere vicino a tutti: dall'altro capo del mondo ogni lookup paga il viaggio.
- **Manutenzione**: un record per host, con host aggiunti e spostati di continuo.

Il DNS è quindi **distribuito per progetto**: gerarchico, basato su domini, e da nessuna parte completo — un sistema **distribuito e decentralizzato**, ovvero **gerarchico**, **basato su domini** e **implementato tramite un database distribuito**.

### Resolver

> [!def] Resolver
> **Componente** usato dalle applicazioni per richiedere la risoluzione dei nomi: costruisce la query DNS e ottiene la risposta, appoggiandosi a un server DNS configurato.

## Il name space DNS

- La gerarchia dei nomi è organizzata da **ICANN** (*Internet Corp. for Assigned Names and Numbers*).
- Esistono circa 250 **top-level domain (TLD)**, di due tipi, tutti gestiti da registrar nominati da ICANN:
  - **Generici**: `aero`, `com`, `edu`, ecc.
  - **Geografici** (country): `uk`, `it`, `tv`, ecc.
- Ogni dominio è partizionato in sotto-domini, e così via; lo name space è gerarchico **dalla radice verso il basso**, con parti diverse delegate a organizzazioni diverse.

Alcuni domini generici di riferimento:

| Dominio | Uso previsto | Anno | Ristretto? |
|---|---|---|---|
| `com` | Commerciale | 1985 | No |
| `edu` | Istituzioni educative | 1985 | Sì |
| `gov` | Governo | 1985 | Sì |
| `int` | Organizzazioni internazionali | 1988 | Sì |
| `mil` | Militare | 1985 | Sì |
| `net` | Fornitori di rete | 1985 | No |
| `org` | Organizzazioni non-profit | 1985 | No |
| `aero` | Trasporto aereo | 2001 | Sì |
| `biz` | Imprese | 2001 | No |
| `info` | Informativo | 2002 | No |
| `name` | Persone | 2002 | No |
| `pro` | Professionisti | 2002 | Sì |
| `tel` | Dettagli di contatto | 2005 | Sì |
| `xxx` | Industria del sesso | 2010 | No |

Regole dei nomi di dominio:

- I nomi sono **percorsi verso l'alto** dal dominio alla radice (es. `eng.mit.edu`); i percorsi **assoluti terminano con un punto**, quelli relativi vanno interpretati.
- È possibile registrarsi sotto **più di un** top-level domain (es. `ibm.com`, `ibm.us`).
- Ogni dominio controlla l'allocazione dei domini sottostanti: creare un nuovo dominio richiede il **permesso del dominio padre**.
- Il naming **non segue** i confini fisici/geografici.
- **Cyber-squatting**: acquisto di domini solo per rivenderli successivamente ad aziende interessate.

## Resource record
I record di risorsa (**resource record**) sono le voci del database distribuito: sono ciò che un server restituisce e ciò di cui è fatta una zona. Una risposta DNS trasporta uno o più record, e questi record, sparsi su molti server, **sono** il database, non è mai conservato interamente da nessuna parte.

> [!def] Resource record
> **Voce** del database distribuito DNS con cinque campi: **name**, **time to live**, **class**, **type**, **value**. Il tipo decide come leggere gli altri due: cosa significa il nome e cosa significa il valore.

La distribuzione DNS mappa i domini su valori tramite **resource record**, con i seguenti campi:

- **Domain name (NAME)**: dominio a cui il record si applica; è la **chiave di ricerca** principale delle query DNS; per ogni dominio esistono normalmente più record su server diversi.
- **Time to live (TTL)**: vita del record; lungo per host stabili (es. 86400 = 1 giorno), breve per host volatili (es. 60 = 1 minuto); massimo $2^{31}-1$, circa 68 anni.
- **Class (CLASS)**: sempre `IN` (Internet) per i record Internet; altri codici sono raramente usati.
- **Type (TYPE)**: tipo del record (vedi sotto).
- **Value (RDATA)**: dipende dal tipo; può contenere un dominio, un valore o una stringa ASCII.

### Tipi di record principali:

| Tipo | Significato | Valore |
|---|---|---|
| `SOA` | Start of authority | Parametri della zona, contatti dell'amministratore |
| `A` | Indirizzo IPv4 dell'host | Intero a 32 bit (più interfacce → più record) |
| `AAAA` | Indirizzo IPv6 dell'host | Intero a 128 bit |
| `MX` | Mail exchange | Priorità, dominio che accetta la posta per il dominio |
| `NS` | Name server | Nome di un server per il dominio (usato nella risoluzione) |
| `CNAME` | Canonical name | Alias: la lookup prosegue col nuovo nome |
| `PTR` | Pointer | Alias per il reverse lookup (nome restituito senza procedere) |
| `SPF` | Sender policy framework | Codifica testuale della policy di invio mail |
| `SRV` | Service | Host che fornisce il servizio |
| `TXT` | Text | Testo ASCII descrittivo |

## Name server e zone

![[Lezione 7-1792083548316.webp|250]]

Un unico server DNS centralizzato non avrebbe senso: lo space DNS è partizionato in **zone non sovrapposte**; il partizionamento spetta all'amministratore della zona.

- Ogni zona contiene **uno o più name server**: uno primario e uno (o più) secondario.
- I name server contengono i dati delle porzioni di name space dette zone.

> [!def] Zona
> **Dominio**: un nodo dell'albero DNS e tutti i suoi discendenti (gerarchia di naming). **Zona**: la porzione di quel dominio gestita dalla **stessa autorità DNS**; delegando un sottodominio si crea una nuova zona, che però resta parte del dominio padre (es. se `cs.unina.it` è delegata, diventa una zona separata restando parte del dominio `unina.it`). Dominio = gerarchia di naming; zona = autorità amministrativa.

### Name resolution

La **risoluzione dei nomi** (name resolution) procede così:

1. L'host interroga un **server DNS locale**.
2. Se il dominio cade sotto la giurisdizione (zona) del server locale, viene restituito un record **authoritative**.
3. Altrimenti il server locale gestisce la query **ricorsivamente** e inoltra query remote: se il server DNS interrogato ha l'indirizzo lo restituisce, altrimenti restituisce il name server di una **zona più bassa**; il processo continua **iterativamente** fino a trovare l'indirizzo.

#### Query ricorsive e iterative

- **Query ricorsiva**: chi viene interrogato deve produrre la risposta finale, o un errore; chi chiede aspetta e non fa nulla.
- **Query iterativa**: la risposta è o la risposta, o un *referral* al server successivo; chi chiede continua a lavorare.

Suddivisione dei ruoli:

- L'**host** chiede una volta, ricorsivamente: una query fuori, un indirizzo dentro.
- Il **server locale** fa il percorso, iterativamente, un server alla volta (**recursive DNS resolver**).
- I server **root, TLD e authoritative** rispondono normalmente in modo iterativo: restituiscono una risposta autoritativa o un referral, invece di fare ricorsione per il client.

#### Root server

Sui **root server**:

- Sono il punto di partenza quando non si ha alcuna informazione.
- Sono **13**, da `a.root-servers.net` a `m.root-servers.net`, altamente replicati.
- Sono molto occupati, quindi in genere restituiscono informazioni su zone più basse, non sui singoli record.

---

Sui tipi di query e record:

- I server DNS locali gestiscono **query ricorsive** (servizio verso i propri host): restituiscono la risposta completa o un errore.
- Molti server DNS (i più occupati, es. quelli vicini alla cima) **non gestiscono** query ricorsive.
- I record sono **authoritative** oppure **cached**: tutte le risposte vengono mesche in cache, i record cached **scadono** (ricorda il TTL) e non provengono dal server che gestisce la zona (risposte *non authoritative*); il caching migliora le prestazioni, poiché l'indirizzo può essere restituito subito dal server locale.
- I root server sono interrogati solo in **assenza totale** di informazioni su un dominio; se per `cs.mit.edu` arriva una richiesta e il server ha l'indirizzo del DNS server di `mit.edu`, può interrogare direttamente quello.

## Il resolver locale e i servizi aggiuntivi

> [!aside]
> > [!def] Local DNS server
> > **Server DNS locale** (o resolver): tipo di server DNS che **non appartiene strettamente** alla gerarchia, tipicamente gestito dagli ISP; fa da **proxy**, inoltrando le query dell'host alla gerarchia DNS.
> 
> - Anche Google fornisce resolver pubblici (Google Public DNS) agli indirizzi `8.8.8.8` e `8.8.4.4`.
> - Quando un host si connette, l'ISP gli fornisce gli IP di uno o più server DNS locali, tipicamente "vicini" all'host.
> 
> ![[Lezione 7-1792083897958.webp|200]]

Servizi aggiuntivi del DNS:

- **Aliasing**: servizio che associa nomi lunghi/complicati (nomi **canonicali**) a nomi più semplici (**alias**); un host con nome complicato può avere alias mnemonici (es. `relay1.west-coast.enterprise.com` → `www.enterprise.com`); l'applicazione può comunque chiedere al DNS il nome canonico di un alias insieme all'indirizzo IP.
- **Load distribution**: distribuzione del carico tra **server replicati** (*round-robin DNS*); i siti trafficati sono replicati su più server con indirizzi IP diversi (più IP associati a un solo nome canonico); il server può **ruotare l'ordine** degli indirizzi nelle risposte, così i client vengono distribuiti sulle repliche.

Con `nslookup` si può eseguire manualmente la query iterativa fatta dal server locale, ed è possibile anche il **reverse lookup** (nome a partire dall'indirizzo).

> [!lab]
> ```bash
> #Richiesta
> ❯ nslookup www.vatican.va
> 
> #Risposta
> Server:         127.0.0.53
> Address:        127.0.0.53#53
> 
> Non-authoritative answer:
> www.vatican.va  canonical name = vatican-g5fcczeabnb9atb6.a03.azurefd.net.
> vatican-g5fcczeabnb9atb6.a03.azurefd.net        canonical name = mr-a03.tm-azurefd.net.
> Name:   mr-a03.tm-azurefd.net
> Address: 150.171.110.52
> Name:   mr-a03.tm-azurefd.net
> Address: 2603:1061:14:133::1
> ```

