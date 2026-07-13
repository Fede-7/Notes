<h1>Modelli Statistici e Inferenza (MSI)</h1>

*Questo documento copre l'intera teoria della probabilità e dell'inferenza statistica, partendo dalle fondamenta insiemistiche fino ai metodi avanzati di stima dei parametri. Il percorso segue la progressione: **fondamenti probabilistici → variabili aleatorie discrete → variabili aleatorie continue → vettori aleatori → processi aleatori → convergenza → inferenza statistica (Bayesiana e non)**. Ogni macro-area introduce i concetti necessari per comprendere quelli successivi, dal singolo evento fino agli stimatori a parametri multipli.*

---

<h2>PARTE I — Fondamenti di Probabilità</h2>

<h3>1. Definizioni di Base</h3>

**1.1 Spazio campionario ed eventi**

<ul>
<li><strong>Esperimento</strong>: operazione il cui esito appartiene a un insieme di possibilità predefinite, non noto a priori (es. lancio di un dado).</li>
<li><strong>Spazio dei campioni</strong> $\Omega$: insieme di tutti i risultati possibili. In questo corso si assume <strong>discreto</strong> (finito o numerabile).</li>
<li><strong>Evento</strong>: sotto-insieme di $\Omega$, definito matematicamente dai suoi elementi e lessicalmente da una proposizione.</li>
<li><strong>Evento elementare</strong> $\omega \in \Omega$: uno dei $|\Omega|$ elementi di $\Omega$.</li>
</ul>

> **Nota**: un evento è univocamente determinato dagli elementi che lo compongono; la proposizione lessicale che lo descrive non è unica.

**1.2 Nomenclatura probabilistica**

<ul>
<li>$\Omega$: <strong>evento certo</strong></li>
<li>$\emptyset$: <strong>evento impossibile</strong></li>
<li>$A$ e $A^c$: <strong>eventi complementari</strong></li>
<li>$A \cap B = \emptyset$: eventi <strong>incompatibili</strong> (mutuamente esclusivi)</li>
<li>$A \subseteq B$: $A$ <strong>implica</strong> $B$</li>
</ul>

<h3>2. Richiami di Insiemistica</h3>

Siano $\{A_i\}_{i=1}^M$ sotto-insiemi di $\Omega$.

**2.1 Operazioni fondamentali**

<ol>
<li><strong>Unione</strong> $A_1 \cup A_2$: insieme di tutti gli elementi di $A_1$ e $A_2$ (senza ripetizioni).</li>
<li><strong>Complemento</strong> $\overline{A_1}$: elementi di $\Omega$ non appartenenti a $A_1$. Vale: $\overline{\Omega} = \emptyset$, $\overline{\overline{A_1}} = A_1$, $A_1 \cup \overline{A_1} = \Omega$.</li>
<li><strong>Intersezione</strong> $A_1 \cap A_2$: elementi comuni ad entrambi.</li>
<li><strong>Sottrazione</strong> $A_1 \setminus A_2 = A_1 \cap \overline{A_2}$: elementi di $A_1$ non in $A_2$.</li>
</ol>

**2.2 Proprietà**

<ul>
<li><strong>De Morgan</strong>: $\overline{A_1 \cup A_2} = \overline{A_1} \cap \overline{A_2}$</li>
<li><strong>Associatività</strong>: $(A_1 \cup A_2) \cup A_3 = A_1 \cup (A_2 \cup A_3)$</li>
<li><strong>Distributività</strong>: $A_1 \cup \left(\bigcap_{i=2}^M A_i\right) = \bigcap_{i=2}^M (A_1 \cup A_i)$</li>
</ul>

<h3>3. Calcolo Combinatorio</h3>

**3.1 Spazi finiti con eventi elementari equiprobabili**

Per uno spazio finito con eventi elementari **equiprobabili**, la frequenza di occorrenza converge alla probabilità:

$$f_n(A) = \frac{n_A}{n} \longrightarrow \frac{|A|}{|\Omega|}, \quad n \to \infty$$

Il calcolo della probabilità si riduce al **conteggio delle cardinalità** dei sotto-insiemi → **calcolo combinatorio**.

**3.2 Prodotto Cartesiano**

Dati $k$ insiemi finiti $A_1, \ldots, A_k$, il prodotto cartesiano $A^{(k)} = A_1 \times \ldots \times A_k$ è l'insieme delle $k$-ple ordinate. La sua cardinalità è:

$$\left|A^{(k)}\right| = \prod_{i=1}^k |A_i|$$

**3.3 $k$-ple ordinate senza ripetizione**

Date $n$ elementi, le stringhe di lunghezza $k$ **senza ripetizioni**:

$$\left|A^{(k)}\right| = n(n-1)(n-2)\cdots(n-k+1) = \prod_{i=0}^{k-1}(n-i)$$

**3.4 Permutazioni**

Caso speciale con $k = n$: numero di $n$-ple ordinate di $n$ elementi distinti.

$$\text{Permutazioni di } n \text{ elementi} = n!$$

**3.5 Combinazioni (Coefficiente Binomiale)**

Le **combinazioni** $C_{n,k}$ contano i sotto-insiemi di cardinalità $k$ (l'ordine non è rilevante):

$$C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

Le $k!$ permutazioni di una stessa $k$-pla "collassano" in un'unica combinazione.

**3.6 Insieme delle Parti**

Dato $A$ con $n$ elementi, l'**insieme delle parti** $\mathcal{P}(A)$ contiene tutti i possibili sotto-insiemi di $A$:

$$|\mathcal{P}(A)| = \sum_{k=0}^n \binom{n}{k} = 2^n$$

<h3>4. Definizione di Probabilità (Approccio Frequentista)</h3>

**4.1 Dalla frequenza alla probabilità**

La **probabilità** di un evento $A$ è il limite della frequenza di occorrenza:

$$\mathbb{P}(A) = \lim_{n \to \infty} \frac{n_A}{n}$$

Per spazi **finiti a eventi elementari equiprobabili**:

$$\mathbb{P}(A) = \frac{|\Omega_A|}{|\Omega|}$$

**4.2 Proprietà di frequenza e probabilità**

Per eventi $A$ e $B$:

<ul>
<li><strong>Complementari</strong>: $\mathbb{P}(\overline{A}) = 1 - \mathbb{P}(A)$</li>
<li><strong>Sub-additività</strong>: $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$</li>
<li><strong>Sottrazione</strong>: $\mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$</li>
<li><strong>Evento certo/impossibile</strong>: $\mathbb{P}(\Omega) = 1$, $\mathbb{P}(\emptyset) = 0$</li>
</ul>

<h3>5. Probabilità Condizionata</h3>

**5.1 Definizione**

La **frequenza condizionata** di $A$ dato $B$, e il suo limite (probabilità condizionata):

$$f_n(A|B) = \frac{n_{A \cap B}}{n_B} \quad \to \quad \mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

**5.2 Legge della probabilità composta**

$$\mathbb{P}(A \cap B) = \mathbb{P}(B|A)\,\mathbb{P}(A) = \mathbb{P}(A|B)\,\mathbb{P}(B)$$

**5.3 Legge della probabilità totale**

Sia $\{B_i\}_{i=1}^k$ una **partizione** di $\Omega$ ($\bigcup B_i = \Omega$, $B_i \cap B_j = \emptyset$):

$$\boxed{\mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(A|B_i)\,\mathbb{P}(B_i)}$$

**5.4 Eventi indipendenti**

$A$ e $B$ sono **indipendenti** se il verificarsi di uno non influenza l'altro:

$$\mathbb{P}(A \cap B) = \mathbb{P}(A)\,\mathbb{P}(B)$$

<h3>6. Approccio Assiomatico alla Probabilità</h3>

**6.1 Algebra di eventi**

Una famiglia $\mathcal{E}$ di sotto-insiemi di $\Omega$ è un'**algebra** se è chiusa rispetto a:

<ul>
<li>Unione: $A_1, A_2 \in \mathcal{E} \Rightarrow A_1 \cup A_2 \in \mathcal{E}$</li>
<li>Complementazione: $A_1 \in \mathcal{E} \Rightarrow \overline{A_1} \in \mathcal{E}$</li>
</ul>

Se $\mathcal{E}$ ha infiniti elementi ed è chiusa anche rispetto all'unione numerabile, si chiama **$\sigma$-algebra**.

**6.2 Proprietà delle algebre**

<ul>
<li>$A, B \in \mathcal{E} \Rightarrow A \cap B \in \mathcal{E}$ (per De Morgan)</li>
<li>$A, B \in \mathcal{E} \Rightarrow A \setminus B \in \mathcal{E}$</li>
<li>La minima algebra contenente $A$ è $\mathcal{E} = \{A, \overline{A}, \Omega, \emptyset\}$</li>
</ul>

**6.3 Assiomi di Kolmogorov**

Una **legge di probabilità** è una funzione $\mathbb{P}: \mathcal{E} \to [0,1]$ che soddisfa:

<ol>
<li><strong>Non negatività</strong>: $\mathbb{P}(A) \geq 0 \quad \forall A \in \mathcal{E}$</li>
<li><strong>Normalizzazione</strong>: $\mathbb{P}(\Omega) = 1$</li>
<li><strong>Sub-additività</strong>: $A \cap B = \emptyset \Rightarrow \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$
  <ul><li><strong>3a. Numerabile additività</strong>: $\mathbb{P}\!\left(\bigcup_{n=1}^\infty B_n\right) = \sum_{n=1}^\infty \mathbb{P}(B_n)$ per $B_n$ incompatibili.</li></ul>
</li>
</ol>

La terna $(\Omega, \mathcal{E}, \mathbb{P})$ è uno **Spazio di Probabilità**.

---

<h2>PARTE II — Variabili Aleatorie Discrete</h2>

<h3>7. Variabile Aleatoria: Definizioni Fondamentali</h3>

**7.1 Definizione**

Una **variabile aleatoria (VA)** è una funzione $X: \Omega \to \mathbb{R}$ che associa a ogni esito $\omega$ un numero reale $x = X(\omega)$.

**7.2 Strumenti di distribuzione**

<ul>
<li><strong>PMF</strong> (Probability Mass Function): $p_X(x) = \mathbb{P}(X = x)$ per VA discrete.</li>
<li><strong>PDF</strong> (Probability Density Function): $f_X(x)$ per VA continue, tale che $\mathbb{P}(a \leq X \leq b) = \int_a^b f_X(x)\,dx$.</li>
<li><strong>CDF</strong> (Cumulative Distribution Function / Funzione di Ripartizione): $F_X(x) = \mathbb{P}(X \leq x)$.</li>
</ul>

Relazioni tra le funzioni:

<ul>
<li>Caso discreto: $F_X(x) = \sum_{x_i \leq x} p_X(x_i)$</li>
<li>Caso continuo: $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$</li>
</ul>

> **Nota di linguaggio**: nel gergo ingegneristico, "pdf" o "DF" sono spesso usati come sinonimi generici della legge di distribuzione, indipendentemente dal tipo di VA.

**7.3 Proprietà della PMF**

$$p_X(x) \geq 0 \qquad \sum_{x \in \mathcal{X}} p_X(x) = 1$$

<h3>8. Media e Valor Atteso (Discreto)</h3>

**8.1 Media campionaria**

Data una successione di $n$ osservazioni $[X(\omega_1), \ldots, X(\omega_n)]$:

$$\overline{X_n} = \frac{1}{n}\sum_{i=1}^n X(\omega_i)$$

**8.2 Valore atteso (media statistica)**

Per $n \to \infty$, la media campionaria converge alla **media statistica**:

$$\mathbb{E}[X] = \sum_{i=1}^M x_i\, p_X(x_i)$$

> **Legge dei Grandi Numeri**: al crescere delle osservazioni, la media campionaria converge al valore atteso teorico.

<h3>9. Distribuzioni Discrete Notevoli</h3>

**9.1 Variabile Uniforme**

$X \sim \mathcal{U}(\mathcal{X})$ con $|\mathcal{X}| = M$:

$$p_X(x) = \frac{1}{M} \quad \forall x \in \mathcal{X} \qquad \mathbb{E}[X] = \frac{1}{M}\sum_{x \in \mathcal{X}} x = \text{media aritmetica dei valori}$$

**9.2 Variabile Poissoniana**

$X \sim \mathcal{P}(\lambda)$ con $\mathcal{X} = \mathbb{N}_0$:

$$p_X(k) = \frac{\lambda^k}{k!}\,e^{-\lambda}, \quad k \in \mathbb{N}_0 \qquad \mathbb{E}[X] = \lambda$$

Verifica di normalizzazione: $\sum_{k=0}^\infty \frac{e^{-\lambda}\lambda^k}{k!} = e^{-\lambda} e^\lambda = 1$.

<h3>10. PMF Condizionali e Medie Condizionate</h3>

**10.1 PMF condizionale**

Per un evento $A$ con $\mathbb{P}(A) > 0$:

$$p_{X|A}(x) = \mathbb{P}(X=x|A) = \frac{\mathbb{P}(\{X=x\} \cap A)}{\mathbb{P}(A)}$$

**10.2 Regola della probabilità totale per le PMF**

Data una partizione $\{E_i\}_{i=1}^M$ di $\Omega$:

$$p_X(x) = \sum_{i=1}^M p_{X|E_i}(x)\,\mathbb{P}(E_i)$$

**10.3 Media condizionata**

$$\mathbb{E}[X|E_i] = \sum_{x \in \mathcal{X}} x\, p_{X|E_i}(x) \qquad \mathbb{E}[X] = \sum_{i=1}^M \mathbb{P}(E_i)\,\mathbb{E}[X|E_i]$$

<h3>11. Funzioni di Variabili Aleatorie (Discrete)</h3>

**11.1 Definizione**

Data $X$ con PMF $p_X$ e funzione $g(\cdot)$, si forma $Y = g(X) \in \mathcal{Y} = g(\mathcal{X})$.

**11.2 Calcolo della PMF di Y**

<ul>
<li><strong>Caso biunivoco</strong> ($|Y| = |X|$): semplice ridenominazione → $p_Y(y_i) = p_X(g^{-1}(y_i))$.</li>
<li><strong>Caso univoco</strong> (più valori di $X$ mappano in uno di $Y$): accumulo delle masse. Per $y_k$ tale che $g(x_1^{(k)}) = \ldots = g(x_{L_k}^{(k)}) = y_k$: $$p_Y(y_k) = \sum_{i=1}^{L_k} p_X(x_i^{(k)})$$</li>
</ul>

**11.3 Media di funzioni di VA (Teorema Fondamentale)**

$$\boxed{\mathbb{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x)\, p_X(x)}$$

<h3>12. Valore Quadratico Medio, Varianza e Deviazione Standard</h3>

**12.1 Definizioni**

Data $X \sim p_X(x)$ con media $\mu_X = \mathbb{E}[X]$:

<ul>
<li><strong>Valore quadratico medio</strong> (Mean Square): $X_\text{rms}^2 = \mathbb{E}[X^2] = \sum_{x} x^2\, p_X(x)$</li>
<li><strong>Valore efficace</strong> (RMS): $X_\text{rms} = \sqrt{\mathbb{E}[X^2]}$</li>
<li><strong>Varianza</strong>: $\sigma_X^2 = \mathbb{E}[(X-\mu_X)^2] = X_\text{rms}^2 - \mu_X^2$</li>
<li><strong>Deviazione standard</strong>: $\sigma_X = \sqrt{\sigma_X^2}$</li>
</ul>

**12.2 Proprietà di media e varianza**

<ul>
<li><strong>Media — Linearità</strong>: $\mathbb{E}[aX+b] = a\,\mathbb{E}[X] + b$</li>
<li><strong>Media — Non-negatività</strong>: se $X(\omega) \geq 0$ per ogni $\omega$, allora $\mathbb{E}[X] \geq 0$</li>
<li><strong>Varianza — Non-negatività</strong>: $\sigma_X^2 \geq 0$</li>
<li><strong>Varianza — Trasformazione lineare</strong> $Y = aX+b$: $\sigma_Y^2 = a^2\,\sigma_X^2$</li>
<li>Per $\mu_X = 0$: $\sigma_X^2 = X_\text{rms}^2$</li>
</ul>

**12.3 Significato di varianza e deviazione standard**

Il rapporto $\mu_X / \sigma_X$ misura la "concentrazione" della distribuzione:

<ul>
<li>Valore elevato → PMF molto concentrata attorno alla media (VA "poco aleatoria").</li>
<li>Valore basso → elevata aleatorietà.</li>
</ul>

**12.4 Disuguaglianza di Chebyshev**

Sia $Z \geq 0$ con PMF $p_Z(z)$ e $\delta > 0$:

$$\mathbb{P}(Z \geq \delta) \leq \frac{\mathbb{E}[Z^2]}{\delta^2}$$

Ponendo $Z = |X - \mu_X|$ e $\delta = k\sigma_X$:

$$\mathbb{P}\{|X - \mu_X| > k\sigma_X\} \leq \frac{1}{k^2} \quad\Longleftrightarrow\quad \mathbb{P}\{\mu_X - k\sigma_X \leq X \leq \mu_X + k\sigma_X\} \geq 1 - \frac{1}{k^2}$$

<h3>13. Variabili Aleatorie Multiple (Discrete)</h3>

**13.1 Definizione di variabile doppia**

$$(X, Y): \omega \mapsto (X(\omega), Y(\omega)) \in \mathcal{X} \times \mathcal{Y} \subseteq \mathbb{R}^2$$

**13.2 PMF congiunta**

$$p_{X,Y}(x,y) = \mathbb{P}(\{X=x\} \cap \{Y=y\}) \qquad p_{X,Y}(x,y) \geq 0, \quad \sum_x\sum_y p_{X,Y}(x,y) = 1$$

**13.3 Marginalizzazione**

$$p_X(x) = \sum_{y \in \mathcal{Y}} p_{X,Y}(x,y) \qquad p_Y(y) = \sum_{x \in \mathcal{X}} p_{X,Y}(x,y)$$

> Caratterizzare congiuntamente $(X,Y)$ implica caratterizzarle marginalmente; non vale il viceversa.

**13.4 Variabili indipendenti**

$X$ e $Y$ sono **indipendenti** $\iff$:

$$p_{X,Y}(x,y) = p_X(x)\, p_Y(y)$$

Generalizzazione a $m$ variabili: $p_{X_1,\ldots,X_m}(x_1,\ldots,x_m) = \prod_{i=1}^m p_{X_i}(x_i)$.

**13.5 PMF condizionate**

$$p_{Y|X}(y|x) = \frac{p_{X,Y}(x,y)}{p_X(x)}$$

> **Legge di Bayes**: $$p_{X|Y}(x|y) = \frac{p_{Y|X}(y|x)\, p_X(x)}{p_Y(y)}$$

**Regola della catena** per tre variabili $(X,Y,Z)$:

$$p_{X,Y,Z}(x,y,z) = p_{Z|X,Y}(z|x,y)\, p_{Y|X}(y|x)\, p_X(x)$$

**13.6 Funzioni di variabili doppie**

Data $Z = g(X,Y)$:

<ul>
<li><strong>Trasformazione biunivoca</strong>: $p_Z(z) = p_{X,Y}(x(z), y(z))$</li>
<li><strong>Trasformazione non biunivoca</strong>: $p_Z(z) = \sum_{(x,y) \in \mathcal{A}(z)} p_{X,Y}(x,y)$ dove $\mathcal{A}(z) = \{(x,y): g(x,y)=z\}$</li>
</ul>

**Valore atteso (Teorema del Calcolo della Media)**:

$$\mathbb{E}[Z] = \mathbb{E}[g(X,Y)] = \sum_{x \in \mathcal{X}}\sum_{y \in \mathcal{Y}} g(x,y)\, p_{X,Y}(x,y)$$

**Linearità del valore atteso** (indipendentemente dalla dipendenza statistica):

$$\mathbb{E}[aX+bY] = a\,\mathbb{E}[X] + b\,\mathbb{E}[Y] \qquad \mathbb{E}\!\left[\sum_{i=1}^m a_i X_i\right] = \sum_{i=1}^m a_i\,\mathbb{E}[X_i]$$

**13.7 Teorema della Media Condizionata (Law of Iterated Expectations)**

$$\boxed{\mathbb{E}[g(X,Y)] = \mathbb{E}\!\left[\mathbb{E}[g(X,Y)|Y]\right]}$$

dove $\mathbb{E}[g(X,Y)|Y=y] = \sum_{x \in \mathcal{X}} g(x,y)\, p_{X|Y}(x|y)$.

<h3>14. Covarianza e Correlazione (Discreto)</h3>

**14.1 Covarianza**

$$\text{COV}[X,Y] = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)] = \mathbb{E}[XY] - \mu_X\mu_Y$$

<ul>
<li>$\text{COV} > 0$: le variabili tendono a crescere insieme.</li>
<li>$\text{COV} < 0$: tendono a muoversi in direzioni opposte.</li>
</ul>

**14.2 Correlazione (Cross-correlazione)**

$$R_{X,Y} = \mathbb{E}[XY] = \sum_x\sum_y xy\, p_{X,Y}(x,y)$$

**14.3 Incorrelazione vs Indipendenza**

<ul>
<li><strong>Indipendenza</strong> $\Rightarrow$ <strong>Incorrelazione</strong> ($\text{COV}[X,Y]=0$).</li>
<li><strong>Incorrelazione</strong> $\nRightarrow$ <strong>Indipendenza</strong> (possibile dipendenza non lineare).</li>
</ul>

**14.4 Coefficiente di Correlazione di Pearson**

$$\rho_{X,Y} = \frac{\text{COV}[X,Y]}{\sigma_X\,\sigma_Y} \in [-1, 1]$$

Dimostrazione del bound: $0 \leq \mathbb{E}\!\left[\left(\frac{X-\mu_X}{\sigma_X} \pm \frac{Y-\mu_Y}{\sigma_Y}\right)^2\right] = 2 \pm 2\frac{\text{COV}[X,Y]}{\sigma_X\sigma_Y}$.

**14.5 Varianza di una combinazione lineare**

Per $Z = aX + bY$:

$$\sigma_Z^2 = a^2\sigma_X^2 + b^2\sigma_Y^2 + 2ab\,\text{COV}[X,Y]$$

---

<h2>PARTE III — Variabili Aleatorie Continue</h2>

<h3>15. Introduzione alle Variabili Continue</h3>

Quando $\Omega \subseteq \mathbb{R}$, la probabilità di un singolo punto è nulla ($\mathbb{P}(X=x)=0$). L'analisi si sposta dai punti agli **intervalli**.

**15.1 PDF — Densità di Probabilità**

$$f_X(x) = \lim_{\Delta x \to 0} \frac{\mathbb{P}\!\left(x - \frac{\Delta x}{2} \leq X \leq x + \frac{\Delta x}{2}\right)}{\Delta x}$$

La probabilità su un intervallo si calcola per integrazione:

$$\mathbb{P}(a \leq X \leq b) = \int_a^b f_X(t)\,dt$$

**Vincoli fondamentali**:

<ul>
<li>Non-negatività: $f_X(x) \geq 0 \quad \forall x \in \mathbb{R}$</li>
<li>Normalizzazione: $\int_{-\infty}^{+\infty} f_X(t)\,dt = 1$</li>
</ul>

**15.2 Raccordo discreto–continuo**

<ul>
<li><strong>Discreto</strong>: $\mathbb{P}(A) = \sum_{x \in A} p_X(x)$</li>
<li><strong>Continuo</strong>: $\mathbb{P}(A) = \int_A f_X(x)\,dx$</li>
</ul>

<h3>16. CDF e CCDF per Variabili Continue</h3>

**16.1 CDF (Cumulative Distribution Function)**

$$F_X(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^x f_X(t)\,dt \implies f_X(x) = \frac{dF_X(x)}{dx}$$

**Proprietà**:

<ul>
<li>$F_X(x) \in [0,1]$</li>
<li>$F_X(-\infty) = 0$, $F_X(+\infty) = 1$</li>
<li>$F_X(x)$ è continua e crescente</li>
</ul>

**Calcolo degli intervalli**:

$$\mathbb{P}(a_1 \leq X \leq a_2) = F_X(a_2) - F_X(a_1)$$

**16.2 CCDF (Complementare)**

$$\overline{F}_X(x) = \mathbb{P}(X > x) = 1 - F_X(x) \implies f_X(x) = -\frac{d\overline{F}_X(x)}{dx}$$

<h3>17. Media Statistica di Variabili Continue</h3>

$$\mathbb{E}[X] = \mu_X = \int_{\mathbb{R}} x\, f_X(x)\,dx$$

**Giustificazione** (limite della versione discreta quantizzata): quantizzando $X$ in intervalli $\Delta$, la sommatoria di Riemann converge all'integrale per $\Delta \to 0$.

**Visione unificata (Integrale di Lebesgue)**:

$$\mathbb{E}[X] = \int_\Omega X(\omega)\,dP(\omega)$$

che si riduce a sommatoria nel caso discreto e a integrale di Riemann nel continuo.

<h3>18. Distribuzioni Continue Notevoli</h3>

**18.1 Variabile Uniforme**

$X \sim \mathcal{U}(a,b)$:

$$f_X(x) = \begin{cases} \frac{1}{b-a} & x \in [a,b] \\ 0 & \text{altrove} \end{cases} \qquad F_X(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \leq x \leq b \\ 1 & x \geq b \end{cases} \qquad \mathbb{E}[X] = \frac{a+b}{2}$$

**18.2 Variabile Esponenziale**

$X \sim \mathcal{E}(\lambda)$, con $\lambda > 0$ e $\text{supp}(X) = [0, +\infty)$:

$$f_X(x) = \lambda e^{-\lambda x}\, u(x) \qquad F_X(x) = (1 - e^{-\lambda x})\, u(x) \qquad \mathbb{E}[X] = \frac{1}{\lambda}$$

**18.3 Variabile Laplaciana**

$X \sim \mathcal{L}(\lambda)$, con $\text{supp}(X) = \mathbb{R}$:

$$f_X(x) = \frac{\lambda}{2}e^{-\lambda|x|} \qquad \mathbb{E}[X] = 0 \quad \text{(pdf pari)}$$

$$F_X(x) = \begin{cases} \frac{1}{2}e^{\lambda x} & x \leq 0 \\ 1 - \frac{1}{2}e^{-\lambda x} & x \geq 0 \end{cases}$$

**18.4 Variabile di Cauchy**

$X \sim \mathcal{C}(a,b)$, con $b > 0$ e $\text{supp}(X) = \mathbb{R}$:

$$f_X(x) = \frac{1}{b\pi}\cdot\frac{1}{1+\left(\frac{x-a}{b}\right)^2} \qquad F_X(x) = \frac{1}{2} + \frac{1}{\pi}\arctan\!\left(\frac{x-a}{b}\right)$$

La media **non è definita** (l'integrale di $|x|\,f_X(x)$ non converge), ma è definibile un punto di simmetria tramite il valore principale di Cauchy: $\lim_{H\to\infty}\int_{-H}^H x\,f_X(x)\,dx = a$.

<h3>19. PDF Condizionata e Legge della Probabilità Totale (Continuo)</h3>

**19.1 PDF condizionata**

Tramite CDF condizionata:

$$F_{X|A}(x) = \frac{\mathbb{P}(\{X \leq x\} \cap A)}{\mathbb{P}(A)} \implies f_{X|A}(x) = \frac{d}{dx}F_{X|A}(x)$$

**19.2 Legge della probabilità totale per PDF, CDF e medie**

Data una partizione $\{E_m\}_{m=1}^M$:

$$f_X(x) = \sum_{m=1}^M f_{X|E_m}(x)\,\mathbb{P}(E_m) \qquad F_X(x) = \sum_{m=1}^M F_{X|E_m}(x)\,\mathbb{P}(E_m)$$

$$\mathbb{E}[X] = \sum_{m=1}^M \mathbb{E}[X|E_m]\,\mathbb{P}(E_m) \qquad \text{con } \mathbb{E}[X|E_m] = \int_{-\infty}^{+\infty} x\, f_{X|E_m}(x)\,dx$$

<h3>20. Funzioni di Variabili Aleatorie Continue</h3>

Data $Y = g(X)$, si distinguono tre casi.

**20.1 Caso 1 — Funzione invertibile (biunivoca)**

Formula unificata per funzioni strettamente monotone:

$$f_Y(y) = \frac{f_X[g^{-1}(y)]}{|g'[g^{-1}(y)]|}$$

<ul>
<li><strong>Crescente</strong> ($g'(x)>0$): $F_Y(y) = F_X[g^{-1}(y)]$</li>
<li><strong>Decrescente</strong> ($g'(x)<0$): $F_Y(y) = 1 - F_X[g^{-1}(y)]$</li>
</ul>

**20.2 Caso 2 — Funzione non invertibile (univoca con $Y$ continuo)**

Se $y$ è generato da più punti $\{x_i(y)\}$:

$$f_Y(y) = \sum_i \frac{f_X[x_i(y)]}{|g'[x_i(y)]|}$$

**Procedura operativa**:

<ol>
<li>Parti dalla CDF: $F_Y(y) = \mathbb{P}(Y \leq y) = \mathbb{P}(g(X) \leq y)$</li>
<li>Esplicita l'evento: risolvi la disequazione $g(X) \leq y$</li>
<li>Calcola la probabilità con $F_X$ o integrando $f_X$</li>
<li>Deriva: $f_Y(y) = \frac{dF_Y(y)}{dy}$</li>
</ol>

**20.3 Caso 3 — Conversione A/D (univoca con $Y$ discreto)**

Mappatura di $X$ continua in $Y$ discreta con $M = 2^R$ livelli (rappresentazione a $R$ bit):

$$Y = y_i \quad \text{se} \quad x_i \leq X < x_{i+1} \qquad p_Y(y_i) = F_X(x_{i+1}) - F_X(x_i)$$

<h3>21. Valore Quadratico Medio e Varianza (Continuo)</h3>

$$X_\text{rms}^2 = \mathbb{E}[X^2] = \int_\mathbb{R} x^2 f_X(x)\,dx \qquad X_\text{rms} = \sqrt{\mathbb{E}[X^2]}$$

$$\sigma_X^2 = \mathbb{E}[(X-\mu_X)^2] = X_\text{rms}^2 - \mu_X^2 \qquad \sigma_X = \sqrt{\sigma_X^2}$$

Tutte le proprietà di linearità e invarianza valide per il caso discreto si applicano analogamente.

<h3>22. Variabili Continue Multiple</h3>

**22.1 Definizione di vettore aleatorio**

$$(X_1, \ldots, X_m): \omega \mapsto (X_1(\omega),\ldots,X_m(\omega)) \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_m \subseteq \mathbb{R}^m$$

**22.2 PDF congiunta di due variabili continue**

$$f_{X,Y}(x,y) = \lim_{\Delta x \to 0}\lim_{\Delta y \to 0} \frac{\mathbb{P}\!\left(\{x-\frac{\Delta x}{2} \leq X \leq x+\frac{\Delta x}{2}\} \cap \{y-\frac{\Delta y}{2} \leq Y \leq y+\frac{\Delta y}{2}\}\right)}{\Delta x\,\Delta y}$$

**Vincoli**: $f_{X,Y}(x,y) \geq 0$ e $\int_{\mathbb{R}^2} f_{X,Y}(x,y)\,dx\,dy = 1$.

**Marginalizzazione**:

$$\int_\mathbb{R} f_{X,Y}(x,y)\,dy = f_X(x) \qquad \int_\mathbb{R} f_{X,Y}(x,y)\,dx = f_Y(y)$$

**Indipendenza statistica**:

$$f_{X,Y}(x,y) = f_X(x)\,f_Y(y) \iff F_{X,Y}(x,y) = F_X(x)\,F_Y(y)$$

**22.3 PDF condizionate**

$$f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$$

**Legge di Bayes per densità**:

$$f_{Y|X}(y|x) = \frac{f_Y(y)\, f_{X|Y}(x|y)}{f_X(x)}$$

**Legge della probabilità totale**:

$$f_X(x) = \int_\mathbb{R} f_{X|Y}(x|y)\, f_Y(y)\,dy$$

**22.4 Valore atteso, linearità e teorema della media condizionata**

Per $Z = g(X,Y)$:

$$\mathbb{E}[Z] = \int_{\mathbb{R}^2} g(x,y)\, f_{X,Y}(x,y)\,dx\,dy$$

**Linearità**: $\mathbb{E}\!\left[\sum_{i=1}^m a_i X_i\right] = \sum_{i=1}^m a_i\,\mathbb{E}[X_i]$

**Teorema della Media Condizionata**:

$$\mathbb{E}[g(X,Y)] = \mathbb{E}\!\left[\mathbb{E}[g(X,Y)|Y]\right] \qquad \text{con } \mathbb{E}[g(X,Y)|Y=y] = \int_\mathbb{R} g(x,y)\, f_{X|Y}(x|y)\,dx$$

**22.5 Covarianza tra variabili continue**

$$\text{COV}[X,Y] = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)] = \mathbb{E}[XY] - \mu_X\mu_Y \qquad \rho_{X,Y} = \frac{\text{COV}[X,Y]}{\sigma_X\sigma_Y}, \quad |\rho_{X,Y}| \leq 1$$

> Indipendenza $\Rightarrow$ Incorrelazione; Incorrelazione $\nRightarrow$ Indipendenza.

<h3>23. Variabili Gaussiane</h3>

**23.1 Gaussiana standard e Gaussiana generica**

**Gaussiana standard** $X_0 \sim \mathcal{N}(0,1)$:

$$f_{X_0}(x_0) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x_0^2}{2}} \qquad \mathbb{E}[X_0] = 0, \quad \sigma_{X_0}^2 = 1$$

**Gaussiana generica** $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ tramite trasformazione lineare $X = \sigma_X X_0 + \mu_X$:

$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma_X^2}}\exp\!\left[-\frac{(x-\mu_X)^2}{2\sigma_X^2}\right] \qquad \mathbb{E}[X] = \mu_X, \quad \text{VAR}[X] = \sigma_X^2$$

**23.2 Funzione Q(x)**

La CDF della Gaussiana standard non ha forma chiusa. Si definisce la **funzione Q**:

$$Q(x) \stackrel{\text{def}}{=} \mathbb{P}(X_0 \geq x) = \frac{1}{\sqrt{2\pi}}\int_x^\infty e^{-\frac{t^2}{2}}\,dt$$

**Relazioni**:

<ul>
<li>$F_{X_0}(x) = 1 - Q(x)$</li>
<li><strong>Simmetria</strong>: $Q(-x) = 1 - Q(x)$</li>
<li>Monotona decrescente: $\frac{dQ(x)}{dx} = -\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}} < 0$</li>
<li>Andamento asintotico: $Q(x) \sim \frac{1}{x\sqrt{2\pi}}e^{-\frac{x^2}{2}}$ per $x \to \infty$</li>
</ul>

Per $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$:

$$\mathbb{P}(X \geq \eta) = Q\!\left(\frac{\eta - \mu_X}{\sigma_X}\right) \qquad 1 - F_X(x) = Q\!\left(\frac{x-\mu_X}{\sigma_X}\right)$$

**23.3 Caratterizzazione congiunta di variabili Gaussiane**

Dati $X_1 \sim \mathcal{N}(\mu_1, \sigma_1^2)$ e $X_2 \sim \mathcal{N}(\mu_2, \sigma_2^2)$, vettore $\mathbf{X} = (X_1, X_2)^T$.

**Matrice di covarianza**:

$$\mathbf{K}_\mathbf{X} = \mathbb{E}[(\mathbf{X}-\boldsymbol{\mu}_\mathbf{X})(\mathbf{X}-\boldsymbol{\mu}_\mathbf{X})^T] = \begin{pmatrix} \sigma_1^2 & \sigma_1\sigma_2\rho_{1,2} \\ \sigma_1\sigma_2\rho_{1,2} & \sigma_2^2 \end{pmatrix}$$

Proprietà: simmetrica, definita non-negativa, invertibile se $\rho_{1,2} \neq \pm 1$.

**PDF congiunta Gaussiana** $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}_\mathbf{X}, \mathbf{K}_\mathbf{X})$:

$$f_\mathbf{X}(\mathbf{x}) = \frac{1}{2\pi|\mathbf{K}_\mathbf{X}|^{1/2}}\exp\!\left[-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_\mathbf{X})^T \mathbf{K}_\mathbf{X}^{-1}(\mathbf{x}-\boldsymbol{\mu}_\mathbf{X})\right]$$

**Caso speciale** ($\rho_{1,2}=0$): la pdf congiunta si fattorizza → **incorrelazione implica indipendenza** (proprietà esclusiva della Gaussiana congiunta).

**23.4 Chiusura rispetto a trasformazioni lineari**

Se $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}_\mathbf{X}, \mathbf{K}_\mathbf{X})$ e $\mathbf{Z} = \mathbf{A}\mathbf{X} + \mathbf{b}$:

$$\mathbf{Z} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu}_\mathbf{X} + \mathbf{b},\; \mathbf{A}\mathbf{K}_\mathbf{X}\mathbf{A}^T)$$

---

<h2>PARTE IV — Vettori Aleatori</h2>

<h3>24. Definizione e Caratterizzazione Completa</h3>

**24.1 Vettore aleatorio (n-pla)**

$$(X_1, \ldots, X_n): \omega \mapsto \mathbf{X}(\omega) = [X_1(\omega),\ldots,X_n(\omega)]^T \in \mathcal{X}_1 \times \ldots \times \mathcal{X}_n \subseteq \mathbb{R}^n$$

**24.2 Caratterizzazione completa**

Una VA è **completamente caratterizzata** quando è nota la sua funzione di distribuzione.

**Caso singolo**:

<ul>
<li>CDF: $F_X(x) = \mathbb{P}\{X \leq x\}$</li>
<li>PMF (discreto): $p_X(x) = \mathbb{P}\{X = x\}$</li>
<li>PDF (continuo): $f_X(x) = \frac{dF_X(x)}{dx}$</li>
</ul>

**Caso congiunto $(X,Y)$**:

<ul>
<li>CDF congiunta: $F_{X,Y}(x,y) = \mathbb{P}\{X \leq x, Y \leq y\}$</li>
<li>PMF congiunta: $p_{X,Y}(x,y) = \mathbb{P}\{X=x, Y=y\}$</li>
<li>PDF congiunta: $f_{X,Y}(x,y) = \frac{\partial^2 F_{X,Y}}{\partial x\, \partial y}$</li>
</ul>

**Caso continuo n-dimensionale**:

$$F_\mathbf{X}(\mathbf{x}) = \mathbb{P}\{X_1 \leq x_1, \ldots, X_n \leq x_n\} \qquad f_\mathbf{X}(\mathbf{x}) = \frac{\partial^n F_\mathbf{X}(\mathbf{x})}{\partial x_1 \cdots \partial x_n}$$

**24.3 Legge di Bayes per vettori aleatori (Regola della catena)**

Iterando la probabilità composta:

$$p_\mathbf{X}(\mathbf{x}) = \prod_{i=1}^n p_{X_i|X_{i-1},\ldots,X_1}(x_i|x_{i-1},\ldots,x_1)$$

Analogo continuo:

$$f_\mathbf{X}(\mathbf{x}) = \prod_{i=1}^n f_{X_i|X_{i-1},\ldots,X_1}(x_i|x_{i-1},\ldots,x_1)$$

**24.4 Caratterizzazione sintetica dei vettori aleatori**

In assenza di caratterizzazione completa, si usano:

<ul>
<li><strong>Vettore media</strong>: $\boldsymbol{\mu}_\mathbf{X} = (\mathbb{E}[X_1],\ldots,\mathbb{E}[X_n])^T$</li>
<li><strong>Matrice di covarianza</strong>: $C_X = \mathbb{E}[(\mathbf{X}-\boldsymbol{\mu}_\mathbf{X})(\mathbf{X}-\boldsymbol{\mu}_\mathbf{X})^T]$, sempre simmetrica e definita non-negativa.</li>
</ul>

---

<h2>PARTE V — Processi Aleatori Tempo-Discreti</h2>

<h3>25. Definizione e Interpretazione</h3>

Un **processo aleatorio tempo-discreto** associa a ogni $\omega \in \Omega$ una successione:

$$X: \omega \mapsto \{X(n,\omega)\}_{n \in \mathbb{Z}}$$

<ul>
<li><strong>Realizzazione</strong>: sequenza deterministica per ogni fissato $\omega$.</li>
<li><strong>Campionamento verticale</strong>: fissato $n=n_0$, $X(n_0, \omega)$ è una variabile aleatoria con propria PDF.</li>
<li><strong>Stazionarietà del 1° ordine</strong>: la PDF è indipendente dall'istante $n_0$.</li>
</ul>

<h3>26. Ordini di Caratterizzazione</h3>

**26.1 Caratterizzazione al primo ordine**

Nota la PDF $f_{X(n)}(x; n)$ per ogni $n$. Se stazionario al 1° ordine → un'unica PDF.

**26.2 Caratterizzazione al secondo ordine**

Nota la PDF congiunta:

$$f_{X(n_1), X(n_2)}(x_1, x_2; n_1, n_2) \quad \forall n_1, n_2$$

**Stazionarietà al 2° ordine**: la PDF congiunta dipende solo dalla differenza temporale $n_2 - n_1$, non dalla posizione assoluta.

> Stazionarietà al 2° ordine $\Rightarrow$ stazionarietà al 1° ordine (non vale il viceversa).

**26.3 Caratterizzazione completa**

Un processo è **completamente caratterizzato** se, per qualunque $M$ e istanti $n_1,\ldots,n_M$, il vettore $\mathbf{X} = [X(n_1),\ldots,X(n_M)]^T$ ha PDF congiunta nota.

**Stazionarietà in senso stretto di ordine M (SSS-M)**: invarianza per traslazione temporale di ordine $M$.

**Processo indipendente** (a campioni indipendenti):

$$f_{X(n_1),\ldots,X(n_M)}(x_1,\ldots,x_M) = \prod_{i=1}^M f_{X(n_i)}(x_i)$$

<h3>27. Processi Discreti in Ampiezza</h3>

Un **processo ampiezza discreto** ha realizzazioni in un alfabeto discreto.

**Esempio — Processo di Bernoulli**: $X(n) \in \{-1,1\}$ con $\mathbb{P}\{X(n)=1\} = \mathbb{P}\{X(n)=-1\} = \frac{1}{2}$.

Tutte le definizioni dei processi continui si estendono sostituendo le PDF con le PMF.

<h3>28. Processi Stazionari in Senso Lato (SSL)</h3>

Un processo è **SSL** se soddisfa:

<ol>
<li><strong>Media costante</strong>: $\mathbb{E}[X(t/n)] = \mu$ (indipendente da $t$ o $n$).</li>
<li><strong>Autocorrelazione invariante per traslazione</strong>: $R_X(t_1,t_2) = \mathbb{E}[X(t_1)X(t_2)] = R_X(t_2-t_1)$.</li>
</ol>

**28.1 Struttura della matrice di covarianza SSL**

Il vettore media è $\boldsymbol{\mu}_\mathbf{X} = \mu\mathbf{1}$. La matrice di covarianza assume struttura di **Toeplitz**:

$$\mathbf{C}_\mathbf{X} = \sigma_X^2 \begin{pmatrix} 1 & \rho_{1,2} & \cdots & \rho_{1,M} \\ \rho_{1,2} & 1 & \cdots & \rho_{2,M} \\ \vdots & & \ddots & \vdots \\ \rho_{1,M} & \rho_{2,M} & \cdots & 1 \end{pmatrix}$$

Proprietà: simmetrica, elementi costanti sulle diagonali parallele, definita non-negativa.

**28.2 Proprietà dei processi Gaussiani**

<ul>
<li><strong>SSL $\implies$ SSS</strong>: nei processi Gaussiani la stazionarietà in senso lato implica quella in senso stretto.</li>
<li><strong>Chiusura lineare</strong>: $\mathbf{A}\mathbf{X}+\mathbf{b} \sim \mathcal{N}(\mathbf{A}\boldsymbol{\mu}+\mathbf{b}, \mathbf{A}\Sigma\mathbf{A}^T)$.</li>
<li><strong>Incorrelazione $\implies$ Indipendenza</strong> (esclusivo dei Gaussiani): matrice di covarianza diagonale → PDF congiunta fattorizzata.</li>
</ul>

---

<h2>PARTE VI — Convergenza e Legge dei Grandi Numeri</h2>

<h3>29. Tipi di Convergenza</h3>

Sia $X_n$ una successione di VA con densità $f_n(x)$ convergente a $X$.

**29.1 Gerarchia (dalla più forte alla più debole)**

<ul>
<li><strong>Puntuale</strong> (più forte): $\mathbb{P}(\lim_{n\to\infty} X_n = X) = 1$</li>
<li><strong>Quasi certa</strong> (con prob. 1 / forte coerenza): $\mathbb{P}\{\lim_{n\to\infty}\hat{B}(\mathbf{X}^n) = B\} = 1$</li>
<li><strong>In media quadratica</strong> (MS): $\lim_{n\to\infty}\mathbb{E}[(X_n-X)^2] = 0$</li>
<li><strong>In probabilità</strong> (debole): $\forall\epsilon>0$, $\lim_{n\to\infty}\mathbb{P}(|X_n-X|>\epsilon) = 0$</li>
<li><strong>In distribuzione</strong>: $\lim_{n\to\infty} F_n(x) = F(x)$ nei punti di continuità</li>
</ul>

> **Continuous Mapping Theorem**: se $g$ è continua, $X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)$.

**29.2 Convergenza forte (quasi certa)**

Ogni nuova serie di dati dalla stessa popolazione converge al valore atteso con probabilità 1 → **consistenza forte**.

**29.3 Convergenza in media quadratica**

$$\lim_{n\to\infty}\mathbb{E}\!\left[(\overline{X}_n - \mathbb{E}[X])^2\right] = 0$$

La convergenza MS implica la convergenza in probabilità (consistenza debole).

<h3>30. Funzione Generatrice dei Momenti (MGF)</h3>

**30.1 Definizione**

$$\Phi_X(s) = \mathbb{E}[e^{sX}] = \int_\mathbb{R} e^{st} f_X(t)\,dt$$

Continua in $s$ dove l'integrale esiste. $\Phi_X(0) = 1$.

**30.2 Proprietà operative**

<ul>
<li><strong>Calcolo dei momenti</strong>: $\Phi_X^{(r)}(0) = \mathbb{E}[X^r]$, con $\Phi_X'(0) = \mathbb{E}[X]$, $\Phi_X''(0) = \mathbb{E}[X^2]$</li>
<li><strong>Somma di VA indipendenti</strong>: $\Phi_{X+Y}(s) = \Phi_X(s)\cdot\Phi_Y(s)$</li>
<li><strong>Sviluppo in serie (MacLaurin)</strong>: $\Phi_X(s) = \sum_{n=0}^\infty \frac{\mathbb{E}[X^n]}{n!}s^n$</li>
</ul>

**30.3 Teoremi fondamentali**

<ul>
<li><strong>Unicità</strong>: due VA con la stessa MGF hanno la stessa CDF.</li>
<li><strong>Continuità di Lévy</strong>: $\Phi_{X_n}(s) \to \Phi_X(s)$ puntualmente $\iff X_n \xrightarrow{d} X$.</li>
</ul>

---

<h2>PARTE VII — Elementi di Statistica Inferenziale</h2>

<h3>31. Statistica Inferenziale: Introduzione</h3>

La **statistica inferenziale** utilizza i dati campionari per dedurre proprietà di una distribuzione sottostante. Si assume che il campione sia estratto da una famiglia di distribuzioni indicizzata da un parametro incognito $\theta$.

**Obiettivi principali**:

<ol>
<li><strong>Stima dei parametri</strong>: identificare $\theta$ tramite stime puntuali o intervalli di confidenza.</li>
<li><strong>Test delle ipotesi</strong>: decidere se un'affermazione su un fenomeno è coerente con i dati.</li>
</ol>

**31.1 Media campionaria e LLN**

$$\overline{x}_n = \frac{1}{n}\sum_{i=1}^n x_i \qquad \xrightarrow{n\to\infty} \mathbb{E}[X] = \sum_{i=1}^M a_i\, p_X(a_i)$$

**Legge dei Grandi Numeri (LLN)**: la media campionaria converge al valore atteso (debole, forte, o in MS).

**31.2 Distribuzione empirica e stimatore di frequenza**

Per $n$ variabili i.i.d., il numero $N_i$ di occorrenze di $X_k = a_i$ segue una distribuzione binomiale:

$$\operatorname{Pr}\{N_i=k\} = \binom{n}{k}p_X(a_i)^k[1-p_X(a_i)]^{n-k}$$

La frequenza relativa $N_i/n$ è uno stimatore non distorto e consistente MS di $p_X(a_i)$.

**31.3 Convergenza quasi certa e forte coerenza**

Per una distribuzione ipotizzata errata $q(a_i) \neq p_X(a_i)$, la probabilità di errore decade esponenzialmente per $n\to\infty$ secondo la **divergenza informativa**:

$$D_i = q(a_i)\log\frac{q(a_i)}{p_X(a_i)} + [1-q(a_i)]\log\frac{1-q(a_i)}{1-p_X(a_i)} > 0$$

<h3>32. Impostazione Bayesiana (Test di Ipotesi)</h3>

**32.1 Quadro delle ipotesi**

Dato un dataset $\mathbf{x}^n \in \mathcal{X}^n$, si definiscono $M$ ipotesi mutuamente esclusive $\{H_i\}_{i=1}^M$ con leggi condizionate $p_{\mathbf{X}^n}(\mathbf{x}^n|H_i)$ e probabilità a priori $\{p(H_i)\}$.

La **regola di decisione** $D: \mathbf{x}^n \mapsto D(\mathbf{x}^n) \in \{1,\ldots,M\}$ minimizza il **rischio Bayesiano medio**:

$$\mathcal{R} = \sum_{i=1}^M\sum_{j=1}^M C_{i,j}\,\mathbb{P}\{D(\mathbf{X}^n)=i, H=H_j\}$$

**32.2 Criteri ottimi (classificazione binaria)**

**Regola MAP (Maximum A-posteriori Probability)**:

$$L(\mathbf{x}^n) = \frac{p_{\mathbf{X}^n}(\mathbf{x}^n|H_1)}{p_{\mathbf{X}^n}(\mathbf{x}^n|H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta$$

**Regola ML (Maximum Likelihood)**: caso speciale MAP con ipotesi equiprobabili ($\eta = 1$).

**32.3 Peso di Hamming**

Il **peso di Hamming** $w_H(\mathbf{x}^n)$ è il numero di elementi uguali a "1" in una sequenza binaria. Per sequenze i.i.d. binarie, la regola ML si riduce a un confronto di soglia su $w_H$:

$$w_H(\mathbf{x}^n) \underset{H_2}{\overset{H_1}{\gtrless}} n\frac{\ln\!\left(\frac{1-p_2}{1-p_1}\right)}{\ln\!\left(\frac{p_1(1-p_2)}{p_2(1-p_1)}\right)} = \eta_1$$

**Probabilità di errore totale**: $\mathbb{P}(e) = \frac{1}{2}\mathbb{P}(e|H_1) + \frac{1}{2}\mathbb{P}(e|H_2)$

**32.4 Classificazione binaria con dati continui**

Il **rapporto di verosimiglianza** (Likelihood Ratio):

$$L(\mathbf{x}^n) = \frac{f_{\mathbf{X}^n|H_1}(\mathbf{x}^n|H_1)}{f_{\mathbf{X}^n|H_2}(\mathbf{x}^n|H_2)} \underset{H_2}{\overset{H_1}{\gtrless}} \frac{P(H_2)}{P(H_1)} = \eta$$

<h3>33. Test di Ipotesi (Scenario Non-Bayesiano)</h3>

**33.1 Definizioni**

<ul>
<li><strong>Ipotesi nulla</strong> $H_0$: assunzione di base con distribuzione nota.</li>
<li><strong>Errore di tipo-I (falso allarme)</strong>: $\alpha = \mathbb{P}\{D(\mathbf{X}^n)=1|H_0\}$ — rifiutare $H_0$ quando è vera.</li>
<li><strong>Errore di tipo-II</strong> (miss): $\beta = \mathbb{P}\{D(\mathbf{X}^n)=0|H_1\}$ — non rifiutare $H_0$ quando è falsa.</li>
<li><strong>Potenza del test</strong>: $1-\beta = \mathbb{P}\{D(\mathbf{X}^n)=1|H_1\}$.</li>
</ul>

**Contesti applicativi**: sicurezza e difesa, cybersecurity (IDS), sistemi ADAS, controllo del traffico aereo.

**33.2 Lemma di Neyman-Pearson**

Il test ottimale massimizza la potenza fissato il vincolo $\alpha$:

$$L(\mathbf{x}^n) = \frac{f_{\mathbf{X}^n|H_1}(\mathbf{x}^n|H_1)}{f_{\mathbf{X}^n|H_0}(\mathbf{x}^n|H_0)} \underset{H_0}{\overset{H_1}{\gtrless}} \eta$$

La soglia $\eta$ soddisfa: $\mathbb{P}\{L(\mathbf{X}^n)>\eta|H_0\} = \alpha$.

**Log-likelihood** (forma logaritmica equivalente):

$$\Lambda(\mathbf{x}^n) = \ln L(\mathbf{x}^n) \underset{H_0}{\overset{H_1}{\gtrless}} \eta'$$

<h3>34. Stima dei Parametri — Impostazione Bayesiana</h3>

**34.1 Definizione di stimatore**

Un **estimatore** $\widehat{\Theta}(\mathbf{X}^n)$ è una VA che stima il parametro $\theta$ dal campione $\mathbf{x}^n$.

**Rischio Bayesiano medio**:

$$\mathcal{R} = \mathbb{E}\!\left[C(\widehat{\Theta}(\mathbf{X}^n) - \Theta)\right]$$

**Distribuzione a posteriori** (tramite Bayes):

$$f_{\Theta|\mathbf{X}^n}(\theta|\mathbf{x}^n) = \frac{f_{\mathbf{X}^n|\Theta}(\mathbf{x}^n|\theta)\, f_\Theta(\theta)}{\int f_{\mathbf{X}^n|\theta}(\mathbf{x}^n|\theta)\, f_\Theta(\theta)\,d\theta}$$

**34.2 Stimatore MMSE**

Costo quadratico $C(\cdot) = (\cdot)^2$ → minimizza l'errore quadratico medio → **media della posteriori**:

$$\widehat{\theta}_\text{MMSE}(\mathbf{x}^n) = \mathbb{E}[\Theta|\mathbf{X}^n = \mathbf{x}^n] = \int \theta\, f_{\Theta|\mathbf{X}^n}(\theta|\mathbf{x}^n)\,d\theta$$

**34.3 Stimatore MAP**

Costo 0-1 → massimizza la posteriori → **moda della posteriori**:

$$\widehat{\theta}_\text{MAP}(\mathbf{x}^n) = \arg\max_\theta\, f_{\Theta|\mathbf{X}^n}(\theta|\mathbf{x}^n)$$

**Applicazione — Modello Bernoulli** (campione binario con peso di Hamming $w(\mathbf{x}^n)$):

<ul>
<li><strong>MAP</strong>: $\widehat{\beta}_\text{MAP}(\mathbf{x}^n) = \frac{w(\mathbf{x}^n)}{n}$</li>
<li><strong>MMSE</strong>: $\widehat{\beta}_\text{MMSE}(\mathbf{x}^n) = \frac{w(\mathbf{x}^n)+1}{n+2}$</li>
</ul>

**34.4 Analisi delle prestazioni: distorsione e consistenza**

$\text{MSE} = \text{Bias}^2 + \text{Varianza}$

Un estimatore è:

<ul>
<li><strong>Non distorto (Unbiased)</strong>: $\mathbb{E}[\widehat{\Theta}(\mathbf{X}^n) - \Theta] = 0$</li>
<li><strong>Asintoticamente non distorto</strong>: bias $\to 0$ per $n\to\infty$</li>
<li><strong>Consistente MS</strong>: $\overline{e_n^2} \to 0$ per $n\to\infty$</li>
<li><strong>Consistente in probabilità (debole)</strong>: $\widehat{\Theta} \overset{P}{\to} \Theta$</li>
<li><strong>Fortemente consistente (quasi certo)</strong>: $\widehat{\Theta} \overset{\text{q.c.}}{\to} \Theta$</li>
</ul>

**Confronto MMSE vs MAP**:

<ul>
<li>MAP: non distorto, $\overline{e^2}_\text{MAP} = \frac{1}{6n}$</li>
<li>MMSE: distorto (ma asintoticamente non distorto), $\overline{e^2}_\text{MMSE} < \overline{e^2}_\text{MAP} \quad \forall n$ (dominanza MSE)</li>
</ul>

**34.5 Unicità degli stimatori Bayesiani**

Se la distribuzione a posteriori è **simmetrica rispetto alla propria media** e la funzione di costo è **pari e convessa**, lo stimatore MMSE minimizza il rischio per qualunque tale funzione di costo.

Sotto simmetria: $\widehat{\mu}_\text{MAP} = \widehat{\mu}_\text{MMSE}$.

<h3>35. Stima dei Parametri — Approccio Non-Bayesiano</h3>

$\theta$ deterministico e sconosciuto (nessun prior). Osservazioni $\mathbf{x}^n$ da $f_{\mathbf{X}^n}(\mathbf{x}^n;\theta)$.

**35.1 Verosimiglianza e stimatore ML**

$$L(\theta;\mathbf{x}^n) = f_{\mathbf{X}^n}(\mathbf{x}^n;\theta) \qquad \Lambda(\theta;\mathbf{x}^n) = \log f_{\mathbf{X}^n}(\mathbf{x}^n;\theta)$$

$$\widehat{\theta}_\text{ML}(\mathbf{x}^n) = \arg\max_{\theta \in \mathcal{S}}\,\log f_{\mathbf{X}^n}(\mathbf{x}^n;\theta)$$

**35.2 Misure di prestazione**

Dato bias $b_n(\theta) = \mathbb{E}[\widehat{\Theta}(\mathbf{X}^n)] - \theta$ e MSE $\overline{e_n^2} = \mathbb{E}[(\widehat{\Theta}(\mathbf{X}^n)-\theta)^2]$:

<ul>
<li>Consistenza debole, forte, MS.</li>
<li>Uno stimatore unbiased MMSE minimizza $\text{Var}[\widehat{\Theta}]$.</li>
</ul>

**35.3 Limite di Cramér-Rao (CRB)**

Fornisce il limite inferiore insuperabile per la varianza di qualunque stimatore.

**Informazione di Fisher**:

$$I_n(\theta) = \mathbb{E}\!\left[\!\left(\frac{\partial \log f_{\mathbf{X}^n}}{\partial\theta}\right)^{\!2}\right] = -\mathbb{E}\!\left[\frac{\partial^2 \log f_{\mathbf{X}^n}}{\partial\theta^2}\right]$$

**CRB**:

$$\text{Var}[\widehat{\Theta}(\mathbf{X}^n)] \geq \frac{[1+b_n'(\theta)]^2}{I_n(\theta)}$$

Caso non distorto ($b_n=0$): $\text{Var}[\widehat{\Theta}] \geq \frac{1}{I_n(\theta)}$.

**Stimatore efficiente**: non distorto che raggiunge il CRB. Coincide necessariamente con lo stimatore ML.

<h3>36. Stima a Parametri Multipli</h3>

**36.1 Inferenza Bayesiana multipla**

$\boldsymbol{\theta} = [\theta_1,\ldots,\theta_m]^T$ casuale. Stimatori:

<ul>
<li><strong>MMSE</strong>: $\widehat{\theta}_i(\mathbf{x}^n) = \mathbb{E}[\Theta_i|\mathbf{X}^n=\mathbf{x}^n]$ (problema separabile)</li>
<li><strong>MAP</strong>: $\nabla_{\boldsymbol{\theta}} f_{\boldsymbol{\Theta}|\mathbf{X}^n}(\boldsymbol{\theta}|\mathbf{x}^n)\big|_{\boldsymbol{\theta}=\widehat{\boldsymbol{\theta}}} = \mathbf{0}$</li>
</ul>

**36.2 MLE multipla (non Bayesiana)**

$$\nabla_{\boldsymbol{\theta}}\,\Lambda(\boldsymbol{\theta};\mathbf{x}^n)\big|_{\boldsymbol{\theta}=\widehat{\boldsymbol{\theta}}} = \mathbf{0}$$

**36.3 Stimatore LMMSE**

Stimatore lineare $\widehat{\Theta}(\mathbf{X}^n) = \mathbf{a}^T\mathbf{X}^n + b$:

$$b_\text{LMMSE} = \mathbb{E}[\Theta] - \mathbf{a}^T\mathbb{E}[\mathbf{X}^n] \qquad \mathbf{a}_\text{LMMSE} = \mathbf{M}^{-1}\mathbf{s}$$

con $\mathbf{M} = \mathbb{E}[(\mathbf{X}^n-\mathbb{E}[\mathbf{X}^n])(\mathbf{X}^n-\mathbb{E}[\mathbf{X}^n])^T]$ e $\mathbf{s} = \mathbb{E}[(\mathbf{X}^n-\mathbb{E}[\mathbf{X}^n])(\Theta-\mathbb{E}[\Theta])]$.

**36.4 Algoritmo del gradiente**

Iterazione per minimizzare l'MSE:

$$\mathbf{a}^{(k+1)} = \mathbf{a}^{(k)} - \gamma(\mathbf{M}\mathbf{a}^{(k)} - \mathbf{s})$$

L'errore converge se $0 < \gamma < \frac{2}{\lambda_\text{MAX}}$ (autovalore massimo di $\mathbf{M}$).

<h3>37. Statistica Descrittiva: Stimatore Least Squares (LS)</h3>

Dataset $\mathbf{X} \in \mathbb{R}^{n\times p}$, target $\mathbf{y} \in \mathbb{R}^p$, modello lineare $\mathbf{y} = \mathbf{X}^T\mathbf{a} + \boldsymbol{\epsilon}$.

**37.1 Estimatore LS**

Minimizzando $\|\mathbf{X}^T\mathbf{a} - \mathbf{y}\|^2$:

$$\mathbf{a}_\text{LS}(p) = (\mathbf{X}(p)\mathbf{X}^T(p))^{-1}\mathbf{X}(p)\mathbf{y}(p) \qquad \text{richiede } p \geq n$$

**37.2 Aggiornamento ricorsivo (Formula di Sherman-Morrison)**

Inversione rank-1 di matrici:

$$(\mathbf{R} + \mathbf{u}\mathbf{v}^T)^{-1} = \mathbf{R}^{-1} - \frac{\mathbf{R}^{-1}\mathbf{u}\mathbf{v}^T\mathbf{R}^{-1}}{1+\mathbf{v}^T\mathbf{R}^{-1}\mathbf{u}}$$

Aggiungendo il campione $\mathbf{x}^n(p+1)$ con $K(p+1) = \mathbf{x}^{nT}(p+1)\mathbf{R}^{-1}(p)\mathbf{x}^n(p+1)$:

$$\mathbf{R}^{-1}(p+1) = \mathbf{R}^{-1}(p) - \frac{\mathbf{R}^{-1}(p)\,\mathbf{x}^n(p+1)\,\mathbf{x}^{nT}(p+1)\,\mathbf{R}^{-1}(p)}{1+K(p+1)}$$

Complessità: $\mathcal{O}(n^2)$ invece di $\mathcal{O}(n^3)$.

**37.3 LS adattivo (media mobile esponenziale)**

Per ambienti variabili nel tempo, con peso $w < 1$ che diminuisce l'importanza dei dati storici:

$$\mathbf{a} = \left[\sum_{i=1}^p w^{p-i}\mathbf{x}^n(i)\mathbf{x}^{nT}(i)\right]^{-1}\sum_{i=1}^p w^{p-i}\mathbf{x}^n(i)\theta(i)$$

Implementabile ricorsivamente via Sherman-Morrison.

**37.4 LS con bias (dati centrati)**

Modello $\widehat{\theta}(\mathbf{x}^n) = \mathbf{a}^T\mathbf{x}^n + b$. Operando su dati centrati ($\mathbf{X}_0 = \mathbf{X} - \bar{\mathbf{x}}\mathbf{1}_p^T$):

$$\mathbf{a}_\text{LMS} = (\mathbf{X}_0\mathbf{X}_0^T)^{-1}\mathbf{X}_0\mathbf{y}_0 \qquad b_\text{LMS} = \tilde{\theta} - \frac{1}{p}\mathbf{1}_p^T\mathbf{X}^T\mathbf{a}_\text{LMS}$$

con $\tilde{\theta} = \frac{1}{p}\sum_i\theta(i)$ media del target.

---

*Fine documento — tutti i concetti del file originale sono stati conservati e riorganizzati secondo la gerarchia richiesta (h1 > h2 > h3 > liste).*
