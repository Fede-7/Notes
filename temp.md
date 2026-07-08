Ecco una sintesi chiara e diretta del testo:

## Trasformazione di variabili aleatorie continue

Data una variabile aleatoria continua $X$ con densità di probabilità $f_X(x)$ e funzione di ripartizione $F_X(x)$, consideriamo la trasformazione $Y = g(X)$.

A seconda delle proprietà della funzione $g$, si distinguono tre scenari:

1. **Trasformazione Biunivoca:** Se $g$ è invertibile, continua e derivabile, la variabile $Y$ rimane continua e la sua distribuzione può essere calcolata direttamente tramite l'inversa di $g$.
2. **Trasformazione Continua non Invertibile:** Se $g$ è continua e derivabile ma non invertibile (es. $g(x) = x^2$), la variabile $Y$ rimane comunque continua.
3. **Quantizzazione (A/D):** Se $g$ è una funzione che "appiattisce" i valori (non continua o a gradini), la variabile $Y$ diventa **discreta**. Questo caso equivale a una conversione Analogico-Digitale (A/D), dove la variabile continua viene quantizzata con perdita di informazioni.