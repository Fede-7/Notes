# SBOBINA - [NOME CORSO NON SPECIFICATO] | LEZIONE SULLA CDF, PDF E STATISTICA CONTINUA

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Da specificare]
- **Docente**: [Nome del docente]
- **Orari e Aule**: Prossima lezione: Martedì; Recuperi: Lunedì mattina alle 09:00.
- **Organizzazione Didattica**:
    - **Contesto**: Il docente sta preparando gli studenti per la "magistrale" (tesi di laurea magistrale), con l'obiettivo di metterli in condizione di poter scegliere e affrontare il progetto di ricerca.
- **Ricevimento e Supporto**: Recuperi previsti per lunedì mattina alle 09:00.
- **Avvisi, Calendario e Assenze**:
    - **Consigli pratici del docente**: 
        - Il docente sottolinea che, in informatica, la sommabilità e le metodologie statistiche sono un **mezzo e non un fine**.
        - Non è necessario perdersi in astrazioni matematiche eccessive (es. integrazione di Lebesgue) se non strettamente necessario per la comprensione del modello.
- **Accesso ai Materiali**: Informazione non menzionata nella lezione.

---

## 🎯 SOMMARIO RAPIDO
- **Caratterizzazione delle Variabili Aleatorie**: Studio della CDF (Cumulativa) e della PDF (Densità) come strumenti equivalenti.
- **Proprietà e Relazioni**: Dimostrazione della monotonicità della CDF e sua relazione differenziale con la PDF.
- **Quantizzazione e Teoria dell'Informazione**: Introduzione al passaggio dal continuo al digitale tramite il concetto di quantizzazione e i teoremi di Shannon.
- **Distribuzioni Notevoli**: Studio approfondito delle distribuzioni Uniforme, Esponenziale e di Laplace (PDF, CDF e Medie).
- **Densità Condizionate**: Definizione formale e applicazione pratica (es. filtraggio segnali radar).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| CDF | $F_X(x)$ | **Cumulative Distribution Function**: Probabilità che la variabile $X$ assuma un valore minore o uguale a $x$. |
| PDF | $f(x)$ | **Probability Density Factor/Function**: Derivata della CDF; rappresenta la densità di probabilità. |
| PMF | $P(X=x)$ | **Probability Mass Function**: Utilizzata per variabili discrete (probabilità puntuale). |
| Supporto | $supp(f)$ | Insieme dei punti in cui la funzione di densità è diversa da zero (define l'alfabeto della variabile). |
| Quantizzazione | - | Processo di conversione da ampiezza continua a ampiezza discreta. |
| Campionamento | - | Conversione da tempo continuo a tempo discreto.
| Sigmoidale | - | Andamento "a S" tipico delle CDF di variabili con benefici epigenetici (es. Laplace). |
| Variabile di Laplace | $X \sim \text{Laplace}(\lambda)$ | Variabile continua con densità simmetrica, caratterizzata dal parametro $\lambda$. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Distribuzione Cumulativa (CDF)
- **Spiegazione Teorica**: Una variabile aleatoria (sia continua che discreta) può essere caratterizzata dalla sua **CDF**, definita come una funzione $F_X: \mathbb{R} \to [0, 1]$.
- **Definizione Formale**:
  $$F_X(x) = P(X \le x)$$
- **Proprietà Fondamentali**:
    1. **Limiti**: $F_X(-\infty) = 0$ e $F_X(+\infty) = 1$. 
       *Motivazione*: Per asse di non-negatività, la probabilità che una variabile sia minore di un minimo assoluto è 0; la probabilità che sia minore di un massimo assoluto è 1.
    2. **Monotonicità**: Se $x_2 > x_1$, allora $F_X(x_2) \ge F_X(x_1)$.
       *Dimostrazione*: $P(X \le x_2) = P(X \le x_1) + P(x_1 < X \le x_2)$. Poiché la probabilità dell'evento $(x_1, x_2]$ è non negativa, ne consegue che $F_X(x_2)$ è maggiore o uguale a $F_X(x_1)$.
    3. **Relazione con la PDF**: Per una variabile continua, la CDF è l'integrale della densità:
       $$F_X(x) = \int_{-\infty}^{x} f(t) dt$$
       Di conseguenza, la densità è la derivata della CDF: $f(x) = \frac{d}{dx} F_X(x)$.
- **Condizioni sulla PDF**: La densità deve essere **non negativa** e **integrabile** su $\mathbb{R}$. Se $F$ è monotona crescente, la sua derivata $f$ deve essere $\ge 0$. La CDF è inoltre **continua a destra**.

### 2. Esempi di Caratterizzazione
- *Esempio Variabile Binaria (Discreta)*: 
  $X \in \{0, 1\}$ con $P(X=1) = p$ e $P(X=0) = 1-p$.
  - $x < 0 \implies F_X(x) = 0$
  - $0 \le x < 1 \implies F_X(x) = 1-p$
  - $x \ge 1 \implies F_X(x) = 1$
  *Osservazione*: La CDF è una funzione a scalini; l'entità dei salti corrisponde esattamente ai valori della PMF.

- *Esempio Variabile Uniforme $U(a, b)$*:
  - **PDF**: $f(x) = \frac{1}{b-a}$ per $x \in [a, b]$, altrimenti 0.
  - **Proprietà**: Integrabile perché l'area del rettangolo è $(b-a) \cdot \frac{1}{b-a} = 1$.
  - **CDF Derivazione**:
    1. Per $x < a$: $F_X(x) = 0$.
    2. Per $a \le x \le b$: $F_X(x) = \int_{a}^{x} \frac{1}{b-a} dt = \frac{x-a}{b-a}$.
    3. Per $x > b$: $F_X(x) = 1$.
  *Geometria*: La CDF è una rampa lineare che parte da $a$ (dove $F=0$) e arriva a $b$ (dove $F=1$).

### 3. Media Statistica e Quantizzazione
- **Transizione Discreto $\rightarrow$ Continuo**: 
  - Discreto: $\mathbb{E}[X] = \sum x_i P(X=x_i)$
  - Continuo: $\mathbb{E}[X] = \int x f(x) dx$
- **Concetto di Quantizzazione**: Le variabili continue sono scomode nel mondo digitale (richiederebbero infiniti bit). Il digitale approssima il continuo tramite:
    1. **Campionamento**: Conversione da tempo continuo a discreto.
    2. **Quantizzazione**: Conversione da ampiezza continua a discreta.
- **Teoria dell'Informazione (Shannon, 1948)**: Shannon dimostrò che il mondo analogico è rappresentabile mediante stringhe binarie con un criterio di fedeltà. Introduse il concetto di entropia e il limite del rate:
  $$R = W \log_2(1 + \text{SNR})$$
  *(Dove $R$ è il rate, $W$ la banda, SNR il rapporto segnale/rumore).*
- **Quantizzazione Vettoriale**: Piuttosto che quantizzare elemento per elemento (subottimo), si quantizzano grossi blocchi di dati in $\mathbb{R}^n$ come un unico vettore.

### 4. Distribuzioni Notevoli (Esponenziale e Laplace)
#### Variabile Esponenziale ($\lambda$)
- **PDF**: $f(x) = \lambda e^{-\lambda x}$ per $x \ge 0$.
- **CDF**: $F_X(x) = 1 - e^{-\lambda x}$ per $x \ge 0$.
- **Media Statistica**:
  $$\mathbb{E}[X] = \int_{0}^{\infty} x \lambda e^{-\lambda x} dx = \frac{1}{\lambda}$$
  *(Utilizzando l'integrale notevole $\int_0^\infty x^n e^{-ax} dx = \frac{n!}{a^{n+1}}$ con $n=1$ e $a=\lambda$)*.
- **Analisi Parametrica**: Se $\lambda$ aumenta, la PDF parte da un valore più alto e decade più rapidamente; se $\lambda$ diminuisce, parte da un valore più basso e decade più lentamente.

#### Variabile di Laplace ($\lambda$)
- **PDF**: $f(x) = \frac{\lambda}{2} e^{-\lambda |x|}$ per $x \in \mathbb{R}$.
- **Caratteristiche**: Funzione pari (simmetrica rispetto all'origine).
- **CDF**:
    1. Per $x \le 0$: $F_X(x) = \frac{1}{2} e^{\lambda x}$.
    2. Per $x > 0$: $F_X(x) = 1 - \frac{1}{2} e^{-\lambda x}$.
- **Andamento**: La CDF ha un andamento **sigmoidale** (a "S").

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Calcolo della Media della Variabile Uniforme
- **Testo**: Determinare la media di una variabile uniforme in $[a, b]$.
- **Risoluzione Passo-Passo**:
  1. Identificare la PDF: $f(x) = \frac{1}{b-a}$.
  2. Impostare l'integrale: $\mathbb{E}[X] = \int_{a}^{b} x \frac{1}{b-a} dx$.
  3. Risoluzione: $\frac{1}{b-a} [\frac{x^2}{2}]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b-a)(b+a)}{2(b-a)} = \frac{a+b}{2}$.
- **Risultato**: La media coincide con la media aritmetica degli estremi.

### Esercizio 2: Calcolo della Media della Variabile Esponenziale
- **Testo**: Calcolare il valore atteso della variabile esponenziale di parametro $\lambda$.
- **Risoluzione Passo-Passo**:
  1. PDF: $f(x) = \lambda e^{-\lambda x}$.
  2. Integrale: $\int_{0}^{\infty} x \lambda e^{-\lambda x} dx$.
  3. Applicazione formula integrale notevole ($n=1$): $\lambda \cdot \frac{1!}{\lambda^2} = \frac{1}{\lambda}$.
- **Concetti Applicati**: Integrazione per parti o formule di integrali notevoli.

### Esercizio 3: Densità Condizionata (Esempio Radar)
- **Testo**: Determinare la densità di $X$ dato che l'evento $A = \{X \in [-1, 2]\}$ si verifica, per una variabile di Laplace.
- **Risoluzione Passo-Passo**:
  1. Calcolare $P(A)$: $P(A) = F_X(2) - F_X(-1) = (1 - \frac{1}{2}e^{-2\lambda}) - (\frac{1}{2}e^{-\lambda})$.
  2. Definire la densità condizionata $f(x|A)$:
     $$f(x|A) = \frac{f(x) \cdot \mathbb{I}_{x \in [-1, 2]}}{P(A)}$$
  3. Interpretazione: Si eliminano gli "outliers" (valori fuori dall'intervallo) e si normalizza la densità sulla probabilità dell'evento $A$.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
  * **PDF $\neq$ Probabilità**: La densità di probabilità non è una probabilità. La probabilità è l'area sotto la curva (l'integrale), mentre la PDF può assumere valori $> 1$ (es. $\lambda=2$ nell'esponenziale).
  * **Differenza tra PMF e PDF**: Sebbene entrambe siano "densità", la PMF è per variabili discrete (conteggio di punti) e la PDF per variabili continue (misura del segmento).
- **Chiarimenti Metodologici**:
  * **Sommabilità come mezzo**: Il docente ammonisce gli studenti a non fossilizzarsi sulla teoria della sommabilità (es. Riemann vs Lebesgue) ma a focalizzarsi sull'uso delle metodologie statistiche come strumenti per risolvere problemi di ingegneria/informatica.
  * **Relazione CDF/PDF**: È sempre più semplice ragionare con la CDF (che è una probabilità) e derivare la PDF, oppure viceversa a seconda del comfort del problema.
- **Punti Critici per l'Esame**:
  * Conoscere le forme grafiche delle CDF (sigmoidali per le distribuzioni continue).
  * Comprendere il processo di quantizzazione (campionamento + quantizzazione ampiezza) come ponte tra mondo analogico e digitale.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**: 
  * Richiede una buona base di analisi matematica (integrali, derivate, monotonicità).
  * Il docente suggerisce che la comprensione del concetto di "supporto" è fondamentale.
- **Consigli di Studio Espliciti**:
  * Non ripetere a pappagallo le formule; comprendere la logica dietro la derivazione delle medie e delle CDF.
  * Studiare le distribuzioni note (Uniforme, Esponenziale, Laplace) non solo come formule, ma analizzando come variano con i parametri (es. l'effetto di $\lambda$).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Shannon, C. E. (1948)**: *"The Mathematical Theory of Communication"* (Bell Lab Technical Journals). Fondamentale per la teoria dell'informazione e la digitalizzazione universale.
- **Note del docente**: Il docente ha citato l'uso di funzioni euleriane per integrali notevoli, ma ha sottolineato che per il corso di Informatica la sommabilità di Riemann è generalmente sufficiente.