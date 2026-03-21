# Appunti — Risoluzione di Ricorrenze
**Corso:** Algoritmi e Progettazione di Strutture Dati — UniNA

---

## 0. Panoramica dei metodi

Le ricorrenze si incontrano nell'analisi di algoritmi divide-et-impera. I metodi per risolverle sono:

| Metodo | Quando usarlo |
|---|---|
| **Master Theorem** | Ricorrenze della forma $T(n) = aT(n/b) + f(n)$ |
| **Akra-Bazzi** | Ricorrenze con più sottoproblemi di taglie diverse |
| **Albero di ricorsione** | Visualizzazione intuitiva, utile quando gli altri non si applicano direttamente |
| **Sostituzione (induzione)** | Verifica di una soluzione già intuita |

---

## 1. Master Theorem

### 1.1 Forma applicabile

$$T(n) = aT(n/b) + f(n), \quad a \geq 1,\ b > 1$$

dove:
- $a$ = numero di sottoproblemi
- $b$ = fattore di riduzione della taglia
- $f(n)$ = costo del lavoro fuori dalla ricorsione

### 1.2 I tre casi

Calcola prima il **valore critico**: $n^{\log_b a}$

| Caso | Condizione | Soluzione |
|---|---|---|
| **Caso 1** | $f(n) = O(n^{\log_b a - \varepsilon})$ per qualche $\varepsilon > 0$ | $T(n) = \Theta(n^{\log_b a})$ |
| **Caso 2** | $f(n) = \Theta(n^{\log_b a} \cdot \log^k n)$ con $k \geq 0$ | $T(n) = \Theta(n^{\log_b a} \cdot \log^{k+1} n)$ |
| **Caso 3** | $f(n) = \Omega(n^{\log_b a + \varepsilon})$ per qualche $\varepsilon > 0$, **e** $af(n/b) \leq cf(n)$ con $c<1$ | $T(n) = \Theta(f(n))$ |

> **Intuizione:** vince chi cresce più velocemente tra il "costo delle foglie" $n^{\log_b a}$ e il "costo del merge" $f(n)$. Se pareggiano, si accumula un logaritmo.

---

## 2. Metodo di Akra-Bazzi

### 2.1 Forma applicabile

$$T(n) = \sum_{i=1}^{k} a_i T(n/b_i) + f(n)$$

con $k \geq 1$, $a_i > 0$, $b_i > 1$. Permette **sottotaglie diverse** (es. $n/2$ e $n/3$ insieme).

### 2.2 Procedura

**Step 1 — Trova $p$** risolvendo l'equazione:

$$\sum_{i=1}^{k} \frac{a_i}{b_i^p} = 1$$

**Step 2 — Applica la formula:**

$$T(n) = \Theta\!\left( n^p \left(1 + \int_1^n \frac{f(u)}{u^{p+1}}\, du \right) \right)$$

> **Nota:** se $f(n) = \Theta(n^q)$, l'integrale si calcola facilmente:
> $$\int_1^n u^{q-p-1}\, du = \begin{cases} \Theta(n^{q-p}) & \text{se } q \neq p \\ \Theta(\log n) & \text{se } q = p \end{cases}$$

---

## 3. Metodo dell'Albero di Ricorsione

Utile per intuire la soluzione prima di verificarla con sostituzione o per applicare Akra-Bazzi manualmente.

### 3.1 Procedura

1. **Disegna i livelli**: al livello $i$, i nodi hanno taglia $n / b^i$
2. **Conta i nodi** a ciascun livello
3. **Calcola il costo per livello**: `(nodi al livello i) × f(taglia al livello i)`
4. **Somma su tutti i livelli**

### 3.2 Schema tipo per $T(n) = aT(n/b) + f(n)$

```
Livello 0:              f(n)                    → costo: f(n)
Livello 1:      f(n/b)  f(n/b) ... [a volte]    → costo: a·f(n/b)
Livello 2:  ...                                  → costo: a²·f(n/b²)
...
Livello log_b(n):  foglie (tutte T(1)=1)         → costo: a^{log_b n} = n^{log_b a}
```

Costo totale = somma geometrica dei costi per livello + costo delle foglie.

---

## 4. Metodo di Sostituzione (Induzione)

1. **Ipotizza** una forma per la soluzione (spesso suggerita dall'albero di ricorsione)
2. **Sostituisci** l'ipotesi nella ricorrenza
3. **Verifica** che i conti tornino con l'induzione
4. **Controlla il caso base**

---

## 5. Risoluzione degli esercizi dalla lavagna

---

### Esercizio 1

$$T(m) = \begin{cases} 1 & \text{se } m = 1 \\ T(m/2) + T(m/3) + m & \text{altrimenti} \end{cases}$$

**Metodo: Akra-Bazzi** (due sottotaglie diverse: $m/2$ e $m/3$)

#### Step 1 — Trova $p$

$$\frac{1}{2^p} + \frac{1}{3^p} = 1$$

Per $p = 1$: $\frac{1}{2} + \frac{1}{3} = \frac{5}{6} < 1$ → troppo piccolo.
Per $p \to 0^+$: $1 + 1 = 2 > 1$.
Quindi $0 < p < 1$.

> Non ha soluzione in forma chiusa semplice, ma il punto chiave è confrontare $p$ con il grado di $f(m) = m^1 = m^{q}$ con $q=1$.

**Poiché $q = 1 > p$**, siamo nel caso in cui $f(m)$ domina.

#### Step 2 — Formula di Akra-Bazzi

$$T(m) = \Theta\!\left( m^p \left(1 + \int_1^m \frac{u}{u^{p+1}}\, du \right) \right) = \Theta\!\left( m^p \cdot \int_1^m u^{-p}\, du \right)$$

Poiché $p < 1$, l'integrale è $\Theta(m^{1-p})$, quindi:

$$T(m) = \Theta\!\left( m^p \cdot m^{1-p} \right) = \Theta(m)$$

> **Risultato:** $T(m) = \Theta(m)$

---

### Esercizio 2

$$T(m) = \begin{cases} 1 & \text{se } m = 1 \\ 2T(m/2) + T(m/3) + m & \text{altrimenti} \end{cases}$$

**Metodo: Akra-Bazzi** ($a_1 = 2, b_1 = 2$; $a_2 = 1, b_2 = 3$)

#### Step 1 — Trova $p$

$$\frac{2}{2^p} + \frac{1}{3^p} = 1 \implies \frac{1}{2^{p-1}} + \frac{1}{3^p} = 1$$

Per $p = 1$: $\frac{2}{2} + \frac{1}{3} = 1 + \frac{1}{3} > 1$ → troppo grande.
Per $p = 2$: $\frac{2}{4} + \frac{1}{9} = 0.5 + 0.11 < 1$ → troppo piccolo.
Quindi $1 < p < 2$. Il valore esatto non è semplice, ma $p \approx 1.2$.

**Poiché $f(m) = m^1$ e $p > 1$**, il costo delle foglie domina su $f$.

#### Risultato

$$T(m) = \Theta(m^p) \quad \text{con } 1 < p < 2$$

> **Risultato:** $T(m) = \Theta(m^p)$ dove $p$ è la soluzione di $2/2^p + 1/3^p = 1$.

---

### Esercizio 3

$$T(m) = \begin{cases} 1 & \text{se } m = 1 \\ 2T(m/2) + \sqrt{m} & \text{se } m > 1 \end{cases}$$

**Metodo: Master Theorem** ($a=2, b=2, f(m)=m^{1/2}$)

#### Calcolo del valore critico

$$n^{\log_b a} = m^{\log_2 2} = m^1 = m$$

#### Confronto con $f(m) = m^{1/2}$

$$f(m) = m^{1/2} = O(m^{1-\varepsilon}) \quad \text{con } \varepsilon = 1/2 > 0$$

→ **Caso 1** del Master Theorem.

$$\boxed{T(m) = \Theta(m)}$$

---

### Esercizio 4

$$T(m) = \begin{cases} 1 & \text{se } m = 1 \\ 8T(m/4) + \sqrt{m} & \text{se } m > 1 \end{cases}$$

**Metodo: Master Theorem** ($a=8, b=4, f(m)=m^{1/2}$)

#### Calcolo del valore critico

$$m^{\log_4 8} = m^{\log_4 8}$$

Calcolo: $\log_4 8 = \frac{\log 8}{\log 4} = \frac{3\log 2}{2\log 2} = \frac{3}{2}$

Quindi il valore critico è $m^{3/2}$.

#### Confronto con $f(m) = m^{1/2}$

$$f(m) = m^{1/2} = O(m^{3/2 - 1}) = O(m^{3/2 - \varepsilon}) \quad \text{con } \varepsilon = 1$$

→ **Caso 1** del Master Theorem.

$$\boxed{T(m) = \Theta(m^{3/2})}$$

---

### Esercizio 5

$$T(m) = \begin{cases} 1 & \text{se } m = 2 \\ 2T(m/2) + m & \text{se } m > 2 \end{cases}$$

*(Nota: caso base $m=2$ invece di $m=1$, non cambia l'analisi asintotica.)*

**Metodo: Master Theorem** ($a=2, b=2, f(m)=m$)

#### Calcolo del valore critico

$$m^{\log_2 2} = m^1 = m$$

#### Confronto con $f(m) = m$

$$f(m) = m = \Theta(m^1) = \Theta(m^{\log_b a})$$

→ **Caso 2** del Master Theorem (con $k=0$).

$$\boxed{T(m) = \Theta(m \log m)}$$

> Questo è il classico risultato del **Merge Sort**!

---

## 6. Schema di attacco rapido — Flowchart

```
La ricorrenza ha la forma aT(n/b) + f(n)?
│
├─ SÌ, con un solo termine ricorsivo → prova Master Theorem
│     ├─ Calcola n^{log_b a}
│     ├─ Confronta con f(n)
│     └─ Applica il caso corretto (1, 2 o 3)
│
└─ NO, ha più termini con tagle diverse (es. n/2 + n/3)?
      └─ Usa Akra-Bazzi
            ├─ Risolvi ∑ aᵢ/bᵢ^p = 1 per trovare p
            └─ Calcola l'integrale e concludi
```

---

## 7. Trucchi e tariffe rapide da ricordare

| Ricorrenza | Risultato | Note |
|---|---|---|
| $T(n) = T(n/2) + 1$ | $\Theta(\log n)$ | Ricerca binaria |
| $T(n) = 2T(n/2) + n$ | $\Theta(n \log n)$ | Merge Sort |
| $T(n) = 2T(n/2) + 1$ | $\Theta(n)$ | Attraversamento albero |
| $T(n) = T(n-1) + n$ | $\Theta(n^2)$ | Insertion Sort |
| $T(n) = aT(n/b) + n^{\log_b a}$ | $\Theta(n^{\log_b a} \log n)$ | Caso 2 MT |
| $T(n) = 8T(n/2) + n^2$ | $\Theta(n^3)$ | Caso 1: $\log_2 8 = 3 > 2$ |

---

*Metodi di riferimento: Master Theorem (CLRS §4.5), Akra-Bazzi (Leighton 1996).*
