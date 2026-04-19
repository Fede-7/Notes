---
date: 2026-04-16
corso: Metodi Statistici dell'Informazione
lezione: "Variabili continue avanzate — Diseguaglianze, Distribuzione Uniforme ed Esponenziale"
tags: [MSI, variabili-continue, markov, chebyshev, distribuzione-uniforme, distribuzione-esponenziale, varianza]
---

> [!question] Argomenti trattati
> - Proprietà di varianza nel cambio di scala: Var(aX + b)
> - Diseguaglianza di Markov (caso continuo)
> - Diseguaglianza di Chebyshev (interpretazione geometrica)
> - Distribuzione uniforme e media
> - Distribuzione esponenziale: parametri e applicazioni
> - Quantizzazione e theory of estimation
> - Separazione tra descrizione algebrica e interpretazione probabilistica

---

## 1. Trasformazioni di varianza

> [!info] Teorema: Varianza di una trasformazione lineare
> Se $X$ è una variabile aleatoria e $Y = aX + b$, allora:
> $$\text{Var}(aX + b) = a^2 \cdot \text{Var}(X)$$
>
> **Dimostrazione:** La costante $b$ non influisce sulla dispersione (traslazione), mentre il fattore $a$ scala la varianza per il suo quadrato.

### Interpretazione

- Se $a = 2$: la varianza quadruplica (scala del 4x)
- Se $a = 1/2$: la varianza si riduce a 1/4
- Se $b = 100$: non cambia nulla (è solo una traslazione)

> [!warning] Errore comune
> Confondere $\text{Var}(aX)$ con $a \cdot \text{Var}(X)$.
> 
> **CORRETTO:** $\text{Var}(aX) = a^2 \cdot \text{Var}(X)$ (il quadrato è essenziale!)

---

## 2. Diseguaglianza di Markov

> [!info] Formulazione (caso continuo)
> Sia $X$ una variabile aleatoria **non negativa** e $\delta > 0$. Allora:
> $$P(X \geq \delta) \leq \frac{E[X]}{\delta}$$
>
> Questa diseguaglianza fornisce un **limite superiore** alla probabilità che $X$ superi una soglia, usando solo la media.

### Derivazione intuitiva

Supponiamo di dividere il supporto di $X$ in intervalli di ampiezza $\delta$:

**Per la variabile discreta approssimata:**
$$E[X_\delta] = \sum_i x_i \cdot P(X_\delta = x_i) = \sum_i x_i \cdot f_X(x_i) \cdot \delta$$

**Considerando solo gli intervalli dove $X \geq \delta$:**
$$E[X] \geq \sum_{x \geq \delta} x \cdot f_X(x) \cdot \delta \geq \sum_{x \geq \delta} \delta \cdot f_X(x) \cdot \delta = \delta^2 \sum_{x \geq \delta} f_X(x) = \delta^2 \cdot P(X \geq \delta)$$

**Quindi:**
$$P(X \geq \delta) \leq \frac{E[X]}{\delta}$$

> [!warning] Limitazione della diseguaglianza
> È un **limite molto approssimato**. Spesso non è stretto (non fornisce informazioni precise).
> Esempio: se $E[X] = 10$ e $\delta = 100$, otteniamo $P(X \geq 100) \leq 0.1$, ma la probabilità reale potrebbe essere quasi nulla.

> [!tip] Quando è utile
> Quando si conosce **solo la media** e nulla della distribuzione. Per distribuzioni specifiche, si ottengono limiti migliori.

---

## 3. Diseguaglianza di Chebyshev

> [!info] Teorema di Chebyshev
> Sia $Y$ una variabile aleatoria con media $\mu$ e varianza $\sigma^2$. Allora, per ogni $k > 0$:
> $$P(|Y - \mu| \geq k\sigma) \leq \frac{1}{k^2}$$
>
> **Equivalentemente:**
> $$P(|Y - \mu| < k\sigma) \geq 1 - \frac{1}{k^2}$$

### Derivazione da Markov

Applicando Markov a $Z = (Y - \mu)^2$ (non negativa):

$$P(|Y - \mu|^2 \geq (k\sigma)^2) \leq \frac{E[(Y - \mu)^2]}{(k\sigma)^2} = \frac{\sigma^2}{k^2\sigma^2} = \frac{1}{k^2}$$

Prendendo la radice quadrata: $P(|Y - \mu| \geq k\sigma) \leq \frac{1}{k^2}$

### Interpretazione pratica

| k | Probabilità massima | Interpretazione |
|---|-----|-----|
| k=1 | P(scostamento ≥ 1σ) ≤ 1 | Non informativo |
| k=2 | P(scostamento ≥ 2σ) ≤ 1/4 | Al massimo il 25% dei dati oltre 2σ |
| k=3 | P(scostamento ≥ 3σ) ≤ 1/9 ≈ 0.11 | Al massimo l'11% dei dati oltre 3σ |
| k=10 | P(scostamento ≥ 10σ) ≤ 1/100 | Al massimo l'1% dei dati |

> [!abstract] Ricordare
> **La coppia (media, deviazione standard) fornisce una caratterizzazione globale** della variabile aleatoria.
> Se conosci $\mu$ e $\sigma$, sai che:
> - Il 75% dei dati cade entro 2 deviazioni standard
> - Il 99% dei dati cade entro 10 deviazioni standard
> 
> Questo vale **indipendentemente dalla forma della distribuzione**.

---

## 4. Distribuzione Uniforme U(a,b)

> [!info] Definizione
> Una variabile aleatoria continua $X$ è **uniforme sull'intervallo [a,b]** se:
> $$f_X(x) = \begin{cases} \frac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

### Funzione di distribuzione cumulativa (CDF)

$$F_X(x) = \begin{cases} 0 & x < a \\ \frac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

La CDF è una **rampa lineare** da 0 a 1.

### Valore atteso

$$E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{a + b}{2}$$

> [!tip] Ricordare per l'esame
> **La media della uniforme è il punto medio dell'intervallo.**
> Non serve calcolare l'integrale: basta ricordare questa proprietà!

### Varianza

$$\text{Var}(X) = \frac{(b-a)^2}{12}$$

> [!example] Interpretazione pratica
> Se $X \sim U(0, 10)$:
> - Media: $(0 + 10)/2 = 5$
> - Varianza: $(10-0)^2/12 = 100/12 ≈ 8.33$
> - Deviazione standard: $\sqrt{8.33} ≈ 2.89$

---

## 5. Distribuzione Esponenziale Exp(λ)

> [!info] Definizione
> Una variabile aleatoria continua $X$ è **esponenziale di parametro λ > 0** se:
> $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}$$

### Interpretazione probabilistica

La distribuzione esponenziale **modella il tempo di attesa di un evento raro** in un processo senza memoria (processo di Poisson):
- Tempo fino al prossimo guasto di una macchina
- Tempo tra arrivi consecutivi in una coda
- Tempo di decadimento radioattivo

### Funzione di distribuzione cumulativa

$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

**Verifica:**
$$F_X(x) = \int_0^x \lambda e^{-\lambda t} \, dt = [-e^{-\lambda t}]_0^x = 1 - e^{-\lambda x}$$

### Valore atteso e varianza

$$E[X] = \frac{1}{\lambda}$$

$$\text{Var}(X) = \frac{1}{\lambda^2}$$

> [!tip] Regola: relazione tra parametro e media
> Se $\lambda$ è **grande**: la media $1/\lambda$ è **piccola** → decadimento veloce
> 
> Se $\lambda$ è **piccolo**: la media è **grande** → decadimento lento
>
> **Esempio:** $\lambda = 0.5$ → media = 2 giorni; $\lambda = 2$ → media = 0.5 giorni

### Proprietà di "assenza di memoria"

$$P(X > s + t \mid X > s) = P(X > t)$$

Il processo "dimentica" il tempo già trascorso. Questa è l'**unica distribuzione continua** con questa proprietà.

---

## 6. Quantizzazione uniforme e applicazioni

> [!info] Quantizzazione
> **Quantizzare** significa trasformare un segnale continuo in valori discreti (es. conversione analogico-digitale).

### Quantizzatore uniforme

Dividi il range continuo in intervalli di ampiezza $\Delta$ (quantizzazione uniforme).

**Errore quadratico medio (distorsione):**
$$\text{MSE} = \frac{\Delta^2}{12}$$

Questa formula **ripropone la varianza della distribuzione uniforme**!

> [!example] Applicazione: CD Audio
> Frequenza di campionamento: 44.1 kHz
> Risoluzione: 16 bit (2^16 = 65536 livelli)
> Distorsione: $\Delta^2/12$ dove $\Delta = $ intervallo tra livelli quantizzati
>
> A 16 bit, la qualità è già eccellente (imperrcettibile all'orecchio umano).

### Quantizzazione vettoriale (cenni)

> [!abstract] Nota storica
> **Shannon (1948):** è **asintoticamente ottimale** quantizzare **blocchi di dati** simultaneamente (quantizzazione vettoriale), non campione per campione.
>
> Questa è la base teorica dei moderni sistemi di compressione:
> - JPEG (immagini)
> - MP3 (audio)
> - Video compression

Quantizzare interi vettori anziché singoli campioni fornisce guadagni enormi in efficienza (con poco overhead computazionale).

---

## 7. Calcoli sui momenti

> [!example] Esercizio: E[X] per distribuzione uniforme
> Calcolare $E[X]$ per $X \sim U(a, b)$:
>
> $$E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{1}{b-a} \int_a^b x \, dx$$
>
> $$= \frac{1}{b-a} \cdot \left[\frac{x^2}{2}\right]_a^b = \frac{1}{b-a} \cdot \frac{b^2 - a^2}{2}$$
>
> $$= \frac{1}{b-a} \cdot \frac{(b-a)(b+a)}{2} = \frac{b+a}{2}$$

> [!example] Esercizio: E[X] per distribuzione esponenziale
> Calcolare $E[X]$ per $X \sim \text{Exp}(\lambda)$:
>
> $$E[X] = \int_0^{+\infty} x \cdot \lambda e^{-\lambda x} \, dx$$
>
> **Integrazione per parti:** $u = x$, $dv = \lambda e^{-\lambda x} dx$
>
> $$= \left[-x e^{-\lambda x}\right]_0^{\infty} + \int_0^{\infty} e^{-\lambda x} \, dx$$
>
> $$= 0 + \left[-\frac{1}{\lambda} e^{-\lambda x}\right]_0^{\infty} = \frac{1}{\lambda}$$

---

## 8. PDF condizionata

> [!info] Definizione
> Dato un evento $A$, la **PDF condizionata** è:
> $$f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x) = \frac{d}{dx} \left[\frac{P(X \leq x \cap A)}{P(A)}\right]$$

### Esempio: Uniforme condizionata

Sia $X \sim U(0, 10)$ e $A = \{X > 3\}$.

$$P(A) = 1 - F_X(3) = 1 - \frac{3}{10} = 0.7$$

**Per $x \in (3, 10)$:**
$$f_{X|A}(x) = \frac{1}{7}$$

> [!abstract] Intuizione
> La PDF condizionata è una **uniforme su (3, 10)** con altezza $1/7$ (non più $1/10$).
> L'intervallo si restringe, ma l'area totale rimane 1.

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **Varianza di trasformazioni:** $\text{Var}(aX + b) = a^2 \text{Var}(X)$
> 2. **Markov:** fornisce limite superiore usando solo la media
> 3. **Chebyshev:** caratterizza la dispersione con media e varianza
> 4. **Uniforme:** media = punto medio, varianza = (b-a)²/12
> 5. **Esponenziale:** media = 1/λ, modella tempi di attesa
> 6. **Quantizzazione:** errore = Δ²/12 (uniforme), ottimale a blocchi (vettoriale)
> 7. **PDF condizionata:** restringe il supporto mantenendo normalizzazione

---

> [!question] Domande d'esame frequenti
> - Dimostrare Markov nel caso continuo
> - Derivare Chebyshev da Markov
> - Calcolare E[X] e Var(X) per uniforme ed esponenziale
> - Interpretare l'errore di quantizzazione
> - Definire e calcolare PDF condizionata
> - Confrontare proprietà discrete vs continue
> - Applicazioni della distribuzione esponenziale

> [!todo] Esercizi suggeriti
> - [ ] Dimostrare che Var(Exp(λ)) = 1/λ²
> - [ ] Calcolare P(X > 5) per X ~ Exp(0.5)
> - [ ] Trovare PDF condizionata di esponenziale su intervallo [0, T]
> - [ ] Progettare un quantizzatore per segnale gaussiano
> - [ ] Comparare limiti Markov vs Chebyshev per una distribuzione nota
> - [ ] Implementare quantizzazione uniforme e vettoriale (Python/R)

---

#MSI #variabili-continue #markov #chebyshev #distribuzione-uniforme #distribuzione-esponenziale #quantizzazione
