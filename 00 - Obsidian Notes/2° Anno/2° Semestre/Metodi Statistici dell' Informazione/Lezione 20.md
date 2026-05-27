# LEZIONE - STIMA BAYESIANA E MASSIMA VEROSIMIGLIANZA

**Corso:** Calcolo della Probabilità e Teoria dell'Informazione
**Programma:** Laurea Triennale in Informatica — II Semestre 2025–2026

---

## INTRODUZIONE METODOLOGICA

### Approccio Didattico del Corso

> **Nota del Docente:** Il metodo di insegnamento tradizionale prevede di iniziare in alto a sinistra della lavagna e terminare in basso a destra, senza mai cancellare. Questo approccio garantisce una traccia visiva del percorso logico seguito. Si evita la cancellazione anche per motivi pratici: il gesso produce polvere allergenica.

**Messaggio chiave:** Si tratta di **prepararsi** adeguatamente prima di affrontare i problemi specifici.

---

## DALLA CLASSIFICAZIONE ALLA STIMA

### Differenza Fondamentale

La stima si differenzia dalla classificazione in un punto cruciale:

| Aspetto | Classificazione | Stima |
|--------|-----------------|-------|
| **Stato della Natura** | M stati **discreti** incapsulati in variabile | Variabile **continua** |
| **Valori Possibili** | Numero finito | Infinito non numerabile |
| **Probabilità di Uguaglianza** | Definita | **Zero** (per variabili continue) |
| **Matrice dei Costi** | Utilizzata | Non applicabile |
| **Probabilità a Priori Discrete** | Utilizzate | Non applicabili |

### Conseguenza Teorica Critica

> **Principio Fondamentale:** Poiché la probabilità che due variabili continue assumano lo stesso valore è zero, il concetto di "errore" classico non ha senso nella stima.

**Implicazione:** Tutta la struttura teorica della classificazione (matrice dei costi, probabilità a priori discrete) deve essere **aggiornata e riformulata**.

---

## FIGURE DI MERITO NELLA STIMA

### Ridefinizione delle Grandezze di Valutazione

Anziché utilizzare la matrice dei costi discreta, nella stima si usano **figure di merito continue** basate su:
- Funzioni di costo arbitrarie
- Densità di probabilità a priori (non più discrete)
- Densità a posteriori del parametro

**Obiettivo:** Ottimizzare il sistema di stima sulla base di queste nuove grandezze.

---

## FRAMEWORK BAYESIANO PER LA STIMA

### Elementi Fondamentali

#### 1️⃣ A Priori del Parametro

- **Simbolo:** $f_\theta(\theta)$ — densità di probabilità a priori del parametro non noto
- **Significato:** Rappresenta la conoscenza iniziale sul parametro prima di osservare i dati
- **Natura:** Il parametro è trattato come una **variabile aleatoria**

#### 2️⃣ Osservabili

- **Simbolo:** $x^n$ — vettore di n osservazioni
- **Caratteristica:** Possono essere **continui o discreti**
  - Se discreti: descritti da PMF (Probability Mass Function)
  - Se continui: descritti da PDF (Probability Density Function)

#### 3️⃣ Densità Condizionale dei Dati

- **Simbolo:** $f_{x^n|\theta}(x^n|\theta)$ oppure $P_{x^n|\theta}(x^n|\theta)$ (caso discreto)
- **Significato:** Descrive come i dati si distribuiscono **dato un valore specifico del parametro**
- **Noto dal Modello:** La densità condizionale è **parte della specificazione del problema**

#### 4️⃣ Densità a Posteriori del Parametro

Una volta osservati i dati $x^n$, la densità a priori si aggiorna mediante il **Teorema di Bayes**:

**Caso Continuo:**
$$f_{\theta|x^n}(\theta|x^n) = \frac{f_{x^n|\theta}(x^n|\theta) \cdot f_\theta(\theta)}{f_{x^n}(x^n)}$$

**Caso Discreto:**
$$P_{\theta|x^n}(\theta|x^n) = \frac{P_{x^n|\theta}(x^n|\theta) \cdot P_\theta(\theta)}{P_{x^n}(x^n)}$$

**Dove:**
- **Numeratore:** Verosimiglianza × A Priori
- **Denominatore:** Evidenza (costante di normalizzazione)

---

## COSTO MEDIO BAYESIANO (RISCHIO BAYESIANO)

### Definizione Formale

Sia $c(\theta, \hat{\theta})$ una funzione di costo arbitraria che rappresenta il costo dell'errore quando il vero parametro è $\theta$ e la stima è $\hat{\theta}$.

Il **rischio bayesiano medio** è:

$$R = \mathbb{E}[c(\theta, \hat{\theta}(x^n))]$$

### Decomposizione Mediante Teorema della Media Condizionale

Applicando il teorema della media condizionale:

$$R = \mathbb{E}_{x^n}\left[\mathbb{E}_{\theta|x^n}[c(\theta, \hat{\theta}(x^n)) | x^n]\right]$$

**Significato:** La media generale si scompone come media della **media condizionale**.

### Integrale di Costo Condizionale

La media condizionale può essere scritta come integrale:

$$\mathbb{E}_{\theta|x^n}[c(\theta, \hat{\theta}(x^n)) | x^n] = \int c(\theta, \hat{\theta}(x^n)) f_{\theta|x^n}(\theta|x^n) d\theta$$

### Principio di Ottimalità

> **Teorema Fondamentale della Stima Bayesiana:** Per minimizzare il rischio bayesiano medio, la stima ottimale è quella che **minimizza il costo condizionale medio** per ogni realizzazione dei dati $x^n$.

**Formula:**
$$\hat{\theta}_{opt}(x^n) = \arg\min_{\hat{\theta}} \int c(\theta, \hat{\theta}) f_{\theta|x^n}(\theta|x^n) d\theta$$

---

## DUE FUNZIONI DI COSTO FONDAMENTALI

### 1️⃣ Costo Quadratico (MMSE - Minimum Mean Square Error)

#### Definizione della Funzione di Costo

$$c(\epsilon) = c(\theta - \hat{\theta}) = \epsilon^2$$

**Interpretazione:** L'errore è pesato al quadrato, penalizzando fortemente errori grandi.

#### Stimatore Ottimale

Minimizzando il costo condizionale medio:

$$\hat{\theta}_{MMSE}(x^n) = \mathbb{E}[\theta|x^n]$$

**Risultato Sorprendente:** Lo stimatore MMSE è semplicemente la **media condizionale del parametro data l'osservazione**.

#### Realizzazione della Stima

Applicando questo stimatore a un vettore di osservazioni specifico $x^n$:

$$\hat{\theta}_{MMSE} = \int \theta \cdot f_{\theta|x^n}(\theta|x^n) d\theta$$

---

### 2️⃣ Costo a Soglia (MAP - Maximum A Posteriori)

#### Definizione della Funzione di Costo

$$c(\epsilon) = \begin{cases} 0 & \text{se } |\epsilon| < \epsilon_0 \\ 1 & \text{se } |\epsilon| \geq \epsilon_0 \end{cases}$$

**Interpretazione:** Il costo è zero all'interno di una "zona di tolleranza" $\epsilon_0$, e aumenta bruscamente oltre.

#### Stimatore Ottimale (nel limite $\epsilon_0 \to 0$)

Minimizzando il costo condizionale medio:

$$\hat{\theta}_{MAP}(x^n) = \arg\max_{\theta} f_{\theta|x^n}(\theta|x^n)$$

**Significato:** Lo stimatore MAP è il **valore del parametro che massimizza la densità a posteriori**, cioè il valore più probabile a posteriori.

#### Proprietà Importante

Poiché $f_{\theta|x^n}(\theta|x^n) \propto f_{x^n|\theta}(x^n|\theta) \cdot f_\theta(\theta)$ (il denominatore è costante), massimizzare la posteriori è equivalente a massimizzare il prodotto:

$$\hat{\theta}_{MAP} = \arg\max_{\theta} \left[f_{x^n|\theta}(x^n|\theta) \cdot f_\theta(\theta)\right]$$

---

## ESEMPIO PRATICO: SORGENTE BINARIA SENZA MEMORIA

### Configurazione del Problema

**Sorgente:** Emette simboli binari {0, 1}
- Probabilità di emettere 1: $\theta$ (non nota)
- Probabilità di emettere 0: $1-\theta$
- **A Priori:** $\theta$ è uniformemente distribuito in [0,1], cioè $f_\theta(\theta) = 1$ per $\theta \in [0,1]$

**Osservazione:** $x^n = (x_1, x_2, \ldots, x_n)$ con $x_i \in \{0,1\}$

**Statistica Sufficiente:** $w_H(x^n)$ = numero di 1 nella sequenza

### Verosimiglianza

$$P_{x^n|\theta}(x^n|\theta) = \theta^{w_H(x^n)} (1-\theta)^{n-w_H(x^n)}$$

### Stima MMSE

Applicando il teorema della media condizionale:

$$\hat{\theta}_{MMSE} = \mathbb{E}[\theta|x^n]$$

Calcolo (con a priori uniforme e verosimiglianza binomiale):

$$\hat{\theta}_{MMSE} = \frac{w_H(x^n) + 1}{n + 2}$$

**Osservazione:** Lo stimatore è **leggermente polarizzato** (biased) in campioni finiti, ma diventa **asintoticamente corretto** per $n \to \infty$.

### Stima MAP

Massimizzando la posteriori (con a priori uniforme):

$$\hat{\theta}_{MAP} = \frac{w_H(x^n)}{n}$$

**Osservazione:** Questo coincide con la **frequenza campionaria** di 1 nella sequenza.

#### Confronto MAP vs MMSE

| Proprietà | MAP | MMSE |
|-----------|-----|------|
| **Formula** | $w_H / n$ | $(w_H + 1) / (n + 2)$ |
| **Al finito** | Non polarizzato | Polarizzato |
| **Asintoticamente** | Non polarizzato | Non polarizzato |
| **Convergenza** | Più veloce | Più lenta inizialmente |

---

## VALUTAZIONE DELLE PRESTAZIONI DELLO STIMATORE

### 1️⃣ Non-Polarizzazione (Unbiasedness)

#### Definizione

Uno stimatore $\hat{\theta}(x^n)$ è **non-polarizzato** se:

$$\mathbb{E}[\hat{\theta}(x^n) | \theta] = \theta$$

**Interpretazione:** La media dello stimatore, calcolata su tutte le possibili realizzazioni del campione, coincide con il vero valore del parametro.

#### Significato Pratico

- **Se non-polarizzato:** Non introduce errore sistematico medio
- **Se polarizzato:** C'è una deviazione sistematica che va sempre nello stesso verso (sopra o sotto il vero valore)

#### Avvertenza

La non-polarizzazione **non garantisce che lo stimatore sia buono**, perché:
- Un errore di +2000% nel 50% dei casi e -2000% nel 50% dei casi ha media zero
- Nonostante ciò, è uno stimatore terrible

**Conclusione:** La media non è un buon indicatore della variabilità della stima.

---

### 2️⃣ Errore Quadratico Medio (MSE)

#### Definizione

$$MSE = \mathbb{E}[(\hat{\theta}(x^n) - \theta)^2]$$

**Interpretazione:** Valore quadratico medio della differenza tra stima e parametro vero.

#### Decomposizione per Stimatori Non-Polarizzati

Se lo stimatore è non-polarizzato:

$$MSE = \text{Var}[\hat{\theta}(x^n)]$$

**Perché:** Il bias è nullo, quindi la varianza coincide con l'MSE.

---

### 3️⃣ Convergenza Asintotica

#### Convergenza in Media Quadratica

Se $\lim_{n \to \infty} MSE = 0$, allora l'errore $E = \hat{\theta}(x^n) - \theta$ ha varianza asintoticamente nulla.

**Significato:** La variabile aleatoria errore converge a zero in media quadratica, il che implica:

$$\lim_{n \to \infty} \text{Var}[E] = 0 \implies \text{Convergenza a costante deterministica (zero)}$$

#### Consistenza in Media Quadratica

> **Definizione:** Uno stimatore si dice **consistente in media quadratica** se $\lim_{n \to \infty} MSE = 0$.

**Proprietà:** Implica convergenza in probabilità (per la disuguaglianza di Chebyshev):

$$P(|\hat{\theta} - \theta| > \epsilon) \to 0 \text{ per } n \to \infty$$

#### Consistenza in Probabilità

> **Definizione:** Uno stimatore è **consistente in probabilità** (o debolmente consistente) se la probabilità di osservare deviazioni dal vero valore maggiori di $\epsilon$ va a zero al crescere di $n$.

**Relazione:** Consistenza in media quadratica ⟹ Consistenza in probabilità, ma non viceversa.

#### Consistenza Forte

Esiste anche un concetto di **consistenza forte** (convergenza quasi certa), più restrittivo.

---

## VERSO LA STIMA NON-BAYESIANA

### Il Caso dell'A Priori Sconosciuto

#### Situazione Comune nella Pratica

Spesso **non siamo in grado di fornire una densità a priori** del parametro. In questi casi:

- Il parametro $\theta$ è trattato come una **variabile deterministica non nota**, non aleatoria
- Non si può parlare di densità a priori o posteriori nel senso bayesiano
- Si adotta un **approccio frequentista** (o non-bayesiano)

#### Quando Accade?

**Esempio Tecnologico: Sincronizzazione nel 5G**

**Scenario:** Trasmissione di un segnale da sorgente a destinazione su canale 5G

1. **Conversione del segnale:** La voce (continua) viene convertita in sequenza binaria via quantizzazione vettoriale (come negli MP3)

2. **Modulazione:** La stringa binaria modula un'oscillazione cosinusoidale:
   $$s(t) = A \cos(2\pi f t + \phi)$$
   dove $f$ è la frequenza portante (2-70 GHz per il 5G)

3. **Trasmissione:** Il segnale viaggia attraverso il canale radio

4. **Ricezione con Phase Shift:** A causa del cammino percorso e della mancanza di visibilità diretta (non Line-of-Sight), il segnale ricevuto è:
   $$r(t) = A \cos(2\pi f t + \phi + \Delta\phi)$$
   dove $\Delta\phi$ è uno **shift di fase ignoto e deterministico**

#### Perché Non C'è A Priori?

- **La fase è deterministica** (non aleatoria)
- **È completamente sconosciuta:** Non sappiamo il cammino esatto percorso dal segnale
- **Dipende dalla posizione relativa ricevitore-trasmettitore** che varia continuamente
- **Varia a ogni frazione di secondo:** Impossibile fornire una distribuzione a priori significativa
- **Lunghezza d'onda piccolissima:** Uno spostamento di pochi millimetri causa variazioni di fase enormi

**Processo di Recupero:** Questa procedura si chiama **sincronizzazione di fase** (phase synchronization)

**Problema Analogo:** Anche nella sincronizzazione di simbolo, la **durata dell'intervallo di bit** è sconosciuta e deterministica, senza a priori definibile.

---

## ROBUSTEZZA E SCELTA DELL'A PRIORI

### Trade-off Pratico nella Scienza dell'Informazione

#### Scenario 1: Fornire un A Priori Specifico

**Vantaggio:** Si ottiene un sistema ottimizzato per quello specifico a priori

**Rischio:** Se il vero a priori **devia da quello supposto**:
- Le prestazioni si **degradano** significativamente
- Il sistema diventa **non robusto**
- Il valore ottimo viene perso

#### Scenario 2: Assumere il Caso Peggiore

**Vantaggio:** Si lavora nel **caso conservativo**
- Il sistema è robusto a variazioni dell'a priori
- Le prestazioni non crollano

**Svantaggio:** Prestazioni generalmente subottimali rispetto al caso ideale

#### Conclusione Pratica

> In molte applicazioni di comunicazione e processing del segnale, quando l'a priori è **veramente ignoto** o **altamente incerto**, si preferisce lavorare nel **regime di massima incertezza** per garantire robustezza, anche se questo significa rinunciare a ottimalità teorica.

---

## STIMA DI MASSIMA VEROSIMIGLIANZA (ML)

### Definizione Formale

Quando $\theta$ è un **parametro deterministico non noto**, non possiamo usare la metodologia bayesiana classica.

In questo caso, definiamo lo **stimatore di Massima Verosimiglianza**:

#### Caso Continuo

$$\hat{\theta}_{ML} = \arg\max_{\theta} f_{x^n|\theta}(x^n|\theta)$$

#### Caso Discreto

$$\hat{\theta}_{ML} = \arg\max_{\theta} P_{x^n|\theta}(x^n|\theta)$$

**Interpretazione:** La stima ML è il valore del parametro che **rende massima la probabilità (o densità) dei dati osservati**.

### Equivalenza con MAP nel Limite di A Priori Uniforme

#### Osservazione Cruciale

La stima ML è **esattamente equivalente** alla stima MAP quando:
- L'a priori è **uniforme** (costante) su tutto il dominio di $\theta$
- $f_\theta(\theta) = \text{costante}$ ⟹ indipendente da $\theta$

**Perché:** Massimizzare $f_{\theta|x^n}(\theta|x^n) \propto f_{x^n|\theta}(x^n|\theta) \cdot f_\theta(\theta)$ diventa equivalente a massimizzare solo $f_{x^n|\theta}(x^n|\theta)$ quando $f_\theta(\theta)$ è costante.

#### Interpretazione Bayesiana

> **Concetto:** La stima ML rappresenta il **limite di una stima MAP quando la densità a priori riflette completa ignoranza** (massima incertezza) sul parametro.

---

## ESEMPIO: STIMA DEL PARAMETRO BINOMIALE

### Setup del Problema

**Osservazione:** Sequenza binaria di n bit

**Statistica Sufficiente:** $w_H$ = peso di Hamming (numero di 1)

**Verosimiglianza:**
$$P_{x^n|\theta}(x^n|\theta) = \theta^{w_H} (1-\theta)^{n-w_H}$$

### Derivazione della Stima ML

#### Passo 1: Logaritmo della Verosimiglianza

$$\Lambda = \log P = w_H \log \theta + (n-w_H) \log(1-\theta)$$

#### Passo 2: Derivata Rispetto a $\theta$

$$\frac{d\Lambda}{d\theta} = \frac{w_H}{\theta} - \frac{n-w_H}{1-\theta}$$

#### Passo 3: Annullare la Derivata

$$\frac{w_H}{\theta} - \frac{n-w_H}{1-\theta} = 0$$

$$w_H (1-\theta) = (n-w_H) \theta$$

$$w_H - w_H \theta = n\theta - w_H \theta$$

$$w_H = n\theta$$

#### Risultato Finale

$$\hat{\theta}_{ML} = \frac{w_H}{n}$$

**Interpretazione:** Lo stimatore ML della probabilità di 1 è la **frequenza relativa di 1 nel campione**.

---

### Proprietà dello Stimatore ML per il Parametro Binomiale

#### Calcolo della Media

La media dello stimatore ML è:

$$\mathbb{E}[\hat{\theta}_{ML}] = \mathbb{E}\left[\frac{w_H}{n}\right] = \frac{1}{n}\mathbb{E}[w_H] = \frac{n\theta}{n} = \theta$$

**Conclusione:** Lo stimatore ML è **non-polarizzato**.

#### Calcolo della Varianza

$$w_H \sim \text{Binomiale}(n, \theta) \implies \text{Var}[w_H] = n\theta(1-\theta)$$

Quindi:

$$\text{Var}[\hat{\theta}_{ML}] = \frac{1}{n^2} \text{Var}[w_H] = \frac{\theta(1-\theta)}{n}$$

#### Consistenza

Poiché:
- Lo stimatore è non-polarizzato
- La varianza va a zero quando $n \to \infty$

**Conclusione:** Lo stimatore ML è **consistente in media quadratica** e quindi anche **consistente in probabilità**.

---

## PROPRIETÀ GENERALI DEGLI STIMATORI ML

### Liste delle Proprietà Fondamentali

Gli stimatori di massima verosimiglianza godono di proprietà straordinarie:

| Proprietà | Descrizione | Sempre Vera? |
|-----------|------------|-------------|
| **Asintoticamente Non-Polarizzato** | Per $n \to \infty$, il bias va a zero | ✅ Sempre |
| **Consistente (Debole)** | Convergenza in probabilità | ✅ Sempre |
| **Non Necessariamente Consistente (Media Quadratica)** | Potrebbe non convergere in media quadratica | ❌ Non sempre |
| **Efficiente (al finito)** | Raggiunge il limite di Cramér-Rao | ❌ Talvolta |
| **Asintoticamente Efficiente** | Raggiunge il limite di Cramér-Rao per $n \to \infty$ | ✅ Sempre |
| **Invariante rispetto a Trasformazioni** | Se $g$ è invertibile: $\hat{g(\theta)}_{ML} = g(\hat{\theta}_{ML})$ | ✅ Sempre |

---

## ESEMPIO: STIMA DELLA MEDIA DI UNA GAUSSIANA

### Setup

**Osservazione:** $x^n = (x_1, \ldots, x_n)$ con $x_i \sim \mathcal{N}(\mu, \sigma_0^2)$ i.i.d.

- Media: $\mu$ (non nota)
- Varianza: $\sigma_0^2$ (nota)

### Densità di Probabilità Congiunta

$$f_{x^n|\mu}(x^n|\mu) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma_0^2}} \exp\left(-\frac{(x_i-\mu)^2}{2\sigma_0^2}\right)$$

$$= \frac{1}{(2\pi\sigma_0^2)^{n/2}} \exp\left(-\frac{1}{2\sigma_0^2}\sum_{i=1}^{n}(x_i-\mu)^2\right)$$

### Logaritmo della Verosimiglianza

$$\Lambda = -\frac{n}{2}\log(2\pi\sigma_0^2) - \frac{1}{2\sigma_0^2}\sum_{i=1}^{n}(x_i-\mu)^2$$

### Derivata rispetto a $\mu$

$$\frac{d\Lambda}{d\mu} = -\frac{1}{\sigma_0^2}\sum_{i=1}^{n}(x_i-\mu) \cdot (-1) = \frac{1}{\sigma_0^2}\sum_{i=1}^{n}(x_i-\mu)$$

### Annullamento della Derivata

$$\sum_{i=1}^{n}(x_i-\mu) = 0$$

$$\sum_{i=1}^{n}x_i = n\mu$$

### Risultato Finale

$$\hat{\mu}_{ML} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

**Conclusione:** Lo stimatore ML della media è la **media campionaria**, non sorprendentemente.

### Proprietà

- **Non-polarizzato:** $\mathbb{E}[\hat{\mu}_{ML}] = \mu$
- **Varianza:** $\text{Var}[\hat{\mu}_{ML}] = \frac{\sigma_0^2}{n}$
- **Consistente in media quadratica:** MSE $\to 0$ quando $n \to \infty$

---

## ESEMPIO: STIMA DELLA VARIANZA

### Setup

Stesso modello gaussiano, ma ora stimiamo **anche la varianza** $\sigma^2$ (media $\mu$ supposta incognita).

### Logaritmo della Verosimiglianza

$$\Lambda = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i-\mu)^2$$

### Derivata rispetto a $\sigma^2$

$$\frac{d\Lambda}{d(\sigma^2)} = -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2}\sum_{i=1}^{n}(x_i-\mu)^2$$

$$= -\frac{n}{2\sigma^2} + \frac{1}{2\sigma^4}\sum_{i=1}^{n}(x_i-\mu)^2$$

### Annullamento della Derivata

$$\frac{n}{2\sigma^2} = \frac{1}{2\sigma^4}\sum_{i=1}^{n}(x_i-\mu)^2$$

$$n\sigma^2 = \sum_{i=1}^{n}(x_i-\mu)^2$$

### Risultato Finale

$$\hat{\sigma}^2_{ML} = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2$$

---

## INVARIANZA DELLO STIMATORE ML

### Principio Fondamentale

> **Teorema:** Se $\hat{\theta}_{ML}$ è lo stimatore ML di $\theta$, e $g$ è una funzione arbitraria, allora lo stimatore ML di $g(\theta)$ è:
>
> $$\hat{g(\theta)}_{ML} = g(\hat{\theta}_{ML})$$

**Significato:** Lo stimatore ML **commuta con trasformazioni arbitrarie**.

### Applicazione: Stima di $\sigma$ da $\sigma^2$

Se vogliamo stimare la **deviazione standard** $\sigma$ (non la varianza $\sigma^2$):

$$\hat{\sigma}_{ML} = \sqrt{\hat{\sigma}^2_{ML}} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2}$$

Questo segue automaticamente dal principio di invarianza, con $g(x) = \sqrt{x}$.

---

## LIMITE DI CRAMÉR-RAO (CRAMÉR-RAO BOUND)

### Introduzione al Concetto

**Domanda Fondamentale:** Esiste un limite teorico alla precisione di uno stimatore?

**Risposta:** Sì. Esiste un limite inferiore alla varianza di qualunque stimatore non-polarizzato, detto **Limit di Cramér-Rao**.

### Teorema di Cramér-Rao

Per uno stimatore **non-polarizzato** $\hat{\theta}$ di un parametro deterministico $\theta$:

$$\text{Var}[\hat{\theta}] \geq \frac{1}{I_n(\theta)}$$

dove $I_n(\theta)$ è l'**Informazione di Fischer** del problema di stima.

### Informazione di Fischer

L'informazione di Fischer è definita come:

$$I_n(\theta) = -\mathbb{E}\left[\frac{\partial^2 \log f_{x^n|\theta}(x^n|\theta)}{\partial \theta^2}\right]$$

oppure, equivalentemente:

$$I_n(\theta) = \mathbb{E}\left[\left(\frac{\partial \log f_{x^n|\theta}(x^n|\theta)}{\partial \theta}\right)^2\right]$$

**Interpretazione:** Misura la **curvatura della funzione di verosimiglianza** e quindi quanta **informazione i dati forniscono** sul parametro.

### Proprietà dell'Informazione di Fischer

- **Dipende dalla taglia del campione $n$:** $I_n(\theta) = n \cdot I_1(\theta)$
- **Dipende dal parametro $\theta$** (non sempre costante)
- **Aumenta con n:** Più dati ⟹ più informazione ⟹ stima più precisa

---

## STIMATORE EFFICIENTE

### Definizione

> **Stimatore Efficiente:** Uno stimatore non-polarizzato si dice **efficiente** se la sua varianza **coincide** con il limite di Cramér-Rao:
>
> $$\text{Var}[\hat{\theta}] = \frac{1}{I_n(\theta)}$$

**Significato:** È lo stimatore più preciso possibile per quel problema.

### Stimatore Asintoticamente Efficiente

> **Stimatore Asintoticamente Efficiente:** Uno stimatore si dice asintoticamente efficiente se l'uguaglianza nel limite di Cramér-Rao vale per $n \to \infty$:
>
> $$\lim_{n \to \infty} \text{Var}[\hat{\theta}] = \lim_{n \to \infty} \frac{1}{I_n(\theta)}$$

**Interpretanza:** Al crescere del campione, lo stimatore diventa sempre più preciso, raggiungendo il limite teorico.

---

## RELAZIONE TRA ML E EFFICIENZA

### Risultato Sorprendente

#### Affermazione 1: ML Non È Necessariamente Efficiente al Finito

La stima ML **può non** raggiungere il limite di Cramér-Rao per valori finiti di $n$.

#### Affermazione 2: Se ML Non È Efficiente, Nessuno Lo È

Se lo stimatore ML non raggiunge il limite di Cramér-Rao per un certo problema, **nessun altro stimatore può raggiungerlo**.

**Implicazione:** La stima ML è in qualche senso "il meglio che si può fare".

#### Affermazione 3: ML È Asintoticamente Sempre Efficiente

**Sempre** vale:
$$\lim_{n \to \infty} \text{Var}[\hat{\theta}_{ML}] = \lim_{n \to \infty} \frac{1}{I_n(\theta)}$$

#### Conclusione Pratica

> Per problemi di stima non-bayesiani, **usare sempre lo stimatore ML**. È garantito essere il migliore (o tra i migliori) sia al finito che asintoticamente.

---

## ESEMPIO NUMERICO: EFFICIENZA DEL PARAMETRO BINOMIALE

### Setup Repetizione

**Parametro:** $\theta$ (probabilità di 1 in sorgente binaria)

**Osservazione:** Peso di Hamming $w_H$ di $n$ bit

**Stimatore ML:** $\hat{\theta}_{ML} = \frac{w_H}{n}$

**Varianza dello Stimatore ML:**
$$\text{Var}[\hat{\theta}_{ML}] = \frac{\theta(1-\theta)}{n}$$

### Calcolo dell'Informazione di Fischer

#### Passo 1: Logaritmo della Verosimiglianza

$$\log P = w_H \log \theta + (n-w_H) \log(1-\theta)$$

#### Passo 2: Prima Derivata

$$\frac{\partial \log P}{\partial \theta} = \frac{w_H}{\theta} - \frac{n-w_H}{1-\theta}$$

#### Passo 3: Seconda Derivata

$$\frac{\partial^2 \log P}{\partial \theta^2} = -\frac{w_H}{\theta^2} - \frac{n-w_H}{(1-\theta)^2}$$

#### Passo 4: Calcolo dell'Informazione di Fischer

$$I_n(\theta) = -\mathbb{E}\left[-\frac{w_H}{\theta^2} - \frac{n-w_H}{(1-\theta)^2}\right]$$

$$= \mathbb{E}\left[\frac{w_H}{\theta^2} + \frac{n-w_H}{(1-\theta)^2}\right]$$

$$= \frac{\mathbb{E}[w_H]}{\theta^2} + \frac{\mathbb{E}[n-w_H]}{(1-\theta)^2}$$

Poiché $\mathbb{E}[w_H] = n\theta$ e $\mathbb{E}[n-w_H] = n(1-\theta)$:

$$I_n(\theta) = \frac{n\theta}{\theta^2} + \frac{n(1-\theta)}{(1-\theta)^2} = \frac{n}{\theta} + \frac{n}{1-\theta} = \frac{n}{\theta(1-\theta)}$$

### Limite di Cramér-Rao

$$\text{Var}[\hat{\theta}] \geq \frac{1}{I_n(\theta)} = \frac{\theta(1-\theta)}{n}$$

### Verifica di Efficienza

**Varianza dello stimatore ML:** $\frac{\theta(1-\theta)}{n}$

**Limite di Cramér-Rao:** $\frac{\theta(1-\theta)}{n}$

**Conclusione:** Lo stimatore ML raggiunge esattamente il limite! È **efficiente**.

---

## RIEPILOGO FINALE DELLA LEZIONE

### Tre Risultati Cruciali

#### 1️⃣ Dalla Bayesian alla Non-Bayesian

Quando non conosciamo l'a priori del parametro (situazione comune in telecomunicazioni e processing del segnale), il parametro diventa una **variabile deterministica non nota**.

In questo regime, la metodologia bayesiana non si applica. Invece, usiamo il framework di **massima verosimiglianza**.

#### 2️⃣ Massima Verosimiglianza È Il Gold Standard

Lo stimatore ML è:
- **Asintoticamente non-polarizzato** (sempre)
- **Consistente in probabilità** (sempre)
- **Asintoticamente efficiente** (sempre)
- **Invariante rispetto a trasformazioni** (sempre)
- **Talvolta efficiente al finito** (non garantito, ma quando non lo è, nessun altro lo può essere)

#### 3️⃣ Efficienza e Limite di Cramér-Rao

Per ogni problema di stima esiste un **limite teorico** alla precisione (varianza) di uno stimatore non-polarizzato. Questo limite è l'**inverso dell'Informazione di Fischer**.

Lo stimatore ML è il più vicino a questo limite, e lo raggiunge asintoticamente.

---

## OSSERVAZIONI DIDATTICHE FINALI

### Sulla Struttura del Corso

- Abbiamo passato da stima **bayesiana** (quando l'a priori è noto) a stima **non-bayesiana** (quando non lo è)
- Entrambe le metodologie sono importanti e complementari
- Nel prossimo incontro approfondiremo la dimostrazione del limite di Cramér-Rao
- Seguiranno esercizi numerici e applicazioni

### Prospettive Future

- **Stima lineare MMSE:** Caso speciale di grande importanza pratica
- **Teoria dell'Informazione:** Misure di incertezza e compressione dei dati
- **Test statistici:** Decisioni su parametri basate su osservazioni

### Consiglio Pratico

Per i vostri studi e la vostra carriera:
- Padroneggiare la **massima verosimiglianza** è essenziale
- Comprendere quando **applicare quale metodo** è critico
- Gli stimatori ML vanno bene "sempre" se il modello è corretto
- Quando il modello è errato, la robustezza diventa più importante dell'ottimalità

