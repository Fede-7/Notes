# DNS: Domain Name System

> **Web Technologies — Lecture 02**
> Università degli Studi di Napoli Federico II
> Luigi Libero Lucio Starace, Ph.D. — luigiliberolucio.starace@unina.it
> https://www.squids.unina.it · https://luistar.github.io · https://www.docenti.unina.it/luigiliberolucio.starace

---

## In precedenza, su Web Technologies

Abbiamo discusso come l'inserimento di un URL nel browser avvii una **catena di lavoro**. Oggi ci concentriamo sul primo passo di questa catena: il **Domain Name System (DNS)**.

---

## DNS: più di una «rubrica telefonica»

- A volte il DNS viene descritto come la «rubrica telefonica» di Internet
- In realtà il DNS è un database **distribuito e gerarchico**

---

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

### Esempi di nomi e gerarchia

Rappresentazione gerarchica dei seguenti nomi DNS:

- `ansa.it.`
- `informatica.dieti.unina.it.`
- `squids.unina.it.`
- `mozilla.org.`
- `w3.org.`

---

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

---

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

| Tipo | Scopo |
| --- | --- |
| A | Da nome a indirizzo IPv4 |
| AAAA | Da nome a indirizzo IPv6 |
| CNAME | Alias verso un nome canonico |
| NS | Server autoritativi di una zona |
| SOA | Identifica una zona |
| MX | Server di posta per un dominio |

### Record A/AAAA

- I record A e AAAA associano un nome DNS a un indirizzo IPv4/IPv6
- Un nome può avere entrambi i tipi, e più record dello stesso tipo
  - Più record dello stesso tipo sono usati per il bilanciamento del carico (load balancing)
  - I client possono usare uno qualunque degli indirizzi forniti e provarne altri in caso di fallimento di quello scelto
- Ad esempio, `www.google.com.` ha molti record A e AAAA:

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| www.google.com. | 286 | IN | A | 142.251.27.100 |
| www.google.com. | 286 | IN | A | 142.251.27.101 |
| www.google.com. | 170 | IN | AAAA | 2a00:1450:4025:1803::8b |
| www.google.com. | 170 | IN | AAAA | 2a00:1450:4025:1803::71 |

### Record CNAME

- Un record CNAME indica che un nome è un **alias** di un altro nome
- Ad esempio, se `www.squids.unina.it.` è un CNAME verso `squids.unina.it.`, il client deve ottenere i record di indirizzo per `squids.unina.it.`
- Un CNAME punta a un altro nome DNS, non direttamente a un indirizzo IP

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| www.squids.unina.it. | 1800 | IN | CNAME | squids.unina.it. |

### Record NS

- I record NS identificano i name server autoritativi di una zona
- In una zona padre, i record NS possono anche creare la delega verso una zona figlia
- Di seguito, i record NS per `unina.it.`:

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| unina.it. | 1753 | IN | NS | dscna1.unina.it |
| unina.it. | 1753 | IN | NS | dscna2.unina.it |

### Record SOA

- I record SOA (Start Of Authority) identificano l'inizio (apex) di una zona
- Contengono metadati amministrativi:
  - Server primario, numeri seriali, valori temporali
- Ogni zona ha **esattamente un** record SOA
- Esempi di record SOA per `unina.it.` e `dieti.unina.it.`:

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| unina.it. | 3600 | IN | SOA | dscna2.unina.it. empty.empty. 29085 3600 600 1209600 3600 |
| dieti.unina.it. | 3600 | IN | SOA | dscna1.unina.it. empty.empty. 114 3600 600 1209600 3600 |

### Record MX

- I record MX identificano il server che accetta e-mail per un dominio
- Esempi di record MX per `unina.it.`:

| Owner name | TTL | Class | Type | Value |
| --- | --- | --- | --- | --- |
| unina.it. | 3600 | IN | MX | 20 fmvip.unina.it. |
| unina.it. | 3600 | IN | MX | 10 unina-it.mail.protection.outlook.com. |

- Il numero è una preferenza: i valori più bassi vengono provati per primi
- I record MX puntano a un nome di server
  - L'indirizzo IP dovrà essere risolto a sua volta (acquisendo il record A/AAAA)

---

## DNS: gli attori

Come fanno i browser (o i client in generale) a passare da un nome DNS a un indirizzo IP? Nel processo sono coinvolti diversi attori:

- Il **client** chiede a un'interfaccia locale di risoluzione (**stub resolver**), gestita a livello di sistema operativo, un record di un certo tipo (es. A) per un dato nome
- Lo stub resolver delega la risoluzione a un **resolver ricorsivo**
  - Tipicamente gestito da ISP o provider pubblici (Google – 8.8.8.8, Cloudflare – 1.1.1.1, …)
- Il resolver ricorsivo naviga la **gerarchia autoritativa** cercando il record
  - Ciò può richiedere il «dialogo» con più server DNS
- Il resolver ricorsivo restituisce il record oppure un errore

---

## Query ricorsive vs iterative

- **Query ricorsive**: «Trova la risposta definitiva per me»
  - Dal client → al resolver ricorsivo
  - Il resolver svolge tutto il lavoro
  - Nella ricorsione, il server interpellato è responsabile di ottenere il risultato
- **Query iterative**: «Dammi la migliore informazione che hai»
  - Dal resolver ricorsivo → ai server DNS
  - Ogni server può restituire una risposta o un referral
  - Nell'iterazione, il resolver segue i referral e decide quale sia la query successiva

---

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

---

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

---

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

---

## La risoluzione DNS in pratica

- Vediamo la risoluzione DNS in pratica con il tool **dig**
  - Strumento potente per analizzare query e risposte DNS
  - Installabile su Linux/WSL (`apt install bind9-dnsutils`)
  - L'opzione **+trace** mostra la risoluzione gerarchica completa (senza cache) dai root server fino ai server autoritativi
- Il comando per la risoluzione completa di `squids.unina.it.` partendo dal server DNS di Google 8.8.8.8:

```bash
luigi@XPS-9520:/$ dig @8.8.8.8 squids.unina.it. +trace
```

### Tracciamento con dig: dai root ai TLD

Il DNS di Google ci rimanda ai name server della radice:

```text
.                    87203   IN      NS      i.root-servers.net.
.                    87203   IN      NS      b.root-servers.net.
.                    87203   IN      NS      a.root-servers.net.
.                    87203   IN      NS      k.root-servers.net.
.                    87203   IN      NS      c.root-servers.net.
.                    87203   IN      NS      e.root-servers.net.
.                    87203   IN      NS      g.root-servers.net.
.                    87203   IN      NS      f.root-servers.net.
.                    87203   IN      NS      m.root-servers.net.
.                    87203   IN      NS      l.root-servers.net.
.                    87203   IN      NS      h.root-servers.net.
.                    87203   IN      NS      j.root-servers.net.
.                    87203   IN      NS      d.root-servers.net.
;; Received 239 bytes from 8.8.8.8#53(8.8.8.8) in 32 ms
```

Il root name server selezionato (`h.root-servers.net`) ci rimanda ai name server responsabili del TLD `.it`:

```text
it.                  172800 IN    NS    a.dns.it.
it.                  172800 IN    NS    m.dns.it.
it.                  172800 IN    NS    r.dns.it.
it.                  172800 IN    NS    v.dns.it.
it.                  172800 IN    NS    dns.nic.it.
it.                  172800 IN    NS    nameserver.cnr.it.
;; Received 427 bytes from 198.97.190.53#53(h.root-servers.net) in 31 ms
```

Il name server `.it` selezionato (`m.dns.it`) ci rimanda ai name server responsabili del dominio di secondo livello `unina.it`, e il name server di `unina.it` (`dscna2.unina.it`) restituisce il record A richiesto:

```text
unina.it.             3600    IN    NS    dscna1.unina.it.
unina.it.             3600    IN    NS    dscna2.unina.it.
;; Received 146 bytes from 217.29.76.4#53(m.dns.it) in 23 ms

squids.unina.it.    1800    IN    A    143.225.131.206
;; Received 88 bytes from 192.133.28.107#53(dscna2.unina.it) in 19 ms
```

> Nota: il DNS è usato anche per ottenere l'IP (record A) del NS selezionato, se la risposta intermedia non lo contiene già nella sezione additional!

---

## Risoluzione DNS: troubleshooting

Cosa succede se proviamo a risolvere un nome che non esiste (es. `webtechnologies.unina.it.`)?

```text
luigi@XPS-9520:/$ dig webtechnologies.unina.it A

; <<>> DiG 9.20.18-1ubuntu2-Ubuntu <<>>
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN

;; QUESTION SECTION:
;webtechnologies.unina.it.        IN      A

;; AUTHORITY SECTION:
unina.it. 3600 IN SOA dscna2.u...
```

Il browser mostra l'errore «Server Not Found» (Firefox non riesce a connettersi al server `webtechnologies.unina.it`).

### Caso di studio: docenti.unina

- Se visitate `www.docenti.unina.it` ottenete la piattaforma che tutti conosciamo
- Se visitate `docenti.unina.it` ottenete un errore «Server Not Found»…
- Perché? `www.docenti.unina.it.` e `docenti.unina.it.` sono **nomi diversi**!
  - Esiste un record A per il primo, ma non per il secondo…

```text
luigi@XPS-9520:/$ dig www.docenti.unina.it A
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
;; QUESTION SECTION:
;www.docenti.unina.it.          IN   A
;; ANSWER SECTION:
www.docenti.unina.it.  73806   IN   A   143.225.212.48

luigi@XPS-9520:/$ dig docenti.unina.it A
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
;; QUESTION SECTION:
;docenti.unina.it.          IN   A
```

→ Risposta **NODATA**: il nome esiste, ma non c'è alcun record A!