# Ripasso Orale — MSI (Modelli Statistici per l'Inferenza)

> **Stile del prof:** Non chiede dimostrazioni formali, vuole capire che hai intuito il ragionamento dietro. Parla come spiegheresti a qualcuno di intelligente che non conosce la materia. Scrivi formule solo per supportare il ragionamento, non come fine a se stesso.

---

## 1. Fondamenti di Probabilità

### Spazio dei campioni, eventi, probabilità

Lo **spazio dei campioni** $\Omega$ è l'insieme di tutti i possibili esiti di un esperimento. Un **evento** è un sottoinsieme di $\Omega$. La **probabilità** è il limite della frequenza relativa con cui un evento si verifica al crescere delle prove:

$$\mathbb{P}(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

Intuitivamente: se lanci una moneta infinite volte, la frequenza di "testa" converge alla sua probabilità.

### Nomenclatura fondamentale (chiesta esplicitamente)

- **Evento certo**: $\Omega$ — si verifica sempre, $\mathbb{P}(\Omega) = 1$
- **Evento impossibile**: $\emptyset$ — non si verifica mai, $\mathbb{P}(\emptyset) = 0$
- **Eventi complementari**: $A$ e $\bar{A}$ — uno si verifica se e solo se l'altro non si verifica; $\mathbb{P}(\bar{A}) = 1 - \mathbb{P}(A)$
- **Incompatibilità / mutua esclusività**: $A \cap B = \emptyset$ — i due eventi non possono verificarsi contemporaneamente. *Esempio: tirando un dado, "esce 1" e "esce 6" sono incompatibili.*

**Partizione di $\Omega$**: una collezione di eventi $B_1, B_2, \dots, B_k$ è una partizione se sono mutualmente incompatibili e la loro unione dà l'intero spazio campionario:
$$\bigcup_{i=1}^{k} B_i = \Omega \quad \text{e} \quad B_i \cap B_j = \emptyset \ \forall\ i \neq j$$

### Assiomi di Kolmogorov

La probabilità è una funzione che assegna un numero a ogni evento, rispettando tre regole:
1. **Non negatività**: $\mathbb{P}(A) \geq 0$
2. **Normalizzazione**: $\mathbb{P}(\Omega) = 1$
3. **Additività**: se $A$ e $B$ sono incompatibili, $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$

### Probabilità condizionata

La probabilità di $A$ dato $B$ è la probabilità che si verifichi $A$ sapendo che $B$ è già avvenuto:

$$\mathbb{P}(A | B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

**Intuizione**: restringiamo l'universo degli esperimenti a quelli in cui si è verificato $B$, e chiediamo quanti di questi presentano anche $A$.

Da qui segue la **legge della probabilità composta**:
$$\mathbb{P}(A \cap B) = \mathbb{P}(A|B)\mathbb{P}(B) = \mathbb{P}(B|A)\mathbb{P}(A)$$

### Legge della Probabilità Totale ⭐ (chiesta esplicitamente)

**Idea**: se non conosco direttamente $\mathbb{P}(A)$, posso "smontare" l'evento $A$ condizionandolo su una partizione di $\Omega$.

Se $B_1, \ldots, B_k$ è una partizione di $\Omega$, allora:

$$\boxed{\mathbb{P}(A) = \sum_{i=1}^{k} \mathbb{P}(A | B_i)\, \mathbb{P}(B_i)}$$

**Intuizione**: immagina di dover calcolare la probabilità che piova domani. Non lo so direttamente, ma so che domani o c'è vento ($B_1$) o non c'è ($B_2$). Condiziono su questi due scenari, calcolo la probabilità di pioggia in ciascuno, e sommo pesando per la probabilità dello scenario.

**Perché funziona**: l'evento $A$ lo possiamo scrivere come unione degli "spicchi" $A \cap B_i$, che sono incompatibili tra loro (perché i $B_i$ lo sono). Quindi $\mathbb{P}(A) = \sum_i \mathbb{P}(A \cap B_i) = \sum_i \mathbb{P}(A|B_i)\mathbb{P}(B_i)$.

### Legge di Bayes

Combinando la legge della probabilità composta con la probabilità totale:

$$\mathbb{P}(B_i | A) = \frac{\mathbb{P}(A | B_i)\,\mathbb{P}(B_i)}{\sum_j \mathbb{P}(A | B_j)\,\mathbb{P}(B_j)}$$

**Intuizione**: osservo $A$, e voglio capire quale causa $B_i$ ha generato $A$. Ho una credenza iniziale (prior $\mathbb{P}(B_i)$) e la aggiorno alla luce di quello che ho osservato.

### Indipendenza tra eventi

Due eventi $A$ e $B$ sono indipendenti se il verificarsi dell'uno non cambia la probabilità dell'altro:

$$\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$$

**Attenzione**: indipendenza ≠ incompatibilità. Due eventi incompatibili (se si verifica uno, l'altro non può) sono anzi molto "dipendenti" tra loro.

---

## 2. Variabili Aleatorie

### Definizione e caratterizzazione

Una **variabile aleatoria** $X$ è una funzione che assegna un numero reale a ogni esito $\omega$:

$$X: \omega \in \Omega \longrightarrow X(\omega) \in \mathbb{R}$$

È il modo in cui traduciamo un evento qualitativo (es. "esce testa") in un numero su cui fare calcoli.

### PMF (caso discreto) e PDF (caso continuo)

- **PMF** (probability mass function): $p_X(x) = \mathbb{P}(X = x)$ — distribuisce la probabilità su valori discreti
- **PDF** (probability density function): $f_X(x)$ — densità continua; la probabilità di un intervallo è l'area sotto la curva
- **CDF** (cumulative distribution function): $F_X(x) = \mathbb{P}(X \leq x)$ — valida sia per il caso discreto che continuo

### Media (valore atteso) e Varianza

$$\mathbb{E}[X] = \sum_x x\, p_X(x) \quad \text{(discreto)}, \qquad \mathbb{E}[X] = \int x\, f_X(x)\, dx \quad \text{(continuo)}$$

**Intuizione**: è la media pesata dei valori, dove i pesi sono le probabilità. Converge alla media campionaria per la Legge dei Grandi Numeri.

$$\sigma_X^2 = \mathbb{E}[(X - \mu_X)^2] = \mathbb{E}[X^2] - \mu_X^2$$

**Varianza**: misura quanto è "sparsa" la distribuzione attorno alla media. Varianza alta = grande incertezza.

**Disuguaglianza di Chebyshev**: anche senza conoscere la forma esatta della distribuzione, sappiamo che:
$$\mathbb{P}(|X - \mu_X| > k\sigma_X) \leq \frac{1}{k^2}$$

### Variabili Gaussiane

$$X \sim \mathcal{N}(\mu, \sigma^2) \quad \Rightarrow \quad f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Fondamentale per il Teorema del Limite Centrale: la somma di molte variabili i.i.d. converge in distribuzione a una Gaussiana, indipendentemente dalla distribuzione originale. È la distribuzione più importante in statistica.

### Distribuzioni notevoli

| Distribuzione | Parametro | Media | Uso tipico |
|---|---|---|---|
| Uniforme $\mathcal{U}(a,b)$ | $a,b$ | $\frac{a+b}{2}$ | prior non informativo |
| Esponenziale $\mathcal{E}(\lambda)$ | $\lambda$ | $\frac{1}{\lambda}$ | tempi di attesa |
| Poissoniana $\mathcal{P}(\lambda)$ | $\lambda$ | $\lambda$ | conteggi di eventi rari |
| Gaussiana $\mathcal{N}(\mu, \sigma^2)$ | $\mu, \sigma^2$ | $\mu$ | errori, rumore |

### Variabili multiple: pmf congiunta, marginale, condizionata

Quando lavoriamo con due variabili $(X,Y)$:
- **Congiunta**: $p_{X,Y}(x,y) = \mathbb{P}(X=x, Y=y)$
- **Marginale**: $p_X(x) = \sum_y p_{X,Y}(x,y)$ — la distribuzione di $X$ "indipendentemente" da $Y$
- **Condizionata**: $p_{Y|X}(y|x) = \frac{p_{X,Y}(x,y)}{p_X(x)}$

**Covarianza e correlazione**:
$$\text{COV}[X,Y] = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)], \qquad \rho_{X,Y} = \frac{\text{COV}[X,Y]}{\sigma_X \sigma_Y} \in [-1, 1]$$

Indipendenza implica incorrelazione ($\rho = 0$), ma non vale il viceversa.

---

## 3. Statistica Inferenziale — Panoramica

**Obiettivo**: dato un campione osservato $\boldsymbol{x}^n = (x_1, \ldots, x_n)$, vogliamo stimare un parametro $\theta$ che descrive il processo che ha generato i dati.

Due filosofie radicalmente diverse:

| Aspetto | Approccio Bayesiano | Approccio Non-Bayesiano (Frequentista) |
|---|---|---|
| Natura di $\theta$ | Variabile casuale con distribuzione a priori $f_\Theta(\theta)$ | Valore deterministico sconosciuto, nessun prior |
| Informazione disponibile | Prior + verosimiglianza → posterior | Solo la verosimiglianza dei dati |
| Output | Distribuzione a posteriori su $\theta$ | Stima puntuale $\hat{\theta}$ |
| Stimatori tipici | MAP, MMSE | ML (Maximum Likelihood) |

---

## 4. Approccio Bayesiano ⭐ (chiesto esplicitamente)

### L'idea centrale

Nel framework bayesiano, $\theta$ **non è un numero fisso ma sconosciuto** — è visto come la realizzazione di una variabile casuale $\Theta$ con distribuzione **a priori** $f_\Theta(\theta)$. Questo prior codifica la nostra conoscenza (o ignoranza) su $\theta$ prima di osservare i dati.

Dopo aver osservato il campione $\boldsymbol{x}^n$, aggiorniamo la nostra credenza tramite Bayes:

$$\underbrace{f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)}_{\text{posterior}} = \frac{\underbrace{f_{\boldsymbol{X}^n|\Theta}(\boldsymbol{x}^n|\theta)}_{\text{verosimiglianza}} \cdot \underbrace{f_\Theta(\theta)}_{\text{prior}}}{\underbrace{\int f_{\boldsymbol{X}^n|\Theta}(\boldsymbol{x}^n|\theta)\,f_\Theta(\theta)\,d\theta}_{\text{normalizzazione (prob. totale)}}}$$

Il denominatore è proprio la **legge della probabilità totale** applicata a variabili continue.

**In parole semplici**: parto con una credenza iniziale su $\theta$ (prior). I dati mi forniscono informazione (verosimiglianza). Le combino e ottengo una credenza aggiornata (posterior).

### Stimatore MAP ⭐ (chiesto esplicitamente)

Il **Maximum A Posteriori** (MAP) restituisce il valore di $\theta$ che ha la massima probabilità a posteriori — la **moda** della distribuzione posterior.

$$\hat{\theta}_{\text{MAP}}(\boldsymbol{x}^n) = \arg\max_\theta\, f_{\Theta|\boldsymbol{X}^n}(\theta|\boldsymbol{x}^n)$$

**Intuizione**: tra tutti i possibili valori di $\theta$, scelgo quello più "credibile" alla luce dei dati osservati. È come scegliere il picco di una collina.

**Funzione di costo associata**: il MAP minimizza il rischio bayesiano quando si usa una **funzione di costo 0-1** (costo zero se sbaglio di poco, costo unitario altrimenti). In questo senso minimizza la probabilità di errore.

**Relazione con ML**: se il prior è uniforme (non ho preferenze a priori su nessun valore di $\theta$), allora il MAP coincide con il Maximum Likelihood (ML). Il prior piatto non altera la forma della posterior.

### Stimatore MMSE

Il **Minimum Mean Square Error** restituisce la **media** della distribuzione a posteriori:

$$\hat{\theta}_{\text{MMSE}}(\boldsymbol{x}^n) = \mathbb{E}[\Theta | \boldsymbol{X}^n = \boldsymbol{x}^n]$$

**Intuizione**: minimizza il valore atteso dell'errore quadratico $({\hat\theta} - \theta)^2$. È il "centro di massa" della distribuzione posterior.

**Quando MAP = MMSE**: se la distribuzione a posteriori è **simmetrica** rispetto alla sua media (es. gaussiana), allora moda e media coincidono, quindi MAP = MMSE.

### Confronto MAP vs MMSE (esempio: Bernoulli)

Dato un campione binario con $w$ successi su $n$ prove, e prior uniforme su $\beta \in [0,1]$:

$$\hat{\beta}_{\text{MAP}} = \frac{w}{n} \qquad \hat{\beta}_{\text{MMSE}} = \frac{w+1}{n+2}$$

- Il MAP coincide con la frequenza empirica — ignora l'effetto del prior
- L'MMSE tiene conto del prior: "spinge" la stima verso il centro $(0.5)$, specialmente quando il campione è piccolo
- Entrambi convergono allo stesso valore per $n \to \infty$ (il prior diventa irrilevante con molti dati)

---

## 5. Approccio Non-Bayesiano (Frequentista) ⭐ (chiesto esplicitamente)

### L'idea centrale

In questo framework $\theta$ è un **numero fisso e sconosciuto**, non una variabile casuale. Non esiste un prior. L'unica informazione disponibile è la **funzione di verosimiglianza** dei dati:

$$L(\theta; \boldsymbol{x}^n) = f_{\boldsymbol{X}^n}(\boldsymbol{x}^n; \theta)$$

che esprime quanto sarebbero "probabili" i dati osservati se il parametro fosse $\theta$.

### Stimatore ML (Maximum Likelihood)

Scegli il valore di $\theta$ che massimizza la verosimiglianza — quello che "spiega meglio" i dati:

$$\hat{\theta}_{\text{ML}} = \arg\max_\theta\, \log f_{\boldsymbol{X}^n}(\boldsymbol{x}^n; \theta)$$

**Intuizione**: tra tutti i possibili modelli, scegli quello sotto il quale i dati che hai osservato sono più probabili.

**Perché il log**: il logaritmo trasforma prodotti in somme (utile quando i campioni sono i.i.d.) e non cambia il massimo.

### Proprietà degli stimatori non-Bayesiani

**Bias (distorsione)**: $b(\theta) = \mathbb{E}[\hat{\Theta}] - \theta$. Uno stimatore si dice **non distorto** (unbiased) se $b(\theta) = 0$, cioè in media centra il valore vero.

**MSE (Mean Square Error)**:
$$\text{MSE} = \mathbb{E}[(\hat{\Theta} - \theta)^2] = \text{Bias}^2 + \text{Varianza}$$

C'è un trade-off: ridurre il bias può aumentare la varianza e viceversa.

**Consistenza**: uno stimatore è consistente se converge al valore vero al crescere di $n$:
- Consistenza in probabilità (debole): $\hat{\Theta}(\boldsymbol{X}^n) \xrightarrow{P} \theta$
- Consistenza MS: $\text{MSE} \to 0$ per $n \to \infty$
- Consistenza quasi certa (forte): $\mathbb{P}(\lim_{n\to\infty} \hat{\Theta} = \theta) = 1$

### Limite di Cramér-Rao

Fornisce un **lower bound** alla varianza di qualsiasi stimatore non distorto. Nessun estimatore può avere varianza inferiore a:

$$\text{Var}[\hat{\Theta}] \geq \frac{1}{I_n(\theta)}$$

dove $I_n(\theta)$ è l'**informazione di Fisher** — misura quanta informazione i dati contengono sul parametro $\theta$.

**Efficienza**: uno stimatore non distorto che raggiunge il CRB si dice **efficiente**. Se esiste uno stimatore efficiente, coincide con l'ML.

---

## 6. Differenza chiave: Bayesiano vs Non-Bayesiano ⭐ (chiesto esplicitamente)

| | Bayesiano | Non-Bayesiano |
|---|---|---|
| $\theta$ è... | Una variabile casuale | Un numero fisso ignoto |
| Ho bisogno di... | Prior $f_\Theta(\theta)$ + verosimiglianza | Solo la verosimiglianza |
| Stimo... | La distribuzione posterior su $\theta$ | Un valore puntuale di $\theta$ |
| Misura di errore | Rischio bayesiano medio | MSE, bias, varianza |
| Stimatori ottimi | MAP (moda posterior), MMSE (media posterior) | ML |
| Quando usarlo | Ho informazione a priori affidabile su $\theta$ | Non ho (o non voglio usare) informazione a priori |

**Intuizione chiave**: l'approccio bayesiano risponde alla domanda "dato che ho osservato $\boldsymbol{x}^n$, qual è la distribuzione più plausibile di $\theta$?". Il frequentista risponde "qual è il valore di $\theta$ che rende $\boldsymbol{x}^n$ più probabile?". Sono domande diverse.

---

## 7. Test di Ipotesi

### Impostazione Bayesiana (classificazione binaria)

Ho due ipotesi $H_1$ e $H_2$ con probabilità a priori $P(H_1)$ e $P(H_2)$. La **regola MAP** minimizza la probabilità di errore:

$$L(\boldsymbol{x}^n) = \frac{p_{\boldsymbol{X}^n}(\boldsymbol{x}^n | H_1)}{p_{\boldsymbol{X}^n}(\boldsymbol{x}^n | H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta$$

Il **rapporto di verosimiglianza** $L$ confronta quanto sono "compatibili" i dati con ciascuna ipotesi.

### Test di Neyman-Pearson (non-Bayesiano)

Quando non si possono assegnare probabilità a priori alle ipotesi (es. sicurezza, difesa), si usa un approccio diverso:

- **Errore tipo I** (falso allarme): rifiuto $H_0$ quando è vera — probabilità $\alpha$
- **Errore tipo II** (miss): accetto $H_0$ quando è falsa — probabilità $\beta$
- **Potenza del test**: $1-\beta$ — capacità di rilevare $H_1$ quando è vera

Il test NP **massimizza la potenza fissato un vincolo sul falso allarme** ($\alpha$). La regola risultante è ancora basata sul rapporto di verosimiglianza con soglia $\eta$ scelto per rispettare il vincolo su $\alpha$.

---

## 8. Stimatori LMMSE e Minimi Quadrati

### LMMSE (Linear Minimum MSE)

Stimatore della forma lineare $\hat{\Theta} = \boldsymbol{a}^T \boldsymbol{X}^n + b$. Non richiede la conoscenza completa della distribuzione, solo media e covarianza dei dati. Nel caso gaussiano coincide con l'MMSE ottimo.

### Minimi Quadrati (Least Squares)

In un approccio puramente descrittivo (non probabilistico), dati $p$ campioni con etichette note, si cerca il coefficiente lineare $\boldsymbol{a}$ che minimizza l'errore quadratico sui dati:

$$\boldsymbol{a}_{\text{LS}} = (\boldsymbol{X}\boldsymbol{X}^T)^{-1}\boldsymbol{X}\boldsymbol{y}$$

**LS ricorsivo**: quando arrivano nuovi dati, invece di ricalcolare tutto da zero (costo $\mathcal{O}(n^3)$), si usa la formula di Sherman-Morrison per aggiornare la stima con costo $\mathcal{O}(n^2)$.

---

## 9. Processi Aleatori (cenni)

Un **processo aleatorio** associa a ogni esito dell'esperimento una sequenza temporale. Se si fissa il tempo, si ottiene una variabile aleatoria; se si fissa l'esito, si ottiene una sequenza deterministica.

**Stazionarietà al 2° ordine**: la pdf congiunta di due campioni dipende solo dalla loro distanza temporale, non dalla loro posizione assoluta. (La stazionarietà al 2° ordine implica quella al 1°, ma non viceversa.)

---

---

## 🚫 Argomenti esclusi e motivazione

Di seguito gli argomenti presenti nelle note che ho scelto di **non includere** nel ripasso, con la relativa motivazione.

### Calcolo Combinatorio (permutazioni, combinazioni, prodotti cartesiani)

Argomenti preparatori alla probabilità discreta, ma non rilevanti per un orale focalizzato su stima e inferenza. Il prof ha chiesto concetti applicativi, non conteggio.

### Algebra di eventi e $\sigma$-algebra

Strutture formali necessarie per fondare la probabilità in modo rigoroso su spazi infiniti. Il prof ha esplicitamente evitato le dimostrazioni formali; questo argomento è puramente strutturale e improbabile all'orale.

### Variabili di Cauchy e Laplaciane

Distribuzioni specifiche non citate nei temi d'esame. Il prof sembra interessato ai concetti generali e alle distribuzioni più usate (Gaussiana, uniforme, esponenziale). La Laplaciana è collegata a MAP con prior Laplaciano, ma questo livello di dettaglio non è emerso.

### Processi aleatori: caratterizzazione completa, stazionarietà al 1° ordine, funzioni di autocorrelazione

La sezione sui processi è presente nelle note ma non è emersa nei temi d'esame del collega. Il prof si è concentrato su stima e inferenza. Ho incluso solo un cenno alla stazionarietà per completezza.

### Teorema del Limite Centrale (TCL) — dettagli tecnici

Il TCL è citato come motivazione per la Gaussiana, ma la sua derivazione formale (convergenza in distribuzione, caratteristiche delle MGF) è fuori dallo stile dell'orale descritto.

### LS ricorsivo e formula di Sherman-Morrison — dettaglio

Ho incluso un cenno, ma le derivazioni dettagliate dell'aggiornamento ricorsivo e la convergenza del gradiente sono formule tecniche improbabili in un orale che non richiede dimostrazioni.

### Informazione di Fisher — derivazione formale e bound CRB completo

Ho spiegato l'intuizione del CRB, ma la derivazione tramite Cauchy-Schwarz e la funzione di punteggio sono dettagli formali che il prof non dovrebbe richiedere.

### Appendici (formule algebriche, tabelle quantili, identità matriciali)

Strumenti di calcolo, non concetti. Utili durante la prova scritta, inutili all'orale.
