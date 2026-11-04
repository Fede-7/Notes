# Lezione 1 DNS: Domain Name System

> [!def] DNS  
> **Database distribuito e gerarchico** di Internet, talvolta descritto in modo improprio come la «rubrica telefonica» della rete. Memorizza e fornisce le informazioni associate ai nomi.

## I nomi

Un nome DNS è una sequenza gerarchica di etichette, lette da destra verso sinistra.

- **Etichetta (label)**: componente elementare del nome; convenzionalmente le etichette sono stampate separate da punti.
- La **gerarchia** si legge da destra verso sinistra: la specificità del nome aumenta da destra verso sinistra.
- Le etichette sono **case insensitive**: non distinguono maiuscole e minuscole.
- **Root**: l'etichetta vuota dopo il punto finale del nome, che rappresenta la radice del namespace.

Nel nome `informatica.dieti.unina.it.` la gerarchia si legge: root → `it` → `unina` → `dieti` → `informatica`.

I nomi DNS sono talvolta chiamati informalmente *hostname*, ma in realtà:

- Un nome può non corrispondere a un host, bensì a un servizio, a un punto di delega, a una policy di instradamento della posta o semplicemente a un nodo del database DNS distribuito.
- Lo stesso host può avere nomi DNS diversi.

## Domini, zone e delega

> [!def] Dominio  
> **Parte dello spazio dei nomi (namespace)**: un nodo dell'albero e il sottoalbero che vi è radicato.

- **Delega**: suddivisione di un dominio in unità più piccole e gestibili, tramite l'assegnazione dell'autorità su di esse.
- **Zona**: unità più piccola risultante dalla delega.
- Ogni zona è servita da uno o più **name server autoritativi**, che memorizzano e forniscono le informazioni DNS della zona.
- Possono esistere più name server autoritativi per la stessa zona, per ridondanza.
- L'autorità di un name server termina in corrispondenza delle zone figlie delegate.
- Un name server può essere autoritativo per molte zone.

### Dominio vs Zona

Dominio e zona sono concetti diversi, ed è la delega a renderli tali.

- Il **dominio** è un concetto **strutturale**: un sottoalbero del namespace.
- La **zona** è un concetto **amministrativo**: la parte del namespace per la quale un'autorità pubblica dati.

Se `unina.it.` delega `dieti.unina.it.` al DIETI, `dieti.unina.it.` smette di far parte della zona `unina.it.` perché l'autorità è stata delegata, ma continua a far parte del dominio `unina.it.` perché resta nel sottoalbero radicato in `unina.it.`.

> I domini descrivono l'albero. Le zone descrivono la responsabilità amministrativa su parti dell'albero.

## Tipi di record

Il DNS memorizza le informazioni come **Resource Record** (RR), descritti dai seguenti campi.


| Owner name                    | TTL   | Class | Type | Value           |
| ----------------------------- | ----- | ----- | ---- | --------------- |
| `informatica.dieti.unina.it.` | 21600 | `IN`  | `A`  | `143.225.97.81` |


- **Owner name**: il nome DNS descritto dal record.
- **TTL** (*time-to-live*): per quanto tempo, in secondi, la risposta può essere conservata in cache.
- **Class**: normalmente `IN`, ovvero Internet.
- **Type**: il tipo di informazione contenuta nel record.
- **Value**: il dato associato al nome.

### Principali tipi di record DNS


| Tipo    | Scopo                           |
| ------- | ------------------------------- |
| `A`     | Da nome a indirizzo IPv4        |
| `AAAA`  | Da nome a indirizzo IPv6        |
| `CNAME` | Alias verso un nome canonico    |
| `NS`    | Server autoritativi di una zona |
| `SOA`   | Identifica una zona             |
| `MX`    | Server di posta per un dominio  |


## Gli attori

Nel passaggio da un nome DNS a un indirizzo IP sono coinvolti diversi attori.

- **Client**: chiede un record di un certo tipo per un dato nome a un'interfaccia locale di risoluzione.
- **Stub resolver**: interfaccia locale di risoluzione gestita a livello di sistema operativo, che riceve la richiesta del client e la delega al resolver ricorsivo.
- **Resolver ricorsivo**: tipicamente gestito da ISP o provider pubblici (Google `8.8.8.8`, Cloudflare `1.1.1.1`); naviga la **gerarchia autoritativa** cercando il record, il che può richiedere il dialogo con più server DNS.
- Il resolver ricorsivo restituisce il record oppure un errore.

## Query ricorsive vs iterative

- **Query ricorsiva**: chiede al server di trovare la risposta definitiva; il server interpellato è responsabile di ottenere il risultato e svolge tutto il lavoro.
- **Query iterativa**: chiede al server la migliore informazione che ha; ogni server può restituire una risposta o un referral, e il resolver segue i referral decidendo quale sia la query successiva.
- La query ricorsiva è usata dal client verso il resolver ricorsivo; la query iterativa è usata dal resolver ricorsivo verso i server DNS.

## Interazioni DNS: query e risposte

Un'interazione DNS consiste normalmente di due messaggi: una **question** e una **response**.

- **Question**: la domanda, es. `informatica.dieti.unina.it. IN A`.
- **Response**: la risposta, articolata in sezioni.

Le sezioni della response sono:

- **Header**: stato e flag.
- **Question**: la domanda, riportata dalla query (echo).
- **Answer**: i record che rispondono alla domanda.
- **Authority**: dati autoritativi o referral.
- **Additional**: record di supporto utili.

Le question contengono tre campi principali: **NAME** (il nome richiesto), **CLASS** (normalmente `IN` per Internet, talvolta omessa) e **TYPE** (il tipo di record richiesto).

## Risposte DNS

Gli header delle risposte DNS iniziano con un **codice di stato**. I principali codici sono:


| Stato      | Significato                                               |
| ---------- | --------------------------------------------------------- |
| `NOERROR`  | Il server ha elaborato la query con successo              |
| `NXDOMAIN` | Il nome richiesto non esiste                              |
| `SERVFAIL` | Il server non è riuscito a completare la query            |
| `REFUSED`  | Il server ha rifiutato di eseguire l'operazione richiesta |
| `FORMERR`  | Il messaggio di query era malformato                      |


### Risposte NOERROR

`NOERROR` significa che il server ha capito ed elaborato la query, ma non implica che il record sia stato trovato. Gli scenari possibili sono:

- **Risposta positiva**: il blocco Answer contiene il record richiesto.
- **Referral**: il blocco Authority contiene record `NS` di una zona che potrebbe sapere di più.
- **NODATA**: il nome esiste ma non esiste alcun record del tipo richiesto; il blocco Answer è vuoto.

## Esempio di risoluzione: cold-cache

> [!example] 
> Nella risoluzione di un record `A` per `squids.unina.it.` con nessun dato in cache, il processo attraversa tutta la gerarchia.
> 
> 1. Il client chiede allo stub resolver.
> 2. Lo stub resolver invia una query DNS al resolver ricorsivo.
> 3. Il resolver ricorsivo interroga la root e riceve un referral verso `.it`.
> 4. Il resolver ricorsivo interroga `.it` e riceve un referral verso `unina.it`.
> 5. Il resolver ricorsivo interroga `unina.it` e riceve il record `A`.
> 6. Il resolver ricorsivo risponde allo stub resolver.
> 

### La cache nella risoluzione DNS

- Nel mondo reale, browser, stub resolver e resolver ricorsivi memorizzano i dati in una cache per efficienza.
- Se un record è già in cache e non è scaduto, non serve alcuna navigazione della gerarchia.
- **Risoluzione cold-cache**: lo scenario peggiore, in cui nessun dato in cache è disponibile durante la risoluzione.
- Il **TTL** determina per quanto tempo un record in cache può essere usato.

## Pratica

> [!Lab]
> 
> 
> - Con **dig**, analizziamo query e risposte DNS; l'opzione **+trace** mostra la risoluzione gerarchica completa, senza cache, dai root server fino ai server autoritativi:
> 
> ```bash
> $ dig @8.8.8.8 squids.unina.it. +trace
> ```
> 
> - Ogni livello rimanda ai name server del livello successivo: il DNS di Google elenca i root server, il root server selezionato rimanda ai name server del TLD `.it`, questi a quelli di `unina.it`, e infine il name server autoritativo (`dscna2.unina.it`) restituisce il record A:
> 
> ```bash
> .                    87203   IN      NS      h.root-servers.net.
> it.                  172800  IN      NS      m.dns.it.
> unina.it.            3600    IN      NS      dscna2.unina.it.
> squids.unina.it.     1800    IN      A       143.225.131.206
> ```
> 
> - Se il nome **non esiste** (es. `webtechnologies.unina.it.`), la risposta ha status **NXDOMAIN** e il browser mostra «Server Not Found»:
> 
> ```bash
> ;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN
> ;webtechnologies.unina.it.        IN      A
> ```
> 
> - Se invece il nome **esiste ma non ha record A**, la risposta è **NODATA** (status NOERROR, nessuna sezione ANSWER), è il caso di `docenti.unina.it` rispetto a `www.docenti.unina.it`, che sono **nomi diversi**: solo il primo ha un record A, quindi il secondo restituisce «Server Not Found»:
> 
> ```bash
> $ dig www.docenti.unina.it A     → NOERROR, A 143.225.212.48
> $ dig docenti.unina.it A         → NOERROR, nessuna ANSWER SECTION
> ```
> 
> > Nota: il DNS è usato anche per ottenere l'IP (record A) del NS selezionato, se la risposta intermedia non lo contiene già nella sezione additional!
