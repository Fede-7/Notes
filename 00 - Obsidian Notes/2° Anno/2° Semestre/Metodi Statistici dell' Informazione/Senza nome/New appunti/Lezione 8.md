# SBOBINA - Teoria della Probabilità | Lezione sulla PMF Congiunta e Variabili Continue

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Teoria della Probabilità (Ingegneria/Informatica)
- **Docente**: Non specificato nel testo (Docente esperto di processi aleatori e filtraggio)
- **Orari e Aule**: Lezione erogata in prossimità di Pasqua; il prossimo incontro è fissato per giovedì dopo Pasqua.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con approfondimenti teorici e passaggi logici sulla lavagna/slide.
    - **Consigli pratici del docente**: 
        - "Non voglio sentire memoria ma logica": Il docente enfatizza l'importanza del ragionamento probabilistico rispetto alla memorizzazione delle formule.
        - **Toy Model**: Iniziare sempre dai modelli più semplici per comprendere il fenomeno prima di complicarlo.
- **Accesso ai Materiali**: Il docente rimanda alle slide per i dettagli formali e le derivazioni analitiche più estese che non sono state riportate integralmente a voce.

---

## 🎯 SOMMARIO RAPIDO
- Passaggio dalle variabili aleatorie discrete alla caratterizzazione congiunta (n-tuple) e marginalizzazione.
- Introduzione della probabilità condizionale, della Legge di Bayes e delle applicazioni ai sistemi dinamici (Catene di Markov, Filtraggio Predittivo).
- Teorema della Media Condizionale e analisi della linearità dell'operatore di speranza.
- Risoluzione di un problema applicativo sulle code di pacchetti (Distribuzioni Poissoniana e Binomiale).
- Introduzione teorica alle variabili aleatorie continue e alla densità di probabilità (PDF).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| PMF Congiunta | $P(x, y)$ | Probabilità congiunta che due variabili discrete assumano rispettivamente i valori $x$ e $y$. |
| Marginalizzazione | $P(x)$ o $P(y)$ | Operazione di somma su una delle variabili della PMF congiunta per ottenere la legge di probabilità della variabile rimanente. |
| Indipendenza | $P(x, y) = P(x)P(y)$ | Condizione in cui la conoscenza di una variabile non fornisce informazioni sull'altra. |
| PMF Condizionale | $P(y|x)$ | Probabilità che $y$ assuma un certo valore dato che $x$ è fissato. |
| Spazio di Stato | $\mathcal{S}$ | Spazio che definisce le caratteristiche di un sistema (es. posizione di un agente mobile).
| Catena di Markov | - | Sequenza di variabili aleatorie in cui lo stato futuro dipende solo dallo stato attuale (indipendenza condizionale). |
| Teorema della Media Condizionale | $E[g(X,Y)] = E_Y[E_X[g(X,Y)|Y]]$ | Metodo per calcolare la media di una funzione di due variabili tramite medie condizionate successive. |
| Distribuzione Poissoniana | $\lambda$ | Distribuzione per eventi rari con media $\lambda$. |
| Distribuzione Binomiale | $B(n, p)$ | Distribuzione del numero di successi in $n$ prove indipendenti con probabilità $p$. |
| Densità di Probabilità | $\rho(x)$ o $f(x)$ | Funzione che descrive la "massa" di probabilità in un intorno di una variabile continua. |
| Insiemi di Borel | $\mathcal{B}(\mathbb{R})$ | Sottoinsieme della $\sigma$-algebra degli aperti della retta reale, necessari per definire misure su spazi continui. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Variabili Discrete e PMF Congiunta
Il docente passa dal concetto di variabile singola alla **variabile della teoria doppia (o n-tupla)**.
- **Concetto di Memoria**: Sebbene sia possibile associare una coppia di variabili discrete a un'unica variabile (memorizzando ogni coppia in una posizione di memoria distinta), è fondamentale distinguere il caso continuo da quello discreto.
- **Omogeneità Dimensionale**: Una coppia $(x, y)$ può non essere dimensionalmente omogenea (es. altezza in cm e peso in kg).
- **Caratterizzazione**: Una coppia di variabili aleatorie è completamente caratterizzata quando la PMF congiunta è assegnata per tutti i valori del **prodotto cartesiano degli alfabeti**.
- **Cardinalità**: Il numero di elementi del prodotto cartesiano è dato dal prodotto delle cardinalità degli alfabeti individuali.
- **Proprietà Fondamentali**:
    - **Normalizzazione**: La somma di tutti i valori della PMF congiunta deve essere uguale a 1 (Assioma di normalizzazione).
    - **Marginalizzazione**: Sommando i valori rispetto a $y$, si ottiene la marginale di $x$ (e viceversa).
    - **Indipendenza**: Due variabili sono indipendenti se e solo se la loro PMF congiunta è il prodotto delle rispettive marginali.
- **Generalizzazione**: Il concetto si estende a n-tuple in uno spazio $\mathbb{R}^n$ o $\mathbb{C}^n$. La probabilità congiunta indica la probabilità dell'intersezione degli eventi.

### 2. Probabilità Condizionale e Filtro Bayesiano
- **Definizione**: La PMF di $y$ dato $x$ è definita quando $y$ varia nel suo alfabeto e $x$ resta fisso.
- **Proprietà**: 
    - $\sum_y P(y|x) = 1$ per ogni $x$ fissato (è una legge di probabilità).
    - $\sum_x P(y|x) \neq 1$ (non è una legge di probabilità poiché si somma sull'evento condizionante).
- **Legge di Bayes**: Relazione fondamentale per conoscere $P(y|x)$ partendo da $P(x|y)$, $P(y)$ e $P(x)$.
- **Applicazioni nei Sistemi Dinamici**:
    - **Spazio di Stato**: Spazio che definisce le caratteristiche di un sistema (es. un missile, un agente mobile).
    - **Filtraggio Predittivo**: Integrazione delle informazioni passate per predire l'evoluzione futura al tempo $t+1$.
    - **Ricorsioni Bayesiane**: Metodo per inseguire la traiettoria di un sistema.
    - **Esempio Mercato Azionario**: Il docente nota che il filtraggio bayesiano ha avuto scarso successo nel mercato azionario a causa degli **eventi imponderabili** (emotivi e non solo fattuali) che rendono difficile la modellazione statistica di eventi che accadono una tantum.
    - **Particle Filters**: Menzionata l'applicazione di filtri statistici particellari nel tracking e nel mondo finanziario.

### 3. Catene di Markov e Complessità Computazionale
- **Indipendenza Condizionale**: $X$ e $Z$ possono essere indipendenti dato $Y$.
- **Esempio della Scacchiera**: La posizione del re dopo due mosse è dipendente dalla posizione iniziale. Tuttavia, data la posizione intermedia, la posizione finale non dipende più da come si è arrivati a quella posizione intermedia.
- **Catena di Markov**: Quando $P(x|y,z) = P(x|y)$, le variabili formano una catena di Markov.
- **Importanza Computazionale**: 
    - La massimizzazione di un funzionale su un insieme discreto senza vincoli è di **complessità esponenziale** ($x^n$).
    - Se un oggetto è schematizzabile come Catena di Markov, i problemi di ricerca di massimo/minimo possono essere ridotti a percorsi su tralicci di stato e risolti con la **programmazione dinamica**, riducendo la complessità da esponenziale ad **algebrica**.

### 4. Teorema della Media Condizionale
- **Generalizzazione**: $E[g(x,y)] = \sum_x \sum_y g(x,y) P(x,y)$.
- **Scomposizione**: Sostituendo $P(x,y) = P(x|y)P(y)$, la sommatoria interna rispetto a $x$ diventa la media di $g(x,y)$ dato $y$.
- **Formulazione**: $E[g(x,y)] = E_y[E_x[g(x,y)|y]]$.
- **Linearità**: La media è un operatore lineare. $E[af(x) + bg(y)] = aE[f(x)] + bE[g(y)]$.

### 5. Introduzione alle Variabili Continue
- **Contiui vs Discreti**: La distinzione tra razionali (numerabili) e reali (continui).
- **Eventi Elementari**: Nelle variabili continue, la probabilità che $x$ sia esattamente uguale a un valore $x_0$ è **zero**. L'evento elementare è l'appartenenza a un intorno (intervallo) $\Delta x$.
- **Insiemi di Borel**: Gli aperti di $\mathbb{R}$ che permettono di definire la misura di probabilità.
- **Densità di Probabilità (PDF)**:
    - Definita come il limite della misura di probabilità del segmento diviso per la sua ampiezza: $\rho(x) = \lim_{\Delta x \to 0} \frac{P(x \in [x - \frac{\Delta x}{2}, x + \frac{\Delta x}{2}])}{\Delta x}$.
    - **Analogia con la Fisica**: La densità di probabilità è simile alla densità di massa. Un segmento può avere la stessa lunghezza (misura ordinaria), ma masse (probabilità) differenti a seconda della densità del materiale (probabilità concentrata o distribuita).
- **Valore Modale**: Il punto di massima densità $\rho(x)$. Il docente avverte che il valore della densità in un punto **non è la probabilità** (che rimane zero), ma indica dove la probabilità è più concentrata.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio: Analisi della Coda di Pacchetti del Router
**Testo**: Un router ha una coda di pacchetti che segue una distribuzione Poissoniana di parametro $\lambda$. Una frazione $p$ dei pacchetti è in errore. Caratterizzare il numero di pacchetti in errore ($M$).

**Risoluzione Passo-Passo**:
1. **Identificazione delle Variabili**:
   - $N$: numero totale di pacchetti in coda $\sim \text{Poisson}(\lambda)$.
   - $M$: numero di pacchetti in errore (variabile di interesse).
   - $p$: probabilità che un singolo pacchetto sia in errore.
2. **Relazione Condizionale**: 
   - Dato $N=n$, il numero di pacchetti in errore $M$ segue una distribuzione **Binomiale**:
     $$P(M=m | N=n) = \binom{n}{m} p^m (1-p)^{n-m}$$
     *Vincolo*: $m \le n$.
3. **Applicazione della Legge della Probabilità Totale**:
   - Per trovare la PMF di $M$, si somma la probabilità condizionata pesata per la marginale di $N$:
     $$P(M=m) = \sum_{n=m}^{\infty} P(M=m | N=n) P(N=n)$$
4. **Sostituzione delle Formule**:
   $$P(M=m) = \sum_{n=m}^{\infty} \left[ \frac{n!}{m!(n-m)!} p^m (1-p)^{n-m} \right] \cdot \left[ \frac{\lambda^n e^{-\lambda}}{n!} \right]$$
5. **Semplificazioni del Docente**:
   - Il termine $n!$ si cancella tra il binomiale e la Poissoniana.
   - Si porta fuori dai simboli della sommatoria tutto ciò che non dipende da $n$:
     $$P(M=m) = \frac{p^m e^{-\lambda}}{m!} \sum_{n=m}^{\infty} \frac{\lambda^n (1-p)^{n-m}}{(n-m)!}$$
   - Sostituzione variabile: $L = n - m \implies n = L + m$.
   - Sostituzione nella sommatoria:
     $$P(M=m) = \frac{p^m e^{-\lambda}}{m!} \sum_{L=0}^{\infty} \frac{\lambda^{L+m} (1-p)^{L}}{L!} = \frac{p^m e^{-\lambda} \lambda^m}{m!} \sum_{L=0}^{\infty} \frac{[\lambda(1-p)]^L}{L!}$$
6. **Riconoscimento della Serie**:
   - La sommatoria $\sum_{L=0}^{\infty} \frac{[\lambda(1-p)]^L}{L!}$ è ilлово sviluppo della funzione esponenziale $e^{\lambda(1-p)}$.
7. **Risultato Finale**:
   $$P(M=m) = \frac{(\lambda p)^m e^{-\lambda} e^{\lambda(1-p)}}{m!} = \frac{(\lambda p)^m e^{-\lambda p}}{m!}$$
   - Il numero di pacchetti in errore $M$ segue una **distribuzione Poissoniana di media $\lambda p$**.

**Concetti Applicati**: Legge della probabilità totale, Media condizionale, Distribuzioni Poissoniana e Binomiale, Semplificazione di serie.
**Semplificazioni/Trucchi**: Il docente utilizza il concetto di *"Reduzio ad unum"* (riduzione all'unità) per riportare il problema complesso alla proprietà fondamentale della Poissoniana.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * **Densità vs Probabilità**: Gli studenti spesso confondono il valore della densità $\rho(x)$ con la probabilità. Il docente ribadisce: in una variabile continua, la probabilità di un punto singolo è sempre zero; la densità indica solo la "concentrazione" della probabilità.
    * **Covarianza vs Indipendenza**: Una covarianza nulla non implica necessariamente indipendenza (eccetto nel caso Gaussiano).
- **Chiarimenti Metodologici**:
    * **Toy Model**: Non cercare di modellare sistemi complessi in un unico colpo; partire da modelli semplici e complicarli progressivamente.
    * **Linearità**: L'operatore di speranza è lineare, il che facilita enormemente il calcolo delle medie di combinazioni lineari di variabili aleatorie.
- **Punti Critici per l'Esame**:
    * Capacità di scomporre problemi complessi in sottoproblemi più semplici tramite condizionamento.
    * Comprensione della differenza tra cardinalità (discreto) e misura/massa (continuo).

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    * **Analisi Matematica**: Richiesta per la comprensione delle funzioni di due variabili e dei limiti.
    * **Algebra Vettoriale**: Fondamentale per la comprensione delle matrici di covarianza e degli autovettori.
    * **Fisica 1**: Il docente suggerisce di usare le intuizioni sulla densità di massa per comprendere la densità di probabilità.
- **Consigli di Studio Espliciti**:
    * "Non voglio sentire memoria ma logica": Concentrarsi sul perché una formula funziona (es. perché la Poissoniana mantiene la sua forma moltiplicando $\lambda$ per $p$).
    * Metodologia "Reduzio ad unum": Cercare sempre di ricondurre le operazioni a principi fondamentali.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Slide del Corso**: Utilizzate dal docente per approfondire le derivazioni analitiche e i dettagli formali delle distribuzioni.
- **Teoria dell'Informazione**: Citata per i test di indipendenza (Distanza di Kullback-Leibler).