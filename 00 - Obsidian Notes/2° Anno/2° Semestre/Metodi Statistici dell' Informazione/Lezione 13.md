---
date: 2026-04-27
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 13
tags: [MSI, esercizi, distribuzione-triangolare, PDF, CDF, densità-condizionata, media-condizionata]
---

# 11. Esercizi su Variabili Aleatorie Continue

## 11.1 Costruzione di una PDF triangolare

Consideriamo la seguente densità di probabilità definita su due intervalli disgiunti:

Nel supporto $[-3, -1]$ la densità è costante, mentre su $[1, 3]$ è triangolare. Descriviamo formalmente questa PDF.

**Su** $[-3, -1]$: $f_X(x) = \frac{1}{4}$ (costante).

**Su** $[1, 3]$: La densità ha forma triangolare con apice nel punto $x = 2$ e valore massimo $\frac{1}{2}$.

Analiticamente, per $x \in [1, 3]$:

$$f_X(x) = \begin{cases} \dfrac{x - 1}{2} & 1 \leq x \leq 2 \\ \dfrac{3 - x}{2} & 2 < x \leq 3 \end{cases}$$

### Verifica di normalizzazione

L'integrale totale della PDF deve fare 1:

$$\int_{-3}^{-1} \frac{1}{4} \, dx + \int_1^3 f_X(x) \, dx = \frac{1}{4} \cdot 2 + \int_1^2 \frac{x-1}{2} \, dx + \int_2^3 \frac{3-x}{2} \, dx$$

$$= \frac{1}{2} + \frac{1}{2} \left[\frac{(x-1)^2}{2}\right]_1^2 + \frac{1}{2} \left[(3x - \frac{x^2}{2})\right]_2^3 = \frac{1}{2} + \frac{1}{2} + 0 = 1 \quad \checkmark$$

## 11.2 Calcolo della CDF

La funzione di distribuzione cumulativa è:

$$F_X(x) = \begin{cases} 0 & x < -3 \\ \dfrac{x+3}{4} & -3 \leq x \leq -1 \\ \dfrac{1}{2} & -1 < x < 1 \\ \dfrac{1}{2} + \int_1^x f_X(t) \, dt & 1 \leq x \leq 3 \\ 1 & x > 3 \end{cases}$$

Per la regione $[1, 3]$, calcoliamo l'integrale della parte triangolare. Per $x \in [1, 2]$:

$$\int_1^x \frac{t-1}{2} \, dt = \frac{1}{2} \cdot \frac{(x-1)^2}{2} = \frac{(x-1)^2}{4}$$

Per $x \in [2, 3]$:

$$\int_1^2 \frac{t-1}{2} \, dt + \int_2^x \frac{3-t}{2} \, dt = \frac{1}{4} + \frac{1}{2} \left(3(x-2) - \frac{(x-2)^2}{2}\right) = \frac{1}{4} + \frac{3(x-2)}{2} - \frac{(x-2)^2}{4}$$

Semplificando: $F_X(x) = \frac{1}{2} + \frac{1}{4} + \frac{3(x-2)}{2} - \frac{(x-2)^2}{4}$ per $x \in [2, 3]$.

> [!abstract] Proprietà dell'alfabeto
> L'alfabeto di $X$ è l'insieme dei valori in cui la PDF è diversa da zero: $\text{supp}(f_X) = [-3, -1] \cup [1, 3]$. Due variabili aleatorie con alfabeti che differiscono per insiemi di probabilità nulla (ad es., due intervalli disgiunti vs. uno solo) sono considerate equivalenti in senso probabilistico.

## 11.3 Media e Condizionamento

### Calcolo della media

Una strategia efficace è usare il **teorema della media condizionata**, evitando integrali complessi.

Definiamo l'evento $A = \{X \leq 0\}$. Allora:

$$E[X] = E[X | A] P(A) + E[X | A^c] P(A^c)$$

**Calcolo di** $P(A)$: $P(A) = P(X \in [-3, -1]) = \int_{-3}^{-1} \frac{1}{4} \, dx = \frac{1}{2}$.

**Calcolo di** $E[X | A]$: Condizionato a $X \in [-3, -1]$, la densità diventa:

$$f_{X|A}(x) = \frac{f_X(x)}{P(A)} = \frac{1/4}{1/2} = \frac{1}{2} \quad \text{per } x \in [-3, -1]$$

Questa è uniforme su $[-3, -1]$, quindi:

$$E[X | A] = \int_{-3}^{-1} x \cdot \frac{1}{2} \, dx = \frac{1}{2} \cdot \frac{(-1)^2 - (-3)^2}{2} = \frac{1}{2} \cdot \frac{1 - 9}{2} = -2$$

**Per simmetria:**  La regione $[1, 3]$ è simmetrica a $[-3, -1]$ rispetto all'origine, quindi $E[X | A^c] = 2$.

**Risultato finale:** $E[X] = (-2) \cdot \frac{1}{2} + 2 \cdot \frac{1}{2} = 0$.

> [!tip] Strategie di calcolo
> Quando una PDF è non uniforme o complessa, il **riconoscimento di strutture simmetriche** e l'uso del **condizionamento** riducono drasticamente il lavoro computazionale rispetto all'integrazione diretta. La dimestichezza con proprietà come la linearità della media è essenziale.

## 11.4 Probabilità Condizionata Composta

Calcoliamo $P(X > 2 | X > -2)$.

Per definizione di probabilità condizionata:

$$P(X > 2 | X > -2) = \frac{P(X > 2 \text{ e } X > -2)}{P(X > -2)} = \frac{P(X > 2)}{P(X > -2)}$$

**Calcolo di** $P(X > 2)$:

$$P(X > 2) = \int_2^3 \frac{3-x}{2} \, dx = \frac{1}{2} \left[3x - \frac{x^2}{2}\right]_2^3 = \frac{1}{2} \left(9 - \frac{9}{2} - 6 + 2\right) = \frac{1}{4}$$

**Calcolo di** $P(X > -2)$:

$$P(X > -2) = P(X \in (-2, -1]) + P(X \in [1, 3]) = \int_{-2}^{-1} \frac{1}{4} \, dx + \frac{1}{2} = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}$$

**Risultato:** $P(X > 2 | X > -2) = \frac{1/4}{3/4} = \frac{1}{3}$.

## 11.5 Integrazione nella Densità Congiunta

Per variabili aleatorie bidimensionali $(X, Y)$ con densità congiunta $f_{X,Y}(x, y)$:

- L'integrale doppio su tutto lo spazio fornisce 1: $\iint_{\mathbb{R}^2} f_{X,Y}(x, y) \, dx \, dy = 1$.
- L'integrale su una regione rettangolare $[x_1, x_2] \times [y_1, y_2]$ fornisce la probabilità congiunta:

$$P(x_1 \leq X \leq x_2, y_1 \leq Y \leq y_2) = \int_{x_1}^{x_2} \int_{y_1}^{y_2} f_{X,Y}(x, y) \, dy \, dx$$

- **Marginalizzazione**: integrare su una variabile fornisce la densità dell'altra:

$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy, \quad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx$$

> [!warning] Avvertenza sugli integrali multipli
> Gli integrali multipli (doppi, tripli, $n$-pli) sono rari nella pratica della probabilità applicata. Ogni volta che si incontra un integrale $n$-plo con $n > 2$, è bene verificare se esiste un approccio alternativo (scomposizione, simmetria, cambio di variabili) che eviti il calcolo diretto. Nella ricerca e nell'industria, problemi con dati $n$-dimensionali ($n \gg 2$) si risolvono con metodi di apprendimento statistico, non con integrazione numerica.

---

#MSI #esercizi #distribuzione-triangolare #PDF #CDF #densità-condizionata #media-condizionata #integrale-doppio
