# Spiegazione semplice e veloce

Questo paragrafo parla di **regressione lineare nel mondo reale** quando hai tanti dati che arrivano continuamente.

## **Il problema di base: Least Squares (LS)**

Hai dati organizzati in una matrice $\boldsymbol{X}$ (features) e un vettore $\boldsymbol{y}$ (quello che vuoi predire).

**Modello**: $\boldsymbol{y} = \boldsymbol{X}^T\boldsymbol{a} + \boldsymbol{\epsilon}$

Cioè: ogni output è una combinazione lineare degli input, più rumore.

**Soluzione**: $\boldsymbol{a}_{\mathrm{LS}} = (\boldsymbol{X}\boldsymbol{X}^T)^{-1}\boldsymbol{X}\boldsymbol{y}$

Trovi i coefficienti $\boldsymbol{a}$ che minimizzano l'errore quadratico.

---

## **Il problema pratico: i dati arrivano continuamente 📊**

Immagina un sistema che riceve **nuovi dati ogni secondo** (come un sensore IoT o un'app mobile).

❌ **Approccio naive**: ogni volta che arriva un nuovo dato, ricalcoli tutta l'inversione della matrice. Costo: $\mathcal{O}($n^3$)$ — **molto lento!**

✅ **Soluzione intelligente**: **Formula di Sherman-Morrison**

Invece di ricalcolare tutto da zero, **aggiorni** la soluzione precedente usando solo il nuovo dato. Costo: $\mathcal{O}($n^2$)$ — **100x più veloce!**

---

## **Esempio reale: Sistema di raccomandazione 🎬**

Stai tracciando: come un utente interagisce con film (features) → rating che dà (target).

- **Primo giorno**: hai 1000 utenti, calcoli $\boldsymbol{a}_{\mathrm{LS}}$
- **Domani**: arriva 1 nuovo utente con il suo rating
  - ❌ Ricalcoli tutto: $\mathcal{O}($n^3$)$ **lentissimo**
  - ✅ Usi Sherman-Morrison: aggiorni in $\mathcal{O}($n^2$)$ **quasi istantaneo**

---

## **Adattività (LS esponenzialmente pesato) 🔄**

In ambienti che **cambiano nel tempo**, non tutti i dati vecchi valgono uguale.

**Idea**: dai più peso ai dati recenti, dimentica gradualmente quelli vecchi.

Usi un fattore $w < 1$:
- Dati di oggi: peso $w^0 = 1$ (massimo)
- Dati di ieri: peso $w^1$ (ridotto)
- Dati di un mese fa: peso $w^{30}$ (quasi trascurabile)

**Uso reale**: previsione di traffico, previsioni meteorologiche, volatilità di borsa.

---

## **LS con bias 📌**

Aggiungi un termine costante $b$ (intercetta) al modello:
$$\widehat{\theta} = \boldsymbol{a}^T\boldsymbol{x}^n + b$$
La soluzione richiede di **centrare i dati** (sottrarre le medie) prima di calcolare $\boldsymbol{a}$, poi recuperare $b$ dalla media del target.

---

## **Riassunto**

| Metodo                              | Quando lo usi                   | Vantaggio                   |
| ----------------------------------- | ------------------------------- | --------------------------- |
| **LS base**                         | Dati statici, calcolo una volta | Semplice                    |
| **LS ricorsivo (Sherman-Morrison)** | Dati arrivano continuamente     | Veloce anche con tanti dati |
| **LS esponenziale**                 | Ambiente che cambia nel tempo   | Si adatta automaticamente   |
| **LS con bias**                     | Vuoi intercetta nel modello     | Più flessibile              |

---




Il simbolo con il doppio modulo ($\|\cdot\|$) rappresenta la **norma di un vettore**. 

Ecco l'essenziale per l'esame:

*   **Significato geometrico**: È la generalizzazione del valore assoluto per i vettori.
*   **Contesto MMSE (Parametri Multipli)**: Indica la **somma dei quadrati degli errori** di tutte le componenti del vettore.
*   **Contesto Minimi Quadrati (Least Squares)**: Viene usato per indicare l'errore totale del modello ($\|\boldsymbol{\epsilon}_n\|^2$), calcolato come la somma dei quadrati degli scarti tra dati osservati e modello lineare.
*   **Perché si usa**: Serve a trasformare un vettore di errori (che ha diverse direzioni) in un unico valore scalare positivo che ne misuri l'entità complessiva.

**In sintesi**: Se hai un solo parametro usi $|x|$, se ne hai molti (vettore) usi $\|\boldsymbol{x}\|$.