# Lezione 20 Network Layer

Materiale di studio, solo teoria tratta dal set di slide "Lecture 20".

## Dal livello di trasporto al livello di rete

- **Compito del livello di rete**: permettere la comunicazione tra host remoti.
- **All'host mittente**: prelevare i segmenti dal livello di trasporto, incapsularli ciascuno in un datagramma e inviarli nella rete.
- **All'host ricevente**: ricevere i datagrammi dalla rete, estrarre i segmenti del livello di trasporto e consegnarli al livello di trasporto.

A questo livello operano alcuni dei più importanti protocolli delle reti di calcolatori, come **IP** e **DHCP**; esistono inoltre dispositivi specializzati, i **router**, che operano a questo livello. All'interno della rete vi sono nodi che inoltrano i datagrammi ai nodi adiacenti (i router) fino all'host di destinazione. I router non eseguono applicazioni né protocolli del livello di trasporto, per cui il loro stack è mostrato troncato. L'atto di un datagramma ridirezionato da un router è detto anche **hop**.

## Servizi e best-effort

> [!def] Best-effort service
> **Modello di servizio** della rete Internet in cui la rete fa del suo meglio per consegnare un pacchetto dalla sorgente alla destinazione, senza alcuna garanzia: i pacchetti non sono garantiti né nell'ordine né nella ricezione stessa, e non esistono garanzie su ritardi o banda minima.

Quali servizi potrebbero teoricamente accompagnare la consegna:

- **Consegna garantita**: un pacchetto inviato da un host sorgente arriva comunque all'host destinazione.
- **Consegna garantita con ritardo limitato**: i pacchetti arrivano entro un limite massimo di ritardo host a host (per esempio entro 100 ms).
- **Consegna dei pacchetti in ordine**: i pacchetti arrivano a destinazione nell'ordine in cui sono stati inviati.
- **Banda minima garantita**: si specifica una velocità minima (per esempio 1 Mbps); se la velocità del mittente è al suo interno, tutti i pacchetti sono finalmente consegnati.
- **Sicurezza**: cifratura/decifratura di tutti i datagrammi alla sorgente/destinazione.

In realtà nessuno di questi servizi è generalmente offerto dalle reti: il livello di rete di Internet fornisce un solo servizio, il best-effort. La consegna host a host, incarnata in questo modello, è comunque adeguata in combinazione con una buona banda: applicazioni come Netflix e la voce-video su IP lavorano con esso.

## Funzioni del livello di rete nei router

> [!def] Forwarding e Routing
> **Forwarding**: azione locale al router di spostare un pacchetto dalla interfaccia di ingresso appropriata a quella di uscita. **Routing**: processo esteso all'intera rete che determina i cammini end-to-end seguiti dai pacchetti.

- **Forwarding**: quando un pacchetto arriva su un collegamento di ingresso, il router deve spostarlo verso il collegamento di uscita appropriato; è possível anche bloccare un pacchetto (ad esempio se proviene da un host noto come malevolo), scartare un pacchetto scaduto, duplicarlo su più collegamenti in uscita, o modificarne la segnalazione di congestione.
- **Routing**: decide la rotta o cammino seguito dai pacchetti dal mittente al ricevitore; gli algoritmi che calcolano questi cammini sono detti **routing algorithms**.

I due compiti operano su scale temporali distanti un miliardo di volte, e per questo hanno nomi separati: il **data plane** fa il forwarding in alcuni nanosecondi ed è implementato in hardware; il **control plane** fa il routing in secondi ed è implementato in software. Tra i due sta un'unica struttura dati, la **forwarding table**: il control plane la scrive, il data plane la legge una volta per pacchetto. Di conseguenza un router inoltra senza conoscere il cammino: sa solo quale dei propri collegamenti è il prossimo.

### Forwarding table

La **forwarding table** è una tabella che associa interfacce di uscita a possibili indirizzi di destinazione. Un router inoltra un pacchetto esaminando il valore di uno o più campi dell'intestazione, che usa per indicizzare la tabella; il valore in ingresso nell'elemento della tabella indica l'interfaccia di uscita a cui reindirizzare il pacchetto.

Tradizionalmente la tabella è calcolata nel router da un algoritmo di routing che dialoga con quelli degli altri router: i router si scambiano messaggi di routing e ciascuno ricalcola la propria tabella locale, ma nessuno possiede l'immagine completa. Il contenuto della tabella si determina raccogliendo informazioni da router diversi: si usano una o più **routing table** (control plane) che portano alla creazione della forwarding table (data plane) in due modi:

- **Decentralizzato (o distribuito)**: ogni router ha un componente di routing che comunica con i componenti di routing degli altri router; è stato l'approccio dominante.
- **Centralizzato**: un controller remoto fisicamente separato dai router calcola e distribuisce le forwarding table da usare.

Nel caso centralizzato il controller può risiedere in un data center remoto, con alta affidabilità e ridondanza, gestito dall'ISP o da terzi. Questo approccio è alla base del **software-defined networking (SDN)**: la rete è "software-defined" perché il controller che calcola le forwarding table e dialoga con i router è un software centralizzato, e le regole di forwarding sono decise da un controller programmabile anziché calcolate autonomamente in ogni router.

## Componenti principali di un router

I componenti principali di un router (diversi dalle porte del livello di trasporto) sono:

- **Porte di ingresso (input ports)**: interfacce fisiche in ingresso che operano con il livello di collegamento sottostante del collegamento collegato; eseguono funzioni fisiche e di link layer, consultano la forwarding table e inoltrano i pacchetti di controllo al processore di routing.
- **Switching fabric**: collegano le porte di ingresso alle porte di uscita.
- **Porte di uscita (output ports)**: salvano i pacchetti ricevuti dalla matrice di commutazione e li trasmettono sul collegamento in uscita eseguendo le funzioni di link layer e fisica necessarie; le porte possono essere bidirezionali (input/output accoppiati).
- **Routing processor**: esegue i protocolli di instradamento, mantiene le informazioni di stato sui collegamenti e calcola/aggiorna la forwarding table.

Il numero di porte dipende fortemente dal tipo di router: da poche porte nei router domestici a decine o centinaia nei router di fascia alta per ISP. Nei router ad alte prestazioni la commutazione dei pacchetti è tipicamente implementata in hardware dedicato; nei router più piccoli può avvenire anche in software.

### Porte di ingresso: funzioni

- **Elaborazione fisica e a livello di collegamento**: ricevono i bit dal collegamento fisico, elaborano i frame in ingresso ed estraggono i pacchetti IP.
- **Lookup sulla forwarding table**: esaminano l'indirizzo IP di destinazione e determinano la porta di uscita appropriata.
- **Pacchetti di controllo**: consegnano al routing processor i messaggi dei protocolli di instradamento destinati al router.
- **Elaborazione dell'intestazione IP**: eseguono controlli e aggiornamenti basilari sull'intestazione IP prima dell'invio.
- **Forwarding distribuito**: nei router ad alte prestazioni le forwarding table sono replicate nelle schede di linea di ingresso, consentendo la ricerca dei pacchetti senza coinvolgere la CPU centrale.

### Perché il forwarding veloce richiede l'hardware

Su collegamento di 100 Gbps, un datagramma di 64 byte lascia 5,12 ns prima dell'arrivo del successivo: $64 \cdot 8 / (100 \cdot 10^9)$. Un router può avere più porte di ingresso operative contemporaneamente, richiedendo all'hardware di elaborare i pacchetti a una frequenza aggregata molto alta. Nessun software arriva vicino a queste cifre, per cui porte di ingresso, di uscita e matrice di commutazione sono tutte hardware; il routing processor sta all'estremo opposto della scala (millisecondi e secondi) e può essere una CPU qualunque con codice ordinario.

### Tipi di router

- **Domestici e piccoli uffici**: hanno poche porte e collegano reti locali a un Internet Service Provider (ISP).
- **Edge router**: operano al confine di una rete, collegandola ad altre reti (ad esempio una rete ISP ai propri clienti o ad altri provider).
- **Core router**: operano all'interno di grandi reti di backbone, inoltrando grandi volumi di traffico tra varie parti della rete.
- **Scalabilità**: router di fascia alta possono supportare centinaia di interfacce ad alta velocità (per esempio il Juniper MX2020 arriva a 800 porte 100 GbE e una capacità di sistema di 80 Tbps).

## Forwarding: prefissi e longest prefix matching

Il ruolo della forwarding table è associare indirizzi IP di destinazione (prefissi) a porte di uscita, consentendo l'invio dei pacchetti verso la destinazione. Un indirizzo **IPv4** è un numero di 4 byte (32 bit) visto di solito in notazione decimale a puntini (`192.168.1.1`) ma anche in forma binaria: `11000000 10101000 00000001 00000001`.

**Problema**: conservare un elemento per ogni possibile indirizzo IPv4 destinazione richiederebbe fino a $2^{32}$ elementi (oltre 4 mila miliardi). **Soluzione**: al posto dei singoli indirizzi si usano **prefissi IP**, che identificano gruppi di indirizzi con gli stessi bit iniziali; ogni elemento della tabella associa un prefisso a un'interfaccia di uscita.

Ogni riga fissa i primi bit e lascia liberi gli altri: la parte fissa dà il nome al gruppo, la parte libera il nome all'host al suo interno. Per esempio, una riga che fissa 21 bit lascia 11 bit liberi, che danno $2^{11} = 2048$ indirizzi, da tutti zero a tutti uno: una riga è un intervallo, e quattro righe sostituiscono quattro miliardi. L'ultima riga della tabella è la **default**: ciò che non ha avuto corrispondenza con nulla deve comunque uscire da qualche parte.

Esempio di tabella a 4 porte:

| Prefisso degli indirizzi IP | Interfaccia |
|---|---|
| `11001000 00010111 00010*** *******` | 0 |
| `11001000 00010111 00011000 *******` | 1 |
| `11001000 00010111 00011*** *******` | 2 |
| otherwise | 3 |

> [!def] Longest prefix matching
> **Regola** usata quando gli elementi della forwarding table non sono mutuamente esclusivi, cioè quando un indirizzo corrisponde a più prefissi: il pacchetto è inoltrato verso l'elemento con la corrispondenza più lunga.

Ad esempio, l'indirizzo `11001000 00010111 00011000 10101010` corrisponde sia alla riga 1 (24 bit) sia alla riga 2 (21 bit): vince la corrispondenza a 24 bit, così il pacchetto va all'interfaccia 1.

L'operazione di **lookup** è svolta quando un pacchetto arriva sul collegamento verso una porta di ingresso ed è eseguita tipicamente in hardware, per essere il più rapida possibile (per esempio in nanosecondi per trasmissioni Gigabit), con memorie dedicate e algoritmi avanzati di ricerca in tabella. Nei router ad alte prestazioni ogni porta ha una copia della forwarding table ricevuta dal routing processor su un bus dedicato (per esempio un bus PCI), per evitare il collo di bottiglia di invocare il routing processor centralizzato pacchetto per pacchetto. Più indirizzi possono essere associati alla stessa porta.

> [!info] Match-plus-action
> **Schema** della duplice operazione di cercare l'indirizzo di destinazione (match) e inoltrare (action), eseguito in molti dispositivi di rete: negli **switch** con azione simile ai router; nei **firewall**, dove l'azione è filtrare pacchetti in ingresso; nei **NAT (Network Address Translator)**, dove l'azione è riscrivere il numero della porta di pacchetti in ingresso prima dell'inoltramento.

Dopo il lookup il pacchetto può essere inviato nella switching fabric; in alcuni dispositivi i pacchetti possono anche mettere in coda (in buffer) temporaneamente se altre porte di ingresso stanno usando la matrice.

## Switching fabric

La matrice di commutazione è realizzabile in tre modi:

- **Switching via memoria**: le porte sono dispositivi I/O che scrivono i pacchetti in celle di memoria e il processo di routing copia il messaggio sulla porta di uscita indicata dalla forwarding table. È l'approccio più lento (necessita di accessi alla memoria) e era comune nei primi router, che erano normali calcolatori.
- **Switching via bus**: la porta di ingresso trasferisce il pacchetto direttamente alla porta di uscita over un bus condiviso, in mutua esclusione, senza l'intervento del processore di routing. Serve una porta per volta, ma spesso è sufficiente per router operanti in piccole aree locali.
- **Switching via rete di interconnessione**: porte di ingresso/uscita collegate da una rete con punti di incrocio che si aprono e chiudono reindirizzando i pacchetti. Più pacchetti possono essere inoltrati in parallelo; metodo usato in diversi router moderni.

### Switching via memoria

I primi router erano normali calcolatori: un pacchetto in arrivo interrompeva il processore, veniva copiato in memoria, ricercato, e copiato in uscita nel buffer della porta di uscita. Il pacchetto attraversa la memoria due volte: se la memoria regge B pacchetti al secondo, il router inoltra meno di B/2; inoltre due pacchetti non possono essere inoltrati contemporaneamente anche verso porte diverse, perché sul bus condiviso c'è una lettura o scrittura per volta. Nelle architetture a memoria condivisa più recenti, l'hardware della porta di ingresso esegue il lookup e trasferisce i pacchetti nei buffer di memoria opportuni, senza coinvolgere la CPU centrale per ogni pacchetto.

### Switching via bus

La porta di ingresso consegna il pacchetto direttamente alla porta di uscita over un bus condiviso: antepone un'etichetta interna che nomina la porta di uscita; tutte le porte vedono il pacchetto, solo quella nominata lo conserva e rimuove l'etichetta. Sul bus passa un solo pacchetto per volta, quindi la velocità di commutazione del router è la velocità del bus. Spesso basta: un noto router enterprise di questo tipo commuta over un backplane a 32 Gbps. Approccio semplice, economico, ma con un tetto rigido.

### Switching via crossbar

> [!def] Crossbar
> **Rete di interconnessione** formata da 2N bus che uniscono N ingressi a N uscite, con un crosspoint in ogni incrocio che si apre e chiude: chiudendo il crosspoint che unisce un ingresso a un'uscita, solo il bus di quell'uscita raccoglie il pacchetto.

Per spostare un pacchetto da A a Y il controller chiude il crosspoint AY, e solo il bus Y lo raccoglie; così A → Y e B → X avvengono contemporaneamente, con pacchetti in parallelo. La matrice è **non-blocking**: un pacchetto non è mai fermato sulla strada verso una porta di uscita che nessun altro sta usando; però due pacchetti diretti alla stessa porta contengono comunque, e uno aspetta all'ingresso.

## Code e buffering nelle porte

- **Buffer**: le porte di ingresso e uscita usano buffer per memorizzare temporaneamente i pacchetti che non possono essere trasferiti o trasmessi immediatamente.
- **Input queueing**: i pacchetti devono aspettare di attraversare la switching fabric.
- **Output queueing**: i pacchetti arrivano a una porta di uscita più veloci di quanto il collegamento in uscita possa trasmetterli.
- **Overflow del buffer**: poiché i buffer hanno capacità limitata, una coda eccessiva può causare perdita di pacchetti.

### Un confronto tra velocità di porta, fabric e collegamento

In un router con N porte di ingresso e N di uscita, tutte che ricevono alla stessa velocità R<sub>line</sub> pacchetti al secondo, nel caso peggiore in cui tutti i pacchetti vadano alla stessa porta:

- Se `Rswitch ≅ N·Rline`, la coda sulle porte di ingresso è trascurabile (la fabric riesce a inoltrare tutti in tempo), ma quella sulla porta di uscita è significativa, perché il tasso in arrivo è N volte quello del solo collegamento di uscita.
- Se `Rline < Rswitch < N·Rline`, ci sono code su entrambe le porte: in ingresso si aspetta la fabric, in uscita il collegamento.
- Se `Rswitch ≅ Rline`, coda trascurabile in uscita ma significativa in ingresso.

Nessuna scelta della fabric rimuove la coda: decide soltanto dove si verifica.

### Head-of-Line blocking

> [!def] Head-of-Line (HOL) blocking
> **Situazione** in cui il pacchetto in testa a una coda di ingresso non può essere inoltrato perché la porta di uscita desiderata è occupata; poiché la stessa coda è servita in FIFO, tutti i pacchetti dietro di lui aspettano anche se le loro porte di destinazione sono libere.

## Gestione dell'output queueing

Anche con una fabric veloce, più pacchetti possono arrivare alla stessa porta di uscita più veloci di quanto il collegamento trasmetta. I pacchetti sono temporaneamente salvati in un **output buffer** in attesa di trasmissione; poiché la capacità è limitata, una coda eccessiva può causare overflow e perdita di pacchetti. Quando il buffer è pieno il router deve decidere quali pacchetti scartare:

- **Drop-tail**: i pacchetti appena arrivati sono scartati.
- **Altre politiche**: pacchetti già in coda possono essere rimossi per fare spazio ai nuovi arrivati.

### La dimensione dei buffer

- **Regola storica**: buffer = RTT medio × capacità del collegamento; per un collegamento a 10 Gbps con 250 ms di RTT, 2,5 Gbit di buffer. La figura derivava dall'analisi di pochi flussi TCP; con N flussi grandi e indipendenti il fabbisogno scende a $RTT \cdot C/\sqrt{N}$, che nel core, dove migliaia di flussi condividono un collegamento, è una riduzione molto grande.
- **Bufferbloat**: più non è meglio, poiché un buffer più grande assorbe burst maggiori ma allunga il ritardo di coda di tutto ciò che è dentro; dieci volte il buffer per evitare perdite può significare un ritardo end-to-end maggiore e un RTT più lungo che rende più lento reagire a ogni mittente di quel cammino.

> [!info] Esempio di bufferbloat
> **Scenario** di un flusso TCP isolato con finestra di 25 pacchetti: a un RTT base di 200 ms (trasmissione per pacchetto di 10 ms), un burst di 25 pacchetti riempie il buffer; successivamente gli ACK arrivano a cadenza di 10 ms, innescando un nuovo pacchetto a ogni arrivo. Circa 5 pacchetti restano persistentemente in coda, aggiungendo circa 50 ms di ritardo di coda senza alcun aumento di throughput: è il *bufferbloat*, la coda persistente che aumenta la latenza anche a collegamento pienamente utilizzato.

## Packet scheduling

Quando più pacchetti aspettano a una porta di uscita, il router deve decidere quale trasmettere per primo: lo decide un **algoritmo di packet scheduling**, che determina l'ordine in cui i pacchetti in coda accedono al collegamento in uscita. Tre approcci comuni:

- **First-Come-First-Served (FCFS/FIFO)**: i pacchetti sono trasmessi nel loro ordine di arrivo.
- **Priority Queueing**: i pacchetti sono classificati per priorità, e le code a priorità più alta sono servite prima.
- **Round-Robin (RR)**: i pacchetti sono divisi in classi diverse, e le code sono servite a turno.

Qualunque sia l'algoritmo, un pacchetto è rimosso solo quando è stato interamente trasmesso: la scelta è fatta alla fine di ogni trasmissione, non in continuazione.

### FIFO

Un'unica coda. I pacchetti sono selezionati per transmission nello stesso ordine di arrivo alla porta di uscita; se il collegamento è occupato, un pacchetto in arrivo è memorizzato nel buffer, e se non c'è spazio la politica di scarto decide il suo destino. Nessun pacchetto può essere favorito né rimandato a favore di un altro: tutto cioè che è sul collegamento condivide una sorte. È il motivo per cui è il default: niente da configurare, niente da sbagliare.

### Priority queueing

I pacchetti in arrivo sul collegamento di uscita sono classificati in **classi di priorità** all'arrivo in coda, sulla base di criteri specifici (numeri di porta a livello di trasporto, indirizzi IP, o marcature di priorità nell'intestazione IP). Un operatore di rete può configurare code affinché pacchetti specifici (per esempio di gestione della rete o voce su IP in tempo reale) abbiano priorità sul traffico utente o non in tempo reale.

Ogni classe di priorità può avere la sua coda: vengono trasmessi prima i pacchetti della classe non vuota con priorità maggiore; la scelta tra i pacchetti della stessa classe avviene tipicamente in modo FIFO. Lo schedulatore è **non-preemptive**: una trasmissione già iniziata non è mai interrotta.

### Round robin e WFQ

Nel **round robin** i pacchetti sono ancora ordinati in classi, ma le classi sono alternate anziché selezionate per priorità; l'algoritmo è **work-conserving**: non lascia mai il collegamento inattivo, e una classe con coda vuota è saltata subito. Un'implementazione comune è la **weighted fair queuing (WFQ)**:

- I pacchetti in arrivo sono classificati e messi in coda nell'area di attesa appropriata.
- A ciascuna classe è assegnato un peso che determina la sua quota della capacità del collegamento in uscita, tenendo conto delle dimensioni dei pacchetti.
- Una classe i di peso $w_i$ riceve una quota $\frac{w_i}{\sum_j w_j}$ del servizio; su un collegamento di velocità R a una classe è garantita una velocità pari almeno a:

$$
R_i = R \times \frac{w_i}{\sum_j w_j}
$$

sulle classi attive.

Per capire la differenza tra gli approcci su un esempio concreto: una priorità alta fa passare avanti un pacchetto appena arrivato rispetto a uno più vecchio di classe bassa, mentre in un round robin un pacchetto della stessa classe non supera un altro già arrivato; e in tutti i casi il collegamento è inattivo prima di un nuovo pacchetto solo se non c'è nulla da inviare, poiché uno schedulatore decide un ordine ma non crea capacità.

Di fronte a questi approcci si distinguono tre varianti:

- **Round-Robin (RR)**: ciascuna coda non vuota è servita a turno, tipicamente trasmettendo un pacchetto per visita.
- **Weighted Round-Robin (WRR)**: a ciascuna classe è assegnato un peso che determina quanti pacchetti può trasmettere per ciclo.
- **Weighted Fair Queuing (WFQ)**: a ciascuna classe è assegnato un peso che determina la sua quota della banda del collegamento in uscita, tenendo conto delle dimensioni dei pacchetti.

Differenza chiave: RR e WRR (a pacchetti) allocano opportunità di trasmissione, mentre WFQ mira ad allocare la banda in modo proporzionale ai pesi.

### Classificazione dei pacchetti

Chi decide a quale classe appartiene ciascun pacchetto?

- Gli algoritmi di schedulazione sono indipendenti dai criteri di classificazione del traffico.
- **Policy di classificazione**: sono definite dagli operatori di rete sulla base dei campi dell'intestazione dei pacchetti (indirizzi IP, porte TCP/UDP, marcature DSCP).
- **Classi diverse**: possono ricevere priorità o quote di banda diverse.
- **Filtri**: meccanismi di classificazione simili possono anche servire per filtrare o limitare specifici tipi di traffico.
- **Net neutrality**: la differenziazione del traffico pone questioni di equità e della misura in cui gli ISP debbano poter dare priorità o limitare il traffico.

## Riassunto

- La rete offre un solo servizio, il best-effort: ordine, consegna e garanzie di ritardo sono assenti, e le estremità hanno costruito ciò di cui avevano bisogno al di sopra.
- Il forwarding è locale e richiede nanosecondi; il routing è esteso a tutta la rete e richiede secondi; la forwarding table è il punto in cui i due si incontrano.
- Una riga della tabella è un prefisso, cioè un gruppo di indirizzi che condividono i primi bit; quando più righe corrispondono, vince la più lunga.
- Tre fabric: memoria, bus, crossbar. L'ultima inoltra in parallelo e comunque non può aiutare due pacchetti che vogliono la stessa porta di uscita.
- Le code si formano dove una velocità incontra una più lenta: all'ingresso, all'uscita o in entrambi; è lì che nasce la perdita che i mittenti deducono.
- Lo scheduling decide l'ordine. Rimane aperto da dove vengono gli indirizzi dentro quei prefissi.