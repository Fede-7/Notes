# SBOBINA - Teoria della Stima dei Parametri | Lezione sulla Stima Continua e Rischio Bayesiano

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Informazione non menzionata nella lezione]
- **Docente**: [Informazione non menzionata nella lezione]
- **Orari e Aule**: [Informazione non menzionata nella lezione]
- **Organizzazione Didattica**:
    - **CFU e Ore**: [Informazione non menzionata nella lezione]
    - **Modalità di erogazione**: [Informazione non menzionata nella lezione]
- **Ricevimento e Supporto**: [Informazione non menzionata nella lezione]
- **Avvisi, Calendario e Assenze**: [Informazione non menzionata nella lezione]
- **Consigli pratici del docente**: 
    - Il docente sottolinea che, sebbene i calcoli matematici siano onerosi, la struttura logica sottostante è sintetica e può essere riassunta in pochi passaggi chiave.
    - Per l'esame orale, è preferibile dimostrare la comprensione dei concetti teorici e delle proprietà degli stimatori piuttosto che la capacità di eseguire calcoli complessi a memoria.
- **Accesso ai Materiali**: [Informazione non menzionata nella lezione]

---

## 🎯 SOMMARIO RAPIDO
1.  **Limiti della classificazione per parametri continui**: Perché la minimizzazione della probabilità di errore non è applicabile alla stima di parametri continui.
2.  **Funzione di Costo e Rischio Bayesiano**: Introduzione del criterio di ottimizzazione tramite la media del costo atteso.
3.  **Derivazione degli stimatori MMSE e MAP**: Dimostrazione matematica dei due stimatori principali e delle loro diverse basi teoriche.
4.  **Analisi delle prestazioni degli stimatori**: Definizione di bias (polarizzazione), consistenza in media quadratica e consistenza in probabilità.
5.  **Esempio applicativo sulla sorgente binaria**: Calcolo pratico di $\hat{\theta}_{MMSE}$ e $\hat{\theta}_{MAP}$ per una sorgente con distribuzione uniforme.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Parametro | $\theta$ | Variabile aleatoria che regola il sistema (es. probabilità di successo). |
| Stimatore | $\hat{\theta}$ | Funzione dei dati osservati utilizzata per determinare un valore prossimo alla realizzazione di $\theta$. |
| Errore | $\delta\theta$ | Differenza tra il valore stimato e il valore vero ($\hat{\theta} - \theta$). |
| Densità Posteriore | $f(\theta | x_n)$ | Distribuzione di probabilità del parametro dato gli osservabili $x_n$. |
| Rischio Bayesiano | $R$ | Media statistica della funzione di costo rispetto ai dati e al parametro. |
| Bias (Polarizzazione) | - | Errore sistematico: uno stimatore è polarizzato se la sua media condizionale non coincide con il parametro vero. |
| Consistenza in Media Quadratica | - | Proprietà per cui l'Errore Quadratico Medio (MSE) tende a zero al crescere della dimensione del campione ($n \rightarrow \infty$). |
| Consistenza in Probabilità | - | Proprietà per cui la probabilità che lo stimatore discosti dal valore vero di più di $\epsilon$ tende a zero per $n \rightarrow \infty$. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Limiti della Classificazione nei Parametri Continui
Il docente distingue tra la **classificazione** (parametri discreti/ipotesi) e la **stima dei parametri** (parametri continui).
- **Problematica**: Nella classificazione, è possibile definire un criterio di ottimo che minimizzi la probabilità di errore. Nella stima di un parametro continuo $\theta$, questo non è possibile poiché $\theta$ assume ogni singolo valore con probabilità nulla. 
- **Conseguenza**: Poiché l'evento $\hat{\theta} = \theta$ ha probabilità 1, non si può utilizzare la probabilità di errore come criterio di progetto. È necessario definire una **funzione di costo**.

### 2. Funzione di Costo e Rischio Bayesiano
Per valutare la qualità di uno stimatore $\hat{\theta}$, si definisce una funzione di costo $C(\delta\theta)$ che penalizza l'errore.
- **Rischio Bayesiano ($R$)**: Si definisce come la media della funzione di costo:
  $$R = E[C(\delta\theta)]$$
- **Ottimizzazione**: L'obiettivo è trovare lo stimatore che minimizza il rischio medio Bayesiano. Per una data funzione di costo, si identifica quindi uno stimatore specifico che elabora i dati per determinare il valore più probabile/ottimale.

### 3. Lo Stimatore MMSE (Minimum Mean Square Error)
Se scegliamo come funzione di costo una funzione quadratica:
$$C(\delta\theta) = (\delta\theta)^2$$
- **Significato**: Questa funzione pesa molto gli errori grandi e poco gli errori piccoli (andamento quadratico).
- **Derivazione**: Per minimizzare l'integrale dell'errore quadratico medio:
  $$\min_{\hat{\theta}} \int (\theta - \hat{\theta})^2 f(\theta | x_n) d\theta$$
  Sviluppando l'integrale e applicando la linearità:
  $$\int \theta^2 f(\theta | x_n) d\theta - 2\hat{\theta} \int \theta f(\theta | x_n) d\theta + \hat{\theta}^2 \int f(\theta | x_n) d\theta$$
  Derivando rispetto a $\hat{\theta}$ e ponendo la derivata uguale a zero:
  $$2\hat{\theta} = 2 \int \theta f(\theta | x_n) d\theta \implies \hat{\theta}_{MMSE} = E[\theta | x_n]$$
- **Conclusione**: Lo stimatore MMSE è la **media condizionale** del parametro dato gli osservabili. Rappresenta la base della regressione (nel caso gaussiano, la regressione lineare).

### 4. Lo Stimatore MAP (Maximum A Posteriori)
Il docente introduce una funzione di costo diversa, basata su un intervallo di "accettabilità" $\epsilon$ (funzione a gradino):
- Se l'errore è piccolo (entro $\pm\epsilon/2$), il costo è 0.
- Se l'errore è grande, il costo è 1.
- **Ottimizzazione**: Minimizzare questo costo equivale a massimizzare la probabilità che il parametro si trovi nell'intervallo di accettabilità. Per $\epsilon$ piccolo, questo significa massimizzare la densità posteriore nel punto in cui essa è massima.
- **Definizione**:
  $$\hat{\theta}_{MAP} = \arg\max_{\theta} f(\theta | x_n)$$
- **Proprietà**: Poiché il logaritmo è monotono crescente, massimizzare $f(\theta | x_n)$ equivale a massimizzare $\ln f(\theta | x_n)$.

### 5. Analisi delle Prestazioni e Consistenza
Il docente confronta i due stimatori attraverso tre criteri:
1.  **Bias (Polarizzazione)**:
    - **MMSE**: È **polarizzato** (presenta un errore sistematico), poiché la sua media condizionata non è esattamente $\theta$, ma tende ad esso. Tuttavia, è **asintoticamente non polarizzato** (corretto), poiché $\lim_{n \to \infty} E[\hat{\theta}_{MMSE} | \theta] = \theta$.
    - **MAP**: È **non polarizzato** (corretto) per definizione del punto di massimo.
2.  **Errore Quadratico Medio (MSE)**:
    - Per $n$ finito, l'errore quadratico medio del MMSE è più piccolo rispetto a quello del MAP (perché è ottimizzato proprio su tale criterio).
3.  **Consistenza**:
    - Entrambi gli stimatori sono **consistenti in media quadratica**, poiché il loro MSE tende a 0 per $n \rightarrow \infty$.
    - **Relazione tra consistenze**: La consistenza in media quadratica è una convergenza forte che implica la **consistenza in probabilità** (consistenza debole).
    - **Dimostrazione (Diseguaglianza di Chebyshev)**:
      $$P(|\hat{\theta} - \theta| > \epsilon) \leq \frac{E[(\hat{\theta} - \theta)^2]}{\epsilon^2}$$
      Se l'MSE ($E[(\hat{\theta} - \theta)^2]$) tende a zero, allora la probabilità che lo stimatore discosti dal valore vero di più di $\epsilon$ tende a zero.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Stima del parametro di una sorgente binaria
**Testo**: Si osserva una stringa binaria $x_n$ proveniente da una sorgente senza memoria (bit indipendenti). La sorgente emette '1' con probabilità $\theta$, dove $\theta$ è una variabile aleatoria uniforme in $[0,1]$. Definire gli stimatori MMSE e MAP.

**Risoluzione Passo-Passo**:
1.  **Likelihood (Verosimiglanza)**: Dato che i bit sono indipendenti, la probabilità di osservare $w$ successi in $n$ prove è:
    $$P(x_n | \theta) = \theta^w (1-\theta)^{n-w}$$
2.  **Prior**: La densità di $\theta$ è uniforme in $[0,1]$:
    $$f(\theta) = 1, \quad \theta \in [0,1]$$
3.  **Densità Posteriore**: Applicando il teorema di Bayes:
    $$f(\theta | x_n) = \frac{P(x_n | \theta) f(\theta)}{P(x_n)}$$
4.  **Calcolo della densità marginale $P(x_n)$**:
    $$P(x_n) = \int_0^1 \theta^w (1-\theta)^{n-w} d\theta$$
    Questo integrale è una **funzione Beta**. Il risultato è:
    $$P(x_n) = \frac{1}{\binom{n}{w}(n+1)}$$
5.  **Calcolo dello stimatore MMSE**:
    $$\hat{\theta}_{MMSE} = E[\theta | x_n] = \frac{\int_0^1 \theta \cdot \theta^w (1-\theta)^{n-w} d\theta}{\frac{1}{\binom{n}{w}(n+1)}} = \frac{\binom{n}{w}(n+1) \cdot \frac{w+1}{n+2}}{\binom{n}{w}(n+1)} = \frac{w+1}{n+2}$$
6.  **Calcolo dello stimatore MAP**:
    $$\hat{\theta}_{MAP} = \arg\max_{\theta} \left( \frac{\theta^w (1-\theta)^{n-w}}{\text{costante}} \right)$$
    Derivando il logaritmo: $\frac{d}{d\theta} [w \ln \theta + (n-w) \ln(1-\theta)] = \frac{w}{\theta} - \frac{n-w}{1-\theta} = 0$
    $$\implies w(1-\theta) = \theta(n-w) \implies w - w\theta = n\theta - w\theta \implies \hat{\theta}_{MAP} = \frac{w}{n}$$

**Concetti Applicati**: Densità condizionali, Funzione Beta, Media condizionale, Ottimizzazione del rischio Bayesiano.
**Semplificazioni/Trucchi**: Il docente nota che, sebbene il calcolo dell'integrale marginale sia complesso, la struttura della soluzione finale è molto semplice e armoniosa.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - Non confondere la **regola di decisione** (dove si sceglie l'ipotesi con la massima probabilità) con la **stima di parametri** (dove si cerca il valore di un parametro continuo).
    - Attenzione alla distinzione tra **polarizzato** e **asintoticamente non polarizzato**: un estimatore può essere "sbagliato" in media per campioni piccoli ma diventare corretto quando il campione cresce.
- **Chiarimenti Metodologici**:
    - La regressione lineare è un caso specifico (spesso associato al caso Gaussiano) di una più generale struttura di regressione.
    - L'uso del logaritmo per trovare il MAP è una semplificazione valida perché il logaritmo è monotono crescente.
- **Punti Critici per l'Esame**:
    - Il docente enfatizza che non si deve "sp काटellare" i conti all'orale; è fondamentale spiegare il passaggio logico (es. "minimizziamo il rischio Bayesiano usando la funzione di costo quadratica").
    - È fondamentale saper distinguere perché, per parametri continui, la probabilità di errore non può essere la cifra di merito.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: [Informazione non menzionata nella lezione]
- **Propedeuticità e Prerequisiti**:
    - **Teoria della Decisione**: Fondamentale per il parallelismo tra regole di decisione e stima.
    - **Probabilità**: Conoscenza delle densità condizionali, funzioni Beta e media condizionale.
- **Consigli di Studio Espliciti**:
    - Studiare bene le densità condizionali, poiché sono la base di tutte le applicazioni discusse.
    - Capire la differenza tra la convergenza in media quadratica e quella in probabilità (uso della diseguaglianza di Chebyshev).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- [Informazione non menzionata nella lezione]