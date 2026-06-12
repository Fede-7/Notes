# SBOBINA - [STATISTICA / ELABORAZIONE DEI SEGNALI] | LEZIONE SULLE TECNICHE DI DETECTION E TEST D'IPOTESI

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato nel testo - Probabile Statistica Inferenziale/Signal Processing]
- **Docente**: [Non specificato]
- **Orari e Aule**: Prossimo incontro previsto per lunedì o martedì (da definire).
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: La lezione odierna presenta una modalità ibrida/telematica (menzionata la possibilità di passare alla modalità telematica a causa della festività).
- **Ricevimento e Supporto**: Informazioni non menzionate nella lezione.
- **Avvisi, Calendario e Assenze**:
    - **Festività**: Domani è festa del lavoro.
    - **Consigli pratici del docente**: Il docente sottolinea l'importanza di non limitarsi ai calcoli "scoccianti" ma di comprendere la logica sottostante (es. il concetto di statistica sufficiente e la transizione tra classificazione e detection).
- **Accesso ai Materiali**: Informazioni non menzionate nella lezione.

---

## 🎯 SOMMARIO RAPIDO
- **Massimizzazione della Probabilità di Corretta Decisione**: Logica di assegnazione delle regioni di decisione $\Omega$ basata sull'integrando massimo.
- **Analisi dei Test d'Ipotesi (Gaussiani, Poissoniani, Varianze)**: Derivazione analitica delle regole di decisione e calcolo delle prestazioni (errori di tipo I e II).
- **Statistica Sufficiente**: Identificazione delle variabili che contengono tutta l'informazione necessaria per il test (es. media campionaria, somma dei quadrati).
- **Detection Theory**: Transizione dai modelli Bayesiani (con a priori e costi noti) ai modelli di rilevazione (senza a priori noti), introducendo $\alpha$ e $\beta$.
- **Lemma di Neyman-Pearson**: Ottimizzazione della potenza del test sotto vincolo di significatività tramite il Rapporto di Verosimiglianza.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **Ipotesi Nulla** | $H_0$ | Stato di "quiete" della natura o assenza di segnale. |
| **Ipotesi Alternativa** | $H_1$ | Stato di perturbazione o presenza di un segnale/evento. |
| **Livello di Significatività** | $\alpha$ | Probabilità di negare $H_0$ quando $H_0$ è vera (Probabilità di Falso Allarme). |
| **Potenza del Test** | $1 - \beta$ | Probabilità di dichiarare correttamente l'evento sotto $H_1$. |
| **Probabilità di Perdita** | $\beta$ | Probabilità di non rilevare $H_1$ quando $H_1$ è vera (Missed Detection / Misprobability). |
| **Statistica Sufficiente** | - | Variabile casuale che contiene tutta l'informazione rilevante del campione per un determinato test. |
| **Rapporto di Verosimiglianza** | Likelihood Ratio | Rapporto tra le densità (o PMF) delle ipotesi $H_1$ e $H_0$. |
| **Distribuzione di Poisson** | $\text{Pois}(\lambda)$ | Distribuzione discreta utilizzata per modellare eventi rari; il parametro $\lambda$ rappresenta la media. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Massimizzazione della Probabilità di Corretta Decisione
Il docente spiega che non è necessario risolvere gli integrali complessi per determinare la regola di decisione. L'obiettivo è identificare quali punti dello spazio campionario $\Omega$ assegnare a ciascuna ipotesi per massimizzare la probabilità di corretta decisione.
- **Logica**: La probabilità di corretta decisione è data dalla sommatoria per ogni ipotesi $H_i$ della probabilità che l'ipotesi $H_i$ sia vera moltiplicata per la probabilità che l'osservabile $x^n$ cada nella regione di decisione $\Omega_i$.
- **Condizioni Tacite**: Si assume che la somma degli integrali (o delle sommatorie) su tutte le regioni $\Omega_i$ sia massima quando ogni punto $x^n$ viene assegnato alla regione $\Omega_k$ in cui l'integrando (la densità di probabilità) è massimo.
- **Proprietà**: Poiché gli integrandi sono funzioni non negative, assegnare un punto a più regioni simultaneamente ridurrebbe il contributo totale alla sommatoria. Pertanto, la regola di decisione ottimale assegna $x^n$ a $\Omega_k$ se e solo se il contributo è maggiore di ogni altro possibile.

### 2. Test d'Ipotesi Gaussiani (Media Campionaria)
Analisi del caso in cui si hanno due ipotesi $H_1$ e $H_2$ con medie $\mu_1$ e $\mu_2$ e varianza $\sigma^2$ nota.
- **Spiegazione Teorica**: Si confrontano le densità di probabilità delle osservazioni indipendenti e identicamente distribuite (i.i.d.).
- **Derivazione del Test**:
    1. La densità del vettore $x^n$ sotto $H_1$ è il prodotto delle PDF dei singoli elementi: $f(x^n|H_1) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu_1)^2}{2\sigma^2}\right)$.
    2. Semplificando il prodotto degli esponenziali, si ottiene $f(x^n|H_1) = \left(\frac{1}{\sqrt{2\pi\sigma^2}}\right)^n \exp\left(-\frac{1}{2\sigma^2} \sum (x_i - \mu_1)^2\right)$.
    3. Applicando il logaritmo per semplificare il confronto, si isolano i dati dai parametri. Il termine che dipende dai dati è la somma dei quadrati.
    4. Sviluppando i quadrati e semplificando i termini che appaiono in entrambi i membri, la decisione si riduce al confronto tra la media campionaria $\bar{x} = \frac{1}{n} \sum x_i$ e una soglia $\eta$.
- **Statistica Sufficiente**: La media campionaria è sufficiente per ogni test sulla media statistica. Non è necessario conoscere tutti gli elementi del vettore, ma solo la loro somma.
- **Calcolo delle Prestazioni**:
    - Sotto $H_1$, la statistica di decisione segue una distribuzione normale $\mathcal{N}(\mu_1, \sigma^2/n)$.
    - Sotto $H_2$, segue $\mathcal{N}(\mu_2, \sigma^2/n)$.
    - La probabilità di errore $P_e$ tende a zero quando $n \rightarrow \infty$ grazie alla Legge dei Grandi Numeri (la media campionaria converge in probabilità alla media statistica).

### 3. Test d'Ipotesi Poissoniani (Caso Discreto)
Analisi del caso in cui $x^n \in \mathbb{N}_0$ segue una distribuzione di Poisson con parametri $\lambda_1$ e $\lambda_2$.
- **Spiegazione Teorica**: Si applica la regola della Verosimiglianza Massima (ML) poiché le probabilità a priori sono equiprobabili ($\pi_1 = \pi_2$).
- **Derivazione**:
    1. La PMF del prodotto è $P(x^n|H_1) = \frac{\lambda_1^{\sum x_i}}{\prod x_i!} e^{-n\lambda_1}$.
    2. Prendendo il logaritmo e isolando i dati: $\sum x_i \ln \lambda_1 - n\lambda_1 > \sum x_i \ln \lambda_2 - n\lambda_2$.
    3. La regola di decisione si riduce a confrontare $\bar{x}$ con una soglia $\eta$.
- **Proprietà della Somma**: Il docente dimostra che la somma di due variabili indipendenti di Poisson $\text{Pois}(\lambda_1)$ e $\text{Pois}(\lambda_2)$ segue una distribuzione $\text{Pois}(\lambda_1 + \lambda_2)$ utilizzando l'espansione binomiale di Newton. Questo semplifica il calcolo della probabilità di errore per la somma delle osservazioni.

### 4. Test sulla Varianza
Confronto tra due varianze $\sigma_1^2$ e $\sigma_2^2$ con medie nulle.
- **Logica**: Il test sulla varianza è equivalentemente un test sulla media dei quadrati $x_i^2$.
- **Derivazione**: Confrontando i logaritmi delle densità gaussiane, si ottiene che la decisione dipende dalla sommatoria $\sum x_i^2$.
- **Connessione con Chi-Quadro**: La statistica $\frac{1}{n} \sum x_i^2$ è legata alla distribuzione $\chi^2$, fondamentale in molti contesti di machine learning e statistica.

### 5. Detection Theory (Teoria della Rivelazione)
Passaggio concettuale fondamentale: dalla *classificazione* alla *rilevazione*.
- **Classificazione (Approccio Bayesiano)**: Si conoscono a priori le probabilità $\pi_i$ e i costi di errore $C_{ij}$. L'obiettivo è minimizzare il rischio di Bayes.
- **Rivelazione (Detection Theory)**: Si definisce uno stato di "natura inquieta" ($H_0$) e uno di "perturbazione" ($H_1$). Non è possibile assegnare costi o a priori affidabili (es. insorgenza di una pandemia o attacchi di droni improvvisi).
- **Parametri Critici**:
    - **$\alpha$ (Significance Level)**: Probabilità di falso allarme (dire che c'è un evento quando non c'è).
    - **$1 - \beta$ (Test Power)**: Probabilità di rilevare correttamente l'evento.
- **Esempi Citati**:
    - *Esempio Droni*: Rilevamento di droni tramite radar passivi. Il costo di un falso allarme (abbattere un aereo civile) deve essere bassissimo ($10^{-9}$, $10^{-12}$), mentre la potenza del test deve essere altissima.
    - *Esempio Pandemia*: Difficoltà nel definire a priori la probabilità di un evento catastrofico e i costi associati.

### 6. Lemma di Neyman-Pearson
- **Obiettivo**: Massimizzare la potenza del test ($1-\beta$) sotto il vincolo che il livello di significatività ($\alpha$) sia minore di un valore massimo consentito.
- **Risoluzione**: Si tratta di un problema di ottimizzazione vincolata. La soluzione garantita dal lemma consiste nel confrontare il **Rapporto di Verosimiglianza (Likelihood Ratio)** con una soglia $\eta$.
- **Soglia $\eta$**: La soglia viene scelta in modo che la probabilità di falso allarme sia esattamente uguale al massimo livello consentito.
- **Trade-off**: Esiste una relazione monotona tra $\alpha$ e $1-\beta$. Se si vuole ridurre $\alpha$ (falsi allarmi quasi nulli), si tende a ridurre anche la potenza del test, a meno di non aumentare $n$ (dimensione del campione) o la complessità del sistema di monitoraggio.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Test di Ipotesi su Medie Gaussiane
- **Testo**: Due ipotesi $H_1, H_2$ con medie $\mu_1 > \mu_2$, varianza $\sigma^2$ nota e osservazioni i.i.d.
- **Risoluzione Passo-Passo**:
    1. Scrittura della verosimiglianza del prodotto delle PDF: $f(x^n|H_1) \propto \exp\left(-\frac{\sum (x_i - \mu_1)^2}{2\sigma^2}\right)$.
    2. Applicazione del logaritmo: $\sum (x_i - \mu_1)^2 < \sum (x_i - \mu_2)^2$.
    3. Espansione dei quadrati e semplificazione dei termini indipendenti dai dati: $\sum x_i^2 - 2\mu_1\sum x_i + n\mu_1^2 < \sum x_i^2 - 2\mu_2\sum x_i + n\mu_2^2$.
    4. Semplificazione finale: $2(\mu_1 - \mu_2)\sum x_i < n(\mu_2^2 - \mu_1^2)$.
    5. Divisione per $2n(\mu_1 - \mu_2)$ (notando che $\mu_1 - \mu_2 > 0$): $\bar{x} < \frac{\mu_1 + \mu_2}{2}$.
- **Concetti Applicati**: Log-verosimiglianza, statistica sufficiente, semplificazione algebrica.
- **Semplificazioni/Trucchi**: Il docente evidenzia come termini come $\sum x_i^2$ "vengano via" perché compaiono in entrambi i membri del confronto.

### Esercizio 2: Test d'Ipotesi Poissoniano
- **Testo**: Confronto tra $\lambda_1$ e $\lambda_2$ per variabili discrete.
- **Risoluzione Passo-Passo**:
    1. PMF: $P(x^n|H_1) = \frac{\lambda_1^{\sum x_i}}{\prod x_i!} e^{-n\lambda_1}$.
    2. Confronto logaritmico: $\sum x_i \ln \lambda_1 - n\lambda_1 > \sum x_i \ln \lambda_2 - n\lambda_2$.
    3. Isolamento dati: $\sum x_i (\ln \lambda_1 - \ln \lambda_2) > n(\lambda_1 - \lambda_2)$.
    4. Regola di decisione: $\bar{x} > \frac{\lambda_1 - \lambda_2}{\ln \lambda_1 - \ln \lambda_2}$.
- **Concetti Applicati**: Somma di variabili Poissoniane, espansione binomiale di Newton.

### Esercizio 3: Test sulla Varianza
- **Testo**: Confronto tra $\sigma_1^2$ e $\sigma_2^2$ con $\mu=0$.
- **Risoluzione Passo-Passo**:
    1. PDF: $f(x^n|H_1) \propto (\sigma_1^2)^{-n/2} \exp\left(-\frac{\sum x_i^2}{2\sigma_1^2}\right)$.
    2. Logaritmo: $-\frac{n}{2} \ln \sigma_1^2 - \frac{\sum x_i^2}{2\sigma_1^2} < -\frac{n}{2} \ln \sigma_2^2 - \frac{\sum x_i^2}{2\sigma_2^2}$.
    3. Semplificazione: $\frac{1}{n} \sum x_i^2 > \text{Soglia}(\sigma_1, \sigma_2)$.
- **Concetti Applicati**: Distribuzione Chi-quadro, statistiche sufficienti.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * Confondere la *classificazione* (dove si conoscono a priori le probabilità e i costi) con la *rilevazione* (dove non si conoscono).
    * Pensare di dover risolvere gli integrali complessi per trovare la regola di decisione; la logica è invece focalizzata sul punto di massimo della densità.
- **Chiarimenti Metodologici**:
    * Il docente sottolinea che la statistica sufficiente (come la media campionaria) è fondamentale perché permette di ridurre la dimensionalità del problema senza perdere informazioni.
    * La transizione dal continuo (PDF) al discreto (PMF) è banale e segue le stesse regole logiche di massimizzazione.
- **Punti Critici per l'Esame**:
    * Comprendere il trade-off tra $\alpha$ e $1-\beta$: è impossibile avere entrambi vicini a zero senza aumentare la dimensione del campione $n$ o la complessità del sistema.
    * Sapere derivare la regola di decisione tramite il rapporto di verosimiglianza (Likelihood Ratio).

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    * Ottimizzazione (ricerca di minimi e massimi vincolati, moltiplicatori di Lagrange).
    * Calcolo delle probabilità (integrali, sommatorie, variabili casuali indipendenti).
- **Consigli di Studio Espliciti**:
    * Non spaventarsi dai calcoli: "sono calcoli scoccianti ma sono sempre gli stessi".
    * Focalizzarsi sulla logica della statistica sufficiente e sui concetti di Detection Theory.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Detection Theory**: Citata come letteratura sterminata e immensa per lo studio della rivelazione degli scostamenti della natura.
- **Espansione Binomiale di Newton**: Utilizzata per la dimostrazione della somma delle variabili Poissoniane.