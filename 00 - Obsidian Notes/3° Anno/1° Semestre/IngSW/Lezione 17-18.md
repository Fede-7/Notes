# Lezione 17-18 Design Patterns

## Software Development Lifecycle

La progettazione con i pattern si colloca all'interno del ciclo di vita dello sviluppo software, che va dai requisiti alla manutenzione.

- **Requirements Engineering**: i requisiti si raccolgono con interviste agli stakeholder, storie e scenari, personas; si specificano con use case, linguaggio naturale e modelli di dominio.
- **System Design**: si definisce l'architettura del sistema, allocando i requisiti ai sottosistemi software e i sottosistemi alle risorse hardware (architectural pattern); si definiscono i sottosistemi e i loro oggetti applicando i software design pattern, con l'usability engineering (wireframing ad alta fedeltà, mock-up).
- **Implementation**: ogni sottosistema è implementato con codice sorgente e altri artefatti, seguendo Clean Code, framework e ORM, con attenzione alla qualità del software.
- **Testing**: si garantisce che il software soddisfi i clienti con code inspection, functional testing (unit, integration, system) e usability testing.
- **Operation and Maintenance**: il sistema è messo in uso pratico; la manutenzione serve a correggere errori non scoperti nelle fasi precedenti e ad adattare il software a cambiamenti dei requisiti o del suo ambiente.

## Riuso di codice e riuso di design

Codice e design si riusano per non reinventare la ruota e per sfruttare il lavoro precedente, ma con requisiti diversi.

- **Riuso di codice**: richiede codice pulito, elegante, comprensibile, generale e stabile.
- **Riuso di design**: richiede una comprensione precisa dei design comuni e ricorrenti.

I sistemi object-oriented sfruttano strutture di design ricorrenti che promuovono **astrazione**, **flessibilità**, **modularità** ed **eleganza**, e in esse risiede una preziosa conoscenza di progettazione. Il problema è catturare, comunicare e applicare questa conoscenza per il riuso.

## Che cos'è un design pattern

> [!def] Design pattern
> **Soluzione comune** a un problema ricorrente nella progettazione. Astrae una struttura di design ricorrente, che comprende classi e/o oggetti con le loro dipendenze, strutture, interazioni e convenzioni; la specifica esplicitamente e distilla l'esperienza di progettazione.

Un design pattern ha quattro parti fondamentali: **nome**, **problema**, **soluzione**, **conseguenze e trade-off** della sua applicazione. È inoltre indipendente dal linguaggio e dall'implementazione, ed è una «micro-architettura»: non si applica meccanicamente, perché lo sviluppatore deve tradurre la soluzione in termini concreti nel contesto dell'applicazione.

La storia del concetto si sintetizza in tre tappe.

- L'architetto **Christopher Alexander** introduce l'idea con *A Pattern Language: Towns, Buildings, Construction* (1977).
- La **Gang of Four** (Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides) pubblica *Design Patterns: Elements of Reusable Object-Oriented Software* (1995).
- Seguono molte conferenze, simposi e libri; i cataloghi principali sono quello GoF e **POSA** (*Pattern-Oriented Software Architecture*, Buschmann et al., 1996).

I design pattern sono importanti per quattro ragioni.

- **Codificano il buon design**: distillano e diffondono esperienza, aiutano novizi ed esperti e astraiono come pensare il design.
- **Danno nomi espliciti alle strutture di design**: creano un vocabolario comune, riducono la complessità e aumentano l'espressività.
- **Catturano e preservano le informazioni di design**: articolano le decisioni in modo succinto e migliorano la documentazione.
- **Facilitano il restructuring/refactoring**: i pattern sono interrelati e aggiungono flessibilità.

## Classificazione dei pattern

I pattern si distinguono per complessità, livello di dettaglio e scala di applicabilità, e in ingegneria del software si separano in due livelli.

- **Architectural pattern**: pattern di alto livello il cui ambito è la struttura dell'intero sistema software; possono essere implementati in qualsiasi linguaggio di programmazione. **REST** può essere considerato un architectural pattern.
- **Design pattern** in senso stretto: pattern di medio/basso livello che si applicano alle scelte di progettazione dentro componenti o moduli e risolvono problemi ricorrenti del design e dell'implementazione object-oriented.

In base allo scopo o **intent** si distinguono tre categorie di design pattern.

- **Creazionali**: meccanismi per creare oggetti, con l'obiettivo di aumentare flessibilità, riuso del codice esistente e manutenibilità.
- **Strutturali**: modi di assemblare oggetti e classi in strutture più grandi, mantenendo le strutture flessibili ed efficienti.
- **Comportamentali**: gestione della comunicazione efficace e dell'assegnazione di responsabilità tra oggetti.

La classificazione GoF incrocia scopo e scope (class/object).

| Scope | Creazionali | Strutturali | Comportamentali |
|---|---|---|---|
| Class | Factory Method | Adapter (class) | Interpreter, Template Method |
| Object | Abstract Factory, Builder, Prototype, Singleton | Adapter (object), Bridge, Composite, Decorator, Flyweight, Facade, Proxy | Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Visitor |

## Data Access Object

Il pattern DAO affronta la variabilità dell'accesso ai dati.

- **Problema**: l'accesso ai dati varia molto a seconda del tipo di memorizzazione (DBMS relazionale, DBMS NoSQL, flat file, ecc.) e dell'implementazione del fornitore.
- **Soluzione**: il pattern **Data Access Object (DAO)** astrae e incapsula ogni accesso alla sorgente dati; ogni DAO gestisce la connessione con la sorgente per ottenere e memorizzare dati e implementa il meccanismo di accesso richiesto per lavorare con essa.

![[c944cc784b59d630641c3aa7fe31e7d171b3512b96e24de9a985624293e6dd60.jpg|200]]

Si definisce una classe DAO per ciascuna classe entità, che astrae le operazioni **CRUD** (Create, Retrieve, Update, Delete); i metodi «utili» dipendono dalla classe di dominio e dall'applicazione (per `LocationDao`: `findById`, `findByName`, `find`, `save`, `delete`). I benefici sono tre.

- Permette di «collegare» implementazioni di memorizzazione diverse con impatto minimo sul resto del sistema.
- Disaccoppia il layer di persistenza.
- Favorisce e supporta il riuso del codice.

## Pattern creazionali

### Singleton

L'intento del Singleton è garantire che una classe abbia solo un'istanza e fornire un punto di accesso globale ad essa. Si applica in due casi.

- Quando deve esistere esattamente una istanza di una classe, accessibile da un punto di accesso ben noto.
- Quando l'unica istanza deve essere estendibile per sottoclassazione e i client devono poter usare l'istanza estesa senza modificare il proprio codice.

La struttura si realizza con un costruttore privato e un'operazione statica di accesso all'istanza.

```java
public class Singleton {
  private static Singleton istanza = null;
  private Singleton() {}
  public static Singleton getSingleton() {
    if (istanza == null) { istanza = new Singleton(); }
    return istanza;
  }
}
```

Pur usando una sola istanza, modifiche all'operazione di accesso possono permettere un numero variabile di istanze (ad esempio una classe che ammette fino a tre istanze). Le conseguenze dell'applicazione sono le seguenti.

- Riduce l'inquinamento del namespace (namespace pollution).
- Rende facile cambiare idea e permettere più di un'istanza.
- Presenta gli stessi difetti di una variabile globale se usato male.
- L'implementazione può essere meno efficiente di una globale e presenta insidie di concorrenza (concurrency pitfalls).

### Builder

Builder e Factory formano una famiglia di pattern che affronta il problema delle classi complesse per cui il meccanismo object-oriented base dei costruttori non è sufficiente a garantire flessibilità ed efficienza. Lo scopo del Builder è rendere la costruzione di un oggetto flessibile e decomponibile, separandola dal costruttore effettivo dell'oggetto.

Nella soluzione il singolo prodotto (`Product`) è costruito dal `ConcreteBuilder`, mentre la classe `Director` può gestire la costruzione di un insieme di oggetti `Product`.

![[911b6ee3abfc9170b5e8471c5d4ab9ad58831adeb2fc66dc9141c2cdab9180e2.jpg|200]]

Il pattern si usa quando sussistono queste condizioni.

- La creazione di un prodotto complesso deve essere indipendente dalle parti specifiche che lo compongono.
- Il processo di creazione non deve conoscere il processo di assemblaggio (come le parti vengono unite per costituire il prodotto).
- Il processo di creazione deve permettere rappresentazioni diverse per l'oggetto costruito.

Nell'uso tipico il prodotto è separato da un oggetto Builder che gestisce tutte le varianti di costruzione in modo flessibile: i metodi `with...` restituiscono il Builder stesso, così le chiamate si innestano; il metodo `build()` valida e invoca il costruttore package-private del prodotto.

```java
Computer gamingPC = new ComputerBuilder("AMD Ryzen 7", 32)
    .withDedicatedGPU("AMD Radeon RX 7800")
    .withSSD(2000)
    .includeOS()
    .build();
```

La logica di validazione sta nel Builder, non nella classe del prodotto: ad esempio `build()` solleva una `IllegalStateException` se la RAM è inferiore a 4GB, quindi un PC «obsoleto» non viene proprio costruito.

Il pattern è molto usato nelle librerie Java standard: `java.lang.StringBuilder` per costruire stringhe, `java.util.Locale.Builder` per oggetti locale complessi (lingua, paese, script, varianti), `java.time.format.DateTimeFormatterBuilder` per i formatter data-ora. La stessa catena di chiamate fluenti si usa nelle API REST, ad esempio per creare un JWT con `JWT.create().withIssuer(...).withClaim(...).sign(...)` e per costruire la risposta con `Response.status(...).entity(...).build()`.

### Factory Method

L'intento del Factory Method è istanziare oggetti senza esporre al client la logica di creazione, riferendosi all'oggetto appena creato tramite un'interfaccia comune.

La motivazione nasce dai framework: usano classi astratte per definire e mantenere relazioni tra oggetti e devono creare oggetti, ma conoscono solo le classi astratte, che non possono istanziare; il factory method incapsula la conoscenza di quale sottoclasse creare, spostandola fuori dal framework.

Il pattern si applica in due situazioni.

- Quando una classe non può anticipare la classe degli oggetti che deve creare.
- Quando le classi delegano la responsabilità a una di diverse sottoclassi ausiliarie e si vuole localizzare la conoscenza di quale sottoclasse sia la delegata.

I partecipanti sono tre: il **Product** definisce l'interfaccia degli oggetti creati dal factory method, il **ConcreteProduct** implementa l'interfaccia del prodotto, il **Creator** dichiara il factory method che restituisce un oggetto di tipo `Product`.

La fabbrica incapsula la scelta dell'istanza concreta, che dipende da una condizione di contesto.

```java
public class VehicleFactory {
  public Vehicle instantiateVehicle() {
    // logica per scegliere l'istanza
    if (weather.rains()) return new Car();
    else return new Bike();
  }
}
```

La motivazione si vede ripartendo dal system design: se `Traveler` ha un attributo di tipo `Car`, c'è un forte accoppiamento e la classe non è riusabile con altri mezzi né robusta a cambiamenti di `Car`. Dichiarando invece un attributo di tipo `Vehicle` (interfaccia con `move()`) e iniettando il mezzo con `setV(...)`, `Traveler` funziona con qualsiasi implementazione (`Car`, `Bike`).

### Abstract Factory

La motivazione dell'Abstract Factory è l'indipendenza dalle famiglie di prodotti: un toolkit di interfaccia utente deve supportare più standard di look-and-feel (X, Windows Vista, il Finder di MacOS) oppure un sistema di facility management per la casa intelligente deve supportare diversi sistemi di controllo (Instabus di Siemens, Metasys di Johnson & Control, lo standard proprietario Zumtobe). In entrambi i casi si vuole un'unica interfaccia, indipendente dal produttore.

![[91b440200d25efb07e9f331fa15d6d1b9981b7b33f2d0f27ce18dd38d09d5837.jpg|200]]

L'applicabilità del pattern copre quattro esigenze.

- **Indipendenza da inizializzazione o rappresentazione**: il sistema non deve dipendere da come i suoi prodotti sono creati, composti o rappresentati.
- **Indipendenza dal produttore**: il sistema va configurato con una tra molteplici famiglie di prodotti; inoltre si può voler fornire una libreria di classi al cliente senza rivelare quale prodotto particolare si sta usando.
- **Vincoli su prodotti correlati**: una famiglia di prodotti correlati è progettata per essere usata insieme e il vincolo va imposto.
- **Gestione del cambiamento in arrivo**: si usa una particolare famiglia di prodotti ma ci si aspetta che la tecnologia sottostante cambi presto, con nuovi prodotti sul mercato.

Nell'esempio GUI una fabbrica astratta, selezionata leggendo la configurazione, decide quale famiglia di widget istanziare.

```java
abstract class GUIFactory {
  public static GUIFactory getFactory() {
    int sys = readFromConfigFile("OS_TYPE");
    if (sys == 0) return new WinFactory();
    else return new OSXFactory();
  }
  public abstract Button createButton();
}
```

Il client ottiene la factory con `getFactory()`, crea il bottone con `createButton()` e lo usa tramite l'astrazione `Button`, senza mai dipendere dalle classi concrete `WinButton` o `OSXButton`.

## Pattern strutturali

### Adapter

Lo scopo dell'Adapter è convertire l'interfaccia di una classe in un'altra interfaccia attesa dal client, permettendo la cooperazione di classi che altrimenti avrebbero interfacce incompatibili; il sinonimo è Wrapper. La motivazione è riusare una classe esistente e già collaudata la cui interfaccia però non corrisponde a quella richiesta.

I partecipanti sono quattro.

> [!aside]
> - **Client**: la classe che vuole usare il servizio da adattare.
> - **Target**: l'interfaccia che vorremmo avere dal servizio da usare.
> - **Adaptee**: la classe esistente che fornisce il servizio.
> - **Adapter**: la classe che adatta l'interfaccia fornita dall'adaptee all'interfaccia Target.
> 
> ---
> 
> ![[2e8f0a7548183fd9a9d4a40af8089c59b08fdc2d3efe7b024af9889a44ae3181.jpg|200]]

L'Adapter può essere usato in tre casi.

1. Si vuole usare una classe esistente (`Adaptee`) con interfaccia incompatibile.
2. Si vuole creare una classe riusabile che dovrà collaborare con classi non prevedibili al momento della sua creazione.
3. Si vuole riusare un insieme di sottoclassi esistenti, ma adattare l'interfaccia creando una sottoclasse per ciascuna è scomodo: meglio creare un adapter per la classe padre.

L'adapter incapsula l'adaptee e ne converte i parametri verso l'interfaccia richiesta.

```java
public class Adapter implements Target {
  public Adaptee adaptee = new Adaptee();
  public double evaluate(double weight, double height) {
    return adaptee.calcolaIMC(weight / 0.453, height / 0.0254);
  }
}
```

L'uso tipico è con servizi e microservizi: il design del software porta a progettare un'interfaccia; un microservizio esistente fornisce il servizio con la propria interfaccia; si implementa un Adapter che interagisce con il fornitore del servizio, converte i parametri (eventualmente rielaborandoli) e li fornisce al Target, che può essere anch'esso una interfaccia. Non si modifica direttamente l'Adaptee perché se ne possiede solo l'interfaccia o perché è già usato da altri.

#### Adapter di classe e adapter a oggetti

Le due varianti del pattern si distinguono per il legame tra Adapter e Adaptee.

- **Adapter di classe**: utile quando una o più classi esistenti forniscono una parte o tutti i servizi necessari ma non usano l'interfaccia richiesta (es. un lettore audio che suona solo mp3 riusa, tramite `MediaAdapter`, un lettore avanzato capace di suonare vlc e mp4).
- **Adapter a oggetti**: la **delega** lega Adapter e Adaptee, mentre l'**ereditarietà di interfaccia** specifica l'interfaccia della classe Adapter; Target e Adaptee (spesso detta sistema legacy) esistono prima dell'Adapter. È usato spesso per fornire una nuova interfaccia a componenti legacy esistenti (interface engineering, reengineering); ad esempio `ServicesEnumeration` adatta un `RegisteredServices` all'interfaccia `Enumeration` delegando `hasMoreElements()` e `nextElement()`.

### Composite

Lo scopo del Composite è comporre oggetti in strutture ad albero che rappresentano gerarchie tutto-parte, facendo sì che i client trattino allo stesso modo oggetti compositi e oggetti singoli.

I partecipanti sono quattro.

> [!aside]
> - **Component**: dichiara l'interfaccia degli oggetti e il comportamento di default, e un'interfaccia per accedere e gestire i componenti figli.
> - **Leaf**: implementa gli oggetti component senza figli e il loro comportamento.
> - **Composite**: definisce il comportamento dei componenti con figli, memorizza i componenti figli e implementa le operazioni sui figli dichiarate dall'interfaccia Component.
> - **Client**: usa gli oggetti compositi tramite l'interfaccia Component.
> 
> ---
> 
> ![[4b0a672dc61ede824b2b4e5cea9a5898695237d97cb65cc26c08a89b2a1c2b95.jpg|200]]

Il caso tipico è un file system, dove una `Directory` può contenere `File` e altre directory (anche vuote) e l'operazione `ls()` viene invocata ricorsivamente e polimorficamente sui figli tramite l'interfaccia `AbstractFile`.

```java
class Directory implements AbstractFile {
  public void ls() {
    System.out.println(EsempioComposite.indentazione + nome);
    for (int i = 0; i < listaFile.size(); ++i) {
      AbstractFile obj = (AbstractFile) listaFile.get(i);
      obj.ls(); // polimorfismo
    }
  }
}
```

Le conseguenze dell'applicazione sono le seguenti.

- Permette di definire gerarchie di classi formate da oggetti primitivi e compositi: i primitivi si compongono in oggetti più complessi, componibili ricorsivamente, e dovunque il client si aspetta un primitivo si può usare indifferentemente un composito.
- Semplifica il client: strutture composite e oggetti singoli si usano in modo uniforme, e il client in genere non sa (né deve saperlo) se sta lavorando con una foglia o con un composito.
- È flessibile: è più facile aggiungere nuovi tipi di componenti, perché nuove sottoclassi di Leaf o Composite funzionano automaticamente nelle strutture esistenti con il codice client.
- È spesso usato per istanziare la gerarchia di widget di una GUI.

### Decorator

Il pattern Decorator permette di creare oggetti complessi aggiungendo funzionalità a oggetti più semplici: l'oggetto complesso include quello semplice e lo «decora». Il meccanismo ha quattro caratteristiche.

- L'oggetto originale è passato come parametro al costruttore del decorator, che restituisce l'oggetto «decorato».
- Più decorator possono essere concatenati tra loro, aggiungendo funzionalità in modo incrementale: la classe complessa è rappresentata dall'ultimo anello della catena.
- La concatenazione segue una composizione arbitraria: il numero di comportamenti possibili dell'oggetto composito cresce con legge combinatoria al crescere dei decorator disponibili.
- È un'alternativa all'ereditarietà singola o multipla: con l'ereditarietà l'aggiunta di funzionalità è statica secondo i legami della gerarchia di classi, e a run-time non si può ottenere una combinazione arbitraria di funzionalità né aggiungerle/rimuoverle.

Nello schema concettuale intervengono quattro ruoli.

> [!aside]
> - **Component** è l'astrazione/interfaccia.
> - **ConcreteComponent** è l'implementazione base del componente.
> - **Decorator** è una classe astratta che include un Component e ne eredita l'operazione.
> - **ConcreteDecorator** migliora il Component: ne assume tutte le caratteristiche (ha un attributo component) e può modificarne i metodi in override.
> 
> ---
> 
> ![[23f68efaaaa8808166891e62f6ce5dcd9a6b178f81d261fb475fdbc5d5561330.jpg|200]]

Un decorator concreto incapsula l'oggetto decorato e ne estende il comportamento in override.

```java
public class Mozzarella extends PizzaDecorator {
  public Mozzarella(Pizza pizza) { super(pizza); }
  public String getDescription() {
    return pizza.getDescription() + ", Mozzarella";
  }
  public double getCost() { return pizza.getCost() + 1.50; }
}
```

Nelle librerie Java il pattern è usato da `Reader` con `BufferedReader(Reader in)`, `InputStream` con `InputStreamReader(InputStream in)` e `BufferedInputStream(InputStream in)`.

```java
BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
```

Vantaggi e svantaggi del pattern si bilanciano così.

- **Vantaggio**: combinando i decorator si ottengono combinazioni illimitate di chiamate al builder, senza dichiarare le classi per ogni combinazione («prosciutto e funghi», «margherita», «margherita doppia mozzarella», ecc.).
- **Svantaggio**: la costruzione di un oggetto richiede di istanziare più oggetti e chiamare più costruttori, quindi il pattern è inefficiente dal punto di vista computazionale e, di conseguenza, anche da quello energetico.

### Bridge

> [!quote] Gamma et al.
> Decouple an abstraction from its implementation so that the two can vary independently.

Il Bridge permette di decidere dinamicamente tra implementazioni diverse di un'interfaccia. È utile quando variano spesso sia la classe sia ciò che la classe fa (la classe stessa può essere pensata come l'implementazione, ciò che può fare come l'astrazione); quando una classe varia spesso il pattern diventa molto utile, perché i cambiamenti al codice si fanno facilmente con una conoscenza minima e preliminare del programma.

Nell'esempio un cerchio può essere disegnato in colori diversi usando lo stesso metodo della classe astratta ma diverse classi implementatrici del bridge.

![[623567b40758151800313a9c850d65e51124327a6d4bf875d4fe08c6e862ddbb.jpg|200]]

L'astrazione mantiene un riferimento all'implementatore, ricevuto nel costruttore.

```java
public abstract class Shape {
  protected DrawAPI drawAPI;
  protected Shape(DrawAPI drawAPI) { this.drawAPI = drawAPI; }
  public abstract void draw();
}
```

Conseguenza: il modo in cui un cerchio viene disegnato può variare indipendentemente dalla classe `Circle`, e la classe `Circle` può variare senza impatti sull'implementazione di disegno.

#### Adapter e Bridge a confronto

Entrambi i pattern nascondono i dettagli dell'implementazione sottostante, ma si collocano in momenti diversi del ciclo di vita del design.

- **Adapter**: mira a far collaborare componenti non correlati; si applica a sistemi già progettati (reengineering, interface engineering).
- **Bridge**: si usa a priori nel design, per far variare indipendentemente astrazioni e implementazioni; è il green field engineering di un «sistema estendibile», in cui nuovi elementi possono essere aggiunti allo «zoo di oggetti» anche se non noti in fase di analisi o di system design.

### Facade

> [!def] Facade
> **Interfaccia unificata** verso un insieme di oggetti di un sottosistema. La facciata definisce un'interfaccia di livello più alto che rende il sottosistema più facile da usare, astrae i dettagli più crudi (*gory details*) e permette di fornire un'architettura chiusa.

La facciata incapsula gli oggetti del sottosistema ed espone operazioni di livello superiore: ad esempio `ShapeMaker` possiede `circle`, `rectangle` e `square` ed espone `drawCircle()`, `drawRectangle()` e `drawSquare()`, ciascuna che delega all'oggetto interno.

La struttura ideale di un sottosistema combina Facade e Adapter/Bridge: un sottosistema consiste di un oggetto interfaccia, di un insieme di oggetti di dominio applicativo (oggetti entità) che modellano entità reali o sistemi esistenti — alcuni dei quali sono interfacce verso sistemi esistenti — e di uno o più oggetti di controllo. I due ruoli chiave sono realizzati con i pattern.

- **Interface object**: realizzato con un Facade, fornisce l'interfaccia del sottosistema.
- **Interfaccia verso sistemi esistenti**: realizzata con Adapter o Bridge, fornisce l'interfaccia al sistema esistente (sistema legacy), che non è necessariamente object-oriented.

## Pattern comportamentali

### Observer

L'intento dell'Observer è definire una dipendenza uno-a-molti tra oggetti, così che quando un oggetto cambia stato tutti i suoi dipendenti sono notificati e aggiornati automaticamente. L'esempio concettuale è un unico dato (es. `SpreadSheet Data`) osservato da più viste (formula, grafico a barre, grafico a torta) che si aggiornano al variare del dato.

![[e61b27c59a3f4c73f3ff42c0c13550754cd3e03bf1dca21fca4a2b97bf318247.jpg|200]]

Il pattern si applica in tre casi.

- Quando un'astrazione ha due aspetti, uno dipendente dall'altro.
- Quando un cambiamento a un oggetto richiede di cambiarne altri e non si sa quanti oggetti vanno cambiati.
- Quando un oggetto deve notificarne altri senza fare assunzioni su chi siano.

![[294493bd42106922731e6c64b09c2e384e31f8dca5ba477601437576fb07e139.jpg|200]]

Nella struttura il soggetto astratto conserva la lista degli osservatori, offre la registrazione e notifica i cambiamenti invocando `aggiorna()` su ciascun osservatore; il soggetto concreto, in `setStato(...)`, effettua la chiamata extra `update()` rispetto a una normale classe; l'osservatore concreto è legato al soggetto che vuole osservare e in `aggiorna()` legge lo stato aggiornato.

```java
public abstract class Soggetto {
  protected ArrayList<Osservatore> osservatori;
  public void registraOsservatore(Osservatore o) {
    osservatori.add(o);
  }
  protected void update() {
    for (int i = 0; i < osservatori.size(); i++)
      osservatori.get(i).aggiorna();
  }
  public abstract void setStato(int s);
}
```

Le conseguenze dell'applicazione sono cinque.

- **Modularità**: subject e observer possono variare indipendentemente.
- **Estensibilità**: si possono definire e aggiungere un numero qualsiasi di observer.
- **Personalizzabilità**: observer diversi forniscono viste diverse del subject.
- **Aggiornamenti inattesi**: gli observer non si conoscono tra loro.
- **Overhead di aggiornamento**: possono servire hint.

Gli aspetti di implementazione riguardano la mappatura subject-observer, i riferimenti pendenti (dangling references), l'evitare protocolli di aggiornamento specifici dell'observer (modelli push e push/pull) e la registrazione esplicita delle modifiche di interesse.

### Strategy

Per lo stesso compito esistono in genere molti algoritmi diversi (es. spezzare un flusso di testo in righe, fare il parsing di un insieme di token in un albero di sintassi astratta, ordinare una lista di clienti). Algoritmi diversi sono appropriati in momenti diversi; non si vogliono supportare tutti se non servono; un nuovo algoritmo va aggiunto facilmente senza disturbare l'applicazione che lo usa.

La **Policy** decide quale Strategy è migliore in funzione del Context corrente.

![[eb6a2bdd4eae9d829f9373ed0eb729f494116262a12a8faba15ba79907b0994f.jpg|200]]

Il pattern si applica in due casi.

- Molte classi correlate differiscono solo per il comportamento: Strategy permette di configurare una singola classe con uno tra molti comportamenti.
- Servono varianti di un algoritmo che scambiano spazio con tempo: tutte le varianti si implementano come gerarchia di classi di algoritmi, selezionabili a run-time.

In un'applicazione database, ad esempio, le strategie di ordinamento `BubbleSort`, `QuickSort` e `ShellSort` implementano la stessa interfaccia e sono intercambiabili rispetto alla classe `Database` che le usa.

### State

Classi e sottosistemi possono essere visti come sistemi reattivi: reagiscono a stimoli esterni (eventi) in base al loro stato corrente. Il caso motivante è una classe `Document` il cui comportamento è descritto da uno statechart con stati `Draft`, `Moderation` e `Published` e transizioni come la pubblicazione da parte dell'utente, l'approvazione o il rifiuto da parte dell'admin e la scadenza della pubblicazione.

![[85bd47df0374693f68a0bdc4b88f3c219d2f7c0565b18e63b311e6b9b3a6b373.jpg|300]]

L'implementazione diretta con condizionali sullo stato sembra gestibile.

```java
public void publish() {
  switch (state) {
    case "draft": state = "moderation"; break;
    case "moderation":
      if ("admin".equals(user.getRole())) state = "published";
      break;
  }
}
```

> [!error] Condizionali mostruosi
> Aggiungendo più stati e più transizioni, quasi tutti i metodi finiscono per contenere condizionali mostruosi; ogni modifica alla logica di transizione richiede di cambiare i condizionali di stato in ogni metodo.

Il pattern State risolve il problema: creare nuove classi per tutti i possibili stati di un oggetto e delegare a queste classi il comportamento specifico dello stato.

![[16cd69c3e7fcccec690c1de072c73398abc9b57b3edef9828f0732c1cf1f8a7d.jpg|200]]

#### State e Strategy a confronto

State è in certa misura simile a Strategy: in entrambi l'implementazione di certe operazioni è delegata a oggetti «pluggabili». La differenza chiave riguarda la consapevolezza reciproca.

- Nel pattern **State** i singoli stati possono conoscersi e avviare transizioni da uno stato all'altro: uno stato può decidere quale sarà il prossimo.
- Nel pattern **Strategy** le strategie quasi mai si conoscono: forniscono implementazioni separate e indipendenti della stessa operazione.

### Iterator

La situazione di partenza è un gruppo di oggetti su cui si vuole iterare senza conoscere la rappresentazione sottostante; magari in più modi (in avanti, all'indietro, saltando elementi, in base ai valori nella struttura) e magari contemporaneamente, in due o più modi. Il pattern è molto comune in Java e .NET.

Un **iteratore** è un oggetto che permette di scorrere tutti gli elementi o le parti contenuti in un altro oggetto, tipicamente un container o una lista; in certi contesti, come i database, è detto **cursor**. Il pattern separa l'implementazione dell'iterazione dalla lista stessa: l'Iterator è un'interfaccia nota, quindi non serve esporre i dettagli della struttura dati sottostante.

I partecipanti sono quattro.

- **Iterator interface**: metodi semplici per attraversare gli elementi della lista.
- **Concrete Iterator**: classe che implementa Iterator.
- **Iteratee interface**: definisce un'interfaccia per creare la lista che verrà iterata.
- **Concrete Iteratee**: crea un iteratore concreto per il proprio tipo di dati.

![[00759d66defc1ec7c2390b0e0c30b0c44f1a20ec32935071d1542e05692185ba.jpg|200]]

Nella collaborazione il client chiede al container un iteratore con `getIterator()`: `Iterator` e `Container` sono le interfacce, il `ConcreteContainer` crea il `ConcreteIterator` per i propri dati.

Le conseguenze riguardano cinque questioni di design.

- Chi controlla l'iterazione: iterator interni ed esterni.
- Chi definisce l'algoritmo: può stare nell'iterator o nell'iteratee.
- La robustezza.
- Gli operatori aggiuntivi (es. `Previous`, `SkipTo`).
- Se gli iterator hanno accesso privilegiato ai dati.

I pattern correlati sono tre.

- **Composite**: gli iterator si possono applicare a strutture ricorsive.
- **Factory Method**: per istanziare la sottoclasse concreta di iterator.
- **Memento**: usato con l'iterator, cattura lo stato di un'iterazione.

## Dependency Injection

> [!def] Dependency Injection
> **Pratica** in cui le risorse da cui un componente dipende sono passate (iniettate) dall'esterno invece che istanziate dal componente stesso durante la propria esecuzione.

Il componente dichiara, ad esempio tramite il costruttore, il tipo (eventualmente generico) e la quantità di tutte le risorse da cui dipende; i riferimenti alle risorse richieste vengono poi passati (iniettati), ad esempio tramite il costruttore.

```java
public class MyClass {
  private Logger logger;
  public MyClass(Logger logger) {
    this.logger = logger;
    logger.info("This is a log message.");
  }
}
```

`MyClass` può scrivere in un log e l'oggetto su cui scrive è quello di tipo `Logger` passato come parametro. Le conseguenze del pattern sono tre.

- Rende la classe più generica, separando il suo comportamento dall'oggetto specifico che le viene passato.
- Introduce una dipendenza tra un oggetto e una classe, che dal punto di vista del coupling può non essere ottimale.
- È detta anche **inversion of control**, perché richiede di creare prima l'oggetto dipendente e poi quello che lo userà, andando in direzione opposta, ad esempio, al modello BCE.

### Dependency Injection e testing

La Dependency Injection è fondamentale per il testing di isolamento e di integrazione: permette di eseguire un test su un oggetto ricevendo in input un oggetto fittizio su cui agire, al posto dell'oggetto concreto, che può non essere disponibile o non essere ancora testato.

- **Esempio**: per testare una classe che chiama un servizio non ancora disponibile, se la classe segue il pattern riceve via costruttore un riferimento all'oggetto servizio; in test si crea un servizio fittizio e lo si passa alla classe, che così si può eseguire anche senza il servizio originale.
- **Controesempio**: se la classe non segue il pattern, il riferimento al servizio è hardcoded o istanziato dentro la classe sotto test e non può essere modificato al momento del test.

## Riuso, ereditarietà e delega

### I due scopi dell'ereditarietà

L'ereditarietà persegue due scopi diversi: la descrizione di tassonomie e il riuso del codice.

- **Identificazione di tassonomie** (usata nell'analisi dei requisiti): si identificano oggetti del dominio applicativo legati gerarchicamente, con l'obiettivo di rendere il modello di analisi più comprensibile; nelle tassonomie l'ereditarietà si trova per specializzazione o per generalizzazione.
- **Specifica dei servizi** (usata nell'object design): con l'obiettivo di aumentare la riusabilità e migliorare modificabilità ed estensibilità.

### Eredità di implementazione e di interfaccia

Esistono due forme di ereditarietà, con scopi diversi.

- **Implementation inheritance** (anche detta eredità di classe): si eredita da una classe esistente con alcune o tutte le operazioni già implementate, per estendere le funzionalità dell'applicazione riusando quelle della classe padre.
- **Interface inheritance** (anche detta subtyping): si eredita da una classe astratta con tutte le operazioni specificate ma non ancora implementate.

Il riuso per implementazione inheritance nasce quando una classe molto simile a quella desiderata è già implementata e fa quasi quello che serve: avendo già una classe `List` e dovendo realizzare uno `Stack`, si può sottoclassare `Stack` da `List` fornendo i tre metodi `Push()`, `Pop()` e `Top()`.

> [!error] Problemi dell'implementazione inheritance
> - L'ereditarietà è il massimo accoppiamento possibile tra due classi.
> - Con l'ereditarietà la sottoclasse espone anche i metodi della superclasse: alcune operazioni ereditate possono avere comportamenti indesiderati (es. cosa succede se l'utente dello `Stack` chiama `Remove()` invece di `Pop()`?).

### Delega

> [!def] Delega
> **Meccanismo** che rende la composizione (ad esempio l'aggregazione) potente per il riuso quanto l'ereditarietà: nella gestione di una richiesta sono coinvolti due oggetti e l'oggetto ricevente delega le operazioni al proprio delegato.

Lo sviluppatore può assicurarsi che l'oggetto ricevente non permetta al client di usare male l'oggetto delegato. La differenza operativa è netta: l'ereditarietà estende una classe base con una nuova operazione o ne sovrascrive una; la delega intercetta un'operazione e la invia a un altro oggetto.

![[c4ca332d92a9ba512deca3f0c60be5e3ea01ffce538159e43e4c6f0bc5863230.jpg|300]]

Delega ed ereditarietà di implementazione si confrontano su pro e contro.

| | Delega | Eredità di implementazione |
|---|---|---|
| Pro | Flessibilità: ogni oggetto è sostituibile a run-time con un altro dello stesso tipo | Semplicità d'uso, supporto di molti linguaggi, facilità di implementare nuove funzionalità |
| Contro | Inefficienza: gli oggetti sono incapsulati | Espone la sottoclasse ai dettagli della classe padre; ogni cambiamento nell'implementazione del padre forza il cambiamento della sottoclasse (e la ricompilazione di entrambe) |

> [!warning] Euristiche di design
> - Evitare l'ereditarietà di implementazione e usare sempre l'eredità di interfaccia.
> - Una sottoclasse non deve mai nascondere operazioni implementate in una superclasse.
> - Se si è tentati di usare l'ereditarietà di implementazione, usare invece la delega.

## Osservazioni e conclusioni

> [!warning] Cautela nell'uso dei pattern
> I pattern sistematizzano soluzioni standard per una classe di problemi: non vanno trattati come soluzioni su misura del proprio contesto specifico, né usati quando esistono soluzioni più semplici; l'abuso produce gerarchie di classi dai nomi mostruosi (es. `BaseEnterpriseVisitorOutputPrintableContextGeneratorSingletonMiddlewareStrategyConfiguratorFactoryReturner`).

Le tre categorie si riassumono per fuoco e problemi risolti.

| Categoria | Fuoco | Problemi risolti |
|---|---|---|
| Strutturali | Come gli oggetti sono composti in strutture più grandi | Realizzare nuove funzionalità da funzionalità esistenti; fornire flessibilità ed estensibilità |
| Comportamentali | Algoritmi e assegnazione di responsabilità agli oggetti | Accoppiamento troppo stretto a un algoritmo particolare; gestione del comportamento stato-dipendente |
| Creazionali | Creazione di oggetti complessi | Nascondere come gli oggetti complessi sono creati e assemblati |

Due osservazioni chiudono la lezione.

- I pattern permettono di progettare a un livello più astratto, trattando molte interazioni tra classi e oggetti come un'unità; spesso sono benefici dopo il design iniziale e sono bersagli per il refactoring delle classi.
- Il **variation-oriented design** considera quali aspetti del design sono variabili, identifica i pattern applicabili, varia i pattern per valutare i trade-off e ripete.

La conclusione è metodologica: prima si definisce il problema, poi si cerca la soluzione; poiché i pattern sono soluzioni a problemi, non vanno cercati prima di aver definito il problema.