# Processi Software e Qualità Software

## Qualità Software nel Ciclo di Vita

L'ingegneria del software si occupa della qualità del prodotto in tutte le fasi del suo ciclo di vita. In questa lezione affrontiamo come identificare le principali attività di sviluppo e operazione, distinguere le proprietà del prodotto dagli esiti del suo utilizzo, discutere gli attributi di qualità e i compromessi tra di essi, e collegare gli obiettivi di qualità ai requisiti e alle evidenze di valutazione. Lo studio dei modelli di processo avverrà successivamente, dopo aver esplorato le attività che organizzano.

## Attività del Ciclo di Vita del Software

Un processo software è l'insieme delle attività correlate che conduce alla produzione di un sistema software. Non esiste un processo universale che funzioni sempre, e nelle pratiche attuali si utilizzano molti processi diversi. Tuttavia, tutti includono, in una forma o nell'altra, quattro attività fondamentali.

### Software Specification
L'attività di specifica consiste nel comprendere i bisogni degli stakeholder e definire il comportamento richiesto e i vincoli del sistema. Questo significa capire cosa il software deve fare e quali limitazioni deve rispettare.

### Software Development
Lo sviluppo riguarda la progettazione e l'implementazione di una soluzione che affronti i bisogni identificati. In questa fase si trasformano i requisiti in codice funzionante e artefatti di progettazione.

### Software Validation
La validazione consiste nel valutare se la soluzione realizzata supporta effettivamente l'uso previsto. Si verifica cioè che il sistema soddisfi le esigenze dei clienti e degli utenti finali.

### Software Evolution
L'evoluzione riguarda l'adattamento del software al cambiamento continuo di requisiti, dipendenze e condizioni di esercizio. Questa attività è essenziale perché il software non è mai veramente finito: requisiti, piattaforme, dipendenze e minacce cambiano costantemente, per cui il software deve essere mantenuto, adattato e evoluto. Progettare per il cambiamento è quindi un problema centrale dell'ingegneria del software.

#### Qualità, Sicurezza, Automazione e Operazione
Queste dimensioni trasversali accompagnano tutte le attività del ciclo di vita.

### Complessità e Coordinamento delle Attività

Le attività descritte sono complesse e includono numerose sotto-attività. Come ogni processo creativo, i processi software si affidano alle persone che prendono decisioni e formulano giudizi. Oltre alle quattro attività fondamentali, i processi software includono tipicamente ulteriori attività come la pianificazione del progetto e il monitoraggio dell'avanzamento.

## Costi dello Sviluppo Software

La distribuzione dei costi nel ciclo di vita del software rivela come la manutenzione rappresenti la fase più onerosa. Secondo le analisi classiche, la manutenzione assorbe il 67% dei costi totali, mentre lo sviluppo iniziale si distribuisce così: testing 15%, requirements engineering 6%, coding 6%, design 5%. Questo dato sottolinea l'importanza di progettare per il cambiamento e di realizzare software che sia facile da mantenere e adattare nel tempo.

## Organizzazione delle Attività

Un processo software definisce come le attività, i ruoli e gli artefatti vengono organizzati e coordinati. Le medesime quattro attività fondamentali possono essere strutturate in modo molto diverso a seconda della metodologia adottata. In questa lezione le studieremo individualmente, mentre alla fine del corso esamineremo come diversi processi le organizzano in modo differente.

## Dettaglio delle Attività del Ciclo di Vita

### Requirements Engineering

#### Obiettivo e Attività Principali

L'obiettivo della requirements engineering è comprendere i bisogni degli stakeholder e definire cosa il software deve conseguire, inclusi i requisiti di qualità e i vincoli. Concretamente, si raccolgono e si analizzano i bisogni insieme agli stakeholder, si registrano i requisiti utilizzando forme adatte come specifiche, casi d'uso o user story, si definiscono i criteri di accettazione e si risolvono le ambiguità. Infine, si mantengono i collegamenti tra requisiti, decisioni di progettazione e test man mano che i requisiti cambiano.

#### Tecniche di Elicitazione e Specifica

I requisiti vengono raccolti attraverso interviste con gli stakeholder, e per rappresentare il contesto e le esigenze si utilizzano tecniche come personas, stories e scenarios. La loro specifica avviene mediante use cases, linguaggio naturale, domain models e mock-up.

### System Design

#### Obiettivo e Strutturazione dell'Architettura

L'obiettivo della progettazione di sistema è disegnare una struttura (architettura) adeguata che supporti il comportamento richiesto e gli attributi di qualità. L'architettura identifica i componenti principali, le responsabilità e le interazioni. In questa fase i requisiti vengono allocati ai sottosistemi software, e i sottosistemi vengono allocati alle risorse hardware. Si applicano pattern architetturali per strutturare il sistema in modo coerente.

#### Progettazione Dettagliata

Nella progettazione dettagliata si definiscono le interfacce, le classi e le loro collaborazioni. Si impiegano design pattern per realizzare ciascun sottosistema in modo uniforme e mantenibile. La progettazione dell'interfaccia utente e i prototipi aiutano a valutare l'interazione con gli utenti. È importante riconoscere che le decisioni progettuali comportano compromessi, come ad esempio tra performance e modifiabilità. Modelli e decision records spiegano la soluzione e la sua logica; il linguaggio UML supporta viste selezionate della progettazione.

#### Usability Engineering

Durante la progettazione si incorporano anche considerazioni di usability engineering e si realizzano wireframe ad alta fedeltà per validare le scelte progettuali.

### Implementation

#### Obiettivo e Principi

L'obiettivo dell'implementazione è realizzare software funzionante mentre si raffinano e si verificano le decisioni progettuali. Nel codificare si implementa il comportamento richiesto e si gestiscono esplicitamente gli errori. Si scrive codice che altri sviluppatori possono comprendere, testare e modificare. Seguire le linee guida di Clean Code aiuta a valutare l'implementazione nel suo contesto.

#### Pratiche di Controllo e Qualità

Si utilizza la code review e l'analisi statica per esaminare l'implementazione. Si automatizzano le build e i regression test per assicurare che i cambiamenti non introducano regressioni. Un aspetto critico è che gli sviluppatori rimangono responsabili della revisione e della validazione dei contributi assistiti da AI, garantendo così il controllo umano sulla qualità del codice prodotto.

### Verification and Validation (V&V)

#### Definizioni e Differenze

La verifica e la validazione rispondono alla domanda centrale: gli artefatti sviluppati soddisfano effettivamente i bisogni degli utenti?

**Verifica** risponde alla domanda "abbiamo costruito la cosa nel modo giusto?". Si tratta di controllare se il sistema è conforme alla sua specifica. Tipicamente si realizza mediante program testing: eseguendo il software in un ambiente controllato e verificando che il suo comportamento sia corretto rispetto alle specifiche.

**Validazione** risponde alla domanda "abbiamo costruito la cosa giusta?". Si tratta di verificare se il sistema incontra le aspettative dei clienti. Tipicamente si realizza definendo ed eseguendo acceptance test. V&V si applica ai requisiti e alle progettazioni oltre che al software eseguibile, e continua man mano che il software evolve. I test di accettazione contribuiscono alla validazione, e il superamento di una suite di test fornisce evidenza nel contesto specifico di quei test.

### Delivery, Operation and Evolution

La delivery prepara e rilascia il software nell'ambiente target. L'operation mantiene il servizio disponibile e fornisce evidenza sul comportamento del sistema in uso. La maintenance corregge i difetti e adatta il software ai bisogni, alle dipendenze e agli ambienti che cambiano. Procedure automatizzate di delivery e di recovery aiutano a gestire i rischi associati al cambiamento. In questo corso introduciamo CI/CD, observability e pratiche che supportano l'evoluzione del software, argomenti approfonditi ulteriormente nel corso di Software Project Management and Evolution.

## Software Quality

### La Molteplicità della Qualità

Non esiste una sola "qualità", ma piuttosto molti approcci e punti di vista diversi. La qualità di un prodotto software dipende fortemente dall'uso previsto e dagli interessi degli stakeholder. Un modello di qualità fornisce agli stakeholder un vocabolario condiviso per discutere requisiti e valutazione.

#### Prospettive sulla Qualità Software

La qualità del software può essere esaminata da tre prospettive distinte:

**Qualità interna** riguarda le proprietà esaminate senza eseguire il software, come le dipendenze e la struttura del codice. Aspetti come la modularità, la leggibilità e l'assenza di code smell rientrano in questa categoria.

**Qualità esterna** riguarda le proprietà osservate durante l'esecuzione, come il tempo di risposta e il comportamento in caso di fallimento. Sono il risultato delle proprietà interne ma osservabili solo in runtime.

**Qualità nell'uso** riguarda gli esiti per le persone e le organizzazioni che utilizzano il sistema in un contesto specifico. Misura quanto bene il sistema aiuta gli utenti a raggiungere i loro obiettivi nel loro ambiente di lavoro reale.

Le pratiche di processo aiutano a conseguire e valutare la qualità. Tuttavia, la loro adozione deve essere accompagnata da evidenza tangibile circa il prodotto e il suo utilizzo.

### Modelli di Qualità Software

La standardizzazione internazionale ha prodotto modelli di riferimento per articolare la qualità. L'ISO/IEC 25010:2023 descrive la qualità del prodotto attraverso nove caratteristiche. L'ISO/IEC 25019:2023 affronta la qualità nell'uso. L'ISO/IEC 25002:2024 spiega il framework e l'uso dei modelli di qualità. Le priorità rilevanti e i criteri di valutazione dipendono dal prodotto specifico e dai suoi stakeholder.

## Qualità del Prodotto Software secondo ISO/IEC 25010:2023

Il modello ISO/IEC 25010:2023 organizza la qualità del prodotto in nove caratteristiche fondamentali: functional suitability, reliability, performance efficiency, interaction capability, security, compatibility, maintainability, flexibility e safety.

### Functional Suitability (Idoneità Funzionale)

La functional suitability è il grado in cui un componente o sistema fornisce funzioni che soddisfano bisogni espliciti e impliciti quando utilizzati in condizioni specificate. Questa caratteristica si compone di tre sotto-caratteristiche.

**Completezza funzionale** misura il grado in cui le funzioni fornite coprono tutti i compiti specificati e gli obiettivi dell'utente. Un'applicazione deve offrire tutte le funzionalità promesse.

**Correttezza funzionale** misura il grado in cui il prodotto fornisce risultati accurati quando utilizzato dagli utenti previsti. I calcoli devono essere corretti e i dati elaborati in modo preciso.

**Appropriatezza funzionale** misura il grado in cui le funzioni facilitano il conseguimento dei compiti e degli obiettivi specificati. Le funzioni devono essere effettivamente utili e ben progettate.

Un esempio concreto: un sistema di prenotazione di aule deve supportare l'annullamento delle prenotazioni, applicare correttamente le regole di booking, e aiutare gli utenti a trovare un'aula adatta.

### Reliability (Affidabilità)

L'affidabilità rappresenta il grado in cui il sistema esegue le sue funzioni in condizioni specificate per un periodo di tempo specificato. Questa caratteristica si articola in quattro sotto-caratteristiche.

**Assenza di difetti** misura il grado in cui un sistema esegue le funzioni specificate senza difetti durante il funzionamento normale. Il software dovrebbe "semplicemente funzionare" nella maggior parte dei casi.

**Disponibilità** misura il grado in cui un sistema è operativo e accessibile quando richiesto per l'uso. Un servizio web deve essere online quando i clienti lo cercano.

**Tolleranza ai difetti** misura il grado in cui un sistema opera come previsto nonostante la presenza di difetti hardware o software. Un'applicazione dovrebbe, per quanto possibile, continuare a funzionare anche se alcune parti falliscono.

**Recuperabilità** riguarda il ripristino dei dati interessati e il ritorno allo stato operativo richiesto dopo un'interruzione o un fallimento. Dopo un crash, il sistema deve poter recuperare i dati non salvati o tornare a uno stato consistente.

### Performance Efficiency (Efficienza Prestazionale)

L'efficienza prestazionale riguarda i tempi di risposta, il throughput e l'utilizzo delle risorse in condizioni operative specificate. Questa caratteristica si articola in tre sotto-caratteristiche.

**Comportamento temporale** misura il grado in cui i tempi di risposta e i tassi di throughput di un prodotto o sistema soddisfano i requisiti. Un'operazione di ricerca potrebbe dover essere completata entro due secondi.

**Utilizzo delle risorse** misura il grado in cui le quantità e i tipi di risorse utilizzate da un prodotto o sistema soddisfano i requisiti. Un'applicazione mobile non dovrebbe consumare tutta la batteria in poche ore.

**Capacità** misura il grado in cui i limiti massimi di un parametro del prodotto o del sistema soddisfano i requisiti. Un database dovrebbe essere in grado di gestire milioni di record senza degradare le prestazioni.

### Interaction Capability (Capacità di Interazione)

La capacità di interazione riguarda le funzionalità del prodotto che supportano gli utenti nell'interagire con il sistema per completare i compiti. Diverse sotto-caratteristiche compongono questa dimensione.

**Riconoscibilità** misura il grado in cui gli utenti possono riconoscere se il sistema è appropriato per i loro bisogni. All'avvio, il sistema dovrebbe comunicare chiaramente cosa fa.

**Imparabilità** misura il grado in cui le funzioni di un prodotto o sistema possono essere imparate da utenti specificati entro un tempo specificato. Un'interfaccia intuitiva non dovrebbe richiedere giorni di formazione.

**Operabilità** misura il grado in cui un prodotto o sistema è facile da utilizzare e controllare. I comandi dovrebbero essere logici e le opzioni facilmente accessibili.

**Protezione dagli errori dell'utente** misura il grado in cui un sistema previene errori. Se un utente è sul punto di eliminare dati importanti, il sistema dovrebbe chiedere conferma.

**Inclusività** misura il grado in cui un sistema può essere utilizzato da persone di vari background: differenti età, abilità, culture, etnie, lingue, generi, situazioni economiche. L'accessibilità è una componente cruciale della qualità moderna.

### Security (Sicurezza)

La sicurezza rappresenta il grado in cui un sistema si difende da attacchi da parte di agenti malintenzionati e protegge le informazioni e i dati applicando meccanismi di autorizzazione appropriati. Tra le sotto-caratteristiche principali:

**Confidenzialità** misura il grado in cui un sistema assicura che i dati siano accessibili solo a coloro che sono autorizzati ad accedervi. Le password e le informazioni sensibili non dovrebbero mai fuoriuscire.

**Integrità** misura il grado in cui un sistema assicura che il suo stato e i suoi dati siano protetti da modifiche o eliminazioni non autorizzate. Un file modificato da un utente non autorizzato viola l'integrità.

**Non-ripudio** misura il grado in cui azioni o eventi possono essere provati come avvenuti, in modo che gli eventi o le azioni non possano essere negati in seguito. Un sistema dovrebbe tracciare chi ha fatto cosa e quando.

**Accountability** misura il grado in cui le azioni di un'entità possono essere rintracciato univocamente a quell'entità. Ogni azione dovrebbe essere attribuibile a un utente specifico.

**Autenticità** misura il grado in cui l'identità di un soggetto o di una risorsa può essere provato come quello dichiarato. Un utente che accede deve provare veramente di essere chi dice di essere.

### Compatibility (Compatibilità)

La compatibilità rappresenta il grado in cui un sistema può scambiare informazioni con altri prodotti, sistemi o componenti, e/o eseguire le sue funzioni richieste condividendo lo stesso ambiente comune e risorse con altri sistemi. Questa caratteristica si articola in due sotto-caratteristiche.

**Coesistenza** misura il grado in cui un prodotto può eseguire le sue funzioni richieste efficientemente condividendo un ambiente comune e le risorse con altri prodotti, senza impatto negativo su nessun altro prodotto. Due applicazioni non dovrebbero interferire l'una con l'altra anche se in esecuzione sullo stesso computer.

**Interoperabilità** misura il grado in cui un sistema, prodotto o componente può scambiare informazioni con altri prodotti e utilizzare reciprocamente le informazioni scambiate. Un software di office suite dovrebbe essere in grado di leggere file creati da competitor.

### Maintainability (Manutenibilità)

La manutenibilità rappresenta il grado di efficacia ed efficienza con cui un prodotto o sistema può essere modificato per migliorarlo, correggerlo o adattarlo a cambiamenti nell'ambiente e nei requisiti. Questa caratteristica include cinque sotto-caratteristiche.

**Modularità** limita l'impatto dei cambiamenti su diversi componenti. Un cambiamento in un modulo non dovrebbe cascata in tutti gli altri.

**Riusabilità** riguarda l'utilizzo di un asset in più di un sistema. Codice ben scritto e generalizzato può essere applicato a problemi diversi.

**Analizzabilità** riguarda la capacità di comprendere i difetti e valutare l'impatto dei cambiamenti. Un codice leggibile facilita il debug e la manutenzione.

**Modifiabilità** riguarda la capacità di realizzare cambiamenti preservando la qualità richiesta. Non ogni cambiamento dovrebbe introdurre bug o degradare le prestazioni.

**Testabilità** riguarda l'istituzione di criteri e il controllo se sono soddisfatti. Un codice ben strutturato è più facile da testare.

### Flexibility (Flessibilità)

La flessibilità è il grado in cui un prodotto può essere adattato a cambiamenti nei requisiti, nei contesti d'uso o nell'ambiente operativo. Questa caratteristica include quattro sotto-caratteristiche.

**Adattabilità** misura il grado in cui un sistema può essere adattato efficacemente ed efficientemente a diversi hardware, software o altri ambienti operativi o di utilizzo. Un'applicazione web dovrebbe funzionare su browser diversi.

**Scalabilità** misura il grado in cui un sistema può gestire carichi di lavoro crescenti o decrescenti o adattare la sua capacità per gestire variabilità. Un database dovrebbe gestire un numero di utenti in crescita.

**Installabilità** misura il grado di efficacia ed efficienza con cui un prodotto o sistema può essere installato e/o disinstallato con successo. L'installazione non dovrebbe essere un incubo per l'utente finale.

**Rimpiazzabilità** misura il grado in cui un prodotto può rimpiazzare un altro prodotto software specificato per lo stesso scopo nello stesso ambiente. Se un software diventa obsoleto, il suo sostituto dovrebbe essere compatibile.

### Safety (Sicurezza di Esercizio)

La sicurezza di esercizio rappresenta il grado in cui un prodotto evita uno stato in cui la vita umana, la salute, la proprietà o l'ambiente sono messi in pericolo. Questa caratteristica include diverse sotto-caratteristiche.

**Fail safe** misura il grado in cui un prodotto può automaticamente posizionarsi in una modalità operativa sicura, o tornare a una condizione sicura in caso di guasto. Un impianto medico dovrebbe tornare a una configurazione sicura se perde potenza.

**Identificazione del rischio** misura il grado in cui un prodotto può identificare un corso di eventi o operazioni che può portare a un rischio inaccettabile. Un sistema dovrebbe avvertire se sta accadendo qualcosa di pericoloso.

**Avviso di pericolo** misura il grado in cui un sistema fornisce avvisi dei rischi inaccettabili alle operazioni o ai controlli interni, in modo che possano reagire in tempo sufficiente. Se una situazione pericolosa è imminente, il sistema deve darne avviso in tempo.

## Qualità nell'Uso (Quality-in-Use)

Oltre alla qualità del prodotto misurata in laboratorio, è fondamentale considerare come il software si comporta quando realmente utilizzato dalle persone in contesti reali. Il modello Quality-in-Use è composto da tre caratteristiche che possono influenzare gli stakeholder quando i prodotti o i sistemi sono utilizzati in un contesto d'uso specificato. Esso misura il grado in cui un prodotto o sistema può essere utilizzato da utenti specifici per soddisfare i loro bisogni e raggiungere obiettivi specifici con efficacia, efficienza, libertà dal rischio e soddisfazione in contesti d'uso specifici.

### Usability (Usabilità)

L'usabilità misura l'estensione in cui gli utenti possono raggiungere i loro obiettivi efficientemente e soddisfacentemente utilizzando il sistema. Questa caratteristica si articola in tre sotto-caratteristiche.

**Efficacia** misura quanto bene gli utenti possono completare i loro compiti previsti utilizzando il sistema. Un utente dovrebbe riuscire a fare quello che vuole fare.

**Efficienza** riguarda le risorse (ad esempio tempo, sforzo) richieste per realizzare i compiti. Anche se efficace, un sistema potrebbe richiedere troppo tempo per essere pratico.

**Soddisfazione** riguarda il comfort dell'utente e l'esperienza positiva mentre utilizza il sistema. L'utente dovrebbe sentirsi bene nell'usare il sistema, non frustrato o confuso.

### Safety in Use (Sicurezza nell'Uso)

La sicurezza nell'uso valuta la capacità del sistema di prevenire danno o nocumento a persone, ambiente e interessi commerciali. Questa caratteristica si articola in quattro sotto-caratteristiche.

**Danno commerciale** valuta quanto bene il sistema previene perdite finanziarie o danni al business. Un'applicazione di e-commerce che va in crash durante una transazione causa danni finanziari.

**Salute e sicurezza dell'operatore** riguarda quanto bene il sistema protegge gli utenti da rischi per la salute o pericoli per la sicurezza mentre lo operano. Un'interfaccia ben progettata riduce l'affaticamento e i problemi ergonomici.

**Salute e sicurezza pubblica** riguarda la prevenzione di rischi o danni al pubblico generale attraverso l'uso o l'operazione del sistema. Un software per controllare un'auto a guida autonoma deve proteggere i pedoni.

**Danno ambientale** riguarda la capacità del sistema di evitare o minimizzare impatti negativi sull'ambiente. Un'applicazione non dovrebbe consumare risorse computazionali in eccesso causando impatti energetici significativi.

### Flexibility in Use (Flessibilità nell'Uso)

La flessibilità nell'uso si riferisce alla capacità del sistema di adeguarsi e operare efficacemente in diversi contesti o ambienti. Questa caratteristica si articola in tre sotto-caratteristiche.

**Conformità al contesto** riguarda la capacità del sistema di adattarsi ai requisiti e ai vincoli specifici di diversi contesti. Uno strumento didattico dovrebbe funzionare per insegnanti con differenti stili pedagogici.

**Estensibilità del contesto** riguarda il potenziale del sistema di espandersi o adeguarsi a nuovi o mutevoli ambienti senza modifiche significative. Un'applicazione dovrebbe essere utile in nuovi scenari d'uso non previsti inizialmente.

**Accessibilità** riguarda quanto efficacemente il sistema può essere utilizzato da tutti, incluse le persone con disabilità, in ambienti diversi. L'accesso deve essere garantito indipendentemente dalle capacità fisiche o cognitive dell'utente.

## Misurazione della Qualità Software

### Valutazione degli Attributi di Qualità

Un attributo di qualità identifica una preoccupazione specifica, come l'efficienza prestazionale o la manutenibilità. Per valutarlo rigorosamente, occorrono elementi specifici.

**Un obiettivo di valutazione** risponde alla domanda: quale decisione dobbiamo prendere? Il contesto aziendale o tecnico determina cosa valutare e perché.

**Una misura** specifica quale proprietà osserveremo e come. Non si può valutare una qualità senza sapere come misurarla concretamente.

**Un contesto** definisce i compiti, gli utenti, il carico di lavoro e l'ambiente. La stessa applicazione potrebbe avere prestazioni diverse con 10 vs. 10.000 utenti.

**Un criterio di accettazione** stabilisce quali risultati considereremo accettabili. Prima di misurare, bisogna concordare cosa significhi "buono abbastanza".

**Evidenza** consiste in osservazioni raccolte utilizzando una procedura documentata. Le misure devono essere riproducibili e verificabili.

È fondamentale riconoscere che la misurazione produce un risultato numerico, mentre la valutazione interpreta quel risultato rispetto ai criteri concordati. Per questo motivo è cruciale concordare i criteri prima di raccogliere i risultati, non dopo.

>[!example] 
>### Esempio Concreto: Performance della Ricerca di Aule
> 
> Consideriamo un caso pratico per illustrare il processo di valutazione.
> 
> #### Bisogno dello Stakeholder
> Gli studenti dovrebbero trovare aule disponibili senza un'attesa eccessiva. Questo è il bisogno originario che guida la valutazione.
> 
> #### Condizioni di Valutazione
> Si stabiliscono le condizioni sperimentali con precisione: 1.000 record di aule e 100 utenti simulati contemporaneamente. Si esegue un carico di ricerca fisso su una configurazione di riferimento documentata. La misurazione dura 10 minuti dopo un riscaldamento iniziale di 2 minuti.
> 
> #### Criteri di Accettazione
> Almeno il 95% delle richieste di ricerca valide deve restituire risultati corretti entro 2 secondi. Al massimo lo 0.1% delle richieste di ricerca valide può fallire. Il tempo trascorso viene misurato al client di test, dal momento dell'invio della richiesta al ricevimento della risposta completa. Errori, risposte non corrette e timeout contano come fallimenti e non possono essere conteggiati come risposte rapide e corrette.
> 
> #### Risultati e Interpretazione
> Su 2.000 richieste totali: 1.940 risposte corrette entro 2 secondi, 50 risposte corrette dopo 2 secondi, 10 richieste fallite. La percentuale di risposte tempestive corrette è 1.940 / 2.000 = 97%, che supera il criterio di almeno il 95%. Tuttavia, le richieste fallite sono 10 / 2.000 = 0.5%, che non soddisfa il criterio di al massimo lo 0.1%. La versione testata non soddisfa i criteri combinati di accettazione. Si deve investigare le cause dei fallimenti, implementare miglioramenti e ripetere la valutazione in condizioni comparabili. È importante notare che questi risultati descrivono questa versione specifica del software nelle condizioni testate, non il comportamento in tutti gli scenari possibili.

### Evidenza e Limiti della Valutazione

Diversi aspetti di qualità richiedono diverse forme di evidenza. La manutenibilità può essere valutata tramite analisi delle dipendenze, revisioni della progettazione e lo sforzo richiesto per realizzare compiti di cambiamento definiti. L'affidabilità richiede osservazioni di fallimento, test di interruzione e risultati di recupero. L'usabilità si valuta misurando il completamento dei compiti, il tempo impiegato e la soddisfazione di utenti rappresentativi.

Nella interpretazione dell'evidenza è fondamentale ricordare che una misura solitamente cattura solo una parte di un attributo. I risultati dipendono dalla procedura di valutazione e dal contesto specifico, per cui ripetere le misurazioni aiuta a rivelare la variabilità. Un'elevata copertura di test da sola non stabilisce la correttezza del codice. Una valutazione di qualità dovrebbe segnalare i criteri, i risultati e i limiti insieme alla decisione che supportano, fornendo così una visione realistica dello stato della qualità.