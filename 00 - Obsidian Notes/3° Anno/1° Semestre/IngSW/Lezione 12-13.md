# Lezione 11-12 Standard Software Architectures

## Architettura del software

> [!def] Architettura del software
> **Struttura** o strutture del sistema, comprendenti gli elementi software, le loro proprietà visibili esternamente e le relazioni tra loro. Le strutture esatte da considerare e i modi di rappresentarle variano secondo gli obiettivi ingegneristici.

La definizione ha diverse implicazioni.

- L'architettura è un'**astrazione** del sistema: definisce gli elementi e come interagiscono, sopprimendo le informazioni puramente locali (i dettagli privati degli elementi non sono architetturali).
- Le proprietà esternamente visibili sono le assunzioni che un elemento può fare su un altro: servizi forniti e richiesti, caratteristiche di performance, gestione dei fault, uso delle risorse.
- **Ogni sistema ha un'architettura**, anche nel caso più semplice di un singolo elemento; ma avere un'architettura è diverso dall'avere un'architettura nota a tutti (l'architettura vs. la specifica dell'architettura): se non la si sviluppa esplicitamente, la si ottiene comunque — e potrebbe non piacere.
- I disegni di box-and-line da soli **non sono** architetture, ma solo un punto di partenza: serve aggiungere specifiche e proprietà.
- I sistemi hanno molte strutture (**viste**): nessuna struttura singola può essere "l'architettura", e l'insieme delle strutture candidate non è fisso né prescritto — si scelgono quelle utili per analisi, comunicazione o comprensione.

## Scopo della progettazione architetturale

L'architettura si definisce nella prima fase di System Design (progettazione architetturale) e ha come scopo primario la scomposizione del sistema in sottosistemi.

- La realizzazione di più componenti distinti è meno complessa della realizzazione di un sistema come monolite.
- Permette di parallelizzare lo sviluppo.
- Favorisce modificabilità, riusabilità, portabilità.

Definire un'architettura significa **mappare funzionalità su moduli** (es. modulo di interfaccia utente, modulo di accesso al database, modulo di gestione della sicurezza). Anche la definizione delle architetture deve seguire i concetti di **alta coesione** e **basso accoppiamento**: ogni sottosezione fornisce servizi altamente correlati, limitando il numero di moduli con cui è legata.

La definizione avviene da due punti di vista che portano alla soluzione finale:

- **identificazione e relazione dei sottosistemi**;
- **definizione delle politiche di controllo**.

Entrambe le scelte sono cruciali: è difficile modificarle quando lo sviluppo è partito, perché molte interfacce dei sottosistemi dovrebbero essere cambiate.

## Divide and conquer

> [!aside]
> Un principio guida della decomposizione è **divide and conquer**: affrontare qualcosa di grande tutto insieme è più difficile che affrontare un insieme di cose più piccole.
> 
> - Ogni componente individuale è più piccolo e quindi più facile da capire.
> - Le parti possono essere sostituite o modificate senza dover sostituire o cambiare estesamente le altre.
> - Persone separate possono lavorare su parti separate, e il singolo ingegnere può specializzarsi.
> 
> Un sistema si divide gerarchicamente: **sistema → layer e sottosistemi → package → classi → metodi**. La decomposizione segue due dimensioni: quella funzionale (sottosistemi) e quella di astrazione/implementazione (layering).
> 
> ---
> 
> ![[5b6c036d261169026d2dd19dd2ef13fceae45724851f490c675bd922d072b293.png|200]]

Nell'architettura logica, layer e partizioni si combinano: i layer dividono il sistema lungo la dimensione dell'astrazione, le partizioni lungo la dimensione funzionale.

![[462b9c3fc06a5699505d54e7548eb4424f82086702a54eaaddfb140bb7e34e48.png|350]]

## L'architettura a livelli

> [!def] Layer
> **Raggruppamento** di sottosistemi che forniscono servizi correlati, eventualmente realizzati usando servizi di altri layer. Una decomposizione gerarchica di un sistema consiste in un insieme ordinato di layer.

- Un layer può dipendere solo dai layer di livello più basso e non ha conoscenza dei layer superiori.
- **Architettura chiusa**: ogni layer può accedere solo al layer immediatamente sotto di esso; design goal: alta manutenibilità e portabilità.
- **Architettura aperta**: un layer può anche accedere ai layer di livello più basso; design goal: efficienza a runtime.

### La macchina virtuale

La prima formalizzazione dell'architettura a layer è la **macchina virtuale** (Dijkstra, 1965): un sistema dovrebbe essere sviluppato come insieme di macchine virtuali, ognuna costruita in termini di quelle al di sotto di essa.

### La layered architecture

Nella layered architecture i sottosistemi sono organizzati in layer: ogni layer usa i servizi del layer sottostante e fornisce servizi al layer superiore tramite interfacce ben definite. I termini **tier** e **layer** sono, per la maggior parte delle persone, intercambiabili. Bilancio di pro e contro:

- **+** astrazione delle preoccupazioni (abstraction of concerns);
- **+** isolamento dei livelli bassi e alti l'uno dall'altro (decoupled);
- **+** riusabilità;
- **−** overhead nell'attraversare i diversi layer;
- **−** complessità.

## L'architettura client-server

> [!def] Client-server
> **Architettura** distribuita dove dati ed elaborazione sono distribuiti su una rete di nodi di due tipi: i server, processori potenti e dedicati che offrono servizi specifici (stampa, gestione di file system, compilazione, gestione del traffico di rete, calcolo); i client, macchine meno prestazionali su cui girano le applicazioni utente che usano i servizi dei server.

Le regole di conoscenza sono asimmetriche.

- I client devono conoscere i nomi e la natura dei server; i server non devono conoscere identità e numero dei client.
- I client chiamano il server, che realizza alcuni servizi e restituisce il risultato; i client conoscono l'interfaccia del server, i server non conoscono le interfacce dei client.
- La risposta è in generale immediata; gli utenti interagiscono solo con il client.

![[250086ab7686895d396fb5fe130641383849f45554585e507c9db53ba6a2626a.png|300]]

## L'architettura a repository

> [!def] Repository
> **Architettura** in cui i sottosistemi accedono e modificano una singola struttura dati chiamata repository; i sottosistemi sono relativamente indipendenti, perché interagiscono solo attraverso il repository.

Il flusso di controllo è dettato o dal repository (un cambiamento nei dati memorizzati) o dai sottosistemi (flusso di controllo indipendente). Esempi tipici: i database management systems e i compilatori moderni.

![[b2ba2a73c8a8997c4100d5965f35933b857b190dbf33732384c084f8e64e4ed0.png|300]]

### Vantaggi del repository

- Modo efficiente di condividere grandi moli di dati: write once for all to read.
- Un sottosistema non deve preoccuparsi di come i dati sono prodotti o usati dagli altri sottosistemi.
- Gestione centralizzata di backup, sicurezza, controllo degli accessi e recovery da errori.
- Il modello di condivisione dei dati è pubblicato come repository schema: è facile aggiungere nuovi sottosistemi.

### Svantaggi del repository

- I sottosistemi devono concordare su un modello dati di compromesso → performance ridotte.
- **Data evolution**: adottare un nuovo modello dati è difficile e costoso, perché deve essere applicato a tutto il repository e tutti i sottosistemi devono essere aggiornati.
- Diversi sottosistemi possono avere requisiti diversi su backup e sicurezza, non supportati.
- È difficile distribuire efficientemente il repository su più macchine continuando a vederlo come logicamente centralizzato: problemi di ridondanza e consistenza dei dati.

## Le architetture three-tier

Le architetture three-tier sono state introdotte negli anni Novanta e trattano la business logic in modo esplicito, su tre livelli.

- **Livello 1 — gestione dei dati**: comunicazione verso DBMS, file XML, ecc.
- **Livello 2 — business logic**: processamento dei dati.
- **Livello 3 — interfaccia utente**: presentazione dei dati, servizi.

![[037291eff6d670a161d588af6de5eeea9e331fa5b06f37f9748610083bba0811.png|300]]

Ogni livello ha obiettivi e vincoli di design propri, e nessun livello fa assunzioni sulla struttura o sull'implementazione degli altri: il livello 2 non assume nulla sulla rappresentazione dei dati né sull'implementazione dell'interfaccia utente, e il livello 3 non assume nulla su come opera la business logic.

- **Non c'è comunicazione diretta tra livello 1 e livello 3**: l'interfaccia utente non riceve né inserisce direttamente dati nel livello di data management; tutti i passaggi di informazione nei due sensi vengono filtrati dalla business logic.
- I livelli operano senza assumere di essere parte di una specifica applicazione: le applicazioni sono viste come collezioni di componenti cooperanti, e ogni componente può essere contemporaneamente parte di applicazioni diverse.

### Vantaggi delle three-tier

- **Flessibilità e modificabilità**: componenti utilizzabili in sistemi diversi; la modifica di una componente non impatta sul resto del sistema (a meno di cambiamenti nelle API); ricerca di bug più focalizzata per la separazione e l'isolamento delle funzionalità; l'aggiunta di funzionalità implica l'estensione delle sole componenti coinvolte o l'aggiunta di nuove componenti.
- **Interconnettività**: le API delle componenti superano il problema degli adattatori del modello client-server, così che interfacce diverse possano essere connesse allo stesso servizio; l'accesso a dati comuni da applicazioni diverse è facilitato.
- **Gestione di sistemi distribuiti**: la business logic di applicazioni distribuite (es. sistemi informativi con server replicati e client remoti) è aggiornabile senza richiedere l'aggiornamento dei client.

### Svantaggi delle three-tier

- **Dimensioni delle applicazioni ed efficienza**: pesante uso della comunicazione in rete, che introduce latenza nel servizio; la comunicazione tra componenti richiede librerie per lo scambio di informazioni, con codice voluminoso.
- **Integrazione di legacy software**: molte imprese usano software vecchio basato sul modello monolitico; è difficile applicare il modello three-tier alle nuove applicazioni e servono adattatori per interfacciare il software legacy.

## Le architetture n-tier

Le architetture **n-tier** sono l'evoluzione delle 3-tier su N livelli e permettono configurazioni diverse. Gli elementi fondamentali sono:

- **Interfaccia utente (UI)**: gestisce l'interazione con l'utente; può essere un web browser, una mobile app, un'interfaccia grafica.
- **Presentation logic**: definisce cosa la UI presenta e come gestire le richieste dell'utente.
- **Business logic**: gestisce le regole di business dell'applicazione.
- **Infrastructure services**: forniscono funzionalità supplementari alle componenti dell'applicazione (messaging, supporto alle transazioni).
- **Data layer**: il livello dei dati dell'applicazione.

![[b19cabbfdb75bba004ec23b9377bdeaecb99a1a0a7a4cd3c70814d62b14404dc.png|350]]

## La Service-oriented Architecture

> [!def] Service-oriented Architecture
> **Architettura** in cui i servizi sono componenti stateless: possono essere replicati e migrare da un computer a un altro.

- Molti server possono essere coinvolti nell'erogazione dei servizi.
- Una SOA è in genere più facile da scalare quando la domanda cresce ed è resiliente ai guasti.

![[9f93dadded8e37f55f48b10a8f61695b026f16a7b5d7370e9e803e5dd2c33fca.png|350]]

## Gli stili architetturali

Nell'ingegneria del software sono stati definiti vari **stili architetturali** usabili come base per uno specifico sistema da sviluppare: Client/Server, Repository, Peer-to-Peer, Model/View/Controller (nelle sue declinazioni), Multi-tiered, Microservices.