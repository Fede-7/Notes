# 🎓 Appunti Ripasso Orale — Informatica Teorica
> Prof. A. De Luca | Federico II Napoli
> Tags: #informatica-teorica #orale #ripasso

---

# 📋 Argomenti da preparare per l'orale

1. Ricorsione Primitiva — definizione e teorema
2. Insiemi Ricorsivi e R.E. — chiusure e relazioni
3. Codifica — Numeri di Gödel e Pairing
4. Automi DFA/NFA — definizioni ed equivalenza
5. Linguaggi Regolari — chiusure e Pumping Lemma
6. Funzione Universale, HALT, STP
7. Teorema di Kleene
8. Pumping Lemma Context-Free
9. PDA e Linguaggi Context-Free

---

# 1. RICORSIONE PRIMITIVA

## Definizione generale (k-aria)

Una funzione $h$ $(n)$-aria si ricava per **ricorsione primitiva** da $f$ $(n-1)$-aria e $g$ $(n+1)$-aria se:

$$h(x_1,\ldots,x_{n-1}, 0) = f(x_1,\ldots,x_{n-1})$$
$$h(x_1,\ldots,x_{n-1}, t+1) = g(x_1,\ldots,x_{n-1}, t, h(x_1,\ldots,x_{n-1},t))$$

> Caso base + passo ricorsivo — come la ricorsione in programmazione.

## Caso unario (il più semplice)

$$h(0) = k \quad \text{(costante)}$$
$$h(t+1) = g(t, h(t))$$

## Teorema di Ricorsione Primitiva

**Enunciato**: Se $f$ e $g$ sono calcolabili, allora $h$ ricavata per ricorsione primitiva è calcolabile.

**Dimostrazione** (programma S):
```
Y <-- f(X1,...,Xn-1)
[A] IF Xn == 0 GOTO E
    Y <-- g(X1,...,Xn-1, Y, Z)
    Z <-- Z+1
    Xn <-- Xn-1
    GOTO A
```

> **Come dirlo all'orale**: "Il programma calcola il caso base con $f$, poi itera $g$ un numero di volte pari all'ultimo argomento, usando un contatore $Z$ per tenere traccia del passo corrente."

## Classi PRC

Un insieme $\mathcal{C}$ è **PRC** se:
- Contiene $n(x)=0$, $s(x)=x+1$, $u_i^{(n)}(x_1,\ldots,x_n)=x_i$
- È chiuso per composizione e ricorsione primitiva

Le funzioni **ricorsive primitive** sono la più piccola classe PRC.

---

# 2. INSIEMI RICORSIVI E R.E.

## Definizioni

| Tipo | Definizione | Intuizione |
|---|---|---|
| **Ricorsivo** | $f_S$ calcolabile | posso decidere sempre |
| **R.P.** | $f_S$ ricorsiva primitiva | decido senza loop |
| **R.E.** | $\exists g$ p.c.: $S=\{x:g(x)\downarrow\}$ | posso confermare ma non negare |

## Proprietà di chiusura

### Insiemi ricorsivi
Chiusi per: $\cup$, $\cap$, complemento $\bar{S}$

**Dimostrazione** (unione):
$$f_{S\cup T}(x) = f_S(x) \vee f_T(x)$$
Composizione di calcolabili → calcolabile ✅

### Insiemi R.E.
Chiusi per: $\cup$, $\cap$ — **NON** per complemento

**Dimostrazione intersezione R.E.**:
```
Z <-- g(X)    ← semi-decide S
Z <-- h(X)    ← semi-decide T
```
Termina sse $g(x)\downarrow$ e $h(x)\downarrow$ ✅

**Dimostrazione unione R.E.** (STP parallelo):
```
[A] IF STP(X,p,Z) GOTO E
    IF STP(X,q,Z) GOTO E
    Z <-- Z+1
    GOTO A
```

## Teorema fondamentale

$$S \text{ ricorsivo} \Leftrightarrow S \text{ r.e.} \wedge \bar{S} \text{ r.e.}$$

**Come dirlo all'orale**: "Un insieme è ricorsivo se e solo se sia lui che il suo complemento sono r.e. — perché se puoi semi-decidere entrambi, puoi aspettare quale dei due termina prima e quindi decidere sempre."

**Dimostrazione** (⟸): Siano $S=W_p$ e $\bar{S}=W_q$. Il programma:
```
[A] IF STP(X,p,Z) GOTO B
    IF STP(X,q,Z) GOTO E
    Z <-- Z+1
    GOTO A
[B] Y <-- Y+1
```
termina sempre perché $S \cup \bar{S} = \mathbb{N}$ ✅

## Insieme Diagonale K

$$K = \{x : \Phi(x,x)\downarrow\} = \{x: x \in W_x\}$$

**K è r.e.** — $K = \{x: \exists t: \text{STP}(x,x,t)\}$ ✅

**$\bar{K}$ NON è r.e.** — dimostrazione:
- Se $\bar{K}$ r.e. → $\bar{K} = W_i$ per qualche $i$
- Allora $i \in \bar{K} \Leftrightarrow i \in W_i \Leftrightarrow i \in K$ — contraddizione ✅

## Teorema di caratterizzazione R.E.

Per $S \neq \emptyset$, equivalenti:
1. $S = \{x: g(x)\downarrow\}$ con $g$ p.c.
2. $S = \{f(n): n \in \mathbb{N}\}$ con $f$ r.p.
3. $S = \{x: \exists t: R(x,t)\}$ con $R$ r.p.
4. $S = \{f(n): f(n)\downarrow\}$ con $f$ p.c.

---

# 3. CODIFICA — NUMERI DI GÖDEL E PAIRING

## Funzione di Pairing

$$\langle x,y \rangle = 2^x(2y+1) - 1$$

**Proprietà**:
- Biettiva (ogni coppia → un numero, ogni numero → una coppia)
- Ricorsiva primitiva

**Inverse** (r.p. per minimalizzazione limitata):
- $l(z)$ = esponente della maggior potenza di 2 che divide $z+1$
- $r(z)$ = l'altro fattore

**Come calcolare**: $z+1 = 2^{l(z)} \cdot (2r(z)+1)$

## Numeri di Gödel

$$[a_1,\ldots,a_k] = \prod_{i=1}^k P_i^{a_i} = 2^{a_1} \cdot 3^{a_2} \cdot 5^{a_3} \cdots$$

**Proprietà**:
- NON biettiva (non surgettiva: 0 non è in immagine; non iniettiva: aggiungere 0 non cambia)
- Per il TFA: la sequenza è univoca a meno di zeri finali

**Inverse**:
- $(x)_i$ = esponente di $P_i$ nella fattorizzazione di $x$
- $Lt(x)$ = indice del massimo primo che divide $x$

**Perché si usano**: per codificare programmi, istruzioni e stati come numeri naturali, permettendo alla funzione universale di operare su di essi.

## Codifica delle istruzioni

$$\#(I) = \langle a, \langle b, c \rangle \rangle$$

- $a$ = etichetta (0 se assente)
- $b$ = tipo (0=pigra, 1=incr, 2=decr, $n+2$=salto a etichetta $n$)
- $c$ = numero variabile $-1$

## Codifica di un programma

$$\#(P) = [\#(I_1), \ldots, \#(I_k)]_k - 1$$

La $-1$ garantisce la surgettività (ogni naturale codifica un programma).

---

# 4. AUTOMI DFA E NFA

## DFA — Automa Finito Deterministico

**Quintupla** $(Q, A, \delta, q_1, F)$:
- $Q$ = stati, $A$ = alfabeto, $\delta: Q \times A \to Q$
- $q_1$ = stato iniziale, $F$ = stati accettanti

**Funzione iterata**:
$$\delta^*(q, \varepsilon) = q, \quad \delta^*(q, wa) = \delta(\delta^*(q,w), a)$$

**Linguaggio accettato**: $L(M) = \{w: \delta^*(q_1,w) \in F\}$

## NFA — Automa Finito Non Deterministico

**Differenza**: $\delta: Q \times A \to \mathcal{P}(Q)$ (insieme di stati, non uno solo)

$$\delta^*(q,wa) = \bigcup_{q' \in \delta^*(q,w)} \delta(q',a)$$

Accetta se $\delta^*(q_1,w) \cap F \neq \emptyset$

## Equivalenza DFA ↔ NFA

**Teorema**: $L$ regolare $\Leftrightarrow$ $L = L(M)$ per qualche NFA $M$

**Costruzione** NFA → DFA (sottoinsiemi):
- Stati del DFA = sottoinsiemi di $Q$
- Stato iniziale = $\{q_1\}$
- $\delta'(Q', a) = \bigcup_{q \in Q'} \delta(q,a)$
- $F' = \{Q' \subseteq Q: Q' \cap F \neq \emptyset\}$

**Come dirlo all'orale**: "Il DFA tiene traccia di tutti gli stati in cui l'NFA potrebbe trovarsi — ogni sottoinsieme di stati diventa uno stato del DFA."

## DFA Non-Restarting

DFA dove $q_1 \notin \delta(Q \times A)$ — non si torna mai allo stato iniziale.

**Utilità**: semplifica le dimostrazioni di chiusura (unione, concatenazione, iterazione).

---

# 5. LINGUAGGI REGOLARI — CHIUSURE E PUMPING LEMMA

## Chiusura dei linguaggi regolari

| Operazione | Chiusura | Tecnica |
|---|---|---|
| Complemento | ✅ | Scambia $F$ e $Q\setminus F$ |
| Unione | ✅ | NFA con stato iniziale comune |
| Intersezione | ✅ | $L \cap L' = \overline{\bar{L} \cup \bar{L}'}$ |
| Concatenazione | ✅ | NFA: connette stati finali di $M$ a $M'$ |
| Iterazione $L^*$ | ✅ | NFA: da stati finali torna all'iniziale |

### Dimostrazione Regolarità dell'Unione

Siano $M=(Q,A,\delta,q_1,F)$ e $M'=(Q',A,\delta',q_1',F')$ DFA non-restarting con $Q \cap Q' = \emptyset$.

Costruisci NFA $\hat{M} = (Q \cup Q' \setminus \{q_1,q_1'\} \cup \{q_0\}, A, \hat{\delta}, q_0, \hat{F})$ con:

$$\hat{\delta}(q_0, a) = \{\delta(q_1,a), \delta'(q_1',a)\}$$

**Intuizione**: $q_0$ simula entrambi gli automi in parallelo — va dove andrebbero entrambi gli stati iniziali.

## Pumping Lemma per linguaggi regolari

**Enunciato**: Sia $M$ DFA con $n$ stati, $x \in L(M)$ con $|x| \geq n$. Allora $\exists u,v,w$:
1. $x = uvw$
2. $v \neq \varepsilon$
3. $\forall i \geq 0: uv^iw \in L(M)$
4. (versione rafforzata) $|uv| \leq n$

**Intuizione**: $n+1$ stati visitati con $n$ stati disponibili → piccionaia → ciclo → puoi pompare.

**Schema per dimostrare NON regolarità**:
1. Supponi $L$ regolare con $p$ stati
2. Scegli $x \in L$ con $|x| \geq p$
3. Per ogni decomposizione $uvw$ con $v \neq \varepsilon$ (e $|uv| \leq p$):
4. Trova $i$ tale che $uv^iw \notin L$
5. Contraddizione

**Alternativa — proprietà di chiusura**:
> "Se $L$ fosse regolare, allora $L \cap \langle\text{regex}\rangle$ sarebbe regolare. Ma quella intersezione è $\{a^nb^n\}$ → contraddizione."

---

# 6. FUNZIONE UNIVERSALE, HALT, STP

## Funzione Universale

$$\Phi^{(n)}(x_1,\ldots,x_n, y) = \Psi_{P_y}^{(n)}(x_1,\ldots,x_n)$$

"Esegui il programma numero $y$ su input $(x_1,\ldots,x_n)$"

**Teorema di Universalità**: $\Phi^{(n)}$ è parzialmente calcolabile per ogni $n$.

**Come dirlo all'orale**: "La funzione universale simula qualsiasi programma dato il suo numero. Il programma universale usa la codifica per interpretare le istruzioni ed aggiornare lo stato."

## Problema della Fermata

$$\text{HALT}(x,y) \Leftrightarrow \Psi_{P_y}^{(1)}(x)\downarrow$$

**HALT non è calcolabile** — dimostrazione per assurdo:
```
[A] IF HALT(X,X) GOTO A
```
Sia $y_0$ il numero di questo programma. Allora:
$$\text{HALT}(y_0,y_0) \Leftrightarrow \neg\text{HALT}(y_0,y_0) \quad \text{Assurdo!}$$

## Predicato STP

$$\text{STP}(x,y,t) \Leftrightarrow \text{il programma } P_y \text{ su input } x \text{ termina in } \leq t \text{ passi}$$

**STP è ricorsivo primitivo** ✅

**Connessioni chiave**:
$$\text{HALT}(x,y) \Leftrightarrow x \in W_y \Leftrightarrow \Phi(x,y)\downarrow \Leftrightarrow \exists t: \text{STP}(x,y,t)$$

---

# 7. TEOREMA DI KLEENE

**Enunciato**: $L \subseteq A^*$ è regolare $\Leftrightarrow$ è finito oppure ottenuto da linguaggi finiti mediante un numero finito di $\cup$, $\cdot$, $^*$.

## Dimostrazione (⟸)

Dato DFA $M=(Q,A,\delta,q_1,F)$ con $Q=\{q_1,\ldots,q_n\}$, definisci:

$$R_{i,j}^{(k)} = \{w \in A^* : \delta^*(q_i,w)=q_j \text{ e percorso usa solo stati } q_1,\ldots,q_k\}$$

**Tre osservazioni fondamentali**:

**Base** ($k=0$):
$$R_{i,i}^{(0)} = \{\varepsilon\} \cup \{a \in A: \delta(q_i,a)=q_i\} \quad \text{(finito)}$$
$$R_{i,j}^{(0)} = \{a \in A: \delta(q_i,a)=q_j\} \quad i\neq j \quad \text{(finito)}$$

**Passo ricorsivo**:
$$R_{i,j}^{(k+1)} = R_{i,j}^{(k)} \cup R_{i,k+1}^{(k)} \cdot (R_{k+1,k+1}^{(k)})^* \cdot R_{k+1,j}^{(k)}$$

**Intuizione del passo**: Le parole che vanno da $q_i$ a $q_j$ usando stati fino a $q_{k+1}$ sono di due tipi: quelle che ignorano $q_{k+1}$ e quelle che ci passano almeno una volta.

**Conclusione**:
$$L(M) = \bigcup_{q_j \in F} R_{1,j}^{(n)}$$

Per induzione su $k$, ogni $R_{i,j}^{(k)}$ è ottenuto da linguaggi finiti con $\cup$, $\cdot$, $^*$ → regolare ✅

**Come dirlo all'orale**: "Costruiamo il linguaggio pezzo per pezzo. Prima solo transizioni dirette (insieme finito), poi aggiungiamo stati intermedi uno alla volta. Ogni aggiunta usa unione, concatenazione e star — alla fine otteniamo un'espressione regolare per tutto il linguaggio."

---

# 8. PUMPING LEMMA CONTEXT-FREE

## Enunciato

$L$ context-free $\Rightarrow \exists p \geq 0: \forall x \in L, |x| \geq p \Rightarrow \exists u,v,w,y,z$:
1. $x = uvwyz$
2. $vy \neq \varepsilon$
3. $\forall i \geq 0: uv^iwy^iz \in L$
4. $|vwy| \leq p$

## Intuizione della dimostrazione

**Passo 1 — FNC**: Trasforma la grammatica in Forma Normale di Chomsky → albero binario (ogni nodo ha esattamente 2 figli).

**Passo 2 — Albero alto**: Se $|x| \geq p = 2^{k+1}$, l'albero ha altezza $\geq k+1$.

**Passo 3 — Piccionaia**: Il percorso radice-foglia ha $\geq k+1$ variabili, ma la grammatica ne ha solo $k$ → una variabile $T$ si ripete.

**Passo 4 — I 5 pezzi**:
```
parola x:
┌─────┬──────┬──────┬──────┬─────┐
│  u  │  v   │  w   │  y   │  z  │
└─────┴──────┴──────┴──────┴─────┘
      ↑       ↑     ↑       ↑
   inizio  inizio  fine   fine
     T1      T2    T2      T1
```

- $u$ = prima di $T_1$
- $v$ = bordo sinistro di $T_1$ intorno a $T_2$
- $w$ = dentro $T_2$
- $y$ = bordo destro di $T_1$ intorno a $T_2$
- $z$ = dopo $T_1$

**Passo 5 — Pompaggio**: Siccome $T$ genera $vTy$, puoi innestare quante copie vuoi → $uv^iwy^iz \in L$ ✅

## Differenza con il pumping regolare

| | Regolare | Context-Free |
|---|---|---|
| Struttura | percorso lineare | albero |
| Ciclo | stato ripetuto | variabile ripetuta |
| Pezzi | 3 ($uvw$) | 5 ($uvwyz$) |
| Si pompano | solo $v$ | $v$ e $y$ insieme |
| Condizione | $|uv| \leq p$ | $|vwy| \leq p$ |

## Come dimostrare NON CF

Stesso schema del pumping regolare, ma con 5 pezzi:

**Esempio** — $\{a^nb^nc^n\}$ non è CF:

Scegli $x = a^pb^pc^p$. Siccome $|vwy| \leq p$, $vwy$ non può contenere sia $a$ che $c$ (troppo distanti). Pompando, il numero di una lettera cambia ma non delle altre → esce dal linguaggio.

---

# 9. PDA — AUTOMI A PILA

## Definizione

Un **PDA** (Pushdown Automaton) è una sestupla $(Q, \Sigma, \Gamma, \delta, q_0, F)$:
- $Q$ = stati
- $\Sigma$ = alfabeto di input
- $\Gamma$ = alfabeto della pila
- $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \times \Gamma \to \mathcal{P}(Q \times \Gamma^*)$ = funzione di transizione
- $q_0$ = stato iniziale
- $F$ = stati accettanti

## Teorema fondamentale

$$L \text{ context-free} \Leftrightarrow L = L(M) \text{ per qualche PDA } M$$

**Intuizione**: La pila permette di "ricordare" un numero arbitrario di simboli → può bilanciare $a^n$ con $b^n$ che un DFA non può fare.

## Differenza con DFA/NFA

| | DFA/NFA | PDA |
|---|---|---|
| Memoria | finita (stati) | pila (infinita) |
| Linguaggi | Regolari | Context-Free |
| Esempio accettato | $a^*b^*$ | $\{a^nb^n\}$ |
| Esempio NON accettato | $\{a^nb^n\}$ | $\{a^nb^nc^n\}$ |

---

# 🎯 Come prepararsi all'orale

## Le domande più probabili

1. "Definisca la ricorsione primitiva nella forma più generale"
2. "Dimostri che se $S$ e $\bar{S}$ sono r.e. allora $S$ è ricorsivo"
3. "Cos'è la funzione universale e perché è calcolabile?"
4. "Dimostri la regolarità dell'unione"
5. "Enunci e spieghi il Pumping Lemma per linguaggi regolari"
6. "Qual è la differenza tra Pumping Lemma regolare e CF?"
7. "Perché HALT non è calcolabile?"
8. "Cos'è $K$ e perché $\bar{K}$ non è r.e.?"

## Come rispondere

Per ogni argomento segui questo schema:

1. **Enunciato** — di cosa si tratta in una frase
2. **Intuizione** — perché ha senso, esempio semplice
3. **Definizione formale** — la formula o la struttura
4. **Dimostrazione** — se richiesta, passo per passo
5. **Esempio** — concreto e breve

## Frasi utili per l'orale

- "Per il principio della piccionaia..."
- "Per la Tesi di Church-Turing..."
- "Per il Teorema di Kleene, esiste un'espressione regolare equivalente..."
- "Supponiamo per assurdo che... allora potremmo calcolare HALT... contraddizione."
- "Siccome $B$ è ricorsivo, la sua funzione caratteristica $f_B$ è calcolabile..."
- "Uso STP in parallelo per evitare di bloccarmi su una funzione che potrebbe divergere..."
