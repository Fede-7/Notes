---
Date:
Professore:
tags:
---
# 📚 Elementi di Informatica Teorica — Lezione Privata Completa
> Guida per superare lo scritto | Prof. A. De Luca | Federico II Napoli
> Tags: #informatica-teorica #esame #studio

---

# 🗺️ Mappa del Corso

Il corso si divide in **due macroparti**:

1. **Calcolabilità** → Linguaggio S → Funzioni ricorsive primitive → Codifica → Halt problem → Insiemi r.e.
2. **Linguaggi Formali** → Automi (DFA/NFA) → Linguaggi regolari → CFG

Ogni esame scritto ha tipicamente **6 esercizi**: i primi 3 su automi/grammatiche/pumping lemma, gli ultimi 3 su ricorsive primitive/calcolabilità/insiemi.

---

# PARTE 1 — CALCOLABILITÀ

---

## 1. Il Linguaggio S

### 1.1 Concetto di calcolabilità

Una **funzione totale** è definita per ogni input:  $f: \mathbb{N}^k \to \mathbb{N}$

Una **funzione parziale** è definita solo per alcuni input:  $f: D \subseteq \mathbb{N}^k \to \mathbb{N}$

> Il simbolo $\uparrow$ indica che la funzione **diverge** (il programma non termina).

**Tesi di Church-Turing:** Qualsiasi funzione determinabile con una procedura algoritmica è parzialmente calcolabile.

- **Funzione parzialmente calcolabile**: esiste un algoritmo (S-programma) che la rappresenta.
- **Funzione calcolabile**: è *totale* e parzialmente calcolabile.
- **Predicato**: funzione totale con codominio $\{0,1\}$ (0 = FALSO, 1 = VERO).

---

### 1.2 Sintassi del Linguaggio S

#### Variabili
| Tipo | Notazione | Inizializzazione |
$$
|---|---|---|
$$
| Input | $X_1, $X_2$, \ldots$ | Valore dell'input |
| Output | $Y$ | 0 |
| Temporanee | $Z_1, $Z_2$, \ldots$ | 0 |

#### Istruzioni (solo 4!)
| Istruzione | Effetto |
$$
|---|---|
$$
$$
| `V <-- V` | Istruzione pigra (nulla) |
$$
$$
| `V <-- V+1` | Incrementa V di 1 |
$$
$$
| `V <-- V-1` | Decrementa V di 1 (se V=0, ignorata) |
$$
| `IF V != 0 GOTO L` | Salta all'etichetta L se V≠0 |

> **Etichette** dalla A alla D (numerate), con **E** riservata alla terminazione.

#### Macro importanti da sapere a memoria
$$
**Salto incondizionato `GOTO L`:**
$$
```
V <-- V+1
IF V != 0 GOTO L
```
$$
**Azzeramento `V <-- 0`:**
$$
```
[A] V <-- V-1
    IF V != 0 GOTO A
```
$$
**Assegnazione `V <-- V1`:**
$$
```
[C] IF V1 != 0 GOTO A
    GOTO E
[A] V <-- V+1
    V1 <-- V1-1
    GOTO C
```

---

### 1.3 Stato e Istantanea

- **Stato** di P: insieme di equazioni `V = n` per ogni variabile di P.
- **Istantanea**: coppia $(i, \sigma)$ dove $i$ è l'indice dell'istruzione corrente e $\sigma$ è lo stato.
- **Istantanea terminale**: $(l+1, \sigma)$ con $l$ = lunghezza del programma.
- **Calcolo terminante**: sequenza finita di istantanee che termina in un'istantanea terminale.

La funzione calcolata da P:
$$\Psi_P^{(k)}(x_1,\ldots,x_k) = \begin{cases} y & \text{se esiste un calcolo terminante} \\ \uparrow & \text{altrimenti} \end{cases}$$
---

## 2. Funzioni Ricorsive Primitive e Classi PRC

### 2.1 Classi PRC

Un insieme di funzioni totali $\mathcal{C}$ è **PRC** se:
1. Contiene le **funzioni iniziali**: $n(x)=0$,  $s(x)=x+1$,  $u_i^{(n)}($x_1$,\ldots,$x_n$)=x_i$
$$
2. È chiuso per **composizione**
$$
$$
3. È chiuso per **ricorsione primitiva**
$$
> ⭐ **Fatto chiave**: le funzioni ricorsive primitive sono la **più piccola** classe PRC, e ogni funzione ricorsiva primitiva è calcolabile.

---

### 2.2 Composizione
$$h(x_1,\ldots,x_n) = f(g_1(x_1,\ldots,x_n),\ldots,g_k(x_1,\ldots,x_n))$$
**Teorema**: Se $f, $g_1$,\ldots,g_k$ sono parzialmente calcolabili, allora $h$ è parzialmente calcolabile.

---

### 2.3 Ricorsione Primitiva
$$h(x_1,\ldots,x_{n-1}, 0) = f(x_1,\ldots,x_{n-1})$$
$$h(x_1,\ldots,x_{n-1}, t+1) = g(x_1,\ldots,x_{n-1}, t, h(x_1,\ldots,x_{n-1},t))$$
**Teorema**: Se $f$ e $g$ sono calcolabili, allora $h$ è calcolabile.

---

### 2.4 Funzioni Ricorsive Primitive — Esempi fondamentali

| Funzione                                    | Definizione                                          | Come si dimostra       |                         |
| ------------------------------------------- | ---------------------------------------------------- | ---------------------- | ----------------------- |
| Addizione $x+y$                             | $a(x,0)=x$;  $a(x,t+1)=s(a(x,t))$                    | Ric. primitiva         |                         |
| Moltiplicazione $x \cdot y$                 | $m(x,0)=0$;  $m(x,t+1)=a(m(x,t),x)$                  | Ric. primitiva         |                         |
| Fattoriale $x!$                             | $0!=1$;  $(t+1)!=m(t+1,t!)$                          | Ric. primitiva         |                         |
| Predecessore $p(x)$                         | $p(0)=0$;  $p(t+1)=t$                                | Ric. primitiva         |                         |
| Sottrazione propria $x \dotminus y$         | $x\dotminus 0=x$;  $x\dotminus(t+1)=p(x\dotminus t)$ | Ric. primitiva         |                         |
| Rilevatore di zeri $\alpha(x)=1\dotminus x$ | $\alpha(x)=1 \text{ se } x=0$                        | Comp. di succ. e sott. |                         |
| Uguaglianza $\beta(x,y)$                    | $\alpha(\|x-y\|)$                                    | Composizione           |                         |
| Predicato Primo                             | $x>1 \wedge \forall z\leq x: (\neg(z                 | x) \vee z=1 \vee z=x)$ | Quantificatori limitati |

---

### 2.5 Proprietà di Chiusura PRC

#### Congiunzione, disgiunzione, negazione
Se $p, q$ sono predicati in $\mathcal{C}$ PRC, allora anche $p \wedge q$, $p \vee q$, $\neg p \in \mathcal{C}$.
$$
**Dimostrazione:**
$$
- $(p \wedge q)(x) = p(x) \cdot q(x)$  → prodotto di funzioni RP
- $(\neg p)(x) = \alpha(p(x))$  → composizione con rilevatore di zeri
- $(p \vee q) \Leftrightarrow \neg(\neg p \wedge \neg q)$  → De Morgan

#### Definizione per casi
Se $g, h \in \mathcal{C}$ e $p$ è un predicato in $\mathcal{C}$:
$$f(x) = \begin{cases} g(x) & p(x) \\ h(x) & \neg p(x) \end{cases}$$
Si dimostra: $f(x) = g(x) \cdot p(x) + h(x) \cdot \neg p(x) \in \mathcal{C}$.

#### Sommatoria e Produttoria
$$\sigma_f(x,y) = \sum_{i=0}^{y} f(x,i), \quad \pi_f(x,y) = \prod_{i=0}^{y} f(x,i)$$
$$
**Dimostrazione** per ricorsione primitiva:
$$
- $\sigma_f(x,0) = f(x,0)$;  $\sigma_f(x,t+1) = \sigma_f(x,t) + f(x,t+1)$

#### Quantificatori limitati
$$E_p(x,y) \Leftrightarrow \exists t \leq y: p(x,t) \quad \text{(vero se la sommatoria > 0)}$$
$$U_p(x,y) \Leftrightarrow \forall t \leq y: p(x,t) \quad \text{(vero se la produttoria = 1)}$$
#### Divisibilità (da ricorsiva primitiva!)
$$x | y \Leftrightarrow \exists z \leq y: x \cdot z = y$$
#### Minimalizzazione limitata
$$\min_{t \leq y} p(x,t) = \text{il minimo } t \leq y \text{ per cui } p \text{ è vera (0 se non esiste)}$$
$$
**Applicazioni importanti:**
$$
- Divisione con resto: $\lfloor x/y \rfloor = \min_{t \leq x}\left((t+1)y > x\right)$
- $x \mod y = x \dotminus \lfloor x/y \rfloor \cdot y$
- $P_n$ (n-esimo primo): $P_0=0$, $P_{n+1} = \min_{t \leq P_n!+1}(\text{Primo}(t) \wedge t >$ $P_n$$)$

---

### 2.6 Minimalizzazione illimitata e funzioni parzialmente calcolabili
$$\mu_t \, p(x,t) = \begin{cases} \min\{t \in \mathbb{N}: p(x,t)\} & \text{se esiste} \\ \uparrow & \text{altrimenti} \end{cases}$$
Programma S:
```
[A] IF p(X1,...,Xn, Y) GOTO E
    Y <-- Y+1
    GOTO A
```

**Teorema di caratterizzazione**: Una funzione è parzialmente calcolabile se e solo se si ottiene dalle funzioni iniziali mediante un numero finito di composizioni, ricorsioni primitive e minimalizzazioni illimitate.

---

## 3. Funzione di Pairing e Numeri di Gödel

### 3.1 Funzione di Pairing (l'"angoletto")
$$\langle x, y \rangle = 2^x(2y+1) - 1$$
$$
**Proprietà**:
$$
- È **biettiva**: ogni coppia $(x,y)$ ha un unico codice, e ogni numero naturale è codice di una unica coppia.
- È **ricorsiva primitiva**.

**Inverse parziali** (ricorsive primitive per minimalizzazione limitata):
- $l(z) = x$ tale che $2^x | (z+1)$ ma $2^{x+1} \nmid (z+1)$  *(estrai la potenza di 2 da z+1)*
- $r(z) = y$ tale che $z+1 = 2^{l(z)}(2y+1)$
$$
**Come calcolare:**
$$
1. Dato $z$: $z+1 = 2^{l(z)} \cdot \text{(dispari)}$. L'esponente è $l(z)$, poi $r(z) = \frac{(z+1)/2^{l(z)}-1}{2}$.

**Esempio**: $\langle 2,3 \rangle = 2^2(7)-1 = 27$. Calcolare $l(23)$: $24 = 2^3 \cdot 3$, dunque $l(23)=3$, $r(23)=1$.

---

### 3.2 Numeri di Gödel
$$[a_1, \ldots, a_k] = \prod_{i=1}^{k} P_i^{a_i}$$
dove $P_i$ è l'$i$-esimo numero primo ($P_1=2, $P_2$=3, $P_3$=5, \ldots$)
$$
**Proprietà**:
$$
- **Non** biettiva (non è surgettiva: 0 non è in immagine; non è iniettiva: aggiungere 0 non cambia il valore).
- Per il TFA: $[$a_1$,\ldots,a_n] = [$b_1$,\ldots,b_m] \Rightarrow$ le sequenze coincidono (a parte gli zeri finali).
$$
**Inverse parziali** (ricorsive primitive):
$$
- $(x)_i = \min_{t \leq x} \neg(P_i^{t+1} | x)$  ← esponente di $P_i$ nella fattorizzazione di $x$
- $Lt(x) = \min_{i \leq x}\left((x)_i \neq 0 \wedge \forall j \leq x: j \leq i \vee (x)_j = 0\right)$ ← lunghezza della sequenza

**Esempio**: $[2,0,1] = 2^2 \cdot 3^0 \cdot 5^1 = 20$. $(30)_2 = 1$ poiché $30=2^1 \cdot 3^1 \cdot 5^1$.

---

## 4. Codifica di Programmi

### 4.1 Codifica delle variabili
$$Y \mapsto 1,\; X_1 \mapsto 2,\; Z_1 \mapsto 3,\; X_2 \mapsto 4,\; Z_2 \mapsto 5, \ldots$$
Assenza di etichetta → 0. Etichette: $A_1 \mapsto 1, B_1 \mapsto 2, C_1 \mapsto 3, D_1 \mapsto 4, E \mapsto 5, \ldots$

Tipo istruzione: Pigra → 0, Incremento → 1, Decremento → 2, Salto a etichetta $n$ → $n+2$.

### 4.2 Codifica di un'istruzione
$$\#(I) = \langle a, \langle b, c \rangle \rangle$$
dove: $a$ = etichetta (0 se assente), $b$ = tipo, $c$ = numero variabile $- 1$.

**Esempio**: `[A] X1 <-- X1+1` ha terna $(1,1,1)$, codice $\langle 1, \langle 1,1 \rangle \rangle = \langle 1,5 \rangle = 21$.

### 4.3 Codifica di un programma
$$\#(P) = [{\#(I_1)}, \ldots, {\#(I_k)}]_k - 1$$
La sottrazione di 1 garantisce che ogni numero naturale codifichi un programma (surjettività). Il programma vuoto ha codice 0.

### 4.4 Codifica di uno stato
$$\#(\sigma) = \prod_{i} P_{\#(V_i)}^{n_i}$$
dove $n_i$ è il valore della variabile $V_i$ nello stato $\sigma$.

---

## 5. Problema della Fermata e Funzione Universale

### 5.1 Esistenza di funzioni non calcolabili (argomento diagonale)

Costruiamo la matrice: riga $n$, colonna $x$ → $\Psi_{P_n}^{(1)}(x)$.

Definiamo:
$$g(n) = \begin{cases} \Psi_{P_n}^{(1)}(n)+1 & \text{se } \Psi_{P_n}^{(1)}(n)\downarrow \\ 0 & \text{altrimenti} \end{cases}$$
Per assurdo: se $g = \Psi_{P_m}^{(1)}$, allora $g(m) = \Psi_{P_m}^{(1)}(m)+1 = g(m)$. **Assurdo** → $g$ non è calcolabile.

---

### 5.2 Problema della Fermata
$$\text{HALT}(x,y) \Leftrightarrow \Psi_{P_y}^{(1)}(x)\downarrow$$
$$
**Teorema**: HALT non è calcolabile.
$$
**Dimostrazione**: Supponiamo HALT calcolabile. Scriviamo:
```
[A] IF HALT(X,X) GOTO A
```
Sia $y_0$ il numero di questo programma. Allora:
$$\Psi_{P_{y_0}}^{(1)}(x) = \begin{cases} 0 & \text{se } \Psi_{P_x}^{(1)}(x)\uparrow \\ \uparrow & \text{se } \Psi_{P_x}^{(1)}(x)\downarrow \end{cases}$$
Per $x = y_0$: $\text{HALT}($y_0$, $y_0$) \Leftrightarrow \neg\text{HALT}($y_0$,$y_0$)$. **Assurdo**.

---

### 5.3 Funzione Universale
$$\Phi^{(n)}(x_1,\ldots,x_n, y) = \Psi_{P_y}^{(n)}(x_1,\ldots,x_n)$$
**Teorema di Universalità**: $\Phi^{(n)}$ è parzialmente calcolabile per ogni $n$.

Il programma universale simula $P_y$ su input $($x_1$,\ldots,$x_n$)$ codificando stato e istruzione corrente tramite Numeri di Gödel.

---

### 5.4 Predicato STP
$$\text{STP}^{(n)}(x_1,\ldots,x_n, y, t) \Leftrightarrow \text{il programma } P_y \text{ su input } (x_1,\ldots,x_n) \text{ termina in } \leq t \text{ passi}$$
- **STP è ricorsivo primitivo** (si aggiunge un contatore al programma universale).
- Relazione chiave: $\text{HALT}(x,y) \Leftrightarrow \exists t: \text{STP}(x,y,t)$

---

### 5.5 Diagramma riassuntivo delle funzioni

```
┌──────────────────────────────────────────────┐
│          Funzioni Parziali                   │
│  ┌────────────────────────────────────────┐  │
│  │       Funzioni Parzialmente Calcolabili│  │
│  │  ┌──────────────────────────────────┐  │  │
│  │  │      Funzioni Calcolabili        │  │  │
│  │  │  ┌────────────────────────────┐  │  │  │
│  │  │  │ Funzioni Ricorsive         │  │  │  │
│  │  │  │ Primitive                  │  │  │  │
│  │  │  └────────────────────────────┘  │  │  │
│  │  └──────────────────────────────────┘  │  │
│  └────────────────────────────────────────┘  │
└──────────────────────────────────────────────┘
```

> Es. Ackermann-Péter: calcolabile ma **non** ricorsiva primitiva.

---

## 6. Insiemi Ricorsivi e Ricorsivamente Enumerabili

### 6.1 Funzione caratteristica
$$f_S(a_1,\ldots,a_n) = \begin{cases} 1 & (a_1,\ldots,a_n) \in S \\ 0 & \text{altrimenti} \end{cases}$$
- $S$ è **ricorsivo** $\Leftrightarrow$ $f_S$ è calcolabile.
- $S$ è **ricorsivo primitivo** $\Leftrightarrow$ $f_S$ è ricorsiva primitiva.

---

### 6.2 Insieme Ricorsivamente Enumerabile (r.e.)

$S \subseteq \mathbb{N}$ è **r.e.** se $\exists g$ parzialmente calcolabile: $S = \{x \in \mathbb{N}: g(x)\downarrow\}$.

**Intuizione**: esiste una *semi-procedura di decisione* (termina sse l'elemento è in $S$).

**Importante**: ogni insieme ricorsivo è anche r.e.:
```
[A] IF ¬f_S(X) GOTO A
```

---

### 6.3 Relazione tra ricorsività e r.e.

> ⭐ **Teorema fondamentale**: $S$ è ricorsivo $\Leftrightarrow$ $S$ e $\bar{S}$ sono entrambi r.e.

**Dimostrazione** (⇐): Siano $S = \{x: \Psi_{P_p}(x)\downarrow\}$ e $\bar{S} = \{x: \Psi_{P_q}(x)\downarrow\}$. Allora $f_S$ è calcolata da:
```
[A] IF STP(X,p,Z) GOTO B
    IF STP(X,q,Z) GOTO E
    Z <-- Z+1
    GOTO A
[B] Y <-- Y+1
```
Si usa STP (non direttamente le funzioni parziali) per evitare loop: siccome $S \cup \bar{S} = \mathbb{N}$, uno dei due STP prima o poi termina.

---

### 6.4 Chiusura per operazioni insiemistiche

**Insiemi ricorsivi** sono chiusi per: $\cup$, $\cap$, complemento $\bar{S}$.

**Insiemi r.e.** sono chiusi per: $\cup$, $\cap$. **Non** per complemento.

**Dimostrazione chiusura r.e. per $\cap$:**
```
Z <-- g(X)
Z <-- h(X)
```
Termina sse $g(x)\downarrow$ e $h(x)\downarrow$.

**Dimostrazione chiusura r.e. per $\cup$:**
```
[A] IF STP(X,p,Z) GOTO E
    IF STP(X,q,Z) GOTO E
    Z <-- Z+1
    GOTO A
```

---

### 6.5 $W_n$ e l'insieme diagonale $K$
$$W_n = \{x \in \mathbb{N}: \Phi(x,n)\downarrow\}$$
$S$ è r.e. $\Leftrightarrow$ $\exists n: S = W_n$.
$$K = \{x \in \mathbb{N}: x \in W_x\} = \{x: \Phi(x,x)\downarrow\}$$
> **Teorema di Enumerazione**: $K$ è r.e. ma **non** ricorsivo (né il suo complemento $\bar{K}$ è r.e.).

**Dimostrazione** ($K$ non ricorsivo via assurdo): Se $\bar{K}$ fosse r.e., allora $\bar{K} = W_i$ per qualche $i$. Ma allora $i \in \bar{K} \Leftrightarrow i \in W_i \Leftrightarrow i \in K$. Contraddizione.

---

### 6.6 Teorema di Caratterizzazione degli insiemi r.e.

Per $S \neq \emptyset$ non vuoto, le seguenti sono equivalenti:
1. $S$ è r.e.
2. $\exists f$ **ricorsiva primitiva** tale che $S = \{f(n): n \in \mathbb{N}\}$
3. $\exists f$ **calcolabile** tale che $S = \{f(n): n \in \mathbb{N}\}$
4. $\exists f$ **parzialmente calcolabile** tale che $S = \{f(n): f(n)\downarrow\}$

**Tecnica utile per gli esercizi**: per mostrare che un insieme $S$ è r.e., si trova una funzione $h$ ricorsiva primitiva tale che $S = \{h(n): n \in \mathbb{N}\}$.

**Dimostrazione** (1 ⟹ 2): Dato $R$ predicato binario r.p. con $S = \{x: \exists t: R(x,t)\}$ e fissato $x_0 \in S$:
$$h(x) = \begin{cases} l(x) & R(l(x), r(x)) \\ x_0 & \text{altrimenti} \end{cases}$$
Allora $S = \{h(x): x \in \mathbb{N}\}$.

---

### 6.7 Schemi di dimostrazione tipici negli esercizi

#### "Mostrare che $S$ è r.e."
**Metodo 1**: Esibire $g$ parzialmente calcolabile con $S = \{x: g(x)\downarrow\}$.
**Metodo 2**: Esibire $h$ r.p. (o calcolabile) con $S = \{h(n): n \in \mathbb{N}\}$.
**Metodo 3**: $S = \{x: \Phi(f(x), g(x))\downarrow\}$ per $f,g$ calcolabili.

#### "Mostrare che $S$ non è ricorsivo"
Mostrare che permetterebbe di calcolare HALT (riduzione).

#### "Mostrare che $g$ è parzialmente calcolabile"
Scrivere un programma S (usando macro STP, HALT, ecc.) che la calcola, oppure esprimerla come composizione di funzioni parzialmente calcolabili.

---

# PARTE 2 — LINGUAGGI FORMALI

---

## 7. Macchine di Turing

Una **Macchina di Turing** è una quadrupla $(Q, A, I, $q_1$)$:
- $Q$: insieme finito di stati
- $A$: alfabeto (non contiene $\sqcup, L, R$)
- $I \subseteq Q \times (A \cup \{\sqcup\}) \times (A \cup \{\sqcup, L, R\}) \times Q$: istruzioni
- $q_1$: stato iniziale

Un linguaggio $L$ è **r.e.** se esiste una TM che termina sse l'input è in $L$.
Un linguaggio $L$ è **ricorsivo** se $L$ e $\bar{L}$ sono r.e.

---

## 8. Automi a Stati Finiti

### 8.1 DFA (Automa Finito Deterministico)

Un **DFA** è una quintupla $(Q, A, \delta, $q_1$, F)$:
- $Q$: insieme finito di stati
- $A$: alfabeto
- $\delta: Q \times A \to Q$: funzione di transizione (totale, deterministica)
- $q_1 \in Q$: stato iniziale
- $F \subseteq Q$: stati accettanti

**Funzione di transizione iterata** $\delta^*$:
$$\delta^*(q, \varepsilon) = q, \quad \delta^*(q, wa) = \delta(\delta^*(q,w), a)$$
**Linguaggio accettato**: $L(M) = \{w \in A^*: \delta^*($q_1$, w) \in F\}$

**Disegno**: nodi = stati, archi etichettati, doppio cerchio = stato accettante, freccia entrante = stato iniziale.

---

### 8.2 NFA (Automa Finito Non Deterministico)

Un **NFA** è una quintupla $(Q, A, \delta, $q_1$, F)$ con $\delta: Q \times A \to \mathcal{P}(Q)$.
$$\delta^*(q, \varepsilon) = \{q\}, \quad \delta^*(q, wa) = \bigcup_{q' \in \delta^*(q,w)} \delta(q', a)$$
$L(M) = \{w: \delta^*($q_1$, w) \cap F \neq \emptyset\}$

**Vantaggio**: più facile da costruire (non serve definire ogni transizione).

---

### 8.3 Equivalenza DFA ↔ NFA

**Teorema**: $L$ è regolare $\Leftrightarrow$ $L = L(M)$ per qualche NFA $M$.

**Costruzione** NFA → DFA (costruzione per sottoinsiemi):
- Stati del DFA: sottoinsiemi di $Q$ (cioè elementi di $\mathcal{P}(Q)$)
- Stato iniziale: $\{q_1\}$
- $\delta'(Q', a) = \bigcup_{q \in Q'} \delta(q,a)$
- $F' = \{Q' \subseteq Q: Q' \cap F \neq \emptyset\}$

---

### 8.4 DFA Non-Restarting

Un DFA è **non-restarting** se $q_1 \notin \delta(Q \times A)$ (non si torna mai allo stato iniziale).

Ogni DFA può essere trasformato in un DFA non-restarting equivalente aggiungendo uno stato iniziale $q_0$ che emula $q_1$.

**Utilità**: semplifica le dimostrazioni di chiusura.

---

## 9. Linguaggi Regolari

### 9.1 Definizione

$L \subseteq A^*$ è **regolare** se esiste un DFA $M$ con $L = L(M)$.

---

### 9.2 Chiusura dei Linguaggi Regolari

| Operazione                  | Chiusura | Tecnica                                                    |
| --------------------------- | -------- | ---------------------------------------------------------- |
| Complemento $\bar{L}$       | ✅        | Scambia $F$ e $Q \setminus F$                              |
| Unione $L \cup L'$          | ✅        | NFA con stato iniziale comune                              |
| Intersezione $L \cap L'$    | ✅        | $L \cap L' = \overline{\bar{L} \cup \bar{L}'}$             |
| Concatenazione $LL'$        | ✅        | NFA: connette stati finali di $M$ a stati iniziali di $M'$ |
| Iterazione $L^*$            | ✅        | NFA: da ogni stato finale torna allo stato iniziale        |
| Differenza $L \setminus L'$ | ✅        | $L \cap \bar{L}'$                                          |

---

### 9.3 Espressioni Regolari

**Sintassi**: $a$ (simbolo), $\varepsilon$, $\emptyset$, $(\alpha \cup \beta)$, $(\alpha \cdot \beta)$, $(\alpha)^*$.

**Semantica** (linguaggio associato $\langle \alpha \rangle$):
- $\langle a \rangle = \{a\}$, $\langle \varepsilon \rangle = \{\varepsilon\}$, $\langle \emptyset \rangle = \emptyset$
- $\langle \alpha \cup \beta \rangle = \langle \alpha \rangle \cup \langle \beta \rangle$
- $\langle \alpha \cdot \beta \rangle = \langle \alpha \rangle \cdot \langle \beta \rangle$
- $\langle \alpha^* \rangle = (\langle \alpha \rangle)^*$

**Precedenza**: $*$ > $\cdot$ > $\cup$

**Teorema di Kleene**: $L$ è regolare $\Leftrightarrow$ $\exists \alpha$ espressione regolare con $L = \langle \alpha \rangle$.

---

### 9.4 Come ricavare un'espressione regolare da un DFA

**Metodo pratico per esami**: analizza i percorsi da $q_1$ agli stati accettanti nel diagramma.

1. Identifica come si raggiunge ogni stato accettante.
2. Scrivi cosa legge l'automa lungo ogni percorso.
3. Combina con $\cup$ i vari percorsi.
4. Usa $*$ per i cappi (self-loop).

**Esempio tipico**: DFA con cappio su $a$ in $q_2$ e transizione $b$ da $q_2$ a $q_3$ (accettante): il linguaggio è $\langle a^+ b \rangle = \langle a \cdot a^* \cdot b \rangle$.

---

## 10. Pumping Lemma per Linguaggi Regolari

### 10.1 Enunciato (versione base)

> Sia $M$ un DFA con $n$ stati e $x \in L(M)$ con $|x| \geq n$. Allora esistono $u, v, w \in A^*$ con:
> 1. $x = uvw$
> 2. $v \neq \varepsilon$
> 3. $\forall i \in \mathbb{N}: uv^iw \in L(M)$

**Dimostrazione**: Per il principio della piccionaia, il percorso di accettazione di $x$ ($\geq n+1$ stati) ha almeno uno stato ripetuto → c'è un ciclo. $u$ porta a quel stato, $v$ è il ciclo, $w$ è il resto.

### 10.2 Versione rafforzata

Aggiunge: $|uv| \leq n$. Quindi $v$ deve stare nelle prime $n$ lettere di $x$.

---

### 10.3 Come usare il Pumping Lemma per dimostrare la non regolarità
$$
**Schema generale**:
$$
1. Supponi per assurdo che $L$ sia regolare, con un DFA di $p$ stati.
2. Scegli $x \in L$ con $|x| \geq p$ (solitamente $x = a^p b^p$ o simili).
3. Per ogni possibile decomposizione $x = uvw$ con $v \neq \varepsilon$ (e $|uv| \leq p$ se usi la versione rafforzata):
   - Mostra che $uv^iw \notin L$ per qualche $i$ (di solito $i=0$ o $i=2$).
4. Contraddizione con il Pumping Lemma.

**Attenzione**: deve funzionare per **ogni** decomposizione $uvw$, non per una sola!

---

### 10.4 Esempi canonici

**1. $L = \{a^n $b^n$: n \geq 0\}$ non è regolare.**
- Scegli $x = a^p b^p$.
- Qualunque $v$ con $|uv| \leq p$ è della forma $v = a^j$ con $j > 0$.
- $uv^0w = a^{p-j}b^p \notin L$.

**2. $L' = \{a^n b a^{2n}: n > 0\}$ non è regolare.**
- Scegli $x = a^p b a^{2p}$.
- $v = a^j$ ($j > 0$) nella parte sinistra: $uv^0w = a^{p-j}ba^{2p}$, ha $p-j \neq 2p-2j$ (salvo $j=0$). Dunque $\notin L'$.

**3. Alternativa: usare le proprietà di chiusura.**
- Se $L$ fosse regolare, allora $L \cap \langle a^* b^* \rangle$ sarebbe regolare (chiusura per intersezione). Ma $L \cap \langle a^* b^* \rangle = \{a^n b^n\}$ che non lo è.

---

## 11. Grammatiche Context-Free (CFG)

### 11.1 Definizione

Una **CFG** è una quadrupla $G = (V, \Sigma, R, S)$:
- $V$: variabili (non terminali)
- $\Sigma$: terminali (lettere)
- $S \in V$: assioma (variabile iniziale)
- $R \subseteq V \times (V \cup \Sigma)^*$: regole di produzione, scritte $X \to u$

**Derivazione elementare** ($w \Rightarrow_G w'$): si rimpiazza una variabile in $w$ con il suo corpo in una regola.

**Derivazione** ($w \Rightarrow_G^* w'$): sequenza di derivazioni elementari.

**Linguaggio generato**: $L(G) = \{w \in \Sigma^*: S \Rightarrow_G^* w\}$

---

### 11.2 Alberi di derivazione

Utili per visualizzare come si genera una parola. La radice è $S$, i figli di un nodo $X$ sono le lettere del corpo della regola applicata. Le foglie (lette da sinistra a destra) formano la parola generata.

---

### 11.3 Grammatiche Regolari

Una grammatica è **regolare** (o lineare destra) se le regole hanno forma:
$$X \to aY \quad \text{oppure} \quad X \to a \quad \text{oppure} \quad X \to \varepsilon$$
Ogni linguaggio regolare è generato da una grammatica regolare e viceversa.

---

### 11.4 Linguaggi CF ma non regolari

**Esempi fondamentali** da sapere:

- ${a^n $b^n$: n \geq 0}$: regola $S \to \varepsilon \mid aSb$
- $\{a^n $b^m$: m \leq n\}$: non regolare
- $\{a^n b^{2n}: n \geq 0\}$
- $\{ww^R: w \in \{a,b\}^*\}$ (palindromi pari)

---

### 11.5 Tecniche per scrivere grammatiche context-free

**Linguaggi con conteggio bilanciato** (tipo $a^n b^n$):
$$S \to \varepsilon \mid aSb$$
**Linguaggi con struttura ricorsiva** (tipo $(ab)^n a^{2n+1}$):
$$S \to a \mid abSaa$$
**Linguaggi con più "blocchi"** (tipo $\{a^i b^j a^k b^j a^\ell\}$):
Introduci variabili per ogni parte indipendente.
$$S \to A \cdot X \cdot A, \quad X \to bXb \mid \varepsilon \text{ (per le } b^j \text{ bilanciate)}$$
**Trucco**: separa le parti che si "accoppiano" e quelle libere. Una variabile per ogni livello di ricorsione indipendente.

---

### 11.6 Schema per descrivere il linguaggio di una CFG

1. Guarda cosa fa l'assioma: espansione diretta e ricorsione.
2. Prova a generare le prime parole: $\varepsilon$, una parola corta, poi vedi il pattern.
3. Formula un'ipotesi: $L(G) = \{\ldots\}$.
4. Se richiesto, verifica per induzione sulla lunghezza della derivazione.

---

# 🎯 Strategie per l'Esame

## Esercizi tipici Parte 1 (Calcolabilità)

### Tipo A: "Mostra che $f$ è ricorsiva primitiva"
1. Esprimi $f$ come **sommatoria/produttoria** di predicati ricorsivi primitivi, oppure
2. Dai la **ricorsione primitiva esplicita**: $f(x,0)=\ldots$;  $f(x,t+1)=g(x,t,f(x,t))$, poi verifica che $g$ sia r.p., oppure
3. Usa **minimalizzazione limitata** su un predicato r.p.

**Scheletro risposta**: "Possiamo definire $f(x) = \sum_{i=0}^{x} [\text{predicato r.p.}]$ che è r.p. per chiusura della sommatoria."

### Tipo B: "Mostra che $f$ è parzialmente calcolabile"
- **Metodo diretto**: scrivi un programma S (o pseudocodice) che la calcola.
- **Metodo indiretto**: esprimi $f$ come composizione di funzioni parzialmente calcolabili note (es. $\Phi$, STP, funzioni calcolabili).

**Schema tipo con STP/OR parallelo:**
```
[A] IF STP(X1, p, Z) GOTO B
    IF STP(X2, q, Z) GOTO C
    Z <-- Z+1
    GOTO A
[B] ...
[C] ...
```

### Tipo C: "Mostra che $f$ NON è calcolabile"
- Supponi per assurdo $f$ calcolabile.
- Costruisci un programma che userebbe $f$ per calcolare HALT o $f_K$ (funzione caratteristica di $K$).
- Contraddizione.

### Tipo D: "Mostra che $S$ è r.e."
- Opzione 1: $S = \{x: g(x)\downarrow\}$ per qualche $g$ parzialmente calcolabile esibita.
- Opzione 2: $S = \{h(n): n \in \mathbb{N}\}$ per qualche $h$ r.p. esibita.
- Opzione 3: Scrivi direttamente che $S = \{x: \exists t: \text{STP}(x, n, t)\}$ per qualche $n$.

### Tipo E: "Mostra che $S$ non è ricorsivo"
- Mostra che $f_S = \text{HALT}$ (o simile) → contraddizione.
- Oppure: $S$ r.e. ma $\bar{S}$ non lo è (usa il teorema sulla relazione ricorsività-r.e.).

---

## Esercizi tipici Parte 2 (Automi/Grammatiche)

### Tipo F: "Disegnare un DFA"
1. Identifica le condizioni da tracciare (contatori, flag booleane).
2. Ogni stato corrisponde a una "situazione" distinta.
3. Assicurati che $\delta$ sia **totale**: ogni stato deve avere una transizione per ogni simbolo (aggiungi uno stato pozzo se necessario).

### Tipo G: "Trovare un'espressione regolare"
1. Analizza il DFA (o descrizione del linguaggio).
2. Usa le operazioni $\cup$, $\cdot$, $^*$ in modo incrementale.
3. Controlla con qualche parola esempio.

### Tipo H: "Dimostrare che $L$ non è regolare"
- **Prima scelta**: Pumping Lemma. Scegli $x$ con molte $a$ (tipo $a^p b^p$).
- **Seconda scelta**: Proprietà di chiusura. Se $L$ fosse regolare, allora $L \cap \langle \text{linguaggio regolare} \rangle$ sarebbe regolare, ma equivale a $\{a^n b^n\}$ → assurdo.

### Tipo I: "Scrivere una CFG"
1. Individua la struttura del linguaggio (simmetria, annidamento, bilanciamento).
2. Introduci una variabile per ogni "livello" di ricorsione.
3. Scrivi le regole base (caso base) e ricorsive (passo).
4. Verifica con una derivazione di esempio.

---

# 📋 Formulario Rapido

## Pairing
$$\langle x,y \rangle = 2^x(2y+1)-1$$
$$l(\langle x,y \rangle)=x, \quad r(\langle x,y \rangle)=y$$
## Numeri di Gödel
$$[a_1,\ldots,a_k] = \prod_{i=1}^k P_i^{a_i}, \quad P_1=2,P_2=3,P_3=5,\ldots$$
$$(x)_i = \text{esponente di } P_i \text{ in } x$$
## Connessioni chiave
$$\text{HALT}(x,y) \Leftrightarrow x \in W_y \Leftrightarrow \Phi(x,y)\downarrow \Leftrightarrow \exists t: \text{STP}(x,y,t)$$
$$K = \{x: \text{HALT}(x,x)\} = \{x: x \in W_x\}$$
## Predicati r.p. importanti
- $x \leq y$, $x = y$, $x < y$ ✅
- $x | y$ (divisibilità) ✅
- $\text{Primo}(x)$ ✅
- $\text{STP}(x,y,t)$ ✅

## Linguaggi non regolari classici
- $\{a^n b^n\}$, $\{a^n b^{2n}\}$, $\{a^m $b^n$: m \leq n\}$
- Palindromi, $\{a^{p}: p \text{ primo}\}$

---

# 🔁 Esercizi d'Esame — Pattern Ricorrenti

## Dagli esafe.dellini@studenti.unina.itmi analizzati (2023-2026)

### Ricorsive Primitive — temi frequenti
- Somma di divisori con proprietà (pari/dispari/primi)
- Numero di cifre in base 10 ($l_{10}(x)$)
- Radici/arrotondamenti ($\lfloor \sqrt[k]{n} \rfloor$)
- Predicati su triangoli rettangoli (Pitagora)
- Il più piccolo numero con $n$ divisori (hint: $2^{n-1}$)
- $x \sqsubseteq y$ (y multiplo di tutti i fattori primi di x)

**Template risposta**: Definisci $f$ per ricorsione primitiva o tramite sommatorie/minimalizzazione limitata. Dimostri che ogni componente è r.p. Concludi per chiusura.

### Calcolabilità/Non calcolabilità — temi frequenti
- $g(x) = \ldots$ con condizione $x \in W_x$ o $x \notin W_y$ → usare STP parallelo
- Funzioni definite "se $\text{HALT}$" → parzialmente calcolabile con STP
- "Non può esistere $f$ calcolabile tale che $f(x) > 0 \Leftrightarrow \text{HALT}$..." → riduzione a HALT

### Insiemi r.e. — temi frequenti
- $\{x: \exists z: \text{STP}(\ldots)\}$ → r.e. per definizione
- $\{f(x): x \in \mathbb{N}\}$ con $f$ r.p. → r.e. per teorema di caratterizzazione
- $B' = \{f(x): x \in B\}$ con $B$ r.e. e $f$ calcolabile → r.e.
- $S \setminus F$ con $F$ finito e $S$ non ricorsivo → $S \setminus F$ non ricorsivo (riduzione: $f_S = f_{S\setminus F}$ su quasi tutti i punti)

---

> 💡 **Consiglio finale**: Negli esercizi di calcolabilità, la parola chiave è **STP**. Se devi costruire qualcosa di parzialmente calcolabile che dipende da HALT, usa il costrutto con STP incrementale (incrementa il contatore di step e controlla entrambe le condizioni in parallelo). Se devi mostrare che qualcosa non è calcolabile, riduci a HALT per assurdo.

---

# 🔧 Sezioni Aggiuntive (da esami recenti)

---

## A. Grammatica Regolare da DFA

Richiesto esplicitamente nell'esame ottobre 2024: *"Scrivere le regole di una grammatica **regolare** G tale che $L(G) = A^* \setminus L(M)$"*.

Una **grammatica regolare** (lineare destra) ha solo regole della forma:
$$X \to aY, \quad X \to a, \quad X \to \varepsilon$$
### Costruzione meccanica DFA → Grammatica Regolare

Dato un DFA $M = (Q, A, \delta, $q_1$, F)$:

1. **Ogni stato** $q_i$ diventa una variabile $Q_i$ (l'assioma è $Q_1$).
2. **Ogni transizione** $\delta($q_i$, a) = q_j$ diventa la regola $Q_i \to a Q_j$.
3. **Per ogni stato accettante** $q_i \in F$: aggiungi la regola $Q_i \to \varepsilon$.

> Il linguaggio generato è esattamente $L(M)$.

### Grammatica per il complemento $A^* \setminus L(M)$

Costruisci prima il DFA complemento $M'$ (scambia $F$ con $Q \setminus F$), poi applica la costruzione sopra.

**Esempio**: DFA con $Q = \{$q_0$, $q_1$, q_2\}$, $F = \{q_1\}$, transizioni $\delta($q_0$,a)=q_1$, $\delta($q_1$,b)=q_0$, $\delta($q_i$,\text{altro})=q_2$ (pozzo).

Per il complemento: $F' = \{$q_0$, q_2\}$. Grammatica:
- $Q_0 \to a Q_1 \mid \varepsilon$ (accettante)
- $Q_1 \to b Q_0$
- $Q_2 \to a Q_2 \mid b Q_2 \mid \varepsilon$ (accettante, pozzo)

---

## B. $L(M) \cup L(G)$ e $L(M) \cap L(G)$

Appare in febbraio 2024: *"Determinare i due linguaggi $L(M) \cup L(G)$ e $L(M) \cap L(G)$"*.
$$
**Fatti fondamentali da sapere**:
$$
| Operazione | Risultato |
$$
|---|---|
$$
| Regolare $\cup$ Regolare | Regolare |
| Regolare $\cap$ Regolare | Regolare |
| CF $\cup$ Regolare | CF |
| CF $\cap$ Regolare | CF |
| CF $\cup$ CF | CF |
| CF $\cap$ CF | **Non necessariamente CF** |

**Come si risponde nell'esame**:
1. Calcola $L(M)$ e $L(G)$ esplicitamente.
2. Determina $L(M) \cup L(G)$ descrivendo le stringhe che appartengono all'uno o all'altro.
3. Determina $L(M) \cap L(G)$ per intersezione diretta.
4. Se il risultato è regolare, esibisci un'espressione regolare o un DFA; se è CF, dai una grammatica.

**Nota**: Se $L(M)$ è regolare e $L(G)$ è CF, l'intersezione $L(M) \cap L(G)$ è sempre CF (e spesso è il linguaggio meno "libero" dei due).

---

## C. Schema STP Parallelo — Versione Completa

Il pattern più frequente negli esercizi sulle funzioni parzialmente calcolabili.

### Scenario 1: "se $x \in W_a$ oppure $x \in W_b$, allora $f(x)=0$, altrimenti $\uparrow$"

```
[A] IF STP(X, a, Z) GOTO E    ← termina se X ∈ W_a
    IF STP(X, b, Z) GOTO E    ← termina se X ∈ W_b
    Z <-- Z+1
    GOTO A
```
Termina sse $x \in W_a \cup W_b$. L'output di Y rimane 0.

### Scenario 2: "se $x \in W_a$ allora output 1, se $x \in W_b$ allora output 0, altrimenti $\uparrow$"

```
[A] IF STP(X, a, Z) GOTO B
    IF STP(X, b, Z) GOTO E    ← output 0 (Y resta 0)
    Z <-- Z+1
    GOTO A
[B] Y <-- Y+1                 ← output 1
```

### Scenario 3: "se $f(x)\downarrow$ e $f(x) \in B$ (con $B$ ricorsivo), allora output 0, altrimenti $\uparrow$"

```
[A] IF STP(X, p, Z) GOTO B    ← p = numero di programma per f
    Z <-- Z+1
    GOTO A
[B] W <-- Φ(X, p)             ← calcola f(x)
    IF f_B(W) != 0 GOTO E     ← controlla se f(x) ∈ B
    GOTO A                    ← se non ∈ B, continua a ciclare
```

### Scenario 4: "se $j \in W_k$ oppure $k \in W_j$, allora output 0, altrimenti $\uparrow$"
(Es. esame gennaio 2026: $g(\langle j,k \rangle) = 0$ se $j \in W_k \vee k \in W_j$)

```
Z1 <-- l(X)      ← estrai j
Z2 <-- r(X)      ← estrai k
[A] IF STP(Z1, Z2, Z) GOTO E   ← j ∈ W_k?
    IF STP(Z2, Z1, Z) GOTO E   ← k ∈ W_j?
    Z <-- Z+1
    GOTO A
```

> **Regola d'oro**: usa sempre STP con un contatore $Z$ che cresce, mai le funzioni parziali direttamente (altrimenti rischi loop infinito nel ramo sbagliato).

---

## D. Teoremi Negativi su Insiemi — Pattern "dimostrare o confutare"

### D1. $S \setminus F$ non è ricorsivo (con $S$ non ricorsivo, $F$ finito)

**Teorema**: Se $S$ non è ricorsivo e $F$ è finito, allora $S \setminus F$ non è ricorsivo.

**Dimostrazione**: Per assurdo, supponi $S \setminus F$ ricorsivo. Allora:
$$S = (S \setminus F) \cup (S \cap F)$$
$(S \cap F)$ è finito (sottoinsieme di $F$ finito) → ricorsivo primitivo.
$(S \setminus F)$ ricorsivo per ipotesi.
L'unione di due insiemi ricorsivi è ricorsiva → $S$ è ricorsivo. Contraddizione.

---

### D2. $B'$ non r.e. (con $B$ non r.e. e $f$ iniettiva calcolabile)

**Teorema**: Se $B$ non è r.e. e $f: \mathbb{N} \to \mathbb{N}$ è calcolabile e iniettiva, allora $B' = \{f(x): x \in B\}$ non è r.e.

**Dimostrazione**: Per assurdo, supponi $B'$ r.e., cioè $\exists g$ p.c. con $B' = \{z: g(z)\downarrow\}$.

Considera il programma:
```
Z <-- f(X)     ← calcola f(x)
Y <-- g(Z)     ← semi-decide B'
```
Questo programma termina sse $g(f(x))\downarrow$ sse $f(x) \in B'$ sse $x \in B$ (per iniettività di $f$).

Quindi $B = \{x: \Psi_P(x)\downarrow\}$ è r.e. Contraddizione.

---

### D3. $B = \{n: \forall t\, \neg\text{STP}(l(n),r(n),t)\}$ non è r.e.

**Analisi**: $B = \{n: \neg\text{HALT}(l(n), r(n))\} = \{\langle x,y\rangle: x \notin W_y\}$.

$\bar{B} = \{n: \text{HALT}(l(n),r(n))\} = \{\langle x,y\rangle: x \in W_y\}$ è r.e. (è $\{n: \Phi(l(n),r(n))\downarrow\}$).

Se $B$ fosse r.e., allora sia $B$ che $\bar{B}$ sarebbero r.e. → $B$ sarebbe ricorsivo → HALT sarebbe calcolabile. Contraddizione.

**Risposta**: $B$ **non** è r.e.

---

### D4. $C = \{x: \Phi(x,x)\downarrow \wedge \Phi(x,x) \in B\}$ è r.e. (con $B$ r.e.)

**Dimostrazione**: $B$ r.e. significa $B = W_n$ per qualche $n$, ovvero $\exists$ programma $P_n$ con $B = \{z: \Phi(z,n)\downarrow\}$.

Considera il programma:
```
Z <-- Φ(X, X)            ← calcola Φ(x,x), diverge se x ∉ K
Y <-- Φ(Z, n)            ← semi-decide se Z ∈ B
```
Termina sse $\Phi(x,x)\downarrow$ e $\Phi(x,x) \in B$, ovvero sse $x \in C$. Dunque $C$ è r.e.
$$
**Alternativa con STP**:
$$
$$C = \{x: \exists t_1, t_2: \text{STP}(x,x,t_1) \wedge \text{STP}(\Phi(x,x), n, t_2)\}$$
il che è r.e. per quantificazione esistenziale su un predicato r.p.

---

### D5. $f$ non calcolabile quando $f(x,y)>0 \Leftrightarrow \exists z: \text{STP}(x,y,z)$

(Esame giugno 2025)

**Dimostrazione**: $f(x,y)>0 \Leftrightarrow \text{HALT}(x,y)$. Se $f$ fosse calcolabile (totale), allora il predicato $f(x,y)>0$ sarebbe calcolabile, e quindi HALT sarebbe calcolabile. Contraddizione.

---

### D6. $\hat{f}$ non calcolabile anche se $f$ è parzialmente calcolabile

(Esame aprile 2024) Definizione: $\hat{f}(x) = f(x)+1$ se $f(x)\downarrow$, altrimenti $0$.

**Esempio**: Sia $h = \Phi^{(1)}(\cdot, \cdot)$ (funzione universale unaria), ovvero $h(x) = \Phi(x,x)$.

Allora:
$$\hat{h}(x) = \begin{cases} \Phi(x,x)+1 & x \in K \\ 0 & x \notin K \end{cases}$$
Se $\hat{h}$ fosse calcolabile, allora:
$$x \in K \Leftrightarrow \hat{h}(x) > 0$$
sarebbe un predicato calcolabile, ma $K$ non è ricorsivo. Contraddizione.

---

## E. Esercizi su Trovare $L_1 \subseteq L(G) \subseteq L_2$

### Pattern "L1, L2 regolari con $L_1 \subseteq L(G) \subseteq L_2$"

Richiesto spesso come esercizio 3 della parte automi.
$$
**Strategia**:
$$
- $L_2$ = versione "allargata" regolare di $L(G)$: rimuovi un vincolo. Es. se $L(G) = \{a^m b (ab)^n: m \leq n\}$, prendi $L_2 = \langle a^+ b (ab)^* \rangle$.
- $L_1$ = sottoinsieme regolare finito o con vincolo fisso. Es. $L_1 = \{ab(ab)\} = $ un singleton.

**Regola pratica**: $L_1$ può essere qualsiasi sottoinsieme finito non vuoto di $L(G)$ (è sempre regolare). $L_2$ si ottiene "dimenticando" il vincolo di uguaglianza tra esponenti.

### Pattern "L1, L2 CF non regolari con $L_1, L_2 \subsetneq L(G)$"

(Esame luglio 2024: trovare due CF non regolari inclusi in $L(G)$)

**Strategia**: Individua due sottolinguaggi di $L(G)$ che hanno struttura "bilanciata" diversa.

**Esempio**: Se $L(G) = \{a^n b^{i_1}c^{i_1}\cdots b^{i_n}c^{i_n}: n,i_j>0\}$, allora:
- $L_1 = \{ab^i $c^i$: i>0\} = $ il caso $n=1$, non regolare
- $L_2 = \{a^2 b^i c^i b^j $c^j$: i,j>0\}$ = il caso $n=2$, non regolare

---

## F. $T_R = \{x: \exists t: R(x,t)\}$ è r.e. (con $R$ predicato r.p. binario)

