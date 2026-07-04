---
date: 2026-04-14
corso: Linguaggi di Programmazione
lezione: "Java — Operatori bitwise, shift, casting e promozione di tipo"
tags: [LP, Java, operatori-bitwise, shift, casting, promozione-tipo, overloading, array]
---

# LP — Operatori Bitwise, Shift e Casting in Java

**Corso:** Linguaggi di Programmazione

---

## Argomenti trattati

- Operatori bitwise: AND, OR, XOR, NOT
- Operatori di shift: logico e aritmetico
- Regole di promozione di tipo negli operatori binari
- Casting esplicito: da tipo più grande a tipo più piccolo
- Overloading di operatori: il `+` con numeri vs stringhe
- Applicazione al calcolo con shift: moltiplicazione e divisione
- Dichiarazione e inizializzazione di array
- Array come type reference e passaggio parametri

---

## 1. Operatori bitwise

> [!info] Operatori bitwise in Java
> Java supporta quattro operatori su singoli bit per interi (`int`, `long`, `byte`, `short`, `char`):

| Operatore | Simbolo | Descrizione | Esempio |
|---|---|---|---|
| AND | `&` | Bit a 1 se entrambi sono 1 | `5 & 3 = 0101 & 0011 = 1` |
| OR | `\|` | Bit a 1 se almeno uno è 1 | `5 \| 3 = 0101 \| 0011 = 7` |
| XOR | `^` | Bit a 1 se sono diversi | `5 ^ 3 = 0101 ^ 0011 = 6` |
| NOT | `~` | Inverte tutti i bit | `~5 = ~0101 = -6` (two's complement) |

> [!warning] Negazione in complemento a due
> In Java gli interi sono **sempre con segno**. Quindi `~5` non dà il valore positivo `1010`, ma il suo negativo in complemento a due: **-6**.

### Applicazioni: bitmask

> [!example] Gestione di flag con bitmask
> ```java
> final int FLAG_READ = 1 << 0;      // 0001
> final int FLAG_WRITE = 1 << 1;     // 0010
> final int FLAG_EXECUTE = 1 << 2;   // 0100
>
> int permissions = FLAG_READ | FLAG_WRITE;  // 0011
>
> if ((permissions & FLAG_READ) != 0) {
>     // Il bit di lettura è acceso
> }
> ```

---

## 2. Operatori di shift

> [!info] Shift a sinistra e a destra
> ```java
> x << n   // Sposta i bit a sinistra di n, riempiendo con 0
> x >> n   // Sposta a destra ARITMETICO (riempie con bit di segno)
> x >>> n  // Sposta a destra LOGICAMENTE (riempie con 0) — solo in Java
> ```

### Proprietà importanti

1. **Normalizzazione:** se `x` è `int` (32 bit), `n` viene normalizzato a `n % 32`. Quindi `x << 33` ≡ `x << 1`.

2. **Shift aritmetico vs logico:**
   - `x >> n`: aritmetico — **preserva il segno** dei numeri negativi
   - `x >>> n`: logico — tratta il numero come unsigned

> [!example] Differenza tra shift aritmetico e logico
> ```java
> int x = -8;        // 11111111111111111111111111111000 (32 bit)
>
> int y = x >> 1;    // 11111111111111111111111111111100 = -4
> int z = x >>> 1;   // 01111111111111111111111111111100 = 2147483644
> ```

### Relazione con moltiplicazione e divisione

> [!tip] Shift per potenze di 2
> - **`x << n`** ≡ $x \cdot 2^n$ (moltiplicazione)
> - **`x >> n`** ≡ $\lfloor x / 2^n \rfloor$ (divisione intera)
>
> I compilatori ottimizzanti trasformano automaticamente `x / 2` in `x >> 1` per costanti potenza di 2.

---

## 3. Promozione di tipo (Type Promotion)

> [!info] Regole di promozione per operatori unari
> Quando si applica un operatore unario a tipi piccoli (`byte`, `short`, `char`), Java esegue **promozione a `int`** automatica.

```java
byte b = 5;
byte result = -b;  // ERRORE: -b produce un int, non un byte
```

> [!warning] Eccezione: autoincremento
> ```java
> short s = 10;
> s++;               // OK: rimane short (cast implicito interno)
> ```

### Promozione per operatori binari

> [!info] Gerarchia di promozione
> Quando due operandi hanno tipi diversi, si allineano al tipo **più ricco**:
> $$\text{double} > \text{float} > \text{long} > \text{int} > \text{short}/\text{byte}/\text{char}$$

> [!warning] Promozione a int con tipi piccoli
> `short`, `byte` e `char` diventano sempre almeno `int` negli operatori binari, **anche se entrambi gli operandi sono piccoli**.

> [!example] Errore comune
> ```java
> short s1 = 5, s2 = 3;
> short result = s1 + s2;  // ERRORE: s1 + s2 è int
>
> // Correzione:
> short result = (short) (s1 + s2);  // Cast esplicito
> ```

---

## 4. Casting esplicito: da tipo grande a tipo piccolo

> [!warning] Casting comporta troncamento
> Assegnare un valore di tipo **più grande** a variabile di tipo **più piccolo** richiede **cast esplicito**. I bit in eccesso vengono **troncati**.

> [!example] Troncamento bit
> ```java
> int x = 300;
> byte b = (byte) x;
>
> // 300 in binario (32 bit): 0000000100101100
> // Truncate ai 8 bit LSB:              01101100 = 44
> ```

Perdita di informazione: il cast esplicito **conferma** al compilatore che il programmatore è consapevole.

---

## 5. Overloading di operatori

> [!info] L'operatore `+` overloaded
> In Java, `+` ha **due significati distinti** a seconda del contesto:
> - **Su numeri:** somma aritmetica
> - **Su stringhe:** concatenazione

```java
int x = 3;
String s = "Numero: " + x;  // "Numero: 3" (concatenazione)
```

### Regola: se uno degli operandi è String

> [!tip] Regola di concatenazione
> Se **almeno uno** dei due operandi di `+` è una `String`, il risultato è **concatenazione di stringhe**. Gli altri operandi sono convertiti via `toString()`.

> [!example] Ordine di valutazione
> ```java
> String msg = "Numero: " + 5 + 3;   // "Numero: 53"
> // 1. "Numero: " + 5 → "Numero: 5" (concat)
> // 2. "Numero: 5" + 3 → "Numero: 53" (concat)
> ```

---

## 6. Array in Java

### Dichiarazione

> [!tip] Forma preferita di dichiarazione array
> ```java
> int[] a;           // ✓ Forma preferita
> int a[];           // ✗ C-style, meno leggibile
> ```

### Inizializzazione

```java
int[] arr = new int[10];  // Alloca 10 elementi (inizializzati a 0)
int[] arr = {1, 2, 3, 4, 5};  // Shorthand per new int[]{...}
```

> [!info] Array è un type reference
> L'array è un **puntatore** (handle) che punta a dati nell'heap. La dichiarazione alloca solo lo spazio del puntatore (`null`).

### Passaggio di array a metodi

> [!example] Modifiche al contenuto sono visibili fuori
> ```java
> void modify_array(int[] arr) {
>     arr[0] = 999;
> }
>
> int[] data = {1, 2, 3};
> modify_array(data);
> System.out.println(data[0]);  // 999 ← modificato
> ```

**Il puntatore è copiato** (pass by value), ma entrambi puntano allo stesso oggetto in memoria.

### Array multidimensionali

```java
int[][] matrix = new int[3][4];  // 3×4
int[][] jagged = new int[3][];   // Dimensioni variabili
jagged[0] = new int[2];
jagged[1] = new int[5];
```

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **Bitwise:** `&`, `|`, `^`, `~` operano su singoli bit — utili per bitmask e flag
> 2. **Shift:** `<<` moltiplica per $2^n$; `>>` divide per $2^n$ (aritmetico, preserva segno)
> 3. **Promozione:** tipi piccoli (`byte`, `short`) → `int` negli operatori binari
> 4. **Casting:** da tipo grande a tipo piccolo richiede cast esplicito; comporta **troncamento**
> 5. **Overloading:** `+` con stringhe fa concatenazione; con numeri, somma
> 6. **Array:** type reference, passato per copia del puntatore; modifiche visibili fuori

---

> [!question] Domande d'esame frequenti
> - Quale è il risultato di `5 & 3`?
> - Differenza tra `>>` e `>>>`?
> - Perché `short s1 = 5, s2 = 3; short r = s1 + s2;` dà errore?
> - Che cosa produce `"a" + 1 + 2` vs `1 + 2 + "a"`?

> [!todo] Esercizi suggeriti
> - [ ] Implementare una classe `BitSet` usando operatori bitwise
> - [ ] Analizzare il bytecode di operazioni con shift (javap)
> - [ ] Misurare performance: shift vs moltiplicazione

---

#LP #Java #operatori-bitwise #shift #casting #promozione-tipo #array
