# SBOBINA - STATISTICA MATEMATICA | LEZIONE SULLA STIMA E TEORIA DELLA DECISIONE

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Statistica Matematica / Teoria della Stima
- **Docente**: Non specificato (Trascrizione didattica)
- **Orari e Aule**: Prossima lezione prevista per **martedì in presenza**.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione svolta in modalità telematica (avviso ricevuto prima delle 30:00).
    - **Accesso ai Materiali**: La lavagna della lezione precedente è stata caricata sulla piattaforma Teams.
- **Ricevimento e Supporto**: Consultare la piattaforma Teams per il caricamento dei materiali didattici.
- **Avvisi, Calendario e Assenze**:
    - La lezione è stata gestita online, ma il docente invita gli studenti a tornare in presenza per la sessione successiva.
- **Consigli pratici del docente**:
    - Il docente sottolinea l'importanza di comprendere la logica sottostante alle derivazioni matematiche (es. il passaggio dalla densità della PMF alla derivata del logaritmo).

---

## 🎯 SOMMARIO RAPIDO
- **Stimatori Non Bayesiani vs Bayesiani**: Distinzione fondamentale tra parametri deterministici e variabili aleatorie.
- **Proprietà degli Stimatori**: Analisi dettagliata di correttezza (unbiasedness), consistenza (quadratica e in probabilità) ed efficienza.
- **Limite di Cramer-Rao (CRLB)**: Derivazione formale della varianza minima tramite l'Informazione di Fisher.
- **Stima Massima Verosimiglianza (MLE)**: Proprietà asintotiche e condizioni di efficienza.
- **Teoria della Decisione e Comunicazioni**: Applicazione di regole MAP e test di Neyman-Pearson in scenari di segnali binari e comunicazioni ottiche (SNR).

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| **Stimatore Non Bayesiano** | $\hat{\theta}$ | Estimatore usato quando manca un modello credibile della variabilità a priori; il parametro $\theta$ è considerato una costante deterministica. |
| **Corretto (Unbiased)** | $E[\hat{\theta}] = \theta$ | Lo stimatore è corretto se la sua media statistica coincide esattamente con il valore vero del parametro. |
| **Consistente in Media Quadratica** | $\lim_{n \to \infty} E[(\hat{\theta}_n - \theta)^2] = 0$ | Forma forte di convergenza: l'errore quadratico medio tende a zero all'aumentare della taglia campionaria $n$. |
| **Consistente in Probabilità** | $\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| > \epsilon) = 0$ | Lo stimatore converge al valore vero con frequenza tendente a 1 per ogni $\epsilon > 0$. |
| **Informazione di Fisher** | $I(\theta)$ | Misura della sensibilità della verosimiglianza rispetto al parametro; definita come l'opposto della media statistica della derivata seconda del logaritmo della densità. |
| **Limite di Cramer-Rao (CRLB)** | $\text{Var}(\hat{\theta}) \ge 1/I(\theta)$ | Limite inferiore alla varianza di ogni stimatore non polarizzato. |
| **Efficiente** | $\text{Var}(\hat{\theta}) = 1/I(\theta)$ | Uno stimatore è efficiente se raggiunge il limite di Cramer-Rao (minima varianza possibile). |
| **Asintoticamente Efficiente** | $\lim_{n \to \infty} \text{Var}(\hat{\theta}_n) = 1/I(\theta)$ | Lo stimatore raggiunge il limite di Cramer-Rao per campioni infiniti. |
| **SNR** | *Signal-to-Noise Ratio* | Rapporto tra l'energia del segnale e l'energia del rumore in una comunicazione. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Fondamenti degli Stimatori Non Bayesiani
- **Spiegazione Teorica**: Uno stimatore non bayesiano è necessario quando non si dispone di informazioni a priori sufficienti per assegnare una distribuzione di probabilità al parametro. In questo contesto, il parametro $\theta$ non è una variabile aleatoria, ma una **costante deterministica** appartenente a un insieme possibile.
- **Relazione con la stima MAP**: Il caso non bayesiano può essere visto come il limite di una stima MAP (Maximum A Posteriori) in cui la densità a priori $\pi(\theta)$ è uniforme (ovvero la sua derivata è nulla). In questo scenario, non è possibile includere il logaritmo della densità a priori nel processo di massimizzazione.
- **Funzione di Verosimiglianza**: Si lavora sulla funzione $\lambda(x^n, \theta)$, che rappresenta il logaritmo della densità (PDF) o della massa di probabilità (PMF) del vettore osservato $x^n$.
- **Definizione di MLE**: Lo stimatore di Massima Verosimiglianza $\hat{\theta}$ è definito come il punto in cui la verosimiglianza è massima:
  $$\hat{\theta} = \text{argmax}_\theta \lambda(x^n, \theta)$$

### 2. Proprietà degli Stimatori e Limite di Cramer-Rao
- **Condizioni di Qualità**:
    - **Correttezza**: $E[\hat{\theta}] = \theta$.
    - **Consistenza in Media Quadratica**: Implica la consistenza in probabilità.
- **Derivazione dell'Informazione di Fisher**:
  Il docente ha dimostrato che per una distribuzione discreta $\sum P(x^n, \theta) = 1$. Derivando rispetto a $\theta$:
  $$\sum \frac{\partial}{\partial \theta} P(x^n, \theta) = 0 \implies \sum \frac{\partial}{\partial \theta} \ln P(x^n, \theta) P(x^n, \theta) = 0$$
  Questo implica che la media statistica della derivata prima del logaritmo della verosimiglianza è nulla: $E\left[ \frac{\partial}{\partial \theta} \lambda(x^n, \theta) \right] = 0$.
- **Derivazione della Varianza**:
  Derivando nuovamente la sommatoria $\sum \frac{\partial}{\partial \theta} \lambda(x^n, \theta) P(x^n, \theta) = 0$ e usando la regola del prodotto:
  $$\sum \frac{\partial^2}{\partial \theta^2} \lambda(x^n, \theta) P(x^n, \theta) + \sum \frac{\partial}{\partial \theta} \lambda(x^n, \theta) \frac{\partial}{\partial \theta} P(x^n, \theta) = 0$$
  Sapendo che $\frac{\partial}{\partial \theta} P = \frac{\partial}{\partial \theta} \lambda P$, la seconda parte diventa $\sum \left(\frac{\partial}{\partial \theta} \lambda\right)^2 P$.
  Da cui: $E\left[ \frac{\partial^2}{\partial \theta^2} \lambda \right] = -E\left[ \left(\frac{\partial}{\partial \theta} \lambda\right)^2 \right]$.
- **Risultato finale (Limite di Cramer-Rao)**:
  Poiché la varianza di uno stimatore corretto $\hat{\theta}$ è $E[(\hat{\theta}-\theta)^2] = E[\hat{\theta}^2] - \theta^2$, e utilizzando la disuguaglianza di Schwarz sulla covarianza tra $\hat{\theta}$ e $\frac{\partial}{\partial \theta} \lambda$, si ottiene:
  $$\text{Var}(\hat{\theta}) \ge \frac{1}{I(\theta)} = -\frac{1}{E\left[ \frac{\partial^2}{\partial \theta^2} \lambda(x^n, \theta) \right]}$$

### 3. Proprietà Asintotiche della MLE
- **Garanzie della MLE**:
    - Se la MLE non raggiunge il limite di Cramer-Rao, nessun altro stimatore può essere più efficiente.
    - La MLE è asintoticamente non polarizzata.
    - La MLE è asintoticamente consistente in probabilità.
    - La MLE è asintoticamente efficiente (raggiunge il limite di Cramer-Rao per $n \to \infty$).

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Stima del parametro $\mu$ della Distribuzione di Laplace
- **Testo**: Dato $x^n$ di variabili indipendenti identicamente distribuite (i.i.d.) con PDF $f(x_i|\mu) = \frac{1}{2\mu} e^{-\frac{|x_i|}{\mu}}$. Determinare lo stimatore MLE di $\mu$, dimostrarne la correttezza, la consistenza in media quadratica e l'efficienza.
- **Risoluzione Passo-Passo**:
  1. **Verosimiglianza**: $\lambda(x^n, \mu) = -n \ln(2\mu) - \frac{1}{\mu} \sum_{i=1}^n |x_i|$.
  2. **Massimizzazione**: Derivando rispetto a $\mu$: $\frac{\partial \lambda}{\partial \mu} = -\frac{n}{\mu} + \frac{1}{\mu^2} \sum |x_i| = 0$.
  3. **Risultato**: $\hat{\mu} = \frac{1}{n} \sum_{i=1}^n |x_i|$.
  4. **Correttezza**: La media di $|x_i|$ per una variabile di Laplace è $\mu$. Quindi $E[\hat{\mu}] = \mu$.
  5. **Varianza**: $\text{Var}(|x_1|) = \mu^2$. Poiché le $x_i$ sono indipendenti, $\text{Var}(\hat{\mu}) = \frac{1}{n^2} \sum \text{Var}(|x_i|) = \frac{n\mu^2}{n^2} = \frac{\mu^2}{n}$.
  6. **Informazione di Fisher**: $I(\mu) = -E[\frac{\partial^2 \lambda}{\partial \mu^2}] = -E[\frac{n}{\mu^2} - \frac{2}{\mu^3} \sum |x_i|] = -\frac{n}{\mu^2} + \frac{2}{\mu^3}(n\mu) = \frac{n}{\mu^2}$.
  7. **Efficienza**: Poiché $\text{Var}(\hat{\mu}) = \frac{\mu^2}{n} = \frac{1}{I(\mu)}$, lo stimatore è efficiente al finito.

### Esercizio 2: Teoria della Decisione (Sorgenti Binarie)
- **Testo**: Due sorgenti $S_1, S_2$ con probabilità di emettere '1' pari a $P_1, P_2$ ($P_1 > P_2$). $\pi_1 = \frac{1}{3}$, $\pi_2 = \frac{2}{3}$. Osservabile $Y$ (numero di '1' in 100 bit). Determinare regola MAP e test di Neyman-Pearson.
- **Risoluzione Passo-Passo**:
  1. **Regola MAP**: Si sceglie $H_1$ se $P(H_1|y) > P(H_2|y)$, ovvero se $\frac{P(y|H_1)}{\pi_1} > \frac{P(y|H_2)}{\pi_2}$.
  2. **Semplificazione**: Con $\frac{\pi_2}{\pi_1} = 2$, la regola è $\frac{P(y|H_1)}{P(y|H_2)} > 2$.
  3. **Soglia**: Espandendo le binomiali e semplificando, la soglia $y$ deve soddisfare una condizione logaritmica legata al rapporto $P_1/P_2$.
  4. **Probabilità di Errore**: Calcolata tramite il teorema della probabilità totale: $P(\text{errore}) = \pi_1 P(\text{errore}|H_1) + \pi_2 P(\text{errore}|H_2)$.
  5. **Test di Neyman-Pearson**: In assenza di priori, si confronta il rapporto di verosimiglianza con una soglia $\lambda$ tale che la Probabilità di Falso Allarme (PFA) sia $\alpha$.

### Esercizio 3: Comunicazioni Ottiche (On-Off Keying)
- **Testo**: Segnale esponenziale. Sotto $H_0$: energia del rumore $\mu_0$. Sotto $H_1$: energia del segnale + rumore $\mu_1 = \mu_0 + P$. Determinare relazione tra $\alpha$ (livello significatività) e potenza del test ($1-\beta$).
- **Risoluzione Passo-Passo**:
  1. **Soglia**: Il ricevitore decide $H_1$ se l'energia $x > \eta'$.
  2. **$\alpha$**: $P(x > \eta' | H_0) = e^{-\eta'/\mu_0} = \alpha \implies \eta' = -\mu_0 \ln \alpha$.
  3. **Potenza ($1-\beta$)**: $P(x > \eta' | H_1) = e^{-\eta'/\mu_1} = \alpha^{\mu_0/\mu_1}$.
  4. **Relazione**: Poiché $\frac{\mu_1}{\mu_0} = \frac{\mu_0 + P}{\mu_0} = 1 + \frac{P}{\mu_0} = 1 + \text{SNR}$, la relazione diventa:
    $$1 - \beta = \alpha^{1/\text{SNR}}$$
- **Interpretazione**: All'aumentare del SNR, la potenza del test tende a 1 per ogni $\alpha > 0$.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errore Comune**: Confondere la varianza di uno stimatore con l'errore quadratico medio. Il docente chiarisce che questi coincidono **solo se lo stimatore è corretto (unbiased)**.
- **Chiarimento Metodologico**: La derivazione dell'Informazione di Fisher per distribuzioni discrete è più immediata rispetto a quelle continue poiché evita l'uso delle derivate parziali, utilizzando la derivata totale.
- **Punti Critici per l'Esame**:
    - Capacità di dimostrare l'efficienza di uno stimatore tramite il limite di Cramer-Rao.
    - Distinzione tra regole MAP (con priori) e test di Neyman-Pearson (livello $\alpha$ fissato).
    - Interpretazione fisica del SNR in contesti di comunicazione reale.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Non specificata (da verificare nei prossimi avvisi).
- **Propedeuticità e Prerequisiti**:
    - Cultura matematica solida (calcolo differenziale e integrale).
    - Conoscenza delle distribuzioni di probabilità base (Binomiale, Laplace, Esponenziale).
- **Consigli di Studio Espliciti**:
    - "Non voglio sentire memoria ma logica": Il docente insiste sulla capacità di seguire i passaggi logici delle derivazioni anziché imparare formule a memoria.
    - Verificare sempre la correttezza dello stimatore prima di procedere al calcolo dell'efficienza.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Distribuzioni di Laplace**: Citata come base per la dimostrazione di efficienza.
- **Distribuzioni Binomiali**: Utilizzate per la teoria della decisione.
- **Funzione Gamma ($\Gamma$)**: Utilizzata per il calcolo delle medie delle distribuzioni.