# SBOBINA - Teoria della Probabilità | Variabili Continue e Trasformazioni

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato nel testo - Probabilità/Statistica]
- **Docente**: [Non specificato nel testo]
- **Orari e Aule**: [Non specificati]
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con supporto digitale (OneNote, Teams).
    - **Recuperi specifici**: Sessioni di recupero previste per il **20 e il 27** (mesi non specificati).
- **Ricevimento e Supporto**: 
    - Il docente ha segnalato alcuni intoppi tecnici (problemi di finestre aperte e "hard reset" di OneNote), suggerendo di non prendersi cura dei glitch tecnici ma di concentrarsi sulla logica.
- **Consigli pratici del docente**:
    - **Focus sulla logica**: Il docente esorta a non limitarsi alla memorizzazione dei risultati, ma a comprendere la logica sottostante.
    - **Approccio intuitivo**: Per i calcoli complessi, è spesso preferibile "passare dalla CDF" piuttosto che lavorare direttamente sulla PDF, poiché le diseguaglianze sono più semplici da gestire.
- **Accesso ai Materiali**: Citazione dell'uso di OneNote per la didattica.

---

## 🎯 SOMMARIO RAPIDO
- Passaggio dalle variabili discrete alle variabili continue e definizione di PDF e CDF.
- Relazioni differenziali e integrali tra PDF e CDF.
- Caratterizzazione condizionale e Legge della Probabilità Totale per variabili continue.
- Trasformazioni di variabili aleatorie (casi monotoni e non monotoni).
- Metodo di generazione di variabili aleatorie (Metodo di Wiener) e calcolo dei momenti.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **Densità di Probabilità** | $f_X(x)$ | Funzione non negativa, integrabile su $\mathbb{R}$ con integrale unitario. Rappresenta il rapporto tra la probabilità in un intervallo e l'ampiezza dell'intervallo stesso ($\Delta x \to 0$). **Nota**: Non è una probabilità. |
| **CDF (Cumulative Distribution Function)** | $F_X(x)$ | Funzione che associa a ogni valore $\alpha$ la probabilità $P(X \le \alpha)$. |
| **Variabile Aleatoria Continua** | $X$ | Variabile in cui la probabilità che assuma un valore specifico è zero ($P(X=x)=0$). |
| **Variabile Binaria** | $B$ | Variabile che assume valori in un insieme discreto (es. $\{-1, 1\}$). |
| **Trasformazione** | $y = g(x)$ | Funzione che lega una variabile aleatoria $X$ a una nuova variabile $Y$. |
| **Valore Quadratico Medio (RMS)** | $\sqrt{E[X^2]}$ | Radice quadrata del secondo momento. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Variabili Continue: PDF e CDF
- **Spiegazione Teorica**: 
    In una variabile continua, gli eventi elementari sono definiti come l'appartenenza della variabile a un intervallo. Poiché la probabilità di un singolo punto è nulla, si definisce la **densità di probabilità** come il limite del rapporto tra la probabilità in un intervallo $\Delta x$ e l'ampiezza dell'intervallo stesso:
    $$f_X(x) = \lim_{\Delta x \to 0} \frac{P(x \le X \le x + \Delta x)}{\Delta x}$$
    *Analogia*: Il docente paragona la densità di probabilità alla densità di massa: se ci sono due modi di misurare le dimensioni di un oggetto, si può definire la densità di una misura rispetto all'altra (misura standard come lunghezza, area, volume).

- **Proprietà della CDF ($F_X(x)$)**:
    1. **Intervallo**: $0 \le F_X(x) \le 1$ (essendo una probabilità).
    2. **Limiti**: $\lim_{x \to -\infty} F_X(x) = 0$ (evento impossibile); $\lim_{x \to \infty} F_X(x) = 1$ (evento certo).
    3. **Monotonicità**: È sempre monotona crescente (non necessariamente strettamente).
    4. **Continuità**: Continua a destra ($F_X(x) = \lim_{x \to x^+} F_X(x)$).

- **Relazioni Fondamentali**:
    - **Differenziale**: $f_X(x) = \frac{d}{dx} F_X(x)$ (La PDF è la derivata della CDF).
    - **Integrale**: $F_X(x) = \int_{-\infty}^x f_X(t) dt$.
    - **Probabilità in un intervallo**: $P(a \le X \le b) = \int_a^b f_X(x) dx = F_X(b) - F_X(a)$.

### 2. Caratterizzazione Condizionale
- **Definizione**: La densità condizionale può essere definita tramite il limite della probabilità condizionata:
    $$f_{X|A}(x) = \lim_{\Delta x \to 0} \frac{P(x \le X \le x + \Delta x | A)}{\Delta x}$$
    In modo equivalente, la CDF condizionale è $F_{X|A}(x) = P(X \le x | A)$, e la PDF condizionale è la sua derivata totale.
- **Grafici (Esempi citati)**:
    - *Variabile di Laplace*: Il docente mostra due PDF di Laplace (una con $\lambda=0.5$, l'altra con $\lambda=1$). La curva con $\lambda=1$ è più concentrata perché l'esponenziale decade più rapidamente, pur mantenendo l'area unitaria.
    - *PDF Condizionali*: In un intervallo $[ -1, 2 ]$, la PDF condizionale ha supporto limitato a tale intervallo e le curve sono più alte perché l'area deve essere normalizzata a 1.

### 3. Legge della Probabilità Totale e Media Condizionale
- **Legge della Probabilità Totale (LTP)**: 
    Data una partizione dell'evento certo $\{E_m\}$, la CDF e la PDF di $X$ sono:
    $$F_X(x) = \sum_m F_{X|E_m}(x) \cdot P(E_m)$$
    $$f_X(x) = \sum_m f_{X|E_m}(x) \cdot P(E_m)$$
- **Teorema della Media Condizionale**:
    $$E[X] = \int_{-\infty}^\infty x f_X(x) dx = \sum_m P(E_m) \int_{-\infty}^\infty x f_{X|E_m}(x) dx = \sum_m P(E_m) E[X|E_m]$$
- **Giustificazione Matematica (Analogia Quantizzazione)**: 
    Il docente spiega che il teorema della media per le variabili continue è il limite della media per variabili discrete quando il passo di quantizzazione $\Delta \to 0$. In questo limite, la variabile discreta approssima la continua con probabilità 1.

### 4. Trasformazioni di Variabili Aleatorie
Data una trasformazione $y = g(x)$ con $X$ continua:

- **Caso 1: Corrispondenza 1 a 1 (Strictly Monotona)**:
    - *Crescente*: $f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{d}{dy} g^{-1}(y)$
    - *Decrescente*: $f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{1}{|g'(g^{-1}(y))|}$ (il segno della derivata viene assorbito dal valore assoluto).

- **Caso 2: Non Invertibile (Non Autonoma)**:
    Se l'equazione $y = g(x)$ ha $m(y)$ soluzioni $\{x_1, x_2, \dots, x_m\}$:
    $$f_Y(y) = \sum_{i=1}^{m(y)} \frac{f_X(x_i)}{|g'(x_i)|}$$

- **Metodo di Generazione (Metodo di Wiener)**:
    Se si ha una variabile uniforme $U \sim \text{Uniform}(0,1)$, si può generare una variabile $X$ con CDF $F_X$ tramite la trasformazione:
    $$X = F_X^{-1}(U)$$
    *Nota*: Se $g$ è monotona decrescente, la relazione diventa $F_Y(y) = 1 - F_X(g^{-1}(y))$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Variabile mista Esponenziale-Laplaciana
**Testo**: Si ha $X \sim \text{Esp}(\lambda)$ e una variabile binaria $B \in \{-1, 1\}$ indipendente da $X$, tale che $P(B=1) = \alpha$. Si definisce $Y = B \cdot X$. Determinare la distribuzione di $Y$.

- **Risoluzione Passo-Passo**:
    1. **Analisi della PDF di Y tramite Legge della Probabilità Totale**:
       Poiché $B$ è binaria, la partizione è $\{B=1, B=-1\}$.
       $f_Y(y) = f_Y(y|B=1)P(B=1) + f_Y(y|B=-1)P(B=-1)$
       Quando $B=1$, $Y=X$ (distribuzione Esponenziale $\lambda$).
       Quando $B=-1$, $Y=-X$ (distribuzione simmetrica rispetto a zero).
    2. **Sviluppo della formula**:
       $f_Y(y) = \alpha (\lambda e^{-\lambda y} \cdot \mathbb{1}_{y \ge 0}) + (1-\alpha) (\lambda e^{\lambda y} \cdot \mathbb{1}_{y \le 0})$
       *Nota*: Il docente ha evidenziato la necessità di fare attenzione ai segni di $y$ e ai limiti di integrazione.
    3. **Calcolo della CDF**:
       Per $y > 0$: $F_Y(y) = 1 - \frac{1}{2} e^{-\lambda y}$ (per $\alpha=0.5$); più precisamente, il docente ha derivato che la CDF dipende dalla somma delle probabilità delle due componenti.
    4. **Calcolo del Valore Quadratico Medio ($E[Y^2]$)**:
       $E[Y^2] = E[(B \cdot X)^2] = E[B^2] \cdot E[X^2]$ (per indipendenza).
       Poiché $B^2 = 1$ sempre (sia per $1$ che per $-1$), $E[B^2] = 1$.
       $E[X^2]$ per un'esponenziale è $2/\lambda^2$.
       Quindi, $E[Y^2] = 2/\lambda^2$.
    5. **Confronto Varianze**:
       - Variabile $X$ (Esponenziale): Media $E[X] = 1/\lambda$, Varianza $\text{Var}(X) = 2/\lambda^2 - (1/\lambda)^2 = 1/\lambda^2$.
       - Variabile $Y$ (Laplaciana): Media $E[Y] = 0$ (per simmetria), Varianza $\text{Var}(Y) = 2/\lambda^2 - 0^2 = 2/\lambda^2$.
       *Conclusione*: La varianza di $Y$ è il doppio di quella di $X$ perché $Y$ include l'incertezza del segno.

### Esercizio 2: Diseguaglianza di Markov per Variabili Continue
**Testo**: Dimostrare che la diseguaglianza di Markov vale anche per variabili continue non negative.

- **Risoluzione Passo-Passo**:
    1. **Punto di partenza**: $P(X \ge \delta) = \int_{\delta}^{\infty} f_X(x) dx$.
    2. **Semplificazione**: Poiché $x \ge \delta$, allora $x^m \ge \delta^m$ (per $m > 0$). Quindi $\frac{x^m}{\delta^m} \ge 1$.
    3. **Sostituzione**: $f_X(x) \le \frac{x^m}{\delta^m} f_X(x)$.
    4. **Integrazione**: $\int_{\delta}^{\infty} f_X(x) dx \le \int_{\delta}^{\infty} \frac{x^m}{\delta^m} f_X(x) dx \le \int_{0}^{\infty} \frac{x^m}{\delta^m} f_X(x) dx$.
    5. **Risultato finale**: $P(X \ge \delta) \le \frac{1}{\delta^m} \int_{0}^{\infty} x^m f_X(x) dx = \frac{E[X^m]}{\delta^m}$.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errore comune (PDF vs Probabilità)**: Non confondere il valore della densità $f_X(x)$ con una probabilità. La densità può essere maggiore di 1, mentre la probabilità non può mai superare 1.
- **Distinzione Monotonia**: Nel calcolo delle trasformazioni, è fondamentale distinguere tra funzioni crescenti e decrescenti per il segno della derivata della funzione inversa.
- **Trattamento del segno**: Il docente ha sottolineato come un piccolo errore nel gestire il segno di $y$ (es. passare da $y$ a $-y$) possa alterare completamente la PDF risultante.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Consigli di Studio**: Il docente suggerisce di focalizzarsi sulla logica delle trasformazioni e sulle proprietà delle CDF. "Passare dalla CDF" è spesso la strategia più sicura per evitare errori di calcolo.
- **Struttura della Prova**: Non specificata esplicitamente, ma si deduce l'importanza della capacità di derivare risultati dai principi fondamentali (LTP, trasformazioni).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Metodo di Wiener**: Citato per la generazione di variabili aleatorie tramite trasformazione della uniforme.
- **Integrali Euleriani**: Riferiti per il calcolo dei momenti della distribuzione esponenziale.