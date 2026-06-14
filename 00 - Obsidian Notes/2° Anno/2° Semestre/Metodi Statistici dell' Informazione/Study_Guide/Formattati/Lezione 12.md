# SBOBINA - PROBABILITÀ E STATISTICA | 20 Aprile 2025

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Probabilità e Statistica (Ingegneria/Matematica)
- **Docente**: [Nome non specificato nella trascrizione]
- **Orari e Aule**: Prossima lezione domani alle ore 14:00 in Aula B06.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con sessioni di esercizi.
    - **Ricevimento e Supporto**: Disponibile tramite Microsoft Teams (cartella "esercizi").
- **Avvisi, Calendario e Assenze**:
    - Data della lezione aggiornata al 20 Aprile 2025.
- **Consigli pratici del docente**:
    - Il docente sottolinea esplicitamente di **non voler apprendere a memoria**, ma di comprendere la **logica** sottostante ai passaggi matematici.
- **Accesso ai Materiali**:
    - Materiali (esercizi) disponibili nella cartella specifica su Teams.

---

## 🎯 SOMMARIO RAPIDO
1. **Esercitazione su Trasformazioni e Distribuzioni**: Analisi di variabili esponenziali, trasformazioni logaritmiche (Gumbel), quantizzazione a bit e calcolo di PDF/CDF.
2. **Analisi di PDF Complesse e Condizionate**: Calcolo di costanti di normalizzazione, medie, varianze e probabilità condizionate con approcci analitici.
3. **Funzione Generatrice dei Momenti (MGF)**: Definizione teorica, proprietà per variabili indipendenti e legame con lo sviluppo di Taylor.
4. **Teorema Centrale del Limite (CLT)**: Dimostrazione del limite della somma di variabili i.i.d. attraverso l'uso delle MGF.
5. **Distribuzione Gaussiana (Normale)**: Caratterizzazione della $\mathcal{N}(\mu, \sigma^2)$, funzione speciale $Q(x)$ e proprietà geometriche/analitiche.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Funzione Densità di Probabilità | $f_X(x)$ | Definisce la densità di probabilità di una variabile aleatoria continua. |
| Funzione di Distribuzione Cumulativa | $F_X(x)$ | Indica la probabilità che la variabile sia minore o uguale a $x$, $F_X(x) = P(X \le x)$. |
| Media Statistica | $\mathbb{E}[X]$ o $\mu$ | Valore atteso della variabile aleatoria. |
| Varianza | $\sigma^2$ o $\mathbb{E}[(X-\mu)^2]$ | Misura della dispersione dei dati attorno alla media. |
| ValoreআরQuadratico Medio | $\mathbb{E}[X^2]$ | Momento di ordine 2. |
| Funzione Generatrice dei Momenti | $M_X(s)$ | Funzione definita come $\mathbb{E}[e^{sX}]$, usata per estrarre i momenti tramite derivate. |
| Quantizzazione a un bit | $\text{sign}(Y)$ | Operazione di conversione analogico-digitale che estrae solo il segno di una variabile. |
| Funzione Speciale $Q$ | $Q(x)$ | Complementary CDF della normale standard; $Q(x) = P(X_0 > x)$. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Trasformazioni e Distribuzioni Specifiche (Gumbel e Signum)
- **Spiegazione Teorica**: Il docente analizza come una variabile aleatoria soggetta a una trasformazione cambi la sua distribuzione. Viene evidenziato il passaggio da una distribuzione continua a una discreta tramite quantizzazione.
- **Condizioni Tacite e Prerequisiti**: Si assume che la variabile iniziale sia definita su un intervallo tale da rendere la trasformazione ben definita.
- **Esempi Specifici Citati**:
  - *Esempio 1 (Trasformazione Logaritmica)*: 
    - Si considera $X \sim \text{Esponenziale}$ con $\mathbb{E}[X] = 1$. Poiché $\mathbb{E}[X] = 1/\lambda$, ne consegue che $\lambda = 1$.
    - PDF di $X$: $f_X(x) = e^{-x} \mathbb{1}_{x \ge 0}$.
    - Trasformazione: $Y = \ln(X)$.
    - Alfabeto di $Y$: $(-\infty, +\infty)$ poiché $\ln(0) \to -\infty$ e $\ln(\infty) \to \infty$.
    - Calcolo di $F_Y(y)$:
      $$F_Y(y) = P(Y \le y) = P(\ln(X) \le y) = P(X \le e^y)$$
      Poiché $X$ è esponenziale con $\lambda=1$, $F_X(x) = 1 - e^{-x}$.
      $$F_Y(y) = 1 - e^{-e^y}$$
    - Calcolo di $f_Y(y)$ per derivazione:
      $$f_Y(y) = \frac{d}{dy}(1 - e^{-e^y}) = e^y \cdot e^{-e^y}$$
      *Nota del docente*: Questa è la **densità di Gumbel**, utilizzata per modellare eventi rari.
  - *Esempio 2 (Quantizzazione a un bit)*:
    - Si considera $Z = \text{sign}(Y)$. Questa è una conversione analogico-digitale.
    - $Z$ è una variabile discreta binaria con alfabeto $\{-1, 1\}$.
    - $P(Z=1) = P(Y \ge 0) = 1 - F_Y(0) = 1 - (1 - e^{-e^0}) = e^{-1} = 1/e$.
    - $P(Z=-1) = 1 - 1/e$.
    - Media di $Z$: $\mathbb{E}[Z] = 1(1/e) + (-1)(1 - 1/e) = \frac{1}{e} - 1 + \frac{1}{e} = \frac{2}{e} - 1$.
    - Varianza di $Z$: $\sigma^2 = \mathbb{E}[Z^2] - (\mathbb{E}[Z])^2$. Poiché $Z^2 = 1$ sempre, $\mathbb{E}[Z^2] = 1$.
      $$\sigma^2 = 1 - \left(\frac{2}{e} - 1\right)^2 = 1 - \left(\frac{4}{e^2} - \frac{4}{e} + 1\right) = \frac{4}{e} - \frac{4}{e^2}$$

### 2. Caratterizzazione di PDF e CDF Complesse
- **Spiegazione Teorica**: Analisi di funzioni definite a tratti e calcolo di costanti di normalizzazione attraverso l'integrazione.
- **Esempi Specifici Citati**:
  - *Esempio 2 (Costante di normalizzazione)*: 
    - $f_X(x) = c(x-2)^2 \mathbb{1}_{[0,2]}$.
    - Per trovare $c$, si impone $\int_0^2 c(x-2)^2 dx = 1$. 
    - Sostituendo $t = x-2$, l'integrale diventa $\int_{-2}^0 t^2 dt = [\frac{t^3}{3}]_{-2}^0 = 0 - (-8/3) = 8/3$.
    - Quindi $c \cdot (8/3) = 1 \implies c = 3/8$.
  - *Esempio 3 (PDF Triangolare e Probabilità Condizionata)*:
    - CDF data: $F_X(x) = \frac{x^2}{2}$ per $x \in [0,1]$; $F_X(x) = -\frac{x^2}{2} + 2x - 1$ per $x \in [1,2]$.
    - PDF derivata: $f_X(x) = x$ per $x \in [0,1]$; $f_X(x) = 2-x$ per $x \in [1,2]$.
    - *Interpretazione*: La PDF ha forma triangolare (base 2, altezza 2). Area totale = 1.
    - Probabilità condizionata $P(X < 3/2 | X > 1)$:
      $$P(X < 3/2 | X > 1) = \frac{P(1 < X < 3/2)}{P(X > 1)} = \frac{F_X(3/2) - F_X(1)}{1 - F_X(1)}$$
  - *Esempio 4 (Simmetria e Teoria degli Insiemi)*:
    - Calcolo di $P(X < 0 | |X| > 1)$ per una PDF simmetrica.
    - L'evento $|X| > 1$ è l'unione disgiunta $X > 1 \cup X < -1$.
    - L'intersezione $X < 0 \cap (|X| > 1)$ equivale a $X < -1$.
    - Per simmetria, la probabilità è $1/2$.

### 3. Funzione Generatrice dei Momenti (MGF)
- **Spiegazione Teorica**: La funzione $M_X(s) = \mathbb{E}[e^{sX}]$ permette di estrarre tutti i momenti della variabile aleatoria tramite la derivazione rispetto al parametro $s$ valutata nell'origine ($s=0$).
- **Proprietà Chiave**:
    - **Derivazione**: $M_X^{(r)}(0) = \mathbb{E}[X^r]$ (momento di ordine $r$).
    - **Indipendenza**: Se $X$ e $Y$ sono indipendenti, $M_{X+Y}(s) = M_X(s) \cdot M_Y(s)$.
    - **Sviluppo di Taylor**: Lo sviluppo di Maclaurin della MGF è $\sum_{r=0}^\infty \frac{M_X^{(r)}(0)}{r!} s^r$. I coefficienti sono i momenti.
- **Esempio di Somma Normalizzata**:
    - Se $Z_n = \frac{\sum_{i=1}^n X_i}{\sqrt{n}}$ con $X_i$ i.i.d. a media 0 e varianza $\sigma^2$:
      $$M_{Z_n}(s) = \left[ M_X\left(\frac{s}{\sqrt{n}}\right) \right]^n$$
      Sviluppando per $s \to 0$ (primo termine non costante): $M_{Z_n}(s) \approx \left[ 1 + \frac{s^2 \sigma^2}{2n} \right]^n \to e^{\frac{s^2 \sigma^2}{2}}$ per $n \to \infty$.

### 4. Teorema Centrale del Limite (CLT) e Distribuzione Gaussiana
- **Spiegazione Teorica**: Il CLT stabilisce che la somma di un gran numero di variabili indipendenti e identicamente distribuite (i.i.d.) con varianza finita tende a una distribuzione Gaussiana (Normale), indipendentemente dalla distribuzione originale delle $X_i$.
- **Distribuzione Normale Standard**: $\mathcal{N}(0,1)$ con PDF $f_{X_0}(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$.
- **Distribuzione Normale Generale**: $\mathcal{N}(\mu, \sigma^2)$ con PDF:
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
- **Funzione Speciale $Q(x)$**: Definita come $Q(x) = \int_x^\infty f_{X_0}(t) dt = 1 - F_{X_0}(x)$. Rappresenta la probabilità che una normale standard ecceda il valore $x$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Trasformazione Logaritmica e Variabile Signum
- **Testo**: $X \sim \text{Esponenziale}(\mu=1)$, $Y = \ln(X)$. Determinare PDF, CDF di $Y$. Per $Z = \text{sign}(Y)$, determinare media e varianza.
- **Risoluzione Passo-Passo**:
  1. Determinazione parametro: $\mu = 1/\lambda \implies \lambda = 1$. PDF $f_X(x) = e^{-x}$.
  2. Calcolo CDF di $Y$: $F_Y(y) = P(\ln(X) \le y) = P(X \le e^y) = 1 - e^{-e^y}$.
  3. Calcolo PDF di $Y$: Derivazione di $F_Y(y)$ $\implies f_Y(y) = e^y e^{-e^y}$.
  4. Caratterizzazione di $Z$: $Z$ è discreta. $P(Z=1) = 1 - F_Y(0) = 1/e$. $P(Z=-1) = 1 - 1/e$.
  5. Media: $\mathbb{E}[Z] = 1(1/e) - 1(1 - 1/e) = 2/e - 1$.
  6. Varianza: $\mathbb{E}[Z^2] - \mathbb{E}[Z]^2 = 1 - (2/e - 1)^2 = 4/e - 4/e^2$.
- **Concetti Applicati**: Trasformazione di variabili, densità di Gumbel, variabili discrete.

### Esercizio 2: Normalizzazione e PDF con Supporto Limitato
- **Testo**: $f_X(x) = c(x-2)^2 \mathbb{1}_{[0,2]}$. Determinare $c$, PDF, e probabilità condizionata.
- **Risoluzione Passo-Passo**:
  1. Calcolo $c$: $\int_0^2 c(x-2)^2 dx = 1 \implies c(8/3) = 1 \implies c = 3/8$.
  2. Calcolo CDF: $F_X(x) = \int_0^x \frac{3}{8}(t-2)^2 dt = [\frac{3}{8} \frac{(t-2)^3}{3}]_0^x = \frac{(x-2)^3}{8} - \frac{(-2)^3}{8} = \frac{(x-2)^3 + 8}{8}$.
  3. Calcolo Probabilità Condizionata: $P(X > 1 | X > 0.5) = \frac{P(X > 1)}{P(X > 0.5)} = \frac{1 - F_X(1)}{1 - F_X(0.5)}$.
- **Concetti Applicati**: Integrazione, normalizzazione, probabilità condizionata.

### Esercizio 4: Densità Simmetrica e Teoria degli Insiemi
- **Testo**: Determinare PDF di una CDF complessa e calcolare $P(X < 0 | |X| > 1)$.
- **Risoluzione Passo-Passo**:
  1. Calcolo PDF: Derivazione dei tratti della CDF $\implies f_X(x)$ risulta essere una PDF triangolare simmetrica.
  2. Analisi evento $|X| > 1$: Equivale a $X \in (-\infty, -1) \cup (1, +\infty)$.
  3. Analisi intersezione $X < 0 \cap (|X| > 1)$: L'intersezione con $X < 0$ scarta l'intervallo $(1, +\infty)$, lasciando solo $X \in (-\infty, -1)$.
  4. Risultato: Per simmetria della PDF, $P(X < -1) = P(X > 1)$. Quindi $P(X < 0 | |X| > 1) = \frac{P(X < -1)}{P(X < -1) + P(X > 1)} = 1/2$.
- **Concetti Applicati**: Teoria degli insiemi, simmetria delle distribuzioni, densità condizionate.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * Distinzione tra $\Phi(x)$ (CDF della normale) e $Q(x)$ (Complementary CDF).
    * Confusione tra media e valore quadratico medio in distribuzioni con media nulla (dove coincidono).
- **Chiarimenti Metodologici**:
    * La derivazione sotto il segno di integrale per le MGF è ammessa qui per comodità, ma richiede formalmente la verifica della convergenza equiassoluta.
    * La variabile $Z = \text{sign}(Y)$ trasforma una variabile continua in una discreta; non si possono usare le PDF per calcolare probabilità puntuali su $Z$.
- **Punti Critici per l'Esame**:
    * Comprendere il perché la Gaussiana è così importante: Teorema Centrale del Limite (sovrapposizione di errori indipendenti).
    * Capacità di manipolare gli insiemi per risolvere probabilità condizionate complesse.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    * Cultura matematica solida (integrali, derivate, serie di Taylor).
- **Consigli di Studio Espliciti**:
    * "Non voglio sentire memoria ma logica": È fondamentale saper ricostruire i passaggi logici delle trasformazioni e delle derivazioni delle MGF.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- Informazione non menzionata nella lezione. (Si consiglia di consultare il materiale su Teams fornito dal docente).