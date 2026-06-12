# SBOBINA - STATISTICA MATEMATICA | LEZIONE SULLE STIME (BAYESIANE, ML, EFFICIENZA)

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato - Calcolo della Probabilità / Statistica Matematica]
- **Docente**: [Non specificato]
- **Orari e Aule**: Informazione non menzionata nella lezione.
- **Organizzazione Didattica**:
    - **Contesto**: Corso del 3° anno, 2° semestre. Destinato a studenti con background di calcolo della probabilità.
    - **Stile del Docente**: Il docente specifica che la sua lezione "deve cominciare a creare e avviare", procedendo dall'alto a sinistra verso il basso a destra della lavagna senza mai cancellare i passaggi precedenti.
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**: Informazione non menzionata nella lezione.
- **Accesso ai Materiali**: Informazione non menzionata nella lezione.

---

## 🎯 SOMMARIO RAPIDO
1. **Transizione da Classificazione a Stima**: Analisi del passaggio da variabili discrete a variabili continue e l'impatto sulla matrice dei costi.
2. **Apparato Bayesiano**: Definizione di densità a priori, condizionali e a posteriori; ottimizzazione del rischio medio-baesiano.
3. **MMSE vs MAP**: Confronto tra stimatori minimizzanti l'errore quadratico (media condizionale) e quelli a massima probabilità a posteriori.
4. **Stima a Massima Verosimiglianza (ML)**: Definizione come limite della stima MAP a priori uniforme; proprietà di invarianza e consistenza.
5. **Efficienza e Limite di Cramér-Rao**: Introduzione dell'Informazione di Fisher come parametro della precisione teorica di uno stimatore.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **Densità a Priori** | $f_\theta(\theta)$ | Densità di probabilità del parametro $\theta$ prima dell'osservazione dei dati (considerato come variabile aleatoria). |
| **Osservabili** | $x^n$ | Vettore dei dati osservati; possono essere continui (PDF) o discreti (PMF). |
| **Densità a Posteriore** | $f(\theta | x^n)$ | Densità del parametro aggiornata dopo l'osservazione dei dati $x^n$. |
| **Rischio Medio-Baesiano** | $E[C(\theta, \hat{\theta}) | x^n]$ | Media statistica della funzione di costo condizionata agli osservabili. |
| **Stimatore MMSE** | $\hat{\theta}_{MMSE}$ | Stimatore che minimizza l'Errore Quadratico Medio; corrisponde alla media condizionale. |
| **Stimatore MAP** | $\hat{\theta}_{MAP}$ | Stimatore che massimizza la densità a posteriori. |
| **Stimatore ML** | $\hat{\theta}_{ML}$ | Stimatore che massimizza la densità condizionale dei dati $f(x^n | \theta)$. |
| **Bias (Polarizzazione)** | $E[\hat{\theta} | \theta] \neq \theta$ | Errore sistematico dello stimatore (se uguale a $\theta$, lo stimatore è *unbiased* o corretto). |
| **Consistenza** | $\hat{\theta} \xrightarrow{n \to \infty} \theta$ | Proprietà per cui lo stimatore converge al vero valore all'aumentare della taglia del campione. |
| **Informazione di Fisher** | $I(\theta)$ | Quantità che misura quanta informazione i dati forniscono sul parametro $\theta$. |
| **Limite di Cramér-Rao** | $\text{Var}(\hat{\theta}) \ge \frac{1}{I(\theta)}$ | Limite teorico inferiore della varianza di qualsiasi stimatore non polarizzato. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Stima vs Classificazione (Il problema della Continuità)
- **Spiegazione Teorica**: Il docente distingue la **classificazione** dalla **stima**. Nella classificazione, lo stato della natura è incapsulato in variabili discrete; nella stima, lo stato della natura è una variabile continua.
- **Condizioni Tacite e Vincoli**: In ambito continuo, la probabilità che due variabili siano uguali è zero ($P(X=x)=0$). 
- **Implicazioni**: Poiché non si può mai vedere il valore esatto di una variabile continua, la "matrice dei costi" associata agli stati discreti non è applicabile direttamente. Si passa a valutare le prestazioni del sistema tramite "cifre di merito" (metriche di ottimizzazione).

### 2. Framework Bayesiano
- **Spiegazione Teorica**: Se il parametro $\theta$ è una variabile aleatoria con densità a priori $f_\theta(\theta)$, e gli osservabili $x^n$ hanno una densità condizionata $f(x^n | \theta)$, la densità a posteriori è data da:
  $$f(\theta | x^n) = \frac{f(x^n | \theta) f(\theta)}{f(x^n)}$$
- **Ottimizzazione del Rischio**: Per una funzione di costo $C(\theta, \hat{\theta})$, lo stimatore ottimo minimizza il costo condizionale medio:
  $$\int C(\theta, \hat{\theta}) f(\theta | x^n) d\theta$$
- **Criteri Specifici**:
    1. **Criterio MMSE**: Se $C(\epsilon) = (\theta - \hat{\theta})^2$, lo stimatore ottimo è la **media condizionale**: $\hat{\theta}_{MMSE} = E[\theta | x^n]$.
    2. **Criterio MAP**: Se il costo è unitario per deviazioni superiori a $\epsilon_0$, lo stimatore ottimo è la **moda** della posteriore.

### 3. Proprietà degli Estimatori
- **Correttezza (Unbiasedness)**: Uno stimatore è corretto se la sua media condizionata è pari al vero valore: $E[\hat{\theta} | \theta] = \theta$.
- **Consistenza**:
    - **In Media Quadratica**: Lo stimatore è consistente se l'errore quadratico medio va a zero per $n \to \infty$.
    - **In Probabilità**: La probabilità che la deviazione superi $\epsilon$ va a zero per $n \to \infty$. (La prima implica la seconda).
- **Simmetria e Convessità**: Se la densità a posteriori $f(\theta | x^n)$ è **simmetrica** rispetto alla sua media e la funzione di costo $C$ è **parità e convessa**, allora gli stimatori MMSE e MAP coincidono.

### 4. Stima a Massima Verosimiglianza (ML) e Invarianza
- **Definizione**: Quando non si dispone di una densità a priori (o essa è uniforme, ovvero di massima incertezza), la stima Bayesiana collassa nella stima ML. Lo stimatore ML massimizza $f(x^n | \theta)$.
- **Invarianza**: La stima ML di una funzione $g(\theta)$ è uguale alla funzione $g$ applicata alla stima ML di $\theta$.
  $$\hat{\theta}_{ML} = g(\hat{\theta}_{ML})$$
- **Esempio Sorgente Binaria (Senza Memoria)**:
    - Dato: Sorgente che emette '1' con probabilità non nota $\theta$.
    - Calcolo ML: $\hat{\theta}_{ML} = \frac{m}{n}$ (dove $m$ è il numero di successi).
    - Risultato: Questo stimatore è non polarizzato e consistente.

### 5. Efficienza e Limite di Cramér-Rao
- **Il Limite Teorico**: Esiste un limite inferiore alla varianza di ogni stimatore non polarizzato, dato dall'inverso dell'Informazione di Fisher $I(\theta)$.
- **Stimatore Efficiente**: Uno stimatore la cui varianza raggiunge esattamente il limite di Cramér-Rao.
- **Efficienza Asintotica**: Lo stimatore ML è **sempre asintoticamente efficiente** (raggiunge il limite quando $n \to \infty$), anche se non lo è necessariamente al finito.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Stima della Frequenza in Sorgente Binaria (ML)
- **Testo**: Determinare lo stimatore ML per la frequenza $\theta$ di una sorgente binaria senza memoria.
- **Risoluzione Passo-Passo**:
  1. Si scrive la PMF: $P(x^n | \theta) = \theta^m (1-\theta)^{n-m}$.
  2. Si prende il logaritmo per massimizzare la verosimiglianza: $\lambda = m \ln(\theta) + (n-m) \ln(1-\theta)$.
  3. Si calcola la derivata rispetto a $\theta$: $\frac{d\lambda}{d\theta} = \frac{m}{\theta} - \frac{n-m}{1-\theta}$.
  4. Si annulla la derivata: $\frac{m}{\theta} = \frac{n-m}{1-\theta} \implies m(1-\theta) = \theta(n-m) \implies m - m\theta = n\theta - m\theta \implies \theta_{ML} = \frac{m}{n}$.
- **Concetti Applicati**: Massima Verosimiglianza, derivate, log-verosimiglianza.
- **Semplificazioni/Trucchi**: Il docente nota che massimizzare il logaritmo è equivalente a massimizzare la funzione originale poiché il logaritmo è monotono crescente.

### Esercizio 2: Derivazione dell'Informazione di Fisher (Sorgente Binaria)
- **Testo**: Calcolare l'informazione di Fisher $I(\theta)$ per una sorgente binaria.
- **Risoluzione Passo-Passo**:
  1. Si parte dalla derivata seconda del logaritmo della PMF.
  2. Si applica il teorema della media statistica per eliminare la dipendenza dai dati specifici $x^n$.
  3. Si ottiene la formula: $I(\theta) = \frac{n}{\theta(1-\theta)}$.
  4. Si deduce il limite di Cramér-Rao: $\text{Var}(\hat{\theta}) \ge \frac{\theta(1-\theta)}{n}$.
- **Concetti Applicati**: Informazione di Fisher, Teorema della Media Condizionale, Limite di Cramér-Rao.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * Non confondere la varianza con la precisione assoluta: una varianza può essere costante (es. stimatore costante $\hat{\theta} = \tan(54^\circ)$), ma questo non lo rende uno stimatore utile.
    * La probabilità può essere "ingannevole" (*deceitful*): non bisogna confondere una varianza zero con la correttezza dello stimatore.
- **Chiarimenti Metodologici**:
    * **Stima vs Prior**: Se il parametro è puramente deterministico e non noto, non ha senso parlare di densità a priori; si parla di "famiglie di distribuzioni".
    * **Robustezza**: Se la priori supposta diverge da quella reale, il sistema diventa non robusto e le prestazioni degradano.
- **Punti Critici per l'Esame**:
    * Lo stimatore ML è sempre asintoticamente efficiente.
    * La stima MMSE e la stima MAP coincidono se la posteriore è simmetrica e la funzione di costo è convessa.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    * Calcolo della Probabilità (fondamentale per le basi di stima e varianza).
- **Consigli di Studio Espliciti**:
    * "Andate sulla ML tutta la vita" (per la sua efficienza asintotica).
    * Studiare bene la distinzione tra varianza al finito e comportamento asintotico.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Fisher, R.A.**: Citato come grande statistico inglese (inventore del test di Fisher).
- **Cramér-Rao**: Citato per il limite della varianza.
- **Nota sulla Teoria dell'Informazione**: Il docente menziona che la teoria dei codici è un sottinsieme della teoria dell'informazione e che la teoria dei codici è spesso trattata in modo differente rispetto alla teoria dell'informazione pura.

---

## 🎙️ ANECDOTI E NOTE DI CONTESTO
- **Esempio Tecnologico (5G)**: Il docente illustra la trasmissione 5G come esempio di parametro deterministico non noto. Il segnale viene convertito da analogico a digitale (quantizzazione), modulato (cosinusoidali) e viaggia per un cammino ignoto. La fase finale è deterministica ma non nota a priori (problema di sincronizzazione).
- **Esempio della Moneta**: Per spiegare la stima $\theta = m/n$, il docente usa l'esempio di una moneta (testa/croce) per capire se è truccata o meno.
- **Esempio Medico**: Per spiegare la mediana (minimizzazione dell'errore assoluto), viene citato il tempo di guarigione/sopravvivenza dei pazienti, dove la mediana è spesso più informativa della media.
- **Esempio "Maria Callas"**: Citato per spiegare la quantizzazione del segnale audio (da tempo continuo a discreto).