### Matrice di covarianza per processi SSL

Dato un vettore aleatorio $\pmb{X}$ di $M$ campioni estratto da un processo stazionario in senso lato (SSL).

*   **Vettore Media**: $\pmb{\mu}_{\pmb{X}} = \mu \mathbf{1}$ (tutti i campioni hanno lo stesso valore atteso $\mu$).
*   **Proprietà Statistiche**: La varianza $\sigma_X^2$ è costante e la correlazione tra due campioni dipende solo dalla loro distanza temporale $|i-j|$.
*   **Struttura della Matrice**: La matrice di covarianza $C_X$ assume una forma simmetrica legata ai coefficienti di correlazione $\rho_{i,j}$:
$$
\boldsymbol {C} _ {\boldsymbol {X}} = \sigma_ {X} ^ {2} \begin{pmatrix} 1 & \rho_ {1, 2} & \dots & \rho_ {1, M} \\ \rho_ {1, 2} & 1 & \dots & \rho_ {2, M} \\ \vdots & \vdots & \ddots & \vdots \\ \rho_ {1, M} & \rho_ {2, M} & \dots & 1 \end{pmatrix}
$$
#### Caratteristiche chiave
*   **Simmetria**: La matrice è sempre simmetrica rispetto alla diagonale principale.
*   **Matrice di Toeplitz**: Se il passo di campionamento è costante, tutti gli elementi sulle diagonali parallele a quella principale sono uguali tra loro.
*   **Definita non-negativa**: Il prodotto scalare tra un vettore arbitrario e la matrice di covarianza è sempre $\ge 0$.****