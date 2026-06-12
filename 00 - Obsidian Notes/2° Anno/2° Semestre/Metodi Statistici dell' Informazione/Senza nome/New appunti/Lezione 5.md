# SBOBINA - STATISTICA E PROBABILITÀ | Lezione su Media, Varianza, Convergenza e Strategie di Gioco

## 📌 METADATI ED ORGANIZZAZIONE DEL CORSO
- **Corso**: [Nome/Codice non specificati nella trascrizione]
- **Docente**: [Nome non specificato]
- **Orari e Aule**: Lezione erogata nella fascia 09:00 - 11:00.
- **Organizzazione Didattica**:
    - **Modalità di erogazione**: Lezione online (uso di lavagna elettronica condivisa).
    - **Accesso ai Materiali**: La lavagna utilizzata dal docente viene messa online al termine della lezione.
- **Avvisi, Calendario e Assenze**:
    - **Consigli pratici del docente**: Il docente sottolinea l'importanza della comprensione logica rispetto alla memoria meccanica.

---

## 🎯 SOMMARIO RAPIDO
1.  **Interpretazione di $\sigma$ e $\mu$**: Analisi della varianza come indicatore di aleatorietà.
2.  **Diseguaglianza di Markov**: Teoria, derivazione e implicazioni sulla concentrazione della probabilità.
3.  **Proprietà Lineari**: Formalizzazione della linearità della media e della covarianza per la scalatura.
4.  **Teoria della Convergenza**: Distinzione tra convergenza in media quadratica e in probabilità.
5.  **Interpretazione Frequentista**: Formalizzazione della probabilità come limite della frequenza di successo.
6.  **Analisi di Strategie di Gioco**: Applicazione pratica sulle strategie di puntata fissa e Martingala.

---

## 🔤 NOMENCLATURA E TERMINOLOGIA TECNICA
| Termine | Simbolo | Definizione e Contesto |
|---|---|---|
| Media Statistica | $\mathbb{E}[X]$ o $\mu_x$ | Indicatore del comportamento globale di una variabile aleatoria. |
| Deviazione Standard | $\sigma_x$ | Misura della dispersione dei dati rispetto alla media. |
| Varianza | $\sigma^2_x$ | Media quadratica degli scarti dalla media; misura della "non-aleatorietà". |
| Diseguaglianza di Markov | - | Relazione che limita la probabilità che una variabile non negativa ecceda un valore $\delta$. |
| Convergenza in Media Quadratica | - | Situazione in cui la norma dell'uguaglianza di $\mathbb{E}[(X_n - X)^2]$ tende a 0. |
| Convergenza in Probabilità | - | Situazione in cui la probabilità che la variabile sia distante dalla media tenda a 0. |
| Frequenza di Successo | $F$ | Rapporto tra numero di successi $N_A$ e numero totale di prove $n$. |
| Conteggio Bernoulli | $N_A$ | Variabile aleatoria che conta il numero di successi in $n$ prove indipendenti. |
| Martingala | - | Strategia di puntata in cui l'importo della scommessa viene raddoppiato dopo ogni perdita. |

---

## 📚 CONTENUTI TEORICI ED ESEMPI (ORDINE CRONOLOGICO)

### 1. Significato di $\sigma$ rispetto a $\mu$
- **Spiegazione Teorica**: La media $\mu_x$ è un buon indicatore del comportamento globale di una variabile aleatoria solo se la deviazione standard $\sigma_x$ è piccola rispetto a $\mu_x$.
    - Se $\sigma_x$ è piccola: La variabile aleatoria è "poco aleatoria" e la maggior parte della probabilità è concentrata attorno alla media.
    - Se $\sigma_x$ è significativa: La media rimane un indicatore del valore atteso, ma è possibile osservare con alta probabilità valori molto distanti da essa.
    - **Conclusione**: Una grande varianza implica una grande aleatorietà; una piccola varianza implica che la variabile si concentra sulla sua media.
- **Esempi Specifici Citati**:
    - *Esempio del portafoglio*: Se la deviazione standard è di 10€, la probabilità di avere almeno 90€ è del 90%. Se invece la deviazione standard è minima (es. $\sigma \approx 0.01$), la probabilità di avere tra 90€ e 110€ è prossima al 100% (99%).

### 2. Diseguaglianza di Markov
- **Spiegazione Teorica**: Data una variabile aleatoria non negativa $X$, la probabilità che essa ecceda un qualunque valore $\delta$ è minore o uguale al momento emesimo diviso $\delta$ alla potenza $m$.
- **Formule e Modelli Matematici**:
  $$P(X \ge \delta) \le \frac{\mathbb{E}[X]}{\delta}$$
- **Derivazione per la Deviazione Standard**:
  Considerando una variabile $X$ arbitraria di media $\mu_x$ e deviazione standard $\sigma_x$, definiamo una variabile non negativa $Y = |X - \mu_x|$. Applicando la diseguaglianza di Markov con $m=2$ e $\delta = k\sigma_x$:
  $$P(|X - \mu_x| \ge k\sigma_x) \le \frac{\mathbb{E}[|X - \mu_x|]^2}{(k\sigma_x)^2} = \frac{\sigma_x^2}{k^2 \sigma_x^2} = \frac{1}{k^2}$$
- **Interpretazione**: La probabilità di trovare $X$ a una distanza superiore a $k$ deviazioni standard dalla sua media è $\le \frac{1}{k^2}$. Equivalentemente, la probabilità di trovare $X$ vicino alla media (entro $k$ deviazioni standard) è $\ge 1 - \frac{1}{k^2}$.
- **Condizioni Tacite**: Valido solo per variabili non negative (nella forma generale) e richiede $\sigma_x > 0$.

### 3. Proprietà Lineari della Media e della Varianza
- **Linearità della Media**: Se $a$ e $b$ sono costanti reali:
  $$\mathbb{E}[ax + b] = a\mathbb{E}[x] + b$$
  *Ragionamento del docente*: $b$ è una costante non aleatoria, quindi $\mathbb{E}[b] = b$. $a$ è una costante deterministica, quindi esce dal segno diaspettativa.
- **Proprietà della Varianza**:
    1. **Invarianza per traslazione**: $\text{Var}(ax + b) = \text{Var}(ax)$. Lo spostamento $b$ non influenza la dispersione.
    2. **Covarianza per scalatura**: $\text{Var}(ax) = a^2\text{Var}(x)$. Il fattore di scala $a$ agisce quadraticamente.
- **Vincoli**: Se $x \ge 0$, allora $\mathbb{E}[x] \ge 0$. La varianza $\sigma^2_x$ è sempre $\ge 0$ poiché è la media di una quantità al quadrato (non negativa). Un risultato di varianza negativa è matematicamente impossibile.

### 4. Teorie della Convergenza
- **Relazione tra Convergenze**:
    - La **convergenza in media quadratica** implica la **convergenza in probabilità**.
    - La convergenza in probabilità **non** implica necessariamente la convergenza in media quadratica.
- **Definizioni**:
    - Convergenza in probabilità: $P(|X_n - X| > \epsilon) \to 0$ per ogni $\epsilon > 0$.
    - Convergenza in media quadratica: $\mathbb{E}[(X_n - X)^2] \to 0$.

### 5. Interpretazione Frequentista della Probabilità
- **Definizione**: La probabilità può essere introdotta come limite della frequenza di successo.
- **Formalizzazione**:
    - Siano $n$ prove indipendenti.
    - $N_A$ è il numero di volte in cui l'evento $A$ si verifica.
    - $F = \frac{N_A}{n}$ è la frequenza di successo.
- **Modellizzazione**:
    - $N_A$ è un **conteggio bernulliano** con parametri $n$ e $P(A) = p$.
    - $\mathbb{E}[N_A] = np$.
    - $\text{Var}(N_A) = np(1-p)$.
    - $\mathbb{E}[F] = \mathbb{E}[\frac{N_A}{n}] = \frac{np}{n} = p$.
    - $\text{Var}(F) = \text{Var}(\frac{N_A}{n}) = \frac{np(1-p)}{n^2} = \frac{p(1-p)}{n}$.
- **Limite**: Al crescere di $n \to \infty$, $\text{Var}(F) \to 0$. Ciò significa che $F$ converge in probabilità a $p$.

---

## 🔨 ESERCIZI SVOLTI E APPLICAZIONI NUMERICHE

### Esercizio 1: Analisi di due strategie di gioco (Suma $S$)
*Il giocatore possiede una somma $S$ e gioca a una scommessa con probabilità di vittoria $p$ (dove $a = 1-p$).*

#### Caso A: Strategia a puntata fissa (€1)
- **Descrizione**: Il giocatore punta 1€ alla volta finché non vince o finisce il denaro.
- **Variabile Aleatoria $X$**: Numero di puntate. Alfabeto $X \in \{1, 2, \dots, S\}$.
- **Distribuzione di Probabilità (PMF)**:
    - Per $k < S$: $P(X=k) = (1-p)^{k-1}p$ (perde $k-1$ volte e vince alla $k$-esima).
    - Per $k = S$: Il giocatore fa $S$ puntate se perde $S-1$ volte (e poi gioca l'ultima puntata indipendentemente dall'esito) oppure se perde $S$ volte.
    - *Semplificazione del docente*: Si può considerare l'evento "perde le prime $S-1$ volte".
    - $P(X=S) = (1-p)^{S-1}$.
- **Guadagno $G$**:
    - Se vince alla puntata $k$: $G = b - k$ (dove $b$ è il premio).
    - Se perde alla puntata $S$: $G = -S$.
- **Guadagno Medio $\mathbb{E}[G]$**:
    - $\mathbb{E}[G] = \sum_{k=1}^{S-1} (b-k) P(X=k) + (-S) P(X=S)$.
    - Calcolo limite per $S \to \infty$: $\mathbb{E}[G] \to \frac{b-1}{1-p}$.
- **Analisi Critica**: Se $b=36$ (rulette) e $p=1/37$, il guadagno è negativo, confermando il vantaggio del banco.

#### Caso B: Strategia Martingala (Raddoppio)
- **Descrizione**: Il giocatore raddoppia la puntata dopo ogni perdita.
- **Puntata alla $k$-esima prova**: $2^{k-1}$.
- **Vincolo di budget $S$**:
    - Somma delle puntate per arrivare alla $k$-esima: $\sum_{i=0}^{k-1} 2^i = 2^k - 1$.
    - Vincolo: $2^k - 1 \le S \implies k \le \log_2(S+1)$.
    - Il numero massimo di puntate è $x_{max} \approx \log_2(S)$.
- **Guadagno $G$**:
    - Se vince alla puntata $k$: $G = \text{Premio} - \text{Totale Speso} = b \cdot 2^{k-1} - (2^k - 1)$.
    - Se perde tutto: $G = -S$.
- **Analisi del limite**:
    - Se $S \to \infty$ (senza limite di puntata), il guadagno medio tende a infinito.
    - *Nota metodologica*: Il limite del guadagno medio non implica la convergenza in probabilità. La convergenza è un concetto temporale; il limite degli eventi non equivale al limite delle probabilità.

---

## 💡 AVVERTIMENTI, ERRORI COMUNI E COMPRENSIONE CRITICA
- ⚠️ **Errori e Confusioni Segnalate**:
    - Non confondere la convergenza in probabilità con la convergenza in media quadratica (non sono implicazioni mutue).
    - Attenzione alla definizione di $P(X=S)$ nell'esercizio della scommessa: deve essere chiaro che il giocatore si alza dal tavolo sia perché finisce il budget che perché vince l'ultima puntata.
- **Chiarimenti Metodologici**:
    - La media statistica è formalmente un **integrale di Lebesgue**, ma gode delle stesse proprietà dell'integrale di Riemann (linearità, uscita delle costanti).
    - L'indipendenza delle prove è fondamentale per la definizione frequentista classica, ma può essere indebolita a una "sintocità indipendente" (casi condizionati minori dei non condizionati).
- **Punti Critici per l'Esame**:
    - Ricapitolare tutte le proprietà della probabilità e della caratterizzazione delle variabili discrete.
    - Prepararsi al passaggio alle variabili continue per analogia.

---

## 📝 INFORMAZIONI E REQUISITI D'ESAME
- **Struttura della Prova**: Non menzionata nella lezione.
- **Propedeuticità e Prerequisiti**:
    - Richiede una buona "cultura matematica" di base.
- **Consigli di Studio Espliciti**:
    - Ripetere tutto quanto fatto sulla probabilità e sulla caratterizzazione delle variabili discrete.
    - Non perdere tempo con formule inutili; concentrarsi sulla comprensione logica degli esercizi (es. le strategie di gioco).

---

## 📚 BIBLIOGRAFIA E RIFERIMENTI CITATI
- **Esercizi Online**: Il docente ha indicato la presenza di una collezione di esercizi online (Esercizio stand, terzo della collezione).
- **Lavagna**: Disponibile online dopo la lezione.