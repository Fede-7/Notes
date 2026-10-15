# Lezione 7 Application Layer DNS

<<FINIRE DI CORREGGERE>>

## Name server e zone

Un unico server DNS centralizzato non avrebbe senso: lo name space DNS è partizionato in **zone non sovrapposte**; il partizionamento spetta all'amministratore della zona.

- Ogni zona contiene **uno o più name server**: uno primario e uno (o più) secondario.
- I name server contengono i dati delle porzioni di name space dette zone.

> [!def] Zona
> **Dominio**: un nodo dell'albero DNS e tutti i suoi discendenti (gerarchia di naming). **Zona**: la porzione di quel dominio gestita dalla **stessa autorità DNS**; delegando un sottodominio si crea una nuova zona, che però resta parte del dominio padre (es. se `cs.unina.it` è delegata, diventa una zona separata restando parte del dominio `unina.it`). Dominio = gerarchia di naming; zona = autorità amministrativa.

Lo stesso albero, tagliato in modo diverso: ogni contorno è una zona, e una zona può essere un nodo o più nodi; nessun contorno attraversa mai una delega.

### Authoritative name server

- Ogni zona è servita da **uno o più authoritative name server**, che detengono i record della zona e forniscono risposte authoritative.
- Server multipli forniscono **ridondanza e disponibilità**; l'hosting DNS può essere gestito direttamente o fornito da terze parti (es. `a.nic.va` ha autorità su `vatican.va`: è lì che quei record vivono).

La gerarchia dei server autoritativi è su tre livelli:

- **Root server**: autoritativi per `.`; rispondono con i server del TLD richiesto (es. "chiedi ai server `.com`").
- **TLD server**: un insieme per ogni top-level domain, con i server dei domini registrati sotto di esso (es. "chiedi ai server `example.com`").
- **Authoritative name server**: autoritativi per le zone delegate sotto il TLD; ulteriori delegazioni possono creare livelli aggiuntivi (es. `www.example.com` → IP).

L'host normalmente interroga un **recursive resolver**, che percorre la gerarchia autoritativa per suo conto.

### Name resolution

La risoluzione dei nomi procede così:

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

- Sono il **punto di partenza** quando un resolver non ha informazioni utili in cache.
- Sono **13 identità logiche**, da `a.root-servers.net` a `m.root-servers.net`; ogni identità è implementata da molte istanze replicate distribuite nel mondo.
- Sono autoritativi per la root zone (`.`).
- Di solito **non restituiscono il record finale** per un nome di host: restituiscono un referral ai name server del **TLD** competente (`.com`, `.org`, `.edu`, …).

## Il resolver locale e i servizi aggiuntivi

> [!def] Local DNS server
> **Server DNS locale** (o resolver): tipo di server DNS che **non appartiene strettamente** alla gerarchia, tipicamente gestito dagli ISP; fa da **proxy**, inoltrando le query dell'host alla gerarchia DNS.

- Il **DNS resolver** è un recursive DNS server; gli host sono configurati per usarne uno o più, forniti dall'ISP, dalla rete locale o da un servizio pubblico.
- Quando un host si connette a un ISP, l'ISP gli fornisce gli IP di uno o più server DNS locali, tipicamente "vicini" all'host.
- Anche Google fornisce resolver pubblici (Google Public DNS) agli indirizzi `8.8.8.8` e `8.8.4.4`.

### Stub resolver

- Un host può non eseguire da solo la risoluzione DNS: uno **stub resolver** sull'host gestisce le richieste delle applicazioni e invia una **query ricorsiva** a un recursive resolver configurato.
- Il recursive resolver esegue la risoluzione effettiva e restituisce la risposta finale.
- Su alcuni sistemi, un servizio DNS locale fa da **stub/forwarder** (es. `127.0.0.53` su molti sistemi Linux).

### Caching

- Ogni risposta che un resolver riceve può essere **cachata** e usata per rispondere a query successive; il caching è ciò che fa funzionare il sistema a questa scala.
- La risposta di un recursive resolver è **non authoritative**: il resolver non è autoritativo per la zona interrogata, che la risposta venga dalla cache o sia appena risolta.
- Sono cachati anche gli **indirizzi dei TLD server**: una risoluzione parte tipicamente sotto la root.
- Non solo indirizzi (`A`/`AAAA`) vengono cachati, ma anche record `NS` e altre informazioni DNS: si evita di ripetere l'intero percorso di risoluzione.
- I record cachati sono mantenuti solo per il loro **TTL**, dopo di che vanno rinfrescati — il TTL impedisce a una copia cachata di mentire per sempre.

Un resolver non parte necessariamente dalla root: parte dal **punto più vicino già noto** della gerarchia. Ad esempio, per risolvere `www.cs.mit.edu` senza il record finale in cache:

| Informazione già in cache | La risoluzione parte da | Nuove informazioni cachabili |
|---|---|---|
| `A`/`AAAA` per `www.cs.mit.edu` | Risponde subito | — |
| `NS` per `cs.mit.edu` | Server autoritativo `cs.mit.edu` | `A`/`AAAA` finale |
| `NS` per `mit.edu` | Server autoritativo `mit.edu` | `NS` di `cs.mit.edu` + `A`/`AAAA` finale |
| `NS` per `.edu` | TLD server `.edu` | `NS` di `mit.edu`, `cs.mit.edu` + `A`/`AAAA` finale |
| Nessuna delega utile | Root server | `NS` di `.edu`, `mit.edu`, `cs.mit.edu` + `A`/`AAAA` finale |

### Servizi aggiuntivi

- **Aliasing**: associa nomi lunghi/complicati (**nomi canonicali**) a nomi più semplici (**alias**); un host con nome complicato può avere alias mnemonici (es. `relay1.west-coast.enterprise.com` → `www.enterprise.com`); l'applicazione può comunque chiedere al DNS il nome canonico di un alias insieme all'indirizzo IP.
- **Load distribution**: distribuzione del carico tra **server replicati** (*round-robin DNS*); i siti trafficati sono replicati su più server con indirizzi IP diversi (più IP associati a un solo nome canonico); il server può **ruotare l'ordine** degli indirizzi nelle risposte, così i client vengono distribuiti sulle repliche.

## Messaggi DNS

Query e risposte hanno lo **stesso formato**: un header di **12 byte** seguito da quattro sezioni.

- **Header**: un identificatore copiato nella risposta (per abbinare domande e risposte) più un insieme di flag.
- **Flag rilevanti**: *authoritative answer*, *recursion desired*, *recursion available*.
- **Question**: il nome richiesto e il tipo richiesto.
- **Answer**: i record che rispondono.
- **Authority**: server che saprebbero rispondere.
- **Additional**: record utili, tipicamente gli indirizzi dei server appena citati.

## Strumenti a riga di comando

### nslookup

- **`nslookup`** è uno strumento a riga di comando per interrogare il DNS: dato un nome di dominio recupera l'indirizzo IP e altre informazioni DNS (es. `nslookup www.example.com`).
- Permette di interrogare un server DNS specifico e di riprodurre manualmente le query iterative fatte da un recursive resolver; è possibile anche il **reverse lookup** (nome a partire dall'indirizzo).
- `nslookup` invia la query al servizio DNS locale (es. `127.0.0.53#53`), che la inoltra al resolver ricorsivo configurato; i record restituiti sono **non authoritative** (non provengono dal server che gestisce la zona), l'host emette una query ricorsiva e il resolver gestisce l'intera risoluzione con query iterative.
- Per controllare la configurazione DNS: `resolvectl status` o `cat /etc/resolv.conf`.

### dig

> [!info] dig
> **`dig`** (*Domain Information Groper*) è lo strumento a riga di comando per interrogare i server DNS e ispezionare le risposte, in un formato vicino a quello reale dei messaggi DNS: può chiedere un tipo di record specifico (`A`, `AAAA`, `NS`, `MX`, `SOA`, …), interrogare un server specifico e, con `+trace`, mostrare il percorso di delega lungo la gerarchia; `+noall +answer` mantiene solo la sezione di risposta.

Osservazioni dagli esempi con `dig`:

- Un header mostra la **ricorsione richiesta (`rd`) e disponibile (`ra`)**; l'assenza del flag `aa` indica una risposta **non authoritative**; la risposta riporta il tempo di query, il server contattato e la dimensione del messaggio.
- `www.mit.edu` risolve in una **catena di due `CNAME`** prima dell'indirizzo finale: il nome pubblicato è un alias di un altro nome, e la macchina che alla fine risponde appartiene a un soggetto del tutto diverso; i TTL mostrano l'alias tenuto per minuti e l'indirizzo finale per pochi secondi.
- L'RDATA di un record `MX` contiene due campi: un valore di **preference** e il nome del **mail server**; preference più basse hanno priorità più alta (es. `mit.edu. 65 IN MX 100 mit-edu.mail.protection.outlook.com.`).
- Una query `NS` può restituire **più record** che insieme formano un **NS RRset**; ciascun record identifica un authoritative name server della zona.
