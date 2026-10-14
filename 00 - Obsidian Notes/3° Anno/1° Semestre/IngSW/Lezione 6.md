# Lezione 10 System Design e Design Practices

## La progettazione di un sistema

> [!def] Software Design
> **Insieme** dei task svolti dall'ingegnere del software per trasformare il modello di analisi nel modello di design del sistema.

L'obiettivo ultimo di System e Object Design è definire un nuovo documento, scritto in linguaggio tecnico e formale, da dare ai programmatori affinché siano in grado di implementare il software descritto nel Documento dei Requisiti Software.

## Scopo di System Design e Object Design

> [!def] System Design
> **Attività** di progettazione con tre scopi: definire gli obiettivi di design del progetto; definire l'architettura del sistema, decomponendolo in sottosistemi più piccoli che possano essere realizzati in parallelo da team individuali; selezionare le strategie per costruire il sistema (hardware/software, gestione dei dati persistenti, flusso di controllo globale, politiche di controllo degli accessi).

> [!def] Object Design
> **Attività** che, data l'architettura del sistema, specifica il dettaglio realizzativo dei sottosistemi più piccoli e seleziona le strategie ottimali per l'implementazione (design pattern).

## Il cambio di prospettiva

Il system design cambia radicalmente il punto di vista rispetto alla fase di analisi.

- Finora si è lavorato per interagire col cliente: linguaggio per profani, poco formale.
- Nel system design gli interlocutori sono le squadre di programmatori che dovranno implementare il sistema: chi leggerà i documenti è un esperto di informatica, quindi il linguaggio è per esperti tecnici.## Le attività del system design

Il system design è costituito da tre macro-attività.

1. **Identificare gli obiettivi di design**: gli sviluppatori identificano quali caratteristiche di qualità ottimizzare e ne definiscono le priorità.
2. **Progettare la decomposizione in sottosistemi**: basandosi sugli use case e sui modelli di analisi, gli sviluppatori decompongono il sistema in parti più piccole, usando stili architetturali standard.
3. **Raffinare la decomposizione**: quella iniziale di solito non soddisfa gli obiettivi di design; gli sviluppatori la raffinano finché gli obiettivi non sono soddisfatti.

### I passi del system design

Il processo completo si articola in otto passi, dal riconoscimento degli obiettivi qualitativi fino alla definizione dell'architettura.

![[b42ec00b73937a2517009f884edd783254b99d5c3fbdd6f1e2ec3cc6484a6085.jpg|450]]

## Gli obiettivi qualitativi del sistema

Identificare gli obiettivi qualitativi è il primo passo del system design: identifica le qualità su cui il sistema deve essere focalizzato.

- Molti design goal si ricavano dai requisiti non funzionali o dal dominio di applicazione; altri sono forniti dal cliente.
- È importante formalizzarli esplicitamente: ogni importante decisione di design deve seguire lo stesso insieme di criteri.

### Criteri di design

Gli obiettivi si selezionano da una lunga lista di qualità desiderabili, organizzate in cinque gruppi.

- **Performance**: tempo di risposta, throughput, requisiti di memoria.
- **Affidabilità**: robustezza, disponibilità, tolleranza ai fault, sicurezza.
- **Costi**: sviluppo, manutenzione, gestione.
- **Mantenimento**: estendibilità, modificabilità, adattabilità, portabilità.
- **Usabilità**.

### Design trade-offs

Quando si definiscono gli obiettivi di design, solo un piccolo sottoinsieme di questi criteri può essere tenuto in considerazione (non è realistico sviluppare software simultaneamente sicuro ed economico). Gli sviluppatori devono dare priorità agli obiettivi, tenendo conto anche di aspetti manageriali come schedule e budget. Casi tipici di trade-off:

- **Spazio vs. velocità**: se il software non rispetta i requisiti di tempo di risposta e throughput, si usa più memoria per velocizzarlo (caching, ridondanza); se non rispetta i requisiti di memoria, si comprime a discapito della velocità.
- **Tempo di rilascio vs. funzionalità**: con tempi stringenti si rilasciano meno funzionalità di quelle richieste, ma nei tempi giusti.
- **Tempo di rilascio vs. qualità**: con tempi stretti si può rilasciare nei tempi prefissati con dei bug da correggere in seguito, oppure rilasciare in ritardo con meno bug.
- **Tempo di rilascio vs. staffing**: si possono aggiungere risorse al progetto per accrescere la produttività.

## Concetti di base di buon design

Molti criteri di design dipendono strettamente dal problema trattato: scegliere il miglior bilanciamento dei vincoli è compito dell'analista, che opera per esperienza e sensibilità. Esistono però criteri generici, validi per qualunque software object-oriented: ben applicati, migliorano notevolmente la qualità interna del codice senza introdurre particolari svantaggi.

Un principio guida trasversale è **pensare in avanti**: quando si progetta una classe bisogna sforzarsi di immaginare quali cambiamenti saranno richiesti in futuro, perché le scelte iniziali devono facilitare l'evoluzione del software.

## La decomposizione

Per ridurre la complessità della soluzione si decompone il sistema in parti più piccole, chiamate **sottosistemi**.

- Un sottosistema corrisponde alla parte di lavoro svolgibile autonomamente da un singolo sviluppatore o da un team.
- Sottosistemi relativamente indipendenti permettono ai team di lavorare con un minimo overhead di comunicazione.
- I sottosistemi complessi si decompongono ulteriormente in sottosistemi più semplici.

### Il vantaggio della decomposizione

Siano `P` un problema, `C(P)` la sua complessità e `E(P)` lo sforzo per risolverlo. Dati due problemi `P1` e `P2`:

- se `C(P1) > C(P2)` allora `E(P1) > E(P2)`;
- ma `C(P1+P2) > C(P1) + C(P2)`, quindi `E(P1+P2) > E(P1) + E(P2)`: affrontare i sottoproblemi separatamente costa meno che affrontare il problema intero.

## Sottosistemi, servizi e interfacce

La modellazione dei sottosistemi ha primitive precise nei linguaggi object-oriented.

- **Subsystem** (in UML: package): collezione di classi, associazioni, operazioni e vincoli correlati.
- **Primitive linguistiche**: Java fornisce i package; C++ e C# usano il costrutto di namespace per lo stesso concetto.

Un sottosistema è caratterizzato dai servizi che fornisce agli altri.

- L'insieme delle operazioni di un sottosistema disponibili agli altri sottosistemi forma l'**interfaccia** del sottosistema: nomi delle operazioni, parametri, tipi e valori di ritorno.
- Il system design si focalizza sulla definizione dei servizi di ogni sottosistema in termini di operazioni, loro parametri e loro comportamento ad alto livello.

### Le responsabilità contano più dei dati

Un esempio classico di scelta di design riguarda l'accesso al database: se tutti i sottosistemi accedono direttamente al DB, non si riescono a specificare chiaramente le responsabilità di ogni modulo e tutti diventano vulnerabili ai cambiamenti dell'interfaccia del sottosistema Database (un cambio di DBMS richiede modifiche in tutte le classi che accedono al DB). Introducendo un sottosistema DataAccess che gestisce l'I/O dal database, le responsabilità diventano chiare e al cambio del DBMS si modifica solo il sottosistema Storage.

> [!warning] Attenzione all'astrazione
> Ridurre le relazioni tra sottosistemi può aumentare la complessità: con l'obiettivo di ridurre le relazioni si rischia di aggiungere livelli di astrazione che consumano tempo di sviluppo e tempo di elaborazione.

## Indipendenza funzionale

La suddivisione in sottosistemi può essere guidata da due fattori qualitativi fondamentali: **coesione** e **accoppiamento**. L'obiettivo è l'indipendenza funzionale dei sottosistemi, che si massimizza con alta coesione e basso accoppiamento.

## La coesione

> [!def] Coesione
> **Misura** di quanto siano fortemente correlate e mirate le responsabilità (o i servizi offerti) di un modulo. Se ciascuna unità è responsabile di un singolo compito, l'unità ha alta coesione.

L'alta coesione è una proprietà desiderabile del codice perché permette di comprendere, riusare e manutenere meglio una classe, di limitare e focalizzare i cambiamenti nel codice e di usare nomi appropriati, efficaci e comunicativi. La coesione si valuta a due granularità.

- **Coesione dei metodi**: un metodo dovrebbe essere responsabile di un solo compito ben definito.
- **Coesione delle classi**: ogni classe dovrebbe rappresentare un singolo concetto ben definito.

### Il Single Responsibility Principle

> [!def] Single Responsibility Principle
> **Principio** per cui una classe dovrebbe avere una sola responsabilità e un solo motivo per cambiare: una responsabilità è un "motivo di cambiamento", e le responsabilità di una classe sono assi di cambiamento.

Se una classe ha due responsabilità, queste sono accoppiate nel design e devono cambiare insieme; una classe con più responsabilità diventa fragile quando cambia uno qualunque dei requisiti. I benefici del SRP: **reuse** (classi più facilmente riusabili), **clarity** (il codice è più pulito), **naming** (un'unica responsabilità rende facile scegliere un buon nome), **readability** (chiarezza, nomi migliori e file più corti).

Una classe con responsabilità multiple viola il principio; il caso tipico è una classe `Report` che raccoglie dati, li formatta e li stampa.

```csharp
class Report
{
  private IList<ReportDataElement> GetData() { ... }
  private void FormatReport() { ... }
  public void Print()
  {
    GetData();
    FormatReport();
    Console.WriteLine("Printing Report...");
  }
}
```

La soluzione separa le responsabilità in classi distinte: `DataAccess` per raccogliere i dati, `ReportFormatter` per la formattazione, `ReportPrinter` per la stampa.

### Indicatori di alta coesione

Un'alta coesione si riconosce da segnali concreti.

- La classe ha responsabilità moderate, limitate a una singola area funzionale.
- Collabora con altre classi per completare i task.
- Ha un numero limitato di metodi, con funzionalità altamente legate tra loro.
- Tutti i metodi sembrano appartenere a uno stesso insieme, con un obiettivo globale simile.
- La classe è facile da comprendere.

## L'accoppiamento

> [!def] Accoppiamento
> **Misura** di quanto fortemente una classe è connessa con, ha conoscenza di, o si basa su altre classi. Due o più classi sono accoppiate quando è impossibile riusare l'una senza dover riusare anche le altre.

Se due classi dipendono strettamente e per molti dettagli l'una dall'altra sono **fortemente accoppiate**; altrimenti sono **debolmente accoppiate**. Per un codice di qualità si punta a un **basso accoppiamento**.

- Un basso accoppiamento permette di capire una classe senza leggere i dettagli delle altre, di modificarla senza conseguenze sulle altre e di riusarla senza dover importare altre classi: migliora la manutenibilità del software.
- Un certo livello di accoppiamento è però insito nel concetto di scambio di messaggi del paradigma object-oriented: è necessario al funzionamento del sistema e va limitato ove possibile.
- Linea guida: definire le responsabilità delle classi in modo da ottenere un basso accoppiamento, anche con la legge di Demetra.

### Tipi di accoppiamento in O-O

Date due classi `X` e `Y`, sono forme di accoppiamento:

- `X` ha un attributo di tipo `Y`;
- `X` ha un metodo con un elemento (parametro, variabile locale, ecc.) di tipo `Y`;
- `X` è una sottoclasse, anche indiretta, di `Y`: lo scenario che porta al massimo accoppiamento in assoluto;
- `X` implementa un'interfaccia di tipo `Y`.

Il caso tipico di accoppiamento forte è una classe con un attributo del tipo concreto di cui ha bisogno, come un `Traveler` con un attributo di tipo `Car`: riusarla con un altro mezzo di trasporto o cambiare i metodi di `Car` richiede modifiche. Introducendo un'interfaccia l'accoppiamento si spezza completamente.

```java
class Traveler
{
  Vehicle v;
  void startJourney() { v.move(); }
}

interface Vehicle { void move(); }
```

Le conseguenze dell'introduzione dell'interfaccia `Vehicle`:

- `Traveler` è ora accoppiato con un'interfaccia, non con una classe concreta.
- Tutte le implementazioni dell'interfaccia funzionano con `Traveler` senza modifiche al codice.
- Sarà possibile usare implementazioni di `Vehicle` non ancora realizzate oggi (anticipare il cambiamento).
- Serve un'entità esterna che faccia l'inject della reale implementazione dell'interfaccia.
- La complessità del codice aumenta.

### Il ruolo delle interfacce

Le interfacce portano due benefici chiave, alla base del loro uso estensivo negli SDK come Java.

- **Standard e contratto**: un'interfaccia definisce un contratto che promuove il riuso; se un oggetto implementa un'interfaccia, promette di conformarsi a uno standard. L'oggetto che ne usa un altro è detto consumer, e l'interfaccia è un contratto tra un oggetto e il suo consumer.
- **Astrazione**: permettono di discutere il comportamento generale del codice senza entrare nei dettagli specifici, rendendo i programmi più facili da capire.

## La legge di Demetra

> [!def] Legge di Demetra
> **Linea guida** chiave per il basso accoppiamento, nata nel progetto Demetra (uno dei primi grandi sistemi object-oriented, sviluppato all'Università di Boston): spinge al massimo l'information hiding, evitando catene di chiamate tipo `Foo.getA().getB().getC()`. Più è lungo il percorso di chiamate attraversato dal programma, più il programma è fragile ai cambiamenti.

Un metodo `M` di un oggetto `O` dovrebbe mandare messaggi solo a:

- l'oggetto contenente (`this`);
- una variabile di istanza di `this`;
- un parametro del metodo;
- un oggetto creato all'interno del metodo;
- i propri oggetti componenti diretti.

### Eliminare il navigation code

Applicare la legge porta a eliminare il navigation code, delegando l'operazione al componente che la possiede: invece di attraversare la catena `Car → Engine → Carburetor` per aprire la valvola del carburatore, il `Car` chiama `engine.speedUp()` e l'`Engine` chiama `carburetor.openFuelValve()`.

![[9f32e096f7ea98d10e60f30c448a0336cc7be6a1d6ae6f08a3c639d1e88620b9.jpg|350]]

## Il responsibility-driven design

Il **responsibility-driven design** (RDD) pensa alla progettazione in termini di classe, responsabilità e collaborazioni.

- Ciascuna classe dovrebbe avere responsabilità e ruoli ben precisi → alta coesione.
- La classe che possiede i dati dovrebbe essere responsabile di processarli → basso accoppiamento.
- Ciascuna classe dovrebbe essere responsabile di gestire i propri dati → incapsulamento.
- Il metodo è facilitato dall'uso di CRC cards.

### Le CRC cards

> [!def] CRC Card
> **Scheda** da associare a ogni classe, introdotta da Kent Beck e Ward Cunningham per insegnare la progettazione object-oriented: riporta il nome della classe, le superclassi e sottoclassi, le responsabilità (conoscenza che la classe mantiene o servizi che fornisce) e i collaboratori (altre classi di cui sfruttare conoscenza o servizi per ottemperare alle responsabilità).

Le CRC cards spingono verso un design con responsabilità chiare e controllo sul numero di classi associate.

- Se non si riesce a specificare chiaramente le responsabilità di una classe, c'è un errore di design.
- Se una classe ha bisogno di troppe classi collaboratrici, c'è un potenziale errore di design.

### Localizzare le modifiche

Il design RDD con CRC cards porta a una **localizzazione delle modifiche**: quando è necessario operare una modifica, dovrebbe essere coinvolto il minor numero possibile di classi. La qualità del proprio codice si osserva proprio quando sorge l'esigenza di fare modifiche.