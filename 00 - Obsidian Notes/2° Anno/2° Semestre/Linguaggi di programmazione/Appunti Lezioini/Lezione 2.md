---
Date: 2026-03-17
Professore: Bonatti
tags:
  - LP
  - Saltata
  - NoAudio
---
# Lezione 2 — Vettori, Data Objects e Type Checking
**Corso:** Linguaggi di Programmazione I — Prof. Bonatti, UniNA

---

## 1. Accesso agli elementi di un vettore in C

### 1.1 Vettore di interi — notazione indicizzata e aritmetica dei puntatori

Dato un vettore dichiarato come `int v[3]`, il nome `v` **non è un puntatore**, ma identifica l'indirizzo (l'ambiente) della prima cella dell'array, ovvero `env(v)`.

```
env(v)
  ↓
[ v[0] | v[1] | v[2] ]
```

Le operazioni di lettura e scrittura si traducono come segue:

| Operazione C | lvalue (sinistra) | rvalue (destra) |
|---|---|---|
| `x = v[i]` | `env(x)` | `mem(env(v) + i)` |
| `v[i] = x` | `env(v) + i` | `mem(env(x))` |

**Esempio concreto:**

```c
int v[3], y;

y = v[1];    // env(y)      ←  mem(env(v) + 1)
v[1] = y;    // env(v) + 1  ←  mem(env(y))
```

> **Nota:** `v[i]` e `*(v+i)` sono notazioni equivalenti (Tabella 2.1, note ufficiali).

### 1.2 Il vettore come puntatore costante

`v` da solo equivale a `&v[0]`, ovvero è un **lvalue costante**. Di conseguenza:

```c
int *p;
p = v;     // OK: p punta alla prima cella di v
v = p;     // ERRORE: "assignment to expression with array type"
v = v + 1; // ERRORE: si tenta di modificare env(v)
```

La differenza è fondamentale: `p` è un puntatore il cui valore può essere modificato a runtime; `v` invece ha il legame di locazione fissato — il nome `v` **è** quell'indirizzo, non lo contiene.

### 1.3 Vettore allocato dinamicamente con `malloc`

```c
int *x = malloc(3 * sizeof(int));
```

Accedere a `x[1]` richiede un passo in più rispetto al vettore statico:

- **Vettore statico `v`:** `mem(env(v) + 1)` — l'indirizzo di base è direttamente `env(v)`.
- **Puntatore `x`:** `mem(mem(env(x)) + 1)` — bisogna prima leggere il valore di `x` (che è un indirizzo) e poi sommare l'offset.

Assegnamento con puntatore a sinistra:

```c
x[1] = y;  →  mem(env(x)) + 1  ←  mem(env(y))
```

---

## 2. Data Objects e Bindings

### 2.1 Definizione di Data Object

> **Data Object** — Una variabile, parametro od oggetto è rappresentato come una **quadrupla**:
>
> **(L, N, V, T)**
>
> - **L** — Locazione (indirizzo di memoria)
> - **N** — Nome (identificatore)
> - **V** — Valore (contenuto della cella)
> - **T** — Tipo (insieme di valori ammessi e operatori)

### 2.2 Binding (Legame)

Un **legame** è la determinazione di uno dei quattro componenti del data object. Si distinguono:

- **Location binding** — quando viene assegnata una locazione di memoria
- **Name binding** — quando un identificatore viene associato al data object
- **Value binding** — quando viene assegnato un valore
- **Type binding** — quando viene determinato il tipo

> Nel paradigma imperativo: il legame di locazione corrisponde alla funzione `env`, mentre il legame di valore di una variabile `x` corrisponde a `mem(env(x))`.

### 2.3 Quando avvengono i legami?

| Legame | Momento tipico |
|---|---|
| **Name** | Compilazione (alla dichiarazione) |
| **Type** | Compilazione (nella maggior parte dei linguaggi) |
| **Location** | Load time o runtime |
| **Value** | Runtime |

Fa eccezione il legame di tipo **dinamico** (APL, Smalltalk): il tipo si determina dal valore corrente e cambia ad ogni assegnamento. Questi linguaggi non richiedono dichiarazioni.

### 2.4 Rappresentazione grafica dei legami

I data object vengono visualizzati con **quattro archi** che si dipartono verso i rispettivi spazi (nomi, tipi, valori, locazioni).

- **Arco in grassetto (bold)** → legame **statico** (tempo di compilazione, immutabile)
- **Arco sottile** → legame **dinamico** (modificabile a runtime)

**Esempi in pseudo-codice:**

```
A: integer;                // Type: grassetto | Location: sottile | Value: assente
B: integer ::= 1;          // Type: grassetto | Location: grassetto (load time)
C: constant integer ::= 1; // Type: grassetto | Value: grassetto (compilazione)
```

### 2.5 Modifiche dei legami

I legami statici (grassetto) sono **immutabili** dopo la compilazione. I legami dinamici possono essere modificati a runtime — ad esempio, il legame di valore cambia ad ogni assegnamento. La modifica del legame di locazione (riassegnazione di un puntatore) può rendere inaccessibile il data object puntato in precedenza.

### 2.6 Il Data Object dei puntatori

I puntatori coinvolgono **due data object**:

```
Data Object 1 (il puntatore stesso)
  N: nome del puntatore         ← legame a compile time
  L: locazione del puntatore    ← legame a load time
  T: "puntatore a T"            ← legame a compile time
  V: indirizzo di Data Object 2 ← legame a runtime

Data Object 2 (la variabile/memoria puntata)
  N: assente (con malloc non ha nome)
  L: determinata a runtime
  T: determinata a runtime
  V: determinato a runtime
```

**Proprietà importante:** nel caso di `malloc`, Data Object 2 non ha legame di nome — non è accessibile per identificatore, solo tramite il puntatore. Modificare il legame di valore del puntatore senza deallocare prima produce un **memory leak**. Alcuni linguaggi risolvono questo con il **garbage collector**.

---

## 3. Tipi di Dato Astratto (ADT)

Un **tipo di dato astratto** separa la specifica (cosa un tipo *fa*) dalla sua implementazione (come lo *fa*). Il tipo è definito dall'insieme dei valori che può assumere e dalle operazioni applicabili — non dalla rappresentazione interna in memoria.

Questo concetto è alla base del **type binding**: il compilatore, incontrando una dichiarazione di tipo, fissa l'insieme dei valori ammissibili e degli operatori.

---

## 4. Type Checking

### 4.1 Definizione

Il **type checking** è il processo con cui si verifica la consistenza della coppia **(valore, tipo)** di un data object. Aiuta a rilevare e prevenire errori prima o durante l'esecuzione.

Può avvenire:
- **A tempo di compilazione** (*static type checking*)
- **A tempo di esecuzione** (*dynamic type checking*)
- **Un mix** dei due
- **Non avvenire affatto**

### 4.2 Linguaggi fortemente vs debolmente tipizzati

| Categoria | Descrizione | Esempi |
|---|---|---|
| **Fortemente tipizzato** | Il controllo avviene sempre | Java, ML |
| **Quasi fortemente tipizzato** | Controllo quasi sempre, con rare eccezioni | Pascal* |
| **Debolmente tipizzato** | Il controllo non avviene sempre | C |

> **Pascal:** unica eccezione è il **record con varianti**, dove un campo può contenere valori di tipo diverso senza garanzia di consistenza a runtime.

> **C:** il **casting esplicito** permette di forzare l'interpretazione di qualsiasi valore secondo qualsiasi tipo, bypassando ogni controllo:
> ```c
> float f = 3.14;
> int *p = (int *) &f;   // Nessun controllo: il compilatore si fida del cast
> ```

### 4.3 Impossibilità di un type checking perfetto

Un linguaggio che garantisse controlli di tipo **sempre corretti e sempre completi** non può esistere. Il motivo è teorico: si riconduce all'**indecidibilità del problema della fermata (Halting Problem / predicato Halt)**.

Determinare staticamente se un'operazione di tipo errato verrà mai eseguita equivale a decidere se un certo ramo del programma verrà raggiunto — e questo, in generale, non è calcolabile.

Di conseguenza, ogni type checker reale deve scegliere tra:
- **Soundness** (nessun falso negativo): rifiuta anche programmi corretti pur di non lasciarne passare di errati → può essere troppo restrittivo.
- **Completeness** (nessun falso positivo): accetta tutti i programmi corretti, ma potrebbe accettarne di errati.

I linguaggi reali trovano un compromesso, spesso accettando qualche falso allarme in cambio di maggiore sicurezza.

---

## 5. Riepilogo: Classificazione dei legami

| Legame       | Statico (compilazione)        | Dinamico (runtime)        |
| ------------ | ----------------------------- | ------------------------- |
| **Name**     | Quasi sempre                  | Raro (linguaggi dinamici) |
| **Type**     | Linguaggi staticamente tipati | APL, Smalltalk, Python... |
| **Location** | Variabili globali/statiche    | Variabili locali, malloc  |
| **Value**    | Costanti (`const`, `final`)   | Variabili ordinarie       |

---

*Riferimento: Note ufficiali Bonatti — UniNA 2023, §2.3 "Data Objects e bindings", §2.3.1 "I puntatori", §2.3.2 "Il legame di tipo", "Type checking".*
