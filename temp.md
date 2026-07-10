Mentre la **statistica descrittiva** si limita a "fotografare" e riassumere i dati che abbiamo già raccolto, la **statistica inferenziale** usa quelle informazioni per capire come funziona l'intero fenomeno (la popolazione) da cui i dati provengono. Il suo scopo è trarre conclusioni generali partendo da un piccolo gruppo di osservazioni, tenendo conto che i risultati sono influenzati dal caso.

>[!quote] Come funziona in breve
L'idea di base è che i dati che analizziamo siano il risultato di un **esperimento casuale**. 
>*   Abbiamo un **campione** di $n$ misure (es. l'altezza di 100 persone).
>*   Sappiamo che se ripetessimo l'indagine oggi stesso, otterremmo valori leggermente diversi proprio a causa della natura casuale del campionamento.
>*   L'inferenza statistica cerca di definire una "legge" (modello probabilistico) che sia valida per qualsiasi campione estratto correttamente dalla stessa popolazione.

>[!focus] I due obiettivi principali
L'inferenza si muove lungo due binari fondamentali:
>
>1.  **Stima dei Parametri (*Parameter Estimation*):** Si cerca di "indovinare" i valori ignoti della popolazione (come la media o la varianza) usando i dati del campione. Possiamo fornire un singolo numero (stima puntuale) o un intervallo di valori entro cui siamo fiduciosi si trovi il vero parametro (intervallo di confidenza).
>$\space$
>2.  **Test delle Ipotesi (*Hypothesis Testing*):** Si definisce una procedura per decidere se un'affermazione su un fenomeno (ad esempio: "questo farmaco è efficace") sia coerente o meno con i dati che abbiamo osservato.

In sintesi, la statistica inferenziale è lo strumento che permette di trasformare i dati grezzi in **conoscenza affidabile** sull'intera realtà che ci circonda.

### La Media Campionaria ($\overline{X}_n$)

> [!def] Definizione di Media Campionaria
> Dato un set di dati $\pmb{x}^{n} = \{$x_1$, \dots, x_n\}$, la media campionaria è:
> $$\overline{x}_{n} = \frac{1}{n} \sum_{i = 1}^{n} x_{i}
> $$

> [!theorem] Legge dei Grandi Numeri (LLN)
> Afferma che la media campionaria converge al valore atteso della popolazione:
> $$\overline{X}_{n} \to \mathbb{E}[X]$$

> [!rb] Tipi di Convergenza
> 1. **Debole (in Probabilità):** La frequenza dei campioni la cui media si discosta significativamente da $\mathbb{E}[X]$ è piccola a piacere.
> 2. **Forte (Quasi Certa):** Il limite della probabilità di discostarsi da $\mathbb{E}[X]$ è zero.
> 3. **In Media Quadratica (Mean-Square):** 
>    $$\lim_{n \to \infty} \mathbb{E} \left[ \left(\overline{X}_{n} - \mathbb{E}[X]\right)^{2} \right] = 0$$


### La Distribuzione Empirica

> [!def] Frequenza di Occorrenza
> Se $N_i$ è il numero di volte in cui l'evento $X_k = a_i$ si verifica in un campione di dimensione $n$ i.i.d. (indipendenti e identicamente distribuite), il conteggio segue una **distribuzione binomiale**:
> $$\operatorname{Pr} \left\{N_{i} = k \right\} = \binom{n}{k} p_{X}(a_{i})^{k} \left[ 1 - p_{X}(a_{i}) \right]^{n - k}$$

> [!dim] Proprietà dello Stimatore di Frequenza
> La frequenza relativa $\frac{N_i}{n}$ converge alla probabilità vera $p_X($a_i$)$ in media quadratica poiché:
> - **Valore Atteso:** $\mathbb{E} \left[ \frac{N_{i}}{n} \right] = p_{X}(a_{i})$
> - **Varianza:** $\operatorname{var} \left[ \frac{N_{i}}{n} \right] = \frac{p_{X}(a_{i}) (1 - p_{X}(a_{i}))}{n}$
> - **Limite MS:** $\lim_{n \rightarrow \infty} \mathbb{E} \left[\left(\frac{N_{i}}{n} - p_{X}(a_{i})\right)^{2} \right] = 0$



## Convergenza quasi certa

> [!def] Convergenza quasi certa (Forte Coerenza)
> In statistica inferenziale, un estimatore si dice **fortemente coerente** (o consistente) se la probabilità che esso devii dal valore vero del parametro tende a zero all'aumentare della dimensione del campione. In termini di frequenze, ciò significa che la frequenza empirica $f_n($a_i$)$ converge alla probabilità reale $p_X($a_i$)$ con probabilità pari a 1 ($f_n($a_i$) \xrightarrow{q.c.} p_X($a_i$)$).

Assumiamo che un campione $\pmb{x}^n$ sia estratto da una popolazione con distribuzione di probabilità (pmf) $p_X($a_i$)$ sconosciuta. Per dimostrare che la frequenza osservata non mente, ipotizziamo una distribuzione alternativa errata $\{q($a_i$)\}$ che differisca dalla vera pmf in almeno due elementi.

> [!dim] Dimostrazione asintotica della coerenza
> 1. **Modello Binomiale**: La probabilità che il numero di occorrenze $N_i$ segua la distribuzione errata $q($a_i$)$ è:
>    $$\operatorname{Pr}\left\{N_i = n q(a_i) \right\} = \binom{n}{n q(a_i)} p_X(a_i)^{n q(a_i)} \left[ 1 - p_X(a_i) \right]^{n (1 - q(a_i))} \quad$$
> 
> 2. **Limite Combinatorio**: Utilizzando il limite basato sull'entropia $H$:
>    $$\sqrt{\frac{n}{8 k (n - k)}} \leq \binom{n}{k} 2 ^ {- n H \left(\frac {k}{n}\right)} \leq \sqrt{\frac{n}{\pi k (n - k)}} \quad$$
> 
> 3. **Approssimazione del coefficiente**: Per $n \to \infty$, impostando $k = n q($a_i$)$, l'espressione del coefficiente binomiale scala con l'entropia binaria $H_2$:
>    $$\binom{n}{n q (a _ {i})} \sim 2 ^ {n H _ {2} (q (a _ {i}), 1 - q (a _ {i}))} \quad$$
> 
> 4. **Decadimento esponenziale**: Raggruppando i termini, la probabilità che si verifichi la frequenza errata collassa in forma esponenziale:
>    $$\operatorname{Pr} \big \{N_i = n q(a_i) \big \} \sim 2^{- n D_i} \quad$$
> 
> 5. **Tasso di errore (Divergenza)**: Il termine $D_i$ rappresenta la divergenza informativa (sempre positiva):
>    $$D_i = q(a_i) \log \frac{q(a_i)}{p_X(a_i)} + [ 1 - q(a_i) ] \log \frac{1 - q(a_i)}{1 - p_X(a_i)} > 0 \quad$$
Poiché $D_i > 0$, il termine $2^{-nD_i}$ tende a zero in modo esponenzialmente veloce per $n \to \infty$. Questo garantisce che la frequenza empirica coincida quasi certamente con la vera probabilità teorica al limite.

> [!theorem] Teorema del Limite Deterministico
> La convergenza quasi certa implica che campioni diversi estratti dalla stessa popolazione mostreranno lo stesso comportamento statistico limite. Per ogni funzione continua $f(\cdot)$ dei dati vale:
> $$\operatorname{Pr} \left\{\lim_{n \rightarrow \infty} f(\boldsymbol{X}^n) = \lim_{n \rightarrow \infty} f(\boldsymbol{x}^n) \right\} = 1 \quad$$
> [!rb] Proprietà della Media Campionaria
> Come conseguenza del teorema precedente, la media campionaria è un estimatore **fortemente coerente**: essa converge con probabilità 1 alla media statistica della popolazione ($\mathbb{E}[X]$), eliminando ogni fluttuazione dovuta al caso nel limite asintotico.

## Commenti

In statistica inferenziale, una volta osservato un campione sufficientemente ampio, è possibile estrarre leggi che ogni altro campione estratto casualmente dalla stessa popolazione dovrebbe rispettare.

> [!def] Frequenza di occorrenza empirica ($f_n$)
> Considerando un campione $\pmb{x}^n \in \mathcal{X}^n$ estratto da una popolazione con spazio campionario $\mathcal{X} = \{ $a_1$, \ldots, a_M \}$ e pmf sconosciuta, la frazione di elementi osservati uguali ad $a_i$ su un totale di $n$ campioni è:
> $$f_n(a_i) = \frac{\# \text{ di elementi uguali a } a_i}{n}, \qquad i = 1, \ldots, M$$

> [!theorem] Limite deterministico delle frequenze
> Per $n \to \infty$, il comportamento delle frequenze diventa deterministico. La frequenza empirica converge con probabilità 1 (quasi certamente) alla probabilità teorica reale della popolazione:
> $$\operatorname{Pr} \left\{\lim_{n \rightarrow \infty} \frac{N_i}{n} = \lim_{n \rightarrow \infty} f_n(a_i) = p_X(a_i) \right\} = 1$$
> Ciò implica che qualsiasi altro campione $\pmb{y}^n$ estratto dalla stessa popolazione mostrerà lo stesso identico comportamento statistico limite.

> [!dim] Invarianza per funzioni continue
> Questo principio si estende a qualsiasi funzione continua $f(\cdot)$ dei dati. Il comportamento statistico limite di un campione casuale $\boldsymbol{X}^n$ è identico a quello del campione osservato $\pmb{x}^n$:
> $$\operatorname{Pr} \left\{\lim_{n \rightarrow \infty} f(\boldsymbol{X}^n) = \lim_{n \rightarrow \infty} f(\boldsymbol{x}^n) \right\} = 1$$

> [!def] Forte Coerenza (o Consistenza Forte)
> Un estimatore si dice **fortemente coerente** se converge quasi certamente (con probabilità 1) al valore vero del parametro che intende stimare all'aumentare della dimensione del campione ($n \to \infty$).

> [!rb] Convergenza della Media Campionaria
> Come conseguenza diretta del teorema precedente applicata alla funzione media, la media campionaria converge con probabilità uno alla media statistica della popolazione ($\mathbb{E}[X]$), soddisfacendo il requisito di **forte coerenza**.
