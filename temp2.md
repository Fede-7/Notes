La **funzione generatrice dei momenti (MGF)**, definita come $\Phi_X(s) = \mathbb{E}[e^{sX}]$, è uno strumento analitico fondamentale per semplificare il calcolo e lo studio delle variabili aleatorie.

Ecco le sue utilità principali:

### 1. Calcolo rapido dei momenti
Invece di risolvere integrali complessi per ogni momento, basta derivare la MGF e valutare il risultato in $s=0$:
*   **Media**: $\mathbb{E}[X] = \Phi'(0)$.
*   **Varianza**: si ricava dal secondo momento $\mathbb{E}[X^2] = \Phi''(0)$.
*   **Momento n-esimo**: $\mathbb{E}[X^n] = \Phi^{(n)}(0)$.

### 2. Caratterizzazione univoca
Esiste una corrispondenza biunivoca tra MGF e funzione di ripartizione: una specifica MGF identifica **una e una sola** distribuzione di probabilità.

### 3. Somma di variabili indipendenti
La MGF trasforma l'operazione di somma di variabili aleatorie indipendenti (che richiederebbe una convoluzione) in una semplice **moltiplicazione**:
$$\Phi_{X+Y}(s) = \Phi_X(s) \cdot \Phi_Y(s)$$
Questa proprietà è usata per dimostrare che la somma di variabili Normali, di Poisson o Gamma segue ancora la stessa famiglia di distribuzione.

### 4. Studio della convergenza (Teorema di Levy)
La MGF è essenziale per l'analisi asintotica: se una successione di MGF $\Phi_{X_n}(s)$ converge puntualmente a $\Phi_X(s)$, allora la successione di variabili $X_n$ **converte in distribuzione** a $X$.

### 5. Sviluppo in serie
La MGF può essere espressa tramite lo sviluppo in serie di **MacLaurin**, dove i coefficienti della serie sono direttamente i momenti della variabile:
$$\Phi_X(s) = \sum_{n=0}^{\infty} \frac{\mathbb{E}[X^n]}{n!} s^n$$