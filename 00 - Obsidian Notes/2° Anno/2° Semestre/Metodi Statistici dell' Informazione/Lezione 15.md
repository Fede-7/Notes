---
date: 2026-04-27
corso: Metodi Statistici per l'Informazione
docente: Marco Lops
lezione: 15
tags: [MSI, processi-aleatori, processi-stocastici, tempo-discreto, tempo-continuo, realizzazione, indice-temporale]
---

# 13. Processi Stocastici e Processi Aleatori

## 13.1 Definizione e Nomenclatura

Un **processo aleatorio** (o **processo stocastico**) è un'estensione delle variabili aleatorie al dominio temporale. Mentre una variabile aleatoria assegna un numero a ogni elemento $\omega$ dello spazio campionario, un processo aleatorio assegna una **sequenza** di numeri.

> [!abstract] Definizione formale
> Dato uno spazio di probabilità $(\Omega, \mathcal{F}, P)$, un **processo stocastico** è una famiglia di variabili aleatorie indicizzate dal tempo:
> $$\{X(t) : t \in \mathcal{T}\}$$
> dove $\mathcal{T}$ è un insieme di indici (tipicamente $\mathbb{N}$ per tempo discreto, $\mathbb{R}$ per tempo continuo) e ogni $X(t)$ è una variabile aleatoria.

Per ogni $\omega \in \Omega$ fissato, la funzione $t \mapsto X(t, \omega)$ è una **realizzazione** (o **traiettoria**) del processo. Le realizzazioni sono sequenze numeriche (nel caso discreto) o funzioni del tempo (nel caso continuo), non numeri singoli.

## 13.2 Dipendenza dalle Due Variabili

Un processo aleatorio dipende da due variabili:

1. **L'indice temporale** $t$: determina quando osserviamo il processo.
2. **L'elemento dello spazio campionario** $\omega$: rappresenta l'incertezza.

Fissando $t$ e variando $\omega$, si ottiene una variabile aleatoria $X(t, \cdot)$. Fissando $\omega$ e variando $t$, si ottiene una realizzazione particolare $X(\cdot, \omega)$.

### Notazione abbreviata

Per brevità, scriviamo $X_t$ (tempo discreto) o $X(t)$ (tempo continuo) intendendo $X(t, \omega)$, dove il contesto rende chiaro se stiamo parlando di una variabile aleatoria (fissato $t$) o di una realizzazione (fissato $\omega$).

## 13.3 Processi in Tempo Discreto vs. Continuo

### Tempo discreto ($\mathcal{T} = \mathbb{Z}$ o $\mathbb{N}$)

La sequenza di variabili aleatorie è $\{X_1, X_2, X_3, \ldots\}$ o $\{X_0, X_1, X_2, \ldots\}$. Una realizzazione è una sequenza numerica:

$$(x_1, x_2, x_3, \ldots)$$

Esempi: prezzi azionari giornalieri, campioni di un segnale audio digitalizzato, numero di clienti in una coda ad ogni istante di campionamento.

### Tempo continuo ($\mathcal{T} = [0, T]$ o $\mathbb{R}_{\geq 0}$)

Una realizzazione è una funzione continua del tempo:

$$t \mapsto X(t, \omega)$$

Esempi: voltaggio di rumore termico in un circuito, posizione di una particella soggetta a moto browniano, intensità di una sorgente luminosa nel tempo.

## 13.4 Caratterizzazione Statistica

Per caratterizzare un processo aleatorio sono necessari:

1. **Medie al primo ordine**: per ogni $t$, la media $\mu_X(t) = E[X(t)]$ e la varianza $\sigma_X^2(t) = \text{Var}(X(t))$.
2. **Medie al secondo ordine**: per ogni coppia di tempi $t_1, t_2$, la covarianza $\text{Cov}(X(t_1), X(t_2)) = E[(X(t_1) - \mu_X(t_1))(X(t_2) - \mu_X(t_2))]$.
3. **Densità congiunte**: le PDF (o PMF) congiunte $f_{X(t_1), X(t_2), \ldots, X(t_n)}$ per qualsiasi $n$ e qualsiasi scelta di tempi $t_1, \ldots, t_n$.

Una caratterizzazione completa (descrizione probabilistica totale) richiede tutte le densità congiunte finite-dimensionali.

## 13.5 Proprietà di Stazionarietà

Un processo è **stazionario** (in senso stretto) se le proprietà statistiche sono invarianti nel tempo. Formalmente:

$$P(X(t_1) \leq x_1, \ldots, X(t_n) \leq x_n) = P(X(t_1 + \tau) \leq x_1, \ldots, X(t_n + \tau) \leq x_n)$$

per ogni scelta di tempi e ritardo $\tau$.

Un processo è **stazionario in senso lato** se:
- $E[X(t)]$ è costante nel tempo.
- $\text{Var}(X(t))$ è costante nel tempo.
- $\text{Cov}(X(t_1), X(t_2))$ dipende solo dalla differenza $t_1 - t_2$.

La stazionarietà semplifica l'analisi: molti processi reali (almeno su scale temporali limitate) possono essere approssimati come stazionari.

## 13.6 Esempio: Processo di Poisson

Il **processo di Poisson** con intensità $\lambda$ è un processo in tempo continuo fondamentale che conta il numero di eventi (arrivi, click, decadimenti) in intervalli di tempo. Se $N(t)$ è il numero di eventi fino al tempo $t$, allora:

$$P(N(t) = k) = \frac{(\lambda t)^k}{k!} e^{-\lambda t}$$

Proprietà caratteristiche:
- **Incrementi indipendenti**: il numero di eventi in intervalli disgiunti sono variabili aleatorie indipendenti.
- **Incrementi stazionari**: la distribuzione del numero di eventi in $[t, t + s]$ dipende solo da $s$, non da $t$.
- **Assenza di memoria**: la probabilità di un prossimo evento non dipende dal passato.

Il processo di Poisson modella code (numero di clienti), affidabilità (numero di guasti), e comunicazioni (numero di pacchetti).

## 13.7 Processi Gaussiani

Se ogni marginale $X(t)$ è gaussiana e ogni densità congiunta è gaussiana multivariata, il processo si dice **gaussiano**. I processi gaussiani:

- Sono completamente caratterizzati dalle loro medie $\mu_X(t)$ e funzione di autocovarianza $\gamma(t_1, t_2) = \text{Cov}(X(t_1), X(t_2))$.
- Generalizzano il concetto di distribuzione normale alle funzioni del tempo.
- Sono importanti nella teoria del filtraggio (Kalman filter) e nell'apprendimento supervisionato (Gaussian Process regression).

---

#MSI #processi-aleatori #processi-stocastici #tempo-discreto #tempo-continuo #realizzazione #stazionarietà #processo-poisson
