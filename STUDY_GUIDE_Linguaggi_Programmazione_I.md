# 📚 GUIDA ALLO STUDIO - Linguaggi di Programmazione I
## Università di Napoli Federico II - A.A. 2022-2023
### Docente: Piero Andrea Bonatti

---

## 📋 INDICE DELLA GUIDA
1. [Overview dell'Esame](#overview)
2. [Glossario dei Termini](#glossario)
3. [Argomenti Core](#argomenti-core)
4. [Mappe Concettuali](#mappe-concettuali)
5. [Domande di Ripasso](#domande-ripasso)
6. [Simulazioni d'Esame](#simulazioni)
7. [Tecniche di Studio](#tecniche-studio)
8. [Consigli Pratico-Organizzativi](#consigli-pratici)

---

<a name="overview"></a>
## 🎯 OVERVIEW DELL'ESAME

### Informazioni Generali
- **Corso**: Linguaggi di Programmazione I
- **CFU**: Tipicamente 6
- **Docente**: Piero Andrea Bonatti
- **Ateneo**: Università di Napoli Federico II
- **Livello**: Primo anno - Corso di Laurea Informatica

### Argomenti Principali e Loro Peso
| Argomento | Peso Stimato | Difficoltà |
|-----------|--------------|-----------|
| Concetti Fondamentali | 10% | Bassa |
| Paradigma Imperativo | 25% | Media |
| Astrazione Procedurale | 20% | Alta |
| Paradigma Object-Oriented (Java) | 30% | Alta |
| Paradigma Funzionale (ML) | 10% | Alta |
| Paradigma Logico (Prolog) | 5% | Molto Alta |

### Formato Esame (Tipico)
- **Parte Teorica**: Domande aperte sugli argomenti e paradigmi
- **Parte Pratica**: Esercizi di codifica in Java, ML e/o Prolog
- **Durata**: 2-3 ore (dipende dalla struttura dell'ateneo)
- **Materiali Ammessi**: Di solito nessuno (verificare con docente)

### Obiettivi di Apprendimento
Al termine del corso devi essere in grado di:
1. ✅ Comprendere cosa è un linguaggio di programmazione e come funziona
2. ✅ Spiegare i diversi paradigmi di programmazione
3. ✅ Implementare programmi nel paradigma imperativo
4. ✅ Usare concetti di astrazione procedurale correttamente
5. ✅ Progettare e programmare in Java (OOP)
6. ✅ Scrivere funzioni in ML (paradigma funzionale)
7. ✅ Risolvere problemi in Prolog (paradigma logico)
8. ✅ Confrontare i diversi paradigmi

---

<a name="glossario"></a>
## 📖 GLOSSARIO DEI TERMINI CHIAVE

### Concetti Fondamentali
- **Linguaggio di Programmazione**: Insieme di regole per comunicare idee tra programmatore e calcolatore
- **Programma**: Espressione codificata di un processo che risolve un problema
- **Macchina Astratta (ML)**: Insieme di strutture dati e algoritmi che memorizzano ed eseguono programmi in un linguaggio L
- **Compilatore**: Programma che traduce il codice sorgente in linguaggio macchina prima dell'esecuzione
- **Interprete**: Programma che traduce ed esegue il codice riga per riga
- **Paradigma**: Modello che permette di descrivere astrattamente l'algoritmo di soluzione

### Paradigma Imperativo
- **Variabile**: Astrazione del programmatore per un indirizzo di memoria
- **Assegnazione**: Operazione che modifica il valore in una locazione di memoria
- **Stato**: Descrizione del contenuto della memoria in un dato momento
- **Ambiente di Esecuzione**: Insieme delle strutture che mantengono lo stato durante l'esecuzione
- **Scope**: Porzione di programma in cui una variabile è visibile
- **Binding**: Associazione tra un identificatore e una locazione di memoria (o valore)

### Astrazione Procedurale
- **Procedura/Funzione**: Astrazione che permette di raggruppare istruzioni
- **Record di Attivazione (AR)**: Struttura dati che mantiene le informazioni di una procedura quando è in esecuzione
- **Stack di Attivazione**: Pila di record di attivazione durante l'esecuzione del programma
- **Parametri**: Variabili che permettono di parametrizzare una procedura
- **Passaggio per Valore**: Il valore dell'argomento è copiato nel parametro
- **Passaggio per Riferimento**: L'indirizzo dell'argomento è passato al parametro
- **Closure**: Funzione che "cattura" variabili dal suo contesto
- **Aliasing**: Situazione dove due nomi si riferiscono alla stessa locazione di memoria

### Paradigma Object-Oriented
- **Classe**: Blueprint per creare oggetti, definisce attributi e metodi
- **Oggetto**: Istanza di una classe con stato (attributi) e comportamento (metodi)
- **Metodo**: Procedura che appartiene a una classe e opera sugli oggetti
- **Ereditarietà**: Meccanismo per cui una classe eredita attributi e metodi da una superclasse
- **Polimorfismo**: Capacità di un oggetto di assumente diverse forme; di un metodo di comportarsi diversamente
- **Incapsulamento**: Nascondere i dettagli interni di una classe (public, private, protected)
- **Costruttore**: Metodo speciale per inizializzare un oggetto
- **Garbage Collector**: Meccanismo automatico che libera memoria non più utilizzata
- **Tipo Primitivo**: Tipo di dato base (int, boolean, double, ecc.)
- **Tipo Reference**: Tipo che fa riferimento a un oggetto (classi, interfacce)

### Paradigma Funzionale
- **Funzione Pura**: Funzione che non ha effetti collaterali e sempre lo stesso output per lo stesso input
- **First-Class Function**: Funzione trattata come un valore (assegnabile, passabile, ritornabile)
- **Higher-Order Function**: Funzione che accetta funzioni come parametri o le ritorna
- **Currying**: Trasformazione di una funzione a n parametri in n funzioni a 1 parametro
- **Pattern Matching**: Tecnica per decomporre valori strutturati
- **Datatype**: Tipo di dato strutturato definito dall'utente
- **Ricorsione**: Strategie di iterazione nel paradigma funzionale
- **Map, Filter, Reduce**: Funzioni fondamentali per processare collezioni

### Paradigma Logico
- **Fatto (Fact)**: Affermazione che è sempre vera nel programma
- **Regola (Rule)**: Implicazione logica (se-allora)
- **Query**: Domanda posta al sistema
- **Unificazione**: Processo di rendere uguali due termini attraverso sostituzioni di variabili
- **Backtracking**: Meccanismo di esplorazione dello spazio di ricerca
- **Predicato**: Relazione o proprietà che può essere vera o falsa
- **Termine**: Elemento base di Prolog (costante, variabile, composto)
- **Albero di Ricerca**: Struttura che rappresenta le possibili soluzioni

---

<a name="argomenti-core"></a>
## 🔥 ARGOMENTI CORE - ORDINE DI STUDIO CONSIGLIATO

### FASE 1: Fondamenti (2-3 giorni)

#### Capitolo 1: Introduzione ai Linguaggi di Programmazione

**Cosa devi sapere:**

1. **Definizione di Linguaggio di Programmazione**
   - È un mezzo di comunicazione tra programmatore e calcolatore
   - Esprime la soluzione a un problema in forma di programma
   - Caratteristica distintiva: programmatore, processore, programma, problema
   - Distinzione: linguaggi computazionalmente completi vs. incompleti
   - Esempio: SQL non è completo (terminazione sempre decidibile), HTML non è completo

2. **Macchine Astratte**
   - Definizione formale: insieme di strutture dati e algoritmi per memorizzare/eseguire programmi
   - Due componenti principali: **memoria** e **processore**
   - Memoria: funzione da locazioni a valori (mem: Locazioni → Valori)
   - Processore: ciclo fetch-decode-execute
   - Tre modalità di implementazione: hardware, software, firmware

3. **Traduzione dei Linguaggi**
   - Due approcci principali:
     - **Compilazione**: traduce tutto prima, poi esegue (batch processing)
     - **Interpretazione**: traduce ed esegue riga per riga
   - Processo di compilazione: sorgente → token → parse tree → AST → codice oggetto
   - Tempo di compilazione vs. runtime
   - Java: compilazione a bytecode + interpretazione dalla JVM (approccio ibrido)

4. **Proprietà dei Linguaggi**
   - **Semplicità**: numero minimo di concetti, unicità rappresentativa
   - **Astrazione**: rappresentazione con attributi rilevanti, eliminazione irrilevanti
   - **Espressività**: facilità nella rappresentazione di oggetti e procedure
   - **Ortogonalità**: grado di coerenza nell'interazione tra concetti
   - **Portabilità**: indipendenza dalla macchina sottostante

5. **Paradigmi Computazionali**
   - **Imperativo**: sequenza di modifiche allo stato della memoria (dichiarativo, sequenziale)
   - **Funzionale**: descrizione delle operazioni per risolvere il problema (no stato mutabile)
   - **Logico**: descrizione logica formale del problema
   - **Object-Oriented**: modellazione di oggetti che si scambiano messaggi
   - **Parallelo**: programmi con entità distribuite (ortogonale ai primi 3)

**Errori Comuni:**
- ❌ Confondere "compilatore" e "interprete"
- ❌ Non capire che Java usa entrambi gli approcci
- ❌ Pensare che complessità ≠ completezza di Turing

---

### FASE 2: Paradigma Imperativo (3-4 giorni)

#### Capitolo 2: Il Paradigma Imperativo

**Cosa devi sapere:**

1. **Fondamenti del Paradigma Imperativo**
   - Basato su: stato della memoria + sequenza di comandi
   - Riflette il funzionamento della CPU a livello macchina
   - Due unità principali: CPU (calcoli) e memoria (dati)
   - Memoria astratta: `mem: Locazioni → Valori`

2. **L'Assegnazione**
   - Sintassi BNF: `<name> ::= <expression>`
   - È l'operazione centrale del paradigma imperativo
   - 4 passi dell'esecuzione:
     1. Recupero indirizzo variabile risultato e operandi
     2. Recupero valori dalle locazioni
     3. Calcolo espressione
     4. Memorizzazione risultato
   - Esempio: `a := b + c` modifica il valore in locazione 'a'

3. **Variabili e Bindings**
   - **Variabile**: nome che astrae un indirizzo di memoria
   - **Binding**: associazione tra nome e locazione (name binding) O tra nome e valore (value binding)
   - **Dynamic Binding**: binding determinato a runtime
   - **Static Binding**: binding determinato a compile-time

4. **Puntatori**
   - Variabili che contengono indirizzi di memoria
   - Operazioni: dereferenziazione (*), indirizzo (&)
   - Utilità: gestione dinamica della memoria
   - Pericoli: dangling pointers, memory leaks

5. **Legame di Tipo**
   - **Static Typing**: tipo determinato a compile-time
   - **Dynamic Typing**: tipo determinato a runtime
   - **Strong Typing**: linguaggio non permette operazioni tra tipi incompatibili
   - **Weak Typing**: linguaggio permette conversioni implicite

6. **Blocchi di Istruzione**
   - Raggruppamento di istruzioni in sequenza
   - Permettono di definire scope locali
   - Struttura: `{ <dichiarazioni> <istruzioni> }`

7. **Scoping e Ambiti**
   - **Name Binding Scope**: dove un nome è visibile nel codice
   - **Location Binding Scope**: dove una locazione è mantenuta attiva
   - **Scope Statico**: determinato dalla struttura del codice (più comune)
   - **Scope Dinamico**: determinato dalla catena di chiamate

8. **Stack di Attivazione**
   - Mantiene i record di attivazione (AR) durante l'esecuzione
   - LIFO: Last In, First Out
   - Creato all'ingresso in un blocco, deallocato all'uscita
   - Consente la ricorsione

**Errori Comuni:**
- ❌ Confondere name binding con location binding
- ❌ Pensare che tutte le variabili occupino spazio statico
- ❌ Non capire il ruolo dello stack di attivazione

---

### FASE 3: Astrazione Procedurale (4-5 giorni)

#### Capitolo 3: Astrazione Procedurale

**Cosa devi sapere:**

1. **Procedure come Astrazioni**
   - Raggruppano sequenze di istruzioni in unità riutilizzabili
   - Astraggono i dettagli implementativi
   - Facilitano la modularità e la manutenzione
   - Possono essere funzioni (ritornano valori) o procedure (effetti collaterali)

2. **Ambiente di una Procedura**
   - **Record di Attivazione (AR)**: struttura dati che mantiene:
     - Parametri attuali
     - Variabili locali
     - Indirizzo di ritorno
     - Link al record di attivazione precedente (dynamic link)
     - Link all'ambiente non locale (static link, per lexical scoping)
   - Creato quando la procedura è chiamata
   - Deallocato quando la procedura termina

3. **Ambiente Locale vs. Non-Locale**
   - **Locale**: variabili dichiarate nella procedura
   - **Non-locale**: variabili della procedura esterna (o più esterne)
   - Accesso tramite static link nel record di attivazione
   - Permette l'implementazione del lexical scoping

4. **Parametrizzazione delle Procedure**
   - **Parametri Formali**: dichiarati nella firma della procedura
   - **Parametri Attuali**: valori passati al momento della chiamata

5. **Modalità di Associazione dei Parametri**
   - **Pass-by-Value (per valore)**:
     - Valore dell'argomento è copiato nel parametro
     - Modifiche al parametro non affettano l'argomento
     - Efficiente per piccoli valori, costoso per grandi strutture
   
   - **Pass-by-Reference (per riferimento)**:
     - Indirizzo dell'argomento è passato
     - Modifiche al parametro affettano l'argomento
     - Efficiente per grandi strutture
     - Permette la restituzione di valori attraverso parametri
   
   - **Pass-by-Name (per nome)**:
     - Argomento è sostituito testualmente (come una macro)
     - Valutazione lazy (solo se usato)
     - Raro nei linguaggi moderni
   
   - **Pass-by-Result (per risultato)**:
     - Valori copiati dal parametro all'argomento alla fine
     - Simile a pass-by-value, ma al contrario

6. **Implementazione del Passaggio dei Parametri**
   - Caricamento nel record di attivazione
   - Differenze nei linguaggi: Java (pass-by-value sempre), C (pass-by-reference con &)

7. **Aliasing**
   - Situazione dove due nomi si riferiscono alla stessa locazione
   - Conseguenze: modifiche attraverso un nome affettano l'altro
   - Esempio: due parametri per riferimento che puntano alla stessa locazione
   - Difficile da debuggare e da verificare

8. **Procedure come Parametri**
   - Funzioni di ordine superiore (higher-order functions)
   - Permettono di passare comportamenti come parametri
   - Importante per implementare callback e plugin

9. **Macro**
   - Sostituzione testuale del codice prima della compilazione
   - A differenza del pass-by-name, avviene al compile-time
   - Utilizzo cautamente: difficili da debuggare

10. **Vettore degli Ambienti Non-Locali**
    - Tecnica di implementazione alternativa al static link
    - Mantiene riferimenti a tutti gli ambienti padre
    - Accesso diretto al livello desiderato (più veloce del chain)
    - Uso di maggior memoria

**Errori Comuni:**
- ❌ Confondere pass-by-value e pass-by-reference
- ❌ Non capire come gli static link abilitano il lexical scoping
- ❌ Pensare che le procedure siano completamente indipendenti (closure)

---

### FASE 4: Paradigma Object-Oriented - Java (6-8 giorni)

#### Capitolo 4: Java e Paradigma Object-Oriented

**Questo è l'argomento più complesso e critico dell'esame.**

1. **Ciclo di Vita di un Programma Java**
   - **Fase 1: Scrittura e Modifica** - Editor di testo
   - **Fase 2: Compilazione** - Compilatore Java → bytecode (.class)
   - **Fase 3: Caricamento** - ClassLoader carica il bytecode in memoria
   - **Fase 4: Verifica** - Bytecode Verifier controlla validità bytecode
   - **Fase 5: Esecuzione** - JVM interpreta il bytecode (o JIT compila a macchina nativa)

2. **Java Runtime Environment (JRE)**
   - Ambiente necessario per eseguire programmi Java
   - Include: JVM, classi standard, garbage collector
   - Indipendente dalla piattaforma (write once, run anywhere)

3. **Garbage Collector**
   - Meccanismo automatico di gestione della memoria
   - Identifica e libera memoria inutilizzata
   - Vantaggio: programmatore non deve gestire manualmente new/delete
   - Svantaggio: pause non deterministiche

4. **Tipi di Dato in Java**
   
   **Tipi Primitivi** (memorizzati nello stack):
   - **Interi**: `byte` (8 bit), `short` (16 bit), `int` (32 bit), `long` (64 bit)
   - **Virgola Mobile**: `float` (32 bit IEEE 754), `double` (64 bit IEEE 754)
   - **Caratteri**: `char` (16 bit, Unicode)
   - **Booleani**: `boolean` (true/false)
   - ⚠️ Importante: dimensioni e range standardizzati
   
   **Tipi Reference** (memorizzati nell'heap):
   - Classi
   - Interfacce
   - Array
   - Tipi null (assenza di valore)

5. **Casting di Tipi Primitivi**
   - **Widening** (automatico): `byte` → `int` → `long` → `float` → `double`
   - **Narrowing** (esplicito richiesto): `double` → `int` → `byte`
   - Rischi nel narrowing: perdita di precisione, overflow

6. **Classi e Oggetti**
   - **Classe**: blueprint che definisce attributi (dati) e metodi (comportamento)
   - **Oggetto**: istanza di una classe con stato specifico
   - Creazione: `new ClassName(parametri)` alloca memoria e chiama costruttore

7. **Costruttore**
   - Metodo speciale con stesso nome della classe
   - Eseguito al momento della creazione dell'oggetto
   - Può inizializzare lo stato dell'oggetto
   - Se non definito, Java fornisce un costruttore di default (no-arg)
   - Possono essere multipli (overloading)

8. **Metodi**
   - Funzioni che appartengono a una classe
   - Sintassi: `modificatore tipoRitorno nomMetodo(parametri) { corpo }`
   - **Metodi di istanza**: operano su un oggetto specifico (accesso a `this`)
   - **Metodi statici**: operano sulla classe (non hanno accesso a istanze)
   - **Return**: specifica il valore da ritornare (o void se nessuno)

9. **Passaggio dei Parametri in Java**
   - Sempre pass-by-value
   - Per i tipi primitivi: valore copiato
   - Per i tipi reference: copia della referenza (non copia dell'oggetto)
   - Conseguenza: modifiche all'oggetto sono visibili al chiamante, ma riassegnazione della variabile no

10. **Shadowing e `this`**
    - **Shadowing**: quando una variabile locale ha lo stesso nome di un attributo
    - **`this`**: referenza all'oggetto corrente
    - Uso: `this.attributo` per accedere all'attributo (evitare shadowing)
    - In costruttori: `this(...)` chiama un altro costruttore della stessa classe

11. **Ereditarietà**
    - Keyword: `extends` per ereditare da una superclasse
    - Una classe può estendere una sola superclasse (ereditarietà singola)
    - Tutte le classi ereditano implicitamente da `Object`
    - Eredita attributi e metodi della superclasse

12. **Keyword `super`**
    - Referenza alla superclasse
    - Uso: `super.metodo()` per chiamare un metodo della superclasse
    - `super(parametri)` per chiamare il costruttore della superclasse
    - Deve essere la prima istruzione nel costruttore (se presente)

13. **Polimorfismo**
    - Capacità di un oggetto di assumere diverse forme
    - **Polimorfismo ad hoc** (overloading):
      - Stesso nome di metodo, parametri diversi
      - Risoluzione a compile-time
      - Esempio: `System.out.println()` ha versioni per int, String, double, ecc.
    
    - **Polimorfismo parametrico**:
      - Attraverso ereditarietà
      - Una variabile può contenere istanze di qualsiasi sottoclasse
      - Risoluzione dinamica a runtime (virtual method invocation)
      - Esempio: `Animal animal = new Dog();` animal può chiamare metodi di Dog

14. **Operatore `instanceof`**
    - Verifica se un oggetto è istanza di una classe
    - Sintassi: `oggetto instanceof Classe`
    - Risultato: boolean
    - Utile prima di casting

15. **Overloading vs Override**
    - **Overloading**:
      - Stesso nome, parametri diversi
      - Risoluzione a compile-time
      - Può essere nella stessa classe o in superclasse
    
    - **Override**:
      - Stesso nome, stessa firma, superclasse diversa
      - Ridefinisce il comportamento del metodo della superclasse
      - Risoluzione a runtime (polymorphism)
      - Annotation `@Override` (facoltativo ma consigliato)
      - Requisiti: stesso tipo ritorno (o sottotipo), no eccezioni nuove

16. **Casting di Tipi Reference**
    - **Upcast**: da sottoclasse a superclasse (sempre sicuro)
      ```java
      Dog dog = new Dog();
      Animal animal = dog; // upcast implicito
      ```
    
    - **Downcast**: da superclasse a sottoclasse (richiede controllo esplicito)
      ```java
      Animal animal = new Dog();
      Dog dog = (Dog) animal; // downcast esplicito
      ```
    - Downcast non sicuro può causare ClassCastException a runtime

17. **Package e Struttura dei File**
    - **Package**: namespace che organizza classi
    - **File sorgenti**: una classe public per file, named `ClassName.java`
    - **Compilazione**: genera `ClassName.class` nella stessa directory (o struttura package)
    - **Cartelle**: struttura di directory riflette gerarchia package
      - Package `com.example.app` → cartella `com/example/app/`

18. **Operatori in Java**
    - **Operatori Logici**: `&&` (AND), `||` (OR), `!` (NOT)
    - **Operatori Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (shift sx), `>>` (shift dx)
    - **Operatori di Confronto**: `==`, `!=`, `<`, `>`, `<=`, `>=`
    - **Operatore Ternario**: `condizione ? valore1 : valore2`

19. **Enunciati di Controllo**
    - **Branch**: `if`, `else if`, `else`, `switch`
    - **Loop**: `for`, `while`, `do-while`, `enhanced for` (for-each)
    - **Break e Continue**: controllo del flusso

20. **Array in Java**
    - **Dichiarazione**: `int[] array;` oppure `int array[];`
    - **Creazione**: `array = new int[10];`
    - **Inizializzazione**: `int[] array = {1, 2, 3, 4, 5};`
    - **Accesso**: `array[indice]` (0-indexed)
    - **Proprietà**: `array.length`
    - **Multidimensionali**: `int[][] matrix = new int[3][4];`
    - Sono oggetti (tipo reference), non primitivi
    - **Classe Arrays**: utility per operazioni su array (sort, binarySearch, equals, ecc.)

21. **Array Multidimensionali**
    - **Matrice 2D**: `int[][] matrix = new int[righe][colonne];`
    - **Array Jagged**: righe di lunghezza diversa (non rettangolare)
    - Accesso: `matrix[i][j]`

22. **Copia di Array**
    - **Assegnazione**: copia la referenza (non i dati)
    - **System.arraycopy()**: copia effettiva
      ```java
      System.arraycopy(src, srcPos, dest, destPos, length);
      ```
    - **Clone()**: copia superficiale (shallow copy)

23. **Costruzione degli Oggetti**
    - Sequenza:
      1. Allocazione memoria
      2. Inizializzazione campi a valori di default
      3. Esecuzione di inizializzatori di istanza
      4. Esecuzione del costruttore
    - Catena di costruttori: `this(...)` e `super(...)`

24. **Classe Object**
    - Superclasse di tutte le classi
    - Metodi importanti:
      - `equals(Object o)`: confronto di uguaglianza (di default confronta referenze)
      - `hashCode()`: hash della referenza
      - `toString()`: rappresentazione in stringa
      - `clone()`: copia superficiale
      - `getClass()`: classe dell'oggetto

25. **Classe String**
    - Sequenza immutabile di caratteri
    - Operazioni: `length()`, `charAt()`, `substring()`, `concat()`, `equals()`, ecc.
    - **Concatenazione**: `+` operator crea nuovo String
    - **StringBuilder**: classe mutabile per costruire string efficientemente

26. **Classi Wrapper**
    - Classi che "wrappano" tipi primitivi (Integer, Double, Boolean, ecc.)
    - Motivo: API che richiedono oggetti (non primitivi)
    - **Autoboxing**: conversione automatica `int` → `Integer`
    - **Unboxing**: conversione automatica `Integer` → `int`
    - Metodi: `parseInt()`, `toString()`, `compareTo()`, ecc.

27. **Modificatori di Accesso**
    - **public**: accessibile da ovunque
    - **protected**: accessibile dalla stessa classe, sottoclassi, stesso package
    - **package-private** (default): accessibile solo stesso package
    - **private**: accessibile solo dalla classe stessa
    - Tabella di accesso (memorizzare!):
      ```
      Modificatore     Classe  Package  Sottoclasse  Altro
      public            ✓       ✓         ✓           ✓
      protected         ✓       ✓         ✓           ✗
      package-private   ✓       ✓         ✗           ✗
      private           ✓       ✗         ✗           ✗
      ```

28. **Modificatore `final`**
    - Variabili: valore non può essere cambiato (costante)
    - Metodi: non possono essere overridden
    - Classi: non possono essere estese
    - Uso: indicare intenzione, permettere ottimizzazioni

29. **Modificatore `abstract`**
    - Classi: non possono essere istanziate, solo estese
    - Metodi: dichiarazione senza implementazione (sottoclassi devono implementare)
    - Utile per definire contratti

30. **Modificatore `static`**
    - Attributi: condiviso da tutte le istanze (una sola copia)
    - Metodi: operano sulla classe, non su istanze (non accesso a `this`)
    - Blochi di inizializzazione: eseguiti all'atto del caricamento della classe
    - Uso: utility, costanti di classe

31. **Altre Modificatori**
    - **native**: implementazione in linguaggio nativo (es. C)
    - **transient**: campo non serializzato
    - **synchronized**: thread-safe (multithreading)
    - **volatile**: valore sempre letto dalla memoria principale (multithreading)

32. **Classi Astratte**
    - Contengono metodi abstract (senza implementazione)
    - Non possono essere istanziate
    - Forzano le sottoclassi a implementare metodi astratti
    - Esempio: `abstract class Animal { abstract void makeSound(); }`

33. **Interfacce**
    - Contratto: specifica quali metodi una classe DEVE implementare
    - Non contengono implementazione (fino a Java 8)
    - Keyword: `interface`
    - Implementazione: `class Dog implements Animal { ... }`
    - Una classe può implementare multiple interfacce
    - Vantaggi:
      - Decoupling: dipendenza dalle interfacce, non dalle implementazioni
      - Polimorfismo: più forme di implementazione
      - Design: contratto esplicito

34. **Eccezioni**
    - Meccanismo per gestire errori
    - **Gerarchia**: `Throwable` → `Exception` → (checked/unchecked) → sottoclassi specifiche
    - **Checked Exception**: deve essere catturata o dichiarata (`throws`)
      - Esempio: `IOException`, `FileNotFoundException`
    - **Unchecked Exception** (RuntimeException): non obbligatorio catturare
      - Esempio: `NullPointerException`, `ArrayIndexOutOfBoundsException`
    
    **Costrutto try-catch-finally:**
    ```java
    try {
      // codice che potrebbe lanciare eccezione
    } catch (TipoEccezione e) {
      // gestione dell'eccezione
    } catch (AltraEccezione e) {
      // gestione di un'altra eccezione
    } finally {
      // eseguito sempre (pulizia risorse)
    }
    ```
    
    **Sollevamento di eccezioni:**
    ```java
    throw new EccezionePersonalizzata("messaggio");
    ```
    
    **Dichiarazione nei metodi:**
    ```java
    public void metodo() throws EccezionePersonalizzata {
      // corpo
    }
    ```

35. **Classi Interne**
    - Classi definite dentro altre classi
    - Accesso ai campi privati della classe esterna
    
    **Classi Membro**:
    - Definite come attributi della classe esterna
    - Accesso tramite: `new OuterClass().new InnerClass()`
    - Possono essere public/private/protected
    
    **Classi Membro Statiche**:
    - Non hanno accesso all'istanza esterna
    - Accesso: `new OuterClass.StaticInnerClass()`
    - Simili a classi package-private annidate
    
    **Classi Locali**:
    - Definite dentro metodi
    - Visibili solo nel metodo
    - Accesso a variabili locali (devono essere effectively final)
    
    **Classi Anonime**:
    - Senza nome, definite e istanziate simultaneamente
    - Tipicamente implementano interfacce o estendono classi
    - Sintassi:
      ```java
      new InterfaceOrClass() {
        // implementazione
      };
      ```

**Errori Comuni:**
- ❌ Confondere pass-by-value con pass-by-reference in Java (è sempre pass-by-value!)
- ❌ Non capire che downcast richiede controllo esplicito e può fallire
- ❌ Confondere override con overloading
- ❌ Pensare che `==` confronti valori degli oggetti (confronta referenze per object)
- ❌ Non capire il ruolo della garbage collection
- ❌ Confondere classe astratta con interfaccia

---

### FASE 5: Paradigma Funzionale - ML (3-4 giorni)

#### Capitolo 5: ML e Paradigma Funzionale

**Cosa devi sapere:**

1. **Concetti Fondamentali del Paradigma Funzionale**
   - **No State Mutability**: variabili non cambiano valore, nuovi valori sono assegnati
   - **Funzioni Pure**: output dipende solo dai parametri, no side effects
   - **First-Class Functions**: funzioni trattate come valori (assegnabili, passabili)
   - **Higher-Order Functions**: funzioni che accettano/ritornano funzioni
   - **Recursion-Based Iteration**: iterazione attraverso ricorsione

2. **Sistema dei Tipi**
   - **Type Inference**: il compilatore deduce i tipi (non sempre devi dichiararli)
   - **Dichiarazioni esplicite**: quando i tipi non sono inferibili
   - Esempio: `val x = 5;` (tipo int inferito)

3. **Dichiarazioni e Scoping**
   - **Identificatori**: nomi per valori, funzioni
   - **`val` vs `var`**:
     - `val`: immutabile (valore non cambia)
     - `var`: mutabile (ma raro in ML puro)
   - **Funzioni**: dichiarate con `fun` oppure `fn`
     ```ml
     fun factorial(n) = 
       if n = 1 then 1 else n * factorial(n-1);
     ```
   - **Blocchi e Scope Locale**: `let...in...end`
     ```ml
     let
       val x = 5
       val y = 3
     in
       x + y
     end
     ```

4. **Dichiarazioni Locali**
   - `let...in...end` definisce variabili locali
   - Scope limitato al blocco
   - Utile per decomporre problemi complessi

5. **Tipi Strutturati**
   - **Prodotto Cartesiano** (Tuple):
     - `(1, "hello", true)` è una tupla di 3 elementi
     - Accesso: pattern matching
   
   - **Record**:
     - Simile a struct in C
     - `{x: int, y: int}` (con etichette)
     - Accesso: `#x record` oppure pattern matching
   
   - **Sinonimi di Tipo**:
     ```ml
     type point = {x: real, y: real};
     ```
   
   - **Datatype** (Tipi Algebrici):
     - Definisce costruttori per valori
     - Esempio:
       ```ml
       datatype color = Red | Green | Blue;
       datatype option = NONE | SOME of int;
       ```
     - Simile a enum, ma con dati associati ai costruttori

6. **Pattern Matching**
   - Tecnica per decomporre valori strutturati
   - Simile a switch/case, ma più potente
   - Esempi:
     ```ml
     fun fst (x, y) = x;  (* tupla *)
     
     fun describe (color) = 
       case color of
       | Red => "Rosso"
       | Green => "Verde"
       | Blue => "Blu";
     
     fun optionValue (NONE) = 0
       | optionValue (SOME x) = x;
     ```

7. **Liste**
   - Struttura dati fondamentale in ML
   - Sintassi: `[1, 2, 3, 4, 5]`
   - Operatori:
     - `::` (cons): aggiunge elemento in testa
     - `@` (append): concatena liste
     - `[]` lista vuota
     - `[1, 2] = 1::(2::[])`
   - Accesso:
     ```ml
     val head::tail = [1, 2, 3];  (* head=1, tail=[2,3] *)
     ```
   - Predicati predefiniti:
     - `length(list)`: numero elementi
     - `null(list)`: verifica se vuota
     - `hd(list)`: primo elemento
     - `tl(list)`: resto della lista

8. **Currying**
   - Trasformazione di funzione a n parametri in n funzioni a 1 parametro
   - Naturale in ML per le funzioni polimorfiche
   - Esempio:
     ```ml
     fun add(x, y) = x + y;      (* 2 parametri *)
     fun add' x y = x + y;        (* curried, equivalente *)
     ```
   - Vantaggi: applicazione parziale, composizione funzioni

9. **Funzioni di Ordine Superiore**
   - Funzioni che operano su altre funzioni
   - **filter**: seleziona elementi che soddisfano predicato
     ```ml
     fun filter p [] = []
       | filter p (x::xs) = 
         if p(x) then x::filter p xs else filter p xs;
     ```
   - **map**: applica funzione a ogni elemento
     ```ml
     fun map f [] = []
       | map f (x::xs) = f(x)::map f xs;
     ```
   - **reduce** (fold): accumula valore applicando funzione
     ```ml
     fun reduce f init [] = init
       | reduce f init (x::xs) = f(x, reduce f init xs);
     ```
   - **Funzioni Anonime**:
     ```ml
     map (fn x => x * 2) [1, 2, 3, 4, 5];
     filter (fn x => x > 3) [1, 2, 3, 4, 5];
     ```

10. **Polimorfismo Parametrico**
    - Funzioni che lavorano con qualsiasi tipo
    - Type variables (generici): `'a`, `'b`, ecc.
    - Esempio:
      ```ml
      fun length [] = 0
        | length (x::xs) = 1 + length xs;
      (* tipo: 'a list -> int *)
      (* funziona per qualsiasi tipo di lista *)
      ```
    - Vantaggi: riutilizzabilità, sicurezza di tipo

11. **Encapsulation e Interfacce**
    - **Signature**: definisce contratto (firma) di modulo
      ```ml
      signature STACK = sig
        type 'a stack
        val empty: 'a stack
        val push: 'a * 'a stack -> 'a stack
        val pop: 'a stack -> 'a stack
      end;
      ```
    - **Structure**: implementazione di una signature
      ```ml
      structure Stack :> STACK = struct
        type 'a stack = 'a list
        val empty = []
        fun push(x, s) = x::s
        fun pop([]) = []
          | pop(x::xs) = xs
      end;
      ```
    - **Functor**: parametrizza su altre strutture (simile a template C++)

12. **Eccezioni**
    - Meccanismo per gestire errori
    - Dichiarazione: `exception NomEccezione of tipo`
    - Sollevamento: `raise NomEccezione valore`
    - Cattura:
      ```ml
      (fn () => 
        if x = 0 then raise Errore else y / x
      ) handle Errore => 0;
      ```

13. **Integrazione con Type Checking**
    - Sistema di tipi previene molti errori
    - Type inference riduce annotazioni necessarie
    - Eccezioni per errori runtime

**Errori Comuni:**
- ❌ Tentare di mutare una variabile (dimenticare che è immutabile)
- ❌ Confondere list e tuple
- ❌ Non capire currying e applicazione parziale
- ❌ Pensare che map/filter/reduce cambino la lista originale (immutabile)
- ❌ Non usare pattern matching adeguatamente

---

### FASE 6: Paradigma Logico - Prolog (3-4 giorni)

#### Capitolo 6: Prolog e Paradigma Logico

**Cosa devi sapere:**

1. **Introduzione al Paradigma Logico**
   - Basato sulla logica del primo ordine
   - Descrivi le **relazioni**, non i **procedimenti**
   - Sistema trova soluzioni cercando tra tutte le possibilità (backtracking)

2. **Costrutti di Base**
   - **Fatto** (Fact): affermazione sempre vera
     ```prolog
     parent(tom, bob).
     parent(tom, liz).
     mother(X) :- female(X), parent(X, _).
     ```
   
   - **Query**: domanda al sistema
     ```prolog
     ?- parent(tom, bob).        % risposta: true
     ?- parent(tom, X).          % risposta: X = bob; X = liz
     ```
   
   - **Variabili Logiche**: iniziano con maiuscola
     - `X`, `Y`, `Parent`
     - Rappresentano incognite da trovare
     - `_` è wildcard (variabile anonima)
   
   - **Termini**: elementi base di Prolog
     - Costanti: `tom`, `42`
     - Variabili: `X`, `Parent`
     - Strutture composte: `parent(tom, bob)`, `f(a, g(b))`
   
   - **Alberi di Termini**:
     ```
     parent(tom, bob)
     ├── parent (functor)
     ├── tom (costante)
     └── bob (costante)
     ```

3. **Regole**
   - Implicazioni logiche (se-allora)
   - Forma: `head :- body`
   - Esempio:
     ```prolog
     grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
     ```
   - Interpretazione: "X è nonno di Z se X è padre di qualcuno (Y) e Y è padre di Z"

4. **Struttura di un Programma Prolog**
   - Fatti e regole
   - Query poste al sistema
   - Sistema risponde con soluzioni o no

5. **Query Semplici**
   - Unificazione con fatti
   - Esempio:
     ```prolog
     ?- parent(tom, bob).
     true.
     ```

6. **Sostituzione e Istanze**
   - **Sostituzione**: assegnazione di valori a variabili
   - **Istanza**: risultato dell'applicazione di sostituzione
   - Esempio: `parent(tom, bob)` è istanza di `parent(tom, X)` con `{X/bob}`

7. **Unificazione**
   - Processo di rendere due termini uguali attraverso sostituzione
   - **Algoritmo**:
     1. Confronta due termini
     2. Se uguali: successo (sostituzione vuota)
     3. Se uno è variabile: unificazione con altro
     4. Se functor e arity uguali: unificazione ricorsiva degli argomenti
     5. Altrimenti: fallimento
   - Esempio:
     ```prolog
     parent(X, bob) unifica parent(tom, Y)
     con sostituzione: {X/tom, Y/bob}
     ```

8. **Vincoli su Alberi**
   - Strutture annidati devono corrispondere
   - Unificazione fallisce se strutture incompatibili

9. **Overloading e Wildcards**
   - Stesso predicato con diverse arità
   - `_` per variabili non usate
   - Esempio:
     ```prolog
     parent(tom, bob).
     parent(tom, bob, source(book)).  % diversa arità
     ```

10. **Liste in Prolog**
    - Sintassi: `[1, 2, 3, 4, 5]`
    - Cons: `[H|T]` dove H è testa, T è coda
    - Operazioni:
      - `append(L1, L2, L3)`: concatena L1 e L2 in L3
      - `length(L, N)`: lunghezza di L è N
      - `member(X, L)`: X è membro di L
      - `last(L, X)`: ultimo elemento di L è X
      - `reverse(L, R)`: R è L invertita

11. **Calcolo Simbolico in Prolog**
    - Manipolazione di simboli e strutture
    - Utilità per programmazione logica

12. **Programmazione Nondeterministica**
    - Programma ha multiple scelte
    - Prolog esplora tutte le alternative

13. **Backtracking**
    - Meccanismo di ricerca
    - Quando una strada fallisce, torna indietro e prova altre strade
    - Esempio:
      ```prolog
      ?- parent(tom, X).
      X = bob ;  % prima soluzione
      X = liz ;  % seconda soluzione (dopo `;` richiedi altre)
      no.        % no più soluzioni
      ```
    - Imperativo: `!` (cut) ferma il backtracking

**Errori Comuni:**
- ❌ Confondere fatti con regole
- ❌ Non capire unificazione
- ❌ Pensare a Prolog come linguaggio imperativo (è dichiarativo!)
- ❌ Struttura scorretta della lista (dimenticare `|`)
- ❌ Uso errato di variabili (iniziali maiuscoli)

---

<a name="mappe-concettuali"></a>
## 🗺️ MAPPE CONCETTUALI

### Mappa 1: Struttura Generale Linguaggi di Programmazione

```
LINGUAGGIO DI PROGRAMMAZIONE
│
├─ DEFINIZIONE: Comunicazione programmatore-calcolatore
│  └─ Elemento distintivo: programma (soluzione a problema)
│
├─ MACCHINA ASTRATTA
│  ├─ Memoria (Locazioni → Valori)
│  ├─ Processore (fetch-decode-execute)
│  └─ Implementazione: HW, SW, FW
│
├─ TRADUZIONE
│  ├─ Compilazione (tutto prima, poi esecuzione)
│  │  └─ Fasi: token → AST → codice oggetto
│  └─ Interpretazione (traduce ed esegue insieme)
│     └─ Ibrido (Java: compile a bytecode, interpreta)
│
├─ PROPRIETÀ
│  ├─ Semplicità
│  ├─ Astrazione
│  ├─ Espressività
│  ├─ Ortogonalità
│  └─ Portabilità
│
└─ PARADIGMI
   ├─ Imperativo: stato mutabile + comandi
   ├─ Funzionale: funzioni pure, no mutabilità
   ├─ Logico: relazioni + backtracking
   ├─ OO: oggetti + messaggi
   └─ Parallelo: entità distribuite (ortogonale)
```

### Mappa 2: Paradigma Imperativo - Esecuzione

```
PARADIGMA IMPERATIVO
│
├─ STATO (memoria)
│  └─ mem: Locazioni → Valori
│
├─ ASSEGNAZIONE (operazione centrale)
│  ├─ Recupera indirizzo locazione
│  ├─ Recupera valori
│  ├─ Calcola
│  └─ Memorizza risultato
│
├─ VARIABILI E BINDING
│  ├─ Name Binding: nome ↔ locazione
│  └─ Value Binding: nome ↔ valore
│
├─ SCOPE
│  ├─ Statico (struttura codice)
│  └─ Dinamico (catena di chiamate)
│
└─ STACK DI ATTIVAZIONE
   └─ Record di Attivazione (AR)
      ├─ Parametri
      ├─ Variabili locali
      ├─ Indirizzo ritorno
      └─ Link dinamici/statici
```

### Mappa 3: Astrazione Procedurale

```
ASTRAZIONE PROCEDURALE
│
├─ PROCEDURA
│  ├─ Raggruppamento istruzioni
│  ├─ Riutilizzabilità
│  └─ Modularità
│
├─ AMBIENTE PROCEDURA
│  ├─ Record di Attivazione (AR)
│  │  ├─ Parametri formali
│  │  ├─ Variabili locali
│  │  ├─ Dynamic Link (procedura precedente)
│  │  └─ Static Link (ambiente non-locale)
│  ├─ Ambiente Locale (variabili della procedura)
│  └─ Ambiente Non-Locale (variabili da procedure esterne)
│
├─ PARAMETRIZZAZIONE
│  ├─ Pass-by-Value: copia valore
│  ├─ Pass-by-Reference: copia indirizzo
│  ├─ Pass-by-Name: sostituzione testuale
│  └─ Pass-by-Result: copia al ritorno
│
├─ ALIASING
│  └─ Due nomi → stessa locazione (pericolo!)
│
└─ VETTORE AMBIENTI NON-LOCALI
   └─ Accesso diretto vs. catena (trade-off spazio/tempo)
```

### Mappa 4: Java OOP - Gerarchia

```
JAVA OBJECT-ORIENTED
│
├─ TIPI
│  ├─ Primitivi: int, double, boolean, char, ...
│  │  └─ Stack
│  └─ Reference: classi, interfacce, array
│     └─ Heap (garbage collected)
│
├─ CLASSE
│  ├─ Attributi (dati)
│  ├─ Metodi (comportamento)
│  ├─ Costruttore (inizializzazione)
│  └─ Modificatori (public, private, protected)
│
├─ CICLO DI VITA OGGETTO
│  ├─ Scrittura → Compilazione → Caricamento
│  ├─ Verifica bytecode → Esecuzione
│  └─ Garbage collection
│
├─ EREDITARIETÀ
│  ├─ extends (singola)
│  ├─ super
│  └─ Tutti ereditano da Object
│
├─ POLIMORFISMO
│  ├─ Overloading: stesso nome, parametri diversi (compile-time)
│  └─ Override: ridefinizione metodo (runtime)
│
├─ INTERFACCE
│  ├─ Contratto (cosa fare)
│  ├─ Multiple implementation
│  └─ Decoupling
│
├─ ECCEZIONI
│  ├─ Checked: obbligatorio catturare
│  ├─ Unchecked: facoltativo
│  └─ try-catch-finally
│
└─ CLASSI INTERNE
   ├─ Membro
   ├─ Membro statica
   ├─ Locale
   └─ Anonima
```

### Mappa 5: Paradigma Funzionale - ML

```
PARADIGMA FUNZIONALE (ML)
│
├─ CARATTERISTICHE
│  ├─ Funzioni pure (no side effects)
│  ├─ Immutabilità (no state mutabile)
│  ├─ Ricorsione (iterazione)
│  └─ First-class functions
│
├─ DICHIARAZIONI
│  ├─ val (immutabile)
│  ├─ fun (funzione)
│  └─ datatype (tipo algebrico)
│
├─ TIPI STRUTTURATI
│  ├─ Tupla: (1, "hello", true)
│  ├─ Record: {x: int, y: int}
│  └─ Datatype: Red | Green | Blue
│
├─ PATTERN MATCHING
│  └─ Decomposizione valori strutturati
│
├─ LISTE
│  ├─ [1, 2, 3, 4, 5]
│  ├─ H::T (cons)
│  └─ map, filter, reduce
│
├─ CURRYING
│  ├─ Applicazione parziale
│  └─ Composizione funzioni
│
├─ FUNZIONI ORDINE SUPERIORE
│  ├─ map: applica funzione
│  ├─ filter: seleziona
│  ├─ reduce: accumula
│  └─ Anonime: fn x => x * 2
│
├─ POLIMORFISMO PARAMETRICO
│  ├─ Type variables: 'a, 'b
│  └─ Funzioni generiche
│
└─ ENCAPSULATION
   ├─ Signature (contratto)
   ├─ Structure (implementazione)
   └─ Functor (parametrico)
```

### Mappa 6: Paradigma Logico - Prolog

```
PARADIGMA LOGICO (PROLOG)
│
├─ ELEMENTI BASE
│  ├─ Fatti: affermazioni vere
│  ├─ Regole: implicazioni logiche
│  ├─ Query: domande
│  └─ Termini: costanti, variabili, strutture
│
├─ UNIFICAZIONE
│  ├─ Rendere due termini uguali
│  ├─ Sostituzione di variabili
│  └─ Algoritmo ricorsivo
│
├─ BACKTRACKING
│  ├─ Ricerca tutte le soluzioni
│  ├─ Esplorazione dello spazio di ricerca
│  └─ Cut (!) per fermare
│
├─ LISTE
│  ├─ [1, 2, 3, 4, 5]
│  ├─ [H|T]
│  └─ append, member, length, reverse
│
├─ PROGRAMMAZIONE NONDETERMINISTICA
│  └─ Multiple scelte esplorate sistematicamente
│
└─ CALCOLO SIMBOLICO
   └─ Manipolazione simboli e strutture
```

---

<a name="domande-ripasso"></a>
## ❓ DOMANDE DI RIPASSO (150+ Domande)

### LIVELLO BASE: Definizioni e Concetti Fondamentali (50 domande)

#### Linguaggi di Programmazione e Macchine Astratte (10 domande)
1. Che cos'è un linguaggio di programmazione e come differisce da un linguaggio naturale?
2. Spiega brevemente i quattro elementi chiave presenti nella definizione di linguaggio di programmazione (processore, programma, persona, problema).
3. Che cos'è una macchina astratta? Quali sono le sue componenti principali?
4. Quali sono le tre modalità di implementazione di una macchina astratta?
5. Spiega il ciclo di esecuzione (fetch-decode-execute) di un processore.
6. Qual è la differenza tra compilazione e interpretazione?
7. Che cos'è il bytecode e qual è il suo ruolo in Java?
8. Elenca le proprietà desiderabili di un linguaggio di programmazione.
9. Spiega il concetto di "ortogonalità" nel contesto dei linguaggi di programmazione.
10. Che cos'è un paradigma di programmazione?

#### Paradigma Imperativo (15 domande)
11. Qual è il principio fondamentale del paradigma imperativo?
12. Come viene astratta la memoria nel paradigma imperativo?
13. Che cos'è una variabile e cosa rappresenta nel paradigma imperativo?
14. Spiega la differenza tra name binding e location binding.
15. Che cosa si intende per "scope" di una variabile?
16. Qual è la differenza tra scope statico e scope dinamico?
17. Che cos'è lo stack di attivazione e perché è importante?
18. Spiega i concetti di "dynamic link" e "static link" nel record di attivazione.
19. Che cosa sono i puntatori e come si usano?
20. Quali sono i due tipi di "legame di tipo" (static e dynamic typing)?
21. Che cos'è lo "shadowing" di una variabile?
22. Spiega la differenza tra "strong typing" e "weak typing".
23. Quale ruolo gioca il compiler nel type checking?
24. Che cosa significa che una variabile è "effectively final"?
25. Come viene gestita la memoria nello stack e nell'heap?

#### Astrazione Procedurale (10 domande)
26. Che cos'è un record di attivazione e cosa contiene?
27. Quale è la differenza tra parametri formali e parametri attuali?
28. Spiega il passaggio per valore (pass-by-value).
29. Spiega il passaggio per riferimento (pass-by-reference).
30. Cosa si intende per "aliasing" in una procedura?
31. Che differenza c'è tra pass-by-name e macro?
32. Cosa sono le procedure di ordine superiore?
33. Come funziona il vettore degli ambienti non-locali?
34. Che cos'è una closure in programmazione?
35. Spiega il concetto di "nesting" di procedure.

#### Java e OOP (15 domande)
36. Qual è la differenza tra una classe e un oggetto?
37. Che cos'è un costruttore e quale è il suo ruolo?
38. Cosa significa che Java è "pass-by-value"?
39. Spiega la parola chiave `this` in Java.
40. Qual è la differenza tra tipi primitivi e tipi reference in Java?
41. Che cosa si intende per "ereditarietà singola"?
42. Spiega la parola chiave `super` e i suoi usi.
43. Che differenza c'è tra overloading e override?
44. Cos'è il polimorfismo e come si manifesta in Java?
45. Spiega il concetto di "garbage collection".
46. Qual è il ruolo della classe `Object`?
47. Che cos'è un'interfaccia e come si differenzia da una classe astratta?
48. Spiega i modificatori di accesso (public, protected, private, package-private).
49. Che cosa si intende per "incapsulamento"?
50. Spiega le differenze tra checked e unchecked exception.

### LIVELLO INTERMEDIO: Applicazione e Comprensione (50 domande)

#### Paradigma Imperativo - Esercizi (12 domande)
51. Scrivi lo pseudocodice di una funzione che calcola il fattoriale usando l'assegnazione.
52. Dato il seguente codice imperativo, traccia l'esecuzione e determina lo stack di attivazione:
    ```
    procedure factorial(n)
      if n = 1 then return 1
      else return n * factorial(n-1)
    end
    ```
53. Spiega cosa accade con lo scope statico vs. dinamico nel seguente caso:
    ```
    x = 10
    procedure A()
      x = 20
      B()
    procedure B()
      print x
    A()
    ```
54. Dato il passaggio di parametri per valore e per riferimento, quale sceglieresti per una lista di 1000 elementi e perché?
55. Illustra il problema di aliasing con un esempio concreto.
56. Scrivi la definizione di una procedura che implementa il merge di due array ordinati.
57. Spiega come il compilatore risolve i nomi di variabili usando la symbol table.
58. Decomponi il processo di esecuzione di un'assegnazione a basso livello.
59. Traccia l'evoluzione dello stack di attivazione in una sequenza di chiamate ricorsive.
60. Quale è l'impatto del passaggio di parametri per riferimento su aliasing e performance?
61. Spiega come il vettore degli ambienti non-locali migliora le prestazioni rispetto al static link.
62. Confronta il memory layout di un programma imperativo con uno funzionale.

#### Java e OOP - Esercizi (15 domande)
63. Scrivi una classe `Person` con attributi name, age e metodo per stampare le informazioni.
64. Progetta una gerarchia di classi per rappresentare animali domestici (Dog, Cat, Bird).
65. Implementa un metodo che verifica se due oggetti `Person` sono uguali (override `equals`).
66. Spiega il ciclo di compilazione e esecuzione di un programma Java.
67. Traccia l'esecuzione di:
    ```java
    Integer x = new Integer(5);
    Integer y = x;
    y = 10;
    System.out.println(x); // Cosa stampa?
    ```
68. Implementa un'interfaccia `Shape` con metodi `area()` e `perimeter()`.
69. Spiega il problema del downcast e come risolverlo con `instanceof`.
70. Scrivi un metodo che accetta un array di qualsiasi tipo (generics).
71. Implementa una classe con costruttore che chiama un altro costruttore (`this`).
72. Spiega il flusso di esecuzione di costruttori in una gerarchia di ereditarietà.
73. Implementa una classe interna (inner class) e spiega i vantaggi.
74. Scrivi un gestore di eccezioni per leggere da file.
75. Confronta l'uso di classe astratta vs. interfaccia in un esempio pratico.
76. Implementa autoboxing/unboxing e spiega quando è conveniente.
77. Spiega il Memory Model di Java per variabili `volatile`.

#### Paradigma Funzionale - Esercizi (12 domande)
78. Scrivi una funzione ricorsiva in ML che calcola il fattoriale.
79. Implementa la funzione `map` in ML e spiega il suo tipo.
80. Scrivi una funzione che filtra una lista di interi e ritorna solo i pari.
81. Dimostra il currying implementando una funzione `add` curried.
82. Implementa la funzione `reduce` (fold) in ML.
83. Scrivi una funzione che usa pattern matching su una tupla.
84. Implementa un datatype per rappresentare un albero binario.
85. Spiega il concetto di "lazy evaluation" e quando è utile.
86. Scrivi una funzione anonima che moltiplica per 2 ogni elemento di una lista.
87. Implementa una firma (signature) e una struttura (structure) per uno stack.
88. Traccia l'esecuzione di una composizione di funzioni in ML.
89. Spiega il polimorfismo parametrico con un esempio.

#### Paradigma Logico - Esercizi (11 domande)
90. Scrivi un programma Prolog che definisce una relazione di parentela.
91. Scrivi una query che trova tutti i padri di "bob".
92. Implementa il predicato `member/2` in Prolog.
93. Scrivi il predicato `append/3` che concatena due liste.
94. Traccia l'unificazione di `parent(X, bob)` con `parent(tom, Y)`.
95. Spiega il processo di backtracking in Prolog con un esempio.
96. Implementa il predicato `length/2` in Prolog.
97. Scrivi una regola che verifica se una lista è ordinata.
98. Spiega l'uso del cut (!) in Prolog.
99. Implementa un fatto e una regola per calcolare il fattoriale in Prolog.
100. Scrivi un programma che risolve il problema delle N regine.

### LIVELLO AVANZATO: Analisi e Sintesi (50 domande)

#### Analisi Comparativa tra Paradigmi (15 domande)
101. Confronta il paradigma imperativo e funzionale nella soluzione dello stesso problema.
102. Spiega i vantaggi e svantaggi dell'uso di paradigma logico rispetto a imperativi.
103. Quando è preferibile usare Java (OOP) rispetto a ML (funzionale)? Fornisci esempi.
104. Analizza la differenza in terms di memoria tra imperative e funzionale.
105. Come il garbage collector in Java cambia la prospettiva rispetto a gestione manuale in C?
106. Confronta il sistema di tipi in Java vs. ML (static, dynamic, type inference).
107. Spiega come i paradigmi differenti affrontano il problema della ricorsione.
108. Quali sono i vantaggi della programmazione logica nel domain di knowledge representation?
109. Confronta la composizione di funzioni in ML con l'ereditarietà in Java.
110. Analizza il trade-off tra semplicità e espressività in diversi paradigmi.
111. Spiega come il polimorfismo ad hoc (overloading) si differenzia da parametrico.
112. Quale paradigma è più adatto per la programmazione parallela e perché?
113. Confronta il ruolo delle variabili nei diversi paradigmi.
114. Analizza la "impedance mismatch" tra il paradigma relazionale (DB) e OOP.
115. Spiega come i diversi paradigmi affrontano il concetto di "state".

#### Design e Architettura (12 domande)
116. Progetta una gerarchia di classi per un sistema bancario.
117. Come useresti le interfacce per implementare il pattern Strategy?
118. Spiega il principio di "separation of concerns" e come realizzarlo.
119. Implementa il pattern Singleton in Java (con considerazioni thread-safety).
120. Progetta una architettura software usando MVC (Model-View-Controller).
121. Come useresti la programmazione funzionale per evitare deadlock?
122. Spiega il pattern Factory Method e i vantaggi.
123. Implementa il pattern Observer usando classi interne anonime.
124. Confronta l'uso di ereditarietà vs. composizione in un design.
125. Come useresti Prolog per fare "planning" in AI?
126. Progetta una API per manipolare file usando le best practices.
127. Spiega il pattern Decorator e implementalo in Java.

#### Questioni di Performance e Correctness (12 domande)
128. Analizza la complessità temporale e spaziale di una procedura ricorsiva imperative.
129. Quale è l'impatto del pass-by-reference sulla performance? E sulla correctness?
130. Spiega come il tail-call optimization migliora performance in ML.
131. Confronta la performance di array statici vs. liste dinamiche.
132. Come il type checking statico previene errori a runtime?
133. Spiega il problema di "thrashing" dello stack di attivazione.
134. Quale è l'impatto della garbage collection sulla performance?
135. Analizza il memory leak in Java e come prevederlo.
136. Come l'immutabilità in ML migliora la thread-safety?
137. Spiega il problema di "double-checked locking" in Java.
138. Quale è il costo di virtual method dispatch in Java?
139. Analizza l'impatto del currying sulla readability e performance.

#### Questioni Teoriche Profonde (11 domande)
140. Dimostra che Java è computazionalmente completo (Turing-complete).
141. Spiega il problema dell'indecidibilità della terminazione dei programmi.
142. Confronta il lambda calculus con il paradigma imperativo.
143. Illustra il concetto di "closure" dal punto di vista della semantica.
144. Spiega la "Church-Turing thesis" e il suo significato per i linguaggi.
145. Come la logica del primo ordine sottende il paradigma logico?
146. Analizza la "homoiconicity" nel contesto di Lisp/ML.
147. Spiega il significato di "lazy evaluation" formalmente.
148. Quale è la relazione tra monade e side effects in linguaggi funzionali?
149. Analizza il problema di "evaluation order" nei diversi paradigmi.
150. Spiega il concetto di "type safety" formalmente.

---

<a name="simulazioni"></a>
## 🧪 SIMULAZIONI D'ESAME

### SIMULAZIONE 1: Esame Teorico (1 ora)

**Domanda 1 (Concetti Fondamentali, 15 punti)**
Spiega cosa sia un linguaggio di programmazione e come si differenzi da un linguaggio naturale. Illustra il ruolo della macchina astratta in questo contesto, descrivendo le sue componenti principali e modalità di implementazione.

**Domanda 2 (Paradigma Imperativo, 20 punti)**
Descrivi il paradigma imperativo. Illustra i concetti di:
- Assegnazione e sua implementazione a basso livello
- Scope statico vs. dinamico
- Stack di attivazione e record di attivazione
- Pass-by-value vs. pass-by-reference

Fornisci un esempio concreto per ogni concetto.

**Domanda 3 (Java e OOP, 25 punti)**
Spiega l'ereditarietà e il polimorfismo in Java. Come si differenziano overloading e override? Illustra con codice.

**Domanda 4 (Paradigma Funzionale, 20 punti)**
Confronta il paradigma funzionale con quello imperativo. Spiega currying e funzioni di ordine superiore (map, filter, reduce). Implementa `map` in ML.

**Domanda 5 (Paradigma Logico, 20 punti)**
Descrivi il paradigma logico. Spiega i concetti di unificazione e backtracking. Scrivi un semplice programma Prolog.

---

### SIMULAZIONE 2: Esame Pratico - Java (1.5 ore)

**Esercizio 1 (Classi e Oggetti, 30 punti)**
Implementa una classe `BankAccount` con:
- Attributi: `accountNumber` (String), `balance` (double), `owner` (String)
- Metodi: `deposit(double)`, `withdraw(double)`, `getBalance()`, `toString()`
- Costruttore che inizializza account number, owner, e balance a 0
- Gestione di eccezioni per withdraw con balance insufficiente

**Esercizio 2 (Ereditarietà e Polimorfismo, 35 punti)**
Crea una gerarchia di classi:
- Superclasse `Vehicle` con attributi `make`, `model`, `year`
- Sottoclassi: `Car`, `Truck`, `Motorcycle`
- Implementa un metodo `getDescription()` specifico per ogni tipo
- Crea un array di vehicle e stampa le descrizioni (polimorfismo)

**Esercizio 3 (Array e Algoritmi, 20 punti)**
Scrivi un metodo che:
- Accetta un array di interi
- Ritorna un nuovo array con elementi ordinati (usa sorting)
- Usa il metodo `Arrays.sort()` della libreria standard

**Esercizio 4 (Eccezioni, 15 punti)**
Scrivi un metodo che legge un file e gestisce le possibili eccezioni.

---

### SIMULAZIONE 3: Esame Pratico - ML (1.5 ore)

**Esercizio 1 (Ricorsione e Matching, 25 punti)**
Scrivi una funzione ML che:
- Calcola il fattoriale usando ricorsione
- Calcola la lunghezza di una lista usando pattern matching
- Implementa una funzione che somma tutti gli elementi di una lista

**Esercizio 2 (Funzioni di Ordine Superiore, 35 punti)**
- Implementa `map`, `filter`, e `reduce` per liste
- Scrivi funzioni anonime che:
  - Moltiplicano ogni elemento per 2
  - Selezionano solo numeri pari
  - Calcolano la somma di una lista
- Testa tutte le funzioni con esempi

**Esercizio 3 (Datatype e Pattern Matching, 20 punti)**
- Definisci un datatype per rappresentare espressioni aritmetiche: `Num of int | Plus of expr * expr | Minus of expr * expr | Mult of expr * expr`
- Scrivi una funzione che valuta l'espressione
- Implementa una funzione che stampa l'espressione

**Esercizio 4 (Currying e Composizione, 20 punts)**
- Implementa una funzione `add` curried
- Scrivi una funzione di composizione che combina due funzioni

---

### SIMULAZIONE 4: Esame Pratico - Prolog (1 ora)

**Esercizio 1 (Fatti e Query, 20 punti)**
Scrivi un programma Prolog che:
- Definisce fatti di parentela
- Risponde a query sul padre, madre, nonno, ecc.

**Esercizio 2 (Liste e Ricorsione, 30 punti)**
- Implementa `member/2`
- Implementa `append/3`
- Implementa `reverse/2`
- Implementa `last/2`

**Esercizio 3 (Regole e Backtracking, 30 punts)**
- Definisci una regola che verifica se una lista è ordinata
- Implementa un risolutore di permutazioni
- Implementa il problema delle N regine (versione semplificata)

**Esercizio 4 (Calcolo e Unificazione, 20 punti)**
- Scrivi una query che calcola tutte le soluzioni
- Demonstra il backtracking trovando tutte le soluzioni

---

<a name="tecniche-studio"></a>
## 📖 TECNICHE DI STUDIO PERSONALIZZATE

### 1. Metodo Feynman
Applica questa tecnica per ogni concetto:

1. **Leggi il capitolo** della guida o del libro
2. **Copri il testo** e spiega il concetto a voce alta come se insegnassi a un bambino di 10 anni
3. **Identifica le lacune** - se non riesci a spiegare qualcosa, rileggi
4. **Semplifica il linguaggio** - usa parole semplici, non terminologia complessa
5. **Usa analogie** - collega a concetti che conosci già

**Esempio:**
```
Concetto: Pass-by-value
Spiegazione Feynman:
"Immagina che tuo cugino ha il numero di telefono di un amico.
Se tu copii il numero su un foglio, puoi perdere il foglio ma il 
tuo cugino ha ancora il numero vero. Questo è pass-by-value."
```

### 2. Spaced Repetition
Rivedi il materiale con questa tempistica:
- **Giorno 1**: Primo contatto (durante la lezione/lettura)
- **Giorno 2**: Rivedi il capitolo (senza leggere tutto, solo titoli)
- **Giorno 4**: Risolvi esercizi sulla prima parte
- **Giorno 7**: Prova a spiegare senza consultare il materiale
- **Giorno 14**: Rivedi capitoli differenti
- **Giorno 30**: Fai una simulazione d'esame parziale

**Tool suggeriti**: Anki, Quizlet

### 3. Active Recall
Non leggere passivamente, ma testa la tua memoria:

1. Leggi una sezione
2. Chiudi il libro
3. Scrivi tutto quello che ricordi
4. Confronta e correggi
5. Ripeti il ciclo

### 4. Elaborazione Concettuale (Concept Mapping)
Per ogni argomento principale, crea una mappa concettuale:
```
PARADIGMA IMPERATIVO
    ├─ Principio: stato mutabile
    ├─ Operazione centrale: assegnazione
    ├─ Memoria: locazioni → valori
    ├─ Scope: statico/dinamico
    └─ Stack di attivazione
```

### 5. Deliberate Practice (Pratica Mirata)
Non fare esercizi a caso, ma strategicamente:

1. **Scegli un argomento specifico** (es. ereditarietà in Java)
2. **Fai esercizi di difficoltà crescente**:
   - Facile: 2-3 esercizi per comprensione
   - Medio: 3-4 esercizi per applicazione
   - Difficile: 1-2 esercizi per sintesi
3. **Traccia il tuo progresso** (quanti ricordi senza aiuti?)
4. **Aumenta gradualmente la difficoltà**

### 6. Insegnare ad Altri
La migliore verifica di comprensione:

1. Spiega il concetto a un compagno
2. Insegna a qualcuno che non conosce il materiale
3. Scrivi un blog post o tutorial (anche solo per te)
4. Rispondi alle domande altrui nel forum

### 7. Esercizi di Coding Incrementali

**Settimana 1: Paradigma Imperativo**
```
Giorno 1: Scrivi un programma che calcola il fattoriale
Giorno 2: Aggiungi gestione di array
Giorno 3: Implementa stack manualmente
Giorno 4: Traccia lo stack di attivazione a mano
Giorno 5: Esercizi misti
```

**Settimana 2: Java OOP**
```
Giorno 1: Scrivi una classe semplice
Giorno 2: Aggiungi ereditarietà
Giorno 3: Implementa polimorfismo
Giorno 4: Usa interfacce
Giorno 5: Gestisci eccezioni
```

### 8. Problem-Solving Strutturato
Per ogni esercizio, segui questo schema:

1. **Comprensione**: Rileggi il problema 3 volte
2. **Analisi**: Quali concetti sono coinvolti?
3. **Piano**: Scrivi lo pseudocodice
4. **Implementazione**: Codifica
5. **Verifica**: Test con vari input
6. **Riflessione**: Cosa ho imparato? Potevo farlo meglio?

### 9. Revisione Critica
Dopo aver risolto un esercizio:
1. Leggi il codice di un compagno
2. Confronta con una soluzione del professore (se disponibile)
3. Annota differenze e miglioramenti
4. Rifa l'esercizio con le lezioni apprese

### 10. Integrazione tra Paradigmi
Confronta come lo stesso problema si risolverebbe in diversi paradigmi:

```
PROBLEMA: Sommare una lista di numeri

IMPERATIVO (Java):
int sum = 0;
for(int x : list) sum += x;

FUNZIONALE (ML):
val sum = reduce (+) 0 list

LOGICO (Prolog):
sum([], 0).
sum([H|T], S) :- sum(T, S1), S is H + S1.
```

---

<a name="consigli-pratici"></a>
## 💡 CONSIGLI PRATICO-ORGANIZZATIVI

### Pianificazione dello Studio
1. **Suddividi il corso in 6 fasi** (vedi Argomenti Core)
2. **Assegna 1-2 settimane per fase** (totale 6-12 settimane)
3. **Dedica 3-4 ore al giorno**:
   - 1 ora: teoria (leggi, mappa concettuale)
   - 1.5 ore: esercizi
   - 1-1.5 ore: revisione, elaborazione

### Risorse di Studio
- **Appunti ufficiali**: Bonatti - UNINA Official Docs (questo file!)
- **Libri consigliati**: 
  - "Programming Languages: Application and Interpretation"
  - "Concepts of Programming Languages" (Sebesta)
- **Online**:
  - Documentazione ufficiale Java
  - Interactive tutors per ML (SML/NJ)
  - SWI-Prolog tutorial
- **Video**:
  - Video lezioni online (Coursera, YouTube)
  - Demo di concetti difficili

### Gestione dell'Ansia durante l'Esame
1. **Leggi tutte le domande prima di iniziare** (5 minuti)
2. **Alloca il tempo**:
   - Domande facili: 15% tempo
   - Domande medie: 50% tempo
   - Domande difficili: 35% tempo
3. **Inizia dalle domande che conosci bene** (confidence boost)
4. **Se blocchi**: passa alla prossima, torna dopo
5. **Verifica finale**: rileggi tutte le risposte (5 minuti)

### Time Management
```
MESI 1-2: Fondamenti + Paradigma Imperativo
├─ Settimana 1: Concetti base
├─ Settimana 2: Assegnazione, variabili, scope
├─ Settimana 3: Stack di attivazione
├─ Settimana 4: Esercizi integrati

MESI 2-3: Astrazione Procedurale + Java
├─ Settimana 1: Record di attivazione, parametri
├─ Settimana 2-4: Java basics (classi, oggetti)
├─ Settimana 5: Ereditarietà e polimorfismo
├─ Settimana 6: Interfacce, eccezioni, inner classes
├─ Settimana 7: Esercizi integrati

MESE 4: Paradigma Funzionale (ML)
├─ Settimana 1: Dichiarazioni, tipi strutturati
├─ Settimana 2: Pattern matching, liste
├─ Settimana 3: Currying, HOF
├─ Settimana 4: Esercizi integrati

MESE 4-5: Paradigma Logico (Prolog)
├─ Settimana 1: Fatti, query, unificazione
├─ Settimana 2: Liste, backtracking
├─ Settimana 3: Esercizi integrati

SETTIMANA FINALE: Revision + Mock Exam
├─ Giorni 1-2: Revisione generale
├─ Giorni 3-4: Simulazione esame
├─ Giorni 5-6: Revisione errori
├─ Giorno 7: Riposo
```

### Struttura di una Sessione di Studio Efficace (3 ore)
```
0:00-0:05   Riscaldamento (leggi titoli capitolo)
0:05-0:35   Lettura attiva (Feynman method)
0:35-0:45   Pausa + caffè
0:45-1:15   Esercizi (problem-solving)
1:15-1:30   Pausa
1:30-2:15   Più esercizi + traccia manuale
2:15-2:45   Elaborazione (mappa concettuale, spiega)
2:45-3:00   Revisione e domande aperte
```

### Errori da Evitare
1. ❌ Leggere passivamente senza esercitarsi
2. ❌ Posticipare lo studio fino all'ultima settimana
3. ❌ Saltare la teoria per saltare subito agli esercizi
4. ❌ Non fare revisioni periodiche (spaced repetition)
5. ❌ Studiare solo tardi di sera (concentrazione cala)
6. ❌ Fare esercizi senza confrontare le soluzioni
7. ❌ Non scrivere il codice (solo leggere non basta)
8. ❌ Concentrarsi su un paradigma trascurando gli altri
9. ❌ Non capire prima di memorizzare
10. ❌ Studiare in ambienti rumorosi o con distrazioni

### Risorse per la Tua Zona di Studio
- Quiete (biblioteca, stanza tranquilla)
- Materiali: penna, carta, computer
- Niente telefono durante le sessioni
- Illuminazione adeguata
- Snack e acqua a portata di mano

### Day Before the Exam
```
✓ Rivedi le mappe concettuali (30 min)
✓ Ripassa i termini chiave (20 min)
✓ Risolvi 1-2 esercizi brevi (30 min)
✓ Riposa 8 ore
✓ Mangia bene il mattino
✓ Arriva 15 min prima
```

---

## 📝 CHECKLIST FINALE

Prima di affrontare l'esame, verifica di:

### Teoria
- [ ] Capire cos'è un linguaggio di programmazione
- [ ] Spiegare il paradigma imperativo senza consultare note
- [ ] Descrivere il stack di attivazione e record di attivazione
- [ ] Differenziare pass-by-value e pass-by-reference
- [ ] Comprendere ereditarietà e polimorfismo in Java
- [ ] Spiegare funzioni di ordine superiore in ML
- [ ] Descrivere unificazione e backtracking in Prolog
- [ ] Confrontare i diversi paradigmi

### Pratica
- [ ] Scrivere una classe Java semplice con costruttore e metodi
- [ ] Implementare ereditarietà e override
- [ ] Risolvere 5+ esercizi Java
- [ ] Implementare map, filter, reduce in ML
- [ ] Scrivere un programma Prolog con unificazione
- [ ] Tracciare manualmente l'esecuzione di programmi semplici
- [ ] Risolvere almeno una simulazione d'esame completa

### Concettuale
- [ ] Capire il WHY dietro ogni concetto (non solo il WHAT)
- [ ] Fare analogie tra concetti diversi
- [ ] Spiegare a qualcuno un argomento difficile
- [ ] Risolvere problemi nuovi applicando principi appresi

---

## 🎯 TIPS FINALI

1. **Non è una gara**: Capire profondamente i concetti è meglio che memorizzare velocemente
2. **Collega i concetti**: Non studiar paradigmi come silos separati, vedi le relazioni
3. **Pratica il coding**: Non basta leggere, DEVI scrivere codice
4. **Insegna agli altri**: Spiegare consolidate la comprensione
5. **Rivedi continuamente**: La spaced repetition è fondamentale
6. **Sleep, eat, exercise**: Prendersi cura di te facilita l'apprendimento
7. **Chiedi aiuto**: Se qualcosa non è chiaro, chiedi al docente o ai compagni
8. **Celebra i progressi**: Ogni concetto capito è una vittoria
9. **Mantieni la calma**: L'ansia non aiuta, la preparazione sì

---

**Buono studio! 🚀**

*Ultimo aggiornamento: 2024*
*Guida creata in base a UNINA Official Docs - Linguaggi di Programmazione I (A.A. 2022-2023)*
