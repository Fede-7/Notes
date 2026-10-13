# Lezione 1 e 2 — Processi Software e Qualità del Software

L'ingegneria del software si occupa della **qualità del prodotto software lungo tutto il suo ciclo di vita**. Lo studio dei processi software non parte dai modelli di processo: prima si analizzano le attività che essi organizzano, poiché è solo comprendendo le singole attività che si può capire come esse vengano coordinate in modi diversi.

## Le attività del ciclo di vita del software

Un **processo software** è un insieme di attività correlate che porta alla produzione di un sistema software. Non esiste un processo universale che funziona sempre: esistono molti processi diversi, tutti ugualmente validi a seconda del contesto. Tutti questi processi, però, includono in qualche forma le stesse **attività fondamentali**, ed è per questo che possiamo studiarle in modo generale prima di affrontare i modelli di processo.

Le quattro attività fondamentali sono:

- La **specifica del software** comprende i bisogni degli stakeholder e definisce il comportamento richiesto e i vincoli.
- Lo **sviluppo del software** progetta e implementa una soluzione che risponde a quei bisogni.
- La **validazione del software** valuta se la soluzione supporta l'uso previsto.
- L'**evoluzione del software** adatta il software al mutare di bisogni, dipendenze e condizioni operative.

Queste attività sono complesse e comprendono molte sotto-attività. Come ogni processo creativo, un processo software si basa su **persone** che prendono **decisioni** e **giudizi**, e include tipicamente anche attività aggiuntive come la **pianificazione** e il **monitoraggio del progetto**.

### Il software non è mai davvero finito

Lo sviluppo iniziale costituisce solo una parte del ciclo di vita del software. Requisiti, piattaforme, dipendenze e minacce cambiano continuamente, quindi il software deve essere costantemente manutenuto, adattato e fatto evolvere. Ne deriva che **progettare per il cambiamento è un problema centrale dell'ingegneria del software**, non un aspetto marginale.

### Stesse attività, organizzazioni diverse

Un processo software definisce **come attività, ruoli e artefatti vengono organizzati e coordinati**. Le attività fondamentali sono sempre le stesse; ciò che cambia da processo a processo è il modo di organizzarle. Per questo motivo le si studia prima singolarmente e i diversi modi di organizzarle in processi completi si vedono alla fine del corso.

## Le attività in dettaglio

### Ingegneria dei requisiti

L'obiettivo è comprendere i bisogni degli stakeholder e definire ciò che il software deve realizzare, inclusi i requisiti di qualità e i vincoli. Il lavoro consiste nell'elicitare e analizzare i bisogni insieme agli stakeholder, per poi registrarli con forme adeguate come specifiche, casi d'uso o user story; a questo punto si definiscono i criteri di accettazione e si risolvono le ambiguità. Poiché i requisiti cambiano nel tempo, è necessario mantenere i legami tra requisiti, decisioni di progetto e test man mano che evolvono.

I requisiti vengono raccolti tramite interviste con gli stakeholder, personas, storie e scenari; vengono specificati usando casi d'uso, linguaggio naturale, modelli di dominio e mock-up.

### Progettazione del software e architettura

L'obiettivo è progettare una **struttura adeguata (architettura)** del software, che supporti il comportamento richiesto e gli attributi di qualità. L'architettura individua i componenti principali, le loro responsabilità e le loro interazioni, mentre la progettazione dettagliata definisce interfacce, classi e le relative collaborazioni. La progettazione della UI e i prototipi servono a valutare l'interazione con gli utenti.

Le decisioni di progetto comportano sempre **compromessi (trade-off)**: ad esempio, puntare sulle prestazioni può sacrificare la modificabilità. Poiché ogni decisione ha una motivazione, modelli e record delle decisioni spiegano la soluzione e la sua ratio; UML supporta viste selezionate del progetto.

La progettazione si articola su due livelli:

- Nella **progettazione di sistema** i requisiti vengono allocati a sotto-sistemi software e i sotto-sistemi a risorse hardware, usando pattern architetturali.
- Nella **progettazione software e della UI** si definiscono gli oggetti necessari a realizzare ogni sotto-sistema, usando design pattern, usability engineering e wireframing ad alta fedeltà.

### Implementazione

L'obiettivo è **costruire software funzionante**, raffinando e verificando le decisioni di progetto. Si implementa il comportamento richiesto gestendo gli errori esplicitamente, e si scrive codice che altri sviluppatori possano comprendere, testare e modificare. Tramite code review e analisi statica si esamina l'implementazione, mentre build e test di regressione vengono automatizzati.

Le linee guida del Clean Code sono **euristiche** da valutare nel contesto, non regole assolute. Un punto critico attuale: gli sviluppatori restano responsabili della revisione e della validazione dei contributi assistiti dall'IA, anche quando il codice viene generato automaticamente.

### Verifica e validazione (V&V)

La domanda alla base della V&V è: gli artefatti sviluppati soddisfano davvero i bisogni degli utenti? Si distinguono due attività complementari. La **verifica** chiede se il sistema è conforme alla sua specifica — cioè "abbiamo costruito la cosa giusta *nel modo giusto*?" — e si fa tipicamente con il testing del programma, eseguendo il software in un ambiente controllato e verificando che il comportamento sia corretto rispetto alle specifiche. La **validazione** chiede invece se il sistema soddisfa le aspettative dei clienti — "abbiamo costruito la cosa giusta?" — e si fa tipicamente definendo ed eseguendo test di accettazione.

La V&V si applica anche a requisiti e progettazione, non solo al software eseguibile, e continua durante l'evoluzione del sistema. I test di accettazione contribuiscono alla validazione, ma con una precisazione importante: superare una suite di test fornisce **evidenze solo nell'ambito di quei test**, non una garanzia generale.

### Rilascio, esercizio ed evoluzione

Il **rilascio** prepara e mette il software nel suo ambiente di destinazione, mentre l'**esercizio** mantiene il servizio disponibile e fornisce evidenze sul comportamento in uso. La **manutenzione** corregge i difetti e adatta il software a bisogni, dipendenze e ambienti in cambiamento: serve sia a riparare errori non scoperti nelle fasi precedenti, sia ad adattare il software a cambiamenti nei requisiti o nell'ambiente. Poiché ogni cambiamento comporta rischi, controlli automatici di rilascio e procedure di ripristino aiutano a gestirli.

Nel corso si introdurranno CI/CD, osservabilità e le pratiche a supporto dell'evoluzione; questi temi sono approfonditi nel corso magistrale di Software Project Management and Evolution.

### Testing

Il testing serve a garantire che il software soddisfi i clienti e comprende: ispezioni del codice, test funzionali (di unità, di integrazione, di sistema) e test di usabilità.

## La qualità del software

### Che cosa si intende per qualità

La qualità di un prodotto riguarda diverse proprietà la cui importanza dipende dall'uso previsto, e questo vale per qualsiasi prodotto, non solo per il software:

- Un'**automobile** è di qualità se si guasta raramente, consuma poco e ha bassi costi di manutenzione.
- Un **orologio** è di qualità se è molto preciso, resistente ad acqua e polvere e resistente ai graffi.
- Delle **parti meccaniche** sono di qualità se hanno basse tolleranze, aderiscono alle specifiche e resistono all'usura.

Per il software la questione è più sfumata, come mostrano tre esempi classici.

#### L'inverse square root di Quake III Arena

Il codice seguente è l'implementazione dell'**inverse square root** attribuita a John Carmack:

```c
float Q_rsqrt(float number){
    long i;
    float x2, y;
    const float threehalfs = 1.5F;

    x2 = number * 0.5F;
    y = number;
    i = * ( long * ) &y;
    i = 0x5f3759df - ( i >> 1 );
    y = * ( float * ) &i;
    y = y * ( threehalfs - ( x2 * y * y ) );

    return y;
}
```

L'inverse square root (1/√x) è molto usato in computer grafica, ad esempio per calcolare gli angoli di incidenza e riflessione. L'approssimazione di Carmack era circa 4 volte più veloce di `(float)(1.0/sqrt(x))`, e molti la considerano un esempio di grande programmazione. Ma il codice è quasi illeggibile: riuscire a capire come funziona è tutt'altro che immediato. Ne deriva la domanda: **essere efficienti è alta qualità?**

#### OpenBSD e Vim

Alcuni considerano **OpenBSD** software di alta qualità perché è un sistema operativo molto stabile e comparativamente difficile da violare — ma allora **essere molto sicuri contro gli attaccanti è alta qualità?** Analogamente, **Vim** è considerato da molti il miglior editor di testo: gli esperti lavorano estremamente veloce con esso, quindi sarebbe software di alta qualità; altri però dicono che è troppo difficile da imparare, e quindi di bassa qualità. La conclusione è che **non esiste «una sola qualità»**, ma molti approcci e punti di vista diversi.

### I modelli di qualità

Un **modello di qualità** offre agli stakeholder un **vocabolario condiviso** per discutere requisiti e valutazione. Le priorità e i criteri di valutazione rilevanti dipendono dal prodotto e dai suoi stakeholder. Gli standard di riferimento sono tre:

- **ISO/IEC 25010:2023** descrive la qualità del prodotto attraverso nove caratteristiche.
- **ISO/IEC 25019:2023** tratta la qualità in uso (*quality in use*).
- **ISO/IEC 25002:2024** illustra il framework e l'uso dei modelli di qualità.

### Le tre prospettive sulla qualità

La qualità del software si può osservare da tre prospettive distinte. La **qualità interna** riguarda le proprietà esaminate senza eseguire il software, come le dipendenze e la struttura del codice. La **qualità esterna** riguarda le proprietà osservate durante l'esecuzione, come il tempo di risposta e il comportamento in caso di guasto. La **qualità in uso** riguarda i risultati per le persone e le organizzazioni che usano il sistema in un contesto specificato.

Le pratiche di processo aiutano a raggiungere e valutare la qualità, ma la loro adozione da sola non basta: deve essere accompagnata da **evidenze sul prodotto e sul suo uso**.

## ISO/IEC 25010:2023 — Qualità del prodotto

Lo standard descrive la qualità del prodotto attraverso **nove caratteristiche**, ciascuna ulteriormente suddivisa in sotto-caratteristiche.

### Adeguatezza funzionale

La **Functional Suitability** è il grado in cui un componente o sistema fornisce funzioni che soddisfano bisogni espliciti e impliciti in condizioni specificate. Si compone di tre sotto-caratteristiche:

- La **completezza funzionale** misura quanto le funzioni fornite coprono tutti i compiti e gli obiettivi utente specificati.
- La **correttezza funzionale** misura quanto il prodotto fornisce risultati accurati quando usato dagli utenti previsti.
- L'**appropriatezza funzionale** misura quanto le funzioni facilitano il raggiungimento dei compiti e degli obiettivi specificati.

Un esempio: un sistema di prenotazione aule deve supportare la cancellazione, applicare correttamente le regole di prenotazione e aiutare gli utenti a trovare un'aula adatta.

### Affidabilità

La **Reliability** è il grado in cui il sistema svolge le sue funzioni in condizioni specificate per un periodo di tempo specificato. Le sue sotto-caratteristiche sono:

- L'**assenza di guasti** (*Faultlessness*) misura quanto il sistema svolge le funzioni specificate senza guasti nel funzionamento normale.
- La **disponibilità** (*Availability*) misura quanto il sistema è operativo e accessibile quando richiesto.
- La **tolleranza ai guasti** (*Fault tolerance*) misura quanto il sistema opera come previsto nonostante la presenza di guasti hardware o software.
- La **ripristinabilità** (*Recoverability*) riguarda il ripristino dei dati affetti e il ritorno allo stato operativo richiesto dopo un'interruzione o un guasto.

### Efficienza prestazionale

La **Performance Efficiency** riguarda tempi di risposta, throughput e uso delle risorse in condizioni operative specificate. Si articola in:

- Il **comportamento temporale** (*Time behaviour*) misura quanto tempi di risposta e throughput soddisfano i requisiti.
- L'**utilizzo delle risorse** (*Resource utilization*) misura quanto quantità e tipi di risorse usate soddisfano i requisiti.
- La **capacità** (*Capacity*) misura quanto i limiti massimi dei parametri del sistema soddisfano i requisiti.

### Capacità di interazione

L'**Interaction Capability** riguarda le caratteristiche del prodotto che supportano gli utenti nell'interagire con il sistema per completare i compiti. Include, tra le altre, le seguenti sotto-caratteristiche:

- La **riconoscibilità** (*Recognizability*) misura quanto gli utenti possono riconoscere se il sistema è adatto ai loro bisogni.
- L'**apprendibilità** (*Learnability*) misura quanto le funzioni possono essere apprese da utenti specificati entro un tempo specificato.
- L'**operabilità** (*Operability*) misura quanto il prodotto è facile da usare e controllare.
- La **protezione dagli errori utente** (*User error protection*) misura quanto il sistema previene gli errori.
- L'**inclusività** (*Inclusivity*) misura quanto il sistema può essere usato da persone di contesti diversi: età, abilità, culture, etnie, lingue, generi, situazioni economiche, ecc.

### Sicurezza informatica

La **Security** è il grado in cui un sistema si difende da attacchi di attori malevoli e protegge informazioni e dati applicando adeguati meccanismi di autorizzazione. Le sue sotto-caratteristiche principali sono:

- La **riservatezza** (*Confidentiality*) misura quanto i dati sono accessibili solo a chi è autorizzato.
- L'**integrità** (*Integrity*) misura quanto stato e dati sono protetti da modifiche o cancellazioni non autorizzate.
- La **non ripudiabilità** (*Non-repudiation*) misura quanto azioni o eventi possono essere provati, così da non poter essere negati in seguito.
- L'**accountability** misura quanto le azioni di un'entità possono essere ricondotte univocamente a essa.
- L'**autenticità** (*Authenticity*) misura quanto l'identità di un soggetto o risorsa può essere provata come quella dichiarata.

### Compatibilità

La **Compatibility** è il grado in cui un sistema può scambiare informazioni con altri prodotti, sistemi o componenti e/o svolgere le sue funzioni condividendo lo stesso ambiente e le stesse risorse comuni con altri sistemi. Si compone di:

- La **co-esistenza** (*Co-existence*) misura quanto un prodotto svolge le sue funzioni in modo efficiente condividendo ambiente e risorse con altri prodotti, senza impatti dannosi su questi ultimi.
- L'**interoperabilità** (*Interoperability*) misura quanto un sistema può scambiare informazioni con altri prodotti e usare reciprocamente le informazioni scambiate.

### Manutenibilità

La **Maintainability** è il grado di efficacia ed efficienza con cui un prodotto può essere modificato per migliorarlo, correggerlo o adattarlo a cambiamenti di ambiente e requisiti. Le sue sotto-caratteristiche riguardano altrettanti obiettivi di progetto:

- La **modularità** (*Modularity*) limita l'impatto dei cambiamenti tra i componenti.
- Il **riuso** (*Reusability*) permette di usare un asset in più di un sistema.
- L'**analizzabilità** (*Analysability*) permette di comprendere i difetti e valutare l'impatto dei cambiamenti.
- La **modificabilità** (*Modifiability*) permette di effettuare cambiamenti preservando la qualità richiesta.
- La **testabilità** (*Testability*) permette di stabilire criteri e verificare se sono soddisfatti.

### Flessibilità

La **Flexibility** è il grado in cui un prodotto può essere adattato a cambiamenti nei requisiti, nei contesti d'uso o nell'ambiente operativo. Si articola in:

- L'**adattabilità** (*Adaptability*) misura quanto il sistema può essere adattato o trasferito efficacemente a diversi hardware, software o ambienti operativi/d'uso.
- La **scalabilità** (*Scalability*) misura quanto il sistema può gestire carichi crescenti o decrescenti o adattarne la capacità alla variabilità.
- L'**installabilità** (*Installability*) misura l'efficacia e l'efficienza con cui il prodotto può essere installato e/o disinstallato con successo.
- La **sostituibilità** (*Replaceability*) misura quanto il prodotto può sostituire un altro prodotto software specificato per lo stesso scopo nello stesso ambiente.

### Sicurezza (Safety)

La **Safety** è il grado in cui un prodotto evita uno stato in cui sono messe in pericolo vita umana, salute, proprietà o ambiente. Include, tra le altre:

- Il **fail safe** misura quanto il prodotto può porsi automaticamente in una modalità operativa sicura o tornare a una condizione sicura in caso di guasto.
- L'**identificazione dei rischi** (*Risk identification*) misura quanto il prodotto può individuare eventi o operazioni che possono portare a rischi inaccettabili.
- La **segnalazione dei pericoli** (*Hazard warning*) misura quanto il sistema fornisce avvisi su rischi inaccettabili a operazioni o controlli interni, così che possano reagire in tempo utile.

## La qualità in uso

Il **modello di qualità in uso** (ISO/IEC 25019) è composto da **3 caratteristiche**, ulteriormente suddivise in sotto-caratteristiche, che possono influenzare gli stakeholder quando i prodotti sono usati in un contesto d'uso specificato. Misura il grado in cui un prodotto può essere usato da utenti specifici per soddisfare i propri bisogni e raggiungere obiettivi specifici con **efficacia, efficienza, assenza di rischio e soddisfazione** in contesti d'uso specifici.

### Usabilità

L'**Usability** misura in che misura gli utenti possono raggiungere i propri obiettivi in modo efficiente e soddisfacente usando il sistema:

- L'**efficacia** (*Effectiveness*) misura quanto bene gli utenti completano i compiti previsti usando il sistema.
- L'**efficienza** (*Efficiency*) riguarda le risorse richieste, ad esempio tempo e sforzo, per svolgere i compiti.
- La **soddisfazione** (*Satisfaction*) riguarda il comfort e l'esperienza positiva dell'utente durante l'uso del sistema.

### Sicurezza

La **Safety** valuta la capacità del sistema di prevenire danni a persone, ambiente e interessi commerciali:

- Il **danno commerciale** (*Commercial Damage*) valuta quanto il sistema previene perdite finanziarie o danni all'attività.
- La **salute e sicurezza degli operatori** (*Operator Health and Safety*) misura quanto il sistema protegge gli utenti da rischi per la salute o per la sicurezza durante l'uso.
- La **salute e sicurezza pubblica** (*Public Health and Safety*) riguarda la prevenzione di rischi o danni per il pubblico generale dall'uso o dall'esercizio del sistema.
- Il **danno ambientale** (*Environmental Harm*) riguarda la capacità del sistema di evitare o minimizzare gli impatti negativi sull'ambiente.

### Flessibilità

La **Flexibility** riguarda la capacità del sistema di adattarsi e operare efficacemente in contesti o ambienti diversi:

- La **conformità al contesto** (*Context Conformity*) è la capacità del sistema di adattarsi ai requisiti e ai vincoli specifici di contesti diversi.
- L'**estensibilità di contesto** (*Context Extensibility*) è il potenziale del sistema di espandersi o adattarsi a ambienti nuovi o in cambiamento senza modifiche significative.
- L'**accessibilità** (*Accessibility*) misura quanto efficacemente il sistema può essere usato da tutte le persone, incluse quelle con disabilità, in ambienti diversificati.

## Misurare la qualità del software

### Valutare un attributo di qualità

Un attributo di qualità individua una **preoccupazione** (*concern*), come l'efficienza prestazionale o la manutenibilità, ma non è ancora una misura. Per valutarlo servono cinque elementi: un **obiettivo di valutazione** (quale decisione dobbiamo prendere), una **misura** (quale proprietà osserveremo e come), un **contesto** (quali compiti, utenti, carico di lavoro e ambiente), un **criterio di accettazione** (quali risultati considereremo accettabili) e le **evidenze** (le osservazioni raccolte con una procedura documentata).

La distinzione fondamentale è che **la misurazione produce un risultato, mentre la valutazione interpreta quel risultato rispetto a criteri concordati**. Ne deriva una regola pratica: i criteri vanno concordati **prima** di raccogliere i risultati, altrimenti l'interpretazione risulta arbitraria.

#### Un requisito di qualità misurabile: prestazioni di ricerca delle aule

Il bisogno degli stakeholder è che gli studenti trovino le aule disponibili senza attese eccessive. Le condizioni di valutazione sono: 1.000 record di aule, 100 utenti simultanei simulati, un carico di ricerca fisso su un setup di riferimento documentato e un periodo di misurazione di 10 minuti dopo un warm-up di 2 minuti.

I criteri di accettazione sono due:

- Almeno il **95% delle richieste di ricerca valide** deve restituire risultati corretti entro **2 secondi**.
- Al massimo lo **0,1% delle richieste valide** può fallire.

Il tempo viene misurato sul client di test, dall'invio della richiesta alla ricezione della risposta completa. Un dettaglio metodologico importante: errori, risposte errate e timeout contano come **fallimenti**, quindi non possono essere contati come risposte rapide andate a buon fine.

#### Risultati della valutazione

I risultati illustrativi di una singola esecuzione del test sono:

| Osservazione | Richieste |
| --- | --- |
| Risposta corretta entro 2 secondi | 1.940 |
| Risposta corretta dopo 2 secondi | 50 |
| Richiesta fallita | 10 |
| **Totale** | **2.000** |

Dai dati si ricava la valutazione. Le risposte riuscite tempestive sono 1.940 su 2.000, cioè il 97%, quindi il criterio ≥95% è soddisfatto. Le richieste fallite sono invece 10 su 2.000, cioè lo 0,5%, quindi il criterio ≤0,1% **non** è soddisfatto. Di conseguenza la versione testata **non soddisfa i criteri di accettazione combinati**: occorre indagare i fallimenti, implementare miglioramenti e ripetere la valutazione in condizioni confrontabili. Questi risultati descrivono questa specifica versione nelle condizioni testate, non il sistema in generale.

### Evidenze e limiti della valutazione

Poiché preoccupazioni di qualità diverse richiedono evidenze diverse, non esiste una misura universale della qualità. Ad esempio:

- La **manutenibilità** si evidenzia tramite analisi delle dipendenze, design review e sforzo richiesto per compiti di cambiamento definiti.
- L'**affidabilità** si evidenzia tramite osservazioni di guasti, test di interruzione e risultati di ripristino.
- L'**usabilità** si evidenzia tramite completamento dei compiti, tempi e soddisfazione con utenti rappresentativi.

Le evidenze vanno interpretate con cautela per quattro motivi: una misura di solito coglie solo una parte di un attributo; i risultati dipendono dalla procedura e dal contesto di valutazione; misure ripetute aiutano a rivelare la variabilità; e una copertura dei test elevata, da sola, **non stabilisce la correttezza**. Per questo motivo una valutazione della qualità dovrebbe sempre riportare criteri, risultati e limiti, insieme alla decisione che essi supportano.