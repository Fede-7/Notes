# SBOBINA - Statistica Avanzata e Teoria dell'Informazione | Lezione su Variabili Congiunte e Distribuzioni Gaussiane

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Statistica Avanzata / Teoria dell'Informazione
- **Docente**: Non specificato (Trascrizione in ucraino/italiano)
- **Orari e Aule**: Informazione non menzionata nella lezione.
- **Organizzazione Didattica**:
    - **Recuperi**: Il docente indica una disponibilità di **4 ore e mezza** per il recupero/ricevimento se gli studenti non sono stati presenti.
    - **Periodo**: Riferimento al mese di settembre per l'inizio/andamento del corso.
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**: Informazione non menzionata nella lezione.
- **Accesso ai Materiali**: Informazione non menzionata nella lezione.

---

## 🎯 SOMMARIO RAPIDO
1.  **Variabili Continue e PDF Congiunta**: Definizione di densità di probabilità per variabili multiple, marginalizzazione e condizioni di indipendenza.
2.  **Covarianza e Matrici di Correlazione**: Formalizzazione della relazione tra variabili tramite la matrice di covarianza $K_X$ e il coefficiente $\rho$.
3.  **Proprietà della Distribuzione Gaussiana**: Analisi delle trasformazioni affini ($Z = AX + B$) e della famiglia "Location-Scale".
4.  **Analisi delle CDF e Funzione Q**: Relazione tra la funzione di errore ($\text{erf}$), la CDF e la funzione complementare $Q(x)$.
5.  **Introduzione alla Teoria dell'Informazione**: Teorema di Shannon, ridondanza dei dati e capacità di canale.
6.  **Sorgenti Binarie e Compressione**: Modellazione di sorgenti senza memoria e implicazioni sulla compressione dati (es. file ZIP).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Densità di Probabilità Congiunta | $f_{XY}(x, y)$ | Funzione che descrive la distribuzione simultanea di due variabili continue. |
| Marginalizzazione | - | Operazione di integrazione su una delle variabili per ottenere la PDF della variabile rimanente. |
| Covarianza | $\text{Cov}(X, Y)$ | Misura del grado di variazione lineare tra due variabili casuali; $\text{Cov}(X, X) = \sigma^2$. |
| Coefficiente di Correlazione | $\rho$ | Parametro che indica la forza e la direzione della relazione lineare (tra -1 e 1). |
| Matrice di Covarianza | $K_X$ | Matrice che sintetizza le varianze e le covarianze di un vettore di variabili casuali. |
| Trasformazione Affine | $Z = AX + B$ | Operazione lineare su un vettore casuale dove $A$ è una matrice e $B$ è un vettore costante. |
| Famiglia Location-Scale | - | Classe di distribuzioni ottenibili tramite traslazione ($\mu$) e scalatura ($\sigma$). |
| Funzione Complementare | $Q(x)$ | Probabilità che una variabile Gaussiana standard sia maggiore di $x$. |
| Capacità di Canale | $C$ | Massimo tasso di trasmissione di informazioni per unità di tempo in un canale. |
| Ridondanza | - | Informazione aggiuntiva inserita per correggere gli errori di trasmissione in canali rumorosi. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Variabili Continue e PDF Congiunta
- **Spiegazione Teorica**: Il docente espande il concetto di variabili casuali discrete alle variabili continue. Per due variabili $X$ e $Y$, la densità di probabilità congiunta $\rho(x, y)$ (o $f(x, y)$) è una funzione di due variabili che è indipendente dal punto specifico della regione. La probabilità che le variabili cadano in un insieme $C$ è data dall'integrale della densità su tale regione.
- **Condizioni Tacite e Prerequisiti**: Richiede la comprensione dell'integrazione su domini aperti e il concetto di densità come "massa" (analogia con l'integrazione della massa in fisica).
- **Formule e Modelli Matematici**:
    - Se $X$ e $Y$ sono indipendenti:
    $$f_{XY}(x, y) = f_X(x) \cdot f_Y(y)$$
    - La marginalizzazione avviene integrando su una variabile:
    $$f_X(x) = \int f_{XY}(x, y) \, dy$$
- **Esempi Specifici Citati**:
    - *Analogia della Massa*: Il docente paragona l'integrazione della PDF alla ricerca della massa di un oggetto in un volume specifico.

### 2. Covarianza e Matrici di Correlazione
- **Spiegazione Teorica**: Viene discussa la relazione tra variabili. La covarianza misura come le variabili variano insieme. In caso di indipendenza, la covarianza è zero. Il docente introduce la struttura matriciale della covarianza per vettori multi-dimensionali.
- **Formule e Modelli Matematici**:
    - Covarianza tra due variabili:
    $$\text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$$
    - Matrice di covarianza $K_X$ per un vettore bi-dimensionale $X = [x_1, x_2]^T$:
    $$K_X = \begin{bmatrix} \sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2 \end{bmatrix}$$
    - Dove $\rho$ è il coefficiente di correlazione.
- **Condizioni Tacite e Prerequisiti**: Si assume che $\sigma^2 \geq 0$ poiché la varianza è il quadrato di una misura non negativa.

### 3. Distribuzione Gaussiana e Trasformazioni Affini
- **Spiegazione Teorica**: La distribuzione Gaussiana è caratterizzata dai parametri $\mu$ (media) e $\sigma$ (deviazione standard). Il docente sottolinea la proprietà fondamentale: **la combinazione lineare di variabili gaussiane produce ancora una variabile gaussiana**.
- **Trasformazioni Affini**: Se $X$ è un vettore gaussiano con media $\mu_x$ e matrice di covarianza $K_x$, la trasformazione $Z = AX + B$ produce un nuovo vettore gaussiano.
- **Formule e Modelli Matematici**:
    - Nuova media: $\mu_z = A\mu_x + B$
    - Nuova matrice di covarianza: $K_z = A K_x A^T$
    - *Nota*: Il termine deterministico $B$ non influisce sulla varianza.
- **Famiglia Location-Scale**: Tutte le distribuzioni gaussiane possono essere ottenute tramite operazioni di scalatura (moltiplicazione per $\sigma$) e traslazione (addizione di $\mu$) della distribuzione standard $\mathcal{N}(0, 1)$.
- **Esempi Specifici Citati**:
    - *Esempio di Scalatura*: Moltiplicando una variabile per $\sigma$, si aumenta la dispersione attorno alla media, rendendo la PDF più "larga".
    - *Esempio di Traslazione*: Cambiando $\mu$, l'intera distribuzione si sposta a destra (se $\mu > 0$) o a sinistra (se $\mu < 0$).

### 4. Analisi delle CDF e Funzione Q
- **Spiegazione Teorica**: Il docente discute la funzione di distribuzione cumulata (CDF). Per la gaussiana, la CDF non ha una forma chiusa elementare, ma si esprime tramite la funzione di errore ($\text{erf}$).
- **Funzione Q**: Viene introdotta la funzione $Q(x)$, che rappresenta la probabilità che una variabile gaussiana standard sia maggiore di $x$.
- **Formule e Modelli Matematici**:
    - Relazione tra CDF e $Q(x)$: $\text{CDF}(x) = 1 - Q(x)$.
    - Simmetria della Gaussiana: L'area sotto la curva a sinistra di 0 è uguale a quella a destra.
    - Comportamento asintotico: Per $x \to \infty$, $Q(x) \to 0$.
- **Condizioni Tacite e Prerequisiti**: Richiede la conoscenza delle proprietà delle integrali impropri.

### 5. Introduzione alla Teoria dell'Informazione
- **Spiegazione Teorica**: Il docente introduce il concetto di canale e il Teorema di Shannon. Il punto centrale è che la "non-idealità" del canale (rumore) non influisce sulla quantità massima di dati trasmissibili, ma solo sulla velocità (throughput).
- **Ridondanza**: Per compensare il rumore, è necessario aggiungere ridondanza ai dati. Questo significa che per trasmettere 30 caratteri informativi, se il canale è disturbato, si potrebbero dover trasmettere molti più simboli.
- **Parametri di Trasmissione**:
    - **Banda Larga (Bandwidth)**: Capacità fisica del canale.
    - **Bitrate**: Velocità di trasmissione.
    - **Throughput**: Quantità effettiva di bit informativi per unità di tempo.
- **Capacità di Canale**:
    $$C = W \log_2(1 + \text{SNR})$$
    Dove $W$ è la banda e $\text{SNR}$ è il rapporto segnale-rumore.

### 6. Sorgenti Binarie e Compressione
- **Spiegazione Teorica**: Modellazione di una sorgente senza memoria che emette bit (0 o 1) indipendentemente.
- **Esempio di Compressione**: Il docente spiega come la compressione (es. file ZIP) funzioni identificando le frequenze dei simboli. Se un file è ben compresso, la frequenza dei 0 e degli 1 è quasi uniforme (massima entropia), rendendo difficile la compressione ulteriore.
- **Formule e Modelli Matematici**:
    - Per una sorgente binaria con probabilità $p$ di emettere 1:
    $$P(x) = p^{\sum x_i} (1-p)^{n-\sum x_i}$$
    - In caso di indipendenza (senza memoria), la PDF congiunta è il prodotto delle PDF marginali.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Trasformazione di un Vettore Gaussiano
- **Testo**: Dato un vettore casuale $X$ con media $\mu_x$ e matrice di covarianza $K_x$, determinare i parametri del vettore $Z = AX + B$.
- **Risoluzione Passo-Passo**:
    1. Identificare che $A$ è una matrice lineare e $B$ è un vettore costante.
    2. Calcolare la nuova media applicando la linearità: $\mu_z = A \mu_x + B$.
    3. Calcolare la nuova matrice di covarianza applicando la proprietà delle trasformazioni lineari: $K_z = A K_x A^T$.
    4. Osservare che la costante $B$ scompare nel calcolo della covarianza poiché la covarianza dipende dalle deviazioni dalla media.
- **Concetti Applicati**: Trasformazioni affini, proprietà delle matrici di covarianza.
- **Semplificazioni/Trucchi**: Ricordare che l'operatore di media non agisce sulla matrice di trasformazione $A$.

### Esercizio 2: Sorgente Binaria senza Memoria
- **Testo**: Modellare una sorgente che emette una sequenza di 10 bit dove la probabilità di emettere 1 è $p$.
- **Risoluzione Passo-Passo**:
    1. Definire gli eventi come indipendenti (senza memoria).
    2. Scrivere la probabilità per una singola emissione: $P(x_i = 1) = p$, $P(x_i = 0) = 1-p$.
    3. Calcolare la PDF congiunta come prodotto delle probabilità singole: $P(x) = \prod_{i=1}^{10} P(x_i)$.
    4. Semplificare la forma finale: $P(x) = p^k (1-p)^{10-k}$, dove $k$ è il numero di bit pari a 1 nella sequenza.
- **Concetti Applicati**: Sorgenti stocastiche, indipendenza, PDF congiunta.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * Non confondere la banda larga con il throughput: aumentare la banda non significa necessariamente aumentare la velocità se il rapporto segnale-rumore è basso.
    * Non confondere la varianza con la deviazione standard: la varianza è sempre non negativa ($\sigma^2 \geq 0$).
- **Chiarimenti Metodologici**:
    * La distribuzione gaussiana è "speciale" perché è l'unica che rimane invariante (in forma) sotto combinazioni lineari.
    * La differenza tra "indipendenza" e "non correlazione": se le variabili sono indipendenti, la covarianza è zero, ma il contrario non è necessariamente vero (eccezione: variabili gaussiane).
- **Punti Critici per l'Esame**:
    * Dimostrazione della trasformazione della matrice di covarianza $K_z = A K_x A^T$.
    * Interpretazione fisica della funzione $Q(x)$ e della sua asimmetria/simmetria.
    * Teorema di Shannon e il ruolo della ridondanza.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    * Calcolo Matriciale (fondamentale per le trasformazioni affini).
    * Probabilità Base (PDF, CDF, Variabili Continue).
- **Consigli di Studio Espliciti**:
    * "Non voglio sentire memoria ma logica": Il docente enfatizza la comprensione dei concetti (es. perché la varianza non cambia con la traslazione) piuttosto che la memorizzazione pura delle formule.
    * Studiare bene le proprietà della distribuzione gaussiana poiché sono alla base delle inferenze statistiche e del machine learning.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- [Non menzionato esplicitamente, ma si fa riferimento alla teoria standard di Shannon e ai manuali di Statistica Matematica].