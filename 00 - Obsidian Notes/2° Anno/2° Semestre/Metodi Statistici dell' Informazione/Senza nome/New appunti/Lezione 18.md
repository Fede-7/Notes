# SBOBINA - STATISTICA INFERENZIALE | LEZIONE SU TEST DI IPOTESI E STIMA

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: Statistica Inferenziale (Ingegneria/Informatica/Matematica)
- **Docente**: [Non specificato nella trascrizione]
- **Orari e Aule**: Menzione di una lezione "stamattina" e un prossimo incontro "giovedì".
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale (con accenno a un recente spostamento forzato di aula per protesta).
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**:
    - Il docente ha menzionato uno spostamento delle aule "per protesta" per cercare un ambiente più fresco.
- **Accesso ai Materiali**:
    - Il docente ha evidenziato che le slide sono state predisposte in modo ordinato per facilitare la comprensione, ma invita a non ignorarle poiché la loro struttura logica è fondamentale.

---

## 🎯 SOMMARIO RAPIDO
- Fondamenti della statistica inferenziale bayesiana (Prior, Likelihood, Posterior).
- Regole di decisione MAP (Maximum A Posteriori) e MLE (Maximum Likelihood).
- Analisi del Rapporto di Verosimiglianza (Likelihood Ratio) e della sua forma logaritmica.
- Teoria dei Test di Ipotesi (Neyman-Pearson): Errori di tipo I ($\alpha$), tipo II ($\beta$), Potenza e "FAR Explosion".
- Distinction tra Stima Bayesiana e Non-Bayesiana, e il concetto di Robustezza vs Ottimità.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Vettore di dati | $x^n$ | Realizzazione di un vettore aleatorio formato da $n$ variabili. |
| Ipotesi | $H_1, \dots, H_m$ | Diversi stati della natura (es. "natura inquieta" vs "natura perturbata"). |
| Probabilità a priori | $\pi_k$ | Probabilità che la natura si trovi nello stato $H_k$ prima dell'osservazione. |
| Densità Condizionale | $f(x^n|H_k)$ | PDF (continua) o PMF (discreta) dei dati dato lo stato della natura. |
| Regola di Decisione | $d(x^n)$ | Funzione che associa ogni realizzazione dei dati a un'ipotesi ritenuta vera. |
| Probabilità Posteriore | $P(H_k|x^n)$ | Probabilità che l'ipotesi $H_k$ sia vera dato che i dati osservati sono $x^n$. |
| Verosimiglianza | Likelihood | Probabilità dei dati dati l'ipotesi ($p(x^n|H_k)$). |
| Rapporto di Verosimiglianza | LR | Rapporto tra le verosimiglianze di due ipotesi (es. $H_2 / H_1$). |
| Falso Allarme | $\alpha$ (False Alarm Rate) | Probabilità di dichiarare $H_1$ (perturbazione) quando è vero $H_0$ (natura tranquilla). |
| Errore di Rilevazione | $\beta$ (Missed Detection) | Probabilità di non rilevare una perturbazione quando questa è presente. |
| Potenza del Test | $1-\beta$ | Probabilità di rilevare correttamente la perturbazione. |
| Rapporto di Verosimiglianza Logaritmico | $\Lambda(x^n)$ | Logaritmo del rapporto di verosimiglianza. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Fondamenti della Statistica Inferenziale Bayesiana
La statistica inferenziale si basa sull'osservazione di un nucleo di dati $x^n$ (vettore di $n$ variabili aleatorie, discrete o continue).
- **Stati della Natura**: La natura può trovarsi in $m$ stati diversi, corrispondenti a $m$ ipotesi $H_1, \dots, H_m$.
- **Informazione a Priori**: Conosciamo la probabilità $\pi_k$ (a priori) che la natura sia in uno stato $H_k$.
- **Distribuzioni Condizionali**: Conosciamo come i dati sono distribuiti dato lo stato della natura, ovvero le densità/funzioni di massa $f(x^n|H_k)$.
- **Probabilità Posteriore**: Una volta osservati i dati $x^n$, le probabilità cambiano. La probabilità che sia vera l'ipotesi $H_k$ dato i dati osservati è:
  $$P(H_k|x^n) = \frac{f(x^n|H_k) \pi_k}{f(x^n)}$$
  *(Nota: $f(x^n)$ è la densità incondizionale, ottenuta integrando/sommando la congiunta su tutti i possibili stati della natura).*
- **Regola di Decisione MAP (Maximum A Posteriori)**: Si sceglie l'ipotesi $H_k$ che massimizza la probabilità posteriore.
- **Regola di Decisione MLE (Maximum Likelihood)**: Se le ipotesi hanno probabilità a priori uguali (es. $\pi_1 = \pi_2$), la regola MAP coincide con la MLE, dove si sceglie l'ipotesi che massimizza la densità condizionale $f(x^n|H_k)$.

### 2. Analisi dell'Errore e Rapporto di Verosimiglanza
- **Probabilità di Errore**: Definita come la sommatoria per $i=1 \dots m$ di $\pi_i$ moltiplicata per la probabilità che $x^n$ non appartenga alla regione di decisione $\Omega_i$ (regione in favore di $H_i$), dato che $H_i$ è vera.
- **Rapporto di Verosimiglianza (Likelihood Ratio)**: Nel caso binario (due ipotesi), il test si riduce al confronto tra:
  $$L(x^n) = \frac{f(x^n|H_2)}{f(x^n|H_1)}$$
  Questo rapporto viene confrontato con una soglia $\eta$ che dipende dalle probabilità a priori.
- **Log-Likelihood Ratio**: È equivalente e spesso più pratico confrontare il logaritmo del rapporto con il logaritmo della soglia:
  $$\Lambda(x^n) = \ln \left( \frac{f(x^n|H_2)}{f(x^n|H_1)} \right) \gtreqless \ln(\eta)$$
  *Vantaggio:* Le quantità che dipendono dai dati appaiono linearmente nel dominio logaritmico.

### 3. Test di Ipotesi (Neyman-Pearson)
Il docente introduce il framework del test di ipotesi per la "rivelazione tempestiva di minacce" (es. hacker, droni, radar).
- **$H_0$**: Natura "inquieta" o "tranquilla" (dipende dal contesto, solitamente lo stato di base).
- **$H_1$**: Natura perturbata (presenza di una minaccia).
- **Errori Fondamentali**:
    1. **Falso Allarme (Tipo I)**: Dichiarare $H_1$ quando è vero $H_0$.
    2. **Errore di Rilevazione (Tipo II)**: Dichiarare $H_0$ quando è vero $H_1$ (*We miss the detection*).
- **Potenza del Test**: $1 - \beta$. L'obiettivo è massimizzare la potenza del test.
- **FAR Explosion**: Se si dichiara sempre $H_1$, la potenza del test è 1, ma il tasso di falso allarme (False Alert Rate) esplode, rendendo il test inutile (es. una macchina non si muoverebbe mai perché "c'è sempre un pedone").
- **Problema di Ottimizzazione**: Poiché potenza e falso allarme sono funzioni monotone l'una dell'altra, il problema non ha soluzione senza vincoli. Si massimizza la potenza del test (1-$\beta$) vincolando il falso allarme a un livello predeterminato $\alpha$.
- **Lemma di Neumann-Pearson**: Il test più potente che garantisce un falso allarme $\leq \alpha$ consiste nel confrontare il rapporto di verosimiglianza con una soglia $\eta$ determinata univocamente da $\alpha$.

### 4. Stima Bayesiana vs Non-Bayesiana
- **Stima Bayesiana**: Il parametro $\theta$ (es. probabilità di emissione di un bit) è considerato una variabile aleatoria con una densità a priori nota $f_\theta(\theta)$. Si ricava la densità a posteriori e si cerca lo stimatore ottimale.
- **Stima Non-Bayesiana**: Il parametro $\theta$ è un valore non noto e non si assume alcuna distribuzione a priori. Si cerca uno stimatore basato puramente sui dati.
- **Robustezza vs Ottimità**: 
    - **Ottimale**: Fornisce la migliore performance possibile se le ipotesi di progetto sono perfettamente verificate.
    - **Robusto**: Fornisce prestazioni soddisfacenti anche quando ci sono deviazioni dalle ipotesi di progetto. Il docente predilige l'approccio non-bayesiano per la sua robustezza.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Classificazione di Sorgenti Binarie
- **Testo**: Una sorgente emette bit indipendenti e identicamente distribuiti (i.i.d.). Non si sa se la probabilità di emettere "1" sia $P_1$ o $P_2$ (entrambe diprobabili).
- **Risoluzione Passo-Passo**:
  1. Si definisce il peso di Hamming $w$ (numero di "1" nella sequenza osservata).
  2. Si scrive la PMF condizionata $p(x^n|H_1)$ basata su $w$.
  3. Si costruisce il rapporto di verosimiglianza $\frac{p(x^n|H_1)}{p(x^n|H_2)}$.
  4. Si prende il logaritmo per ottenere il *log-likelihood ratio*.
  5. Si osserva che il test è equivalente a confrontare il peso $w$ con una soglia che dipende dalle probabilità a priori.
- **Concetti Applicati**: Rapporto di verosimiglianza, Log-likelihood ratio, indipendenza dei dati.

### Esercizio 2: Test sulla Media (Gaussiana)
- **Testo**: Vettori $x^n$ con media $\mu_1$ o $\mu_2$. Si assume $\pi_1 = \pi_2$.
- **Risoluzione Passo-Passo**:
  1. Il rapporto di verosimiglianza sotto ipotesi di indipendenza semplifica eliminando i termini non dipendenti dai dati.
  2. Si isola la media campionaria $\bar{x}$.
  3. Il test consiste nel confrontare $\bar{x}$ con la media aritmetica $\frac{\mu_1 + \mu_2}{2}$.
  4. Se $\bar{x} > \frac{\mu_1 + \mu_2}{2}$, si sceglie $H_2$, altrimenti $H_1$.
- **Concetti Applicati**: Statistica sufficiente, media campionaria.

### Esercizio 3: Test su Distribuzioni Esponenziali
- **Testo**: Sotto $H_1$ i dati sono esponenziali con parametro $\lambda_1$; sotto $H_0$ con $\lambda_0$. Determinare il test ottimo di Neumann-Pearson.
- **Risoluzione Passo-Passo**:
  1. Scrittura delle PDF: $f(x^n|H_1) = \lambda_1^n e^{-\lambda_1 \sum x_j}$ e $f(x^n|H_0) = \lambda_0^n e^{-\lambda_0 \sum x_j}$.
  2. Calcolo del rapporto di verosimiglianza: $L = \left(\frac{\lambda_1}{\lambda_0}\right)^n e^{-(\lambda_1 - \lambda_0) \sum x_j}$.
  3. Applicazione del logaritmo: $\Lambda = n \ln(\frac{\lambda_1}{\lambda_0}) - (\lambda_1 - \lambda_0) \sum x_j$.
  4. Isolamento dei dati: Il test si riduce a confrontare $\sum x_j$ con una soglia.
  5. Determinazione della soglia $\eta'$ per il caso non-bayesiano: $\eta' = \frac{1}{\lambda_0 - \lambda_1} \ln \frac{\pi_0}{\pi_1} - \frac{\ln(\lambda_1/\lambda_0)}{\lambda_0 - \lambda_1}$.
- **Semplificazioni**: Il docente nota che nel caso bayesiano la soglia è nota, mentre nel caso di Neumann-Pearson va determinata tramite il vincolo di $\alpha$.

### Esercizio 4: Rumore di Laplace con Perturbazione (Spike)
- **Testo**: Segnale $z \sim \text{Laplace}(0)$ sotto $H_0$. Sotto $H_1$, $z = n + 4$ (dove $n$ è rumore).
- **Risoluzione Passo-Passo**:
  1. PDF sotto $H_0$: $f(z|H_0) = \frac{1}{2}e^{-|z|}$.
  2. PDF sotto $H_1$: $f(z|H_1) = \frac{1}{2}e^{-|z-4|}$.
  3. Analisi della zona critica $z \in (0, 4)$:
     - $|z| = z$
     - $|z-4| = 4-z$
     - Rapporto di verosimiglianza: $\frac{f(z|H_1)}{f(z|H_0)} = \frac{e^{-(4-z)}}{e^{-z}} = e^{z-4-z} = e^{-4}$.
  4. Analisi della zona $z > 4$:
     - $|z| = z$
     - $|z-4| = z-4$
     - Rapporto di verosimiglianza: $\frac{e^{-(z-4)}}{e^{-z}} = e^{-z+4+z} = e^4$.
  5. Analisi del valore $z = 4.5$: Questo valore potrebbe essere dovuto a una perturbazione di 4 + rumore 0.5, oppure a un rumore molto alto sotto $H_0$. La decisione dipende dalle probabilità a priori $\pi_0, \pi_1$.
- **Punto Critico**: Il docente mostra che se $\pi_1$ è molto piccola (perturbazione improbabile), un valore di 4.5 deve essere attribuito a $H_0$ (rumore alto) anche se "sembra" una perturbazione.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    *   **Confusione tra $\alpha$ e Confidenza**: Il docente chiarisce che "Confidence Level" non è sinonimo di "Confidenza" in senso medico; è il livello di affidabilità del test.
    *   **L'illusione dell'Ottimità**: Dichiarare sempre $H_1$ massimizza la potenza ma causa un "FAR Explosion" (esplosione del tasso di falsi allarmi).
- **Chiarimenti Metodologici**:
    *   **Distinzione tra Stima e Test**: Il test di ipotesi si chiede "è successo qualcosa?", la stima si chiede "qual è il valore del parametro nascosto?".
    *   **Robustezza**: Un algoritmo ottimo non è necessariamente robusto. La robustezza garantisce prestazioni soddisfacenti anche in caso di deviazione dalle ipotesi di progetto.
- **Punti Critici per l'Esame**:
    *   Il docente ha insistito sulla distinzione tra il caso bayesiano (soglia nota dai priori) e il caso di Neumann-Pearson (soglia determinata dal vincolo $\alpha$).
    *   Importanza della linearizzazione dei dati tramite il logaritmo del rapporto di verosimiglianza.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    *   Richiede una buona "cultura matematica" (integrazione e derivazione).
- **Consigli di Studio Espliciti**:
    *   **Non memorizzare, ma capire la logica**: Il docente sottolinea di non voler sentire "memoria ma logica".
    *   **Ordine delle Slide**: Seguire l'ordine logico delle slide è fondamentale per ricostruire il ragionamento correttamente.
    *   **Ottimizzazione**: Alcuni concetti avanzati (come i vincoli semidefiniti) potrebbero essere approfonditi in altri corsi di ottimizzazione.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- Informazione non menzionata nella lezione.