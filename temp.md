### Definizioni nel test di ipotesi

> [!def] Ipotesi Nulla ($H_0$) e Decisione
> Assunzione di base secondo cui il dataset osservato $\pmb { x } ^ { n }$ è la realizzazione di un vettore casuale con distribuzione nota $p _ { X ^ { n } | H _ { 0 } }$ (o $f _ { { \pmb X } ^ { n } | H _ { 0 } }$). Il test mira a decidere se rifiutare $H_0$ a favore di un'ipotesi alternativa $H_1$ tramite una partizione del dominio $\mathcal{X}^n$ in regioni di decisione.

> [!theorem] Errore di tipo-I (Falso Allarme)
> Rappresenta la probabilità di rifiutare $H_0$ quando essa è in realtà vera (ovvero assegnare i dati alla regione di rifiuto $\Omega_1$):
> $$
> \mathbb{P} \{D(\boldsymbol{X}^n) = 1 | H_0\} = \begin{cases} \int_{\Omega_1} f_{\boldsymbol{X}^n | H_0} (\boldsymbol{x}^n | H_0) d \boldsymbol{x}^n & \text{Dati Continui} \\ \sum_{\boldsymbol{x}^n \in \Omega_1} p_{\boldsymbol{X}^n | H_0} (\boldsymbol{x}^n | H_0) & \text{Dati Discreti} \end{cases}
> $$

> [!theorem] Potenza del test
> Rappresenta la capacità del test di rifiutare correttamente l'ipotesi nulla quando è falsa ($H_1$ vera):
> $$
> 1 - \beta = \mathbb{P} \{D(\boldsymbol{X}^n) = 1 | H_1\} = \begin{cases} \int_{\Omega_1} f_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1) d \boldsymbol{x}^n & \text{Dati Continui} \\ \sum_{\boldsymbol{x}^n \in \Omega_1} p_{\boldsymbol{X}^n | H_1} (\boldsymbol{x}^n | H_1) & \text{Dati Discreti} \end{cases}
> $$

## Test di Neyman-Pearson

 >[!theorem] Lemma di Neyman-Pearson
> Fornisce la regola di decisione ottimale per un test di ipotesi in uno scenario non-Bayesiano. Il test massimizza la **potenza del test** ($1 - \beta$) fissato un vincolo sulla probabilità di **errore di tipo-I** ($\alpha$):
> $$\text { Determine } \Omega_ {1} \colon \left\{ \begin{array}{l l} 1 - \beta & \text { massimo } \\ \text { s.t. } & \mathbb{P}(\text{falso allarme}) \leq \alpha \end{array} \right.$$

> [!def] Rapporto di Verosimiglianza ($L$)
> Il test risultante dall'ottimizzazione è basato sul confronto tra il rapporto delle verosimiglianze e una soglia $\eta$:
> $$L \left(\boldsymbol {x} ^ {n}\right) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta$$
> Dove $L(\pmb{x}^n)$ è definito come:
> - **Dati Continui**: $\frac {f _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{f _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})}$
> - **Dati Discreti**: $\frac {p _ {\boldsymbol {X} ^ {n} | H _ {1}} (x ^ {n} | H _ {1})}{p _ {\boldsymbol {X} ^ {n} | H _ {0}} (x ^ {n} | H _ {0})}$ [2]

La soglia $\eta$ si ottiene risolvendo l'equazione legata al vincolo sul falso allarme:
 $$\mathbb {P} \left\{L (\boldsymbol {X} ^ {n}) > \eta \mid H _ {0} \right\} = \alpha$$ 

> [!tip] Trasformazione Logaritmica
> Poiché l'applicazione di una funzione monotonicamente crescente non altera l'ottimalità del test, si utilizza spesso il **log-likelihood** $\Lambda(\pmb{x}^n)$ per semplificare i calcoli:
> $$\Lambda (\boldsymbol {x} ^ {n}) = \ln L (\boldsymbol {x} ^ {n}) \underset {H _ {0}} {\overset {H _ {1}} {\gtrless}} \eta'$$



