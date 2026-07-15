---
date: 2026-04-16
corso: Linguaggi di Programmazione
lezione: "Java — Array come Oggetti, Memory Layout, e Type System"
tags: [LP, Java, array, reference-types, memory-management, bounds-checking, aliasing]
---

> [!question] Argomenti trattati
> - Array come tipi reference in Java
> - Allocazione in heap vs stack
> - Array monodimensionali vs multidimensionali (array di array)
> - Differenze critiche tra C e Java nel memory layout
> - Passaggio di array per copia di reference (aliasing)
> - Attributo immutabile `.length` e bounds checking
> - Buffer overflow e sicurezza della memoria
> - Copia di array: `System.arraycopy()`

---

## 1. Array in Java: tipi reference

> [!info] Classificazione
> In Java, **gli array sono sempre tipi reference** (come gli oggetti).
> Una variabile array contiene un **puntatore (reference)** all'oggetto array nello heap, non l'array stesso.

### Dichiarazione vs Allocazione

```java
int[] x;                    // Dichiarazione: x è null
int[] x = new int[10];      // Allocazione: x punta a un oggetto array di 10 interi
```

**Memoria:**
- Dichiarazione: nessuna allocazione, `x = null`
- `new int[10]`: alloca nello heap un oggetto con 10 celle contigue + metadati (length, type)

> [!warning] Errore comune
> Confondere:
> - **Dichiarazione:** `int[] x;` → allocazione **zero**, x è null
> - **Allocazione:** `new int[10]` → allocazione nello heap

---

## 2. Proprietà degli array in Java

### Attributo `.length`

> [!info] Proprietà immutabile
> Ogni array ha un attributo **final** `length` che contiene il numero di elementi:
>
> ```java
> int[] arr = new int[5];
> System.out.println(arr.length);  // Output: 5
> // arr.length = 10;  // ERRORE: è finale, non modificabile
> ```

**Implementazione interna:** l'oggetto array include un campo `length` non modificabile.

### Bounds Checking

> [!abstract] Garanzia di sicurezza
> Java **sempre controlla i limiti** agli indici:
> ```java
> int[] arr = new int[5];
> arr[10] = 5;  // ArrayIndexOutOfBoundsException
> ```
>
> Se accedi a `arr[i]` con `i >= arr.length`, ottieni eccezione a runtime.

> [!warning] CONTRASTO CON C
> In C **nessun controllo**: accedi a memoria arbitraria → comportamento indefinito, corruptela di memoria, crash.

---

## 3. Array monodimensionali vs multidimensionali

### Monodimensionali

```java
int[] v = new int[5];  // Array lineare di 5 interi
```

### Multidimensionali: Array di Array

> [!info] Cruciale: multidimensionali in Java
> Un array **bidimensionale** è in realtà un **array di array**:
>
> ```java
> int[][] m = new int[3][4];  // Array di 3 righe, ognuna è un array di 4 interi
> ```
>
> Internamente: `m` punta a un array di 3 puntatori, ognuno punta a un array di 4 interi.

### Implicazione: righe di lunghezza variabile

> [!example] Matrici non rettangolari
> ```java
> int[][] m = new int[3][];  // 3 righe, lunghezze da definire
> m[0] = new int[2];         // Prima riga: 2 elementi
> m[1] = new int[5];         // Seconda riga: 5 elementi
> m[2] = new int[3];         // Terza riga: 3 elementi
> ```
>
> Ogni riga ha `.length` indipendente:
> ```java
> m[0].length  // 2
> m[1].length  // 5
> m.length     // 3 (numero di righe)
> ```

---

## 4. Differenza critica: C vs Java

### C: Buffer Contiguo in Memoria

```c
int v[3][4];  // Allocato come buffer lineare continuo
// Layout: v[0][0], v[0][1], v[0][2], v[0][3], v[1][0], v[1][1], ...
```

**Calcolo indirizzo di v[i][j]:**
```
indirizzo = &v[0][0] + i * COLONNE + j
```

**Problema:** il compilatore **DEVE conoscere il numero di COLONNE** al compile time.

### Java: Array di Array nello Heap

```java
int[][] m = new int[3][4];
// Layout: m → [puntatore0, puntatore1, puntatore2]
//             ↓              ↓              ↓
//         [0][0]...[0][3] [1][0]...[1][3] [2][0]...[2][3]
```

Il compilatore **conosce già la struttura**: m è un array di 3 puntatori, ogni puntatore punta a un array di 4 interi.

---

## 5. Sintassi di allocazione

### Dichiarazione corretta in Java

#### ✅ CORRETTO

```java
int[][] m = new int[3][4];     // Entrambe le dimensioni specificate
int[][] m = new int[3][];      // Solo prima dimensione (righe variabili)
int[] v = new int[5];          // Monodimensionale
```

#### ❌ ERRATO IN JAVA (ma non in C)

```java
int[][] m = new int[][4];  // ERRORE: quante righe?
```

Perché? Stai dicendo che ogni riga ha 4 colonne, ma non specifi quante righe hai. Dove li metti i puntatori alle righe?

### Allocazione parziale

```java
int[][] m = new int[3][4];      // Alloca sia l'indice (3) sia le righe (ognuna di 4 elementi)
int[][] m = new int[3][];       // Alloca solo l'indice (array di 3 puntatori)
                                 // Le righe devono essere allocate singolarmente
```

---

## 6. Passaggio di array e aliasing

> [!info] Regola: Passaggio per copia di reference
> Quando si passa un array a un metodo, si **copia il puntatore**, non l'array.
> 
> Conseguenza: **modifiche all'interno del metodo si vedono da fuori** (aliasing).

### Esempio pratico

```java
void metodo(int[] arr) {
    arr[0] = 999;  // Modifica l'elemento
}

int[] v = new int[5];
v[0] = 10;
metodo(v);
System.out.println(v[0]);  // Output: 999 (modificato!)
```

**Perché?** Il puntatore a `v` è copiato dentro `arr`. Entrambe le variabili puntano allo **stesso oggetto**.

### Aliasing

> [!abstract] Concetto
> **Aliasing** = due (o più) variabili reference che puntano allo stesso oggetto.
> 
> Modifiche tramite un alias **si vedono tramite gli altri alias**.

---

## 7. Bounds checking: il vantaggio di Java

### Protezione dalla memoria

> [!example] Caso: Stack Smashing in C
> ```c
> void copiaStringa(char* dest, char* src) {
>     while (*src) *dest++ = *src++;  // No bounds check!
> }
> 
> char buffer[10];
> char input[100] = "stringa molto lunga";
> copiaStringa(buffer, input);  // Overflow! Corrompe stack
> ```
>
> In C, il puntatore di ritorno nel record di attivazione viene sovrascritto → crash o exploit.

### In Java: Impossibile

```java
void copiaArray(int[] dest, int[] src) {
    for (int i = 0; i < src.length; i++) {
        dest[i] = src[i];  // Se i >= dest.length → ArrayIndexOutOfBoundsException
    }
}
```

Java controlla **sempre** gli indici → niente buffer overflow, niente stack smashing.

---

## 8. Attributi ed elementi degli array

### Inizializzazione di default

> [!info] Valori iniziali
> - **Array di interi:** elementi = 0
> - **Array di double:** elementi = 0.0
> - **Array di boolean:** elementi = false
> - **Array di object (reference):** elementi = null

### Memoria interna dell'oggetto array

Oltre agli elementi, l'oggetto array contiene:
- **length:** numero di elementi (final, immutabile)
- **type information:** tipo degli elementi
- **metadati:** per garbage collection

Quando accedi a `arr[i]`, Java:
1. Valida che `i >= 0` e `i < arr.length`
2. Accede all'elemento in memoria

---

## 9. Copia di array: System.arraycopy()

> [!info] Metodo statico
> ```java
> System.arraycopy(Object src, int srcPos, 
>                  Object dest, int destPos, 
>                  int length);
> ```
>
> Copia `length` elementi da `src` a partire da `srcPos` in `dest` a partire da `destPos`.

### Esempio

```java
int[] vecchio = {1, 2, 3, 4, 5};
int[] nuovo = new int[10];

// Copia i 3 primi elementi di vecchio in nuovo
System.arraycopy(vecchio, 0, nuovo, 0, 3);
// nuovo contiene: {1, 2, 3, 0, 0, 0, 0, 0, 0, 0}
```

### Cosa NON cambia

```java
int[] v = {1, 2, 3};
int[] w = {10, 20, 30};

System.arraycopy(v, 0, w, 0, 3);
// w viene modificato: {1, 2, 3}
// v rimane: {1, 2, 3}

// Ma i puntatori v e w NON cambiano:
v  // Still points to original array
w  // Now contains the copied values
```

---

## 10. Array di reference vs array di primitivi

### Array di primitivi

```java
int[] primitivi = {1, 2, 3};  // Array di 3 interi nel heap
```

### Array di reference

```java
String[] stringhe = {"a", "b", "c"};
// stringhe → [puntatore0, puntatore1, puntatore2]
//            ↓             ↓             ↓
//          String("a")   String("b")  String("c")
```

Quando fai `System.arraycopy()` su un array di reference, **si copiano i puntatori**, non gli oggetti:

```java
String[] v = {"a", "b", "c"};
String[] w = new String[3];

System.arraycopy(v, 0, w, 0, 3);
// v[0] e w[0] puntano allo STESSO oggetto String
```

> [!warning] Shallow copy
> Questo è una **shallow copy**: i puntatori vengono copiati, non gli oggetti.
> Se modifichi l'oggetto tramite un alias, l'altra variabile "vede" il cambiamento.

---

## 11. Parametri main() e linea di comando

> [!info] Firma standard
> ```java
> public static void main(String[] args) { ... }
> ```
>
> - `args` è un array di stringhe contenente gli argomenti dalla linea di comando
> - È **statico** (no this): non richiede un oggetto per l'esecuzione

### Accesso agli argomenti

```bash
java MyClass arg1 arg2 arg3
```

```java
public static void main(String[] args) {
    System.out.println(args.length);   // 3
    System.out.println(args[0]);       // "arg1"
    System.out.println(args[1]);       // "arg2"
}
```

> [!warning] Stampa dell'array
> ```java
> System.out.println(args);      // Stampa indirizzo di memoria ([Ljava/lang/String;@...)
> System.out.println(args[0]);   // Stampa il primo elemento
> ```
>
> Per stampare l'intero array: `System.out.println(Arrays.toString(args));`

---

## 12. Conversione di tipo negli array

### Assegnamento tra array

```java
int[] v = new int[5];
int[] w = new int[5];

v = w;  // OK: v punta ora a w (cambio di indirizzo)
```

Questo è un **assegnamento di reference**, non una copia.

### Incompatibilità di tipo

```java
int[] v = new int[5];
Object[] o = new Object[5];

v = o;  // ERRORE: tipi incompatibili

Object[] o2 = v;  // OK: autoboxing
```

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **Array = objects:** allocati in heap, accessibili via reference
> 2. **Multidimensionali = array di array:** righe possono avere lunghezze diverse
> 3. **Memory layout diverso C vs Java:** C = buffer lineare, Java = struttura di puntatori
> 4. **Passaggio per copia di reference:** aliasing possibile, modifiche visibili all'esterno
> 5. **Bounds checking:** Java SEMPRE controlla limiti, C no
> 6. **`.length` immutabile:** non è modificabile
> 7. **Copia:** `System.arraycopy()` copia elementi (shallow copy per objects)
> 8. **Sicurezza:** impossibile buffer overflow in Java

---

> [!question] Domande d'esame frequenti
> - Differenza tra dichiarazione e allocazione di array
> - Perché in Java devi specificare tutte le dimensioni tranne la prima?
> - Spiegare il concetto di aliasing
> - Bounds checking: come protegge Java?
> - Struttura di memoria di un array multidimensionale
> - Cosa succede in System.arraycopy()?
> - Shallow copy vs deep copy
> - Come passare array al main() dalla linea di comando?

> [!todo] Esercizi suggeriti
> - [ ] Creare matrice non rettangolare e accedere agli elementi
> - [ ] Implementare metodo che modifica array passato come parametro
> - [ ] Usare System.arraycopy() per gestire array dinamici
> - [ ] Confrontare memory layout di array monodimensionali vs multidimensionali
> - [ ] Provare ad accedere oltre i limiti e osservare l'eccezione
> - [ ] Implementare una copia profonda (deep copy) di array di objects
> - [ ] Leggere argomenti da linea di comando nel main()

---

#LP #Java #array #reference-types #memory-management #bounds-checking #aliasing #type-system
