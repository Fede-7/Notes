Ecco una riscrittura completa del testo della slide strutturata come una vera e propria **scheda di teoria**, priva dei riferimenti all'esercizio e focalizzata esclusivamente sulle definizioni generali e sulle formule matematiche astratte.

---

# Funzioni di Variabili Casuali Doppie (o Multivariate)

Sia data una **variabile casuale doppia discreta** $(X, Y)$ regolata da una funzione di massa di probabilità (pmf) congiunta $p_{X,Y}(x, y)$, definita sullo spazio di supporto complessivo dato dal prodotto cartesiano $\mathcal{X} \times \mathcal{Y}$.

Si definisca una nuova variabile casuale discreta $Z$ come trasformazione deterministica delle prime due attraverso una funzione scalare $g(x, y)$:


$$Z = g(X, Y)$$

L'obiettivo teorico è determinare la legge di probabilità (pmf) della nuova variabile $Z$, indicata come $p_Z(z)$, a partire dalla conoscenza della pmf congiunta $p_{X,Y}(x, y)$. A seconda della natura della funzione $g(x,y)$, si distinguono due scenari matematici:

### 1. Trasformazione Biunivoca (Inversa Unica)

Se la funzione $g(x,y)$ mappa ogni singola coppia del dominio $(x,y)$ in un valore di $z$ unico e distinto (ovvero la funzione è iniettiva sullo spazio di supporto), esiste un'unica coppia invertibile $(x(z), y(z))$ tale per cui $z = g(x, y)$.

In questo caso, la probabilità che $Z$ assuma il valore $z$ coincide esattamente con la probabilità congiunta dell'unico punto di partenza che lo ha generato:


$$p_Z(z) = \mathbb{P}(Z = z) = p_{X, Y}[x(z), y(z)]$$

### 2. Trasformazione Non Biunivoca (Collassamento delle Probabilità)

Se la funzione $g(x,y)$ assegna lo stesso valore $z$ a più coppie distinte $(x,y)$ (trasformazione *molti-a-uno*), si verifica un fenomeno di **collassamento (o accumulo) delle probabilità**.

Per determinare la probabilità del punto $z$, è necessario individuare l'insieme di controimmagini $\mathcal{A}(z)$, definito come il sottoinsieme dello spazio di supporto contenente tutte le coppie che producono come output esattamente $z$:


$$\mathcal{A}(z) = \{ (x, y) \in \mathcal{X} \times \mathcal{Y} : g(x, y) = z \}$$

La pmf di $Z$ si ottiene applicando il principio di additività, ovvero **sommando** le probabilità congiunte di tutte le coppie appartenenti a tale insieme:


$$p_Z(z) = \sum_{(x, y) \in \mathcal{A}(z)} p_{X, Y}(x, y)$$

---

### Regola Operativa Generale

Per ricavare la distribuzione di $Z = g(X,Y)$ nel caso discreto:

1. **Determinazione del supporto:** Si calcola l'insieme di tutti i valori numerici possibili $\mathcal{Z}$ generati dall'applicazione di $g(x,y)$ su ogni coppia del dominio.
2. **Partizione dello spazio:** Per ogni elemento $z \in \mathcal{Z}$, si raggruppano le coppie di variabili originarie che soddisfano l'uguaglianza $g(x,y)=z$.
3. **Marginalizzazione/Sommatoria:** Si sommano i valori di probabilità associati a tali coppie all'interno della distribuzione congiunta di partenza.
