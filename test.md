# Funzioni di variabili aleatorie

## Funzioni di variabili aleatorie discrete

### Trasformazione della probability mass function (pmf)

> [!important] Definizione (**Trasformazione della pmf per funzioni di VA**)
> Sia $X$ una variabile aleatoria discreta con alfabeto $\mathcal{X}$ e probability mass function $p_X(x) = \mathbb{P}(X = x)$. Sia $g(\cdot)$ una funzione definita sui punti di $\mathcal{X}$ che genera una nuova variabile aleatoria $Y = g(X)$ con alfabeto $\mathcal{Y} = g(\mathcal{X})$. La pmf $p_Y(y)$ della variabile aleatoria $Y$ è definita per ogni $y \in \mathcal{Y}$ come:
> $$p_Y(y) = \sum_{x \in \mathcal{X} : g(x) = y} p_X(x)$$
> 
> 

#### Perché serve:
Consente di determinare il comportamento probabilistico completo di una nuova variabile aleatoria ottenuta elaborando, filtrando o trasformando i dati di una variabile già nota, senza dover effettuare nuove misurazioni sperimentali sul sistema.

#### Derivazione:
Per ricavare la caratterizzazione di $Y$ in termini di pmf a partire da quella di $X$, si distinguono due casi geometrici fondamentali:

1. **Caso biunivoco:** La funzione $g(x)$ mappa ogni elemento di $\mathcal{X}$ in un unico elemento di $\mathcal{Y}$ in modo invertibile, per cui $|\mathcal{Y}| = |\mathcal{X}|$. Esiste allora la funzione inversa $x = g^{-1}(y)$. L'evento $\{Y = y_i\}$ equivale esattamente all'evento $\{X = g^{-1}($y_i$)\} = \{X = x_i\}$. Sfruttando l'uguaglianza logica tra gli eventi si ha: $$p_Y(y_i) = \mathbb{P}(Y = g(x_i)) = \mathbb{P}(X = g^{-1}(y_i)) = \mathbb{P}(X = x_i) = p_X(x_i)$$

2. **Caso univoco (non invertibile):** La funzione $g(x)$ associa a più valori distinti di $X$ lo stesso valore di $Y$, determinando una contrazione dell'alfabeto tale per cui $|\mathcal{X}| = n$ e $|\mathcal{Y}| = m$ con $n > m$. Per un generico punto $y_k \in \mathcal{Y}$, si definisce l'insieme delle sue controimmagini $x_1^{(k)}, x_2^{(k)}, \dots, x_{L_k}^{(k)}$ tali che $g(x_i^{(k)}) = y_k$ per ogni $i = 1, \dots, L_k$. L'evento $\{Y = y_k\}$ corrisponde all'unione disgiunta degli eventi elementari della variabile $X$: $$\{Y = y_k\} = \bigcup_{i = 1}^{L_k} \{X = x_i^{(k)}\}$$

Poiché i singoli eventi $\{X = x_i^{(k)}\}$ sono mutuamente esclusivi per definizione di variabile aleatoria, applicando l'assioma dell'additività lineare della probabilità si ottiene: $$p_Y(y_k) = \mathbb{P}\left(\bigcup_{i = 1}^{L_k} \{X = x_i^{(k)}\}\right) = \sum_{i = 1}^{L_k} \mathbb{P}(X = x_i^{(k)}) = \sum_{i = 1}^{L_k} p_X(x_i^{(k)})$$


#### Formule chiave:

> [!important] Calcolo della pmf trasformata
> $$p_Y(y) = \begin{cases} p_X(g^{-1}(y)) & \text{se } g \text{ è biunivoca} \\ \sum_{x: g(x)=y} p_X(x) & \text{se } g \text{ è univoca} \end{cases}$$
> 
> 

Collegamenti:
Richiede: Definizione di variabile aleatoria discreta, probability mass function (pmf), eventi mutuamente esclusivi. Usato in: Calcolo dei momenti di variabili trasformate e analisi dei sistemi di modulazione numerica.

> [!warning] Attenzione
> Nel caso di trasformazioni non invertibili (univoche), dimenticare di sommare le probabilità di *tutte* le controimmagini $x$ che mappano nello stesso punto $y$ porta a una pmf non normalizzata, la cui somma su tutto l'alfabeto $\mathcal{Y}$ risulterebbe erroneamente inferiore a 1.

---

### Media di funzioni e LOTUS

> [!important] Teorema (**Teorema fondamentale per il calcolo della media**)
> Sia $X$ una variabile aleatoria discreta con pmf $p_X(x)$ e sia $Y = g(X)$ una nuova variabile aleatoria ottenuta tramite la trasformazione $g(\cdot)$. Il valore atteso (o media statistica) di $Y$ può essere calcolato direttamente a partire dalla pmf di $X$ senza ricavare preventivamente la pmf $p_Y(y)$, secondo la relazione:
> $$\mathbb{E}[g(X)] = \sum_{x \in \mathcal{X}} g(x) p_X(x) \tag{1}$$
> 
> 

#### Perché serve:
Evita il laborioso passaggio intermedio di determinazione della nuova pmf $p_Y(y)$ quando l'unico obiettivo dell'analisi è la conoscenza del valor medio o dei momenti statistici di ordine superiore (come la varianza) del segnale trasformato.

#### Derivazione:
Si consideri la definizione formale di valore atteso applicata alla variabile aleatoria $Y$, per la quale si ha $\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} y p_Y(y)$.

1. Se la funzione $g(\cdot)$ è biunivoca, si applica la ridenominazione diretta dell'alfabeto $y = g(x)$ e $p_Y(y) = p_X(x)$, ottenendo immediatamente:
$$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} y p_Y(y) = \sum_{x \in \mathcal{X}} g(x) p_X(x)$$

2. Se la funzione $g(\cdot)$ è univoca (non invertibile), si esprime $p_Y(y)$ come la somma delle probabilità delle sue controimmagini. Sostituendo tale espressione nella definizione di valore atteso si ricava:
$$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} y \left( \sum_{x: y = g(x)} p_X(x) \right)$$

3. Poiché la condizione sotto la sommazione interna impone che l'argomento $y$ sia esattamente pari a $g(x)$, è possibile portare $y$ dentro la seconda sommatoria sostituendolo con l'espressione funzionale equivalente $g(x)$:
$$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} \sum_{x: y = g(x)} g(x) p_X(x) \tag{2}$$

4. Poiché l'unione disgiunta di tutti i sottoinsiemi di controimmagini $\{x \in \mathcal{X} : g(x) = y\}$ al variare di $y \in \mathcal{Y}$ ricostituisce esattamente l'intero alfabeto di partenza $\mathcal{X}$, la doppia sommatoria vincolata equivale a un'unica sommatoria estesa a tutti i punti di $\mathcal{X}$. Pertanto, l'equazione (1) include l'equazione (2) come caso speciale:
$$\mathbb{E}[Y] = \sum_{x \in \mathcal{X}} g(x) p_X(x)$$


#### Formule chiave:

> [!important] Valore atteso di una trasformazione
> $$\mathbb{E}[Y] = \sum_{y \in \mathcal{Y}} y p_Y(y) = \sum_{x \in \mathcal{X}} g(x) p_X(x)$$
> 
> 

Collegamenti:
Richiede: Definizione di valore atteso per variabili discrete, trasformazione della pmf. Usato in: Definizione di varianza ($\mathbb{E}[(X-\mu)^2]$), calcolo dei momenti e funzioni generatrici dei momenti.