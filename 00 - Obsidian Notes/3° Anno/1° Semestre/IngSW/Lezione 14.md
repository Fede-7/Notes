# Lezione 14 Virtualizzazione e Cloud

## La virtualizzazione

> [!def] Virtualizzazione
> **Tecnica** per aumentare l'efficacia e l'efficienza di Centri Elaborazione Dati complessi: consiste nella creazione di una versione virtuale di una risorsa normalmente fornita fisicamente e appartenente a un sistema. Risalente agli anni Sessanta, è tornata in auge grazie all'evoluzione tecnologica delle CPU.

## L'evoluzione delle CPU

I microprocessori hanno sempre avuto un rapidissimo incremento delle prestazioni e una diminuzione dei costi; la strategia storica per migliorarle è stata aumentare la "velocità" del processore.

- **1978**: Intel 8086, 4 MHz.
- **1985**: Intel 386, 25 MHz (~6x).
- **1995**: Intel Pentium Pro, 200 MHz (~8x).
- **2005**: Intel Pentium 4, 3,8 GHz (~19x).

Questa strategia si è arrestata nel 2005: processori recenti (es. Intel Core Ultra 9 285K, 2,5–4,6 GHz) girano su frequenze comparabili.

### Le CPU multicore

Raggiunti i limiti fisici del silicio, la soluzione è stata aumentare il numero di unità di elaborazione (**multicore**) per aumentare la potenza di calcolo (es. AMD Ryzen 9 9955HX, 2,5–5,4 GHz, 32 unità di calcolo). Il problema: i programmi sono tradizionalmente scritti per un computer con una singola CPU e la stragrande maggioranza delle applicazioni è sequenziale — come sfruttare più unità in parallelo?

## L'infrastruttura tradizionale di un CED

Il modello tradizionale di Centri Elaborazione Dati prevede singoli server che offrono singoli servizi o applicazioni (**one workload, one box**): un nuovo servizio o applicazione richiede un nuovo server, con proprio storage. Le conseguenze:

- **Sottoutilizzo delle risorse**: la maggior parte dei server sfrutta in media tra il 5% e il 15% della propria capacità computazionale; per i servizi critici serve ridondanza (computer di riserva normalmente non usati).
- **Aumento dei costi di installazione e gestione**: rilascio di aggiornamenti su scala nazionale molto costoso; backup da effettuare su ogni macchina.
- **Servizi intrinsecamente interconnessi**: es. il server di dominio, che gestisce le autenticazioni, è interrogato da tutti gli altri servizi.

### Il fail di un server

In caso di guasto di un server si possono bloccare i servizi degli altri server in comunicazione con esso, con conseguenze pesanti.

- Interruzione dell'operatività collegata a quel servizio; nei casi più gravi, interruzione dell'intera operatività aziendale.
- Aumento dei costi: costi di fermo e di ripristino.
- Tempi di fermo non sempre prevedibili.

## Le macchine virtuali

Un server fisico consiste di risorse hardware, un sistema operativo e uno o più software applicativi. L'idea della virtualizzazione: se la CPU del server ha più unità di calcolo parallele, si può "simulare" l'esistenza di più computer, indipendenti dal vero hardware sottostante.

### L'hypervisor

> [!def] Hypervisor
> **Strato** software che parte prima del sistema operativo e simula l'esistenza di più computer virtuali su un server fisico: offre le risorse fisiche ai computer virtualizzati e le gestisce in modo concorrente a favore delle macchine virtuali.

Su ogni computer virtualizzato si installa un normalissimo sistema operativo, che non ha modo di sapere se sta funzionando su un computer reale o virtuale.

![[3206b1bbd2dc71f527f86e6b7e2106f2cf7032953251b9e3d7317d51ab0c3b94.png|300]]

### Le proprietà delle macchine virtuali

- **Indipendenza dall'hardware**: l'hypervisor simula una configurazione standard di un server, nascondendo il vero hardware fisico; le VM possono funzionare su server fisici diversi senza bisogno di essere configurate.
- **Memorizzazione**: una VM è un file, contenente sistema operativo, applicativi, dati e rappresentazione della memoria del server; un file memorizza lo stato di un server virtuale e ne permette la copia su un numero arbitrario di server fisici. Esistono strumenti commerciali che trasformano il contenuto di un server fisico in una VM.
- **Isolamento**: ogni VM è totalmente isolata dalle altre VM in esecuzione sullo stesso server fisico; in caso di attacco o crash di una VM, le altre non sono intaccate.
- **Gestione centralizzata**: tutte le VM di un CED possono essere gestite attraverso un'unica finestra, semplificando notevolmente la gestione dell'intero centro.

## La virtualizzazione enterprise ad alta disponibilità

Un CED enterprise deve disporre di almeno **due server fisici** e di un'unità di dischi rigidi (**SAN**, Storage Area Network), collegati tra loro ad altissima velocità (fibra ottica). Nella virtualizzazione enterprise le macchine virtuali risiedono nello storage SAN.

La virtualizzazione garantisce la **business continuity** tramite funzioni dedicate.

- **HA (High Availability, alta disponibilità)**: se un server ha un guasto, le macchine virtuali presenti sono istantaneamente migrate sugli altri server disponibili e fatte ripartire, minimizzando il downtime al tempo di restart delle VM.
- **FT (Fault Tolerant)**: garantisce la continuità di funzionamento delle VM dopo il guasto di un server, azzerando il tempo di fermo; è al momento quanto di meglio si possa avere per la business continuity.
- **Live migration**: la migrazione "a caldo" delle VM tra i server fisici consente operazioni di manutenzione o di bilanciamento del carico mantenendo l'operatività dei server virtuali.

## I benefici della virtualizzazione

Con l'introduzione della virtualizzazione si parla di **consolidamento** di un CED: sfruttando le risorse di computazione parallela dei nuovi processori, si riduce significativamente il numero di server necessari per erogare i servizi richiesti da un ente. Gli altri benefici:

- **Ottimizzazione delle risorse HW**: esecuzione di distinti sistemi operativi contemporaneamente in una singola macchina.
- **Ottimizzazione dello spazio disco**: a ogni VM viene assegnato lo spazio strettamente necessario, e il resto del volume resta disponibile per nuove macchine virtuali.
- **Semplificazione**: backup e disaster recovery (l'intero server — SO, applicazioni, dati, dispositivi e stato — non è altro che un file); indipendenza dall'hardware; rilasci semplificati; possibilità di clonare "live" le VM per test e aggiornamenti senza compromettere l'integrità dell'originale.
- **Riduzione dei costi**: meno server significa risparmio sui costi energetici, di condizionamento e sugli spazi fisici richiesti dal CED; la gestione centralizzata attraverso un'unica interfaccia di amministrazione incrementa la produttività del reparto IT.

## Il cloud computing

> [!def] Cloud computing
> **Modello** in cui le risorse IT sono fornite come servizio: calcolo, storage, database, code. Sfrutta le economie di scala dell'hardware commodity (storage economico, reti ad alta banda, processori multicore) e data center geograficamente distribuiti; offerte da Microsoft, Amazon, Google e altri.

### Scalabilità ed elasticità

Le due proprietà chiave del cloud sono strettamente correlate.

> [!def] Scalabilità
> **Proprietà** desiderabile di un sistema, una rete o un processo, che indica la capacità di gestire quantità crescenti di lavoro in modo graduale o di essere ingrandito prontamente.

La scalabilità statica non basta: le risorse devono seguire la domanda in tempo reale.

> [!def] Elasticità
> **Capacità** di far crescere o ridurre dinamicamente le risorse dell'infrastruttura in base al bisogno, adattandosi in modo autonomo ai cambiamenti del carico di lavoro e massimizzando l'uso delle risorse.

Queste proprietà si ottengono con il **dynamic provisioning** e il **multi-tenant design**.

### Il dynamic provisioning

> [!def] Dynamic provisioning
> **Modalità** di un ambiente complesso di server in rete in cui le istanze di calcolo vengono provisionate o deployate da una console amministrativa o da un'applicazione client, da parte dell'amministratore di server o di rete o di qualsiasi altro utente abilitato.

Nel modello di calcolo tradizionale ci sono due problemi comuni: la sottostima dell'utilizzo del sistema, che porta a un under-provisioning, e la sovrastima, che porta a un basso utilizzo. La soluzione è provisionare dinamicamente le risorse del cloud, per:

- far fronte alle variazioni stagionali della domanda;
- far fronte alle variazioni di domanda tra settori diversi;
- gestire il burst demand di eventi straordinari.

## I service model

I servizi cloud si organizzano in tre modelli, che si distinguono per quanta infrastruttura è gestita dal provider e quanta resta sotto il controllo del consumatore.

> [!def] Infrastructure as a Service (IaaS)
> **Modello** in cui il provider offre elaborazione, storage, reti e altre risorse di calcolo fondamentali, e il consumatore può deployare ed eseguire software arbitrario, inclusi sistemi operativi e applicazioni. Il consumatore non gestisce né controlla l'infrastruttura cloud sottostante, ma ha controllo su sistemi operativi, storage, applicazioni deployate ed eventuale controllo limitato di alcune componenti di rete.

Un gradino più in alto, il provider fornisce anche la piattaforma di sviluppo ed esecuzione.

> [!def] Platform as a Service (PaaS)
> **Modello** in cui al consumatore è data la capacità di deployare sull'infrastruttura cloud applicazioni da lui create o acquisite, usando librerie e strumenti supportati dal provider. Il consumatore non gestisce l'infrastruttura sottostante (rete, server, sistemi operativi, storage), ma ha controllo sulle applicazioni deployate ed eventualmente sulle configurazioni dell'ambiente di hosting.

Al gradino più alto, il consumatore usa direttamente applicazioni già pronte.

> [!def] Software as a Service (SaaS)
> **Modello** in cui al consumatore è data la capacità di usare le applicazioni del provider in esecuzione su un'infrastruttura cloud, accessibili da vari dispositivi client tramite thin client come un browser web (es. email web-based). Il consumatore non gestisce l'infrastruttura né le singole capacità applicative, salvo limitate impostazioni di configurazione user-specific.

Esempi tipici: per IaaS, Amazon EC2, Azure Compute, OpenNebula; per PaaS, Microsoft Azure SQL Database, Amazon AWS Lambda, Hadoop; per SaaS, Google Apps (Gmail, Google Docs, Google Sites) e Amazon AWS QuickSight.

## I deployment model

I modelli di deployment primari del cloud sono tre — public, private e hybrid — che insieme al community cloud compongono l'ecosistema cloud. Le loro differenze stanno principalmente nello scope e nell'accesso dei servizi cloud pubblicati verso i consumatori.

> [!def] Public cloud
> **Infrastruttura** cloud resa disponibile al grande pubblico o a un grande gruppo industriale e di proprietà di un'organizzazione che vende servizi cloud; nota anche come cloud esterno o multi-tenant cloud, rappresenta un ambiente apertamente accessibile.

Caratteristiche di base: infrastruttura omogenea, politiche comuni, risorse condivise e multi-tenant, infrastruttura affittata, economie di scala.

> [!def] Private cloud
> **Infrastruttura** cloud gestita esclusivamente per un'organizzazione; può essere gestita dall'organizzazione o da terzi e risiedere on premise o off premise. Nota anche come cloud interno o on-premise cloud, limita intenzionalmente l'accesso alle risorse ai consumatori della stessa organizzazione proprietaria.

Caratteristiche di base: infrastruttura heterogenea, politiche personalizzate, risorse dedicate, infrastruttura interna, controllo end-to-end.

### Public vs. private

| | Public Cloud | Private Cloud |
| --- | --- | --- |
| Infrastruttura | Omogenea | Heterogenea |
| Modello di policy | Comuni e definite | Personalizzate |
| Modello di risorse | Condivise e multi-tenant | Dedicate |
| Modello di costi | Operational expenditure | Capital expenditure |
| Modello economico | Grandi economie di scala | Controllo end-to-end |

> [!def] Hybrid cloud
> **Composizione** di due o più cloud (private, community o public) che restano entità uniche ma sono legate insieme da tecnologie standard o proprietarie che abilitano la portabilità di dati e applicazioni (es. cloud bursting per il bilanciamento del carico tra cloud).