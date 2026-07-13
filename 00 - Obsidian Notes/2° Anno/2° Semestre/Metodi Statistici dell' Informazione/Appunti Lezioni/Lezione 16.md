---
date: 2026-04-28
corso: Metodi Statistici dell'Informazione
docente: Marco Lops
lezione: 16
tags: [MSI, statistica-inferenziale, convergenza, legge-grandi-numeri, bayes, rischio-bayesiano, map, ml]
---

# 🧠 Lezione 16 — Fondamenti di Statistica Inferenziale, Convergenza e Decisione Bayesiana

---

## 1. Introduzione alla Statistica Inferenziale

> [!abstract] Essenza
> La **statistica inferenziale** è il processo bottom-up che utilizza l'analisi dei dati per inferire le proprietà di una distribuzione di probabilità sottostante (popolazione), a differenza della **statistica descrittiva** (o "statistica Excel") che si limita a descrivere le proprietà dei soli dati osservati senza assumere che essi provengano da una popolazione più grande.

Immaginiamo che un dataset $\mathbf{x}^n$ (vettore $n$-dimensionale) sia una realizzazione di un vettore aleatorio $\mathbf{X}^n$. Collezionando un altro dataset $\mathbf{x}'^n$, otterremo valori diversi, ma che condividono le stesse caratteristiche globali della popolazione originaria.

### Obiettivi Fondamentali della Statistica Inferenziale
1. **Test di Ipotesi**: decidere se la natura si trova in uno stato discreto tra una serie di scenari incompatibili.
2. **Stima Parametrica**: determinare il valore di uno o più parametri continui nascosti nei dati.

---

## 2. Successioni di Variabili Aleatorie e Convergenza

Una variabile aleatoria non è un singolo numero, ma una funzione $Y(\omega)$ definita sullo spazio campionario. Pertanto, la convergenza di una successione di variabili aleatorie $Y_n(\omega)$ richiede definizioni specifiche.

### 2.1 Convergenza in Distribuzione
> [!info] Definizione
> La successione $Y_n$ converge in distribuzione a $Y$ ($Y_n \xrightarrow{d} Y$) se la legge di probabilità (CDF) di $Y_n$ converge alla CDF di $Y$ in tutti i punti di continuità.
> 
> *Esempio classico:* Il **Teorema Centrale del Limite (TCL)**. Se $X_i$ sono i.i.d. con media $0$ e varianza $\sigma^2$, allora:
> $$Y_n = \frac{1}{\sqrt{n}}\sum_{i=1}^n X_i \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$

### 2.2 Convergenza in Probabilità
> [!info] Definizione
> La successione $Y_n$ converge in probabilità a $Y$ ($Y_n \xrightarrow{P} Y$) se, per ogni $\epsilon > 0$:
> $$\lim_{n\to\infty} P(|Y_n - Y| > \epsilon) = 0$$

### 2.3 Convergenza in Media Quadratica (MS)
> [!info] Definizione
> La successione $Y_n$ converge in media quadratica a $Y$ ($Y_n \xrightarrow{m.q.} Y$) se:
> $$\lim_{n\to\infty} E[(Y_n - Y)^2] = 0$$

> [!important] Relazione tra convergenze
> La convergenza in media quadratica **implica** la convergenza in probabilità, ma il viceversa non è sempre vero.

### 2.4 Legge Debole dei Grandi Numeri: Dimostrazione
Consideriamo una successione $X_i$ di variabili aleatorie discrete i.i.d., appartenenti all'alfabeto $\{a_1, \dots, a_m\}$ con $P(X_i = a_j) = p_j$.
Vogliamo analizzare la media campionaria:
$$\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$$

Possiamo riordinare la somma raggruppando i termini uguali:
$$\bar{X}_n = \sum_{j=1}^m a_j \frac{N_j}{n}$$
dove $N_j$ è la variabile aleatoria (binomiale) che conta quante volte compare il simbolo $a_j$ su $n$ campioni.
La variabile $N_j$ ha:
- Media: $E[N_j] = n p_j$
- Varianza: $\text{Var}(N_j) = n p_j (1 - p_j)$

Considerando la frequenza relativa $N_j / n$:
- Media: $E\left[\frac{N_j}{n}\right] = p_j$
- Varianza: $\text{Var}\left[\frac{N_j}{n}\right] = \frac{p_j(1-p_j)}{n}$

Applicando la **Disuguaglianza di Chebyshev** per una generica soglia $\delta > 0$:
$$P\left( \left| \frac{N_j}{n} - p_j \right| > \delta \right) \leq \frac{\text{Var}(N_j/n)}{\delta^2} = \frac{p_j(1-p_j)}{n\delta^2}$$
Prendendo il limite per $n \to \infty$:
$$\lim_{n\to\infty} P\left( \left| \frac{N_j}{n} - p_j \right| > \delta \right) = 0$$
Dunque, la frequenza relativa $N_j/n$ converge in probabilità (e in media quadratica, poiché la varianza va a zero) a $p_j$.
Di conseguenza, la media campionaria $\bar{X}_n$ converge alla media statistica:
$$\bar{X}_n \xrightarrow{P} E[X] = \sum_{j=1}^m a_j p_j$$
Questa è la **Legge Debole dei Grandi Numeri**.

> [!tip] Legge Forte dei Grandi Numeri
> Se la convergenza avviene con probabilità 1 (quasi certamente), si parla di Legge Forte. Una condizione sufficiente per la convergenza quasi certa è fornita dal **Lemma di Borel-Cantelli**: se la serie $\sum_{n=1}^\infty P(|Y_n - Y| > \epsilon)$ è sommabile (finita), allora $Y_n \to Y$ con probabilità 1.

---

## 3. Classificazione e Decisione Bayesiana

### 3.1 Formulazione del Problema
- **Osservabili**: $\mathbf{x}^n \in \mathcal{X}^n$, realizzazione del vettore aleatorio $\mathbf{X}^n$.
- **Stati della natura (Ipotesi)**: la natura può trovarsi in uno tra $M$ stati mutualmente esclusivi, descritti dalle ipotesi $H_1, H_2, \dots, H_M$.
- **Distribuzioni condizionate**: se è vera $H_i$, i dati seguono la legge condizionale $P(\mathbf{x}^n | H_i)$ (caso discreto, PMF) o $f(\mathbf{x}^n | H_i)$ (caso continuo, PDF).
- **Probabilità a priori**: $P(H_i) = \pi_i$, con $\sum_{i=1}^M \pi_i = 1$.

### 3.2 Regola di Decisione e Rischio di Bayes
Una regola di decisione è una mappa $d(\mathbf{x}^n)$ che associa a ciascun dataset osservato una decisione $i \in \{1, \dots, M\}$, partizionando lo spazio degli osservabili in $M$ regioni disgiunte $\Omega_1, \dots, \Omega_M$.

Definiamo una **matrice dei costi** $C \in \mathbb{R}^{M \times M}$, in cui $c_{ij}$ rappresenta il costo associato alla scelta dell'ipotesi $H_i$ quando lo stato reale della natura è $H_j$.
Il costo effettivo pagato è una variabile aleatoria $C(\mathbf{X}^n)$. Il **Rischio Medio Bayesiano** è definito come il valore atteso del costo:
$$R_B = \sum_{i=1}^M \sum_{j=1}^M c_{ij} P(d(\mathbf{X}^n) = i, H_j)$$
Una regola di decisione è **Bayes-ottima** se minimizza $R_B$.

### 3.3 Minimizzazione della Probabilità di Errore ($P_e$)
Se impostiamo i costi in modo da non penalizzare le decisioni corrette e penalizzare equamente tutti gli errori:
$$c_{ii} = 0, \quad c_{ij} = 1 \quad (\forall i \neq j)$$
Il rischio medio bayesiano coincide esattamente con la **probabilità di errore $P_e$**:
$$R_B = P_e = \sum_{i \neq j} P(d(\mathbf{X}^n) = i, H_j)$$
Minimizzare $P_e$ equivale a massimizzare la probabilità di decisione corretta $P_c = 1 - P_e$.

#### Caso Binario ($M=2$)
La probabilità di corretta decisione è:
$$P_c = P(H_1) P(d(\mathbf{X}^n)=1 | H_1) + P(H_2) P(d(\mathbf{X}^n)=2 | H_2)$$
Definendo $\Omega_1$ e $\Omega_2$ come le partizioni dello spazio campionario:
$$P_c = \sum_{\mathbf{x}^n \in \Omega_1} \pi_1 P(\mathbf{x}^n | H_1) + \sum_{\mathbf{x}^n \in \Omega_2} \pi_2 P(\mathbf{x}^n | H_2)$$
Per massimizzare questa somma, per ogni stringa osservata $\mathbf{x}^n$, la assegniamo alla regione che fornisce il contributo maggiore. Dunque la regola ottima (a minima probabilità di errore) è:
$$\text{Decidi } H_1 \iff \pi_1 P(\mathbf{x}^n | H_1) > \pi_2 P(\mathbf{x}^n | H_2)$$
Applicando il Teorema di Bayes, dividendo entrambi i membri per la probabilità totale $P(\mathbf{x}^n)$, otteniamo la regola **MAP (Maximum A Posteriori)**:
$$\text{Decidi } H_1 \iff P(H_1 | \mathbf{x}^n) > P(H_2 | \mathbf{x}^n)$$

> [!important] Regola MAP vs ML
> - **MAP (Maximum A Posteriori)**: Sceglie l'ipotesi che massimizza la probabilità a posteriori del parametro date le osservazioni.
> - **ML (Maximum Likelihood / Massima Verosimiglianza)**: Se le ipotesi sono a priori equiprobabili ($\pi_1 = \pi_2$), la regola MAP si semplifica nel confronto diretto delle verosimiglianze (Likelihood):
>   $$\text{Decidi } H_1 \iff P(\mathbf{x}^n | H_1) > P(\mathbf{x}^n | H_2)$$

---

## 4. Esempio Pratico: Classificazione di Sorgenti Binarie I.I.D.

### Setup
- Gli osservabili sono stringhe binarie $\mathbf{x}^n \in \{0, 1\}^n$.
- Le ipotesi sono equiprobabili ($\pi_1 = \pi_2 = 1/2$), perciò MAP coincide con ML.
- Sotto $H_1$: la sorgente è i.i.d. e genera $1$ con probabilità $p_1$.
- Sotto $H_2$: la sorgente è i.i.d. e genera $1$ con probabilità $p_2$.
- Si assume $p_1 > p_2$.

### Sviluppo del Test
La PMF condizionata sotto l'ipotesi $H_j$ per una stringa indipendente è:
$$P(\mathbf{x}^n | H_j) = p_j^{w(\mathbf{x}^n)} (1 - p_j)^{n - w(\mathbf{x}^n)}$$
dove $w(\mathbf{x}^n) = \sum_{i=1}^n x_i$ è il **peso di Hamming** (il numero di $1$ nella stringa).

La regola di massima verosimiglianza impone:
$$\frac{P(\mathbf{x}^n | H_1)}{P(\mathbf{x}^n | H_2)} \gtrdot 1 \implies \frac{p_1^{w(\mathbf{x}^n)} (1 - p_1)^{n - w(\mathbf{x}^n)}}{p_2^{w(\mathbf{x}^n)} (1 - p_2)^{n - w(\mathbf{x}^n)}} \gtrdot 1$$
Prendendo il logaritmo naturale (funzione monotona crescente):
$$w(\mathbf{x}^n) \ln\left(\frac{p_1}{p_2}\right) + [n - w(\mathbf{x}^n)] \ln\left(\frac{1 - p_1}{1 - p_2}\right) \gtrdot 0$$
Raggruppando i termini per il peso di Hamming $w(\mathbf{x}^n)$:
$$w(\mathbf{x}^n) \left[ \ln\left(\frac{p_1}{p_2}\right) - \ln\left(\frac{1 - p_1}{1 - p_2}\right) \right] \gtrdot n \ln\left(\frac{1 - p_2}{1 - p_1}\right)$$
Poiché $p_1 > p_2$, il coefficiente tra parentesi quadre è strettamente positivo. Possiamo dividere isolando il peso di Hamming:
$$w(\mathbf{x}^n) \underset{H_2}{\overset{H_1}{\gtrdot}} \eta_1$$
dove la soglia ottima $\eta_1$ è data da:
$$\eta_1 = n \frac{\ln\left(\frac{1 - p_2}{1 - p_1}\right)}{\ln\left(\frac{p_1(1-p_2)}{p_2(1-p_1)}\right)}$$

> [!info] Interpretazione Geometrica
> Il test ottimo si riduce semplicemente a **contare il numero di 1** nella sequenza ricevuta e a confrontarlo con la soglia $\eta_1$.

### Calcolo della Probabilità di Errore ($P_e$)
L'errore si commette se superiamo la soglia sotto $H_2$, o se non la superiamo sotto $H_1$:
$$P_e = \frac{1}{2} P(w(\mathbf{X}^n) > \eta_1 | H_2) + \frac{1}{2} P(w(\mathbf{X}^n) \leq \eta_1 | H_1)$$
Sotto l'ipotesi $H_j$, il peso di Hamming $w(\mathbf{X}^n)$ è una variabile aleatoria binomiale di parametri $n$ e $p_j$:
$$P_e = \frac{1}{2} \sum_{k = \lfloor \eta_1 \rfloor + 1}^n \binom{n}{k} p_2^k (1 - p_2)^{n-k} + \frac{1}{2} \sum_{k = 0}^{\lfloor \eta_1 \rfloor} \binom{n}{k} p_1^k (1 - p_1)^{n-k}$$