# SBOBINA - Teoria della Probabilità | Lezione su Variabili Continue, Convoluzione e Quantizzazione

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Teoria della Probabilità (Ingegneria/Informatica)
- **Docente**: Non specificato nella trascrizione
- **Orari e Aule**: Prossima lezione: **Lunedì ore 09:00**.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con sessione di esercizi.
    - **Materiali**: Gli esercizi saranno caricati sul canale **Teams** nel weekend (sabato o domenica) per il download degli studenti.
- **Ricevimento e Supporto**:
    - Canale principale di comunicazione: **Teams**.
- **Avvisi, Calendario e Assenze**:
    - Lezioni successive dedicate principalmente alla risoluzione di esercizi.
- **Accesso ai Materiali**:
    - Slide e PDF degli esercizi disponibili su Teams.

---

## 🎯 SOMMARIO RAPIDO
- Estensione delle disuguaglianze di Markov e Chebyshev alle variabili continue.
- Caratterizzazione statistica delle variabili tramite la coppia (Media, Varianza) e applicazioni alla quantizzazione.
- Studio della densità di probabilità (PDF) di variabili congiunte e condizionate (approccio limite).
- Derivazione della PDF della somma di variabili indipendenti tramite l'operazione di convoluzione.
- Introduzione al Teorema Centrale del Limite e ai sistemi lineari tempo-invarianti (LTI).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Varianza | $\text{Var}(X)$ o $\sigma^2$ | Misura della dispersione dei dati attorno alla media. |
| Momento di ordine $m$ | $E[X^m]$ | Il valore atteso della variabile elevata alla potenza $m$. |
| PDF | $f_X(x)$ | Densità di Probabilità; funzione che caratterizza la distribuzione di una variabile continua. |
| CDF | $F_X(x)$ | Funzione di Distribuzione Cumulativa; $P(X \le x)$. |
| Supporto | $\text{supp}(f_X)$ | L'insieme dei valori per cui la PDF è diversa da zero. |
| Quantizzazione | $\Delta$ | Ampiezza dell'intervallo di quantizzazione (errore di rappresentazione). |
| Convoluzione | $f_Z = f_X \ast f_Y$ | Operazione matematica per determinare la PDF della somma di due variabili indipendenti. |
| Sistema Tempo-Invariante | LTI | Sistema in cui la risposta non dipende dal momento temporale del sollecito, ma solo dalla forma del sollecito. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Revisione e Disuguaglianze (Caso Continuo)
- **Spiegazione Teorica**: Il docente ripercorre la proprietà della varianza: $\text{Var}(ax+b) = a^2 \text{Var}(X)$. Si sottolinea che tale proprietà è valida anche per variabili continue.
- **Disuguaglianza di Markov**: Viene dimostrato che la disuguaglianza di Markov può essere estesa al caso continuo.
- **Condizioni Tacite e Prerequisiti**: Si assume che la variabile $X$ sia **non negativa**.
- **Formule e Modelli Matematici**:
  Per una variabile non negativa $X$ e $\delta > 0$:
  $$P(X \ge \delta) \le \frac{E[X^m]}{\delta^m}$$
  *Derivazione del docente:*
  1. Il docente parte dall'integrale della probabilità nel caso continuo: $P(X \ge \delta) = \int_\delta^\infty f_X(x) dx$.
  2. Utilizza il fatto che se $X$ è non negativa, l'integrando è maggiore o uguale di $\frac{x}{\delta^m} f_X(x)$ (per $x \ge \delta$).
  3. Aggiungendo l'intervallo $[0, \delta]$ all'integrale, si ottiene il limite superiore: $\int_0^\infty \frac{x}{\delta^m} f_X(x) dx$.
  4. Poiché l'intervallo coincide con il supporto di $X$, l'integrale risulta uguale a $\frac{E[X^m]}{\delta^m}$.
- **Disuguaglianza di Chebyshev**: Se $\delta = k\sigma_Y$ (dove $\sigma_Y$ è la deviazione standard), la probabilità che gli scostamenti dalla media superino $k$ deviazioni standard è:
  $$P(|Y - \mu| \ge k\sigma_Y) \le \frac{1}{k^2}$$
  *Nota del docente:* La coppia $(\mu, \sigma)$ fornisce una caratterizzazione globale della variabile aleatoria, anche se il "optimum" sarebbe la conoscenza della PDF completa.

### 2. Variabili Uniformi e Teoria della Quantizzazione
- **Momenti della Uniforme**: Per una variabile $X \sim \mathcal{U}(A, B)$:
    - Media: $E[X] = \frac{A+B}{2}$ (punto medio).
    - Varianza: $\text{Var}(X) = \frac{(B-A)^2}{12}$.
- **Applicazione Pratica (Quantizzazione)**:
    - Il valore quadratico medio della distorsione in un quantizzatore uniforme è pari a $\frac{\Delta^2}{12}$, dove $\Delta = B-A$ è l'ampiezza dell'intervallo di quantizzazione.
- **Quantizzazione Uniforme vs Adattativa**:
    - *Uniforme:* Usata quando non si ha conoscenza a priori della distribuzione dei dati (si assume che siano uniformi).
    - *Adattativa (Q-learning):* Se si hanno informazioni a priori, è logico quantizzare più finemente gli intervalli con alta probabilità e meno finemente quelli con bassa probabilità.
- **Quantizzatore Vettoriale**: Invece di quantizzare elemento per elemento, si quantizza un blocco di $n$ dati. Questo approccio è "ottimo" e simile alla compressione moderna.

### 3. Distribuzioni Specifiche e Supporto
- **Distribuzione di Cauchy**: Caratterizzata da una varianza infinita.
- **Contesto Fisico**: Modella il rumore atmosferico (impulsi causati da fulmini) che distrugge il segnale con "potenza infinita".
- **Supporto**: Definizione formale dell'alfabeto come l'insieme dei valori in cui la PDF è diversa da zero.

### 4. Variabili Congiunte e Condizionate
- **Densità di Probabilità Congiunta (Limite)**:
  La densità $f_{XY}(x,y)$ è definita come il limite del rapporto tra la probabilità congiunta e la misura ordinaria:
  $$f_{XY}(x,y) = \lim_{\Delta x, \Delta y \to 0} \frac{P(x \in \Delta x, y \in \Delta y)}{\Delta x \Delta y}$$
- **Indipendenza**: Due variabili $X$ e $Y$ sono indipendenti se e solo se la PDF congiunta è il prodotto delle marginali:
  $$f_{XY}(x,y) = f_X(x) \cdot f_Y(y)$$
- **Densità Condizionale (Il Problema della Probabilità Nulla)**:
  - Nel caso discreto $f_{X|Y} = f_{XY} / f_Y$ è ben definito.
  - Nel caso continuo, l'evento $Y=y$ ha probabilità nulla ($0/0$).
  - **Risoluzione del Docente**: Si definisce tramite un artificio limite:
    $$f_{X|Y}(x|y) = \lim_{\Delta y \to 0} \frac{f_{XY}(x, y)}{f_Y(y)}$$
    Questo permette di definire la densità condizionale nonostante il condizionamento sia su un evento a probabilità nulla.

### 5. Convoluzione e Teorema Centrale del Limite
- **Somma di Variabili Indipendenti**: Se $Z = X + Y$, la PDF di $Z$ si ottiene tramite l'integrale:
  $$f_Z(z) = \int_{-\infty}^{\infty} f_X(z-y) f_Y(y) dy$$
- **Proprietà della Convoluzione**:
    - Commutativa: $f_X \ast f_Y = f_Y \ast f_X$.
    - Distributiva e Associativa.
- **Sistemi LTI (Lineari Tempo-Invarianti)**: La convoluzione regola la relazione ingresso-uscita di tutti i sistemi LTI.
    - *Linearità:* Risposta alla somma delle sollecitazioni è la somma delle risposte.
    - *Tempo-Invarianza:* L'ordine delle operazioni non cambia il risultato (esempio del docente sulla porta aperta: se prima si corre e poi si apre, il risultato è diverso rispetto a se prima si apre e poi si corre).
- **Teorema Centrale del Limite (TCL)**:
  La sovrapposizione di un gran numero di fenomeni elementari indipendenti e con uguale peso risulta in un fenomeno **Gaussiano**. Questo spiega l'uso (e l'abuso) della normale nella teoria degli errori.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Calcolo di Media e CDF per una PDF mista (Rettangolo e Triangolo)
- **Testo**: Data una PDF definita da un rettangolo e un triangolo (descritta graficamente dal docente).
- **Risoluzione Passo-Passo**:
  1. **Verifica della PDF**: L'area del rettangolo è $\frac{1}{2}$ (base 2, altezza 1/4). L'area del triangolo è $\frac{1}{2}$ (base 2, altezza 1/2). La somma delle aree è 1, quindi è una PDF valida.
  2. **Supporto**: L'alfabeto è $x \in [-3, -1] \cup [1, 3]$.
  3. **Forma Analitica**: Il docente identifica la parte triangolare come una traslazione e scalatura di una funzione $g(x) = 1 - |x|$, identificandola come $g(x-2)$.
  4. **Calcolo della CDF ($F_X(x)$)**:
     - Per $x < -3$: $F_X(x) = 0$.
     - Per $x \in [-3, -1]$: Integrale di $1/4 \implies F_X(x) = \frac{x+3}{4}$.
     - Per $x \in [-1, 1]$: Poiché $f_X(x)=0$, la CDF resta costante a $F_X(-1) = 0.5$.
     - Per $x \in [1, 3]$: $F_X(x) = 0.5 + \int_1^x \frac{t-1}{2} dt$. Risulta una funzione quadratica concava verso l'alto.
  5. **Calcolo della Media ($E[X]$)**:
     - **Metodo Pedisseco**: Calcolo diretto dell'integrale $\int t f_X(t) dt$ su tutti gli intervalli del supporto.
     - **Metodo "Smart" (Simmetria/Condizionalità)**:
       - Si nota che la variabile è divisa in due parti uguali (negativa e positiva).
       - Condizionando su $X \le 0$: la distribuzione è uniforme tra -3 e -1 $\implies$ media $-2$.
       - Condizionando su $X > 0$: la distribuzione è simmetrica rispetto a $2 \implies$ media $2$.
       - Media finale: $\frac{1}{2}(-2) + \frac{1}{2}(2) = 0$.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
  * Non confondere la varianza nel caso continuo con la somma discreta; nel continuo si passa sempre all'integrale.
  * Attenzione al calcolo della densità condiziona: ricordare che nel continuo il condizionamento è su un evento a probabilità nulla e richiede ilgebrio di limite.
- **Chiarimenti Metodologici**:
  * Il docente sottolinea che la convoluzione è l'operazione fondamentale per la statistica delle somme e per l'ingegneria dei sistemi LTI.
  * "Sapere di non sapere" è il punto di partenza del processo di apprendimento (citazione socratica).
- **Punti Critici per l'Esame**:
  * Prepararsi un **formulario sintetico** personale con tutte le formule rilevanti (non affidarsi solo ai libri durante la prova).
  * Capire la distinzione tra "misura di probabilità" (integrale/somma) e "misura ordinaria" (area/lunghezza) per definire la densità.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Non specificata (ma indicata la possibilità di consultare un formulario personale).
- **Consigli di Studio Espliciti**:
  * Preparare un formulario sintetico con i concetti più rilevanti.
  * Non limitarsi alla memorizzazione delle formule, ma comprendere la logica dei limiti (specialmente per le PDF condizionate).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Materiale didattico**: Esercizi caricati sul canale Teams del corso (disponibili dal sabato/domenica).
- **Riferimenti teorici**: Teorema Centrale del Limite, Teorema della Media Condizionata, Legge di Bayes (tutte estese dal caso discreto al continuo).