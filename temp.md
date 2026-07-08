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

##### Proprietà della matrice di covarianza

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

