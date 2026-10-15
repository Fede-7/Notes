# Lezione 2-3 Software Processes and Software Quality

## La disciplina in una definizione

> [!quote] IEEE Standard Glossary
> «Software Engineering is the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software»

La disciplina è anche descritta come state of the art dello sviluppare software di qualità in tempo e entro budget (Bruegge e Dutoit).

## Il modello a cascata

Il modello a cascata deriva dai modelli di processo ingegneristici usati nell'ingegneria di grandi sistemi militari.

- Il processo consiste in fasi **sequenziali**, in un processo **plan-driven** (guidato dal piano).
- Il risultato di ogni fase è un documento approvato (**signed-off**).
- La fase successiva non può iniziare finché il risultato della fase precedente non è completo.

### Limiti del modello

L'approccio rigido e **feed-forward** ha senso per l'ingegneria hardware, dove i costi di produzione sono alti; per lo sviluppo software è troppo rigido.

- Le fasi possono sovrapporsi e alimentarsi di informazione: durante il system design possono emergere problemi nei requisiti, durante l'implementazione problemi nel design.
- I requisiti possono cambiare durante lo sviluppo.

## Le fasi del modello a cascata

### Requirements Engineering

L'obiettivo è capire cosa il software da sviluppare deve fare, non come implementarlo.

- Richiede un'analisi accurata dei bisogni dell'utente e del dominio del problema.
- Coinvolgono clienti, utenti finali e ingegneri del software.
- L'output principale è un **documento di specifica dei requisiti** (Software Requirements Specification).

### System e software/UI design

L'obiettivo è progettare una struttura (architettura) adeguata per il software, su due livelli diversi.

- **System design**: architettura complessiva del sistema; scomposizione in moduli e componenti; allocazione delle funzionalità ai moduli e dei moduli ai componenti hardware; definizione di relazioni e collaborazioni tra moduli.
- **Software e UI design**: dettagli di come implementare ogni modulo; architettura software di basso livello (ad es. quali classi serviranno); prototipazione della interfaccia utente.

L'output è un insieme di specifiche di design, spesso formalizzate con linguaggi di design come UML.

### Implementation

L'obiettivo è «tradurre» le specifiche di design in un linguaggio o tecnologia scelti: non una traduzione qualunque, ma di alta qualità. Il codice risultante deve essere:

- **leggibile** e **manutenibile**;
- **riusabile** ed **estendibile**;
- **testabile**;
- in una sola parola, **clean**.

### Verification e Validation

Dopo l'implementazione occorre chiedersi se soddisfa i bisogni degli utenti: qui entrano verifica e validazione.

> [!def] Verifica
> **Controllo** che il sistema sia conforme alla propria specifica: "have we built the thing right?". Tipicamente fatta con il testing del programma: esecuzione del software in ambiente controllato e controllo che il comportamento sia corretto rispetto alle specifiche.

Accanto alla conformità alla specifica si controlla la conformità ai bisogni del cliente.

> [!def] Validazione
> **Controllo** che il sistema soddisfi le aspettative dei clienti: "have we built the right thing?". Tipicamente fatta definendo ed eseguendo acceptance test.

### Operation and Maintenance

- **Operation**: il sistema viene distribuito e installato per i clienti e messo in uso effettivo.
- **Maintenance**: il software cambierà a un certo punto: i bisogni del cliente possono cambiare, il contesto d'uso può cambiare (es. una nuova legge che richiede procedure diverse) ed emergono bug sfuggiti alla fase di V&V.

## La qualità del software

La qualità del prodotto è un concetto complesso e non univoco: giudizi diversi (efficienza, sicurezza, stabilità, usabilità) possono dare valutazioni diverse dello stesso prodotto. Lo standard **ISO/IEC 25002** definisce i modelli di qualità del software.

- **Product Quality Model**: 9 caratteristiche, ulteriormente suddivise in sotto-caratteristiche, relative alle proprietà di qualità dei prodotti; forniscono un modello di riferimento per specificare, misurare e valutare la qualità dei prodotti.
- **Quality-in-use Model**: 3 caratteristiche, ulteriormente suddivise in sotto-caratteristiche, che influenzano gli stakeholder quando i prodotti sono usati in un contesto d'uso specificato.

## Qualità del prodotto (ISO 25002)

### Functional Suitability

Grado in cui un componente o sistema fornisce funzioni che soddisfano bisogni espliciti e impliciti quando usato in condizioni specificate.

- **Functional completeness**: grado di copertura di tutti i task e obiettivi specificati.
- **Functional correctness**: grado di risultati accurati con gli utenti previsti.
- **Functional appropriateness**: grado in cui le funzioni facilitano il compimento di task e obiettivi specificati.

### Reliability

Grado in cui il sistema esegue le sue funzioni in condizioni specificate per un periodo di tempo specificato.

- **Faultlessness**: grado di esecuzione senza guasti in operazione normale.
- **Availability**: grado di essere operativo e accessibile quando richiesto.
- **Fault tolerance**: grado di operare come previsto nonostante guasti hardware o software.
- **Recoverability**: grado di ripristino dopo un'interruzione o un guasto.

### Performance Efficiency

Grado di esecuzione delle funzioni entro vincoli di risorse specificati, usando le risorse (CPU, memoria, storage, energia) in modo efficiente.

- **Time behaviour**: grado di soddisfare requisiti su tempi di risposta e throughput.
- **Resource utilization**: grado di soddisfare requisiti su quantità e tipi di risorse usate.
- **Capacity**: grado di soddisfare requisiti sui limiti massimi dei parametri.

### Usability

Grado con cui un prodotto può essere interagito dai suoi utenti. L'usabilità può fare la differenza tra successo e fallimento di un prodotto, e persino tra vita e morte.

- **Recognizability**: grado in cui gli utenti riconoscono se il sistema è adatto ai loro bisogni.
- **Learnability**: grado in cui le funzioni possono essere imparate da utenti specificati entro un tempo specificato.
- **Operability**: grado in cui il sistema è facile da operare e controllare.
- **User error protection**: grado in cui il sistema previene gli errori.
- **Inclusivity**: grado in cui il sistema è usabile da persone di background diversi (età, abilità, culture, lingue, generi, condizioni economiche).

### Security

Grado di difesa da attacchi di attori malevoli e di protezione di informazioni e dati con meccanismi di autorizzazione adeguati.

- **Confidentiality**: grado di rendere i dati accessibili solo a chi è autorizzato.
- **Integrity**: grado di proteggere stato e dati da modifiche o cancellazioni non autorizzate.
- **Non-repudiation**: grado di provare che azioni o eventi hanno avuto luogo, così che non possano essere ripudiate.
- **Accountability**: grado di tracciare univocamente le azioni di un'entità a quell'entità.
- **Authenticity**: grado di provare che l'identità di un soggetto o risorsa è quella dichiarata.

### Compatibility

Grado in cui un sistema può scambiare informazioni con altri prodotti o componenti e/o eseguire le sue funzioni condividendo lo stesso ambiente e le stesse risorse di altri sistemi.

- **Co-existence**: grado di eseguire le funzioni richieste condividendo ambiente e risorse con altri prodotti senza impatti dannosi.
- **Interoperability**: grado di scambiare informazioni con altri prodotti e usare reciprocamente le informazioni scambiate.

### Maintainability

Grado di efficacia ed efficienza con cui un prodotto può essere modificato per migliorarlo, correggerlo o adattarlo a cambiamenti di ambiente e requisiti.

- **Modularity**: grado di composizione in componenti discreti, così che una modifica a un componente abbia impatto minimo sugli altri.
- **Reusability**: grado con cui un software o modulo può essere usato come asset in più di un sistema.
- **Modifiability**: grado di modifica efficace ed efficiente senza introdurre difetti o degradare la qualità.
- **Testability**: grado con cui si possono stabilire criteri di test ed eseguire test per verificarli.

### Flexibility

Grado con cui un prodotto può essere adattato a cambiamenti nei requisiti, nei contesti d'uso o nell'ambiente operativo.

- **Adaptability**: grado di adattamento o trasferimento efficace ed efficiente a diversi ambienti hardware, software o operativi.
- **Scalability**: grado di gestire carichi crescenti o decrescenti o adattare la capacità alla variabilità.
- **Installability**: grado di efficacia ed efficienza di installazione e/o disinstallazione.
- **Replaceability**: grado con cui un prodotto può sostituire un altro prodotto specificato per lo stesso scopo nello stesso ambiente.

### Safety

Grado con cui un prodotto evita uno stato in cui vita, salute, proprietà o ambiente sono messi in pericolo.

- **Fail safe**: grado di porsi automaticamente in modalità operativa sicura o di tornare a una condizione sicura in caso di guasto.
- **Risk identification**: grado di identificare corsi di eventi o operazioni che portano a rischi inaccettabili.
- **Hazard warning**: grado di fornire avvisi di rischi inaccettabili in tempo utile perché si possa reagire.

## Qualità nell'uso (Quality-in-use Model)

La qualità nell'uso misura il grado con cui un prodotto può essere usato da utenti specifici per raggiungere obiettivi specifici con efficacia, efficienza, libertà da rischi e soddisfazione in contesti d'uso specifici.

### Usability (quality-in-use)

Misura fino a che punto gli utenti raggiungono i loro obietivi in modo efficiente e soddisfacente usando il sistema.

- **Effectiveness**: quanto bene gli utenti completano i task previsti con il sistema.
- **Efficiency**: le risorse (tempo, sforzo) richieste per portare a termine i task.
- **Satisfaction**: comfort ed esperienza positiva dell'utente nell'uso del sistema.

### Safety (quality-in-use)

Valuta la capacità del sistema di prevenire danni a persone, ambiente e interessi commerciali.

- **Commercial damage**: quanto bene il sistema previene perdite finanziarie o danni al business.
- **Operator health and safety**: quanto bene protegge gli operatori da rischi per la salute e per la sicurezza.
- **Public health and safety**: prevenzione di rischi o danni al pubblico tramite l'uso del sistema.
- **Environmental harm**: il sistema deve evitare o minimizzare impatti negativi sull'ambiente.

### Flexibility (quality-in-use)

Riferita alla capacità del sistema di adattarsi e operare efficacemente in contesti o ambienti diversi.

- **Context conformity**: capacità di adattarsi a requisiti e vincoli di contesti diversi.
- **Context extensibility**: potenziale di espansione o adattamento ad ambienti nuovi o in cambiamento senza modifiche significative.
- **Accessibility**: quanto efficacemente il sistema è usabile da tutte le persone, incluse quelle con disabilità, in ambienti diversi.