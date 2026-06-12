# SBOBINA - [Nome Corso non specificato] | Lezione sulle Distribuzioni Discrete

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non menzionato nel testo]
- **Docente**: [Non menzionato nel testo]
- **Orari e Aule**: [Non menzionati nel testo]
- **Organizzazione Didattica**:
    - **CFU e Ore**: Informazione non menzionata nella lezione.
    - **Modalità di erogazione**: Lezione frontale/digitale. Il docente indica che la lezione continuerà il martedì successivo.
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**:
    - Il docente annuncia che un file contenente una serie di esercizi verrà messo online "tra un'oretta".
- **Consigli pratici del docente**:
    - Il docente sottolinea l'importanza di non perdere l'intuizione matematica nonostante la complessità delle sommatorie: "non vi deve tagliare l'intuizione".
    - Enfasi sulla necessità di capire le regole fondamentali (composta, totale, Bayes) per rendere i calcoli fattibili.
- **Accesso ai Materiali**: File di esercizi in arrivo (da controllare sulla piattaforma).

---

## 🎯 SOMMARIO RAPIDO
- Analisi della Legge dei Grandi Numeri e convergenza della media campionaria.
- Caratterizzazione delle variabili aleatorie discrete (Binomiale, Uniforme, Poissoniana, Geometrica).
- Applicazioni pratiche delle distribuzioni (compressione dati, traffico reti, teoria delle code).
- Applicazione del Teorema di Bayes su eventi condizionati con variabili geometriche.
- Concetto di caratterizzazione condizionale e "potatura" dei dati (Outliers).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Esperimento Omega | $\Omega$ | Spazio dei campioni (insieme di tutti i risultati possibili). |
| Valore Osservato | $x_\omega$ | Il valore numerico associato a un particolare risultato $\omega$. |
| Media Campionaria | $\bar{x}$ | Somma dei valori osservati divisa per il numero di tentativi $n$. |
| Media Statistica | $E[X]$ | Valore atteso della variabile aleatoria. |
| Probabilità Masse (PMF) | $P(X=x)$ | Probabilità che la variabile aleatoria assuma un valore specifico. |
| Variabile Binaria | $n=2$ | Contestualizzato come numero di tentativi o esiti possibili in alcuni esempi. |
| Parametro di Successo | $p$ | Probabilità di successo di un evento indipendente. |
| Parametro Poissoniano | $\lambda$ | Media degli eventi che si verificano in un intervallo definito. |
| Parametro Geometrico | $p$ | Probabilità di successo del primo evento desiderato. |
| Variabile Aleatoria Uniforme | $X \sim U$ | Variabile in cui ogni valore dell'alfabeto ha la stessa probabilità. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Legge dei Grandi Numeri (LLN)
- **Spiegazione Teorica**: La legge dei grandi numeri stabilisce che la media campionaria converge alla media statistica quando il numero di tentativi $n$ cresce all'infinito. Tale legge è fondamentale non solo per la statistica, ma anche per la **compressione dati** e la teoria della codifica (es. algoritmi Lempel-Ziv, ZIP). Esistono due versioni: la *Legge Debole* e la *Legge Forte*, che dipendono dalla modalità di convergenza del rapporto $\frac{n_i}{n}$.
- **Condizioni Tacite e Prerequisiti**: Si assume che i tentativi siano indipendenti.
- **Formule e Modelli Matematici**:
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_{\omega_i}$$
  Dove $x_{\omega_i}$ è l'ennesimo valore osservato. In termini di variabili discrete con un alfabeto di $m$ valori distinti $\{x_1, x_2, \dots, x_m\}$, la media può essere espressa come:
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^{m} n_i x_i$$
  dove $n_i$ è il numero di volte in cui il valore $x_i$ è stato osservato. Al tendere di $n \to \infty$, il rapporto $\frac{n_i}{n}$ converge alla probabilità $P(X=x_i)$.
- **Esempi Specifici Citati**:
  - *Esempio del Portafoglio*: Per sapere mediamente quanti soldi si hanno in tasca, si può aprire il portafoglio 100 volte, sommare le cifre ottenute e dividere per 100. Questo rappresenta la media campionaria.

### 2. Distribuzione Binomiale
- **Spiegazione Teorica**: Modella il numero di successi ($k$) in un numero fissato ($n$) di prove indipendenti, dove ogni prova ha una probabilità di successo $p$.
- **Condizioni Tacite e Prerequisiti**: Le prove devono essere **indipendenti statisticamente**. Se la probabilità di un evento dipendesse dal precedente, il modello non sarebbe applicabile.
- **Formule e Modelli Matematici**:
  $$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
  Dove $\binom{n}{k}$ è il coefficiente binomiale che indica i modi in cui $k$ successi possono essere distribuiti in $n$ prove.
  **Media Statistica**:
  $$E[X] = \sum_{k=0}^{n} k \binom{n}{k} p^k (1-p)^{n-k} = np$$
  *(Il docente mostra la derivazione tramite la sostituzione $k-1 = L$ e l'uso della serie binomiale).*
- **Esempi Specifici Citati**:
  - *Esempio della Stringa Binaria*: In una stringa di lunghezza $n=4$, qual è la probabilità di osservare una particolare stringa con $k=3$ successi? Se le posizioni sono fisse (es. 1011), la probabilità è $p^3(1-p)^1$. Se le posizioni non sono fisse, si moltiplica per il numero di combinazioni $\binom{4}{3}=4$.
  - *Esempio della Roulette*: Puntare sul numero 7 in 100 lanci. Se la probabilità di successo è $1/37$, la media attesa è $np = 100 \cdot (1/37)$.
  - *Esempio del Vaccino*: In una classe di 30 bambini, si somministra un vaccino efficace nel 10% dei casi ($p=0.1$). Il numero atteso di bambini immuni è $np = 30 \cdot 0.1 = 3$.

### 3. Distribuzione Uniforme
- **Spiegazione Teorica**: Una variabile aleatoria $X$ è uniforme su un alfabeto se la sua Probabilità Masse (PMF) è costante. Ogni evento nell'alfabeto ha la stessa probabilità.
- **Formule e Modelli Matematici**:
  $$P(X=x_i) = \frac{1}{m}$$
  La media statistica corrisponde alla media aritmetica dei valori dell'alfabeto.
- **Esempi Specifici Citati**:
  - *Aneddoto di Gauss*: Il docente cita la storia di Gauss che trovò il metodo efficiente per sommare i numeri da 1 a 100: $\sum_{i=1}^{m} i = \frac{m(m+1)}{2}$.

### 4. Distribuzione Poissoniana
- **Spiegazione Teorica**: Modella il numero di eventi che si verificano in un intervallo continuo (tempo, spazio, area). È il limite per le distribuzioni discrete e non tiene conto degli eventi passati ("non invecchia"). È alla base della **Teoria delle Code**.
- **Condizioni Tacite e Prerequisiti**: $\lambda > 0$.
- **Formule e Modelli Matematici**:
  $$P(X=i) = \frac{\lambda^i e^{-\lambda}}{i!}$$
  Dove $\lambda$ è il parametro della media.
  **Media Statistica**:
  $$E[X] = \sum_{i=0}^{\infty} i \frac{\lambda^i e^{-\lambda}}{i!} = \lambda$$
  *(Derivato tramite la serie di Maclaurin della funzione esponenziale).*
- **Esempi Specifici Citati**:
  - *Semaforo Urbano*: Modellare il numero di auto in coda per regolare il tempo del verde.
  - *Router*: Garantire che il numero di pacchetti in attesa non superi una certa soglia per evitare latenze.
  - *Ufficio Postale*: Determinare il numero di sportelli necessari in base alle persone in attesa.

### 5. Distribuzione Geometrica
- **Spiegazione Teorica**: Modella il numero di tentativi necessari per ottenere il **primo successo** in una serie di prove indipendenti.
- **Formule e Modelli Matematici**:
  $$P(X=n) = q^{n-1}p$$
  Dove $q = 1-p$ è la probabilità di fallimento.
  **Media Statistica**:
  $$E[X] = \frac{1}{p}$$
  *(Derivata tramite la derivata della serie geometrica $\sum q^n$).*
- **Esempi Specifici Citati**:
  - *Roulette (Primo Successo)*: Puntare sullo zero. La variabile $X$ indica alla quale puntata esce lo zero per la prima volta.
  - *Analisi del Banco*: Il docente spiega che il banco non perde statisticamente nel lungo termine, ma introduce concetti di limiti di puntata e strategie di gioco (Teoria dei Giochi).

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Il problema dei dadi (Bayes + Geometrica)
- **Testo**: In un'urna ci sono 3 dadi: 2 onesti (uniformi, $P(6)=1/6$) e 1 truccato (il 6 esce con probabilità $1/2$, gli altri risultati sono equiprobabili). Si estraggono 2 dadi e si lanciano fino a ottenere una coppia di 6. Sapendo che la prima coppia di 6 si è ottenuta al secondo lancio, qual è la probabilità che i dadi estratti siano entrambi onesti?
- **Risoluzione Passo-Passo**:
  1.  **Caratterizzazione dei dadi**:
      - Dato onesto ($H$): $P(X=i) = 1/6$ per $i \in \{1..6\}$.
      - Dato truccato ($T$): $P(X=6) = 1/2$, $P(X \neq 6) = 1/10$.
  2.  **Probabilità di estrazione**:
      - Probabilità di estrarre due onesti ($HH$): $\frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3}$ (Poiché dopo aver estratto il primo, ne rimangono 2).
      - Probabilità di estrarre un onesto e uno truccato ($HT$): $\frac{2}{3} \cdot \frac{1}{3} = \frac{2}{9}$.
  3.  **Applicazione della Legge di Bayes**:
      $$P(HH | X=2) = \frac{P(X=2 | HH) P(HH)}{P(X=2)}$$
  4.  **Calcolo delle probabilità condizionate (Geometriche)**:
      - Se i dadi sono $HH$: La probabilità di successo è $(1/6) \cdot (1/6) = 1/36$. Essendo una geometrica, la probabilità del successo al lancio 2 è $(35/36) \cdot (1/36)$.
      - Se i dadi sono $HT$: La probabilità di successo è $(1/6) \cdot (1/2) = 1/12$. La probabilità del successo al lancio 2 è $(11/12) \cdot (1/12)$.
  5.  **Probabilità Totale**: Calcolare $P(X=2)$ sommando i prodotti delle probabilità condizionate per i diversi tipi di dadi estratti.
- **Concetti Applicati**: Legge di Bayes, Probabilità Composta, Distribuzione Geometrica.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    *   **Indipendenza**: Non si può usare la distribuzione binomiale o geometrica se le emissioni non sono indipendenti (es. se la probabilità cambia ad ogni lancio).
    *   **Confusione sulle serie**: Il docente avverte di non farsi distrarre dalle operazioni algebriche delle sommatorie: "non vi deve tagliare l'intuizione".
- **Chiarimenti Metodologici**:
    *   Distinzione tra **probabilità condizionata** (cambia lo spazio campionario $\Omega$) e **probabilità incondizionata**.
    *   La media statistica è il valore atteso $E[X]$.
- **Punti Critici per l'Esame**:
    *   Saper derivare la media delle distribuzioni principali (Binomiale, Poissoniana, Geometrica) usando le serie di potenze.
    *   Saper applicare il Teorema di Bayes in contesti di probabilità composta.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    *   Conoscenza della probabilità classica (eventi, spazi campioni, probabilità composta).
    *   Conoscenza delle serie matematiche (serie geometrica, serie esponenziale/di Maclaurin).
- **Consigli di Studio Espliciti**:
    *   "Se capite bene questo [la caratterizzazione delle variabili aleatorie], poi andiamo avanti facilmente."
    *   Esercitarsi a vedere come si calcola la media statistica anche se il risultato è noto intuitivamente.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Lempel-Ziv (LZ)**: Algoritmo di compressione citato per il contesto della teoria dell'informazione.
- **Huffman/Ziff**: Citati in relazione agli algoritmi di compressione universale (1977).
- **Note del docente**: Un file con esercizi verrà messo online per ilucidare i concetti trattati.