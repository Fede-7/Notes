---
date: 2026-04-14
corso: Metodi Statistici dell'Informazione
lezione: "Variabili continue — CDF, PDF e distribuzioni notevoli"
tags: [MSI, variabili-continue, CDF, PDF, distribuzione-uniforme, distribuzione-esponenziale, misura-probabilita]
---

# MSI — Variabili Continue: CDF, PDF e Distribuzioni Notevoli

**Corso:** Metodi Statistici dell'Informazione

---

## Argomenti trattati

- Passaggio da variabili discrete a variabili continue
- Caratterizzazione mediante misura di probabilità su intervalli
- Definizione formale di CDF e PDF per variabili continue
- Relazione tra CDF e PDF: integrazione e derivazione
- Distribuzioni continue notevoli: uniforme, esponenziale
- Valore atteso per variabili continue
- Introduzione alla PDF condizionata

---

## 1. Variabili continue: definizione

> [!info] Variabile aleatoria continua
> Una variabile aleatoria $X$ è **continua** se gli eventi elementari corrispondono all'appartenenza di $X$ a un **intervallo**, non a un valore puntuale.
> 
> **Caratteristica:** $P(X = x) = 0$ per ogni $x \in \mathbb{R}$ — gli eventi puntuali hanno probabilità nulla.

Conseguenza: le probabilità si assegnano a **intervalli** $[a, b]$, non a singoli punti.

---

## 2. Funzione di distribuzione cumulativa (CDF)

> [!info] CDF (Cumulative Distribution Function)
> La **funzione di distribuzione cumulativa** di $X$ è:
> $$F_X(x) = P(X \leq x) \quad \forall x \in \mathbb{R}$$
> Definita per **qualsiasi** variabile aleatoria, discreta o continua.

### Proprietà della CDF

1. **Valori agli estremi:** $F_X(-\infty) = 0$, $F_X(+\infty) = 1$
2. **Monotonia crescente:** se $x_1 < x_2$, allora $F_X(x_1) \leq F_X(x_2)$
3. **Continuità a destra:** per variabili continue, la CDF è continua ovunque
4. **Probabilità di intervalli:** 
$$P(a < X \leq b) = F_X(b) - F_X(a)$$

---

## 3. Densità di probabilità (PDF)

> [!info] PDF (Probability Density Function)
> La **funzione di densità di probabilità** è la derivata della CDF:
> $$f_X(x) = \frac{d}{dx} F_X(x)$$
> 
> **Relazione inversa (integrazione):**
> $$F_X(x) = \int_{-\infty}^{x} f_X(t) \, dt$$

### Proprietà della PDF

1. **Non negatività:** $f_X(x) \geq 0$ per ogni $x$ (la CDF è monotona)
2. **Normalizzazione:** 
$$\int_{-\infty}^{+\infty} f_X(x) \, dx = 1$$

3. **Probabilità di intervalli:** 
$$P(a \leq X \leq b) = \int_a^b f_X(x) \, dx$$

> [!warning] Errore comune: "La PDF è una probabilità"
> **FALSO!** La PDF può valere più di 1 (es. $f_X(0) = 5$). È una **densità**, non una probabilità. La probabilità è l'**area** sotto la curva su un intervallo.

---

## 4. Variabile uniforme $U(a, b)$

> [!info] Distribuzione uniforme
> Una variabile $X$ è **uniforme** sull'intervallo $[a, b]$ se la probabilità è distribuita **uniformemente**:
> $$f_X(x) = \begin{cases} \dfrac{1}{b-a} & a \leq x \leq b \\ 0 & \text{altrove} \end{cases}$$

**Verifica di normalizzazione:**
$$\int_a^b \frac{1}{b-a} \, dx = 1 \quad \checkmark$$

### CDF della uniforme

$$F_X(x) = \begin{cases} 0 & x < a \\ \dfrac{x-a}{b-a} & a \leq x \leq b \\ 1 & x > b \end{cases}$$

La CDF è una **rampa lineare** da 0 a 1.

### Valore atteso

$$E[X] = \int_a^b x \cdot \frac{1}{b-a} \, dx = \frac{a + b}{2}$$

> [!tip] Ricordare per l'esame
> **Media della uniforme = punto medio dell'intervallo** — intuitivo e facile da verificare

---

## 5. Variabile esponenziale $\text{Exp}(\lambda)$

> [!info] Distribuzione esponenziale
> Una variabile $X$ è **esponenziale** di parametro $\lambda > 0$ se:
> $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x \geq 0 \\ 0 & x < 0 \end{cases}$$

**Interpretazione:** modella il tempo di attesa di un evento raro in un processo senza memoria (es. tempo fino al prossimo arrivo in una coda Poissoniana).

### CDF della esponenziale

$$F_X(x) = \begin{cases} 0 & x < 0 \\ 1 - e^{-\lambda x} & x \geq 0 \end{cases}$$

**Derivazione:**
$$F_X(x) = \int_0^x \lambda e^{-\lambda t} \, dt = \left[-e^{-\lambda t}\right]_0^x = 1 - e^{-\lambda x}$$

### Valore atteso

$$E[X] = \int_0^{+\infty} x \cdot \lambda e^{-\lambda x} \, dx = \frac{1}{\lambda}$$

> [!tip] Regola: parametro e media
> Se $\lambda$ è grande, la media $1/\lambda$ è **piccola** (decadimento veloce). Se $\lambda$ è piccolo, la media è grande (decadimento lento).

> [!warning] Errore comune: confondere PDF e probabilità
> $f_X(0) = \lambda$, che può essere $> 1$ se $\lambda > 1$. **La PDF non è una probabilità!**

---

## 6. Valore atteso: derivazione dalla quantizzazione

> [!example] Giustificazione di $E[X] = \int x f_X(x) \, dx$

Dividiamo il supporto di $X$ in intervalli di ampiezza $\delta$, e approssimiamo con una variabile discreta $X_\delta$.

Per la variabile discreta:
$$E[X_\delta] = \sum_i x_i \cdot P(X_\delta = x_i) = \sum_i x_i \cdot f_X(c_i) \cdot \delta$$

Questa è la **somma di Riemann** dell'integrale $\int x f_X(x) \, dx$. Quando $\delta \to 0$:

$$E[X] = \int_{-\infty}^{+\infty} x f_X(x) \, dx$$

> [!info] Applicazione: quantizzazione vettoriale
> **Shannon (1948):** per digitalizzare dati analogici è **ottimale quantizzare blocchi di dati simultaneamente**, non campione per campione. La quantizzazione vettoriale è asintoticamente molto più efficiente e fonda i moderni sistemi di compressione (JPEG, MP3, ecc.).

---

## 7. PDF e CDF condizionate

> [!info] Probabilità e PDF condizionate
> Data un evento $A$:
> $$F_{X|A}(x) = P(X \leq x | A) = \frac{P(X \leq x \cap A)}{P(A)}$$
> 
> **PDF condizionata:** derivando la CDF
> $$f_{X|A}(x) = \frac{d}{dx} F_{X|A}(x)$$

### Esempio: PDF condizionata di una uniforme

Sia $X \sim U(0, 10)$ e $A = \{X > 3\}$.

$$P(A) = 1 - F_X(3) = 0.7$$

Per $x \in (3, 10)$:
$$f_{X|A}(x) = \frac{1}{7} \quad \text{(uniforme su intervallo ridotto)}$$

> [!tip] Interpretazione
> La PDF condizionata è una **uniforme su $(3, 10)$** — ridimensionata perché la larghezza è 7, non 10.

---

> [!abstract] Riepilogo: Punti Chiave
> 1. **CDF:** $F_X(x) = P(X \leq x)$ — definita per variabili continue e discrete
> 2. **PDF:** $f_X(x) = F_X'(x)$ — densità, non probabilità
> 3. **Uniforme:** PDF costante, media $= \frac{a+b}{2}$, CDF lineare
> 4. **Esponenziale:** media $= \frac{1}{\lambda}$, modella tempi di attesa
> 5. **Valore atteso:** giustificato da quantizzazione e somme di Riemann
> 6. **PDF condizionata:** definita tramite CDF condizionata

---

> [!question] Domande d'esame frequenti
> - Dimostrare che l'integrale di una PDF è 1
> - Calcolare CDF e media per una distribuzione uniforme
> - Confrontare PDF e PMF (massa vs densità)
> - Interpretare il significato di PDF > 1

> [!todo] Esercizi suggeriti
> - [ ] Dimostrare che $E[\text{Exp}(\lambda)] = 1/\lambda$
> - [ ] Calcolare PDF condizionata di esponenziale su intervallo $[0, T]$
> - [ ] Generare variabili uniformi e esponenziali in Python/R

---

#MSI #variabili-continue #CDF #PDF #distribuzione-uniforme #distribuzione-esponenziale
