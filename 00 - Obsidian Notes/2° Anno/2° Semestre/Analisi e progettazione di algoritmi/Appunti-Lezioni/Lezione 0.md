---
Date: 2026-03-03
Professore: Benerecetti
tags:
  - "#APA"
  - 6-CFU
---
# APA — Lezione 1: Analisi della Complessità e Notazione Asintotica
**Corso:** Analisi e Progettazione di Algoritmi | **CFU:** 6
*Seconda parte del corso di Algoritmica (continua dal primo semestre)*

---

## 📋 Informazioni pratiche

| Campo | Dettaglio |
$$
|---|---|
$$
| Orario | Mar (quest'ora) + Gio 16:15–18:00 (anticipato di 15 min su richiesta) |
| Comunicazioni | Iscriversi al sito docenti e **attivare ricezione email** |
| Teams | Attivato dalla settimana successiva (solo per emergenze/didattica remota) |

### Modalità d'esame
- **Prova scritta** con esercizi di analisi e progettazione (nessun progetto)
- Corso nuovo → non esiste ancora uno storico completo di esercizi; parte verrà recuperata dal vecchio corso di Algoritmica

---

## 🎯 Obiettivi del corso

Il corso si divide in due macro-aree:

### 1. Analisi degli algoritmi
- Formalizzare la stima del **tempo di esecuzione** (introdotta informalmente nel primo semestre)
- Tecniche di analisi della **complessità computazionale**
- Dimostrazione della **correttezza** degli algoritmi

### 2. Progettazione degli algoritmi
Dato un problema, come si costruisce una soluzione algoritmica? Si seguono due principi fondamentali:

> [!info] Decomposizione
> Scomporre il problema in **sottoproblemi più semplici**, risolverli separatamente e comporre le soluzioni.
> *Esempio già visto:* problema delle coppie → generazione + filtraggio/conteggio.

> [!info] Riduzione
> Ridurre un problema a un **problema già noto** e risolverlo sfruttando quella soluzione.
> *Esempio già visto:* ordinamento topologico → ridotto alla visita DFS su grafi.

### Tecniche avanzate (se il tempo lo consente)
- **Divide et impera** — decomposizione ricorsiva
- **Programmazione dinamica** — problemi di ottimizzazione (trovare la soluzione *migliore* tra molte ammissibili)
- **Algoritmi greedy** — classi specifiche di problemi di ottimizzazione

---

## 🤖 Modello Computazionale RAM

Per analizzare matematicamente un algoritmo serve un **ponte** tra il mondo degli algoritmi e il mondo della matematica. Questo ponte è il modello RAM (*Random Access Machine*).

> [!info] Modello RAM
> Astrazione di un calcolatore con:
> - **Memoria illimitata** di celle accessibili a tempo costante (accesso diretto)
> - Un insieme di **istruzioni elementari:** operazioni aritmetiche, lettura/scrittura in memoria
> - **Costo unitario:** ogni istruzione elementare richiede esattamente **1 unità di tempo**

### Funzione di tempo di esecuzione
$$T_A : \mathbb{N} \rightarrow \mathbb{R}^+$$
Dove $n \in \mathbb{N}$ è la **dimensione dell'input** (es. numero di elementi di un array) e $T_A(n)$ è il numero di operazioni elementari necessarie.

> [!info] Perché $\mathbb{R}^+$ e non $\mathbb{N}$?
> Il numero di operazioni è un naturale, ma le espressioni che useremo (es. con logaritmi) assumono valori reali. Lavorare in $\mathbb{R}$ ci dà accesso a strumenti più potenti: derivate, integrali, limiti — tutti strumenti di $\mathbb{R}$ non disponibili (o difficili) nel discreto.

> [!tip] Codifica dell'input
> - **Input numerico** → per semplicità si usa codifica **unaria** (complessità = valore del numero). La codifica corretta (binaria) darebbe $\log_2 n$ bit, che produce risultati diversi.
> - **Input strutturato** (array, grafi, …) → la dimensione è il **numero di elementi**: il problema della codifica scompare.

---

## 📐 Analisi del tempo di esecuzione — Algoritmi iterativi

### Metodo: contributo per linea

Per ogni linea di codice:
$$\text{contributo}_i = \underbrace{\text{numero di esecuzioni}(n)}_{\text{dipende da } n} \times \underbrace{\text{costo singola esecuzione}}_{\text{n° operazioni elementari}}$$
$$T(n) = \sum_{i} \text{contributo}_i$$
> [!tip] For vs While
> Nel ciclo `for` il numero di iterazioni è **esplicito** (dato dagli estremi). Nel ciclo `while` il numero di iterazioni è **implicito** e dipende dalla condizione — spesso richiede un'analisi separata per trovare un limite inferiore e superiore.

---

## 🔢 Caso di studio: Conteggio coppie ordinate

**Problema:** dato $n$, contare quante coppie $(i, j)$ con $i, j \in \{1, \ldots, n\}$ soddisfano $i \leq j$.

### Algoritmo 1 — Forza bruta

```python
1. sam = 0
2. for i = 1 to n:
3.   for j = 1 to n:
4.     if i <= j:
5.       sam = sam + 1
6. return sam
```

| Linea | Esecuzioni                                 | Costo/esec | Contributo         |
| ----- | ------------------------------------------ | ---------- | ------------------ |
| 1     | $1$                                        | $1$        | $1$                |
| 2     | $n+1$                                      | $2$        | $2(n+1)$           |
| 3     | $\sum_{i=1}^{n}(n+1)$                      | $2$        | $2n(n+1)$          |
| 4     | $\sum_{i=1}^{n} n$                         | $3$        | $3n^2$             |
| 5     | $\sum_{i=1}^{n}(n-i+1) = \frac{n(n+1)}{2}$ | $1$        | $\frac{n(n+1)}{2}$ |
| 6     | $1$                                        | $1$        | $1$                |
$$T_1(n) = \frac{7}{2}n^2 + \frac{9}{2}n + 4 \quad \Rightarrow \quad \Theta(n^2)$$
### Algoritmo 2 — Prima ottimizzazione (j parte da i)

Far partire `j` da `i` invece che da `1`: si evitano i confronti inutili (tutti i `j < i` falliscono sicuramente).

> [!warning] Nessun miglioramento asintotico
> La linea 5 viene eseguita le stesse volte di prima (conta solo le coppie buone). Il termine dominante rimane $\frac{n(n+1)}{2}$, ancora $\Theta($n^2$)$. Il miglioramento è solo nella costante moltiplicativa.

### Algoritmo 3 — Eliminazione del ciclo interno

**Osservazione chiave:** fissato $i$, il numero di $j \geq i$ è esattamente $n - i + 1$, noto a priori senza scorrere i valori.

```python
1. sam = 0
2. for i = 1 to n:
3.   sam = sam + (n - i + 1)
4. return sam
```
$$T_3(n) = 6n + 4 \quad \Rightarrow \quad \Theta(n)$$
> [!tip] Miglioramento asintotico
> Da $\Theta($n^2$)$ a $\Theta(n)$: un ciclo annidato in meno produce un salto di classe di complessità.

### Algoritmo 4 — Soluzione a tempo costante (geometrica)

**Riduzione algebrica:** le coppie $(i, j)$ corrispondono biunivocamente alle celle di una matrice $n \times n$. Totale celle: $n^2$. Le celle con $i \leq j$ sono il triangolo superiore + diagonale:
$$\text{risultato} = \frac{n^2 - n}{2} + n = \frac{n(n+1)}{2}$$
```python
1. return n * (n + 1) / 2
```
$$T_4(n) = O(1)$$
> [!tip] Tempo costante
> Nessun ciclo: la risposta si calcola in un numero fisso di operazioni indipendentemente da $n$.

---

> [!example] Lezione metodologica
> L'analisi riga per riga non serve solo a *misurare* il tempo: serve a **individuare le sorgenti di inefficienza** e a guidare verso soluzioni migliori. In questo caso ha portato da $O($n^2$)$ a $O(1)$ in tre passi.

---

## 📊 Notazione Asintotica

### Perché l'analisi asintotica?

Confrontare due funzioni punto per punto non è sempre possibile (potrebbero incrociarsi). Ci interessa il comportamento **al crescere illimitato di $n$**, cioè il regime asintotico.

> [!info] Intuizione fondamentale
> Un algoritmo è **intrinsecamente** migliore di un altro se lo è **indipendentemente dall'hardware** su cui gira. Un computer può essere $c$ volte più veloce di un altro, ma questo fattore è **costante** e non dipende da $n$. Due algoritmi sono equivalenti se la differenza tra loro è solo una costante moltiplicativa fissa.

### Le tre notazioni

| Notazione             | Significato intuitivo      | Analogia con $\leq, =, \geq$ |
| --------------------- | -------------------------- | ---------------------------- |
| $f(n) = O(g(n))$      | $f$ non è peggio di $g$    | $f \lesssim g$               |
| $f(n) = \Omega(g(n))$ | $f$ non è meglio di $g$    | $f \gtrsim g$                |
| $f(n) = \Theta(g(n))$ | $f$ e $g$ sono equivalenti | $f \asymp g$                 |

---

### $O$ grande — Limite superiore asintotico

> [!info] O grande
> $$f(n) = O(g(n)) \iff \exists\, c > 0,\ \exists\, n_0 > 0 : \forall n \geq n_0,\quad f(n) \leq c \cdot g(n)$$
**Interpretazione:** $c$ è il fattore con cui posso *rallentare* l'esecutore di $g$ per renderlo peggio di $f$. Se esiste tale $c$ fissata a priori, allora $f$ non è peggio di $g$.

> [!warning] $c$ deve essere scelta a priori!
> $c$ e $n_0$ vanno scelti **prima** di far variare $n$ — sono costanti, non funzioni di $n$. Altrimenti si potrebbe scegliere $c = n$ e "dimostrare" che $n^2 = O(n)$, il che è falso.
>
> **Esempio del paradosso:** se $c$ potesse dipendere da $n$, fissato $n = 100$, scelgo $c = 100$ e ottengo $100^2 \leq 100 \cdot 100$ ✓. Ma poi per $n = 101$ devo scegliere $c = 101$… $c$ non è più una costante, è diventata una funzione.

---

### $\Omega$ grande — Limite inferiore asintotico

> [!info] Omega grande
> $$f(n) = \Omega(g(n)) \iff \exists\, c > 0,\ \exists\, n_0 > 0 : \forall n \geq n_0,\quad f(n) \geq c \cdot g(n)$$
Duale di $O$ grande: $c$ è ora il fattore con cui *accelero* l'esecutore di $g$.

---

### $\Theta$ (Theta) — Equivalenza asintotica

> [!info] Theta
> $$f(n) = \Theta(g(n)) \iff \exists\, c_1, c_2 > 0,\ \exists\, n_0 > 0 : \forall n \geq n_0,\quad c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$$
Equivale a: $f = O(g)$ **e** $f = \Omega(g)$.

Graficamente: da $n_0$ in poi, $f$ è "intrappolata" tra $c_1 \cdot g$ (sotto) e $c_2 \cdot g$ (sopra).

> [!example] Conseguenze pratiche
> - $2n,\ 5n,\ n+100,\ 3n+\log n$ sono tutti $\Theta(n)$ — tutte rette, equivalenti.
> - $n^2,\ 3n^2+7n,\ \frac{n(n+1)}{2}$ sono tutti $\Theta($n^2$)$ — tutte parabole, equivalenti.
> - $n = O($n^2$)$ ma $n \neq \Theta($n^2$)$ — non si può fare il contrario con una costante fissa.

---

## 📈 Velocità di crescita e impatto pratico

Al crescere di $n$, prestazioni degradano a velocità diverse. Dati 10 secondi di limite, la dimensione massima gestibile è tanto più grande quanto più lenta è la crescita:

| Classe        | Esempio                  | Degrado      |
| ------------- | ------------------------ | ------------ |
| $O(1)$        | Formula diretta          | Nessuno      |
| $O(\log n)$   | Ricerca binaria          | Trascurabile |
| $O(n)$        | Scansione array          | Lento        |
| $O(n \log n)$ | MergeSort                | Moderato     |
| $O($n^2$)$    | Doppio for annidato      | Rapido       |
| $O(2^n)$      | Forza bruta combinatoria | Esplosivo    |

---

## 🔬 Calcolo della classe asintotica — Metodo dei limiti

Invece di usare direttamente le definizioni (difficile con logaritmi ed esponenziali), si usa il seguente criterio:
$$L = \lim_{n \to \infty} \frac{f(n)}{g(n)}$$

| Valore di $L$     | Relazione                                                                |
| ----------------- | ------------------------------------------------------------------------ |
| $L = 0$           | $f(n) = O(g(n))$, $f(n) \neq \Omega(g(n))$ — $g$ cresce più velocemente  |
| $L = +\infty$     | $f(n) = \Omega(g(n))$, $f(n) \neq O(g(n))$ — $f$ cresce più velocemente  |
| $0 < L < +\infty$ | $f(n) = \Theta(g(n))$ — stessa velocità di crescita (a meno di costante) |

> [!tip] Per l'esame
> Quando si chiede di confrontare due funzioni, **calcolare il limite del rapporto** è l'approccio più pratico. Ripassare: regola di L'Hôpital, limiti notevoli con logaritmi ed esponenziali.

---

## 📅 Prossimi argomenti

- [ ] Dimostrazione formale della coerenza tra metodo dei limiti e definizioni di $O$, $\Omega$, $\Theta$
- [ ] Esempi di calcolo con logaritmi ed esponenziali
- [ ] Analisi degli **algoritmi ricorsivi** (la ripetizione è implicita → si usano le *relazioni di ricorrenza*)
- [ ] Algoritmi di ordinamento come caso di studio per le tecniche di analisi e progettazione