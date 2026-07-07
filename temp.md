Dire che esiste un numero fisso di formule per la correlazione non è del tutto esatto, poiché la formula esatta varia in base alla **natura dei dati** (se continui o discreti) e al **tipo di relazione** che si vuole misurare.

Tuttavia, nel campo della probabilità e della statistica, si fa generalmente distinzione tra **tre o quattro varianti principali** della formula di correlazione a seconda del contesto. Ecco quali sono:

---

### 1. Correlazione Teorica (Variabili Casuali)

Questa è la formula matematica che definisce la correlazione (chiamata anche cross-correlazione) tra due variabili casuali astratte. Si divide in base alla natura delle variabili:

* **Per variabili discrete (quella della tua domanda precedente):**
$$$$

* **Per variabili continue:**
Invece delle somme si usano gli integrali e la densità di probabilità congiunta $f_{X,Y}(x,y)$:
$$R_{X,Y} = \mathbb{E}[XY] = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} x y f_{X,Y}(x, y) \,dx\,dy$$


---

### 2. Indice di Correlazione Lineare di Pearson (La più usata in statistica)

Spesso, quando si parla semplicemente di "correlazione" in statistica e analisi dei dati, ci si riferisce al **Coefficiente di correlazione di Pearson** ($\rho$ o $r$). Questo coefficiente non misura solo il valore atteso del prodotto, ma normalizza il risultato in un intervallo compreso tra $-1$ e $+1$ per capire quanto forte sia il legame lineare.

* **Formula teorica (per popolazioni):**
$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{\mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]}{\sqrt{\mathbb{E}[X^2] - \mathbb{E}[X]^2}\sqrt{\mathbb{E}[Y^2] - \mathbb{E}[Y]^2}}$$


*(Mette in rapporto la covarianza con il prodotto delle deviazioni standard).*
* **Formula empirica (per un campione di dati reali):**
Se hai una serie di $n$ coppie di dati reali $($x_1$, $y_1$), ($x_2$, $y_2$), \dots, ($x_n$, $y_n$)$, la formula diventa:
$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$


*(Dove $\bar{x}$ e $\bar{y}}$ sono le medie campionarie).*

---

### 3. Correlazione per Ranghi (Relazioni non lineari)

Quando la relazione tra le variabili non è una linea retta, o i dati sono espressi sotto forma di classifiche (es. primo, secondo, terzo posto), la formula di Pearson non funziona bene. In questo caso si usano formule basate sui "ranghi" (le posizioni in classifica), tra cui le due principali sono:

* **Coefficiente di Spearman ($\rho_s$):** Applica la formula di Pearson direttamente ai ranghi dei dati.
* **Tau di Kendall ($\tau$):** Calcola la differenza tra le coppie di dati "concordi" e "discordi".

---

### Riassunto

In sintesi, si può dire che esistono **2 formule fondamentali per la definizione teorica** (una discreta e una continua) e **1 formula principale per l'applicazione pratica sui dati** (il coefficiente di Pearson), accompagnata da alcune varianti specifiche (come Spearman) per i casi non lineari.