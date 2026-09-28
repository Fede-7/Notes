# DNS: Domain Name System
## DNS: più di una «rubrica telefonica»

- A volte il DNS viene descritto come la «rubrica telefonica» di Internet
- In realtà il DNS è un database **distribuito e gerarchico**

## DNS: i nomi

- I nomi DNS sono una sequenza di **etichette** (label)
  - Convenzionalmente stampate separate da punti
  - La gerarchia si legge da destra verso sinistra; la specificità aumenta da destra verso sinistra
  - Le etichette non distinguono maiuscole/minuscole (case insensitive)
- Si consideri: `informatica.dieti.unina.it.`
  - L'etichetta vuota dopo il punto finale è la «radice» (root)
  - «root» → `it` → `unina` → `dieti` → `informatica`
- I nomi DNS sono talvolta chiamati informalmente *hostname*
  - Possono non corrispondere a un host, ma a un servizio, a un punto di delega, a una policy di instradamento della posta, o semplicemente a un nodo del database DNS distribuito
  - Inoltre, lo stesso host può avere nomi DNS diversi
  
## Domini, zone e delega

- Un **dominio** è una parte dello spazio dei nomi (namespace)
  - Un nodo e il sottoalbero che vi è radicato
- Tutti i domini di primo livello e molti domini di secondo livello e inferiori sono suddivisi, tramite **delega**, in unità più piccole e gestibili
- Queste unità più piccole si chiamano **zone**
- Ogni zona è servita da uno o più **name server autoritativi**
  - I name server memorizzano e forniscono le informazioni DNS per le zone
  - Possono esistere più name server autoritativi per ridondanza
  - L'autorità di un name server termina in corrispondenza di zone figlie delegate
  - Un name server può essere autoritativo per molte zone

### Dominio vs Zona

Dominio e zona sono concetti diversi:

- Il **dominio** è un concetto **strutturale** (un sottoalbero del namespace)
- La **zona** è un concetto **amministrativo** (la parte del namespace per la quale un'autorità pubblica dati)
- È la delega a renderli diversi!

Se **unina.it.** delega **dieti.unina.it.** al DIETI:

- **dieti.unina.it.** smette di far parte del dominio **unina.it.**? **No.** Fa ancora parte del sottoalbero radicato in `unina.it.`
- **dieti.unina.it.** smette di far parte della zona **unina.it.**? **Sì.** L'autorità è stata delegata!

> *I domini descrivono l'albero. Le zone descrivono la responsabilità amministrativa su parti dell'albero.*

## DNS: tipi di record

Il DNS memorizza le informazioni come **Resource Record** (RR):

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| informatica.dieti.unina.it. | 21600 | IN | A | 143.225.97.81 |

- **Owner name**: il nome DNS descritto dal record
- **TTL**: time-to-live, ovvero per quanto tempo la risposta può essere conservata in cache (in secondi)
- **Class**: normalmente «IN», ovvero Internet
- **Type**: il tipo di informazione contenuta nel record
- **Value**: il dato associato al nome

### Principali tipi di record DNS

| Tipo  | Scopo                           |
| ----- | ------------------------------- |
| A     | Da nome a indirizzo IPv4        |
| AAAA  | Da nome a indirizzo IPv6        |
| CNAME | Alias verso un nome canonico    |
| NS    | Server autoritativi di una zona |
| SOA   | Identifica una zona             |
| MX    | Server di posta per un dominio  |

## DNS: gli attori

Come fanno i browser (o i client in generale) a passare da un nome DNS a un indirizzo IP? Nel processo sono coinvolti diversi attori:

- Il **client** chiede a un'interfaccia locale di risoluzione (**stub resolver**), gestita a livello di sistema operativo, un record di un certo tipo (es. A) per un dato nome
- Lo stub resolver delega la risoluzione a un **resolver ricorsivo**
  - Tipicamente gestito da ISP o provider pubblici (Google – 8.8.8.8, Cloudflare – 1.1.1.1, …)
- Il resolver ricorsivo naviga la **gerarchia autoritativa** cercando il record
  - Ciò può richiedere il «dialogo» con più server DNS
- Il resolver ricorsivo restituisce il record oppure un errore

## Query ricorsive vs iterative

- **Query ricorsive**: «Trova la risposta definitiva per me»
  - Dal client → al resolver ricorsivo
  - Il resolver svolge tutto il lavoro
  - Nella ricorsione, il server interpellato è responsabile di ottenere il risultato
- **Query iterative**: «Dammi la migliore informazione che hai»
  - Dal resolver ricorsivo → ai server DNS
  - Ogni server può restituire una risposta o un referral
  - Nell'iterazione, il resolver segue i referral e decide quale sia la query successiva

## Interazioni DNS: query e risposte

Un'interazione DNS consiste normalmente di due messaggi:

- **Question** (domanda)
  - Es. `informatica.dieti.unina.it. IN A`
- **Response** (risposta)
  - *Header*: stato e flag
  - *Question*: riportata dalla query (echo)
  - *Answer*: record che rispondono alla domanda
  - *Authority*: dati autoritativi o referral
  - *Additional*: record di supporto utili

Le domande contengono tre campi principali:

- **NAME** (il nome richiesto)
- **CLASS** (normalmente IN per Internet — talvolta omessa)
- **TYPE** (il tipo di record richiesto)

## Risposte DNS

Gli header delle risposte DNS iniziano con un **codice di stato**. I possibili codici includono:

| Stato | Significato |
| --- | --- |
| **NOERROR** | Il server ha elaborato la query con successo |
| **NXDOMAIN** | Il nome richiesto non esiste |
| **SERVFAIL** | Il server non è riuscito a completare la query |
| **REFUSED** | Il server ha rifiutato di eseguire l'operazione richiesta |
| **FORMERR** | Il messaggio di query era malformato |

### Risposte NOERROR

- **NOERROR** non significa necessariamente che il record sia stato trovato
- Significa che il server DNS ha capito ed elaborato la query
- Sono possibili scenari diversi:
  - **Risposta positiva.** Il blocco Answer contiene il record richiesto
  - **Referral.** Il blocco Authority contiene record **NS** di una zona che potrebbe sapere di più
  - **NODATA.** La risposta può confermare che il nome esiste, ma non esiste alcun record del tipo richiesto (blocco Answer vuoto)

## Esempio di risoluzione: cold-cache

Il client vuole ottenere un record A per `squids.unina.it.`:

1. Il client chiede allo stub resolver
2. Lo stub resolver invia una query DNS al resolver ricorsivo
3. Il resolver ricorsivo interroga la root → riceve un referral verso `.it`
4. Il resolver ricorsivo interroga `.it` → riceve un referral verso `unina.it`
5. Il resolver ricorsivo interroga `unina.it` → riceve il record A
6. Il resolver ricorsivo risponde allo stub resolver

### La cache nella risoluzione DNS

- Nello scenario precedente il resolver ricorsivo ha navigato l'intera gerarchia
- Nel mondo reale, i sistemi memorizzano i dati in una cache per efficienza
  - Questo vale per browser, stub resolver, resolver ricorsivi, …
- Se un record è già in cache (e non è scaduto), non serve alcuna navigazione!
- Lo scenario in cui nessun dato in cache è disponibile durante la risoluzione è lo scenario peggiore
  - Chiamato anche **risoluzione cold-cache**
- Il **TTL** determina per quanto tempo un record in cache può essere usato

## Pratica

> [!NOTE]
> 
> 
> - Con **dig**, analizziamo query e risposte DNS; l'opzione **+trace** mostra la risoluzione gerarchica completa, senza cache, dai root server fino ai server autoritativi:
> 
> ```terminal
> luigi@XPS-9520:/$ dig @8.8.8.8 squids.unina.it. +trace
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
> - Se invece il nome **esiste ma non ha record A**, la risposta è **NODATA** (status NOERROR, nessuna sezione ANSWER) — è il caso di `docenti.unina.it` rispetto a `www.docenti.unina.it`, che sono **nomi diversi**: solo il primo ha un record A, quindi il secondo restituisce «Server Not Found»:
> 
> ```bash
> $ dig www.docenti.unina.it A     → NOERROR, A 143.225.212.48
> $ dig docenti.unina.it A         → NOERROR, nessuna ANSWER SECTION
> ```
> 
> > Nota: il DNS è usato anche per ottenere l'IP (record A) del NS selezionato, se la risposta intermedia non lo contiene già nella sezione additional!