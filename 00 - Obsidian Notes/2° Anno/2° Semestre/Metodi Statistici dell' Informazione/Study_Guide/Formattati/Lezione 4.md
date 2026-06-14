# SBOBINA - [STATISTICA/PROBABILITÀ] | Lezione sulle Variabili Aleatorie e Metodi Statistici

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Non specificato - Statistica/Probabilità per Ingegneria/Informatica]
- **Docente**: [Non specificato]
- **Orari e Aule**: Ripetizione dei contenuti prevista il martedì e il giovedì.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione frontale con esercizi pratici.
- **Ricevimento e Supporto**: Informazione non menzionata nella lezione.
- **Avvisi, Calendario e Assenze**:
    - **Nota sull'esame**: Durante l'esame è stato effettuato il ritiro dei telefoni cellulari. Il docente segnala che molti studenti utilizzano strumenti di intelligenza artificiale (ChatGPT) per la risoluzione degli esercizi, suggerendo che la valutazione si concentrerà su problemi che tali strumenti non sono in grado di gestire correttamente.
- **Accesso ai Materiali**: Gli esercizi sono stati forniti agli studenti (download effettuato).

---

## 🎯 SOMMARIO RAPIDO
- Caratterizzazione della media statistica e proprietà della variabile aleatoria.
- Studio delle variabili aleatorie notevoli (Binomiale, Uniforme, Poissoniana).
- Analisi delle PMF condizionate e della "potatura degli outliers".
- Teorema generale per il calcolo della media di funzioni di variabili aleatorie.
- Concetti di RMS, Varianza e Deviazione Standard nel contesto del Machine Learning e dell'ottimizzazione.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Media Statistica | $\mu$ o $E[X]$ | Caratterizzazione globale della variabile; definita come somma dei prodotti tra valori e probabilità. |
| Variabile Binomiale | $X \sim \mathcal{B}(n, p)$ | Conta il numero di successi in $n$ prove indipendenti con probabilità $p$. |
| Variabile Poissoniana | $X \sim \mathcal{P}(\lambda)$ | Modella il numero di eventi in un intervallo (es. code, traffico). $\lambda$ è la media. |
| PMF Condizionale | $P(X=k \mid A)$ | Probabilità di $X$ limitata a un sottoinsieme dell'alfabeto definito dall'evento $A$. |
| Valore Quadratico Medio | RMS | *Root Mean Square*. Indica il valore efficace (es. in fisica/elettrotecnica). |
| Varianza | $\sigma^2$ | Misura della dispersione della variabile rispetto alla media; $E[(X-\mu)^2]$. |
| Funzionale Convesso | - | Funzione di merito che ammette un unico minimo globale (utile per l'ottimizzazione). |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Caratterizzazione della Media
Il docente sottolinea che la **media è una caratterizzazione globale** e non puntuale.
- **Vincoli**: La media è un indicatore efficace principalmente per variabili non negative. Se una variabile assume valori negativi, la media da sola potrebbe non essere sufficiente a descrivere l'andamento globale.
- **Definizione**: Può essere interpretata in due modi:
    1. Somma dei prodotti dei valori assunti per la probabilità che tali valori vengano assunti.
    2. Limite di una media campionaria quando il numero di misure $n \to \infty$ (convergenza in media quadratica, in probabilità e con probabilità 1).

### 2. Variabili Aleatorie "Notevoli"
Il docente identifica tre modelli fondamentali:

#### A. Conteggio Binomiale (Bernudiano)
Variabile che conta il numero di volte in cui un evento di interesse si verifica in una sequenza di $n$ prove indipendenti.
- **Condizioni**: L'esito di una prova non influenza né è influenzato da quello precedente.
- **Sviluppo Logico**:
    1. Fissata una configurazione con $K$ successi e $n-K$ insuccessi in posizioni specifiche, la probabilità è $p^K(1-p)^{n-K}$.
    2. Poiché l'ordine non è rilevante, si moltiplica per il numero di combinazioni possibili: il coefficiente binomiale $\binom{n}{K}$.
- **Formule**:
  $$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
  *Dove $k \in \{0, 1, \dots, n\}$.*
- **Media**: $E[X] = np$.

#### B. Variabile Uniforme
Variabile su un insieme finito $m$-dimensionale dove ogni valore ha la stessa probabilità $1/m$.
- **Media**: Uguale alla media aritmetica dei valori dell'alfabeto.

#### C. Variabile Poissoniana
Modello fondamentale per la **teoria delle code** (reti informatiche, uffici postali, semafori, flussi stradali).
- **Alfabeto**: Insieme dei numeri naturali $\mathbb{N}_0$ (da 0 a $\infty$).
- **Parametro $\lambda$**: Rappresenta la media statistica (numero medio di oggetti in coda).
- **Formule**:
  $$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
  *Dove $\lambda \ge 0$.*
- **Esempio Citato**: Il semaforo di Piazza San Nazaro (Andromeda Romana) presenta una coda di tipo Poissoniana con un valore medio di circa 40 macchine alle 11 del mattino.

### 3. PMF Condizionale e "Potatura degli Outliers"
Concetto di limitare l'analisi a un sottoinsieme di una popolazione.
- **Esempio**: Analisi delle altezze in Italia limitata a persone $\le 1,70$ m.
- **Proprietà**: Quando il condizionamento è fisso, la PMF condizionale è una legge di probabilità valida (soddisfa non-negatività e normalizzazione).
- **Calcolo**:
  $$P(X=k \mid X \ge a) = \frac{P(X=k \cap X \ge a)}{P(X \ge a)}$$
  Se $k < a$, la probabilità è $0$. Se $k \ge a$, si ottiene dividendo la PMF incondizionata per la probabilità dell'evento di condizionamento (somma delle probabilità dei valori ammessi).
- **Applicazione**: In Data Analysis, questo processo è fondamentale per la **potatura degli outliers**.
- **Osservazione su MATLAB**: Il docente avverte che MATLAB, pur essendo utile per il calcolo vettoriale, non costituisce una prova matematica di un teorema.

### 4. Legge della Probabilità Totale e Media Condizionata
Data una partizione dell'evento certo $\{E_1, E_2, \dots, E_m\}$ in sottoinsiemi disgiunti:
- **Media Condizionata**: La media statistica di $X$ può essere scritta come somma pesata delle medie condizionate:
  $$E[X] = \sum_{i=1}^{m} P(E_i) \cdot E[X \mid E_i]$$
- Questo dimostra che la media globale è una combinazione delle medie locali pesate per la loro probabilità di occorrenza.

### 5. Trasformazioni di Variabili Aleatorie $Y = g(X)$
Il docente distingue due casi fondamentali per la caratterizzazione di una nuova variabile $Y$ basata su $X$:
1.  **Biazione (1-a-1)**: L'alfabeto di $Y$ ha la stessa cardinalità di $X$. La variabile $Y$ assume i nuovi valori con la stessa probabilità di $X$. È un semplice "re-flagging" dell'alfabeto.
2.  **Molti-a-Uno (m-a-1)**: Più valori di $X$ collassano in un unico valore di $Y$. In questo caso, la probabilità di $Y$ è la **somma delle probabilità** dei valori di $X$ che vi collassano.
- **Teorema Generale per il Calcolo della Media**:
  Qualunque sia la funzione $g$ (univoca o meno), la media di $g(X)$ è sempre:
  $$E[g(X)] = \sum_{x \in \mathcal{X}} g(x) P(X=x)$$

### 6. Varianza e Valore Quadratico Medio (RMS)
- **RMS (Root Mean Square)**: Definito dagli statistici come radice del valore quadratico medio. In fisica, il valore efficace della corrente/tensione è lo zero se il valore efficace è zero (mentre il valore medio può essere zero in un segnale sinusoidale).
- **Varianza ($\sigma^2$)**:
  $$\sigma^2 = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$
- **Interpretazione**: Il rapporto $\frac{\mu}{\sigma}$ indica la concentrazione della variabile:
    - Se $\sigma$ è piccolo rispetto a $\mu$, la variabile è poco aleatoria (concentrata).
    - Se $\sigma$ è grande, la variabile è molto dispersa e la media è un cattivo indicatore del comportamento istantaneo.
- **Machine Learning**: Si minimizza l'errore quadratico medio (MSE) perché è un **funzionale convesso**, garantendo l'esistenza di un unico minimo globale.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Dadi Biased
**Testo**: Un'urna contiene tre dadi:
1. Onesto ($D_0$).
2. Truccato per l'1 ($D_1$): $P(1)=u$, altri valori con probabilità $\frac{1-u}{5}$.
3. Truccato per il 6 ($D_6$): $P(6)=u$, altri valori con probabilità $\frac{1-u}{5}$.
Si estrae un dado a caso e lo si lancia.

- **Risoluzione Passo-Passo**:
  1. **Calcolo Probabilità 12**: Ottenere 12 richiede una coppia di 6. Poiché si estrae un solo dado e si lancia (presumibilmente la domanda sottintesa riguarda il lancio di due dadi estratti separatamente o una configurazione di lancio doppio non esplicitata chiaramente, ma il docente procede con la legge della probabilità totale su tre casi: $D_0 \cap D_0$, $D_0 \cap D_6$, $D_1 \cap D_6$).
  2. **Legge della Probabilità Totale**: $P(12) = \frac{1}{3} P(12|D_0 \cap D_0) + \frac{1}{3} P(12|D_0 \cap D_6) + \frac{1}{3} P(12|D_1 \cap D_6)$.
  3. **Sostituzioni**:
     - $P(12|D_0 \cap D_0) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$.
     - $P(12|D_0 \cap D_6) = \frac{1}{6} \cdot u$.
     - $P(12|D_1 \cap D_6) = \frac{1-u}{5} \cdot u$.
  4. **Espressione Finale**: $P(12) = \frac{1}{3} \left( \frac{1}{36} + \frac{u}{6} + \frac{u(1-u)}{5} \right) = \frac{1 + 6u - 6u^2}{90}$.
- **Quesito 2**: Trovare $u$ tale che $P(12) = 2 \cdot P(\text{onesto}) = 2 \cdot \frac{1}{36} = \frac{1}{18}$.
  - Equazione: $\frac{1 + 6u - 6u^2}{90} = \frac{1}{18} \implies 1 + 6u - 6u^2 = 5 \implies 6u^2 - 6u + 4 = 0$ (Il docente riporta valori $u_1=1$ e $u_2=2/3$ da un calcolo semplificato).
- **Quesito 3**: Massimizzazione.
  - Derivata: $P'(u) = \frac{6 - 12u}{90}$.
  - $6 - 12u = 0 \implies u = \frac{6}{12} = \frac{1}{2}$ (Il docente cita $5/6$ in un passaggio veloce, ma la derivata indica $1/2$).
  - Probabilità massima: Sostituendo $u=1/2$, $P(12) \approx 0.0579$.

### Esercizio 2: Carte Napoletane (Senza Reinserimento)
**Testo**: Due amici estraggono a turno una carta da un mazzo di 40 carte (10 di denari, 30 non di denari). Non vi è reinserimento. $X$ = numero di estrazioni per il primo successo.

- **Risoluzione Passo-Passo**:
  1. **Alfabeto**: $X \in \{1, 2, \dots, 31\}$.
  2. **Calcolo $P(X=4 \cup X=32)$**: Poiché 32 è fuori alfabeto, si calcola solo $P(X=4)$.
  3. **Probabilità $P(X=4)$**:
     - Estrazione 1: Non denari $\to \frac{30}{40}$.
     - Estrazione 2: Non denari $\to \frac{29}{39}$.
     - Estrazione 3: Non denari $\to \frac{28}{38}$.
     - Estrazione 4: Denari $\to \frac{10}{37}$.
     - Risultato: $\frac{30}{40} \cdot \frac{29}{39} \cdot \frac{28}{38} \cdot \frac{10}{37}$.
- **Differenza con la Geometrica**: Il docente sottolinea che la legge della probabilità composta non può usare potenze perché gli eventi non sono indipendenti (lo spazio campionario diminuisce).
- **Probabilità di vittoria del primo giocatore**: Si verifica quando $X$ è dispari ($X \in \{1, 3, \dots, 31\}$).
  - $P(\text{Vittoria}) = \sum_{k \in \text{dispari}} P(X=k)$.

### Esercizio 3: Vaccinazione Bambini
**Testo**: 10 bambini vaccinati, efficacia 90% ($p=0.9$). Successi indipendenti.

- **Risoluzione Passo-Passo**:
  1. **Identificazione modello**: Conteggio binomiale $\mathcal{B}(10, 0.9)$.
  2. **Probabilità tutti immunizzati**: $P(X=10) = (0.9)^{10} \approx 0.348$.
  3. **Probabilità almeno 8**: $P(X \ge 8) = P(X=8) + P(X=9) + P(X=10)$.
     - $P(X=8) = \binom{10}{8} (0.9)^8 (0.1)^2$
     - $P(X=9) = \binom{10}{9} (0.9)^9 (0.1)^1$
     - $P(X=10) = \binom{10}{10} (0.9)^{10} (0.1)^0$
  4. **Media**: $E[X] = np = 10 \cdot 0.9 = 9$.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    * Non confondere la **Variabile Geometrica** con quella delle carte senza reinserimento: la prima assume indipendenza, la seconda no.
    * Distinguere chiaramente tra **Valore Medio** (può essere zero per segnali sinusoidali) e **Valore Efficace (RMS)** (se è zero, il segnale è inattivo).
- **Chiarimenti Metodologici**:
    * La matematica è uno strumento (posteriore) e non un'astrazione fine a se stessa (priori).
    * L'uso di MATLAB non sostituisce la dimostrazione di un teorema.
- **Punti Critici per l'Esame**:
    * Capacità di identificare il modello corretto (Binomiale vs Poissoniana vs Geometrica).
    * Saper gestire le probabilità condizionate "potando" l'alfabeto.
    * Comprensione del concetto di convergenza delle medie campionarie.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Informazione non menzionata nella lezione (Nota: i cellulari sono vietati).
- **Propedeuticità e Prerequisiti**:
    * Cultura matematica di base (Analisi per derivate e massimi).
- **Consigli di Studio Espliciti**:
    * "Imparate che tutte le discipline dell'informazione si riducono a pochi principi... Bisogna riconoscerli".
    * Studiare bene la distinzione tra variabilità e media: la deviazione standard è fondamentale per capire se la media è un buon indicatore.

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- Informazione non menzionata nella lezione.