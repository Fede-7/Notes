---
toc: true
title: Metodi Statistici dell' Informazione
---
Report Tecnico: Teoria della Probabilità e Analisi Statistica
1. Analisi Combinatoria e Calcolo delle Cardinalità
L'analisi combinatoria costituisce l'impalcatura metodologica indispensabile per la determinazione rigorosa dello spazio campionario ( $\Omega$ ). In contesti caratterizzati da eventi elementari equiprobabili, la corretta enumerazione dei casi favorevoli rispetto ai casi possibili rappresenta l'unico strumento analitico atto a definire la misura della probabilità prima di introdurre variabili di condizionamento o asimmetrie stocastiche.
1.1 Principio del Prodotto Cartesiano e Disposizioni
Il calcolo delle  $k$ -uple ordinate, o disposizioni semplici, definisce il numero di modalità con cui  $k$  oggetti distinti possono essere estratti da un insieme di  $n$  elementi. La formula è espressa come:$$D_{n,k} = \frac{n!}{(n-k)!}$$Considerando la cardinalità di una mano di poker definita da semi specifici (cuori, fiori, picche, quadri) in un ordine prestabilito, il calcolo deriva dal prodotto delle cardinalità di quattro insiemi indipendenti di 13 carte ciascuno (prodotto cartesiano), risultando in  $13^4$ . La distinzione tra ordine e ripetizione è determinante: l'introduzione dell'ordinamento espande la dimensione dello spazio campionario, mentre la ripetizione ne modifica la struttura combinatoria fondamentale.
1.2 Combinazioni ( $k$ -uple non ordinate)
Qualora l'ordine di estrazione risulti irrilevante, si applica il principio di divisione per il fattoriale di  $k$ , riducendo le disposizioni a combinazioni semplici. Il coefficiente binomiale è definito come:$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$Esempio Pratico : In un mazzo da 32 carte, il numero di cinquine contenenti esattamente due assi si ottiene selezionando 2 assi su 4 e le restanti 3 carte dai 28 non-assi. Applicando il principio di divisione per il calcolo delle combinazioni non ordinate:  $$\binom{4}{2} \times \binom{28}{3} = \frac{4 \times 3}{2 \times 1} \times \frac{28 \times 27 \times 26}{3 \times 2 \times 1} = 6 \times 3.276 = 19.656$$
1.3 Sequenze Binarie e Coefficiente Multinomiale
Il conteggio di sequenze di  $n$  bit con esattamente  $k$  uni è una derivazione diretta del coefficiente binomiale:  $\frac{n!}{k!(n-k)!}$ . In presenza di un alfabeto  $m$ -ario, la formula si generalizza nel coefficiente multinomiale:$$\frac{n!}{n_1! n_2! \dots n_m!} \quad \text{con} \quad \sum_{i=1}^{m} n_i = n$$Tabella di Sintesi delle Tecniche di Conteggio| Tipo di Raggruppamento | Formula LaTeX | Condizione (Ordine/Ripetizione) || ------ | ------ | ------ || Disposizione Semplice | $\frac{n!}{(n-k)!}$ | Ordine rilevante / No ripetizione || Combinazione Semplice | $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ | Ordine irrilevante / No ripetizione || Permutazione | $n!$ | Ordine rilevante / Tutti gli elementi || Disposizione con Ripetizione | $n^k$ | Ordine rilevante / Con ripetizione |
La corretta determinazione della cardinalità degli eventi permette di traslare il conteggio discreto nella misurazione formale della probabilità.
2. Fondamenti e Assiomi della Probabilità
La transizione dalla frequenza empirica all'assiomatizzazione di Kolmogorov rappresenta il passaggio da una misurazione basata sull'osservazione sperimentale a un modello matematico coerente. Tale struttura garantisce la consistenza logica necessaria per l'analisi di eventi complessi, superando i limiti della pura intuizione frequentista.
2.1 Definizione Frequentista
La probabilità è definita come il limite della frequenza relativa di un evento  $A$  su un numero di prove  $n$  tendente all'infinito:$$P(A) = \lim_{n \to \infty} \frac{n_A}{n}$$Il principio di convergenza in probabilità assicura che, per  $n$  sufficientemente elevato, la frequenza relativa si stabilizzi intorno al valore teorico  $P(A)$ .
2.2 Assiomi di Kolmogorov
Il modello matematico della probabilità è fondato sui seguenti tre assiomi:
$$P(A) \geq 0, \quad \forall A \subseteq \Omega$$
$$P(\Omega) = 1$$
$$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i) \quad \text{se} \quad A_i \cap A_j = \emptyset, \quad \forall i \neq j$$
2.3 Proprietà Derivate
Dalla struttura assiomatica discendono le proprietà fondamentali per il calcolo operativo:
Unione :  $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
Complemento :  $P($A^c$) = 1 - P(A)$Esempio Pratico : La probabilità di un evento impossibile  $\emptyset$  è derivata come complemento dello spazio campionario certo:  $P(\emptyset) = 1 - P(\Omega) = 1 - 1 = 0$ .L'efficacia del modello probabilistico risiede nella capacità di aggiornare la misura della probabilità in funzione di informazioni parziali.
3. Probabilità Condizionata, Indipendenza e Teorema di Bayes
La probabilità condizionata è lo strumento cardine per l'inferenza statistica, consentendo la riduzione dello spazio campionario originale  $\Omega$  a un sottoinsieme coerente con l'informazione acquisita.
3.1 Definizione di Probabilità Condizionata
La misura della probabilità di un evento  $A$  dato il verificarsi di  $B$  è definita dal rapporto:$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$
3.2 Indipendenza Statistica
Due eventi si definiscono indipendenti se il verificarsi di  $B$  non altera la misura di  $A$ , ovvero se:$$P(A \cap B) = P(A)P(B)$$L'indipendenza semplifica i modelli di calcolo permettendo la fattorizzazione delle probabilità congiunte.
3.3 Legge della Probabilità Totale e Teorema di Bayes
Data una partizione  $\{E_i\}$  di  $\Omega$ , la probabilità di un evento  $A$  è data da  $P(A) = \sum_i P(A|$E_i$)P($E_i$)$ . L'inversione stocastica avviene tramite il Teorema di Bayes:$$P(E_i|A) = \frac{P(A|E_i)P(E_i)}{\sum_j P(A|E_j)P(E_j)}$$Esempio Pratico : Si consideri un'urna contenente un dado onesto ( $D_o$ ) e uno truccato ( $D_t$ ) con  $P(6|$D_t$)=1/2$  e altri esiti equiprobabili  $P(i|$D_t$)=1/10$ . Estratto un dado, si osserva la sequenza "55".
$P(55|$D_t$) = (1/10)^2 = 0.01$
$P(55|$D_o$) = (1/6)^2 \approx 0.027$
Assumendo  $P($D_t$)=P($D_o$)=0.5$ :  $P(D_t|55) = $\frac{0.01 \times 0.5}{(0.01 \times 0.5) + (0.027 \times 0.5)}$ \approx 0.27$La formalizzazione degli esiti probabilistici trova la sua massima espressione quantitativa attraverso il concetto di variabile aleatoria.
4. Variabili Aleatorie Discrete e Distribuzioni Notevoli
Le variabili aleatorie operano una mappatura misurabile tra gli eventi dello spazio campionario e i numeri reali, abilitando l'analisi quantitativa tramite funzioni matematiche.
4.1 Probability Mass Function (PMF)
Per variabili discrete, la PMF definisce la probabilità che  $X$  assuma il valore  $x$ :  $p_X(x) = P(X=x)$ . La funzione deve soddisfare il requisito di normalizzazione:$$\sum_{i} p_i = 1$$
4.2 Distribuzione Binomiale
Modella il numero di successi  $k$  in  $n$  prove indipendenti (processo di Bernoulli) con probabilità di successo  $p$ :$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
4.3 Distribuzione di Poisson
Modella il numero di eventi rari che si verificano in un intervallo continuo con tasso medio  $\lambda$ :$$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$Tabella Comparativa delle Distribuzioni| Distribuzione | Parametri | Media  $EX$ | Contesto d'uso || ------ | ------ | ------ | ------ || Binomiale | $n, p$ | $np$ | Prove discrete indipendenti || Poisson | $\lambda$ | $\lambda$ | Eventi rari su intervalli continui |
La sintesi delle distribuzioni avviene attraverso gli indicatori globali o momenti, che ne descrivono la forma e la dispersione.
5. Caratterizzazione Globale: Media, Varianza e Disuguaglianze
La media e la varianza sono descrittori sintetici atti a interpretare il comportamento di una variabile aleatoria identificandone il baricentro e il grado di incertezza.
5.1 Valore Atteso (Media)
Rappresenta la tendenza centrale della distribuzione:$$EX = \sum_{i} x_i p_i$$L'operatore valore atteso è lineare:  $EaX + b = aEX + b$ .
5.2 Varianza e Deviazione Standard
La varianza misura la dispersione quadratica intorno alla media:$$\sigma^2 = Var(X) = EX^2 - (EX)^2$$La varianza risente quadraticamente della scalatura:  $Var(aX + b) = a^2 Var(X)$ .
5.3 Disuguaglianze di Markov e Chebyshev
Forniscono limiti superiori alla probabilità di eventi estremi. La disuguaglianza di Chebyshev stabilisce:$$P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$Esempio Pratico : La probabilità che una variabile disti più di 10 deviazioni standard dalla propria media è limitata superiormente dal valore:  $$P(|X - \mu| \geq 10\sigma) \leq \frac{1}{10^2} = 0.01$$L'analisi si estende naturalmente a sistemi complessi in cui più variabili aleatorie interagiscono e mostrano dipendenze reciproche.
6. Variabili Aleatorie Multiple e Correlazione
L'analisi di database multidimensionali richiede lo studio della dipendenza statistica tra variabili per comprendere come il variare di un parametro influenzi la distribuzione degli altri.
6.1 PMF Congiunta e Marginalizzazione
La PMF congiunta  $P(X=x, Y=y)$  descrive la probabilità simultanea degli esiti. La marginalizzazione permette di isolare il comportamento di una singola variabile:$$P(X=x) = \sum_{y} P(x,y)$$
6.2 Indipendenza tra Variabili
Le variabili sono indipendenti se la PMF congiunta è data dal prodotto delle marginali:  $P(X,Y) = P(X)P(Y)$ .Esempio Pratico : Data una tabella  $2 \times 2$  con  $P(0,0)=1/4, P(0,1)=1/8, P(1,0)=1/8, P(1,1)=1/2$ :
Marginali:  $P(X=0) = 3/8$ ;  $P(Y=0) = 3/8$ .
Verifica:  $P(X=0)P(Y=0) = 9/64 \neq 1/4$ . Le variabili presentano dipendenza statistica.
6.3 PMF Condizionale per Variabili Multiple
Definisce come l'osservazione di una variabile modifichi la distribuzione dell'altra:$$P(X|Y) = \frac{P(X,Y)}{P(Y)}$$Tabella di Sintesi Relazioni Multidimensionali| Relazione | Formula | Significato || ------ | ------ | ------ || Congiunta | $P(X,Y)$ | Probabilità simultanea di  $X$  e  $Y$ || Marginale | $\sum_y P(x,y)$ | Probabilità di  $X$  indipendentemente da  $Y$ || Condizionale | $P(X,Y) / P(Y)$ | Probabilità di  $X$  data l'osservazione di  $Y$ |

