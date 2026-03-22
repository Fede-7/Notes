## Formulario Completo — Linguaggio S

---

## 1. Variabili

| Tipo | Notazione | Valore iniziale |
|---|---|---|
| Input | $X_1, X_2, X_3, \ldots$ | valore dell'input |
| Output | $Y$ | 0 |
| Temporanee | $Z_1, Z_2, Z_3, \ldots$ | 0 |

---

## 2. Istruzioni Base

| Istruzione | Effetto |
|---|---|
| `V <-- V` | nulla (pigra) |
| `V <-- V+1` | incrementa V di 1 |
| `V <-- V-1` | decrementa V di 1 (se V=0, ignorata) |
| `IF V != 0 GOTO L` | salta a L se V≠0, altrimenti continua |

---

## 3. Etichette

| Etichetta | Uso |
|---|---|
| `A`, `B`, `C`, `D` (numerate) | etichette generiche |
| `E` | terminazione del programma |

---

## 4. Macro Base

| Macro | Codice | Effetto |
|---|---|---|
| `GOTO L` | `V <-- V+1` `IF V != 0 GOTO L` | salto incondizionato |
| `V <-- 0` | `[A] V <-- V-1` `IF V != 0 GOTO A` | azzera V |
| `V <-- V1` | `V <-- 0` poi copia V1 in V | assegnazione |
| `IF V == 0 GOTO L` | `IF V != 0 GOTO A` `GOTO L` `[A]` | salta se V=0 |

---

## 5. Funzioni Aritmetiche

| Funzione | Macro | Note |
|---|---|---|
| `Y <-- X1 + X2` | ciclo di incremento | somma |
| `Y <-- X1 * X2` | ciclo di somme | prodotto |
| `Y <-- X1 - X2` | sottrazione propria $\dotminus$ | 0 se X1<X2 |
| `Y <-- X1 ^ X2` | ciclo di prodotti | potenza |
| `Y <-- X1 / X2` | minimalizzazione limitata | divisione intera |
| `Y <-- X1 mod X2` | combinazione | resto |

---

## 6. Predicati Calcolabili

| Predicato | Come si usa | Note |
|---|---|---|
| `f_S(X)` | `IF f_S(X) != 0 GOTO L` | caratteristica di S ricorsivo |
| `Primo(X)` | `IF Primo(X) != 0 GOTO L` | X è primo? |
| `X1 \| X2` | `IF Div(X1,X2) != 0 GOTO L` | X1 divide X2? |
| `X1 = X2` | `IF Eq(X1,X2) != 0 GOTO L` | uguaglianza |
| `X1 <= X2` | `IF Leq(X1,X2) != 0 GOTO L` | minore uguale |

---

## 7. Funzioni della Teoria

| Funzione | Notazione | Significato |
|---|---|---|
| Pairing | `<X1, X2>` | codifica coppia in un numero |
| Parte sinistra | `l(X)` | primo elemento della coppia |
| Parte destra | `r(X)` | secondo elemento della coppia |
| Numero di Gödel | `[X1,...,Xk]` | codifica k-pla |
| i-esimo esponente | `(X)_i` | esponente di $P_i$ in X |
| Lunghezza | `Lt(X)` | lunghezza della sequenza |

---

## 8. Funzioni di Calcolabilità

| Funzione | Notazione | Significato |
|---|---|---|
| Funzione universale | `Φ(X, Y)` | esegui programma Y su input X |
| Predicato STP | `STP(X, Y, T)` | programma Y su input X termina in T passi? |
| Halt | `HALT(X, Y)` | programma Y termina su X? (non calcolabile!) |

---

## 9. Schema STP — pattern tipici

**Aspetta che $f$ termini** (f p.c., $p$ = suo numero):
```
[A] IF STP(X, p, T) GOTO B
    T <-- T+1
    GOTO A
[B] Z <-- Φ(X, p)          ← ora Z = f(x)
```

**OR parallelo** ($x \in W_a$ oppure $x \in W_b$):
```
[A] IF STP(X, a, T) GOTO E
    IF STP(X, b, T) GOTO E
    T <-- T+1
    GOTO A
```

**Divergi se condizione vera** (loop se $x \in B$):
```
Z <-- f(X)
[LOOP] IF f_B(Z) != 0 GOTO LOOP
Y <-- Z
```

---

## 10. Template completo tipico

```
(1) Calcola variabili necessarie
        Z1 <-- f(X1)           ← se f calcolabile
        oppure STP + Φ         ← se f p.c.

(2) Controlla condizione
        IF condizione GOTO OK
        GOTO LOOP              ← divergi se non soddisfatta

(3) Output
[OK]    Y <-- risultato
        GOTO E

(4) Loop infinito
[LOOP]  GOTO LOOP
```

---

## 11. Regole d'oro

| Situazione                  | Cosa fare                 |
| --------------------------- | ------------------------- |
| $f$ calcolabile             | `Z <-- f(X)` direttamente |
| $f$ p.c.                    | usa STP prima             |
| $x \in B$ con $B$ ricorsivo | usa `f_B(X)`              |
| $x \in K$                   | usa `STP(X, X, T)`        |
| $x \in W_y$                 | usa `STP(X, y, T)`        |
| OR di condizioni            | STP parallelo             |
| divergi se condizione       | loop infinito             |
| termina se condizione       | `GOTO E`                  |