---
date: 2026-04-21
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 14
tags:
  - MSI
  - PDF-congiunta
  - indipendenza
  - marginalizzazione
  - densità-condizionata
  - derivata-parziale
---

# 12. Variabili Aleatorie Continue Bivariate

## 12.1 Densità di Probabilità Congiunta

Analogamente al caso monodimensionale, una coppia di variabili aleatorie continue $(X, Y)$ è caratterizzata da una **densità di probabilità congiunta** (PDF congiunta):

$$f_{X,Y}(x, y) \geq 0, \quad \iint_{\mathbb{R}^2} f_{X,Y}(x, y) \, dx \, dy = 1$$

### Interpretazione geometrica

La densità di probabilità congiunta rappresenta la "densità di massa" su un piano: il valore $f_{X,Y}(x, y)$ indica la concentrazione di probabilità in un intorno del punto $(x, y)$. La probabilità che la coppia cada in una regione $C \subset \mathbb{R}^2$ è:

$$P((X, Y) \in C) = \iint_C f_{X,Y}(x, y) \, dx \, dy$$

Geometricamente, questa è il volume sotto la "superficie" $z = f_{X,Y}(x, y)$ sulla regione $C$.

### Analogy con la fisica

La nozione di densità congiunta in probabilità è esattamente analoga alla densità di massa in fisica. Come la densità di massa (o densità di un materiale non uniforme) rappresenta il rapporto tra massa e volume in un intorno di un punto, la densità di probabilità rappresenta il rapporto tra probabilità e "volume ordinario" (area nel caso bidimensionale, volume nel caso tridimensionale, ecc.).

## 12.2 Funzione di Distribuzione Cumulativa Congiunta

La **CDF congiunta** è:

$$F_{X,Y}(x, y) = P(X \leq x, Y \leq y) = \int_{-\infty}^x \int_{-\infty}^y f_{X,Y}(u, v) \, dv \, du$$

Proprietà:
- $F_{X,Y}(-\infty, y) = 0$ e $F_{X,Y}(x, -\infty) = 0$ (eventi impossibili).
- $F_{X,Y}(+\infty, +\infty) = 1$ (evento certo).
- $F_{X,Y}(+\infty, y) = F_Y(y)$ e $F_{X,Y}(x, +\infty) = F_X(x)$ (marginalizzazione).

La PDF congiunta si recupera dalla CDF mediante derivata parziale mista:

$$f_{X,Y}(x, y) = \frac{\partial^2 F_{X,Y}(x, y)}{\partial x \partial y}$$

## 12.3 Distribuzioni Marginali

Marginalizzando rispetto a una variabile, si ottengono le densità univariate:

$$f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y) \, dy, \quad f_Y(y) = \int_{-\infty}^{+\infty} f_{X,Y}(x, y) \, dx$$

Queste sono esattamente gli analoghi continui delle marginalizzazioni nel caso discreto (dove la somma su $y$ fornisce la PMF marginale di $X$).

## 12.4 Indipendenza

Due variabili aleatorie $X$ e $Y$ sono **indipendenti** se e solo se:

$$F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y)$$

equivalentemente,

$$f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)$$

L'indipendenza significa che la conoscenza del valore di $X$ non fornisce informazione sul valore di $Y$, e viceversa.

> [!example] Test di indipendenza
> Se una PDF congiunta si fattorizza come $f_{X,Y}(x, y) = g(x) \cdot h(y)$ per opportune funzioni $g, h \geq 0$, allora $X$ e $Y$ sono indipendenti. Basta normalizzare: $\int g(x) dx = c_1$ e $\int h(y) dy = c_2$ con $c_1 \cdot c_2 = 1$, quindi $f_X(x) = \frac{g(x)}{c_1}$ e $f_Y(y) = \frac{h(y)}{c_2}$.

## 12.5 Densità Condizionale

Data la PDF congiunta $f_{X,Y}(x, y)$ e un valore $y_0$ di $Y$, la **densità di probabilità condizionale di** $X$ **dato** $Y = y_0$ è:

$$f_{X|Y}(x | y_0) = \frac{f_{X,Y}(x, y_0)}{f_Y(y_0)}$$

(per $f_Y(y_0) > 0$).

### Interpretazione

La densità condizionale è la "restrizione" della densità congiunta al "filo" di ordinata costante $y = y_0$, riscalata affinché integri a 1. Se integriamo sulla variabile $x$:

$$\int_{-\infty}^{+\infty} f_{X|Y}(x | y_0) \, dx = \frac{\int_{-\infty}^{+\infty} f_{X,Y}(x, y_0) \, dx}{f_Y(y_0)} = \frac{f_Y(y_0)}{f_Y(y_0)} = 1 \quad \checkmark$$

### Analogia con il caso discreto

L'espressione $f_{X|Y}(x | y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}$ è formalmente identica a $P(X = x | Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}$ nel caso discreto. L'unica differenza è che nel caso continuo $P(Y = y) = 0$, quindi la definizione è in senso limite (come descritto nella lezione 11).

## 12.6 Derivate Parziali e Cambio di Variabili

### Derivata parziale

Se $g(x, y) = \sin^2(xy) + x^3 y^4$, le derivate parziali sono:

$$\frac{\partial g}{\partial x} = 2 \sin(xy) \cos(xy) \cdot y + 3x^2 y^4 = y \sin(2xy) + 3x^2 y^4$$

$$\frac{\partial^2 g}{\partial x \partial y} = \sin(2xy) + 2xy \cos(2xy) + 12x^2 y^3$$

La regola è semplice: si deriva rispetto a una variabile trattenendo le altre come costanti.

### Theorem di Schwarz

Per funzioni sufficientemente regolari, l'ordine di derivazione non conta:

$$\frac{\partial^2 g}{\partial x \partial y} = \frac{\partial^2 g}{\partial y \partial x}$$

Questa proprietà è sfruttata nel ricavare la PDF congiunta dalla CDF congiunta.

## 12.7 Caso di Variabili Indipendenti Gaussiane

Se $X \sim \mathcal{N}(\mu_X, \sigma_X^2)$ e $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$ sono indipendenti, allora:

$$f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y) = \frac{1}{2\pi \sigma_X \sigma_Y} \exp\left(-\frac{(x-\mu_X)^2}{2\sigma_X^2} - \frac{(y-\mu_Y)^2}{2\sigma_Y^2}\right)$$

Questa è la PDF di una distribuzione **gaussiana bivariata** con covarianza nulla.

---

#MSI #PDF-congiunta #indipendenza #marginalizzazione #densità-condizionale #CDF-congiunta #derivata-parziale
