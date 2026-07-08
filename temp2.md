Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, uniformato il codice LaTeX e migliorato la struttura didattica mantenendo il rigore matematico richiesto.

---

# Variabili Gaussiane: Caratterizzazione Marginale

Una variabile aleatoria $X_0 \in \mathbb{R}$ si definisce **Gaussiana** (o Normale) standard se segue la distribuzione $X_0 \sim \mathcal{N}(0, 1)$, la cui funzione di densità di probabilità (PDF) è data da:

$$f_{X_0}(x_0) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x_0^2}{2}}, \quad x_0 \in \mathbb{R}$$

Da questa definizione si deducono immediatamente i parametri di primo e secondo ordine:
$$\mathbb{E}[X_0] = 0, \quad \sigma_{X_0}^2 = \mathbb{E}[X_0^2] = 1$$

> [!dim] Dimostrazione della densità della variabile Gaussiana generica
> Partendo da $X_0 \sim \mathcal{N}(0, 1)$ e applicando la trasformazione lineare $X = \sigma_X X_0 + \mu_X$:
> 
> 1. **Trasformazione inversa:** Definiamo $x_0 = g^{-1}(x) = \frac{x - \mu_X}{\sigma_X}$. Il Jacobiano della trasformazione è:
> $$\left| \frac{d}{dx} g^{-1}(x) \right| = \frac{1}{\sigma_X}$$
> 
> 2. **Cambio di variabile:** Applicando la formula $f_X(x) = f_{X_0}(g^{-1}(x)) \cdot \left| \frac{d}{dx} g^{-1}(x) \right|$, otteniamo:
> $$f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu_X}{\sigma_X}\right)^2} \cdot \frac{1}{\sigma_X} = \frac{1}{\sqrt{2\pi\sigma_X^2}} e^{-\frac{(x - \mu_X)^2}{2\sigma_X^2}}$$
> Ciò conferma che $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$.
> 
> 3. **Momenti:**
> - $\mathbb{E}[X] = \mathbb{E}[\sigma_X X_0 + \mu_X] = \sigma_X \mathbb{E}[X_0] + \mu_X = \mu_X$
> - $\operatorname{Var}(X) = \operatorname{Var}(\sigma_X X_0 + \mu_X) = \sigma_X^2 \operatorname{Var}(X_0) = \sigma_X^2$

#### Andamenti delle PDF Gaussiane
![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/14bd5c980e8521e5eb02a7517ff1fac46626c196028264217617a09b4afc4823.jpg)
*Figura 1: Confronto tra diverse funzioni di densità di probabilità Gaussiane.*

---

# La Funzione $Q(x)$ e la Coda della Distribuzione

Sia $X_0 \sim \mathcal{N}(0, 1)$ una variabile casuale normale standard. Poiché l'integrale della funzione $e^{-t^2/2}$ non ammette primitive elementari, la sua funzione di ripartizione (CDF) e la relativa funzione complementare (CCDF) non possono essere espresse in forma chiusa.

Per superare tale limite, si introduce la **funzione $Q(x)$**:
$$Q(x) \stackrel{\text{def}}{=} \mathbb{P}(X_0 \geq x) = 1 - F_{X_0}(x) = \frac{1}{\sqrt{2\pi}} \int_x^\infty e^{-\frac{t^2}{2}} dt$$

Da questa definizione derivano le seguenti relazioni fondamentali:
*   **Funzione di ripartizione:** $F_{X_0}(x) = 1 - Q(x)$
*   **Probabilità in un intervallo:** $\mathbb{P}(x \leq X_0 \leq x + \Delta x) = Q(x) - Q(x + \Delta x)$

Per una variabile casuale generale $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$, la probabilità complementare è espressa come:
$$1 - F_X(x) = Q\left(\frac{x - \mu_X}{\sigma_X}\right)$$

#### Comportamento Asintotico di $Q(x)$
Per valori elevati di $x$, la funzione $Q(x)$ decade rapidamente seguendo il comportamento asintotico:
$$Q(x) \sim \frac{1}{x\sqrt{2\pi}} e^{-\frac{x^2}{2}} < e^{-\frac{x^2}{2}}, \quad \text{per } x \to \infty$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9e014a72e6bb4cff5f6045f5e3af68f8479b85e9889bcb10a79b45de356eb16a.jpg)
*Figura 2: Andamento della funzione $Q(x)$.*

#### Proprietà Analitiche di $Q(x)$

La funzione $Q(x)$ è caratterizzata dalle seguenti proprietà:

1.  **Valori Limite:**
    $$Q(-\infty) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty e^{-\frac{t^2}{2}} dt = 1, \quad Q(+\infty) = 0$$
2.  **Monotonia:** Derivando la funzione si ottiene:
    $$\frac{dQ(x)}{dx} = -\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} < 0, \quad \forall x \in \mathbb{R}$$
    Questo dimostra che $Q(x)$ è una funzione **strettamente decrescente**.
3.  **Simmetria:** La funzione soddisfa la relazione:
    $$Q(-x) = 1 - Q(x)$$
4.  **Generalizzazione:** Per una variabile casuale $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$, la probabilità che $X$ superi una soglia $\eta$ è data da:
    $$\mathbb{P}(X \geq \eta) = Q\left(\frac{\eta - \mu_X}{\sigma_X}\right)$$

### Caratterizzazione congiunta di variabili Gaussiane

Siano $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ e $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$ due variabili casuali. Le loro proprietà statistiche individuali sono descritte da:

$$
\sigma_1^2 = \mathbb{E}[(X_1 - \mu_1)^2], \quad \sigma_2^2 = \mathbb{E}[(X_2 - \mu_2)^2]
$$

Il coefficiente di correlazione $\rho_{1,2}$ è definito come:

$$
\rho_{1,2} = \frac{\mathbb{E}[(X_1 - \mu_1)(X_2 - \mu_2)]}{\sigma_1 \sigma_2} = \frac{\text{Cov}(X_1, X_2)}{\sigma_1 \sigma_2}
$$

Sebbene questi parametri forniscano una descrizione parziale della coppia $(X_1, X_2)$, è possibile organizzare le variabili in un vettore casuale bidimensionale $\pmb{X} \in \mathbb{R}^{2 \times 1}$:

$$
\pmb{X} = \begin{pmatrix} X_1 \\ X_2 \end{pmatrix}, \quad \pmb{\mu}_X = \begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}
$$

#### Matrice di covarianza

La **matrice di covarianza** $\boldsymbol{K}_{\pmb{X}} \in \mathbb{R}^{2 \times 2}$ è definita come:

$$
\boldsymbol{K}_{\pmb{X}} \stackrel{\text{def}}{=} \mathbb{E}[(\pmb{X} - \pmb{\mu}_X)(\pmb{X} - \pmb{\mu}_X)^T] = \mathbb{E} \left[ \begin{pmatrix} X_1 - \mu_1 \\ X_2 - \mu_2 \end{pmatrix} (X_1 - \mu_1, X_2 - \mu_2) \right]
$$

Espandendo il prodotto esterno, otteniamo la forma chiusa:

$$
\boldsymbol{K}_{\pmb{X}} = \begin{pmatrix} \mathbb{E}[(X_1 - \mu_1)^2] & \mathbb{E}[(X_1 - \mu_1)(X_2 - \mu_2)] \\ \mathbb{E}[(X_2 - \mu_2)(X_1 - \mu_1)] & \mathbb{E}[(X_2 - \mu_2)^2] \end{pmatrix} = \begin{pmatrix} \sigma_1^2 & \sigma_1 \sigma_2 \rho_{1,2} \\ \sigma_1 \sigma_2 \rho_{1,2} & \sigma_2^2 \end{pmatrix} \tag{1}
$$

#### Proprietà della matrice di covarianza

La matrice $\boldsymbol{K}_{\pmb{X}}$ possiede le seguenti proprietà fondamentali:

*   **Simmetria:** Per costruzione, $\boldsymbol{K}_{\pmb{X}} = \boldsymbol{K}_{\pmb{X}}^T$.
*   **Definitività non negativa:** Poiché il determinante è $|\boldsymbol{K}_{\pmb{X}}| = \sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2) \geq 0$, la matrice è definita non negativa.
*   **Invertibilità:** Se $\rho_{1,2} \neq \pm 1$, la matrice è invertibile e la sua inversa è definita positiva:
    $$
    \boldsymbol{K}_{\pmb{X}}^{-1} = \frac{1}{\sigma_1^2 \sigma_2^2 (1 - \rho_{1,2}^2)} \begin{pmatrix} \sigma_2^2 & -\sigma_1 \sigma_2 \rho_{1,2} \\ -\sigma_1 \sigma_2 \rho_{1,2} & \sigma_1^2 \end{pmatrix}
    $$
*   **Condizione di positività:** Per ogni vettore $\pmb{z} = [z_1, z_2]^T \in \mathbb{R}^{2 \times 1}$, vale:
    $$
    \pmb{z}^T \boldsymbol{K}_{\pmb{X}}^{-1} \pmb{z} \geq 0
    $$
*   **Caso di indipendenza (Incorrelazione):** Se $X_1$ e $X_2$ sono incorrelate ($\rho_{1,2} = 0$), la matrice di covarianza diventa diagonale:
    $$
    \boldsymbol{K}_{\pmb{X}} = \begin{pmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{pmatrix} \implies \boldsymbol{K}_{\pmb{X}}^{-1} = \begin{pmatrix} \frac{1}{\sigma_1^2} & 0 \\ 0 & \frac{1}{\sigma_2^2} \end{pmatrix}
    $$

#### Variabili congiuntamente Gaussiane

Le variabili $X_1$ e $X_2$ si dicono **congiuntamente Gaussiane** se la loro funzione di densità di probabilità (pdf) congiunta $f_{\pmb{X}}(\pmb{x})$ è data dalla seguente forma:

$$
f_{\pmb{X}}(\pmb{x}) = \frac{1}{2\pi |\boldsymbol{K}_{\pmb{X}}|^{1/2}} \exp \left[ -\frac{1}{2} (\pmb{x} - \pmb{\mu}_X)^T \boldsymbol{K}_{\pmb{X}}^{-1} (\pmb{x} - \pmb{\mu}_X) \right]
$$

> [!IMPORTANT]
> La caratterizzazione congiunta tramite la matrice di covarianza $\boldsymbol{K}_{\pmb{X}}$ è sufficiente a definire completamente la distribuzione di una coppia di variabili Gaussiani, poiché essa cattura sia le varianze individuali che la correlazione tra le componenti.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, corretto le incongruenze nei simboli (come l'uso di $\mu_Y$ invece di $\mu_Z$) e strutturato il contenuto per una migliore leggibilità didattica.

---

# Distribuzioni Gaussiane e Trasformazioni Lineari

## La Distribuzione Gaussiana Bivariata
La densità di probabilità di una variabile aleatoria bivariata gaussiana è definita dalla seguente espressione:

$$f(x_1, x_2) = \frac{1}{2\pi \sqrt{|\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right) \tag{2}$$

Espandendo la formula in termini di parametri specifici ($\sigma_1^2, \sigma_2^2$ e il coefficiente di correlazione $\rho_{1,2}$), otteniamo:

$$f(x_1, x_2) = \frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})}} \exp \left[ - \frac {\sigma_ {2} ^ {2} (x _ {1} - \mu_ {1}) ^ {2} + \sigma_ {1} ^ {2} (x _ {2} - \mu_ {2}) ^ {2} - 2 \rho_ {1 , 2} (x _ {1} - \mu_ {1}) (x _ {2} - \mu_ {2})}{2 \sigma_ {1} ^ {2} \sigma_ {2} ^ {2} (1 - \rho_ {1 , 2} ^ {2})} \right]$$

Per semplicità, si utilizza comunemente la notazione abbreviata:
> [!IMPORTANT] Notazione Standard
> $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{K})$

### Caso di Indipendenza
Nel caso speciale in cui le variabili siano non correlate ($\rho_{1,2} = 0$), la densità bivariata si scompone nel prodotto delle densità marginali:

$$f_{\mathbf{X}}(x_1, x_2) = f_{X_1, X_2}(x_1, x_2) = \frac {1}{2 \pi \sqrt {\sigma_ {1} ^ {2} \sigma_ {2} ^ {2}}} e ^ {- \frac {(x _ {1} - \mu_ {1}) ^ {2}}{2 \sigma_ {1} ^ {2}} - \frac {(x _ {2} - \mu_ {2}) ^ {2}}{2 \sigma_ {2} ^ {2}}} = f_{X_1}(x_1) f_{X_2}(x_2)$$

[!NOTE] Proprietà Fondamentale
Per le variabili congiuntamente Gaussiane, l'**incorrelazione implica l'indipendenza statistica**. Questa proprietà è specifica della famiglia gaussiana.

---

## Proprietà di Chiusura rispetto a Trasformazioni Lineari
Se $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}_X, \mathbf{K}_X)$, ogni trasformazione lineare di $\mathbf{X}$ produce una nuova variabile aleatoria che segue una distribuzione gaussiana.

### Combinazione Lineare Semplice
Consideriamo la combinazione lineare $Z = a_1 X_1 + a_2 X_2$. I parametri della nuova variabile $Z$ sono dati da:

$$ \mu_Z = a_1 \mu_1 + a_2 \mu_2, \quad \sigma_Z^2 = a_1^2 \sigma_1^2 + a_2^2 \sigma_2^2 + 2 a_1 a_2 \sigma_1 \sigma_2 \rho_{1,2} $$
$$ \boxed{Z \sim \mathcal{N}(\mu_Z, \sigma_Z^2)} $$

### Trasformazione Lineare Generale
Più in generale, data la trasformazione $\mathbf{Z} = \mathbf{A}\mathbf{X} + \mathbf{b}$, con $\mathbf{A} \in \mathbb{R}^{2 \times 2}$ e $\mathbf{b} \in \mathbb{R}^{2 \times 1}$, i parametri della distribuzione risultano:

- **Vettore dei medi:**
  $$\boldsymbol{\mu}_Z = \mathbf{A}\boldsymbol{\mu}_X + \mathbf{b} \tag{3}$$
- **Matrice di covarianza:**
  $$\mathbf{K}_Z = \mathbb{E}[(Z - \boldsymbol{\mu}_Z)(Z - \boldsymbol{\mu}_Z)^T] = \mathbf{A}\mathbf{K}_X\mathbf{A}^T \tag{4}$$

Pertanto, la distribuzione risultante è:
$$\mathbf{Z} \sim \mathcal{N}(\boldsymbol{\mu}_Z, \mathbf{K}_Z)$$

---

## Fondamenti sulle Variabili Aleatorie
Si consideri uno spazio di probabilità $(\Omega, \mathcal{T}, \mathbb{P})$, dove $\Omega$ è lo spazio dei campioni, $\mathcal{T}$ è una $\sigma$-algebra di eventi e $\mathbb{P}: \mathcal{T} \to [0, 1]$ è la legge di probabilità.

### Definizioni Base
- **Variabile Aleatoria (V.A.):** Una funzione misurabile $X: \Omega \to \mathcal{X} \subseteq \mathbb{R}$.
  - La V.A. è definita come *discreta* o *continua* a seconda della natura del suo supporto $\mathcal{X}$.
- **Coppia di Variabili Aleatorie:** Un'applicazione $X, Y: \Omega \to \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$.

### Caratterizzazione delle Distribuzioni
Una variabile aleatoria $X$ è completamente caratterizzata dalla sua **funzione di ripartizione (CDF)** $F_X(x)$. In base alla natura della variabile, si utilizzano le seguenti forme:

1. **Variabile Discreta:** Definita tramite la funzione di massa (PMF) $p_X(x)$:
   $$p_X(x) = \mathbb{P}\{X = x\}, \quad \forall x \in \mathcal{X}$$
2. **Variabile Continua:** Definita tramite la funzione di densità di probabilità (PDF) $f_X(x)$:
   $$f_X(x) = \frac{dF_X(x)}{dx}$$

Per una coppia $(X, Y)$, le funzioni corrispondenti sono:
- **CDF Bivariata:** $F_{X,Y}(x,y) = \mathbb{P}\{X \leq x, Y \leq y\}$
- **PDF Bivariata:** $f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}(x,y)}{\partial x \partial y}$
- **PMF Bivariata:** $p_{X,Y}(x,y) = \mathbb{P}\{X = x, Y = y\}$

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Vettori Aleatori

Un **vettore aleatorio** rappresenta la generalizzazione naturale del concetto di coppia di variabili aleatorie. Formalmente, un vettore aleatorio $\boldsymbol{X}$ è definito come una mappa che associa a ogni elemento dello spazio campione $\omega \in \Omega$ una $n$-pla di valori:

$$
\boldsymbol{X}(\omega) = (X_1(\omega), \dots, X_n(\omega)) \in \mathcal{X}_1 \times \dots \times \mathcal{X}_n \subseteq \mathbb{R}^n
$$

In notazione matriciale, il vettore può essere espresso come:

$$
\boldsymbol{X}(\omega) = [X_1(\omega), \dots, X_n(\omega)]^T \in \prod_{i=1}^n \mathcal{X}_i \subseteq \mathbb{R}^n
$$

La caratterizzazione statistica del vettore dipende dalla natura degli alfabeti $\mathcal{X}_i$:

### 1. Casi Discreti
Se gli alfabeti $\mathcal{X}_1, \dots, \mathcal{X}_n$ sono discreti, il vettore è definito dalla **funzione di probabilità (PMF) congiunta**:

$$
p_{\boldsymbol{X}}(\boldsymbol{x}) = P(X_1 = x_1, \dots, X_n = x_n) = p_{\mathcal{X}}(x_1, \dots, x_n), \quad \forall \boldsymbol{x} \in \prod_{i=1}^n \mathcal{X}_i
$$

dove $\boldsymbol{x} = [x_1, \dots, x_n]^T$.

### 2. Casi Continui
Per alfabeti continui, il vettore è caratterizzato dalla **funzione di ripartizione (CDF)** e dalla relativa **densità di probabilità (PDF)**:

$$
F_{\boldsymbol{X}}(\boldsymbol{x}) = P(X_1 \leq x_1, \dots, X_n \leq x_n), \quad \forall \boldsymbol{x} \in \mathbb{R}^n
$$

$$
f_{\boldsymbol{X}}(\boldsymbol{x}) = \frac{\partial^n F_{\boldsymbol{X}}(\boldsymbol{x})}{\partial x_1 \dots \partial x_n}
$$

dove $\boldsymbol{x} = [x_1, \dots, x_n]^T \in \mathbb{R}^n$.

---

# Legge di Bayes per Vettori Aleatori

Consideriamo un vettore aleatorio discreto con PMF $p_{\boldsymbol{X}}(\boldsymbol{x})$. La **Legge di Bayes** stabilisce che:

$$
P(A \cap B) = P(A | B) P(B)
$$

Applicando questa proprietà al vettore $\boldsymbol{X}$, ponendo $A = \{X_n = x_n, \dots, X_2 = x_2\}$ e $B = \{X_1 = x_1\}$, otteniamo:

$$
p_{\boldsymbol{X}}(\boldsymbol{x}) = P(X_n = x_n, \dots, X_2 = x_2 | X_1 = x_1) P(X_1 = x_1)
$$

### Regola della Catena (Chain Rule)
Iterando il ragionamento precedente, si deriva la **regola della catena**, che permette di scomporre la distribuzione congiunta in una serie di distribuzioni condizionate:

$$
\begin{aligned}
p_{\boldsymbol{X}}(\boldsymbol{x}) &= P(X_1 = x_1) P(X_2 = x_2 | X_1 = x_1) \dots P(X_n = x_n | X_{n-1} = x_{n-1}, \dots, X_1 = x_1) \\
&= \prod_{i=1}^n p_{X_i | X_{i-1}, \dots, X_1}(x_i | x_{i-1}, \dots, x_1)
\end{aligned}
$$

dove per convenzione si assume $p_{X_1 | X_0}(x_1 | x_0) = p_{X_1}(x_1)$.

Analogamente, per vettori continui, la densità congiunta può essere espressa come:

$$
f_{\boldsymbol{X}}(\boldsymbol{x}) = \prod_{i=1}^n f_{X_i | X_{i-1}, \dots, X_1}(x_i | x_{i-1}, \dots, x_1)
$$

> [!IMPORTANT]
> La regola della catena è fondamentale per modellare sistemi sequenziali e processi stocastici, poiché permette di descrivere la probabilità di una sequenza come il prodotto delle probabilità condizionate dei singoli eventi.

---

# Processi Aleatori Tempo-Discreti

Si definisce **processo aleatorio tempo-discreto** un'applicazione che associa a ogni elemento dello spazio campione $\omega \in \Omega$ una successione di variabili aleatorie indicizzate su un insieme discreto (solitamente gli interi):

$$
X: \omega \in \Omega \longrightarrow \{X(n, \omega)\}_{n \in \mathbb{Z}}
$$

> [!example] Esempio 1: Realizzazioni di un processo tempo-discreto
> Di seguito sono riportate tre diverse realizzazioni (traiettorie) del medesimo processo aleatorio tempo-discreto.
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/7e76ee276ef5ef4aa0a28d11f4fc129e3b4bfc5e7363b6e3ebb01def91168f7a.jpg)
> *Figura 1: Realizzazione 1*
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/eef731154ce7b72b160d3d277cbe6b34a0a3867f94f145234edd9dd15d98f5db.jpg)
> *Figura 2: Realizzazione 2*
>
> ![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/057411ab0f31edbb00e115bfa3816d1d5e5f1c3faed5ab464cbf318ca0bb423a.jpg)
> *Figura 3: Realizzazione 3*

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica, la fluidità formale e il rigore matematico.

---

## Analisi delle Proprietà del Processo Aleatorio

### Caratterizzazione al Primo Ordine
Consideriamo un processo aleatorio $X(n, \omega)$ definito su uno spazio campionario $\Omega$. Per ogni realizzazione $\omega \in \Omega$, il processo evolve in una sequenza di valori appartenenti all'intervallo $[-1, 1]$.

*   **Variabile Aleatoria:** Fissando un istante temporale $n = n_0$ e variando la realizzazione $\omega$, otteniamo la variabile aleatoria $X(n_0, \omega)$. Questo avviene poiché il "campionamento verticale" (ovvero la valutazione del processo in un punto fisso per diverse realizzazioni) produce una distribuzione di valori diversi.
*   **Stazionarietà al Primo Ordine:** La variabile aleatoria $X(n_0)$ possiede una funzione di densità di probabilità (pdf) $f_{X(n)}(x; n)$. Se tale pdf è indipendente dall'istante di campionamento $n$, il processo è definito **stazionario al primo ordine**.

**Esempio Pratico:**
Nel caso in esame, il processo è generato assumendo stazionarietà al primo ordine e una distribuzione marginale uniforme nell'intervallo $[-0.5, 0.5]$. La pdf è dunque:
$$f_{X(n)}(x) = \Pi(x - 0.5)$$

> [!IMPORTANT] Osservazione sulla Media
> Poiché la pdf è simmetrica rispetto all'origine, il valore atteso del processo è nullo:
> $$\mathbb{E}[X(n)] = \int_{-0.5}^{0.5} x \Pi(x - 0.5) \, dx = 0$$
> Il processo è pertanto a media identicamente nulla.

---

### Esempio: Processo Gaussiano Tempo-Discreto
Consideriamo un secondo esempio di processo tempo-discreto stazionario al primo ordine, caratterizzato da una pdf gaussiana:
$$f_{X(n)}(x) = \frac{1}{\sqrt{2\pi}} \exp \left[ -\frac{(x + 0.5)^2}{2} \right]$$

Questa espressione descrive una densità marginale con media $\mu = -0.5$ e varianza $\sigma^2 = 1$. Le figure sottostanti illustrano diverse realizzazioni del processo:

*(Inserire qui le immagini)*
*   **Figura 4:** Realizzazione Gaussiana 1
*   **Figura 5:** Realizzazione Gaussiana 2
*   **Figura 6:** Realizzazione Gaussiana 3

---

## Caratterizzazione del Secondo Ordine

La descrizione statistica di un processo può essere approfondita analizzando le relazioni tra campioni diversi:

1.  **Caratterizzazione al Primo Ordine:** Il processo è caratterizzato al primo ordine se è nota la pdf $f_{X(n)}(x; n)$ per ogni istante $n$. Se il processo è stazionario al primo ordine, tale pdf non dipende da $n$.
2.  **Caratterizzazione al Secondo Ordine:** Il processo è caratterizzato al secondo ordine se è nota la pdf congiunta di due campioni:
    $$f_{X(n_1), X(n_2)}(x_1, x_2; n_1, n_2), \quad \forall n_1, n_2$$
3.  **Stazionarietà al Secondo Ordine:** Un processo è definito stazionario al secondo ordine se la pdf congiunta dipende esclusivamente dalla differenza temporale $h$ tra i due campioni:
    $$f_{X(n_1), X(n_2)}(x_1, x_2; n_1, n_2) = f_{X(n_1 + h), X(n_2 + h)}(x_1, x_2; n_1, n_2 + h)$$

In termini intuitivi, un processo stazionario al secondo ordine presenta una caratterizzazione congiunta che è invariante rispetto a traslazioni temporali (atti di moto rigido). In altre parole, la statistica del processo dipende dalla "distanza" tra i punti e non dalla loro posizione assoluta nel tempo.

> [!NOTE] Relazione tra Stazionarietà al Primo e Secondo Ordine
> È fondamentale notare che ogni processo stazionario al secondo ordine è necessariamente stazionario al primo ordine. Tuttavia, la conversione non è reciproca: un processo può presentare una media costante (stazionarietà al primo ordine) pur avendo correlazioni tra campioni che variano nel tempo (mancanza di stazionarietà al secondo ordine).

Ecco una versione revisionata e formattata del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Caratterizzazione dei Processi Aleatori

## Definizione di Caratterizzazione Completa
Un processo aleatorio $X(n)$ è definito **completamente caratterizzato** se, per ogni intero $M$ e per ogni insieme di istanti arbitrari $\{n_1, \dots, n_M\}$, il vettore aleatorio:

$$ \mathbf{X} = [X(n_1), \dots, X(n_M)]^T $$

possiede una densità di probabilità $f_{\mathbf{X}}(x_1, \dots, x_M)$ nota.

## Stazionarietà e Indipendenza

### Stazionarietà in senso stretto (Strict-Sense Stationarity)
Un processo aleatorio è **stazionario in senso stretto di ordine $M$** se la sua densità di probabilità di ordine $M$ è invariante rispetto a una traslazione temporale $h$. Formalmente:

$$ f_{X(n_1), \dots, X(n_M)}(x_1, \dots, x_M; n_1, \dots, n_M) = f_{X(n_1+h), \dots, X(n_M+h)}(x_1, \dots, x_M; n_1+h, \dots, n_M+h) $$

> [!IMPORTANT]
> Un processo stazionario di ordine $M$ è necessariamente stazionario per ogni ordine $i \leq M$.

### Processi a Campioni Indipendenti (IID)
Un processo si definisce **indipendente** se, per ogni intero $M$, le componenti del vettore $\mathbf{X} = [X(n_1), \dots, X(n_M)]^T$ sono variabili aleatorie indipendenti. In questo caso, la densità di probabilità congiunta si scompone nel prodotto delle densità marginali:

$$ f_{X(n_1), \dots, X(n_M)}(x_1, \dots, x_M) = \prod_{i=1}^{M} f_{X(n_i)}(x_i) $$

## Processi Discreti

### Definizione Generale
Un **processo ampiezza discreto** (o semplicemente *processo discreto*) è un processo aleatorio le cui realizzazioni sono sequenze di valori appartenenti a un alfabeto discreto predefinito.

### Il Processo di Bernoulli
Un caso fondamentale è il **processo indipendente binario**, definito da $X(n) \in \{-1, 1\}$ con probabilità equiprobabili:
$$ \mathbb{P}\{X(n) = 1\} = \mathbb{P}\{X(n) = -1\} = \frac{1}{2} $$
Questo modello è comunemente noto come **Processo di Bernoulli**.

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/62faba250dc710ba5cb9fbd4a331bfdc4d2dc4cd5d3bd696b38454e5f14bc19a.jpg)
*Figura 7: Realizzazioni del processo di Bernoulli.*

### Esempio: Processo Quaternario
Un'estensione comune prevede l'utilizzo di un **alfabeto quaternario**, ad esempio $X(n) \in \{-2, -1, 1, 2\}$. In questo scenario, si assume che i livelli siano equiprobabili:
$$ \mathbb{P}\{X(n) = i\} = \frac{1}{4}, \quad \forall i \in \{-2, -1, 1, 2\} $$

Le realizzazioni di tale processo sono illustrate nella figura seguente:

![image](https://cdn-mineru.openxlab.org.cn/result/2026-06-27/b5f5d426-9c48-4e21-b90d-66928c562c74/9f7957aa1d5176320b74eb7c6ea5945937ed809d0cfc9354252211d9f644fc02.jpg)
*Figura 1: Realizzazioni di un processo quaternario.*

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e il rigore tecnico.

---

# Caratterizzazione dei Processi Discreti

Le definizioni relative ai processi continui sono estendibili ai **processi discreti**, con l'unica distinzione fondamentale che le densità di probabilità vengono sostituite dalle **funzioni di massa di probabilità** (PMF, *Probability Mass Function*).

> [!THEOREM] Definizione: Funzione di Massa di Probabilità (PMF)
> Intuitivamente, la PMF indica la probabilità che una variabile aleatoria discreta assuma un valore specifico. Ad esempio, nel lancio di un dado regolare, la PMF assegna il valore $1/6$ a ciascun numero dell'insieme $\{1, \dots, 6\}$.
>
> Formalmente, per una variabile aleatoria discreta $X$, la funzione di massa $p(x)$ è definita come:
> $$p(x) = P(X = x)$$

## Stazionarietà e Indipendenza

Un processo discreto si definisce **stazionario in senso stretto** se, per ogni intero $M \geq 1$, il vettore aleatorio $\mathbf{X} = [X(n_1), \dots, X(n_M)]^T$ soddisfa la seguente proprietà per ogni spostamento temporale $h$:

$$
\begin{aligned}
\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2, \dots, X(n_M) = x_M\} &= \mathbb{P}\{X(n_1 + h) = x_1, X(n_2 + h) = x_2, \dots, X(n_M + h) = x_M\}
\end{aligned}
$$

### Osservazioni chiave:
*   **Gerarchia della stazionarietà:** La stazionarietà di ordine $M$ implica necessariamente la stazionarietà di ogni ordine $k \leq M$.
*   **Marginali:** Un processo stazionario possiede una PMF marginale indipendente dal tempo.

Se un processo discreto è sia **stazionario** che **indipendente**, la probabilità congiunta si scompone nel prodotto delle probabilità marginali:

$$
\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2, \dots, X(n_M) = x_M\} = \prod_{i=1}^{M} \mathbb{P}\{X(n_i) = x_i\} = \prod_{i=1}^{M} p_X(x_i)
$$

dove $p_X(\cdot)$ è la PMF marginale, invariante rispetto al tempo.

---

# Caratterizzazione Sintetica dei Vettori Aleatori

Analogamente alle variabili aleatorie scalari, anche per i processi aleatori è possibile definire una **caratterizzazione sintetica**. Sebbene non sia possibile fornire una descrizione completa della distribuzione di ogni processo, è possibile identificare statistiche descrittive significative.

Mentre nel caso scalare la coppia $(\mu_X, \sigma_X^2)$ e nel caso delle coppie la quintupla $(m_{X}, \sigma_{X}, m_{Y}, \sigma_{Y}, \text{COV}(X,Y))$ offrono una sintesi utile del comportamento dei dati, per un vettore aleatorio $\mathbf{X} = [X_1, \dots, X_n]^T$ si utilizzano i seguenti parametri:

### 1. Media Statistica
Il vettore delle medie è definito come:
$$
\boldsymbol{\mu}_{\mathbf{X}} = \left(\mathbb{E}[X_1], \dots, \mathbb{E}[X_n]\right)^T
$$

### 2. Matrice di Covarianza
La **matrice di covarianza** $\mathbf{C}_X$ descrive la variabilità e le relazioni lineari tra le componenti del vettore. È definita come:
$$
\mathbf{C}_X = \mathbb{E}\left[ (\mathbf{X} - \boldsymbol{\mu}_{\mathbf{X}})(\mathbf{X} - \boldsymbol{\mu}_{\mathbf{X}})^T \right]
$$

In forma esplicita, la matrice è rappresentata come:
$$
\mathbf{C}_X = 
\begin{pmatrix} 
\sigma_{X_1}^2 & \text{COV}(X_1, X_2) & \dots & \text{COV}(X_1, X_n) \\ 
\text{COV}(X_2, X_1) & \sigma_{X_2}^2 & \dots & \text{COV}(X_2, X_n) \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\text{COV}(X_n, X_1) & \text{COV}(X_n, X_2) & \dots & \sigma_{X_n}^2 
\end{pmatrix}
$$

> [!IMPORTANT] Nota Tecnica
> La matrice di covarianza è per definizione **simmetrica** e **semidefinita positiva**, garantendo che le varianze sulla diagonale principale siano sempre non negative.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, corretto la notazione matematica (eliminando spazi superflui e migliorando la coerenza dei simboli) e strutturato il contenuto per una migliore leggibilità didattica.

---

# Processi Stazionari in Senso Lato (SSL)

Sebbene l'analisi si concentri sui processi a tempo discreto, le proprietà descritte sono valide anche per i processi a tempo continuo. Un processo $X(n) \in \mathcal{X}$ è definito **stazionario di secondo ordine** se soddisfa le seguenti condizioni:

1. La distribuzione di probabilità non dipende dal tempo:
   $$\mathbb{P}\{X(n) = x\} = p_X(x), \quad \forall x$$
2. La distribuzione congiunta è invariante rispetto a una traslazione temporale $h$:
   $$\mathbb{P}\{X(n_1) = x_1, X(n_2) = x_2\} = \mathbb{P}\{X(n_1 + h) = x_1, X(n_2 + h) = x_2\}$$

Da queste condizioni derivano due proprietà fondamentali:
- La media $\mu_X$ è costante nel tempo:
  $$\mu_X = \mathbb{E}[X(n)] = \sum_{x \in \mathcal{X}} x p_X(x)$$
- L'autocorrelazione dipende esclusivamente dalla differenza temporale $\tau = n_2 - n_1$:
  $$\mathbb{E}[X(n_1)X(n_2)] = \mathbb{E}[X(n_1+h)X(n_2+h)]$$

### Definizione di Stazionarietà in Senso Lato (SSL)
Un processo $X(t)$ (continuo o discreto), non necessariamente stazionario di secondo ordine, è detto **stazionario in senso lato** se soddisfa i seguenti requisiti:

*   **Media costante:** $\mathbb{E}[X(t)]$ non dipende dal tempo.
*   **Autocorrelazione invariante:** La funzione di autocorrelazione $R_X$ dipende solo dallo scostamento temporale:
    $$R_X(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)] = R_X(t_2 - t_1)$$

> [!IMPORTANT]
> Un processo è SSL se le sue statistiche di primo e secondo ordine sono invarianti rispetto a traslazioni temporali.

---

# Matrice di Covarianza per Processi SSL

Sia $X(t)$ un processo SSL e $\pmb{x} = [X_1, \dots, X_M]^T$ un vettore aleatorio $M$-dimensionale composto dai campioni del processo presi negli istanti $(t_1, \dots, t_M)$.

### Proprietà del Vettore di Campioni
Data la natura SSL del processo, le statistiche del vettore $\pmb{x}$ presentano le seguenti caratteristiche:

1.  **Vettore delle Medie:**
    $$\pmb{\mu} = \mathbb{E}[\pmb{x}] = \mu \mathbf{1}$$
    dove $\mu$ è lo scalare della media e $\mathbf{1}$ è un vettore di unità $M$-dimensionale.

2.  **Momenti del Processo:**
    Per la condizione SSL, le aspettative incrociate e le varianze sono definite come:
    $$\mathbb{E}[X_i X_j] = f(|i - j|)$$
    $$\mathbb{E}[X_i^2] = \overline{X^2}$$
    $$\operatorname{Var}(X_i) = \sigma_X^2 = \overline{X^2} - \mu^2$$

3.  **Matrice di Covarianza:**
    Definendo il coefficiente di correlazione $\rho_{i,j} = \frac{\operatorname{Cov}(X_i, X_j)}{\sigma_X^2}$, la matrice di covarianza $\mathbf{C}_{\pmb{x}}$ assume la forma:
    $$\mathbf{C}_{\pmb{x}} = \sigma_X^2 \begin{pmatrix} 1 & \rho_{1,2} & \rho_{1,3} & \dots & \rho_{1,M} \\ \rho_{1,2} & 1 & \rho_{2,3} & \dots & \rho_{2,M} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ \rho_{1,M} & \rho_{2,M} & \rho_{3,M} & \dots & 1 \end{pmatrix}$$

Per costruzione, la matrice di covarianza di un vettore estratto da un processo SSL è sempre **simmetrica**.

> [!NOTE]
> **Struttura di Toeplitz:** Se il passo di campionamento del processo è costante (ovvero $\Delta t = t_{i+1} - t_i$ è costante per ogni $i$), la matrice di covarianza assume una forma di **Toeplitz**, in cui ogni diagonale contiene elementi identici.

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica, il rigore formale e la fluidità della lettura.

---

# Analisi dei Processi Stocastici: Proprietà e Convergenze

## Esercizio: Semidefinitività della Matrice di Covarianza

> [!example] Esercizio 1
> Dimostrare che la **matrice di covarianza** $\Sigma$ è una matrice definita non negativa.
>
> *Suggerimento: Analizzare il prodotto quadratico tra un vettore arbitrario e la matrice di covarianza.*

### Definizione Preliminare
Si ricorda che una matrice $A \in \mathbb{R}^{M \times M}$ è definita non negativa se, per ogni vettore $x \in \mathbb{R}^M$, si verifica la condizione:
$$x^T A x \geq 0$$

### Dimostrazione
Consideriamo un vettore aleatorio $M$-dimensionale $X$ con media $\mu$ e matrice di covarianza $\Sigma$. Definiamo il prodotto quadratico $(X-\mu)^T \Sigma (X-\mu)$. Tale quantità è una variabile aleatoria scalare la cui aspettativa può essere espansa come segue:

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \mathbb{E}\left[\sum_{i=1}^M \sum_{j=1}^M (X_i - \mu_i) \Sigma_{ij} (X_j - \mu_j)\right]
$$

Utilizzando la linearità dell'operatore di aspettativa, possiamo scambiare il segno di sommatoria con l'integrale:

$$
\mathbb{E}[(X-\mu)^T \Sigma (X-\mu)] = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)]
$$

Poiché, per definizione, $\mathbb{E}[(X_i - \mu_i)(X_j - \mu_j)] = \Sigma_{ij}$, la derivazione si semplifica in:

$$
\sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij} \Sigma_{ij} = \sum_{i=1}^M \sum_{j=1}^M \Sigma_{ij}^2 \geq 0
$$

[!IMPORTANT]
**Conclusione:** Poiché la somma dei quadrati $\sum \Sigma_{ij}^2$ è sempre non negativa, ne consegue che la matrice di covarianza $\Sigma$ è definita non negativa.

---

## Estensione ai Processi Continui

Le proprietà derivate per i processi a ampiezza discreta sono estendibili ai **processi a ampiezza continua**. Dato un processo stazionario $X(t)$, la sua caratterizzazione è definita dalle seguenti funzioni:

1.  **Media:** $\mu(t) = \mathbb{E}[X(t)]$
2.  **Funzione di Autocorrelazione:** $R(t_1, t_2) = \mathbb{E}[X(t_1)X(t_2)]$

Le definizioni di stazionarietà in senso lato (WSS) e in senso stretto si applicano analogamente ai processi continui.

---

## Processi Gaussiani

Un processo $X(t)$ è definito **Gaussiano** se ogni suo campione di dimensione $M$ genera un vettore aleatorio $X$ che segue una distribuzione normale multivariata.

### Distribuzione di Probabilità
Dato un vettore aleatorio $X$ con media $\mu$ e matrice di covarianza $\Sigma$:
$$
\begin{cases} \mathbb{E}[X] = \mu \\ \text{Cov}(X) = \Sigma \end{cases}
$$
La funzione di densità di probabilità (PDF) è espressa in forma chiusa come:

$$
f(x) = \frac{1}{\sqrt{(2\pi)^M |\Sigma|}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right)
$$

dove $|\Sigma|$ indica il determinante della matrice di covarianza.

### Proprietà Fondamentali
*   **Relazione tra Stazionarietà:** La stazionarietà in senso lato implica la stazionarietà in senso stretto. In particolare, nel caso di stazionarietà in senso lato, la matrice di covarianza presenta una struttura **Toeplitz**.
*   **Chiusura per Trasformazioni Lineari:** Se $X \sim \mathcal{N}(\mu, \Sigma)$, allora la trasformazione lineare $AX + b$ segue la distribuzione:
    $$AX + b \sim \mathcal{N}(A\mu + b, A\Sigma A^T)$$
*   **Incorrelazione vs Indipendenza:** Per i processi Gaussiani, l'incorrelazione implica l'indipendenza statistica. Se un processo è incorrelato, la matrice di covarianza è diagonale: $\Sigma = \text{diag}(\sigma_1^2, \dots, \sigma_M^2)$. Sostituendo nella PDF, otteniamo il prodotto delle densità marginali:
    $$f(x) = \prod_{i=1}^M \frac{1}{\sqrt{2\pi\sigma_i^2}} \exp\left(-\frac{(x_i-\mu_i)^2}{2\sigma_i^2}\right)$$

---

## Tipi di Convergenza

Sia $\{X_n\}$ una successione di variabili aleatorie con densità $f_n(x)$. Definiamo la convergenza della successione verso un limite $X$ attraverso diverse modalità, ordinate per forza di implicazione:

1.  **Convergenza Quasi Certa (o con probabilità 1):** È la forma più forte di convergenza. Si verifica se:
    $$P(\lim_{n \to \infty} X_n = X) = 1$$
    dove $\Omega$ rappresenta lo spazio dei campioni dello spazio di probabilità sottostante.
2.  **Convergenza in Media Quadratica:** La successione converge se $\mathbb{E}[|X_n - X|^2] \to 0$.
3.  **Convergenza in Probabilità:** La probabilità che la differenza tra $X_n$ e $X$ superi una soglia $\epsilon$ tende a zero per ogni $\epsilon > 0$.
4.  **Convergenza in Distribuzione:** La forma più debole, dove la legge di probabilità della successione converge a quella del limite.

Ecco una versione revisionata del testo, ottimizzata per fluidità, rigore accademico e chiarezza didattica.

---

# Convergenza in Distribuzione

Si dice che una successione di variabili aleatorie $X_n$ converge in distribuzione a una variabile $X$, indicativamente $X_n \xrightarrow{d} X$, se la relativa funzione di ripartizione $F_n(x)$ soddisfa:

$$
\lim_{n \to \infty} F_n(x) = F(x)
$$

dove l'uguaglianza deve valere per ogni $x$ appartenente agli insiemi di continuità della funzione $F(x)$.

> [!theorem] Teorema della Mappatura Continua (*Continuous Mapping Theorem*)
> Siano $X_n$ e $X$ variabili aleatorie tali che $X_n \xrightarrow{d} X$. Se $g$ è una funzione continua, allora:
> $$
> g(X_n) \xrightarrow{d} g(X)
> $$

> [!theorem] Teorema di Continuità di Lévy
> Sia definita la **funzione generatrice dei momenti** (moment generating function, mgf):
> $$
> M_X(s) = \mathbb{E}[e^{sX}]
> $$
> per i valori di $s$ in cui l'integrale è definito. La convergenza puntuale delle funzioni $M_{X_n}(s)$ a $M_X(s)$ è equivalente alla convergenza in distribuzione $X_n \xrightarrow{d} X$.

## La Funzione Generatrice dei Momenti (mgf)

La funzione generatrice dei momenti $\Phi_X(s)$ possiede proprietà analitiche fondamentali per lo studio delle variabili aleatorie.

> [!quote] Proprietà di Continuità
> Se la densità $f_X$ è sommabile, la mgf definita da
> $$
> \Phi_X(s) = \int_{\mathbb{R}} e^{st} f_X(t) \, dt
> $$
> è una funzione continua di $s$ in ogni intervallo in cui l'integrale converge.

### Derivabilità e Sviluppo in Serie

Qualora i momenti di ordine $r$ esistano, la mgf è $r$-volte derivabile e le sue derivate valutate in $s=0$ restituiscono i momenti della variabile:

> [!theorem] Momenti e Derivate
> $$
> \Phi_X(0) = 1, \quad \Phi_X'(0) = \mathbb{E}[X], \quad \Phi_X''(0) = \mathbb{E}[X^2], \dots, \quad \Phi_X^{(r)}(0) = \mathbb{E}[X^r]
> $$

Sotto tali condizioni di esistenza, la mgf ammette lo sviluppo in serie di MacLaurin:

> [!example] Sviluppo in Serie della mgf
> $$
> \Phi_X(s) = \sum_{n=0}^{\infty} \frac{\mathbb{E}[X^n]}{n!} s^n
> $$
> 
> [!IMPORTANT]
> Questa espansione giustifica la denominazione di "funzione generatrice dei momenti": i coefficienti della serie sono direttamente proporzionali ai momenti della variabile aleatoria $X$.

---

# Elementi di Statistica Inferenziale

## Definizioni Fondamentali

Consideriamo un campione di dimensione $n$, rappresentato dal vettore $\mathbf{x} \in \mathbb{R}^n$. 
Assumiamo che tale campione sia il risultato di un esperimento casuale; ne consegue che un nuovo campionamento produrrebbe un set di risultati differente, indicato come $\mathbf{x}' \in \mathbb{R}^n$.

> [!theorem] Inferenza Statistica
> L'**inferenza statistica** è il processo mediante il quale si utilizzano i dati osservati per dedurre proprietà della distribuzione di probabilità sottostante. In sostanza, mira a identificare la legge probabilistica che governa la popolazione da cui sono estratti i campioni.
> 
> Si distingue nettamente l'inferenza dalla **statistica descrittiva**:
> *   **Statistica Descrittiva:** Analizza esclusivamente le proprietà intrinseche dei dati osservati (es. medie campionarie, varianze).
> *   **Statistica Inferenziale:** Estende le conclusioni dai dati campionari alla popolazione generale, basandosi su assunzioni probabilistiche.
> 
> Gli obiettivi primari dell'inferenza statistica sono:
> 1. **Test delle Ipotesi:** Valutare la validità di affermazioni riguardanti i parametri della popolazione.
> 2. **Stima dei Parametri:** Determinare valori puntuali o intervalli di confidenza per le caratteristiche ignote della distribuzione.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, uniformato la notazione matematica e migliorato la struttura didattica mantenendo il rigore richiesto.

---

# Analisi della Media Campionaria e Distribuzione Empirica

## 1. La media campionaria e le Leggi dei Grandi Numeri

Sia $\mathbf{x}^n \in \mathcal{X}^n \subseteq \mathbb{R}^n$ un insieme di dati osservati. La **media campionaria** è definita come:

$$
\bar{x}_n = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

Considerando $X^n$ come un campione casuale estratto da una popolazione, la **Legge dei Grandi Numeri** stabilisce che la media campionaria converge al valore atteso della popolazione:

$$
\frac{1}{n} \sum_{i=1}^{n} X_i \xrightarrow{n \to \infty} \mathbb{E}[X]
$$

La natura di tale convergenza dipende dalla legge statistica sottostante. In particolare, si distinguono tre forme principali:

> [!IMPORTANT] Tipi di Convergenza
> *   **Convergenza debole (in probabilità):** La probabilità che la media campionaria si discosti significativamente da $\mathbb{E}[X]$ tende a zero per $n$ sufficientemente grande.
> *   **Convergenza forte:** La probabilità che la media campionaria non converga a $\mathbb{E}[X]$ è nulla nel limite asintotico.
> *   **Convergenza in media quadratica (Mean-Square):** La varianza dell'errore tende a zero:
>     $$ \lim_{n \to \infty} \mathbb{E} \left[ \left(\bar{X}_n - \mathbb{E}[X]\right)^2 \right] = 0 $$

## 2. Rappresentazione tramite frequenze e densità

Assumiamo che lo spazio campionario $\mathcal{X} = \{a_1, \dots, a_M\}$ sia discreto e finito. La media campionaria può essere espressa come una somma pesata sulle frequenze relative:

$$
\bar{x}_n = \sum_{i=1}^{M} a_i f_n(a_i)
$$

dove $f_n(a_i)$ rappresenta la frazione di elementi nel campione che assumono il valore $a_i$. Se $X$ è una variabile casuale con funzione di massa di probabilità (pmf) $\{p_X(a_i)\}_{i=1}^M$, il suo valore atteso è:

$$
\mathbb{E}[X] = \sum_{i=1}^{M} a_i p_X(a_i)
$$

Da queste definizioni, segue la seguente disuguaglianza di errore:

$$
| \bar{x}_n - \mathbb{E}[X] | \leq \sum_{i=1}^{M} |a_i| \cdot |f_n(a_i) - p_X(a_i)|
$$

> [!NOTE] Inferenza Statistica
> Se si può dimostrare che $f_n(a_i) \to p_X(a_i)$ in un senso di convergenza appropriato, allora $\mathbf{x}^n$ può essere considerato un campione estratto da una popolazione governata dalla densità marginale $\{p_X(a_i)\}_{i=1}^M$.

## 3. La distribuzione empirica

Sia $\mathbf{x}^n$ un campione di $n$ variabili casuali i.i.d. con marginale $\{p_X(a_i)\}_{i=1}^M$ non noto a priori. La frequenza di occorrenza dell'evento $X_k = a_i$ è una variabile casuale. 

Sia $N_i$ il numero di volte in cui il valore $a_i$ appare nel campione di dimensione $n$. La distribuzione di $N_i$ segue una legge binomiale:

$$
\operatorname{Pr}\{N_i = k\} = \binom{n}{k} p_X(a_i)^k \left[ 1 - p_X(a_i) \right]^{n-k}
$$

Analizzando le proprietà del rapporto $N_i/n$, otteniamo:

$$
\mathbb{E}\left[ \frac{N_i}{n} \right] = p_X(a_i), \quad \operatorname{var}\left[ \frac{N_i}{n} \right] = \frac{p_X(a_i)(1 - p_X(a_i))}{n}
$$

Ne consegue che la frequenza relativa $N_i/n$ converge a $p_X(a_i)$ in media quadratica:

$$
\lim_{n \to \infty} \mathbb{E}\left[ \left( \frac{N_i}{n} - p_X(a_i) \right)^2 \right] = 0
$$

Ecco una versione revisionata del testo. Ho migliorato la fluidità sintattica, standardizzato il codice LaTeX e strutturato il contenuto per massimizzare la chiarezza didattica, mantenendo intatto il rigore matematico originale.

---

# Analisi della Convergenza Quasi Certa

## Derivazione della Probabilità di Frequenza
Sia $\{q(a_i)\}$ una funzione di massa di probabilità (pmf) definita su $\mathcal{X}$ che differisce dalla vera distribuzione $p_X(a_i)$ in almeno due elementi. Consideriamo la probabilità che il numero di occorrenze $N_i$ sia pari a $n q(a_i)$:

$$
\operatorname{Pr}\{N_i = n q(a_i)\} = \binom{n}{n q(a_i)} p_X(a_i)^{n q(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))}
$$

Utilizzando il limite per il coefficiente binomiale:

$$
\sqrt{\frac{n}{8k(n-k)}} \leq \binom{n}{k} 2^{-n H\left(\frac{k}{n}\right)} \leq \sqrt{\frac{n}{\pi k (n - k)}}
$$

Impostando $k = n q(a_i)$, otteniamo per $n$ sufficientemente grande:

$$
\sqrt{\frac{1}{8 n q(a_i) (1 - q(a_i))}} \leq \binom{n}{n q(a_i)} 2^{-n \left[ q(a_i) \log \frac{1}{q(a_i)} + (1 - q(a_i)) \log \frac{1}{1 - q(a_i)} \right]} \leq \sqrt{\frac{1}{\pi n q(a_i) (1 - q(a_i))}}
$$

Da cui si deduce la seguente asintotica:

$$
\binom{n}{n q(a_i)} \sim 2^{n H_2(q(a_i), 1 - q(a_i))}
$$

## Analisi Asintotica e Divergenza di Kullback-Leibler
Consideriamo un valore $a_j$ tale che $q(a_i) \neq p_X(a_i)$. Espandendo la probabilità per $n \to \infty$, si ottiene:

$$
\begin{aligned}
\operatorname{Pr}\{N_i = n q(a_i)\} &\sim 2^{n H_2(q(a_i), 1 - q(a_i))} p_X(a_i)^{n q(a_i)} [1 - p_X(a_i)]^{n(1 - q(a_i))} \\
&= 2^{n H_2(q(a_i), 1 - q(a_i))} 2^{n [q(a_i) \log p_X(a_i) + (1 - q(a_i)) \log (1 - p_X(a_i))]} \\
&= 2^{n \left[ q(a_i) \log \frac{p_X(a_i)}{q(a_i)} + (1 - q(a_i)) \log \frac{1 - p_X(a_i)}{1 - q(a_i)} \right]} \\
&= 2^{-n D_i}
\end{aligned}
$$

dove $D_i$ rappresenta la divergenza di Kullback-Leibler:

$$
D_i = q(a_i) \log \frac{q(a_i)}{p_X(a_i)} + (1 - q(a_i)) \log \frac{1 - q(a_i)}{1 - p_X(a_i)} > 0
$$

> [!IMPORTANT]
> **Conclusione:** La probabilità che la frequenza di occorrenza differisca dalla vera probabilità tende a zero esponenzialmente al crescere di $n$. Ciò implica che la frequenza campionaria converge quasi certamente: $f_n(a_i) \to p_X(a_i)$.

## Commenti e Proprietà Statistiche
Sia $\mathbf{x}^n \in \mathcal{X}^n$ un campione estratto da un vettore casuale $\mathbf{X}^n$ con pmf sconosciuta, dove $\mathcal{X} = \{a_1, \dots, a_M\}$. Definiamo le frequenze di occorrenza come:

$$
f_n(a_i) = \frac{\# \{ \text{elementi uguali a } a_i \}}{n}, \quad i = 1, \dots, M
$$

Le proprietà di convergenza garantiscono che:

$$
\operatorname{Pr}\left\{\lim_{n \to \infty} \frac{N_i}{n} = \lim_{n \to \infty} f_n(a_i)\right\} = 1
$$

Questa proprietà implica che qualsiasi altro campione $\mathbf{y}^n$ estratto dalla medesima popolazione mostrerà lo stesso comportamento statistico per $n \to \infty$. Più in generale, per ogni funzione $f(\cdot)$ applicata ai dati:

$$
\operatorname{Pr}\left\{\lim_{n \to \infty} f(\mathbf{X}^n) = \lim_{n \to \infty} f(\mathbf{x}^n)\right\} = 1
$$

Di conseguenza, la media campionaria converge con probabilità uno alla media della popolazione. In statistica inferenziale, questa proprietà è nota come **forte coerenza**.

> [!THEOREM] Forte Coerenza
> Un estimatore è definito *forte coerente* se converge quasi certamente (con probabilità 1) al valore vero del parametro che intende stimare all'aumentare della dimensione del campione $n$.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità sintattica, uniformato la notazione matematica e strutturato il contenuto per una migliore leggibilità didattica.

---

# Statistica Inferenziale

Il principio fondamentale della statistica inferenziale risiede nella capacità di dedurre le caratteristiche di una popolazione partendo dall'analisi di un campione sufficientemente ampio. L'obiettivo è identificare proprietà statistiche che ogni altro campione estratto dalla medesima popolazione dovrebbe, con alta probabilità, rispettare.

In molti contesti, è possibile integrare l'analisi dei dati con conoscenze pregresse (*a priori*). Ad esempio, si può assumere che il campione provenga da una popolazione la cui distribuzione è nota fino a un insieme di parametri ignoti. 

Formalmente, si assume che il campione sia estratto da una famiglia di distribuzioni indicizzata da un parametro $\theta$, il cui valore deve essere stimato.

> [!IMPORTANT]
> **Domanda centrale:** Come possiamo elaborare il dataset disponibile per inferire il valore del parametro $\theta$?

## Impostazione Bayesiana: Regola di Decisione

Sia $\mathbf{x}^n \in \mathcal{X}^n$ un dataset costituito da una realizzazione del vettore casuale $\mathbf{X}^n$. Supponiamo che, a seconda dello stato della natura, i dati possano essere generati da una delle $M$ diverse leggi di probabilità.

Definiamo quindi un insieme di $M$ ipotesi mutuamente esclusive $\{H_i\}_{i=1}^M$, dove ogni ipotesi $H_i$ definisce una specifica legge condizionale per il set di dati:

$$p_{\mathbf{X}^n}(\mathbf{x}^n \mid H_i), \quad i = 1, \dots, M$$

Si assuma che il vettore casuale $\mathbf{X}^n$ sia estratto da una famiglia di distribuzioni con funzione di probabilità (pmf) $p_{\mathbf{X}^n|\Theta}(\mathbf{x}^n \mid \theta)$, dove $\theta$ è il parametro ignoto. Inoltre, siano assegnate le probabilità a priori $\{P(H_i)\}_{i=1}^M$ per ciascuno stato della natura.

Una **regola di decisione** è definita come una mappa:

$$D: \mathbf{x}^n \in \mathcal{X}^n \Longrightarrow D(\mathbf{x}^n) \in \{1, \dots, M\}$$

tale da determinare quale dei possibili stati della natura sia quello effettivamente in vigore sulla base delle osservazioni.

## Costi Bayesiani e Rischio

Per valutare l'efficacia di una regola di decisione, si definisce la matrice di costo $M \times M$:

$$\mathbf{C} = \begin{bmatrix} 
C_{1,1} & C_{1,2} & \dots & C_{1,M} \\
\vdots & \vdots & \ddots & \vdots \\
C_{M,1} & C_{M,2} & \dots & C_{M,M} 
\end{bmatrix}$$

In cui $C_{i,j}$ rappresenta il costo associato all'evento in cui la regola di decisione assegna l'ipotesi $i$ (ovvero $D(\mathbf{x}^n) = i$) mentre lo stato della natura è effettivamente $H_j$.

Il **rischio Bayesiano medio** $\mathcal{R}$ è definito come:

$$\mathcal{R} = \sum_{i=1}^M \sum_{j=1}^M C_{i,j} \mathbb{P}\left(D(\mathbf{X}^n) = i, H = H_j\right)$$

Data una matrice di costo $\mathbf{C}$, una regola di decisione è definita **ottimale** se minimizza il rischio Bayesiano $\mathcal{R}$.

> [!NOTE]
> **Osservazione:** Se la matrice di costo è definita in modo che $C_{k,k} = 0$ (nessun costo per la decisione corretta) e $C_{k,j} = 1$ per $j \neq k$ (costo unitario per ogni errore), il rischio Bayesiano medio coincide con la probabilità di commettere un errore di classificazione:
>
> $$R = \sum_{k=1}^M P(H_k) \sum_{j=1}^M P(D(\mathbf{X}^n)=j \mid H_k) C_{k,j}$$

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e il rigore tecnico.

---

# Problema di Classificazione Binaria

Si consideri un problema di classificazione binaria in cui $K=2$. Definiamo le matrici di costo tali che $C_{1,1} = C_{2,2} = 0$ (costo nullo per la decisione corretta) e $C_{1,2} = C_{2,1} = 1$ (costo unitario per l'errore). In questo contesto, la probabilità di errore totale $\mathbb{P}(e)$ è espressa come:

$$
\mathcal{R} = \mathbb{P}\{D(\mathbf{X}^n) = 2, H_1\} + \mathbb{P}\{D(\mathbf{X}^n) = 1, H_2\} = \mathbb{P}(e)
$$

### Definizione della Regola di Decisione
Progettare una regola di decisione consiste nel determinare una partizione dello spazio campionario $\mathcal{X}^n$ in due sottoinsiemi disgiunti, $\Omega_1$ e $\Omega_2$, tali che la funzione di decisione $D(\mathbf{x}^n)$ sia definita come:

$$
D(\mathbf{x}^n) = \begin{cases} 1 & \text{se } \mathbf{x}^n \in \Omega_1 \\ 2 & \text{se } \mathbf{x}^n \in \Omega_2 \end{cases}
$$

La probabilità di errore corrispondente può quindi essere riscritta come:

$$
\mathbb{P}(e) = \mathbb{P}\{\mathbf{X}^n \in \Omega_1, H_2\} + \mathbb{P}\{\mathbf{X}^n \in \Omega_2, H_1\}
$$

L'obiettivo è determinare la legge di decisione ottimale, ovvero quella che minimizza $\mathbb{P}(e)$.

# Classificazione Binaria: Dati Discreti

Assumiamo che le osservazioni $\mathbf{X}^n$ siano un **vettore casuale discreto** caratterizzato dalle funzioni di probabilità (pmf) condizionali $p_{\mathbf{X}^n}(\mathbf{x}^n | H_i)$.

La probabilità di errore può essere espressa in termini di probabilità corrette:

$$
\mathbb{P}(e) = 1 - \left[ \sum_{\mathbf{x}^n \in \Omega_1} p(H_1) p_{\mathbf{X}^n}(\mathbf{x}^n | H_1) + \sum_{\mathbf{x}^n \in \Omega_2} p(H_2) p_{\mathbf{X}^n}(\mathbf{x}^n | H_2) \right]
$$

Per minimizzare $\mathbb{P}(e)$, è necessario massimizzare il termine tra parentesi. Tale obiettivo viene raggiunto definendo la regola di decisione ottimale come:

$$
\mathbf{x}^n \in \Omega_i \iff p_{\mathbf{X}^n}(\mathbf{x}^n | H_1) P(H_1) > p_{\mathbf{X}^n}(\mathbf{x}^n | H_2) P(H_2)
$$

Questa condizione può essere riformulata in termini di **rapporto di verosimiglianza**:

$$
L(\mathbf{x}^n) = \frac{p_{\mathbf{X}^n}(\mathbf{x}^n | H_1)}{p_{\mathbf{X}^n}(\mathbf{x}^n | H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta
$$

> [!IMPORTANT] Concetto Chiave
> La quantità $L(\mathbf{x}^n)$ definita sul lato sinistro (LHS) è il **rapporto di verosimiglianza** (*likelihood ratio*) tra le due ipotesi alternative. Il valore critico $\eta$ rappresenta la soglia di decisione ottimale basata sulle probabilità a priori delle ipotesi.

Ecco una versione revisionata del testo. Ho migliorato la fluidità sintattica, uniformato la notazione matematica e strutturato il contenuto per una migliore leggibilità didattica.

---

## Analisi della Regola di Decisione

La regola di decisione precedentemente definita è nota come **Massima Probabilità a Posteriori (MAP)**. Tale definizione deriva direttamente dalla legge di Bayes:

$$
\mathbb{P}(H = H_i \mid \boldsymbol{X}^n = \boldsymbol{x}^n) = \frac{\mathbb{P}(\boldsymbol{X}^n = \boldsymbol{x}^n \mid H_i) P(H_i)}{\mathbb{P}(\boldsymbol{X}^n = \boldsymbol{x}^n)} = \frac{p_{\boldsymbol{X}^n}(\boldsymbol{x}^n \mid H_i) P(H_i)}{p_{\boldsymbol{X}^n}(\boldsymbol{x}^n)}
$$

L'espressione dimostra che la regola seleziona l'ipotesi la cui probabilità *a posteriori*, condizionata ai dati osservati, è massima.

### Casi Speciali e Probabilità di Errore
Nel caso specifico in cui le due ipotesi siano equiprobabili ($P(H_1) = P(H_2)$), la soglia di decisione diventa $\eta = 1$ e la regola coincide con il criterio di **Massima Verosimiglianza (ML)**.

Le probabilità di errore condizionali sono definite come:
$$
P(e \mid H_1) = \mathbb{P}(L(\boldsymbol{X}^n) < \eta \mid H_1), \quad P(e \mid H_2) = \mathbb{P}(L(\boldsymbol{X}^n) > \eta \mid H_2)
$$

Di conseguenza, la probabilità di errore totale è data dalla combinazione lineare:
$$
\mathbb{P}(e) = P(H_1) P(e \mid H_1) + P(H_2) P(e \mid H_2)
$$

---

## Esempio: Classificazione di Sorgenti Binarie

> [!EXAMPLE] Esempio 1: Classificazione di sorgenti binarie
> Si considerino osservazioni $\boldsymbol{X}^n$ come variabili binarie i.i.d. provenienti da una delle due sorgenti con probabilità uguali. Le probabilità di successo per le due sorgenti sono $p_1$ e $p_2$, con $p_1 > p_2$.
> 
> La funzione di verosimiglianza è espressa come:
> $$
> p_{\boldsymbol{X}^n}(\boldsymbol{x}^n \mid H_i) = p_i^{w_H(\boldsymbol{x}^n)} (1 - p_i)^{n - w_H(\boldsymbol{x}^n)}
> $$
> dove $w_H(\boldsymbol{x}^n)$ rappresenta il **peso di Hamming** della sequenza osservata $\boldsymbol{x}^n$ (ovvero il numero di bit pari a 1).
>
> Il test per la minimizzazione della probabilità di errore è definito da:
> $$
> \left( \frac{p_1}{p_2} \right)^{w_H(\boldsymbol{x}^n)} \left[ \frac{1 - p_1}{1 - p_2} \right]^{n - w_H(\boldsymbol{x}^n)} \underset{H_2}{\overset{H_1}{\gtrless}} 1
> $$
>
> Applicando il logaritmo naturale, la condizione diventa:
> $$
> w_H(\boldsymbol{x}^n) \ln\left( \frac{p_1}{p_2} \right) + (n - w_H(\boldsymbol{x}^n)) \ln\left( \frac{1 - p_1}{1 - p_2} \right) \underset{H_2}{\overset{H_1}{\gtrless}} 0
> $$
>
> Semplificando l'espressione, otteniamo la forma finale del test:
> $$
> w_H(\boldsymbol{x}^n) \left[ \ln\left( \frac{p_1}{1 - p_1} \cdot \frac{1 - p_2}{p_2} \right) \right] \underset{H_2}{\overset{H_1}{\gtrless}} n \ln\left( \frac{1 - p_2}{1 - p_1} \right)
> $$

---

## Valutazione delle Prestazioni

Poiché $p_1 > p_2$, tutti i termini logaritmici risultano non negativi. Il test può essere riscritto in una forma standardizzata:
$$
w_H(\boldsymbol{x}^n) \underset{H_2}{\overset{H_1}{\gtrless}} n \frac{\ln\left( \frac{1 - p_2}{1 - p_1} \right)}{\ln\left( \frac{p_1}{1 - p_1} \cdot \frac{1 - p_2}{p_2} \right)} = \eta_1
$$

Assumendo che $\eta_1$ non sia un numero intero, le probabilità di errore condizionali sotto le due ipotesi alternative sono calcolate tramite la distribuzione binomiale:

*   **Sotto $H_1$:**
    $$
    \mathbb{P}(e \mid H_1) = \mathbb{P}(w_H(\boldsymbol{X}^n) < \eta_1 \mid H_1) = \sum_{i=0}^{\lfloor \eta_1 \rfloor} \binom{n}{i} p_1^i (1 - p_1)^{n-i}
    $$

*   **Sotto $H_2$:**
    $$
    \mathbb{P}(e \mid H_2) = \mathbb{P}(w_H(\boldsymbol{X}^n) > \eta_1 \mid H_2) = \sum_{i=\lfloor \eta_1 \rfloor + 1}^{n} \binom{n}{i} p_2^i (1 - p_2)^{n-i}
    $$

La probabilità di errore media, assumendo ipotesi equiprobabili, è:
$$
\mathbb{P}(e) = \frac{1}{2} \mathbb{P}(e \mid H_1) + \frac{1}{2} \mathbb{P}(e \mid H_2)
$$

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e la fluidità didattica, mantenendo il rigore matematico richiesto.

---

## Classificazione Binaria: Legge dei Dati Continui

Consideriamo un modello in cui i dati possono essere estratti da $M$ possibili leggi di probabilità continue. Sia $\{ f_{\mathbf{X}^n | H_i}(\mathbf{x}^n | H_i) \}_{i=1}^M$ l'insieme delle funzioni di densità di probabilità (PDF) condizionali candidate per ogni ipotesi $H_i$. 

A differenza del caso discreto, la probabilità associata a un intervallo $\Omega_i$ è definita dall'integrale della densità:

$$
\mathbb{P}\{\mathbf{X}^n \in \Omega_1 | H_1\} = \int_{\Omega_1} f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1) d\mathbf{x}^n, \quad \mathbb{P}\{\mathbf{X}^n \in \Omega_2 | H_2\} = \int_{\Omega_2} f_{\mathbf{X}^n | H_2}(\mathbf{x}^n | H_2) d\mathbf{x}^n
$$

Seguendo la logica del caso discreto, il test di probabilità di errore minima (MAP - *Maximum A Posteriori*) è definito dalla condizione:

$$
\mathbf{x}^n \in \Omega_i \iff f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1) P(H_1) > f_{\mathbf{X}^n | H_2}(\mathbf{x}^n | H_2) P(H_2)
$$

Questa condizione può essere riscritta in termini di **rapporto di verosimiglianza** (likelihood ratio):

$$
L(\mathbf{x}^n) = \frac{f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)}{f_{\mathbf{X}^n | H_2}(\mathbf{x}^n | H_2})} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta
$$

> [!IMPORTANT]
> La quantità $L(\mathbf{x}^n)$ rappresenta il rapporto di verosimiglianza tra le due ipotesi alternative e costituisce la base per la decisione statistica.

---

## Esempio: Test della Media di una Popolazione Gaussiana

> [!example] Esempio 2 (Test della media di una popolazione Gaussiana)
>
> Si assuma che il set di dati $\mathbf{x}^n$ sia una realizzazione di un vettore casuale gaussiano indipendente, i cui elementi condividono la stessa varianza $\sigma^2$, ma presentano medie distinte $\mu_1$ e $\mu_2$, con $\mu_2 < \mu_1$.
>
> Data la funzione di densità:
> $$f_{\mathbf{X}^n | H_i}(\mathbf{x}^n | H_i) = \prod_{k=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x_k - \mu_i)^2}{2\sigma^2}}$$
>
> Il test ottimo è espresso dal rapporto di verosimiglianza:
> $$L(\mathbf{x}^n) = \frac{f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)}{f_{\mathbf{X}^n | H_2}(\mathbf{x}^n | H_2})} = e^{\frac{\sum_{k=1}^n (x_k - \mu_2)^2 - (x_k - \mu_1)^2}{2\sigma^2}} \underset{H_2}{\overset{H_1}{\gtrless}} 1$$
>
> Applicando il logaritmo naturale a entrambi i membri e semplificando l'espressione, otteniamo il test equivalente:
> $$\frac{1}{n} \sum_{k=1}^n x_k \underset{H_2}{\overset{H_1}{\gtrless}} \frac{\mu_1 + \mu_2}{2} = \eta$$
>
> In questo contesto, la quantità $\sum x_k$ è definita come una **statistica sufficiente**, poiché contiene tutta l'informazione necessaria dal set di dati per il parametro di interesse.

Ecco la versione revisionata del testo, ottimizzata per chiarezza accademica, fluidità e rigore tecnico.

---

# Valutazione delle prestazioni

Sotto l'ipotesi $H_j$, la statistica del test definita da 
$$Z_n = \frac{1}{n} \sum_{i=1}^n X_i$$
segue una distribuzione Gaussiana con media e varianza rispettivamente pari a:

$$\mathbb{E}[Z_n | H_j] = \mu_j, \quad \sigma_{Z_n}^2 = \frac{\sigma^2}{n}$$

Sulla base di tali parametri, le probabilità di errore condizionali sono espresse come segue:

*   **Errore di Tipo I (sotto $H_1$):**
    $$\mathbb{P}(e | H_1) = \mathbb{P}(Z_n < \eta | H_1) = 1 - Q\left(\frac{\eta - \mu_1}{\sigma_{Z_n}}\right) = 1 - Q\left(\sqrt{n} \frac{\mu_2 - \mu_1}{2\sigma}\right)$$

*   **Errore di Tipo II (sotto $H_2$):**
    $$\mathbb{P}(e | H_2) = \mathbb{P}(Z_n > \eta | H_2) = Q\left(\frac{\eta - \mu_2}{\sigma_{Z_n}}\right) = Q\left(\sqrt{n} \frac{\mu_1 - \mu_2}{2\sigma}\right)$$

Assumendo che $\mu_1 - \mu_2 > 0$, si ottiene la simmetria delle probabilità di errore:
$$\mathbb{P}(e | H_1) = \mathbb{P}(e | H_2) = Q\left(\sqrt{n} \frac{\mu_1 - \mu_2}{2\sigma}\right)$$

Di conseguenza, la probabilità totale di errore $\mathbb{P}(e)$ è data da:
$$\mathbb{P}(e) = Q\left(\sqrt{n} \frac{\mu_1 - \mu_2}{2\sigma}\right) \xrightarrow{n \to \infty} 0$$

> [!IMPORTANT]
> **Conclusione:** La probabilità di errore decade esponenzialmente al crescere della dimensione del campione $n$, garantendo la convergenza del test.

---

# Introduzione al Test di Ipotesi

In molti scenari applicativi, è necessario prendere una decisione tra due ipotesi alternative senza poter definire formalmente una matrice di costo $C$ o assegnare probabilità a priori affidabili. 

Tali situazioni sono comuni in diversi ambiti critici, tra cui:
*   **Sicurezza:** Rilevamento precoce di minacce in aree pattugliate;
*   **Cybersecurity:** Identificazione di intrusioni in server o domini protetti;
*   **Automazione Veicolare:** Rilevamento e localizzazione di ostacoli nei sistemi *Advanced Driver Assistance Systems* (ADAS);
*   **Gestione del Traffico:** Controllo e monitoraggio del traffico aereo;
*   **Difesa:** Numerose applicazioni in ambito militare.

In questi contesti, risulta spesso impraticabile quantificare il costo economico o sociale di un errore di giudizio sullo "stato della natura" (ovvero la distinzione tra "condizioni normali" e "presenza di anomalie"). Analogamente, l'assegnazione di una probabilità a priori alla presenza di anomalie nel set di dati è spesso considerata trascurabile o non determinabile con precisione.

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica, la fluidità espositiva e il rigore matematico.

---

# Fondamenti del Test di Ipotesi

## Definizioni Preliminari

> [!theorem] Ipotesi Nulla ($H_0$)
> L'**ipotesi nulla**, denotata con $H_0$, rappresenta l'assunzione di base secondo cui il set di dati osservati $\mathbf{x}^n$ è una realizzazione di un vettore casuale con una distribuzione condizionale nota. Tale distribuzione è espressa dalla funzione di probabilità (pmf) o densità di probabilità (pdf):
> $$p_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0) \quad \text{o} \quad f_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0)$$

L'obiettivo del test di ipotesi è determinare se, dati i dati osservati $\mathbf{x}^n$, sia necessario rifiutare $H_0$ a favore di un'ipotesi alternativa $H_1$, caratterizzata da una legge di probabilità differente $p_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)$ o $f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)$.

In un contesto di classificazione binaria, il dominio $\mathcal{X}^n$ viene partizionato in due regioni di decisione. Si noti che, a differenza del framework bayesiano, l'approccio frequentista non richiede la conoscenza delle probabilità a priori per definire le regole di decisione.

### Parametri del Test
Per progettare una regola di decisione (test), si definiscono i seguenti parametri fondamentali:

> [!theorem] Errore di Tipo I ($\alpha$)
> L'**errore di tipo I**, o probabilità di falso allarme, è la probabilità di rifiutare $H_0$ quando essa è vera. È definito come:
> $$ \mathbb{P}\{D(\mathbf{X}^n) = 1 | H_0\} = \begin{cases} \int_{\Omega_1} f_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0) d\mathbf{x}^n & \text{Dati Continui} \\ \sum_{\mathbf{x}^n \in \Omega_1} p_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0) & \text{Dati Discreti} \end{cases} $$

> [!theorem] Potenza del Test ($1 - \beta$)
> La **potenza del test** rappresenta la capacità di rifiutare correttamente $H_0$ quando essa è falsa. È definita come:
> $$ 1 - \beta = \mathbb{P}\{D(\mathbf{X}^n) = 1 | H_1\} = \begin{cases} \int_{\Omega_1} f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1) d\mathbf{x}^n & \text{Dati Continui} \\ \sum_{\mathbf{x}^n \in \Omega_1} p_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1) & \text{Dati Discreti} \end{cases} $$

---

## Il Test di Neyman-Pearson

Il criterio di Neyman-Pearson fornisce la regola di decisione ottima attraverso il seguente problema di ottimizzazione vincolata:

$$
\text{Massimizzare } (1 - \beta) \quad \text{soggetto a} \quad \mathbb{P}\{D(\mathbf{X}^n) = 1 | H_0\} \leq \alpha
$$

Il **Lemma di Neyman-Pearson** garantisce l'esistenza di una soluzione a tale problema, la quale identifica il **Test del Rapporto di Verosimiglianza** (*Likelihood Ratio Test*). La regola di decisione è definita come:

$$
L(\mathbf{x}^n) \underset{H_0}{\overset{H_1}{\gtrless}} \eta L(\mathbf{x}^n) = \begin{cases} \frac{f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)}{f_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0)} & \text{Dati Continui} \\ \frac{p_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)}{p_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0)} & \text{Dati Discreti} \end{cases}
$$

La soglia $\eta$ viene determinata risolvendo l'equazione:
$$ \mathbb{P}\{L(\mathbf{X}^n) > \eta | H_0\} = \alpha $$

> [!quote] Osservazione Didattica
> Poiché l'applicazione di una funzione monotonicamente crescente non altera l'ordine delle disuguaglianze, è possibile applicare il logaritmo naturale al rapporto di verosimiglianza senza perdere l'ottimalità del test. Si definisce così la *log-likelihood*:
> $$\Lambda(\mathbf{x}^n) = \ln L(\mathbf{x}^n)$$
> Il confronto avviene quindi rispetto a una nuova soglia determinata analiticamente.

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e il rigore tecnico.

---

# Test della media per popolazioni Gaussiane

## Definizione del problema
Consideriamo un modello in cui le osservazioni $X_i$ sono variabili casuali indipendenti e identicamente distribuite (iid) seguenti una distribuzione Gaussiana. Le ipotesi di test sono definite come segue:

*   **Ipotesi Nulla ($H_0$):** $X_i \sim \mathcal{N}(0, \sigma^2)$
*   **Ipotesi Alternativa ($H_1$):** $X_i \sim \mathcal{N}(\mu, \sigma^2)$

## Derivazione del test del rapporto di verosimiglianza
Il rapporto di verosimiglianza (Likelihood Ratio Test) per il campione $\mathbf{x}^n$ è espresso come:

$$L(\mathbf{x}^n) = \frac{f_{\mathbf{X}^n | H_1}(\mathbf{x}^n | H_1)}{f_{\mathbf{X}^n | H_0}(\mathbf{x}^n | H_0)} = \exp\left( \frac{\sum_{k=1}^n (x_k - \mu)^2 - x_k^2}{2\sigma^2} \right) \underset{H_0}{\overset{H_1}{\gtrless}} \eta$$

dove $\eta$ è la soglia di decisione. Applicando il logaritmo naturale a entrambi i membri, semplificando l'espressione e assorbendo le costanti indipendenti dai dati in una nuova soglia $\eta'$, otteniamo la statistica del test equivalente:

$$\frac{1}{n} \sum_{i=1}^n x_i \underset{H_0}{\overset{H_1}{\gtrless}} \eta'$$

La soglia $\eta'$ viene determinata in modo da garantire che la probabilità di errore di tipo I sia pari al livello di significatività $\alpha$ predefinito.

## Analisi delle prestazioni del test

### Determinazione della soglia
Sotto l'ipotesi nulla $H_0$, la statistica del test segue una distribuzione $\mathcal{N}(0, \sigma^2/n)$. Pertanto, la soglia $\eta'$ è calcolata come:

$$\mathbb{P} \left\{ \frac{1}{n} \sum_{i=1}^n X_i > \eta' \mid H_0 \right\} = Q\left( \frac{\sqrt{n}\eta'}{\sigma} \right) = \alpha \implies \eta' = \frac{\sigma}{\sqrt{n}} Q^{-1}(\alpha)$$

dove $Q(\cdot)$ denota la funzione di ripartizione della distribuzione normale standard (o la sua complementare, a seconda della convenzione adottata).

### Calcolo della potenza
La potenza del test ($1-\beta$) rappresenta la probabilità di rifiutare correttamente $H_0$ quando $H_1$ è vera. Sotto $H_1$, la statistica segue una distribuzione $\mathcal{N}(\mu, \sigma^2/n)$. La potenza è dunque:

$$1 - \beta = \mathbb{P} \left\{ \frac{1}{n} \sum_{i=1}^n X_i > \eta' \mid H_1 \right\} = Q\left( \sqrt{n} \frac{\eta' - \mu}{\sigma} \right)$$

### Comportamento asintotico
Si osserva che, per $n \to \infty$, la soglia $\eta'$ tende a zero per ogni $\alpha$ fissato. Di conseguenza:

$$\lim_{n \to \infty} (1 - \beta) = \lim_{n \to \infty} Q\left( \sqrt{n} \frac{\eta'(n) - \mu}{\sigma} \right) = 1$$

> [!IMPORTANT]
> **Conclusione:** Nel limite asintotico ($n \to \infty$), il test converge alla prestazione ideale, dove la probabilità di errore di tipo I rimane $\alpha$ e la potenza del test tende a $1$.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, rimosso le ridondanze nei simboli LaTeX (pulendo i comandi superflui) e strutturato il contenuto per una migliore leggibilità didattica.

---

# Stima dei Parametri: Generalità

Sia $\mathbf{X}^n \in \mathcal{X}^n$ un dataset costituito da una realizzazione del vettore casuale $\mathbf{X}^n$. Assumiamo che tale vettore sia estratto da una famiglia di distribuzioni caratterizzate dalla funzione di probabilità (pmf) o densità di probabilità (pdf):
$$p_{\mathbf{X}^n|\Theta}(\mathbf{x}^n | \theta) \quad \text{oppure} \quad f_{\mathbf{X}^n|\Theta}(\mathbf{x}^n | \theta)$$
dove il parametro $\theta$ è sconosciuto.

### Natura del Parametro $\theta$
Il parametro $\theta$ può essere interpretato in due modi a seconda del framework adottato:
1. **Impostazione Bayesiana:** $\theta$ è una realizzazione di una variabile casuale continua $\Theta$, con una distribuzione marginale nota $f_{\Theta}(\theta)$.
2. **Impostazione Frequentista:** $\theta$ è una quantità deterministica sconosciuta che assume valori in un insieme continuo (o discreto).

### Il Problema della Stima
L'obiettivo principale è determinare come stimare $\theta$ sulla base del campione raccolto $\mathbf{x}^n$. Nell'impostazione Bayesiana, l'applicazione diretta della regola di Bayes fornisce la distribuzione a posteriori:

$$f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n) = \frac{f_{\mathbf{X}^n|\Theta}(\mathbf{x}^n | \theta) f_{\Theta}(\theta)}{f_{\mathbf{X}^n}(\mathbf{x}^n)}$$

dove la densità marginale $f_{\mathbf{X}^n}(\mathbf{x}^n)$ è definita dall'integrale:
$$f_{\mathbf{X}^n}(\mathbf{x}^n) = \int f_{\mathbf{X}^n|\Theta}(\mathbf{x}^n | \theta) f_{\Theta}(\theta) d\theta$$

> [!IMPORTANT] Osservazione
> Se $\Theta$ è una variabile discreta, il problema di stima si riduce a un problema di **classificazione**. L'equazione sopra descrive la probabilità che il parametro appartenga a una determinata classe data l'osservazione.

---

# Teoria della Stima dei Parametri

> [!theorem] Definizione: Estimatore
> Un **estimatore** del parametro $\theta$ è una variabile casuale $\widehat{\Theta}(\mathbf{X}^n)$ — le cui realizzazioni sono indicate come $\hat{\theta}(\mathbf{x}^n)$ — che fornisce una stima del valore di $\theta$ basandosi sull'osservazione $\mathbf{x}^n \in \mathcal{X}^n$.

### Il Bayes Risk
Per progettare un estimatore efficace, definiamo il **Bayes Risk** medio $\mathcal{R}$, espresso come l'aspettativa della funzione di costo $C(\cdot)$:

$$\mathcal{R} = \mathbb{E}\left[ C(\widehat{\Theta}(\mathbf{X}^n) - \Theta) \right] = \mathbb{E}_{\mathbf{X}^n} \left[ \mathbb{E} \left[ C(\widehat{\Theta}(\mathbf{X}^n) - \Theta) \mid \mathbf{X}^n \right] \right]$$

dove $C(\theta, \hat{\theta})$ rappresenta una funzione di costo adeguatamente definita (es. errore quadratico medio).

### Estimatore Ottimo
Un estimatore è definito come **ottimo** se minimizza il Bayes Risk:

$$\widehat{\Theta}_{\text{opt}}(\mathbf{X}^n) = \arg \min_{\widehat{\Theta}} \mathbb{E}\left[ C(\widehat{\Theta}(\mathbf{X}^n) - \Theta) \right]$$

Espandendo l'aspettativa in funzione della distribuzione marginale e della densità a posteriori, otteniamo:

$$\mathcal{R} = \sum_{\mathbf{x}^n \in \mathcal{X}^n} p_{\mathbf{X}^n}(\mathbf{x}^n) \int C(\hat{\theta}(\mathbf{x}^n) - \theta) f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n) d\theta$$

Di conseguenza, la stima Bayes-ottimale per un campione osservato $\mathbf{x}^n$ è data dal valore che minimizza l'integrale sulla densità a posteriori:

$$\hat{\theta}(\mathbf{x}^n) = \arg \min_{\hat{\theta}} \int C(\hat{\theta} - \theta) f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n) d\theta$$

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, corretto le incongruenze nei simboli (come l'uso di $\beta$ e $\theta$) e strutturato il contenuto per una migliore leggibilità accademica.

---

# Estimatori Bayesiani: MMSE e MAP

## 1. Estimatore del Minimo Errore Quadratico Medio (MMSE)

Si consideri la funzione di costo quadratica definita da:
$$C(\hat{\theta}, \theta) = (\hat{\theta} - \theta)^2$$

L'estimatore Bayes-ottimale $\hat{\theta}(\mathbf{x}^n)$ è ottenuto minimizzando il rischio atteso. Tale valore corrisponde alla soluzione dell'equazione derivata dalla minimizzazione dell'integrale del rischio:

$$
\frac{\partial}{\partial \hat{\theta}(\mathbf{x}^n)} \int (\hat{\theta}(\mathbf{x}^n) - \theta)^2 f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n) \, d\theta = 0
$$

Risolvendo l'equazione, otteniamo la stima:

$$
\hat{\theta}(\mathbf{x}^n) = \int \theta f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n) \, d\theta = \mathbb{E}[\Theta | \mathbf{X}^n = \mathbf{x}^n]
$$

> [!IMPORTANT]
> La stima MMSE corrisponde esattamente all'**aspettativa condizionata** del parametro dato l'osservato. Tale soluzione garantisce un minimo globale poiché la funzione di rischio scelta è convessa.

---

## 2. Esempio: Modello Bernoulli Composto

Si consideri una sequenza binaria $\mathbf{X}^n \in \{0, 1\}^n$ condizionalmente distribuita come Bernoulli con parametro $\beta$, assumendo una distribuzione a priori uniforme $p(\beta) \sim \mathcal{U}(0, 1)$.

### Derivazione della Legge di Probabilità
Il peso di Hamming $w(\mathbf{x}^n)$ rappresenta il numero di successi (ovvero il numero di uno) nella sequenza. La verosimiglianza è data da:

$$
p_{\mathbf{X}^n|\beta}(\mathbf{x}^n | \beta) = \beta^{w(\mathbf{x}^n)} (1 - \beta)^{n - w(\mathbf{x}^n)}
$$

Integrando su $\beta$ per ottenere la legge incondizionata, si ha:

$$
p_{\mathbf{X}^n}(\mathbf{x}^n) = \int_0^1 \beta^{w(\mathbf{x}^n)} (1 - \beta)^{n - w(\mathbf{x}^n)} \, d\beta = \frac{\Gamma(w+1)\Gamma(n-w+1)}{\Gamma(n+2)} = \frac{1}{\binom{n+1}{w(\mathbf{x}^n)}}
$$

Di conseguenza, la legge condizionale (posterior) è:

$$
f_{\beta|\mathbf{X}^n}(\beta | \mathbf{x}^n) = \frac{\beta^{w(\mathbf{x}^n)} (1 - \beta)^{n - w(\mathbf{x}^n)}}{\binom{n+1}{w(\mathbf{x}^n)}}
$$

### Calcolo della Stima MMSE
Applicando la definizione di aspettativa condizionata:

$$
\hat{\beta}_{\text{MMSE}}(\mathbf{x}^n) = \frac{1}{p_{\mathbf{X}^n}(\mathbf{x}^n)} \int_0^1 \beta \cdot \beta^{w(\mathbf{x}^n)} (1 - \beta)^{n - w(\mathbf{x}^n)} \, d\beta
$$

Risolvendo l'integrale tramite la funzione Beta, si ottiene:

$$
\hat{\beta}_{\text{MMSE}}(\mathbf{x}^n) = \frac{\Gamma(w+2)\Gamma(n-w+1)}{\Gamma(n+3)} \cdot \frac{1}{\binom{n+1}{w(\mathbf{x}^n)}} = \frac{w(\mathbf{x}^n) + 1}{n + 2}
$$

---

## 3. Estimatore Maximum A Posteriori (MAP)

Si consideri ora una funzione di costo basata sulla distanza discreta:

$$
C(\hat{\Theta}(\mathbf{X}^n), \Theta) = \mathbb{I}\left( \frac{|\hat{\Theta}(\mathbf{X}^n) - \Theta|}{\epsilon} \geq \frac{1}{2} \right) = 
\begin{cases} 
0 & \text{se } |\hat{\Theta}(\mathbf{X}^n) - \Theta| < \frac{\epsilon}{2} \\
1 & \text{altrimenti}
\end{cases}
$$

Poiché $\epsilon$ può essere reso arbitrariamente piccolo, la minimizzazione di tale costo equivale a massimizzare la probabilità a posteriori. L'estimatore MAP è quindi definito come:

$$
\hat{\theta}(\mathbf{x}^n) = \arg \max_{\theta} f_{\Theta|\mathbf{X}^n}(\theta | \mathbf{x}^n)
$$

### Applicazione al Modello Bernoulli Composto
Applicando questo criterio allo stesso scenario precedente, la stima che massimizza la densità posteriore è:

$$
\hat{\beta}_{\text{MAP}}(\mathbf{x}^n) = \frac{w(\mathbf{x}^n)}{n}
$$

> [!NOTE]
> Mentre l'estimatore **MMSE** "regolarizza" la stima aggiungendo un termine di bias (corrispondente alla media a priori), l'estimatore **MAP** fornisce la massima verosimiglianza corretta dalla distribuzione a priori, che in questo caso specifico coincide con la frequenza relativa dei successi.

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e il rigore tecnico.

---

## Analisi delle Prestazioni degli Estimatori

In questa sezione si analizzano le proprietà statistiche degli stimatori considerati, con particolare attenzione all'errore sistematico (*bias*) e alla consistenza.

### 1. Errore Sistematico (Bias)
Si considerino preliminarmente le proprietà di distorsione del parametro $B$. Assumendo la distribuzione uniforme su $[0, 1]$, si ottengono:

$$ \mathbb{E}[B] = \int_{0}^{1} \beta \, d\beta = \frac{1}{2}, \quad \mathbb{E}[B^2] = \frac{1}{3}, \quad \sigma_B^2 = \frac{1}{12} $$

Definiamo la variabile $w(\boldsymbol{X}^n)$. Le sue aspettative sono calcolate tramite la legge della probabilità totale:

$$ \mathbb{E}[w(\boldsymbol{X}^n)] = \mathbb{E}\left[ \underbrace{\mathbb{E}[w(\boldsymbol{X}^n) | B]}_{nB} \right] = \frac{n}{2} $$
$$ \mathbb{E}[w^2(\boldsymbol{X}^n)] = \mathbb{E}\left[ \underbrace{\mathbb{E}[w^2(\boldsymbol{X}^n) | B]}_{nB(1-B) + n^2B^2} \right] = \frac{n}{6} + \frac{n^2}{3} $$

Da cui si ricava la varianza:
$$ \sigma_{w(\boldsymbol{X}^n)}^2 = \frac{n}{6} \left( 1 + \frac{n}{2} \right) $$

#### Confronto tra MMSE e MAP
Analizziamo il bias per i due stimatori:

*   **MMSE (Minimum Mean Square Error):**
    $$ \mathbb{E}[\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n) | B = \beta] = \frac{n\beta + 1}{n + 2} \implies \mathbb{E}[\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n)] = \frac{\frac{n}{2} + 1}{n + 2} $$

*   **MAP (Maximum A Posteriori):**
    $$ \mathbb{E}[\hat{B}_{\text{MAP}}(\boldsymbol{X}^n) | B = \beta] = \beta \implies \mathbb{E}[\hat{B}_{\text{MAP}}(\boldsymbol{X}^n)] = \frac{\frac{n}{2}}{n} = \frac{1}{2} $$

> [!IMPORTANT] Conclusione sul Bias
> Lo stimatore **MMSE** è distorto (*biased*), mentre lo stimatore **MAP** è non distorto (*unbiased*). Tuttavia, l'MMSE è asintoticamente non distorto, poiché il bias svanisce per $n \to \infty$.

---

### 2. Errori Casuali e Consistenza
L'analisi dell'errore quadratico medio (MSE) permette di valutare la precisione degli stimatori:

$$ \mathbb{E}\left[ (\hat{B}_{\text{MMSE}}(\boldsymbol{X}^n) - B)^2 \right] = \overline{e^2}_{\text{MMSE}} = \frac{n - 2}{6(n + 2)^2} $$
$$ \mathbb{E}\left[ (\hat{B}_{\text{MAP}}(\boldsymbol{X}^n) - B)^2 \right] = \overline{e^2}_{\text{MAP}} = \frac{1}{6n} $$

Si osserva che $\overline{e^2}_{\text{MMSE}} < \overline{e^2}_{\text{MAP}}$ per ogni $n$. 

#### Proprietà di Consistenza
Poiché entrambi gli MSE tendono a zero all'aumentare della dimensione del campione ($n \to \infty$), i due stimatori sono definiti **MS consistenti**. 

Applicando la disuguaglianza di Chebyshev, si deduce che entrambi gli estimatori convergono a $B$ in probabilità (consistenza debole):
$$ \forall \epsilon > 0, \quad \lim_{n \to \infty} \text{Pr}\left\{ |\hat{B}(\boldsymbol{X}^n) - B| > \epsilon \right\} = 0 $$

Inoltre, è possibile dimostrare che entrambi gli stimatori sono **fortemente consistenti**, ovvero:
$$ \hat{B}(\boldsymbol{X}^n) \xrightarrow{\text{a.s.}} B \quad \text{per } n \to \infty $$

Ecco una versione revisionata del testo, ottimizzata per la chiarezza accademica e il rigore tecnico.

---

# Fondamenti di Stima Statistica e Inferenza Bayesiana

## Definizioni Generali

Sia $\mathbf{X}^n$ un campione estratto da un vettore casuale $\mathbf{Y}$. Si assume che $\mathbf{X}^n$ segua una distribuzione nota (PDF per variabili continue, PMF per variabili discrete) appartenente a una famiglia con prior specificato. 

Formalmente, si considerano note la densità di probabilità congiunta $f_{\mathbf{X}^n, \Theta}(\mathbf{x}^n, \theta)$ e la distribuzione a priori del parametro $f_\Theta(\theta)$. L'obiettivo dell'inferenza è stimare il valore del parametro $\theta$ sulla base della realizzazione osservata $\mathbf{x}^n$.

Le due principali strategie di stima sono definite come segue:

*   **Stima MMSE (Minimum Mean Square Error):** Corrisponde al valore atteso del parametro condizionato all'osservazione.
    $$\widehat{\theta}_{\text{MMSE}}(\mathbf{x}^n) = \mathbb{E}[\Theta \mid \mathbf{X}^n = \mathbf{x}^n] = \int \theta f_{\Theta \mid \mathbf{X}^n}(\theta \mid \mathbf{x}^n) \, d\theta$$

*   **Stima MAP (Maximum A Posteriori):** Corrisponde al valore che massimizza la densità a posteriori.
    $$\widehat{\theta}_{\text{MAP}}(\mathbf{x}^n) = \arg \max_{\theta} f_{\Theta \mid \mathbf{X}^n}(\theta \mid \mathbf{x}^n)$$

### Proprietà degli Estimatori

> [!IMPORTANT] Proprietà Fondamentali
> 1. **Non Distorto (Unbiased):** Un estimatore è non distorto se $\mathbb{E}[\widehat{\Theta}(\mathbf{X}^n) - \Theta] = 0$.
> 2. **Asintoticamente Non Distorto:** Un estimatore è asintoticamente non distorto se la condizione di non distorsione è soddisfatta nel limite $n \to \infty$.
> 3. **Consistente:** Un estimatore è consistente se $\widehat{\Theta}(\mathbf{X}^n) \xrightarrow{P} \Theta$ (convergenza in probabilità).
> 4. **MS Consistente:** Un estimatore è MS consistente se $\widehat{\Theta}(\mathbf{X}^n) \xrightarrow{MS} \Theta$ (convergenza in media quadratica).
> 5. **Fortemente Consistente:** Un estimatore è fortemente consistente se $\widehat{\Theta}(\mathbf{X}^n) \xrightarrow{a.s.} \Theta$ (convergenza quasi certa).

---

## Esempio Applicativo: Osservazioni Gaussiane con Media Casuale

Consideriamo un modello in cui $x_i$ è estratto da una distribuzione Gaussiana con media $\mu$, dove $\mu$ è essa stessa una variabile casuale. La verosimiglianza (likelihood) è data da:

$$f_{\mathbf{X}^n \mid M}(\mathbf{x}^n \mid \mu) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left[ -\frac{(x_i - \mu)^2}{2\sigma^2} \right]$$

L'obiettivo è inferire il valore di $\mu$. Assumendo un prior Gaussiano per la media, $M \sim \mathcal{N}(\mu_0, \sigma_M^2)$, la densità a posteriori risulta essere:

$$f_{M \mid \mathbf{X}^n}(\mu \mid \mathbf{x}^n) = \frac{f_{\mathbf{X}^n \mid M}(\mathbf{x}^n \mid \mu) f_M(\mu)}{f_{\mathbf{X}^n}(\mathbf{x}^n)} = \mathcal{N} \left( \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}, \frac{1}{\frac{n}{\sigma^2} + \frac{1}{\sigma_M^2}} \right)$$

> [!NOTE] Proprietà della Distribuzione Coniugata
> In questo contesto, la distribuzione Gaussiana è il **prior coniugato** per la media di una distribuzione Gaussiana; ciò implica che la distribuzione a posteriori mantiene la stessa forma funzionale del prior.

### Confronto tra Stimatori MMSE e MAP

Dalla derivazione della densità a posteriori, si ottengono i seguenti stimatori:

1.  **Stima MMSE:**
    $$\widehat{\mu}_{\text{MMSE}}(\mathbf{x}^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

2.  **Stima MAP:**
    Partendo dal logaritmo della densità a posteriori:
    $$\ln f_{M \mid \mathbf{X}^n}(\mu \mid \mathbf{x}^n) = \ln f_{\mathbf{X}^n \mid M}(\mathbf{x}^n \mid \mu) + \ln f_M(\mu) - \ln f_{\mathbf{X}^n}(\mathbf{x}^n)$$
    Massimizzando rispetto a $\mu$, otteniamo:
    $$\widehat{\mu}_{\text{MAP}}(\mathbf{x}^n) = \frac{\sum_{i=1}^{n} x_i}{n + \frac{\sigma^2}{\sigma_M^2}}$$

> [!QUOTE] Osservazione Teorica
> Si nota che, in questo specifico modello Gaussiano, gli stimatori **MMSE e MAP coincidono**. Questa non è una coincidenza casuale: per distribuzioni con simmetria gaussiana, il valore atteso (MMSE) e la moda (MAP) della distribuzione a posteriori coincidono esattamente.

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, uniformato la notazione matematica e strutturato il contenuto per massimizzare la chiarezza didattica.

---

# Unicità degli stimatori Bayesiani

Sia $C(\cdot)$ una funzione di costo arbitraria dell'errore di stima. Si consideri che $C(\cdot)$ sia una funzione pari e convessa. 

Supponiamo inoltre che la distribuzione a posteriori della variabile casuale $\Theta$, data l'osservazione $\mathbf{x}^n$, sia simmetrica rispetto alla sua media $\mathbb{E}[\Theta | \mathbf{X}^n = \mathbf{x}^n]$. Formalmente, tale condizione è espressa come:

$$f_{\Theta | \mathbf{X}^n}(\theta - \mathbb{E}[\Theta | \mathbf{X}^n = \mathbf{x}^n] \mid \mathbf{x}^n) = f_{\Theta | \mathbf{X}^n}(-\theta + \mathbb{E}[\Theta | \mathbf{X}^n = \mathbf{x}^n] \mid \mathbf{x}^n)$$

In queste condizioni, lo stimatore **MMSE** (Minimum Mean Square Error) minimizza il rischio Bayesiano per qualsiasi funzione di costo appartenente a questa classe.

> [!IMPORTANT]
> **Nota sulla stima MAP:** Sebbene la funzione di costo 0-1 utilizzata per derivare lo stimatore MAP non sia differenziabile, si può dimostrare che, sotto la condizione di simmetria sopra indicata, le due stime coincidono:
> $$\widehat{\mu}_{\text{MAP}}(\mathbf{x}^n) = \widehat{\mu}_{\text{MMSE}}(\mathbf{x}^n)$$

---

# Inferenza non Bayesiana: Stima di parametri non casuali

In questo contesto, assumiamo che le osservazioni $\mathbf{x}^n \in \mathcal{X}^n$ siano estratte da una famiglia di funzioni di densità di probabilità (pdf) $f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)$. 

Si considerano le seguenti ipotesi:
*   Il parametro $\theta$ è deterministico e sconosciuto.
*   Non disponiamo di informazioni *a priori* sufficienti per assegnare una distribuzione prior $f_\Theta(\theta)$.
*   Lo spazio dei parametri è definito dall'insieme $\mathcal{S}$.

### Verosimiglianza e Massima Verosimiglianza
Definiamo la **verosimiglianza** del parametro $\theta$, data l'osservazione $\mathbf{x}^n$, come la funzione:
$$L(\theta; \mathbf{x}^n) = f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)$$

Oppure, in forma logaritmica (log-verosimiglianza):
$$\Lambda(\theta; \mathbf{x}^n) = \log f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)$$

Una stima di **Massima Verosimiglianza (ML)** di $\theta$ è ottenuta come:
$$\widehat{\theta}_{\text{ML}}(\mathbf{x}^n) = \arg \max_{\theta \in \mathcal{S}} \log f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)$$

Essa rappresenta una specifica realizzazione dello stimatore di Massima Verosimiglianza (MLE):
$$\widehat{\Theta}_{\text{ML}}(\mathbf{X}^n) = \arg \max_{\theta \in \mathcal{S}} \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)$$

---

# Inferenza non Bayesiana: Misure di prestazione

Data una funzione stimatore $\Theta(\mathbf{x}^n)$ del parametro non casuale $\theta$, definiamo le seguenti metriche di prestazione:

### 1. Bias (Distorsione)
L'aspettativa dello stimatore è data da:
$$\mathbb{E}[\Theta(\mathbf{X}^n)] = \theta + b_n(\theta)$$
dove $b_n(\theta)$ rappresenta il **bias** dello stimatore.
*   Lo stimatore è **non distorto (unbiased)** se $b_n(\theta) = 0$.
*   Lo stimatore è **asintoticamente non distorto** se $b_n(\theta) \to 0$ all'aumentare di $n$.

### 2. Errore Quadratico Medio (MSE)
L'errore casuale dello stimatore è quantificato tramite il valore *Mean Square*:
$$\mathbb{E}[(\Theta(\mathbf{X}^n) - \theta)^2] = \overline{e_n^2}$$

Uno stimatore **MMSE non distorto** di $\theta$ è quello che minimizza la varianza:
$$\operatorname{Var}[\Theta(\mathbf{X}^n)] = \mathbb{E}[\Theta^2(\mathbf{X}^n)] - \theta^2$$

### 3. Consistenza
La convergenza dello stimatore verso il valore vero $\theta$ può essere classificata in tre modi:
*   **Debolmente consistente:** $\Theta(\mathbf{x}^n) \xrightarrow{P} \theta$ (convergenza in probabilità).
*   **Fortemente consistente:** $\Theta(\mathbf{x}^n) \xrightarrow{a.s.} \theta$ (convergenza quasi certa).
*   **MS consistente:** $\overline{e_n^2} \to 0$ (convergenza in senso quadratico medio).

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Il Limite di Cramér-Rao: Fondamenti e Derivazione

## 1. Fatti Preliminari

Sia $\mathbf{X}^n$ un vettore casuale con densità di probabilità $f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)$, dove $\theta$ è un parametro non casuale (scalar). Sia $\mathbf{x}^n$ la realizzazione del campione.

Consideriamo l'identità fondamentale della densità di probabilità:
$$ \int_{\mathbb{R}^n} f_{\mathbf{X}^n}(\mathbf{x}^n; \theta) \, d\mathbf{x}^n = 1 $$

Differenziando entrambi i membri rispetto a $\theta$, otteniamo:
$$ \int_{\mathbb{R}^n} \frac{\partial f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)}{\partial \theta} \, d\mathbf{x}^n = 0 $$

Utilizzando la proprietà della derivata del logaritmo, $\frac{\partial f}{\partial \theta} = \frac{\partial \log f}{\partial \theta} f$, possiamo riscrivere l'integrale come:
$$ \int_{\mathbb{R}^n} \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)}{\partial \theta} f_{\mathbf{X}^n}(\mathbf{x}^n; \theta) \, d\mathbf{x}^n = 0 $$

Questa espressione corrisponde esattamente all'aspettativa del punteggio (score function):
$$ \mathbb{E} \left[ \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right] = 0 $$

Differenziando ulteriormente rispetto a $\theta$, si ottiene la relazione tra la varianza dello score e la derivata seconda del logaritmo della densità:
$$ \mathbb{E} \left[ \left( \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right)^2 \right] = \text{Var} \left[ \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right] = - \mathbb{E} \left[ \frac{\partial^2 \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta^2} \right] $$

> [!IMPORTANT]
> **Nota chiave:** La derivata seconda del logaritmo della densità è legata alla curvatura della distribuzione rispetto al parametro $\theta$. Il segno negativo garantisce che la varianza sia non negativa, poiché la funzione di densità deve essere integrabile.

## 2. Derivazione del Limite di Cramér-Rao

Sia $\widehat{\Theta}(\mathbf{X}^n)$ uno stimatore del parametro $\theta$ tale che il suo valore atteso soddisfi:
$$ \mathbb{E}[\widehat{\Theta}(\mathbf{X}^n)] = \int_{\mathbb{R}^n} \widehat{\Theta}(\mathbf{x}^n) f_{\mathbf{X}^n}(\mathbf{x}^n; \theta) \, d\mathbf{x}^n = \theta + b_n(\theta) $$
dove $b_n(\theta)$ rappresenta il *bias* dello stimatore.

Differenziando l'identità rispetto a $\theta$:
$$ \frac{\partial}{\partial \theta} \int_{\mathbb{R}^n} \widehat{\Theta}(\mathbf{x}^n) f_{\mathbf{X}^n}(\mathbf{x}^n; \theta) \, d\mathbf{x}^n = 1 + b_n'(\theta) $$

Applicando la regola della derivata sotto l'integrale:
$$ \int_{\mathbb{R}^n} \widehat{\Theta}(\mathbf{x}^n) \frac{\partial f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)}{\partial \theta} \, d\mathbf{x}^n = 1 + b_n'(\theta) $$

Sostituendo nuovamente $\frac{\partial f}{\partial \theta} = \frac{\partial \log f}{\partial \theta} f$, otteniamo:
$$ \int_{\mathbb{R}^n} \widehat{\Theta}(\mathbf{x}^n) \left( \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{x}^n; \theta)}{\partial \theta} \right) f_{\mathbf{X}^n}(\mathbf{x}^n; \theta) \, d\mathbf{x}^n = 1 + b_n'(\theta) $$

Questa espressione è la definizione della covarianza tra lo stimatore e lo score:
$$ \text{Cov} \left[ \widehat{\Theta}(\mathbf{X}^n), \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right] = 1 + b_n'(\theta) $$

Applicando la **diseguaglianza di Cauchy-Schwarz**, che stabilisce che $|\text{Cov}(X, Y)|^2 \leq \text{Var}(X)\text{Var}(Y)$, otteniamo:
$$ \left| \text{Cov} \left[ \widehat{\Theta}(\mathbf{X}^n), \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right] \right|^2 = [1 + b_n'(\theta)]^2 \leq \text{Var}[\widehat{\Theta}(\mathbf{X}^n)] \cdot \text{Var} \left[ \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right] $$

Da cui si deduce il limite inferiore per la varianza dello stimatore:
$$ \text{Var}[\widehat{\Theta}(\mathbf{X}^n)] \geq \frac{[1 + b_n'(\theta)]^2}{\text{Var} \left[ \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right]} $$

Ecco una versione revisionata del testo, ottimizzata per chiarezza didattica, fluidità e rigore tecnico.

---

# Limite di Cramér-Rao: Analisi Avanzata e Applicazioni

## Fondamenti del Limite di Cramér-Rao (CRB)

Dalle derivazioni precedenti, si evince che la varianza di qualsiasi stimatore $\Theta(\mathbf{X}^n)$ di un parametro non casuale $\theta$ è vincolata da un limite inferiore:

$$
\operatorname{Var}[\Theta(\mathbf{X}^n)] \geq \frac{[1 + b_n'(\theta)]^2}{\mathbb{E}\left[ \left( \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right)^2 \right]} = \frac{[1 + b_n'(\theta)]^2}{I_n(\theta)}
$$

In questa espressione, $I_n(\theta)$ rappresenta l'**Informazione di Fisher**, definita attraverso la seguente identità:

$$
I_n(\theta) = \mathbb{E}\left[ \left( \frac{\partial \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta} \right)^2 \right] = -\mathbb{E}\left[ \frac{\partial^2 \log f_{\mathbf{X}^n}(\mathbf{X}^n; \theta)}{\partial \theta^2} \right]
$$

## Stimatori Non Distorti ed Efficienza

Si consideri uno stimatore $\Theta(\mathbf{x}^n)$ **non distorto** (unbiased), ovvero tale che soddisfi la condizione:
$$
\mathbb{E}[\Theta(\mathbf{X}^n)] = \theta
$$

In tale scenario, il valore atteso del quadrato dell'errore coincide con la varianza, e la diseguaglianza si semplifica in:

$$
\mathbb{E}[(\Theta(\mathbf{X}^n) - \theta)^2] = \operatorname{Var}[\Theta(\mathbf{X}^n)] \geq \frac{1}{I_n(\theta)}
$$

Pertanto, il Limite di Cramér-Rao (CRB) stabilisce il limite inferiore per l'Errore Quadratico Medio (MSE) di ogni stimatore non distorto. 

> [!IMPORTANT] Definizione di Efficienza
> Uno stimatore non distorto è definito **efficiente** se il suo MSE raggiunge il limite di Cramér-Rao, ovvero:
> $$ \operatorname{Var}[\Theta(\mathbf{X}^n)] = \frac{1}{I_n(\theta)} $$
> 
> **Nota teorica:** Se esiste uno stimatore efficiente per un problema di stima non Bayesiana, esso coincide necessariamente con lo stimatore del Massimo di Verosimiglianza (Maximum Likelihood Estimator - MLE).

---

## Esempio Applicativo: Inferenza della Frequenza di Cifratura

Consideriamo una sorgente senza memoria che produce una sequenza $\mathbf{x}^n \in \{0, 1\}^n$ estratta da una distribuzione binomiale $\mathbf{X}^n \sim \mathcal{B}(1, \beta)$, dove $\beta$ è il parametro sconosciuto (frequenza di cifratura).

### 1. Derivazione della MLE
Sia $w(\mathbf{x}^n)$ il peso di Hamming della sequenza osservata. La funzione di verosimiglianza è data da:
$$
p_{\mathbf{X}^n}(\mathbf{x}^n) = \beta^{w(\mathbf{x}^n)} (1 - \beta)^{n - w(\mathbf{x}^n)}
$$

Per trovare lo stimatore MLE, massimizziamo il logaritmo della verosimiglianza:
$$
\frac{\partial \log p_{\mathbf{X}^n}(\mathbf{x}^n)}{\partial \beta} = 0 \implies \widehat{\beta}_{\mathrm{ML}}(\mathbf{x}^n) = \frac{w(\mathbf{x}^n)}{n}
$$

### 2. Proprietà dello stimatore $\widehat{\beta}$
Lo stimatore $\widehat{\beta}(\mathbf{X}^n) = \frac{w(\mathbf{X}^n)}{n}$ presenta le seguenti proprietà:
*   **Non distorsione:** $\mathbb{E}\left[ \frac{w(\mathbf{X}^n)}{n} \right] = \beta$
*   **Consistenza:** Lo stimatore è consistente in MSE.

### 3. Verifica dell'Efficienza
Per determinare se lo stimatore è efficiente, calcoliamo l'Informazione di Fisher. Partendo dal logaritmo della verosimiglianza:
$$
\log p_{\mathbf{X}^n}(\mathbf{X}^n; \beta) = w(\mathbf{X}^n) \log \beta + [n - w(\mathbf{X}^n)] \log(1 - \beta)
$$

Le derivate prime e seconde rispetto a $\beta$ sono:
$$
\frac{\partial \log p_{\mathbf{X}^n}(\mathbf{X}^n; \beta)}{\partial \beta} = \frac{w(\mathbf{X}^n)}{\beta} - \frac{n - w(\mathbf{X}^n)}{1 - \beta}
$$
$$
\frac{\partial^2 \log p_{\mathbf{X}^n}(\mathbf{X}^n; \beta)}{\partial \beta^2} = -\frac{w(\mathbf{X}^n)}{\beta^2} - \frac{n - w(\mathbf{X}^n)}{(1 - \beta)^2}
$$

Utilizzando l'aspettativa $\mathbb{E}[w(\mathbf{X}^n)] = n\beta$, otteniamo:
$$
I_n(\beta) = -\mathbb{E}\left[ \frac{\partial^2 \log p_{\mathbf{X}^n}}{\partial \beta^2} \right] = \frac{n\beta}{\beta^2} + \frac{n - n\beta}{(1 - \beta)^2} = \frac{n}{\beta} + \frac{n}{1 - \beta} = \frac{n}{\beta(1 - \beta)}
$$

Di conseguenza, il limite di Cramér-Rao è:
$$
\mathrm{CRB} = \frac{1}{I_n(\beta)} = \frac{\beta(1 - \beta)}{n}
$$

Poiché la varianza dello stimatore $\widehat{\beta}_{\mathrm{ML}}$ è esattamente $\operatorname{var}\left[ \frac{w(\mathbf{X}^n)}{n} \right] = \frac{\beta(1 - \beta)}{n}$, concludiamo che **la MLE della frequenza di cifratura è efficiente**.

Ecco una revisione professionale del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Inferenza Bayesiana con Parametri Multipli

Consideriamo un vettore di $m$ parametri casuali $\pmb{\theta} = [\theta_1, \dots, \theta_m]^T$, caratterizzati da una funzione di densità di probabilità (pdf) nota $f_{\Theta}(\pmb{\theta})$. Siano dati $\pmb{x}^n$ estratti da una pdf condizionale $f_{\pmb{X}^n|\pmb{\theta}}(\pmb{x}^n | \pmb{\theta})$.

Definiamo la funzione di costo $C$ come segue:
$$ C(\pmb{\theta} - \widehat{\pmb{\theta}}) = C\left(\theta_1 - \widehat{\theta}_1, \dots, \theta_m - \widehat{\theta}_m\right) $$

L'estimatore Bayes-ottimale $\widehat{\pmb{\theta}}(\pmb{x}^n)$ è ottenuto risolvendo il problema di minimizzazione del valore atteso della funzione di costo:
$$ \widehat{\pmb{\theta}}(\pmb{x}^n) : \mathbb{E}\left[ C(\pmb{\Theta} - \widehat{\pmb{\Theta}}(\pmb{X}^n)) \right] = \min $$

Applicando la procedura analitica utilizzata per il caso a parametro singolo, l'estimatore può essere espresso in forma chiusa come:
$$ \widehat{\pmb{\Theta}}(\pmb{X}^n) = \arg \min_{\widehat{\pmb{\theta}}} \int_{\mathbb{R}^m} C\left(\pmb{\theta} - \widehat{\pmb{\theta}}(\pmb{X}^n)\right) f_{\Theta|\pmb{X}^n}(\pmb{\theta} | \pmb{X}^n) \, d\pmb{\theta} $$

## L'Estimatore MMSE (Minimum Mean Square Error)

> [!THEOREM] Estimatore MMSE
> L'**MMSE** è l'estimatore che minimizza il valore atteso del quadrato dell'errore tra la stima e il valore reale del parametro.
> 
> **Formalizzazione:**
> $$ \hat{\theta}_{MMSE} = \arg\min_{\hat{\theta}} \mathbb{E}\left[ \|\theta - \hat{\theta}\|^2 \right] $$

Assumendo che la funzione di costo sia definita dalla somma dei quadrati degli scarti:
$$ C(\pmb{\theta} - \widehat{\pmb{\theta}}) = \sum_{i=1}^m (\theta_i - \widehat{\theta}_i(\pmb{x}^n))^2 $$

Poiché il problema di minimizzazione è separabile (disgiunto) per ogni componente del vettore, la stima ottimale per ogni parametro $i$ è data dalla media condizionale:
$$ \widehat{\theta}_i(\pmb{x}^n) = \mathbb{E}\left[ \Theta_i | \pmb{X}^n = \pmb{x}^n \right] = \int \theta_i f_{\theta_i|\pmb{X}^n}(\theta_i | \pmb{x}^n) \, d\theta_i $$

Di conseguenza, l'estimatore vettoriale MMSE è identificato come:
$$ \widehat{\pmb{\Theta}}(\pmb{X}^n) = \mathbb{E}\left[ \pmb{\Theta} | \pmb{X}^n \right] $$

## L'Estimatore MAP (Maximum A Posteriori)

> [!THEOREM] Estimatore MAP
> La stima **MAP** massimizza la probabilità a posteriori del parametro, integrando la verosimiglianza dei dati con la conoscenza *a priori* sulla distribuzione dei parametri.
> 
> **Formalizzazione:**
> $$ \hat{\theta}_{MAP} = \arg\max_{\theta} p(\theta | \mathbf{x}) $$

Se consideriamo una funzione di costo basata su una funzione di perdita (es. logaritmica o correlata alla densità), definita come:
$$ C(\pmb{\theta} - \widehat{\pmb{\theta}}) = \sum_{i=1}^m \Pi\left(\frac{\theta_i - \widehat{\theta}_i(\pmb{x}^n)}{\epsilon}\right) $$

Seguendo la procedura di derivazione, l'estimatore MAP soddisfa la condizione di stazionarietà:
$$ \frac{\partial f_{\Theta|\pmb{X}^n}(\pmb{\theta} | \pmb{x}^n)}{\partial \theta_i} \Bigg|_{\theta_i = \widehat{\theta}_i(\pmb{x}^n)} = 0 $$

In termini vettoriali, la stima MAP risolve l'equazione del gradiente nullo della pdf a posteriori:
$$ \nabla_{\pmb{\theta}} f_{\pmb{\Theta}|\pmb{X}^n}(\pmb{\theta} | \pmb{x}^n) \Big|_{\pmb{\theta} = \widehat{\pmb{\theta}}(\pmb{x}^n)} = 0 $$

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Stima non Bayesiana di parametri multipli

Assumiamo che il vettore dei parametri $\boldsymbol{\theta}$ sia reale e deterministico. Consideriamo un insieme di dati osservati $\mathbf{x}^n$ estratti da una famiglia di distribuzioni $f_{\mathbf{X}^n}(\mathbf{x}^n; \boldsymbol{\theta})$. 

## Log-verosimiglianza e Maximum Likelihood (ML)

Definiamo la funzione di log-verosimiglianza $\Lambda(\boldsymbol{\theta}; \mathbf{x}^n)$ come:
$$
\Lambda(\boldsymbol{\theta}; \mathbf{x}^n) = \log f_{\mathbf{X}^n}(\mathbf{x}^n, \boldsymbol{\theta})
$$

L'estimatore di Maximum Likelihood (ML) del vettore $\boldsymbol{\theta}$, indicato con $\widehat{\boldsymbol{\theta}}(\mathbf{x}^n)$, è definito come la soluzione dell'equazione del gradiente nullo:
$$
\nabla_{\boldsymbol{\theta}} \Lambda(\boldsymbol{\theta}; \mathbf{x}^n) \big|_{\boldsymbol{\theta} = \widehat{\boldsymbol{\theta}}(\mathbf{x}^n)} = 0
$$

> [!IMPORTANT]
> L'estimatore $\widehat{\Theta}(\mathbf{X}^n)$ derivato in questo modo gode di proprietà fondamentali quali la consistenza e l'efficienza asintotica.

---

# Estimatori MMSE Lineari (LMMSE)

Consideriamo un problema scalare in cui si desidera progettare un estimatore lineare per un parametro casuale $\Theta$, distribuito secondo una legge nota, basandosi sul campione osservato $\mathbf{x}^n$. L'estimatore assume la forma:
$$
\widehat{\Theta}(\mathbf{X}^n) = \mathbf{a}^T \mathbf{X}^n + b, \quad \mathbf{a} \in \mathbb{R}^n
$$

L'obiettivo è determinare il vettore $\mathbf{a}$ e la costante $b$ che minimizzano l'Errore Quadratico Medio (MSE):
$$
\text{MSE} = \mathbb{E}\left[ (\widehat{\Theta}(\mathbf{X}^n) - \Theta)^2 \right] = \mathbb{E}\left[ (\mathbf{a}^T \mathbf{X}^n + b - \Theta)^2 \right]
$$

Espandendo l'espressione, otteniamo:
$$
\text{MSE} = \mathbf{a}^T \mathbf{R} \mathbf{a} + b^2 + \mathbb{E}[\Theta^2] - 2b\mathbb{E}[\Theta] - 2\mathbf{a}^T \mathbb{E}[\mathbf{X}^n \Theta] - 2b\mathbf{a}^T \mathbb{E}[\mathbf{X}^n]
$$
dove $\mathbf{R} = \mathbb{E}[\mathbf{X}^n (\mathbf{X}^n)^T]$ è la matrice di correlazione del vettore casuale $\mathbf{X}^n$.

## Derivazione dell'ottimo

Per minimizzare l'MSE, calcoliamo le derivate rispetto a $b$ e $\mathbf{a}$ e le poniamo uguali a zero:

1. **Derivata rispetto a $b$:**
   $$
   \frac{\partial \text{MSE}}{\partial b} = 2b - 2\mathbb{E}[\Theta] - 2\mathbf{a}^T \mathbb{E}[\mathbf{X}^n] = 0
   $$

2. **Gradiente rispetto a $\mathbf{a}$:**
   $$
   \nabla_{\mathbf{a}} \text{MSE} = 2\mathbf{R}\mathbf{a} - 2\mathbb{E}[\mathbf{X}^n \Theta] = 0
   $$

### Risoluzione per $b$ e $\mathbf{a}$

Dalla prima equazione, isoliamo $b$:
$$
b_{\text{LMMSE}} = \mathbb{E}[\Theta] - \mathbf{a}^T \mathbb{E}[\mathbf{X}^n]
$$

Sostituendo $b$ nell'equazione dell'estimatore, otteniamo una forma centrata:
$$
\widehat{\Theta}(\mathbf{X}^n) = \mathbf{a}^T (\mathbf{X}^n - \mathbb{E}[\mathbf{X}^n]) + \mathbb{E}[\Theta]
$$

Inserendo questa espressione nell'MSE dimostra che $\mathbf{a}$ deve minimizzare il seguente termine:
$$
\left\| \mathbf{a}^T (\mathbf{X}^n - \mathbb{E}[\mathbf{X}^n]) + (\Theta - \mathbb{E}[\Theta]) \right\|^2
$$

Definendo $\mathbf{M} = \mathbb{E}[(\mathbf{X}^n - \mathbb{E}[\mathbf{X}^n])(\mathbf{X}^n - \mathbb{E}[\mathbf{X}^n])^T]$ come la matrice di covarianza di $\mathbf{X}^n$, la soluzione ottimale per il vettore $\mathbf{a}$ è:
$$
\mathbf{a}_{\text{LMMSE}} = \mathbf{M}^{-1} \mathbb{E}\left[ (\mathbf{X}^n - \mathbb{E}[\mathbf{X}^n])(\Theta - \mathbb{E}[\Theta]) \right] = \mathbf{M}^{-1} \mathbf{s}
$$
dove $\mathbf{s}$ rappresenta il vettore di cross-correlazione tra l'osservabile e il parametro da stimare.

Ecco una versione revisionata del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

# Analisi dell'Algoritmo del Gradiente e Approccio Least Squares

## 1. L'Algoritmo del Gradiente per il problema LMMSE

Consideriamo la risoluzione iterativa del problema *Linear Minimum Mean Square Error* (LMMSE). Il gradiente dell'errore quadratico medio (MSE) è espresso come:

$$
\nabla_{a} \mathbb{E} \left[ \left(\boldsymbol{a}^{T} \boldsymbol{X}^{n} + b - \Theta\right)^{2} \right] = 2 \boldsymbol{M} \boldsymbol{a} - 2 \mathbb{E} \left[ \boldsymbol{X}^{n} \Theta \right] = 2 \boldsymbol{M} \boldsymbol{a} - 2 \boldsymbol{s}
$$

dove $\boldsymbol{s} = \mathbb{E} \left[ \boldsymbol{X}^{n} \Theta \right]$ è un vettore noto. Per determinare l'estimatore $\boldsymbol{a}_{\text{LMMSE}}$, definiamo la seguente regola di aggiornamento iterativa:

$$
\boldsymbol{a}^{(n+1)} = \boldsymbol{a}^{(n)} - \gamma (\boldsymbol{M} \boldsymbol{a}^{(n)} - \boldsymbol{s})
$$

Questa espressione può essere riformulata per evidenziare la convergenza verso la soluzione ottima:

$$
\boldsymbol{a}^{(n+1)} = \boldsymbol{a}^{(n)} - \gamma \boldsymbol{M} \left(\boldsymbol{a}^{(n)} - \underbrace{\boldsymbol{M}^{-1} \boldsymbol{s}}_{\boldsymbol{a}_{\text{LMMSE}}}\right)
$$

### Analisi della Convergenza
Definiamo l'errore all'iterazione $(n+1)$ come la differenza tra il vettore corrente e la soluzione ottimale:

$$
\boldsymbol{\epsilon}^{(n+1)} = \boldsymbol{a}^{(n+1)} - \boldsymbol{a}_{\text{LMMSE}} = (\boldsymbol{I} - \gamma \boldsymbol{M}) \boldsymbol{\epsilon}^{(n)}
$$

Per ricorsione, l'errore alla $n$-es iterazione è dato da:

$$
\boldsymbol{\epsilon}^{(n+1)} = (\boldsymbol{I} - \gamma \boldsymbol{M})^{n} \boldsymbol{\epsilon}^{(1)}
$$

Utilizzando la decomposizione spettrale della matrice $\boldsymbol{M}$, dove $\boldsymbol{\Lambda}$ è la matrice diagonale dei valori propri e $\boldsymbol{U}$ è la matrice degli autovettori corrispondenti, otteniamo:

$$
\boldsymbol{\epsilon}^{(n+1)} = \boldsymbol{U} (\boldsymbol{I} - \gamma \boldsymbol{\Lambda})^{n} \boldsymbol{U}^{T}
$$

> [!IMPORTANT]
> **Condizione di Convergenza:** L'errore converge a zero se e solo se il modulo massimo dei valori propri della matrice $(\boldsymbol{I} - \gamma \boldsymbol{M})$ è strettamente minore di uno. Ciò implica:
> $$
> -1 < 1 - \gamma \lambda_{\max} < 1 \implies 0 < \gamma < \frac{2}{\lambda_{\max}}
> $$
> dove $\lambda_{\max}$ rappresenta il valore proprio massimo di $\boldsymbol{M}$.

---

## 2. Approccio basato sulla Statistica Descrittiva

In questa sezione, si trasita dall'approccio probabilistico alla **statistica descrittiva**. In questo contesto, i campioni non sono trattati come realizzazioni di variabili casuali, ma come entità dati discrete.

Definiamo un *dataset* di addestramento come una collezione di $p$ campioni $n$-dimensionali, strutturati nella matrice $\boldsymbol{X} \in \mathbb{R}^{n \times p}$:

$$
\boldsymbol{X} = \begin{bmatrix} 
x_{1}(1) & \dots & x_{1}(p) \\ 
\vdots & \ddots & \vdots \\ 
x_{n}(1) & \dots & x_{n}(p) 
\end{bmatrix}
$$

Supponendo di conoscere $p$ valori misurati del parametro $\theta_r$, corrispondenti ai campioni del *training set*, definiamo il vettore delle osservazioni:

$$
\boldsymbol{y} = [\theta(1), \dots, \theta(p)] \in \mathbb{R}^{p}
$$

L'obiettivo è adattare i dati a un modello lineare della forma:

$$
\mathbf{y} = \mathbf{X}\boldsymbol{\theta} + \boldsymbol{\epsilon} \tag{1}
$$

dove $\boldsymbol{\epsilon}$ rappresenta l'errore di modellazione.

## 3. L'Estimatore dei Minimi Quadrati (Least Squares)

Data la struttura del dataset $p$-dimensionale, si procede alla ricerca del vettore $\boldsymbol{a}$ che minimizza la seguente funzione di costo:

$$
\|\boldsymbol{\epsilon}\|^2 = \sum_{i=1}^{p} \left[ \boldsymbol{a}^{T} \boldsymbol{x}^{(i)} - \theta(i) \right]^{2}
$$

Il problema può essere riformulato in termini matriciali come la minimizzazione della norma:

$$
\|\boldsymbol{X}^{T} \boldsymbol{a} - \boldsymbol{y}\|^2
$$

Espandendo il prodotto scalare, otteniamo la forma quadratica:

$$
\|\boldsymbol{X}^{T} \boldsymbol{a} - \boldsymbol{y}\|^2 = \boldsymbol{a}^{T} \boldsymbol{X} \boldsymbol{X}^{T} \boldsymbol{a} + \|\boldsymbol{y}\|^2 - 2 \boldsymbol{a}^{T} \boldsymbol{X} \boldsymbol{y}
$$

Ecco una versione revisionata del testo. Ho ottimizzato la fluidità, uniformato la notazione matematica e strutturato il contenuto per massimizzare la chiarezza didattica, mantenendo il rigore tecnico richiesto.

---

# L'Estimatore dei Minimi Quadrati (LS)

## Derivazione dell'Estimatore
Partendo dalla funzione di costo associata ai minimi quadrati, differenziamo rispetto al vettore dei parametri $\boldsymbol{a}$ per trovare il punto di minimo:

$$ \nabla_{\boldsymbol{a}} \| \boldsymbol{X}^T \boldsymbol{a} - \boldsymbol{y} \|^2 = 2\boldsymbol{X}\boldsymbol{X}^T\boldsymbol{a} - 2\boldsymbol{X}\boldsymbol{y} = 0 $$

L'equazione risultante definisce il sistema lineare:

$$ (\mathbf{X}^T\mathbf{X})\boldsymbol{\theta} = \mathbf{X}^T\mathbf{y} \tag{2} $$

Da cui si ricava la soluzione analitica per l'estimatore LS:

$$ \boldsymbol{a}_{\mathrm{LS}} = (\boldsymbol{X}\boldsymbol{X}^T)^{-1} \boldsymbol{X}\boldsymbol{y} $$

> [!IMPORTANT]
> **Condizione di Invertibilità:** Affinché la soluzione sia definita, la matrice $(\mathbf{X}\mathbf{X}^T)$ deve essere invertibile. Questo richiede che il numero di osservazioni $p$ sia sufficiente rispetto alla dimensionalità del sistema (es. $p \geq n$).

Per convenzione, definiamo la stima basata su un campione di dimensione $p$ come:

$$ \boldsymbol{\theta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \tag{3} $$
$$ \boldsymbol{a}_{\mathrm{LS}}(p) = \left[ \boldsymbol{X}(p)\boldsymbol{X}^T(p) \right]^{-1} \boldsymbol{X}(p)\boldsymbol{y}(p) $$

## Dinamiche di Apprendimento e Aggiornamento
In un contesto di osservazione a orizzonte infinito, dove la dimensione del campione $p$ può aumentare indefinitamente, si distinguono due scenari operativi:

1.  **Miglioramento Progressivo:** Raffinamento della stima tramite l'integrazione continua di nuove osservazioni.
2.  **Adattamento Dinamico:** Aggiornamento della stima attraverso la "dimenticanza" delle osservazioni datate, permettendo di dare maggiore peso ai dati recenti (es. tramite finestre mobili o decadimento esponenziale).

È possibile ottimizzare l'estimatore LS per gestire entrambi gli scenari mantenendo una complessità computazionale contenuta.

## Apprendimento Ricorsivo e Complessità
Supponendo che sia stata calcolata la stima $\boldsymbol{a}_{\mathrm{LS}}(p)$, consideriamo l'inserimento di un nuovo vettore $\boldsymbol{x}^{n}(p+1)$ e della relativa osservazione $\theta(p+1)$. La nuova stima sarebbe teoricamente:

$$ \boldsymbol{a}_{\mathrm{LS}}(p+1) = \left[ \boldsymbol{X}(p+1)\boldsymbol{X}^T(p+1) \right]^{-1} \boldsymbol{X}(p+1)\boldsymbol{y}(p+1) \tag{4} $$

> [!NOTE]
> **Analisi della Complessità:** 
> Ricalcolare l'intera inversione di matrice per ogni nuovo dato è inefficiente. Mentre il prodotto di matrici ha una complessità $O(n^2)$, l'operazione di inversione richiede $O(n^3)$. Per ottimizzare il processo, è necessario utilizzare metodi di aggiornamento incrementale.

## La Formula di Sherman-Morrison
Per evitare il ricalcolo completo dell'inversa, si utilizza il lemma di inversione con aggiornamento *rank-1*. Sia $\boldsymbol{R}$ una matrice invertibile di ordine $n$, e siano $\boldsymbol{u}$ e $\boldsymbol{v}$ vettori colonna $n$-dimensionali:

$$ (\boldsymbol{R} + \boldsymbol{u}\boldsymbol{v}^T)^{-1} = \boldsymbol{R}^{-1} - \frac{\boldsymbol{R}^{-1}\boldsymbol{u}\boldsymbol{v}^T\boldsymbol{R}^{-1}}{1 + \boldsymbol{u}^T\boldsymbol{R}^{-1}\boldsymbol{v}} $$

## Applicazione all'Aggiornamento LS
Definiamo la matrice di covarianza (o matrice di struttura) come $\boldsymbol{R}(p) = \boldsymbol{X}(p)\boldsymbol{X}^T(p)$. L'aggiunta di una nuova osservazione può essere espressa come:

$$ \underbrace{\boldsymbol{X}(p+1)\boldsymbol{X}^T(p+1)}_{\boldsymbol{R}(p+1)} = \sum_{i=1}^{p+1} \boldsymbol{x}^n(i)\boldsymbol{x}^{nT}(i) = \underbrace{\boldsymbol{X}(p)\boldsymbol{X}^T(p)}_{\boldsymbol{R}(p)} + \boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1) $$

Applicando la formula di Sherman-Morrison, l'inversa della matrice aggiornata si ottiene direttamente dalla precedente:

$$ \boldsymbol{R}^{-1}(p+1) = \boldsymbol{R}^{-1}(p) - \frac{\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1)\boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)}{1 + K(p+1)} $$

dove il termine scalare $K(p+1)$ è definito come:

$$ K(p+1) = \boldsymbol{x}^{nT}(p+1)\boldsymbol{R}^{-1}(p)\boldsymbol{x}^n(p+1) $$

Ecco una revisione professionale del testo, ottimizzata per la chiarezza didattica e il rigore accademico.

---

## Derivazione dell'Aggiornamento Ricorsivo

Consideriamo le seguenti definizioni per gli stati al passo $p+1$:

$$ \boldsymbol{X}(p+1) = [\boldsymbol{X}(p) \,\, \mathbf{x}^n(p+1)], \quad \mathbf{y}(p+1) = [\mathbf{y}(p) \,\, \theta(p+1)]^T $$

Da queste definizioni, si deduce la relazione:

$$ \boldsymbol{X}(p+1)\mathbf{y}(p+1) = \boldsymbol{X}(p)\mathbf{y}(p) + \theta(p+1)\mathbf{x}^n(p+1) $$

Data la definizione del vettore dei parametri $\mathbf{a}(p+1) = \mathbf{R}^{-1}(p+1)\boldsymbol{X}(p+1)\mathbf{y}(p+1)$, e applicando il lemma di Sherman-Morrison per l'inversione della matrice di covarianza, si ottiene la seguente forma aggiornata:

$$ \mathbf{a}(p+1) = \left[ \mathbf{I}_n - \frac{\mathbf{R}^{-1}(p)\mathbf{x}^n(p+1)}{1 + K(p+1)} \mathbf{x}^{nT}(p+1) \right] \left[ \mathbf{a}(p) + \theta(p+1)\mathbf{R}^{-1}(p)\mathbf{x}^n(p+1) \right] $$

> [!IMPORTANT]
> **Complessità Computazionale:** L'operazione di aggiornamento presenta una complessità $\mathcal{O}(n^2)$, risultando indipendente dal numero di campioni $p$. Questa proprietà garantisce l'efficienza dell'algoritmo in scenari con grandi dataset.

## Adattività nel Least Squares (LS)

Per modellare sistemi in cui l'ambiente circostante varia lentamente nel tempo, è necessario assegnare un peso minore ai dati storici rispetto alle osservazioni più recenti ("fresche"). 

Un approccio standard per ottenere tale comportamento è l'utilizzo della **media mobile esponenziale** (Exponentially Weighted Moving Average), che introduce la seguente funzione di costo:

$$ J = \sum_{i=1}^{p} w^{p-i} \left[ \mathbf{a}^T \mathbf{x}^n(i) - \theta(i) \right]^2 $$

In questo contesto, il parametro $w < 1$ determina la velocità di "oblio" del modello rispetto ai dati passati. Minimizzando tale funzione rispetto a $\mathbf{a}$, si ottiene la soluzione per il **Least Squares mediato esponenzialmente**:

$$ \mathbf{a} = \left[ \sum_{i=1}^{p} w^{p-i} \mathbf{x}^n(i) \mathbf{x}^{nT}(i) \right]^{-1} \sum_{i=1}^{p} w^{p-i} \mathbf{x}^n(i) \theta(i) $$

Questa formulazione è particolarmente interessante poiché ammette un'implementazione ricorsiva efficiente grazie all'applicazione del lemma di Sherman-Morrison.

## Generalizzazione del Modello

Si consideri ora la ricerca di una soluzione LS nella forma lineare generale:

$$ \widehat{\theta}(\mathbf{x}^n) = \mathbf{a}^T \mathbf{x}^n + b $$

Attraverso calcoli analitici, si ottiene la formulazione **LMS generale**:

$$ \mathbf{a}_{\text{LMS}} = (\mathbf{X}_0 \mathbf{X}_0^T)^{-1} \mathbf{X}_0 \mathbf{y}_0, \qquad b_{\text{LMS}} = \underbrace{\frac{1}{p} \sum_{i=1}^{p} \theta(i)}_{\widetilde{\theta}} - \frac{1}{p} \mathbf{1}_p^T \mathbf{X}^T \mathbf{a}_{\text{LMS}} $$

dove $\mathbf{1}_p$ è un vettore di unità $p$-dimensionale. Le matrici e i vettori coinvolti sono definiti come segue:

$$ \mathbf{X}_0 = \begin{bmatrix} x_1(1) - \bar{x}_1 & \dots & x_1(p) - \bar{x}_1 \\ \vdots & \ddots & \vdots \\ x_n(1) - \bar{x}_n & \dots & x_n(p) - \bar{x}_n \end{bmatrix} \in \mathbb{R}^{n \times p}, \quad \mathbf{y}_0 = [y_1 - \bar{\theta}, \dots, y_p - \bar{\theta}]^T $$

con le medie:

$$ \bar{x}_k = \frac{1}{p} \sum_{i=1}^{p} x_k(i) \iff \bar{\mathbf{x}} = \frac{1}{p} \sum_{i=1}^{p} \mathbf{x}^n(i), \quad \mathbf{X}_0 = \mathbf{X} - \bar{\mathbf{x}}\mathbf{1}_p^T $$