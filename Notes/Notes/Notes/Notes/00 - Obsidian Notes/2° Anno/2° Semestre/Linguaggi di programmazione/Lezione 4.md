---
date: 2026-03-24
corso: Linguaggi di Programmazione
docente: N/D
lezione: Passaggio parametri, macro, funzioni di ordine superiore
tags: [LP, passaggio-parametri, macro, ordine-superiore, stack-attivazione]
---

# LP — Lezione 4: Passaggio Parametri, Macro e Funzioni di Ordine Superiore

**Corso:** Linguaggi di Programmazione

---

## Argomenti trattati

- Riepilogo modalità di passaggio parametri (in, out, in-out per copia e per riferimento)
- Simulazione del passaggio per riferimento in C++ e Java
- Fenomeni di aliasing
- Funzioni e procedure di ordine superiore
- Macro (`#define` in C): vantaggi e pericoli
- Esercizi su stack di attivazione con diverse modalità di passaggio

---

## 1. Riepilogo: modalità di passaggio parametri

In un linguaggio Pascal-like, la dichiarazione di un parametro formale determina la sua modalità:

| Modalità | Sintassi | Semantica | Implementazione tipica |
|---|---|---|---|
| **in** (sola lettura) | nessuna annotazione | il parametro può essere solo letto | copia del valore |
| **in per riferimento** | `var` (Pascal) | il parametro può essere solo letto, ma è un alias | puntatore (sola lettura) |
| **out** (sola scrittura) | `out` | il parametro può essere solo scritto; deve essere inizializzato prima dell'uso | copia-out |
| **in-out per copia** | `in out` | il parametro si legge e si scrive; valore copiato dentro e fuori | copia-in / copia-out |
| **in-out per riferimento** | `var` (Pascal, per in-out) | il parametro si legge e si scrive; è un alias della variabile del chiamante | puntatore |

> [!important] Errori a compile-time per modalità in
> Un parametro dichiarato `in` non deve mai comparire a sinistra di un assegnamento. Il compilatore lo rileva staticamente. Se trovate questa violazione, il programma non compila e non ha senso costruire lo stack di attivazione.

> [!important] Errori per modalità out
> Un parametro dichiarato `out` non deve essere letto prima di essere scritto. Poiché il suo valore iniziale è indefinito ("spazzatura"), leggerne il valore prima dell'inizializzazione è un errore.

---

## 2. Passaggio per riferimento in C++ e Java

### Simulazione in C

C non ha il passaggio per riferimento nativo. Si simula passando un **puntatore** alla variabile:

```c
void f(int *param) {
    *param = *param + 1;   // dereferenziazione necessaria
}

// chiamata:
int y = 5;
f(&y);   // si passa l'indirizzo
```

Le differenze rispetto a un vero passaggio per riferimento (come in Ada):

- In Ada basterebbe dichiarare `param : in out Integer` e usarlo come una normale variabile, senza `*` e `&`.
- In C la simulazione "espone" il meccanismo: dereferenziazione esplicita nel corpo, `&` nella chiamata.

### Oggetti in Java

> [!warning] Passaggio per riferimento in Java
> In Java il passaggio parametri è **sempre per copia**. Tuttavia, quando si passa un oggetto, si copia il **puntatore** all'oggetto (il riferimento). Di conseguenza, le modifiche al contenuto dell'oggetto dentro la procedura sono visibili all'esterno. Questo assomiglia al passaggio per riferimento, ma non lo è: riassegnare il parametro formale a un nuovo oggetto non influenza la variabile del chiamante.

---

## 3. Aliasing e fenomeni anomali

L'aliasing si verifica quando due nomi diversi denotano la stessa locazione di memoria. Si presenta naturalmente con il passaggio per riferimento.

> [!example] Esempio di aliasing con passaggio per riferimento
> ```pascal
> var a : integer;
>
> procedure test(var x : integer; var y : integer);
> begin
>   x := a + y;
>   write(a, x, y)
> end;
>
> begin
>   a := 1;
>   test(a, a)   // x, y e a sono la stessa locazione!
> end.
> ```
> Quando si chiama `test(a, a)`:
> - `env(x) = env(y) = env(a)`: tutti e tre puntano alla stessa locazione.
> - L'espressione `a + y` vale `1 + 1 = 2`.
> - L'assegnamento `x := 2` modifica l'unica locazione condivisa.
> - Pertanto `write(a, x, y)` stampa `2, 2, 2`.

Questo illustra come il riuso di una variabile in contesti con aliasing possa produrre comportamenti controintuitivi.

---

## 4. Funzioni e procedure di ordine superiore

Una procedura o funzione è **di ordine superiore** se può ricevere come parametro un'altra funzione (o procedura). Il meccanismo è usato:

- Nei **linguaggi funzionali** come ML, al posto dei cicli (che non esistono nei linguaggi puri privi di variabili mutabili).
- In **C**, passando il nome di una funzione (che ha come valore l'indirizzo di partenza del codice).
- In linguaggi come **Ada** o Pascal, con apposita sintassi che specifica il tipo della funzione-parametro (firma/segnatura).

> [!warning] C non verifica la firma delle funzioni passate come argomento
> In C, il nome di una funzione è solo un puntatore al codice. Non c'è informazione sul numero o tipo dei parametri, né sul tipo di ritorno. Linguaggi più moderni (C++, Java, Ada) effettuano controlli di tipo sulla segnatura.

> [!example] Esempio Pascal-like: gestione degli errori con funzioni di ordine superiore
> ```pascal
> procedure testpos(x : real; procedure error(msg : string));
> begin
>   if x <= 0 then error('x negativo in testpos')
> end;
>
> procedure E1(msg : string); begin write('E1 ', msg) end;
> procedure E2(msg : string); begin write('E2 ', msg) end;
>
> begin
>   read(v);
>   testpos(v, E1);   // usa E1 come gestore di errore
>   testpos(v, E2);   // usa E2 come gestore di errore
> end.
> ```
> Se `v < 0`, la prima chiamata stampa `E1 x negativo in testpos`, la seconda `E2 x negativo in testpos`.

In C, lo stesso meccanismo si usa per la gestione delle eccezioni con POSIX (`signal`): si passa il puntatore a una funzione handler il cui prototipo è definito dallo standard POSIX.

---

## 5. Macro in C (`#define`)

### Macro senza parametri

```c
#define MAX_RECORDS 123
```

Il preprocessore sostituisce ogni occorrenza di `MAX_RECORDS` con `123` prima della compilazione. Non viene allocata memoria; non esiste come variabile a runtime.

### Macro con parametri (funzione-like)

```c
#define M(x, y) ...corpo...
```

Ogni chiamata `M(2, 3)` viene **sostituita testualment** con il corpo, rimpiazzando `x` con `2` e `y` con `3`, prima della compilazione. Non viene creato nessun record di attivazione.

> [!warning] Pericoli delle macro: nessun ambiente protetto
> Le macro non hanno un proprio scope. Le variabili temporanee usate nel corpo della macro appartengono all'ambiente del chiamante, non a un ambiente separato. Questo può causare conflitti con variabili omonime del codice chiamante.

> [!example] Macro SWAP: tre problemi
>
> **Problema 1: conflitto sul nome `temp`**
> ```c
> #define SWAP(x, y) { int temp = x; x = y; y = temp; }
>
> // se nel codice chiamante esiste già una variabile `temp` importante:
> // la macro la sovrascrive!
> ```
>
> **Problema 2: argomento con effetto collaterale (`i` e `M[i]`)**
> ```c
> int i = 3; int M[10] = ...;
> SWAP(i, M[i]);
> // espansione: temp = i; i = M[i]; M[i] = temp;
> // Ma dopo `i = M[i]`, il valore di i è cambiato!
> // Quindi `M[i] = temp` scrive in una posizione diversa da M[3].
> ```
>
> **Problema 3: argomento `temp` passato direttamente**
> ```c
> SWAP(temp, i);
> // espansione: int temp = temp; ... // sovrascrive se stesso subito
> ```
>
> Con una vera procedura, i parametri vengono "congelati" al momento della chiamata (sia per copia che per riferimento), e le variabili locali hanno un ambiente separato — nessuno di questi problemi si presenterebbe.

> [!tip] Usare le macro con giudizio
> Le macro sono più efficienti (nessun overhead di chiamata), ma pericolose. Preferire funzioni inline (`inline` in C++) quando possibile. Se si usano macro, evitare variabili temporanee con nomi comuni e non passare mai espressioni con effetti collaterali.

---

## 6. Esercizi sullo stack di attivazione

### Procedura di lavoro

1. **Prima di costruire lo stack**, verificare se la modalità di passaggio causa errori a compile-time o runtime:
   - Modalità `in`: verificare che il parametro non compaia mai a sinistra di un assegnamento.
   - Modalità `out`: verificare che il parametro non venga letto prima di essere inizializzato.
   - Modalità `in-out`: nessun errore a priori.
2. Se non ci sono errori, costruire lo stack seguendo l'ordine di esecuzione.
3. Seguire rigorosamente le regole di scoping statico (o dinamico, se richiesto).

### Quattro modalità a confronto (Esercizio 2)

Il programma di esempio ha due procedure annidate (`P1` e `P2`) con due parametri `A` e `B`, con modalità variabile. Segue l'analisi per ogni caso.

#### a) In per copia

I parametri sono **allocati nello stack** di P2 (e P1), inizializzati con i valori attuali. Le modifiche rimangono locali.

Stack finale e output:

```
Esercizio2: a=1, b=5, c=10
  → chiama P2(c, b) = P2(10, 5)
    P2: A_locale=10, B_locale=5
      A = A - B → A_locale = 5
      if A == c? → 5 ≠ 10 → else → chiama P1(A, B) = P1(5, 5)
        P1: A_locale=5, B_locale=5
          A = A * B → A_locale = 25
          if C/B == A? → 10/5 = 2 ≠ 25 → else → A_locale = 100
        fine P1: nessuna copia fuori (in per copia)
      fine P2: nessuna copia fuori (in per copia)
  stampa a, b, c: 1, 5, 10
```

**Output: `1 5 10`**

#### b) In-out per riferimento

I parametri sono **alias** delle variabili del chiamante. Ogni modifica si riflette immediatamente sulla variabile originale.

```
env(A_P2) = env(c), env(B_P2) = env(b) → stessa locazione

A = A - B → c diventa 5 (A e c sono la stessa locazione)
if A == c? → 5 == 5 (aliasing!) → then branch → chiama P1(B, A) = P1(b, c)
  env(A_P1) = env(b), env(B_P1) = env(c)   [aliasing: B_P1 e c]
  A = A * B → b = 5 * 5 = 25... ma attenzione: B è c, e c è cambiata in 5
  → quindi A*B = 5*5 = 25 → b = 25
  if C/B == A? → c e B_P1 sono la stessa variabile → rapporto = 1 ≠ 25 → else
  → A_P1 = 100 → b = 100
fine: a=1, b=100, c=5
```

**Output: `1 100 5`**

#### c) In-out per copia

I parametri vengono copiati dentro all'inizio e **copiati fuori** al termine. Analogamente al passaggio per riferimento, ma le modifiche sono visibili solo a fine procedura.

```
P2 riceve copie: A_P2=10, B_P2=5. Da copiare fuori: A→c, B→b
  A = A - B → A_P2 = 5
  if A == c? → 5 ≠ 10 (c non è ancora aggiornata) → else → chiama P1(A_P2, B_P2)
    P1 riceve copie: A_P1=5, B_P1=5. Da copiare fuori: A→A_P2, B→B_P2
      A = A * B → A_P1 = 25
      if C/B == A? → 10/5 = 2 ≠ 25 → else → A_P1 = 100
    fine P1: copia fuori → A_P2 = 100, B_P2 rimane 5
  fine P2: copia fuori → c = 100, b = 5
stampa: a=1, b=5, c=100
```

**Output: `1 5 100`**

> [!tip] Consiglio per l'esame
> Nella modalità in-out per copia, segnate esplicitamente nel vostro stack "da copiare: A→c, B→b" prima di eseguire il corpo della procedura. È facilissimo dimenticare la copia in uscita, che è la parte che differenzia questa modalità dal passaggio per riferimento.

> [!warning] L'ordine della copia-out può influenzare il risultato
> Se ci sono parametri out multipli e ci sono dipendenze tra di loro (aliasing), il risultato può dipendere dall'ordine con cui vengono copiati (da sinistra a destra o da destra a sinistra). Lo standard non lo specifica: è uno dei comportamenti indefiniti da investigare.

---

## 7. Funzioni: cenni

Le funzioni restituiscono un valore singolo. In linguaggi "vecchi" si usa una pseudo-variabile con lo stesso nome della funzione; nei linguaggi moderni si usa `return`. Si ricorre alle funzioni quando:

- Si vuole restituire un solo valore (alternativa ai parametri `out`).
- Il linguaggio non supporta parametri di tipo `out`.

---

> [!summary] Punti chiave della lezione
> - Le modalità di passaggio parametri (`in`, `out`, `in-out`, per copia o per riferimento) determinano l'ambiente del parametro e quando le modifiche diventano visibili all'esterno.
> - Il passaggio per riferimento crea aliasing, che può produrre comportamenti controintuitivi.
> - Le macro C sono sostituzioni testuali senza ambiente protetto: possono causare conflitti di nomi, doppia valutazione di argomenti con side effect, e comportamenti imprevedibili.
> - Le funzioni di ordine superiore permettono di passare codice come dato; in C si implementano con puntatori a funzione, senza controllo di tipo sulla firma.
> - Lo stack di attivazione va costruito solo dopo aver verificato l'assenza di errori per la modalità di passaggio scelta.

## Prossimi argomenti

- [ ] Esercizi completi con tutte le combinazioni di modalità (in, out, in-out × copia/riferimento)
- [ ] Scoping dinamico vs. statico sugli esercizi di stack
- [ ] Parametri di ritorno
- [ ] Linguaggio ML: funzioni di ordine superiore nei linguaggi funzionali

#LP #passaggio-parametri #macro #ordine-superiore #stack-attivazione #aliasing
