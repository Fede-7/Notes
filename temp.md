Ecco il testo completo, sistemato e ripulito da rumore tipografico, spazi spuri nelle formule, notazioni incoerenti (come $p\chi$ al posto di $p_X$, o frammenti di testo sovrapposti) e refusi di formattazione LaTeX (come l'operatore `\operatorname*` errato o vettori duplicati).

Viene mantenuta l'impaginazione in Markdown e LaTeX originale con i blocchi di citazione/teorema formattati correttamente.

---

## Un esempio: la media campionaria

Assumiamo di avere un set di dati $\pmb{x}^{n} \in \mathcal{X}^{n} \subseteq \mathbb{R}^{n}$.

Sappiamo che la **media campionaria** è definita come
$$\overline{{x}}_{n} = \frac{1}{n} \sum_{i = 1}^{n} x_{i}$$
La **Legge dei Grandi Numeri** ci dice che $\overline{X}_{n} \to \mathbb{E}[X]$ (il tipo di convergenza dipende dalla legge statistica sottostante), nel senso che, denotando con $X^{n}$ un campione casuale estratto dalla popolazione, abbiamo
$$\frac{1}{n} \sum_{i = 1}^{n} X_{i} \to \mathbb{E}[X]$$
> [!rb] Osservazione
> La **convergenza debole** (cioè, convergenza in probabilità) ci dice che la frequenza dei campioni la cui media campionaria si discosta significativamente da $\mathbb{E}[X]$ è piccola quanto desideriamo;
> La **convergenza forte** afferma che nel limite la probabilità di discostarsi da $\mathbb{E}[X]$ è zero;
> La **convergenza in media quadratica** (Mean-Square) afferma che
> $$
\lim_{n \to \infty} \mathbb{E} \left[ \left(\overline{X}_{n} - \mathbb{E}[X]\right)^{2} \right] = 0
> $$

Assumiamo che $\pmb{x}^{n} \in \mathcal{X}^{n}$, con $\mathcal{X} = \{ a_{1}, \dotsc, a_{M} \}$ discreto e finito; sappiamo che
$$\overline{{x}}_{n} = \sum_{i = 1}^{M} a_{i} f_{n}(a_{i})$$
dove $f_{n}(a_{i})$ è la frazione dei valori del campione che assumono il valore $a_{i}$.

Sappiamo che, se $X$ è una variabile casuale con pmf $\{ p_{X}(a_{i}) \}_{i = 1}^{M}$, allora:
$$\mathbb{E}[X] = \sum_{i = 1}^{M} a_{i} p_{X}(a_{i})$$
Di conseguenza, abbiamo
$$| \overline{{x}}_{n} - \mathbb{E}[X] | \leq \sum_{i = 1}^{M} | a_{i} | | f_{n}(a_{i}) - p_{X}(a_{i}) |$$
> [!note] Osservazione
> Si noti che se possiamo affermare che $f_{n}(a_{i}) \to p_{X}(a_{i})$ (in qualche senso), allora possiamo inferire che $\pmb{x}^{n}$ è un campione da una popolazione i cui elementi sono estratti da un vettore casuale $X^{n}$ con densità marginale $\{ p_{X}(a_{i}) \}_{i = 1}^{M}$.

## La distribuzione empirica

> [!def] Distribuzione Empirica
> Metodo per inferire la legge di probabilità ignota di una popolazione osservando la frequenza con cui determinati valori compaiono in un campione di dati.

Assumiamo che un campione di dati $\pmb{x}^{n}$ sia composto da $n$ variabili casuali **i.i.d.** con probabilità marginale $\{ p_{X}(a_{i}) \}_{i = 1}^{M}$ non nota.

> [!rb] I.I.D. (Indipendenti Identicamente Distribuite)
> Variabili casuali che sono indipendenti tra loro e condividono esattamente la stessa legge di probabilità.

### Modello Statistico e Frequenze
Il numero di volte $N_{i}$ in cui l'evento $X_{k} = a_{i}$ si verifica nel campione è una variabile casuale che segue la **distribuzione binomiale**:
$$\operatorname{Pr} \left\{N_{i} = k \right\} = \binom{n}{k} p_{X}(a_{i})^{k} \left[ 1 - p_{X}(a_{i}) \right]^{n - k}$$.

> [!theorem] Caratterizzazione della Frequenza Relativa
> La frazione del campione $\frac{N_{i}}{n}$ che assume il valore $a_i$ (frequenza relativa) agisce come stimatore della probabilità teorica $p_X($a_i$)$ con le seguenti proprietà:
> - **Valore Atteso (Non distorsione)**: $\mathbb{E} \left[ \frac{N_{i}}{n} \right] = p_{X}(a_{i})$
> - **Varianza (Incertezza)**: $\operatorname{var} \left[ \frac{N_{i}}{n} \right] = \frac{p_{X}(a_{i}) (1 - p_{X}(a_{i}))}{n}$.

### Convergenza
> [!dim] Consistenza in Media Quadratica
> All'aumentare della dimensione del campione ($n \to \infty$), la frequenza relativa converge alla probabilità vera poiché l'errore quadratico medio tende a zero:
> $$\lim_{n \rightarrow \infty} \mathbb{E} \left[\left(\frac{N_{i}}{n} - p_{X}(a_{i})\right)^{2} \right] = 0$$.## Convergenza quasi certa

Assumiamo che $\{ q(a_{i}) \}$ sia qualsiasi altra pmf su $\mathcal{X}$ differente dalla vera distribuzione $p_{X}(a_{i})$ in almeno due elementi. Abbiamo:
$$\operatorname{Pr} \left\{N_{i} = n q(a_{i}) \right\} = \binom{n}{n q(a_{i})} p_{X}(a_{i})^{n q(a_{i})} \left[ 1 - p_{X}(a_{i}) \right]^{n (1 - q(a_{i}))}$$
Utilizzando il limite di Stirling per il coefficiente binomiale:
$$\sqrt{\frac{n}{8 k (n - k)}} \leq \binom{n}{k} 2^{- n H_2\left(\frac{k}{n}\right)} \leq \sqrt{\frac{n}{\pi k (n - k)}}$$
abbiamo, impostando $k = n q(a_{i})$:
$$\sqrt{\frac{1}{8 n q(a_{i}) (1 - q(a_{i}))}} \leq \binom{n}{n q(a_{i})} 2^{- n \left[ q(a_{i}) \log_2 \frac{1}{q(a_{i})} + (1 - q(a_{i})) \log_2 \frac{1}{1 - q(a_{i})} \right]} \leq \sqrt{\frac{1}{\pi n q(a_{i}) (1 - q(a_{i}))}}$$
da cui si deduce che, per $n$ sempre più grandi:
$$\binom{n}{n q(a_{i})} \sim 2^{n H_{2}(q(a_{i}), 1 - q(a_{i}))}$$
Consideriamo ora un valore $a_{i}$ per il quale $q(a_{i}) \neq p_{X}(a_{i})$. Quando $n$ diventa grande abbiamo:
$$\begin{aligned} 
\operatorname{Pr} \big\{N_{i} = n q(a_{i}) \big\} & \sim 2^{n H_{2}(q(a_{i}), 1 - q(a_{i}))} p_{X}(a_{i})^{n q(a_{i})} \left[ 1 - p_{X}(a_{i}) \right]^{n (1 - q(a_{i}))} \\ 
& = 2^{n H_{2}(q(a_{i}), 1 - q(a_{i}))} 2^{n [ q(a_{i}) \log_2 p_{X}(a_{i}) + (1 - q(a_{i})) \log_2 (1 - p_{X}(a_{i})) ]} \\ 
& = 2^{n \left[ q(a_{i}) \log_2 \frac{p_{X}(a_{i})}{q(a_{i})} + (1 - q(a_{i})) \log_2 \frac{1 - p_{X}(a_{i})}{1 - q(a_{i})} \right]} = 2^{- n D_{i}} 
\end{aligned}$$
con
$$D_{i} = q(a_{i}) \log_2 \frac{q(a_{i})}{p_{X}(a_{i})} + [ 1 - q(a_{i}) ] \log_2 \frac{1 - q(a_{i})}{1 - p_{X}(a_{i})} > 0$$
Concludiamo quindi che la probabilità che la frequenza empirica devii dalla vera probabilità tende a zero esponenzialmente con $n$. Ciò implica che $f_{n}(a_{i}) \to p_{X}(a_{i})$ quasi certamente.

## Commenti

Si consideri un campione $\pmb{x}^{n} \in \mathcal{X}^{n}$, con $\mathcal{X} = \{ a_{1}, \ldots, a_{M} \}$, estratto da un vettore casuale $X^{n}$ di pmf (Probability Mass Function) sconosciuta.

Se si calcolano le frequenze di occorrenza empiriche:
$$f_{n}(a_{i}) = \frac{\# \text{ di elementi uguali a } a_{i}}{n}, \qquad i = 1, \ldots, M$$
si ottiene che:
$$\operatorname{Pr} \left\{\lim_{n \rightarrow \infty} \frac{N_{i}}{n} = \lim_{n \rightarrow \infty} f_{n}(a_{i}) = p_{X}(a_{i}) \right\} = 1$$
Ciò implica che qualsiasi altro campione, ad esempio $\pmb{y}^{n}$, estratto dalla stessa popolazione mostrerà, per $n \to \infty$, lo stesso comportamento statistico.

Risulta evidente che per ogni funzione continua $f(\cdot)$ dei dati vale la relazione:
$$\operatorname{Pr} \left\{\lim_{n \rightarrow \infty} f(\boldsymbol{X}^{n}) = \lim_{n \rightarrow \infty} f(\boldsymbol{x}^{n}) \right\} = 1$$
Di conseguenza, la media campionaria converge con probabilità uno alla media statistica della popolazione. Questa proprietà è definita in statistica inferenziale come **forte consistenza** (o coerenza forte).

> [!theorem] Forte Consistenza
> In statistica, un estimatore si dice fortemente consistente se converge quasi certamente (con probabilità 1) al valore vero del parametro che intende stimare all'aumentare della dimensione del campione.