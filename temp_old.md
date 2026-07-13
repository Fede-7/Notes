## Definizioni Generali

Consideriamo un campione $\mathbf{X}$ estratto da un vettore casuale $\mathbf{Y}$. 

$\mathcal { X } ^ { n }$ può essere discreto o continuo, ma si assume che $X ^ { n }$ abbia una pdf (pmf, nel caso discreto) nota appartenere a una famiglia con prior nota. Si assume quindi la conoscenza della pdf congiunta $f _ { \pmb { X } ^ { n } , \Theta } ( \pmb { x } ^ { n } , \theta )$ e del parametro prior $f _ { \Theta } ( \theta )$. 

L'obiettivo è inferire il valore del parametro di $\theta$ per la realizzazione osservata $\pmb { x } ^ { n }$. La stima MMSE e la stima MAP sono quindi definite come:

$$
\widehat {\theta} _ {\mathrm{MMSE}} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n}) d \theta , \quad \widehat {\theta} _ {\mathrm{MAP}} (\boldsymbol {x} ^ {n}) = \arg \max _ {\theta} f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta | \boldsymbol {x} ^ {n})
$$

> [!theorem] Non distorto (Unbiased)
> Un estimatore è non distorto (*unbiased*) se $\mathbb { E } \left[ \widehat { \Theta } ( \pmb { \cal X } ^ { n } ) - \Theta \right] = 0 ;$.

> [!theorem] Asintoticamente non distorto
> Un estimatore è asintoticamente non distorto se è non distorto solo nel limite di una dimensione del campione infinita.

> [!theorem] Consistente
> Un estimatore è consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in probabilità.

> [!theorem] MS Consistente
> Un estimatore è MS consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ in media quadratica.

> [!theorem] Fortemente Consistente
> Un estimatore è fortemente consistente se ${ \widehat { \Theta } } ( X ^ { n } ) \to \Theta$ quasi certamente.

## Un esempio: Osservazioni Gaussiane con media casuale

Sia $x$ estratto da $y$ con: 

$$
f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) = \prod_ {i = 1} ^ {n} \frac {1}{\sqrt {2 \pi \sigma^ {2}}} \exp \left[ - \frac {(x _ {i} - \mu) ^ {2}}{2 \sigma^ {2}} \right]
$$

Sia $\mathbf{x}$ una realizzazione di $\mathbf{y}$. 

Vogliamo inferire il valore $\mu$ di $M$ appartenente all'osservazione $\mathbf{x}$ di $\mathbf{y}$. 

Si noti che la densità a posteriori della media è: 

$$
f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \frac {f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) f _ {M} (\mu)}{f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})} = \mathcal {N} \left(\frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}, \frac {1}{\frac {n}{\sigma^ {2}} + \frac {1}{\sigma_ {M} ^ {2}}}\right)
$$

In altri termini, il prior coniugato della media di una distribuzione Gaussiana è nuovamente Gaussiano. 

Abbiamo quindi che la stima MMSE della media è: 

$$
\widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} x _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text { MMSE }} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

Consideriamo ora la stima MAP. È possibile scrivere: 

$$
\ln f _ {M | \boldsymbol {X} ^ {n}} (\mu | \boldsymbol {x} ^ {n}) = \ln f _ {\boldsymbol {X} ^ {n} | M} (\boldsymbol {x} ^ {n} | \mu) + \ln f _ {M} (\mu) - \ln f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n})
$$

Massimizzando rispetto a $\mu$ si ottiene lo stimatore MAP: 

$$
\widehat {\mu} _ {\text {MAP}} (\boldsymbol {x} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}} \Longleftrightarrow \widehat {M} _ {\text {MAP}} (\boldsymbol {X} ^ {n}) = \frac {\sum_ {i = 1} ^ {n} X _ {i}}{n + \frac {\sigma^ {2}}{\sigma_ {M} ^ {2}}}
$$

che coincide con l'MMSEE. 

> [!quote] Osservazione
> È casuale o esiste un motivo più profondo per la coincidenza di questi due stimatori?

## Unicità degli stimatori Bayesiani

Sia $C(\cdot)$ una funzione di costo arbitraria dell'errore di stima. 

Si assuma che $C(\cdot)$ sia pari e convessa e che $\mathbf{y}$ sia simmetrica rispetto alla sua media $\mu$, ovvero: 

$$
f _ {\Theta | \boldsymbol {X} ^ {n}} (\theta - \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n}) = f _ {\Theta | \boldsymbol {X} ^ {n}} (- \theta + \mathbb {E} [ \Theta | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} ] | \boldsymbol {x} ^ {n})
$$

Allora l'MMSEE minimizza il rischio Bayesiano per qualsiasi funzione di costo in questa classe. 

La dimostrazione è omessa in questo testo. 

Si noti che, rigorosamente parlando, la funzione di costo 0-1 che porta a uno stimatore MAP non è differenziabile. Tuttavia, può essere dimostrato che, sotto la condizione di simmetria sopra indicata sulla distribuzione a posteriori, si ha: 

$$
\widehat {\mu} _ {\text { MAP }} (\boldsymbol {x} ^ {n}) = \widehat {\mu} _ {\text { MMSE }} (\boldsymbol {x} ^ {n})
$$

# Inferenza non Bayesiana: Stima di parametri non casuali

Assumiamo ora che le osservazioni $\pmb { x } ^ { n } \in \mathcal { X } ^ { n }$ siano estratte da una famiglia di pdf, $f _ { { \pmb X } ^ { n } } \big ( { \pmb x } ^ { n } ; { \boldsymbol \theta } \big )$; 

Assumiamo che $\theta$ sia deterministico e sconosciuto: equivalentemente, possiamo assumere che non abbiamo informazioni a priori sufficienti per assegnare un prior $f _ { \Theta } ( \theta )$ ); 

Assumiamo che lo spazio dei parametri sia $S$; 

Definiamo la **verosimiglianza** del parametro $\theta$, dato che le osservazioni $\pmb { x } ^ { n }$ sono disponibili, la funzione: 

$$
L (\theta ; \boldsymbol {x} ^ {n}) = f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

o, equivalentemente, la log-verosimiglianza la funzione 

$$
\Lambda (\theta ; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta)
$$

Una stima di Massima Verosimiglianza (ML) di $\theta$ è 

$$
\widehat {\theta} _ {\mathrm{ML}} \left(\boldsymbol {x} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right)
$$

ed è una realizzazione dello stimatore di Massima Verosimiglianza (MLE): 

$$
\widehat {\Theta} _ {M L} \left(\boldsymbol {X} ^ {n}\right) = \arg \max _ {\theta \in \mathcal {S}} \log f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \theta\right)
$$

## Inferenza non Bayesiana: Misure di prestazione

Data uno stimatore $\Theta ( { \pmb x } ^ { n } )$ del parametro non casuale $\theta ,$, abbiamo: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \theta + b _ {n} (\theta)
$$

con $b _ { n } ( \theta )$ il **bias** dello stimatore; 

Lo stimatore è non distorto (unbiased) se $b _ { n } ( \theta ) = 0$, mentre è solo asintoticamente non distorto se $b _ { n } ( \theta )$ diventa infinitesimale con $n ;$ 

L'errore casuale dello stimatore è solitamente quantificato tramite il suo valore Mean Square, ovvero: 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \overline {{e _ {n} ^ {2}}}
$$

Uno stimatore MMSE non distorto di $\theta$ è uno stimatore che minimizza la varianza: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \mathbb {E} \left[ \Theta^ {2} (\boldsymbol {X} ^ {n}) \right] - \theta^ {2}
$$

Uno stimatore è debolmente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ in probabilità, fortemente consistente se $\Theta ( { \pmb x } ^ { n } ) \to \theta$ quasi certamente, MS consistente se $\overline { { e _ { n } ^ { 2 } } } \to 0$ 

## Limite di Cramér-Rao 
### Fatti preliminari

Sia $\pmb { x } ^ { n }$ un campione estratto da un vettore casuale ${ \pmb X } ^ { n } \sim f _ { { \pmb X } ^ { n } } ( { \pmb x } ^ { n } ; { \pmb \theta } )$ con $\theta$ non casuale; 

Consideriamo l'identità 

$$
\int_ {\mathbb {R} ^ {n}} f _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {x} ^ {n}; \theta\right) d \boldsymbol {x} ^ {n} = 1
$$

Dopo la differenziazione rispetto a $\theta$ della precedente abbiamo 

$$
\begin{array}{c} \int_ {\mathbb {R} ^ {n}} \frac {\partial f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} d \boldsymbol {x} ^ {n} = \int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}; \theta) d \boldsymbol {x} ^ {n} \\ = \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 0 \end{array}
$$

Differenziando ancora abbiamo: 

$$
\begin{array}{c} \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = \text {var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = \\ = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right] \end{array}
$$

### Derivazione

Sia $\widehat { \Theta } ( X ^ { n } )$ uno stimatore del parametro non casuale $\theta$ con: 

$$
\mathbb {E} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] = \int_ {\mathbb {R} ^ {n}} \widehat {\Theta} (\boldsymbol {X} ^ {n}) f _ {\boldsymbol {X} ^ {n}} (x ^ {n}; \theta) d x ^ {n} = \theta + b _ {n} (\theta)
$$

Differenziando rispetto a $\theta$ l'identità precedente abbiamo 

$$
\begin{array}{l} \mathbb {E} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \\ \int_ {\mathbb {R} ^ {n}} \Theta (x ^ {n}) \frac {\partial f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta}   d x ^ {n} = \overbrace {\int_ {\mathbb {R} ^ {n}} \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)}{\partial \theta} f _ {\boldsymbol {X} ^ {n}} (x ^ {n} ; \theta)   d x ^ {n}} \\ \text { COV } \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] = 1 + b _ {n} ^ {\prime} (\theta) \end{array}
$$

Applicando la diseguaglianza di Cauchy-Schwarz, otteniamo finalmente 

$$
\left| \operatorname{COV} \left[ \Theta (\boldsymbol {X} ^ {n}), \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right] \right| ^ {2} = \left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2} \leq \operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \operatorname{Var} \left[ \frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta} \right]
$$

### Ulteriori discussioni

Elaborando le derivazioni precedenti, otteniamo un limite inferiore imbattibile alla varianza di qualsiasi stimatore del parametro non casuale $\theta$ nella forma: 

$$
\operatorname{Var} \left[ \Theta (\boldsymbol {X} ^ {n}) \right] \geq \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{\mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right]} = \frac {\left[ 1 + b _ {n} ^ {\prime} (\theta) \right] ^ {2}}{I _ {n} (\theta)}
$$

La quantità $I _ { n } ( \theta )$ è definita come **Informazione di Fisher**, e obbedisce alla seguente identità: 

$$
I _ {n} (\theta) = \mathbb {E} \left[ \left(\frac {\partial \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta}\right) ^ {2} \right] = - \mathbb {E} \left[ \frac {\partial^ {2} \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \theta)}{\partial \theta^ {2}} \right]
$$

### Stimatori non distorti

Come anticipato, lo stimatore $\Theta ( { \pmb x } ^ { n } )$ è non distorto se $\mathbb{E}$ $[ \Theta ( { \pmb x } ^ { n } ) ] = \theta$ 

In questa situazione, abbiamo che 

$$
\mathbb {E} \left[ (\Theta (\boldsymbol {X} ^ {n}) - \theta) ^ {2} \right] = \operatorname{Var} [ \Theta (\boldsymbol {X} ^ {n}) ] \geq \frac {1}{I _ {n} (\theta)}
$$

Così il Limite di Cramér-Rao (CRB) diventa un limite inferiore imbattibile all'MSE di qualsiasi stimatore. 

Uno stimatore non distorto il cui MSE è uguale al CRB è definito **efficiente** 

> [!theorem] Fatto importante
> Se esiste uno stimatore efficiente per un dato problema di stima non Bayesiana, questo coincide necessariamente con lo stimatore ML. 

## Un esempio: inferire la frequenza del cifrario di una sorgente senza memoria

Consideriamo inizialmente $\pmb { x } ^ { n } \in \{ 0 , 1 \} ^ { n }$ , estratto da $\pmb { X } ^ { n } \sim  { \mathcal { B } } ( 1 , \beta )$ , $\beta$ sconosciuto; 

Abbiamo visto che, se $w ( \pmb { x } ^ { n } )$ è il peso di Hamming della sequenza osservata, allora: 

$$
p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}) = \beta^ {w (\boldsymbol {x} ^ {n})} (1 - \beta) ^ {n - w (\boldsymbol {x} ^ {n})}
$$

La stima ML viene quindi trovata come: 

$$
\frac {\partial \log p _ {X ^ {n}} (x ^ {n})}{\partial \beta} = 0 \Longrightarrow \widehat {\beta} _ {\mathrm{ML}} (x ^ {n}) = \frac {w (x ^ {n})}{n}
$$

L'estimatore $\begin{array} { r } { \beta ( \pmb { X } ^ { n } ) = \frac { w ( \pmb { X } ^ { n } ) } { n } } \end{array}$ è tale che: 

$$
\mathbb {E} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \beta  ,
$$

$$
\operatorname{var} \left[ \frac {w (\boldsymbol {X} ^ {n})}{n} \right] = \frac {\beta (1 - \beta)}{n}
$$

Di conseguenza, è non distorto (unbiased) e MS consistente. È efficiente?

Si noti che abbiamo: 

$$
\log p _ {\boldsymbol {X} ^ {n}} \left(\boldsymbol {X} ^ {n}; \beta\right) = w \left(\boldsymbol {X} ^ {n}\right) \log \beta + [ n - w \left(\boldsymbol {X} ^ {n}\right) ] \log (1 - \beta)
$$

Pertanto abbiamo: 

$$
\frac {\partial p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta} = \frac {w (\boldsymbol {X} ^ {n})}{\beta} - \frac {n - w (\boldsymbol {X} ^ {n})}{1 - \beta}
$$

$$
\frac {\partial^ {2} p _ {\boldsymbol {X} ^ {n}} (\boldsymbol {X} ^ {n} ; \beta)}{\partial \beta^ {2}} = - \frac {w (\boldsymbol {X} ^ {n})}{\beta^ {2}} - \frac {n - w (\boldsymbol {X} ^ {n})}{(1 - \beta) ^ {2}}
$$

Poiché $\mathbb { E } [ w ( \pmb { X } ^ { n } ) ] = \pmb { n } \beta$ , abbiamo: 

$$
I _ {n} (\beta) = \frac {n}{\beta} + \frac {n}{1 - \beta} = \frac {n}{\beta (1 - \beta)} \Longrightarrow \mathrm{CRB} = \frac {\beta (1 - \beta)}{n}
$$

Concludiamo che la **MLE** (Maximum Likelihood Estimation) della frequenza di cifratura è efficiente. 

# Stima a parametri multipli
## inferenza Bayesiana

Assumiamo ora di avere $m$ parametri casuali, $\pmb { \theta } [ \theta _ { 1 } , \ldots , \theta _ { m } ] ^ { T }$ estratti da una pdf nota $f _ { \Theta } ( \pmb { \theta } )$ e un set di dati $\pmb { x } ^ { n }$ estratti da una pdf condizionale $f _ { { \pmb X } ^ { n } | \pmb \theta } ( { \pmb x } ^ { n } | \pmb \theta )$.

Definiamo una funzione di costo 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = C \left(\theta_ {1} - \widehat {\theta} _ {1}, \dots , \theta_ {m} - \widehat {\theta} _ {m}\right)
$$

Un estimatore Bayes-ottimale può essere trovato risolvendo il problema di minimizzazione: 

$$
\widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n}): \quad \mathbb {E} \left[ C (\boldsymbol {\Theta} - \widehat {\boldsymbol {\Theta}} (\boldsymbol {X} ^ {n})) \right] = 0
$$

Utilizzando la stessa procedura del caso a parametro singolo otteniamo quindi: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \arg \min \int_ {\mathbb {R} ^ {m}} C \left(\boldsymbol {\theta} - \widehat {\theta} \left(\boldsymbol {X} ^ {n}\right)\right) f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {X} ^ {n}\right) d \boldsymbol {\theta}
$$

### L'estimatore MMSE

> [!theorem] Estimatore MMSE
> L'**MMSE** (Minimum Mean Square Error) è l'estimatore che minimizza il valore atteso del quadrato dell'errore tra la stima e il valore reale.
> 
> Formalizzazione:
> $$ \hat{\theta}_{MMSE} = \arg\min_{\hat{\theta}} E[||\theta - \hat{\theta}||^2] $$

Assumiamo che la funzione di costo sia 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \left(\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}))\right)
$$

Poiché il problema di minimizzazione è disgiunto (ovvero, separabile), abbiamo: 

$$
\widehat {\theta} _ {i} (\boldsymbol {x} ^ {n}) = \mathbb {E} \left[ \Theta_ {i} | \boldsymbol {X} ^ {n} = \boldsymbol {x} ^ {n} \right] = \int \theta_ {i} f _ {\theta_ {i} | \boldsymbol {X} ^ {n}} (\theta_ {i} | \boldsymbol {x} ^ {n}) d \theta_ {i}
$$

dove l'estimatore vettoriale MMSE si legge: 

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \mathbb {E} \left[ \Theta | \boldsymbol {X} ^ {n} \right]
$$

### L'estimatore MAP

> [!theorem] Estimatore MAP
> La **MAP** (Maximum A Posteriori) è un metodo di stima che massimizza la probabilità a posteriori del parametro, combinando la verosimiglianza dei dati con la conoscenza a priori sulla distribuzione dei parametri.
> 
> Formalizzazione:
> $$ \hat{\theta}_{MAP} = \arg\max_{\theta} p(\theta | \mathbf{x}) $$

Se assumiamo 

$$
C (\boldsymbol {\theta} - \widehat {\boldsymbol {\theta}}) = \sum_ {i = 1} ^ {m} \Pi \left(\frac {\theta_ {i} - \widehat {\theta} _ {i} (\boldsymbol {x} ^ {n})}{\epsilon}\right)
$$

considerando la stessa procedura abbiamo 

$$
\widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right): \quad \frac {\partial f _ {\Theta | \boldsymbol {X} ^ {n}} \left(\boldsymbol {\theta} \mid \boldsymbol {x} ^ {n}\right)}{\partial \theta_ {i}} \Bigg | _ {\theta_ {i} = \widehat {\theta} _ {i} \left(\boldsymbol {x} ^ {n}\right)} = 0
$$

Equivalentemente, abbiamo che la stima MAP risolve l'equazione: 

$$
\nabla_ {\boldsymbol {\theta}} f _ {\boldsymbol {\Theta} | \boldsymbol {X} ^ {n}} (\boldsymbol {\theta} | \boldsymbol {x} ^ {n}) \big | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (x ^ {n})} = 0
$$

## Stima non Bayesiana di parametri multipli

Assumiamo ora che il vettore dei parametri $\pmb { \theta }$ sia reale e deterministico; 

Possiamo definire la funzione di log-verosimiglianza dei dati osservati, assunti estratti da una famiglia di distribuzioni $f _ { \pmb { X } ^ { n } } ( \pmb { x } ^ { n } ; \pmb { \theta } )$ come: 

$$
\Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) = \log f _ {\boldsymbol {X} ^ {n}} (\boldsymbol {x} ^ {n}, \boldsymbol {\theta})
$$

Definiamo la stima Maximum-Likelihood del vettore $\pmb { \theta }$ come la soluzione dell'equazione: 

$$
\nabla_ {\boldsymbol {\theta}} \Lambda (\boldsymbol {\theta}; \boldsymbol {x} ^ {n}) | _ {\boldsymbol {\theta} = \widehat {\boldsymbol {\theta}} (\boldsymbol {x} ^ {n})} = 0
$$

L'estimatore corrispondente $\widehat { \Theta } ( X ^ { n } )$ è di nuovo definito come un estimatore Maximum Likelihood (ML) e gode di una serie di proprietà fondamentali. 

### Estimatori MMSE lineari

0 Iniziamo con un semplice problema scalare. Assumiamo che $\pmb { x } ^ { n }$ sia il campione osservato, estratto da $X ^ { n }$, e assumiamo di voler progettare un estimatore lineare di un parametro casuale $\Theta ,$, distribuito secondo una legge nota, nella forma: 

$$
\widehat {\Theta} (\boldsymbol {X} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b \quad \boldsymbol {a} \in \mathbb {R} ^ {n}
$$

Un estimatore **Linear MMSE** (LMMSE) seleziona il vettore $\mathbf{a}$ e la costante $b$ in modo da minimizzare l'MMSE 

$$
\mathbb {E} \left[ (\widehat {\Theta} (\boldsymbol {X} ^ {n}) - \Theta) ^ {2} \right] = \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]
$$

che è uguale a 

$$
\boldsymbol {a} ^ {T} \boldsymbol {R} \boldsymbol {a} + b ^ {2} + \mathbb {E} [ \Theta^ {2} ] - 2 b (\overline {{{\Theta}}}) - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] - 2 b \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

dove $\pmb { R } = \mathbb { E } \left[ \pmb { X } ^ { n } \pmb { X } ^ { n T } \right]$ è la matrice di correlazione del vettore casuale $X ^ { n }$.

Annullando il gradiente rispetto ad $\mathbf{a}$ e la derivata rispetto a $b$ otteniamo: 

$$
\nabla_ {\boldsymbol {a}} \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} [ \boldsymbol {X} ^ {n} \Theta ] = 0
$$

$$
\frac {\partial \mathbb {E} \left[ (\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta) ^ {2} \right]}{\partial b} = 2 b - 2 \overline {{\Theta}} - 2 \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ] = 0
$$

- Risolvendo per b si ottiene:

$$
b _ {\text { LMMSE }} = \mathbb {E} [ \Theta ] - \boldsymbol {a} ^ {T} \mathbb {E} [ \boldsymbol {X} ^ {n} ]
$$

$$
\widehat {\Theta} \left(\boldsymbol {X} ^ {n}\right) = \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + \mathbb {E} [ \Theta ]
$$

che, reinserito nell'MSE dimostra che $\mathbf{a}$ dovrebbe minimizzare 

$$
\left\| \boldsymbol {a} ^ {T} \left(\boldsymbol {X} ^ {n} - \mathbb {E} \left[ \boldsymbol {X} ^ {n} \right]\right) + (\Theta - \mathbb {E} [ \Theta ]) \right\| ^ {2}
$$

Di conseguenza, denotando $\pmb { M } = \mathbb { E } \left[ ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ( \pmb { X } ^ { n } - \mathbb { E } [ \pmb { X } ^ { n } ] ) ^ { T } \right]$ la matrice di covarianza di $X ^ { n }$, l'estimatore LMMSE si legge 

$$
\boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {M} ^ {- 1} \mathbb {E} \left[ \left(\boldsymbol {X} ^ {n} - \mathbb {E} [ \boldsymbol {X} ^ {n} ]\right) (\Theta - \mathbb {E} [ \Theta ]) \right] = \boldsymbol {M} ^ {- 1} \boldsymbol {s}
$$

### L'algoritmo del gradiente

Assumiamo di voler risolvere iterativamente il problema LMMSE delineato in precedenza; 
Abbiamo visto che il gradiente dell'MSE è scritto come 

$$
\nabla_ {a} \mathbb {E} \left[ \left(\boldsymbol {a} ^ {T} \boldsymbol {X} ^ {n} + b - \Theta\right) ^ {2} \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \mathbb {E} \left[ \boldsymbol {X} ^ {n} \Theta \right] = 2 \boldsymbol {M} \boldsymbol {a} - 2 \boldsymbol {s}
$$

con $\mathbb { E } \left[ \pmb { X } ^ { n } \Theta \right] = \pmb { s }$ noto; 

Consideriamo la seguente iterazione per determinare $\pmb { \alpha } _ { \mathrm { L M M S E } }$ 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma (\boldsymbol {M a} ^ {(n)} - \boldsymbol {s})
$$

che può essere riscritta come 

$$
\boldsymbol {a} ^ {(n + 1)} = \boldsymbol {a} ^ {(n)} - \gamma \boldsymbol {M} \left(\boldsymbol {a} ^ {(n)} - \underbrace {\boldsymbol {M} ^ {- 1} \boldsymbol {s}} _ {\boldsymbol {a} _ {\text { LMMSE }}}\right)
$$


L'errore alla $(n + 1)$-es iterazione si legge 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = \boldsymbol {a} ^ {(n + 1)} - \boldsymbol {a} _ {\text { LMMSE }} = \boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }} - \gamma \boldsymbol {M} (\boldsymbol {a} ^ {(n)} - \boldsymbol {a} _ {\text { LMMSE }}) = (\boldsymbol {I} - \gamma \boldsymbol {M}) \boldsymbol {\epsilon} ^ {(n)}
$$

Di conseguenza abbiamo 

$$
\boldsymbol {\epsilon} ^ {(n + 1)} = (\boldsymbol {I} - \gamma \boldsymbol {M}) ^ {n} \boldsymbol {\epsilon} ^ {(1)} = \boldsymbol {U} (\boldsymbol {I} - \gamma \boldsymbol {\Lambda}) ^ {n} \boldsymbol {U} ^ {T}
$$

dove $\Lambda$ è la matrice diagonale dei valori propri di $M$ e $U$ contiene i suoi autovettori. 

L'errore converge quindi a zero se il modulo massimo dei valori propri o $\pmb { I } - \gamma \pmb { M }$ è minore di uno, cioè: 

$$
- 1 <   1 - \gamma \lambda_ {M A X} <   1 \Longrightarrow 0 <   \gamma <   \frac {2}{\lambda_ {M A X}}
$$

# Un approccio diverso: statistica descrittiva

In questa sezione si abbandona l'approccio probabilistico per adottare la **statistica descrittiva**, in cui i campioni sono considerati come entità dati e non come realizzazioni di vettori casuali.

Si definisce un *dataset* di addestramento come una collezione di $p$ campioni $n$-dimensionali, organizzabili nella matrice $n \times p$:

$$
\boldsymbol {X} = \left[ \begin{array}{c c c} x _ {1} (1) & \dots & x _ {1} (p) \\ \dots & \dots & \dots \\ x _ {n} (1) & \dots & x _ {n} (p) \end{array} \right] \in \mathbb {R} ^ {n \times p}
$$

Si supponga di conoscere $p$ valori misurati del parametro $\theta _ { r }$, ciascuno corrispondente a uno dei $p$ campioni $n$-dimensionali del *training set*, ovvero:

$$
\boldsymbol {y} = [ \theta (1), \dots , \theta (p) ] \in \mathbb {R} ^ {p}
$$

L'obiettivo è adattare i dati a un modello lineare nella forma:

$$ \mathbf{y} = \mathbf{X}\boldsymbol{\theta} + \boldsymbol{\epsilon} \tag{1} $$

dove $\epsilon _ { n }$ incapsula l'errore di modellazione.

## L'estimatore dei Minimi Quadrati (Least Squares)

Data la natura del dataset $p$-dimensionale, si procede alla selezione di $a$ al fine di minimizzare la seguente funzione di costo:

$$
\parallel \epsilon_ {n} \parallel^ {2} = \sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il problema consiste nel selezionare ottimamente $a$ e $b$. Preliminarmente, si osserva che:

$$
\sum_ {i = 1} ^ {p} \left[ \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} (i) - \theta (i) \right] ^ {2} = \| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2}
$$

Si nota inoltre che:

$$
\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \| ^ {2} = \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} + \| \boldsymbol {y} \| ^ {2} - 2 \boldsymbol {a} ^ {T} \boldsymbol {X} \boldsymbol {y}
$$


Differenziando la funzione di costo rispetto a $a$, si ottiene:

$$
\nabla_ {a} \left\| \boldsymbol {X} ^ {T} \boldsymbol {a} - \boldsymbol {y} \right\| ^ {2} = 2 \boldsymbol {X} \boldsymbol {X} ^ {T} \boldsymbol {a} - 2 \boldsymbol {X} \boldsymbol {y} = 0
$$

L'equazione risultante produce:

$$ (\mathbf{X}^T\mathbf{X})\boldsymbol{\theta} = \mathbf{X}^T\mathbf{y} \tag{2} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} = \left(\boldsymbol {X} \boldsymbol {X} ^ {T}\right) ^ {- 1} \boldsymbol {X} \boldsymbol {y}
$$

Questa condizione richiede che la matrice $( { \pmb x } { \pmb x } ^ { T } )$ sia invertibile $( \mathsf { i . e . , } \ p \geq n )$. Per riferimento futuro, la stima basata su un campione $p$-dimensionale viene denominata:

$$ \boldsymbol{\theta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y} \tag{3} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left(\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)\right) ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Si consideri un'osservazione dell'ambiente a orizzonte infinito, tale che la dimensione del campione $p$ possa aumentare indefinitamente. Si distinguono due scenari operativi:

1. Miglioramento progressivo della stima mediante l'aggiunta di nuove osservazioni;
2. Adattamento a condizioni variabili attraverso la "dimenticanza" delle osservazioni datate, al fine di pesare maggiormente i dati recenti.

È possibile regolare l'estimatore LS per gestire entrambi gli scenari con una complessità computazionale limitata.

## Apprendimento LS

Si supponga $p \geq n$ e che sia stata valutata la stima:

$$
\boldsymbol {a} _ {\mathrm{LS}} (p) = \left[ \boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p) \right] ^ {- 1} \boldsymbol {X} (p) \boldsymbol {y} (p)
$$

Considerando l'inserimento di un nuovo vettore nel dataset, denominato $\pmb { x } ^ { n } ( p + 1 )$, e una nuova osservazione $\theta ( p + 1 )$, la nuova stima sarebbe:

$$ \boldsymbol{\theta}_{new} = (\mathbf{X}_{new}^T\mathbf{X}_{new})^{-1}\mathbf{X}_{new}^T\mathbf{y}_{new} \tag{4} $$

$$
\boldsymbol {a} _ {\mathrm{LS}} (p + 1) = \left[ \boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1) \right] ^ {- 1} \boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1)
$$

> [!quote] Osservazione
> È necessario ricalcolare l'intera inversione di matrice per ogni nuovo dato?
> 
> L'operazione di inversione comporta una complessità $O(n^3)$, mentre il prodotto di matrici ha una complessità $O(n^2)$ (in termini di moltiplicazioni).

## La Formula di Sherman-Morrison

Sia $R$ una matrice invertibile di ordine $n ;$. Siano $u$ e $v$ vettori colonna $n$-dimensionali. Si applica il seguente lemma di inversione di matrice con aggiornamento *rank-1*:

$$
\left(\boldsymbol {R} + \boldsymbol {u v} ^ {T}\right) ^ {- 1} = \boldsymbol {R} ^ {- 1} - \frac {\boldsymbol {R} ^ {- 1} \boldsymbol {u v} ^ {T} \boldsymbol {R} ^ {- 1}}{1 + \boldsymbol {u} ^ {T} \boldsymbol {R} ^ {- 1} \boldsymbol {v}}
$$

## Applicazione

 Notare che



$$
\underbrace {\boldsymbol {X} (p + 1) \boldsymbol {X} ^ {T} (p + 1)} _ {\boldsymbol {R} (p + 1)} = \sum_ {i = 1} ^ {p + 1} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) = \underbrace {\boldsymbol {X} (p) \boldsymbol {X} ^ {T} (p)} _ {\boldsymbol {R} (p)} + \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1)
$$

Di conseguenza:



$$
\boldsymbol {R} ^ {- 1} (p + 1) = \boldsymbol {R} ^ {- 1} (p) - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p)}{1 + K (p + 1)}
$$

con:



$$
K (p + 1) = \boldsymbol {x} ^ {n T} (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)
$$


 D'altra parte abbiamo



$$
\boldsymbol {X} (p + 1) = \left[ \boldsymbol {X} (p) \boldsymbol {x} ^ {n} (p + 1) \right], \quad \boldsymbol {y} (p + 1) = \left[ \boldsymbol {y} (p) \theta (p + 1) \right] ^ {T}
$$

implicando:



$$
\boldsymbol {X} (p + 1) \boldsymbol {y} (p + 1) = \boldsymbol {X} (p) \boldsymbol {y} (p) + \theta (p + 1) \boldsymbol {x} ^ {n} (p + 1)
$$

Poiché ${ \pmb a } ( p + 1 ) = { \pmb R } ^ { - 1 } ( p + 1 ) { \pmb X } ( p + 1 ) { \pmb y } ( p + 1 )$, si ottiene:



$$
\boldsymbol {a} (p + 1) = \left[ \boldsymbol {I} _ {n} - \frac {\boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1)}{1 + K (p + 1)} \boldsymbol {x} ^ {n T} (p + 1) \right]
$$



$$
\left[ \boldsymbol {a} (p) + \theta (p + 1) \boldsymbol {R} ^ {- 1} (p) \boldsymbol {x} ^ {n} (p + 1) \right]
$$

L'operazione presenta una complessità $\mathcal { O } ( n ^ { 2 } )$, risultando indipendente (e non scalabile con) $p .$.

## Adattività in LS

Al fine di gestire situazioni in cui l'ambiente circostante può essere (lentamente) variabile nel tempo, è opportuno forzare i dati storici a pesare meno rispetto ai dati più recenti ("freschi").

Un metodo per ottenere tale comportamento è l'utilizzo della **media mobile esponenziale**, la cui idea principale consiste nell'adottare la seguente funzione di costo:

$$
\sum_ {i = 1} ^ {p} w ^ {p - i} \left[ \pmb {\mathscr {a}} ^ {T} \pmb {x} ^ {n} (i) - \theta (i) \right] ^ {2}
$$

Il peso $w < 1$ regola la velocità con cui il passato viene "dimenticato" dal modello.

Minimizzando rispetto a $a$ si ottiene l'**LS mediato esponenzialmente**:

$$
\boldsymbol {a} = \left[ \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \boldsymbol {x} ^ {n T} (i) \right] ^ {- 1} \sum_ {i = 1} ^ {p} w ^ {p - i} \boldsymbol {x} ^ {n} (i) \theta (i)
$$

Questa formulazione è suscettibile di un'implementazione ricorsiva grazie all'applicazione del lemma di Sherman-Morrison.

## Generalizzazione

Supponiamo ora che, mantenendo le stesse condizioni precedentemente analizzate, si desideri trovare un LS nella forma più generale:

$$
\widehat {\theta} (\boldsymbol {x} ^ {n}) = \boldsymbol {a} ^ {T} \boldsymbol {x} ^ {n} + b
$$

Calcoli analitici, sebbene articolati, portano alla forma **LMS generale**:

$$
\boldsymbol {a} _ {\text { LMS }} = (\boldsymbol {X} _ {0} \boldsymbol {X} _ {0} ^ {T}) ^ {- 1} \boldsymbol {X} _ {0} \boldsymbol {y} _ {0}, \qquad b _ {\text { LMS }} = \underbrace {\frac {1}{p} \sum_ {i = 1} ^ {p} \theta (i)} _ {\widetilde {\theta}} - \frac {1}{p} \boldsymbol {1} _ {p} ^ {T} \boldsymbol {X} ^ {T} \boldsymbol {a} _ {\text { LMS }}
$$

dove ${ \bf 1 } _ { p }$ è un vettore di tutti uno $p -$ dimensionale e

$$
\boldsymbol {X} _ {0} = \left[ \begin{array}{c c c} x _ {1} (1) - \overline {{x}} _ {1} & \dots & x _ {1} (p) - \overline {{x}} _ {1} \\ \dots & \dots & \dots \\ x _ {n} (1) - \overline {{x}} _ {n} & \dots & x _ {n} (p) - \overline {{x}} _ {n} \end{array} \right] \in \mathbb {R} ^ {n \times p}, \quad \boldsymbol {y} _ {0} = \left[ y _ {1} - \overline {{\theta}}, \ldots , y _ {p} - \overline {{\theta}} \right] ^ {T}
$$

con

$$
\overline {{x}} _ {k} = \frac {1}{p} \sum_ {i = 1} ^ {p} x _ {k} (i) \Longleftrightarrow \overline {{\mathbf {x}}} = \frac {1}{p} \sum_ {i = 1} ^ {p} \mathbf {x} ^ {n} (i), \quad \mathbf {X} _ {0} = \mathbf {X} - \overline {{\mathbf {x}}} \mathbf {1} _ {p} ^ {T}
$$
