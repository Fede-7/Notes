# Lezione 7: Il DNS

## Introduzione al DNS

Un host si può identificare in due modi: per **hostname** e per **indirizzo IP**. Le persone preferiscono il più mnemonico hostname, mentre i dispositivi di rete preferiscono gli IP, a lunghezza fissa e strutturati gerarchicamente (esempio: `www.unina.it` → `143.225.15.50`). Il **Domain Name System** (DNS) è un protocollo di livello applicazione che gestisce la traduzione da hostname a indirizzo IP. È un protocollo **client-server**: un client DNS chiede a un server DNS una specifica traduzione nome→indirizzo. I server DNS sono spesso macchine UNIX con il software *Berkeley Internet Name Domain* (BIND), **tipicamente via UDP** sulla porta 53.

Un repository (tabella) centralizzato sarebbe impossibile da gestire, a causa dell'elevato numero di host e della distanza geografica (con i relativi ritardi). Il DNS è quindi un sistema **distribuito e decentralizzato**: gerarchico, basato su domini e implementato tramite un database distribuito.

### Il resolver

Il **resolver** è il programma che restituisce l'indirizzo IP associato a un nome: interroga un server DNS locale, e tutti i messaggi scambiati sono pacchetti UDP.

## Lo spazio dei nomi DNS

Lo spazio dei nomi è una gerarchia organizzata da ICANN (*Internet Corp. for Assigned Names and Numbers*), con circa 250 domini di primo livello; ogni dominio è partizionato in sotto-domini, e così via. I domini di primo livello sono di due tipi: **generici** (aero, com, edu, ...) e **di paese** (uk, it, tv, ...), tutti gestiti da registrar nominati da ICANN. Lo spazio dei nomi è gerarchico **dalla radice verso il basso**, con parti delegate a organizzazioni diverse.

### Domini generici di primo livello

Controllati da ICANN, che nomina i registrar che li gestiscono:

| Dominio | Uso previsto | Attivo dal | Ristretto? |
| --- | --- | --- | --- |
| com | Commerciale | 1985 | No |
| edu | Istituzioni educative | 1985 | Sì |
| gov | Governo | 1985 | Sì |
| int | Organizzazioni internazionali | 1988 | Sì |
| mil | Militare | 1985 | Sì |
| net | Provider di rete | 1985 | No |
| org | Organizzazioni no-profit | 1985 | No |
| aero | Trasporto aereo | 2001 | Sì |
| biz | Aziende | 2001 | No |
| coop | Cooperative | 2001 | Sì |
| info | Informativo | 2002 | No |
| museum | Musei | 2002 | Sì |
| name | Persone | 2002 | No |
| pro | Professionisti | 2002 | Sì |
| cat | Catalano | 2005 | Sì |
| jobs | Lavoro | 2005 | Sì |
| mobi | Dispositivi mobili | 2005 | Sì |
| tel | Dati di contatto | 2005 | Sì |
| travel | Industria del viaggio | 2005 | Sì |
| xxx | Industria del sesso | 2010 | No |

## Nomi di dominio

I nomi sono cammini dal dominio verso l'alto fino alla radice (esempio: `eng.mit.edu`). I cammini **assoluti** terminano con un punto, mentre quelli **relativi** vanno interpretati. È possibile registrarsi sotto più domini di primo livello (es. `ibm.com`, `ibm.us`); il **cyber-squatting** è l'acquisto di domini solo per rivenderli poi ad aziende interessate. Ogni dominio controlla l'allocazione dei domini sottostanti, quindi creare un nuovo dominio richiede il permesso del dominio padre. Va infine notato che la nomenclatura non segue i confini fisici o geografici.

## Record di risorsa (resource records)

I campi di un record di risorsa sono:

- **Nome di dominio (NAM)**: indica il dominio cui il record si applica; è la chiave di ricerca principale per le query DNS. Normalmente esistono più record per dominio, su server diversi.
- **Time to live (TTL)**: vita del record; lungo per host stabili (es. 86400 = 1 giorno), corto per quelli volatili (es. 60 = 1 minuto). Valore massimo $2^{31}-1$, circa 68 anni.
- **Classe (CLASS)**: sempre `IN` (Internet) per i record Internet; altri codici sono raramente usati.
- **Tipo (TYPE)**: vedi sotto.
- **Valore (RDATA)**: dipende dal tipo di record; può contenere un dominio, un valore o una stringa ASCII.

### Tipi di record

- **SOA** (*Start of Authority*): informazioni sulla zona del server, contatto dell'amministratore, ecc.
- **A**: indirizzo IPv4 a 32 bit di un'interfaccia dell'host (alcuni host hanno più interfacce); equivalente **AAAA** per IPv6.
- **MX** (*Mail eXchange*): nome dell'host che accetta la posta nel dominio.
- **NS** (*Name Server*): name server del dominio, usato nella risoluzione dei nomi.
- **CNAME** (*Canonical Name*): permette alias; la lookup prosegue con il nuovo nome.
- **PTR** (*Pointer*): alias per la lookup inversa; la lookup non prosegue, restituisce il nome.

Altri tipi:

| Tipo | Significato | Valore |
| --- | --- | --- |
| SOA | Inizio di autorità | Parametri della zona |
| A | Indirizzo IPv4 di un host | Intero a 32 bit |
| AAAA | Indirizzo IPv6 di un host | Intero a 128 bit |
| MX | Mail exchange | Priorità, dominio che accetta la posta |
| NS | Name server | Nome di un server per il dominio |
| CNAME | Nome canonico | Nome di dominio |
| PTR | Puntatore | Alias di un indirizzo IP |
| SPF | Sender policy framework | Codifica testuale della policy di invio mail |
| SRV | Servizio | Host che lo fornisce |
| TXT | Testo | Testo ASCII descrittivo |

### Esempio (dati autorevoli per cs.vu.nl)

```
cs.vu.nl.    86400  IN  SOA  star boss (9527,7200,7200,241920,86400)
cs.vu.nl.    86400  IN  MX   1 zephyr
cs.vu.nl.    86400  IN  MX   2 top
cs.vu.nl.    86400  IN  NS   star

star         86400  IN  A    130.37.56.205      ; name server
zephyr       86400  IN  A    130.37.20.10       ; mail gateway
top          86400  IN  A    130.37.20.11
www          86400  IN  CNAME star.cs.vu.nl
ftp          86400  IN  CNAME zephyr.cs.vu.nl

flits        86400  IN  A    130.37.16.112
flits        86400  IN  A    192.31.231.165
flits        86400  IN  MX   1 flits
flits        86400  IN  MX   2 zephyr
flits        86400  IN  MX   3 top

rowboat      IN  A  130.37.56.201
             IN  MX 1 rowboat
             IN  MX 2 zephyr

little-sister IN  A  130.37.62.23
laserjet     IN  A  192.31.231.216
```

## Name server

Un server DNS unico e centralizzato non avrebbe senso. Lo spazio dei nomi DNS è diviso in **zone non sovrapposte**, e il partizionamento spetta all'amministratore della zona; ogni zona contiene uno o più name server, uno **primario** e uno o più **secondari**. I name server contengono i dati delle porzioni di spazio dei nomi dette **zone**.

### Risoluzione dei nomi

1. Un host interroga un name server locale.
2. Se il dominio ricade nella giurisdizione (zona) del server locale, viene restituito un record **autoritativo**.
3. Altrimenti il server locale gestisce la query **ricorsivamente**, emettendo query remote: se il server DNS ha l'indirizzo, lo restituisce; altrimenti restituisce il name server di una zona più in basso; il processo prosegue **iterativamente** fino a trovare l'indirizzo.

I **root server** sono il punto di partenza quando non si ha alcuna informazione: sono 13, da `a.root-servers.net` a `m.root-servers.net`, altamente replicati. Poiché sono molto occupati, di solito restituiscono informazioni su zone inferiori (non sui singoli record).

### Esempio: nslookup

Possiamo eseguire manualmente le query iterative fatte da un server DNS locale; è possibile anche la **lookup inversa** (nome dall'indirizzo). Il server di default (in questo caso il router) è `127.0.0.53` (porta 53). I record restituiti sono **non autoritativi** (in cache), cioè non provengono dal server DNS che gestisce la zona. Il server locale gestisce l'intera risoluzione via query iterative, mentre l'host emette una **query ricorsiva**: gli viene restituita la risposta completa oppure un errore.

```
andrea@turgia:~$ nslookup www.vatican.va
Server:  127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
www.vatican.va canonical name = wcm-disp.spc.va.
Name:    wcm-disp.spc.va
Address: 185.152.70.33
```

### Tipi di query e record

I server DNS locali gestiscono query ricorsive: è un servizio verso i propri host. Molti server DNS (i più occupati, come quelli vicini alla radice) invece non gestiscono query ricorsive. I record sono **autoritativi** o **in cache**: i record in cache scadono (si ricordi il TTL), ma il caching aiuta le prestazioni perché tutte le risposte vengono messe in cache, così l'indirizzo può essere restituito subito dal server locale. Se arriva una richiesta per `cs.mit.edu` e il server ha l'indirizzo del DNS server per `mit.edu`, può interrogare direttamente quel server; i root server sono interrogati solo in assenza di qualunque informazione su un dominio.

## Il resolver locale

C'è un altro tipo importante di server DNS: il **local DNS server** (o **DNS resolver**). Non appartiene strettamente alla gerarchia di server ed è **tipicamente gestito dagli ISP**; anche Google fornisce server simili in tutto il mondo (Google Public DNS) agli indirizzi 8.8.8.8 e 8.8.4.4. Quando un host si connette a un ISP, l'ISP fornisce gli IP di uno o più dei suoi server DNS locali (tipicamente "vicini" all'host). Quando l'host fa una query DNS, questa va al server locale, che **agisce da proxy**, inoltrandola alla gerarchia DNS.

## Alias

Il DNS fornisce un servizio di **aliasing** per server, in cui nomi complicati o lunghi (detti **canonici**) sono associati a nomi più semplici e corti (detti **alias**). Con l'**host aliasing**, host con hostname complicati possono essere associati ad alias più mnemonici (esempio: `relay1.west-coast.enterprise.com` → `www.enterprise.com`). Il DNS può essere invocato da un'applicazione **per ottenere l'hostname canonico (originale)** a partire da un alias, insieme all'indirizzo IP associato.

## Distribuzione del carico

Il DNS può essere usato per la **distribuzione del carico** tra server replicati (detto **round-robin DNS**). I siti molto trafficati (es. Google, Amazon, CNN) sono tipicamente **replicati su più server**, ognuno su un sistema finale diverso con un IP diverso (più IP associati a un solo hostname canonico). Il database DNS contiene questo insieme di IP: quando i client fanno una query per un nome mappato su un insieme di indirizzi, il server può **ruotare l'ordine** in cui gli indirizzi vengono restituiti.