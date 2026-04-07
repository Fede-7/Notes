---
date: 2026-03-26
corso: Modelli Statistici e Probabilità
docente: N/D
lezione: Canale binario simmetrico, entropia e PMF condizionale — esercizi
tags:
  - canale-binario
  - entropia
  - informazione
  - PMF-condizionale
  - Bayes
  - esercizi
  - MSI
---

# Lezione 7: Canale Binario Simmetrico, Entropia e Esercizi su PMF Congiunta

**Corso:** Modelli Statistici e Probabilità

---

## Argomenti trattati

- Canale binario simmetrico: modello, probabilità di errore, legge di Bayes
- Caso peggiore del canale: $\varepsilon = 1/2$
- Introduzione all'entropia e al concetto di informazione (Claude Shannon)
- PMF condizionale e proprietà di marginalizzazione come media
- Regola della catena per tre variabili aleatorie
- Indipendenza condizionale e catene di Markov (cenni)
- Esercizi: urna con due estrazioni, dado onesto e dado truccato

---

## 1. Canale binario simmetrico (BSC)

### Modello

Un **canale di comunicazione** trasferisce un bit $X$ (input) a una destinazione come bit $Y$ (output). Il canale introduce errori con probabilità $\varepsilon$: con probabilità $1-\varepsilon$ il bit è ricevuto correttamente, con probabilità $\varepsilon$ è invertito.

Il canale è detto **simmetrico** perché il comportamento è identico per $X=0$ e $X=1$:

$$p_{Y|X}(0|0) = p_{Y|X}(1|1) = 1 - \varepsilon$$
$$p_{Y|X}(1|0) = p_{Y|X}(0|1) = \varepsilon$$

```
         1-ε
    0 ────────→ 0
    │      ε   ↗
    └──────────
         ε    ↗
    1 ────────→ 1
         1-ε
```

### Probabilità di errore

Sia $P(X=1) = p$, quindi $P(X=0) = 1-p$.

Per la legge della probabilità totale:

$$P(\text{errore}) = P(Y \neq X) = P(Y \neq X | X=0) \cdot P(X=0) + P(Y \neq X | X=1) \cdot P(X=1)$$

$$= \varepsilon (1-p) + \varepsilon p = \varepsilon$$

> [!abstract] Risultato: probabilità di errore nel BSC
> In un canale binario simmetrico, la probabilità di errore è esattamente $\varepsilon$, indipendentemente dalla distribuzione dell'input. Il parametro $\varepsilon$ è la **frazione di bit trasferiti incorrettamente**.

### Inferenza: qual è il bit trasmesso?

Data $Y=0$, qual è la probabilità che $X=0$? (Legge di Bayes)

$$P(X=0|Y=0) = \frac{P(Y=0|X=0) \cdot P(X=0)}{P(Y=0)}$$

Il denominatore si calcola con la legge della probabilità totale:

$$P(Y=0) = P(Y=0|X=0) \cdot P(X=0) + P(Y=0|X=1) \cdot P(X=1) = (1-\varepsilon)(1-p) + \varepsilon p$$

Quindi:

$$P(X=0|Y=0) = \frac{(1-\varepsilon)(1-p)}{(1-\varepsilon)(1-p) + \varepsilon p}$$

### Il caso peggiore: $\varepsilon = 1/2$

Potrebbe sembrare che il caso peggiore sia $\varepsilon = 1$ (tutti i bit invertiti). Ma se $\varepsilon = 1$, il canale è ancora determinisitco: basta invertire il bit ricevuto.

Il caso peggiore è quando **osservare l'uscita non dà informazioni sull'ingresso**, cioè quando la probabilità a posteriori è uguale a quella a priori:

$$P(X=0|Y=0) = P(X=0)$$

Questo accade quando $\varepsilon = 1/2$: il canale produce rumore puro, e $Y$ è completamente indipendente da $X$.

> [!abstract] Definizione: caso peggiore del BSC
> Il caso peggiore per il canale binario simmetrico è $\varepsilon = 1/2$: osservare l'uscita non fornisce alcuna informazione sull'ingresso.

---

## 2. Entropia e informazione (introduzione)

### Misura dell'informazione

L'informazione ricevuta quando si osserva un evento $A$ di probabilità $P(A)$ deve soddisfare tre proprietà di senso comune:

1. **Non negativa**: $I(A) \geq 0$ (non si mente).
2. **Decrescente nella probabilità**: più raro l'evento, più informazione porta.
3. **Additiva per eventi indipendenti**: $I(A \cap B) = I(A) + I(B)$ se $A \perp B$.

L'unica funzione che soddisfa tutte e tre è:

$$I(A) = \log_2 \frac{1}{P(A)} = -\log_2 P(A)$$

La base 2 fa sì che l'unità sia il **bit** (unità di misura dell'informazione).

> [!example] Casi limite
> - Evento certo ($P(A) = 1$): $I(A) = \log_2 1 = 0$ (nessuna informazione: "il Sole sorgerà domani").
> - Evento impossibile ($P(A) = 0$): $I(A) \to \infty$ (informazione infinita: "il Sole non sorgerà domani").

### Entropia di una variabile aleatoria

Dato che la quantità di informazione $I(X = x) = \log_2 \frac{1}{p_X(x)}$ è essa stessa una variabile aleatoria, si definisce l'**entropia** come la sua media statistica:

> [!abstract] Definizione: Entropia
> L'entropia di una variabile aleatoria discreta $X$ con PMF $p_X$ è:
> $$H(X) = E\left[\log_2 \frac{1}{p_X(X)}\right] = \sum_{x \in \mathcal{X}} p_X(x) \log_2 \frac{1}{p_X(x)}$$
> Si misura in **bit**.

### Entropia di una variabile Bernoulliana

Per $X \in \{0,1\}$ con $P(X=1) = p$:

$$H(X) = p \log_2 \frac{1}{p} + (1-p) \log_2 \frac{1}{1-p}$$

Proprietà: $0 \leq H(X) \leq 1$, con $H(X) = 1$ se e solo se $p = 1/2$.

> [!important] Implicazione per i file compressi
> Una variabile Bernoulliana porta al più 1 bit di informazione, e esattamente 1 bit solo quando $p = 1/2$ (i due valori sono equiprobabili). Un file compresso idealmente è una sequenza binaria in cui 0 e 1 sono equiprobabili e statisticamente indipendenti: questa è la condizione di massima complessità informazionale.

### Entropia di una variabile quaternaria uniforme

Per $X \in \{1,2,3,4\}$ con $p_X(x) = 1/4$ per ogni $x$:

$$H(X) = 4 \cdot \frac{1}{4} \log_2 4 = \log_2 4 = 2 \text{ bit}$$

Una variabile quaternaria equiprobabile porta 2 bit di informazione, coerentemente con il fatto che 4 valori si codificano con 2 bit binari.

> [!quote]
> "Una variabile bistabile trasporta una quantità di informazione che è al più un bit."

---

## 3. PMF condizionale e marginalizzazione come media

### Ricapitolo

La PMF condizionale di $X$ dato $Y$ è:

$$p_{X|Y}(x|y) = \frac{p_{XY}(x,y)}{p_Y(y)}$$

Per ogni $y$ fissato, è una legge di probabilità su $\mathcal{X}$.

### Marginalizzazione come media

Riscrivendo la proprietà di marginalizzazione:

$$p_X(x) = \sum_y p_{XY}(x,y) = \sum_y p_{X|Y}(x|y) \cdot p_Y(y) = E_Y[p_{X|Y}(x|Y)]$$

Cioè: **la PMF marginale di $X$ è la media (rispetto a $Y$) della PMF condizionale di $X$ dato $Y$**. Questo offre un modo alternativo di calcolare le marginali, utile quando la struttura condizionale è più facile da specificare rispetto a quella congiunta.

---

## 4. Regola della catena

Per tre variabili aleatorie $X$, $Y$, $Z$:

$$p_{XYZ}(x,y,z) = p_Z(z) \cdot p_{Y|Z}(y|z) \cdot p_{X|YZ}(x|y,z)$$

e tutte le permutazioni degli indici sono valide.

> [!example] Uso nell'esercizio del dado
> Nell'esercizio con dado onesto e dado truccato si è usata la legge della catena:
> $$P(X_1=6, X_2=6 | \text{onesto}) = P(X_1=6|\text{onesto}) \cdot P(X_2=6|X_1=6, \text{onesto})$$
> Dove il secondo fattore vale $1/6$ (stesso dado, $X_1=6$ è pari → non si cambia dado).

---

## 5. Indipendenza condizionale e catene di Markov (cenni)

> [!abstract] Definizione: Indipendenza condizionale
> $X_1$ e $X_3$ sono **condizionalmente indipendenti dato $X_2$** se:
> $$p_{X_1 X_3 | X_2}(x_1, x_3 | x_2) = p_{X_1|X_2}(x_1|x_2) \cdot p_{X_3|X_2}(x_3|x_2)$$

Questo è diverso dall'indipendenza (marginale): $X_1$ e $X_3$ possono essere dipendenti, ma diventano indipendenti una volta noto $X_2$.

> [!example] Mosse del re su una scacchiera
> La posizione del re alla mossa 1 ($X_1$) e alla mossa 3 ($X_3$) sono dipendenti: se il re è in un angolo al tempo 1, non può essere lontano al tempo 3. Tuttavia, nota la posizione al tempo 2 ($X_2$), la posizione al tempo 3 dipende solo da $X_2$ e non più da $X_1$. Quindi $X_1$ e $X_3$ sono condizionalmente indipendenti dato $X_2$.

Quando vale questa proprietà, la terna $(X_1, X_2, X_3)$ è detta **catena di Markov**. Questa struttura è alla base della teoria delle code e dei processi stocastici in generale.

---

## 6. Esercizio: urna con due estrazioni senza reinserimento

**Setup**: urna con 6 palline — 1 marcata "1", 2 marcate "2", 3 marcate "3". Due estrazioni senza reinserimento. $X_1$ = risultato prima estrazione, $X_2$ = risultato seconda estrazione.

### PMF marginale di $X_1$

$$p_{X_1}(1) = \frac{1}{6}, \quad p_{X_1}(2) = \frac{2}{6} = \frac{1}{3}, \quad p_{X_1}(3) = \frac{3}{6} = \frac{1}{2}$$

### PMF congiunta

Si usa la regola della probabilità composta: $p_{X_1 X_2}(x_1, x_2) = p_{X_1}(x_1) \cdot p_{X_2|X_1}(x_2|x_1)$.

Le probabilità condizionali $p_{X_2|X_1}(x_2|x_1)$ si calcolano ricordando che si lavora **senza reinserimento**: estratta $x_1$, rimangono 5 palline.

| | $X_2=1$ | $X_2=2$ | $X_2=3$ |
|---|---|---|---|
| $X_1=1$ | 0 | $\frac{1}{6} \cdot \frac{2}{5} = \frac{1}{15}$ | $\frac{1}{6} \cdot \frac{3}{5} = \frac{1}{10}$ |
| $X_1=2$ | $\frac{1}{3} \cdot \frac{1}{5} = \frac{1}{15}$ | $\frac{1}{3} \cdot \frac{1}{5} = \frac{1}{15}$ | $\frac{1}{3} \cdot \frac{3}{5} = \frac{1}{5}$ |
| $X_1=3$ | $\frac{1}{2} \cdot \frac{1}{5} = \frac{1}{10}$ | $\frac{1}{2} \cdot \frac{2}{5} = \frac{1}{5}$ | $\frac{1}{2} \cdot \frac{2}{5} = \frac{1}{5}$ |

> [!example] Verifica della somma
> $0 + \frac{1}{15} + \frac{1}{10} + \frac{1}{15} + \frac{1}{15} + \frac{1}{5} + \frac{1}{10} + \frac{1}{5} + \frac{1}{5} = 1$ ✓

### PMF condizionale $p_{X_2|X_1}$

Organizzata per righe (condizionamento = valore di $X_1$):

| | $X_2=1$ | $X_2=2$ | $X_2=3$ | Somma |
|---|---|---|---|---|
| $X_1=1$ | 0 | $2/5$ | $3/5$ | 1 ✓ |
| $X_1=2$ | $1/5$ | $1/5$ | $3/5$ | 1 ✓ |
| $X_1=3$ | $1/5$ | $2/5$ | $2/5$ | 1 ✓ |

> [!warning] Attenzione alla costruzione della tabella condizionale
> Il condizionamento è $X_1$: le righe sommano a 1, le colonne no. Non confondere le righe con le colonne quando si costruisce la tabella.

---

## 7. Esercizio: dado onesto e dado truccato

**Setup**: bussolotto con un dado onesto e uno truccato ($P(6|\text{truccato}) = 1/2$, $P(i|\text{truccato}) = 1/10$ per $i \neq 6$). Si estrae un dado casualmente (prob. $1/2$ ciascuno), si lancia, se il risultato è pari si rilancia lo stesso dado, se dispari si cambia dado.

### Distribuzione del dado truccato

$P(6|\text{truccato}) = 5 \cdot P(i|\text{truccato}) = 5p$. Normalizzazione: $5p + 5p = 1 \Rightarrow p = 1/10$.

$$P(i|\text{truccato}) = \begin{cases} 1/2 & i=6 \\ 1/10 & i \in \{1,2,3,4,5\} \end{cases}$$

### Calcolo di $P(X_1=6, X_2=6)$

Per la legge della probabilità totale (condizionando sul dado estratto):

$$P(X_1=6, X_2=6) = \frac{1}{2} P(X_1=6, X_2=6|\text{onesto}) + \frac{1}{2} P(X_1=6, X_2=6|\text{truccato})$$

- Dado onesto: $P(X_1=6|\text{onesto}) = 1/6$. Dato $X_1=6$ (pari), si rilancia lo stesso dado: $P(X_2=6|X_1=6, \text{onesto}) = 1/6$. Contributo: $1/6 \cdot 1/6 = 1/36$.
- Dado truccato: $P(X_1=6|\text{truccato}) = 1/2$. Dato $X_1=6$ (pari), si rilancia lo stesso dado: $P(X_2=6|X_1=6, \text{truccato}) = 1/2$. Contributo: $1/2 \cdot 1/2 = 1/4$.

$$P(6,6) = \frac{1}{2} \cdot \frac{1}{36} + \frac{1}{2} \cdot \frac{1}{4} = \frac{1}{72} + \frac{1}{8} = \frac{1 + 9}{72} = \frac{10}{72} = \frac{5}{36}$$

### Calcolo di $P(X_1=6, X_2=5)$

- Dado onesto: $P(X_1=6|\text{onesto})=1/6$. Dato $X_1=6$ (pari), si rilancia lo stesso dado: $P(X_2=5|X_1=6, \text{onesto})=1/6$. Contributo: $1/36$.
- Dado truccato: $P(X_1=6|\text{truccato})=1/2$. Dato $X_1=6$ (pari), si rilancia il dado truccato: $P(X_2=5|X_1=6, \text{truccato})=1/10$. Contributo: $1/2 \cdot 1/10 = 1/20$.

$$P(6,5) = \frac{1}{2} \cdot \frac{1}{36} + \frac{1}{2} \cdot \frac{1}{20} = \frac{1}{72} + \frac{1}{40}$$

### Confronto: $P(6,5)$ vs. $P(5,6)$

> [!important] Asimmetria della coppia $(6,5)$ vs $(5,6)$
> Per il calcolo di $P(X_1=5, X_2=6)$: dato $X_1=5$ (dispari), si **cambia dado**. Quindi, se il primo dado era onesto, il secondo è truccato (e viceversa). Questo cambia radicalmente le probabilità:
>
> - Dado onesto primo: $P(X_1=5|\text{onesto})=1/6$. Dato $X_1=5$ (dispari), si usa il dado truccato: $P(X_2=6|\text{truccato})=1/2$. Contributo: $1/6 \cdot 1/2 = 1/12$.
> - Dado truccato primo: $P(X_1=5|\text{truccato})=1/10$. Dato $X_1=5$ (dispari), si usa il dado onesto: $P(X_2=6|\text{onesto})=1/6$. Contributo: $1/10 \cdot 1/6 = 1/60$.
>
> $$P(5,6) = \frac{1}{2} \cdot \frac{1}{12} + \frac{1}{2} \cdot \frac{1}{60} \neq P(6,5)$$
>
> La PMF congiunta **non è simmetrica**: $P(6,5) \neq P(5,6)$. La regola "pari → stesso dado, dispari → cambia dado" rompe la simmetria.

---

> [!summary] Punti chiave della lezione
> - Nel canale binario simmetrico la probabilità di errore è $\varepsilon$ indipendentemente dall'input; il caso peggiore è $\varepsilon=1/2$ (l'uscita non dà informazioni sull'ingresso).
> - L'entropia $H(X) = E[\log_2(1/p_X(X))]$ misura la quantità media di informazione in bit; per una variabile Bernoulliana vale al più 1 bit, raggiunto con $p=1/2$.
> - La PMF marginale è la media della PMF condizionale rispetto alla variabile condizionante.
> - L'indipendenza condizionale (e le catene di Markov) è un concetto distinto dall'indipendenza marginale.
> - Negli esercizi probabilistici complessi, condizionare su un evento ausiliario (legge della probabilità totale) e applicare la regola della catena sistematicamente porta alla soluzione.

## Prossimi argomenti

- [ ] Esercizio 3 della raccolta (da svolgere autonomamente)
- [ ] Approfondimento sulla teoria dell'informazione e sulla compressione
- [ ] Processi di Poisson e catene di Markov
- [ ] Nota: prossima lezione martedì (auguri di Pasqua)

#MSP #canale-binario #entropia #informazione #PMF-condizionale #Bayes #esercizi
