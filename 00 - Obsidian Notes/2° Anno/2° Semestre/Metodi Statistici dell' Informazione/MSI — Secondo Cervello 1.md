 # Metodi Statistici dell'Informazione (MSI)

## I Fondamenti della Probabilità

### L'Origine dell'Informazione
> [!ABSTRACT] 
> L'informazione nasce dall'ignoranza. Se conosci già il risultato, l'informazione è nulla. La probabilità misura questa incertezza iniziale.
> [!QUOTE] 
> Teoria dell'Informazione. Telecomunicazioni: trasferimento nello spazio. Informatica: trasferimento nel tempo (compressione e memoria).
> [!EXAMPLE] 
> Apri un pacco postale. Sai che contiene un libro. L'informazione è zero. Apri un pacco a sorpresa. L'incertezza si azzera. L'informazione esplode.
> [!DANGER] 
> Confondere il "dato" con l'"informazione". Il dato esiste sempre. L'informazione richiede un'incertezza precedente.

- Nodo Incertezza: Il risultato ignoto genera valore informativo.
- Nodo Telecomunicazioni: Il sistema sposta informazione nello spazio.
- Nodo Informatica: Il sistema conserva informazione nel tempo.

### Spazio dei Campioni ed Eventi
> [!ABSTRACT] 
> L'universo di tutte le possibilità si chiama Spazio Campionario. Un evento rappresenta un pezzo di questo universo.
> [!QUOTE] 
> Spazio campionario $\Omega$. Evento $A \subseteq \Omega$. Evento elementare $\omega \in \Omega$.
> [!EXAMPLE] 
> Lancia un dado sul tavolo. Il tavolo rappresenta $\Omega$ (tutti i numeri). Copri i numeri pari con la mano. La mano rappresenta l'evento $A$.
> [!DANGER] 
> Trattare l'evento come un singolo numero. L'evento è un insieme. Applica sempre le regole degli insiemi.

- Nodo Esperimento: L'azione produce esiti multipli.
- Nodo Universo: Lo spazio campionario racchiude ogni esito.
- Nodo Sottoinsieme: L'evento isola risultati specifici.
- Nodo Unione: L'operatore richiede un evento oppure l'altro.
- Nodo Intersezione: L'operatore richiede entrambi gli eventi.

### Calcolo Combinatorio
> [!ABSTRACT] 
> Se gli eventi hanno chance uguali, la probabilità diventa un calcolo meccanico: conti i casi buoni e li dividi per i casi totali.
> [!QUOTE] 
> Permutazioni: $n!$. Disposizioni: $\frac{n!}{(n-k)!}$. Combinazioni: $\binom{n}{k}$. 
> [!EXAMPLE] 
> Estrai palline da un'urna. Metti le palline in fila sul banco. L'ordine conta. Butti le palline dentro un cesto. L'ordine svanisce.
> [!DANGER] 
> Sbagliare la formula tra disposizioni e combinazioni. Verifica sempre la rilevanza dell'ordine prima di calcolare.

- Nodo Conteggio: La probabilità divide i casi favorevoli per i casi totali.
- Nodo Permutazione: Il calcolo ordina tutti gli elementi disponibili.
- Nodo Disposizione: Il calcolo seleziona elementi rispettando l'ordine.
- Nodo Combinazione: Il calcolo seleziona elementi ignorando l'ordine.

### Assiomi di Kolmogorov
> [!ABSTRACT] 
> La probabilità funziona come la massa fisica. Ha un peso positivo e il totale forma un blocco intero. Non ha massa negativa.
> [!QUOTE] 
> Spazio $(\Omega, \mathcal{E}, P)$. Assioma 1: $P(A) \geq 0$. Assioma 2: $P(\Omega) = 1$. Assioma 3: $P(\cup A_i) = \sum P(A_i)$ per $A_i$ disgiunti.
> [!EXAMPLE] 
> Taglia una torta. La torta intera pesa 1. Ogni fetta pesa una frazione positiva. La somma delle fette ricompone la torta.
> [!DANGER] 
> Pensare che probabilità zero significhi evento impossibile. Un evento con probabilità zero avviene fisicamente nei sistemi continui.

- Nodo Positività: La funzione genera valori positivi.
- Nodo Totalità: Lo spazio campionario somma uno.
- Nodo Additività: L'operatore somma insiemi completamente separati.

### Probabilità Condizionata
> [!ABSTRACT] 
> La scoperta di un fatto nuovo taglia via possibilità. L'universo di riferimento si restringe all'evento appena accaduto.
> [!QUOTE] 
> Definizione: $P(B|A) = \frac{P(A \cap B)}{P(A)}$. Legge Composta: $P(A \cap B) = P(A)P(B|A)$.
> [!EXAMPLE] 
> Cerca una persona nel mondo intero. Scopri che indossa occhiali. Il mondo scompare. Rimane solo il gruppo dei portatori di occhiali. Cerca lì dentro.
> [!DANGER] 
> Invertire condizione ed evento. $P(A|B)$ differisce totalmente da $P(B|A)$. Leggi attentamente il testo.

- Nodo Restringimento: L'informazione nuova riduce lo spazio campionario.
- Nodo Condizione: L'evento accaduto diventa il nuovo denominatore.
- Nodo Composizione: La formula moltiplica i singoli passaggi condizionati.

### Probabilità Totale
> [!ABSTRACT] 
> Spezzi un problema complesso in pezzi semplici. Calcoli la probabilità in ogni pezzo e sommi i risultati parziali.
> [!QUOTE] 
> Teorema: $P(A) = \sum P(A|E_i)P(E_i)$. Gli eventi $E_i$ formano una partizione di $\Omega$.
> [!EXAMPLE] 
> Calcola la probabilità di incidente. Dividi le strade in città, autostrada e sterrato. Calcola l'incidente per ogni strada. Somma i tre risultati.
> [!DANGER] 
> Usare pezzi sovrapposti. La partizione richiede pezzi totalmente disgiunti. La loro unione forma l'intero spazio.

- Nodo Suddivisione: La partizione rompe lo spazio campionario.
- Nodo Parziale: La formula calcola l'evento in ogni sottospazio.
- Nodo Somma: L'operatore unisce tutti i calcoli parziali.

### Teorema di Bayes
> [!ABSTRACT] 
> Il Teorema inverte il tempo e la logica. Parti dall'effetto visibile e risali alla causa invisibile. Aggiorna la tua idea iniziale.
> [!QUOTE] 
> Formula di Bayes: $P(B|A) = \frac{P(A|B)P(B)}{P(A)}$.
> [!EXAMPLE] 
> Entri in casa e vedi fumo (effetto). Vuoi scoprire se c'è fuoco (causa). Il teorema usa la presenza del fumo per confermare il fuoco.
> [!DANGER] 
> Ignorare la probabilità a priori. Un test medico positivo non garantisce la malattia se la malattia colpisce una persona su un milione.

- Nodo Effetto: L'evento visibile attiva il calcolo.
- Nodo Causa: La formula cerca l'origine del fenomeno.
- Nodo Aggiornamento: La probabilità a posteriori corregge l'ipotesi iniziale.

### Indipendenza Stocastica
> [!ABSTRACT] 
> Due eventi vivono in mondi separati. Il verificarsi del primo non influenza minimamente le possibilità del secondo.
> [!QUOTE] 
> Definizione: $P(A \cap B) = P(A)P(B)$. Equivalenza: $P(B|A) = P(B)$.
> [!EXAMPLE] 
> Lancia due dadi da due mani diverse. Il primo dado cade sul tavolo. Il secondo dado cade a terra. Il pavimento ignora il tavolo.
> [!DANGER] 
> Dedurre l'indipendenza totale dall'indipendenza a coppie. Tre eventi indipendenti a due a due possono collassare insieme. Verifica l'intersezione tripla.

- Nodo Fattorizzazione: L'intersezione moltiplica le probabilità assolute.
- Nodo Isolamento: La condizione lascia intatta la probabilità.
- Nodo Indipendenza: Gli eventi bloccano lo scambio di informazioni.

## Variabili Aleatorie Discrete

### Concetto di Variabile Aleatoria
> [!ABSTRACT] 
> La Variabile Aleatoria traduce la realtà in numeri. Assegna un numero preciso a ogni esito possibile di un esperimento fisico.
> [!QUOTE] 
> Funzione $X : \Omega \to \mathcal{X}$. Associa un valore reale all'esito $\omega$.
> [!EXAMPLE] 
> Lancia una moneta. La moneta mostra "Testa" o "Croce". Il matematico non usa parole. Il matematico scrive 1 per Testa e 0 per Croce. La Variabile Aleatoria è questo traduttore.
> [!DANGER] 
> Credere che la Variabile Aleatoria sia un numero casuale. La Variabile Aleatoria è una funzione deterministica. L'incertezza risiede nell'esperimento iniziale, non nella funzione.

- Nodo Traduzione: La funzione trasforma l'esito fisico in valore numerico.
- Nodo Unificazione: Il modello raggruppa esperimenti fisici logicamente identici.
- Nodo Alfabeto: L'insieme contiene tutti i valori numerici raggiungibili.

### Probability Mass Function (PMF)
> [!ABSTRACT] 
> La PMF mappa ogni numero alla sua precisa probabilità. Mostra esattamente la forma geometrica dell'incertezza.
> [!QUOTE] 
> Formula: $p_X(x) = P(X = x)$. Condizioni: $p_X(x) \geq 0$ e $\sum p_X(x) = 1$.
> [!EXAMPLE] 
> Costruisci un istogramma fatto di blocchi di mattoni. L'asse orizzontale posiziona i numeri. L'altezza dei blocchi indica la probabilità. La somma di tutti i blocchi forma un quadrato perfetto di area uno.
> [!DANGER] 
> Dimenticare la normalizzazione. Una funzione rappresenta una PMF vera solo se la somma totale dei valori fa esattamente uno.

- Nodo Mappatura: La funzione associa il valore numerico alla probabilità percentuale.
- Nodo Positività: L'altezza del blocco rimane strettamente positiva.
- Nodo Normalizzazione: La somma globale garantisce l'unità assoluta.

### Valore Atteso (Media Statistica)
> [!ABSTRACT] 
> Il Valore Atteso fissa il baricentro dell'incertezza. Indica il valore di equilibrio che ottieni mediando infiniti esperimenti.
> [!QUOTE] 
> Formula: $E[X] = \mu_X = \sum x \cdot p_X(x)$. Legge Grandi Numeri: la media campionaria $\bar{X}_n$ converge a $E[X]$. Teorema Fondamentale: $E[g(X)] = \sum g(x) \cdot p_X(x)$.
> [!EXAMPLE] 
> Metti dei pesi su un'asta orizzontale. Il valore $x$ indica la posizione sul braccio. La probabilità indica la massa del peso. Il Valore Atteso è l'esatto punto in cui metti il dito per non far cadere l'asta.
> [!DANGER] 
> Confondere la media statistica con la media aritmetica. La media statistica pesa ogni valore con la sua vera probabilità. La media aritmetica dà a tutti lo stesso peso e vale solo per la distribuzione uniforme.

- Nodo Baricentro: L'operatore bilancia geometricamente i pesi probabili.
- Nodo Linearità: La funzione conserva inalterate le somme e i prodotti per costanti.
- Nodo Asintoto: La frequenza empirica converge asintoticamente alla media teorica.
- Nodo Trasformazione: Il calcolo diretto evita di costruire la PMF della funzione derivata.

### Varianza e Dispersione
> [!ABSTRACT] 
> La Varianza misura lo sparpagliamento dei dati. Indica quanto violentemente l'incertezza allontana i valori dal baricentro centrale.
> [!QUOTE] 
> Formula base: $\sigma_X^2 = E[(X - \mu_X)^2]$. Formula rapida: $\sigma_X^2 = E[X^2] - \mu_X^2$. Deviazione standard: $\sigma_X = \sqrt{\sigma_X^2}$.
> [!EXAMPLE] 
> Spara con un arco a un bersaglio. Le frecce colpiscono il centro (media). Certe frecce colpiscono molto lontano. La varianza misura la distanza media di ogni freccia dal centro esatto. Frecce strette danno varianza bassa. Frecce larghe danno varianza alta.
> [!DANGER] 
> Dimenticare l'elevamento al quadrato. I valori distanti a destra e a sinistra si annullerebbero a vicenda senza il quadrato. La varianza eleva tutto al quadrato per sommare gli errori assoluti.

- Nodo Dispersione: Il calcolo quantifica l'allontanamento quadratico dal centro.
- Nodo Esplosione: Il parametro scala con il quadrato del coefficiente moltiplicativo.
- Nodo Traslazione: Il parametro ignora totalmente l'aggiunta di costanti fisse.

### Disuguaglianze Notevoli
> [!ABSTRACT] 
> Le Disuguaglianze pongono un limite al disastro estremo. Fissano un tetto massimo alle probabilità di eventi rari senza nemmeno conoscere la PMF esatta.
> [!QUOTE] 
> Markov: $P(X \geq \delta) \leq \frac{E[X]}{\delta}$ (per variabili non negative). Chebyshev: $P(|X - \mu_X| \geq k\sigma_X) \leq \frac{1}{k^2}$.
> [!EXAMPLE] 
> Costruisci un grande recinto per le pecore. Non sai dove pascolano di preciso le pecore. Chebyshev ti garantisce matematicamente che quasi nessuna pecora scappa fuori da un recinto molto largo, qualunque sia il comportamento imprevedibile del gregge.
> [!DANGER] 
> Credere che le disuguaglianze forniscano probabilità esatte. Le formule generano limiti ultra-conservativi d'emergenza. Il valore reale risulta sempre drasticamente più basso del limite matematico.

- Nodo Markov: La disuguaglianza lega la media all'esito estremo superiore.
- Nodo Chebyshev: La disuguaglianza blocca statisticamente i valori fuori dal recinto di sicurezza.
- Nodo Universalità: Il limite resiste matematicamente a ogni tipo di distribuzione strana.

### Modelli Notevoli: Bernoulli e Binomiale
> [!ABSTRACT] 
> Bernoulli fotografa il singolo attimo vitale di successo o fallimento. La Binomiale somma questi singoli successi ripetuti uguali nel tempo.
> [!QUOTE] 
> Bernoulli: Alfabeto $\{0,1\}$, $E[X] = p$. Binomiale: Somma di $n$ Bernoulli indipendenti. $P(S_n = k) = \binom{n}{k} p^k (1-p)^{n-k}$, $E[S_n] = np$.
> [!EXAMPLE] 
> Tira un singolo rigore. Fai gol (1) o sbagli (0). Questa è Bernoulli pura. Tira dieci rigori consecutivi uguali. Conta i gol totali fatti. Questa è la Binomiale aggregata.
> [!DANGER] 
> Confondere la successione ordinata con l'insieme disordinato. Il coefficiente binomiale raggruppa le sequenze con lo stesso numero di successi ma in ordine diverso. Ometterlo fa crollare tutto il conto della probabilità.

- Nodo Scelta: L'esperimento fissa l'esito puramente binario.
- Nodo Replica: La sequenza ripete l'esperimento isolato alle stesse condizioni.
- Nodo Accumulo: La formula somma matematicamente i successi totali ottenuti.

### Modelli Notevoli: Uniforme Discreta e Poisson
> [!ABSTRACT] 
> L'Uniforme appiattisce ogni opzione alla stessa probabilità. Poisson conta gli eventi rari e imprevedibili che piovono in un intervallo di tempo.
> [!QUOTE] 
> Uniforme: $p_X(x) = \frac{1}{M}$, $E[X] = \frac{M+1}{2}$. Poisson: Alfabeto $\mathbb{N}_0$, $P(X = k) = \frac{\lambda^k}{k!} e^{-\lambda}$, $E[X] = \lambda$.
> [!EXAMPLE] 
> L'Uniforme lancia un dado perfetto: ogni faccia vale un sesto. Poisson osserva un casello autostradale di notte: conta quante rare auto passano in una specifica ora buia.
> [!DANGER] 
> Usare Poisson per eventi frequenti. Poisson modella esclusivamente il limite in cui i tentativi tendono all'infinito ma la probabilità singola tende a zero, mantenendo una media costante.

- Nodo Appiattimento: L'uniforme assegna lo stesso peso identico a ogni esito.
- Nodo Rarità: Poisson conta fenomeni isolati estremi in un lasso temporale.
- Nodo Limite: Poisson approssima la Binomiale per grandi numeri e basse probabilità.

### Modelli Notevoli: Geometrica
> [!ABSTRACT] 
> La Geometrica conta l'attesa logorante. Misura quanti tentativi falliti devi sopportare prima di assaporare il primo successo.
> [!QUOTE] 
> Formula: $P(X = k) = (1-p)^{k-1} p$. Alfabeto: $\mathbb{N}_{>0}$. Media: $E[X] = \frac{1}{p}$. Proprietà: Assenza di memoria $P(X > n+m \mid X > n) = P(X > m)$.
> [!EXAMPLE] 
> Compra biglietti del gratta e vinci. Continua a comprare biglietti finché non trovi finalmente quello vincente. La Geometrica si ferma esattamente al primo premio.
> [!DANGER] 
> Dimenticare l'Assenza di Memoria. Fallire dieci volte non aumenta minimamente le tue chance all'undicesimo tentativo. Il passato muore istantaneamente ad ogni nuovo tentativo.

- Nodo Attesa: La funzione traccia il percorso continuo verso il primo successo.
- Nodo Amnesia: Il sistema distrugge la memoria dei tentativi passati falliti.
- Nodo Coda: La probabilità decresce esponenzialmente al crescere dei fallimenti.

## Variabili Multiple Discrete e Informazione

### PMF Congiunta Bivariata
> [!ABSTRACT] 
> La PMF congiunta osserva due fenomeni simultanei incrociati. Usa una scacchiera per mappare la probabilità di ogni combinazione possibile.
> [!QUOTE] 
> Definizione: $p_{XY}(x,y) = P(X=x, Y=y)$. Normalizzazione: $\sum_x \sum_y p_{XY}(x,y) = 1$.
> [!EXAMPLE] 
> Compila un foglio Excel. Usa le righe per l'età e le colonne per l'altezza. Incrocia le celle. Ogni cella contiene la probabilità esatta di pescare una persona con quella specifica età e altezza contemporaneamente.
> [!DANGER] 
> Ricavare la congiunta dalle marginali. Non puoi mai unire due marginali per ricavare la congiunta, a meno che le variabili siano dimostratamente indipendenti. L'operazione isolata cancella le informazioni di legame.

- Nodo Tabella: La matrice mappa l'intersezione pura degli eventi.
- Nodo Dipendenza: La griglia blocca il comportamento incrociato delle due variabili.

### Marginalizzazione
> [!ABSTRACT] 
> La marginalizzazione schiaccia la scacchiera in una sola linea. Cancella una dimensione sommando tutti i valori lungo di essa.
> [!QUOTE] 
> Formula $X$: $p_X(x) = \sum_y p_{XY}(x,y)$. Formula $Y$: $p_Y(y) = \sum_x p_{XY}(x,y)$. Come valore atteso: $p_X(x) = E_Y[p_{X|Y}(x \mid Y)]$.
> [!EXAMPLE] 
> Prendi il foglio Excel di prima. Somma tutti i numeri di una singola riga (tutte le altezze per una singola età) e scrivi il totale alla fine della riga. Hai appena schiacciato l'altezza, trovando la probabilità marginale dell'età.
> [!DANGER] 
> Dimenticare che la marginalizzazione è un'operazione distruttiva a senso unico. Dalla congiunta trovi sempre le marginali. Dalle marginali non puoi quasi mai tornare alla congiunta.

- Nodo Schiacciamento: La somma distrugge fisicamente una dimensione della matrice.
- Nodo Proiezione: L'operatore estrae la singola variabile dal contesto multiplo.

### PMF Condizionale
> [!ABSTRACT] 
> La PMF condizionale isola una singola riga della scacchiera e la trasforma in un nuovo universo indipendente a sé stante.
> [!QUOTE] 
> Formula: $p_{X|Y}(x|y) = \frac{p_{XY}(x,y)}{p_Y(y)}$ per $p_Y(y) > 0$. Somma sulle colonne: $\sum_x p_{X|Y}(x|y) = 1$.
> [!EXAMPLE] 
> Fissa un'altezza precisa sul foglio Excel (es. 180cm). Ignora tutte le altre colonne. Prendi i numeri di quella singola colonna e dividili per il loro totale. Ora hai una probabilità valida solo per chi è alto 180cm.
> [!DANGER] 
> Sommare lungo la dimensione sbagliata. Una tabella condizionale $p_{X|Y}(x|y)$ somma a uno solo muovendosi su $x$ tenendo fermo $y$. Se muovi $y$, i numeri non formano una probabilità valida.

- Nodo Isolamento: La condizione blocca una variabile a un valore costante.
- Nodo Riscalamento: La divisione ripristina la somma finale a uno.

### Regola della Catena e Modelli di Markov
> [!ABSTRACT] 
> La regola della catena scompone un evento simultaneo complesso in una sequenza temporale di eventi condizionati uno dopo l'altro. Markov semplifica la catena ricordando solo l'ultimo passo.
> [!QUOTE] 
> Catena Generale: $p(x,y,z) = p(z) \cdot p(y|z) \cdot p(x|y,z)$. Catena di Markov: $P(X_{n+1} | X_n, X_{n-1}, \dots) = P(X_{n+1} | X_n)$.
> [!EXAMPLE] 
> Gioca a Monopoli. Il tiro attuale determina la tua prossima posizione. Non importa affatto come sei arrivato in quella specifica casella dieci turni prima. Il presente contiene tutto ciò che serve per il futuro. Questo è Markov.
> [!DANGER] 
> Applicare Markov a sistemi con memoria a lungo termine. Se estrai carte da un mazzo senza rimetterle dentro, la decima carta dipende da tutte le prime nove, non solo dalla nona.

- Nodo Scomposizione: La regola frammenta la probabilità congiunta in passaggi sequenziali.
- Nodo Miopia: Markov taglia via tutta la storia remota del processo.
- Nodo Stato: Il presente assorbe tutta l'informazione storica rilevante.

### Covarianza e Correlazione
> [!ABSTRACT] 
> La Covarianza misura quanto due fenomeni si muovono insieme. La Correlazione è la stessa misura ma con un limite fisso di velocità tra -1 e +1.
> [!QUOTE] 
> Covarianza: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$. Correlazione: $\rho_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}$ con $-1 \leq \rho_{XY} \leq 1$.
> [!EXAMPLE] 
> Osserva temperatura e vendita di gelati. Salgono insieme: covarianza positiva. Osserva temperatura e vendita di stufe. Una sale e l'altra scende: covarianza negativa. Osserva temperatura e numero di scarpe. Nessun legame logico: covarianza vicina a zero.
> [!DANGER] 
> Assumere che incorrelazione significhi indipendenza. Due variabili possono viaggiare su una parabola perfetta (dipendenza totale) ma risultare matematicamente incorrelate. Solo nel caso gaussiano coincidono.

- Nodo Sincronia: L'operatore quantifica il movimento accoppiato delle variabili.
- Nodo Normalizzazione: Il coefficiente schiaccia il risultato tra valori assoluti limite.
- Nodo Linearità: La correlazione rileva esclusivamente dipendenze puramente lineari.

### Entropia di Shannon
> [!ABSTRACT] 
> L'Entropia misura l'incertezza media di un'intera sorgente di dati. Indica quanti bit ti servono per comprimere quel messaggio al limite estremo.
> [!QUOTE] 
> Informazione di evento: $I(x) = -\log_2 P(x)$ [bit]. Entropia: $H(X) = E[-\log_2 p_X(X)] = -\sum p_X(x) \log_2 p_X(x)$. Limite: $0 \leq H(X) \leq \log_2 |\mathcal{X}|$.
> [!EXAMPLE] 
> Comprimi un file di testo pieno di 'A'. Non c'è sorpresa, l'entropia è zero, lo comprimi in un morso. Comprimi un file di numeri casuali totali. L'entropia è massima, il programma ZIP non riesce a comprimerlo di un singolo byte.
> [!DANGER] 
> Confondere entropia termodinamica ed entropia informazionale. Quella informazionale riguarda unicamente la probabilità dei simboli emessi dalla sorgente.

- Nodo Bit: Il logaritmo calcola la lunghezza del messaggio in bit ottimali.
- Nodo Media: L'entropia pesa ogni sorpresa con la sua frequenza reale.
- Nodo Uniformità: Il massimo disordine si raggiunge con probabilità tutte identiche.

### Canale Binario Simmetrico (BSC)
> [!ABSTRACT] 
> Il BSC è il peggior incubo di chi trasmette dati. Prende un bit e, ogni tanto, lo capovolge a tradimento durante il viaggio.
> [!QUOTE] 
> Probabilità di crossover: $P(Y=0|X=1) = P(Y=1|X=0) = \varepsilon$. Probabilità di errore complessiva: $P_e = \varepsilon$.
> [!EXAMPLE] 
> Grida un messaggio in una stanza molto rumorosa. Tu dici "Sì" (1). Il rumore distorce la parola e l'altra persona sente "No" (0). La probabilità $\varepsilon$ misura quanto è forte questo rumore.
> [!DANGER] 
> Pensare che il danno massimo avvenga quando $\varepsilon = 1$. Se il canale inverte sempre ($\varepsilon = 1$), tu semplicemente reinverti il messaggio all'arrivo e recuperi tutto. Il danno massimo assoluto è $\varepsilon = 1/2$, dove ogni bit è pura casualità sganciata dall'input.

- Nodo Rumore: Il canale inverte fisicamente il bit trasmesso in ricezione.
- Nodo Simmetria: Il difetto colpisce ugualmente sia gli zeri che gli uni.
- Nodo Caos: Il canale con probabilità un mezzo azzera completamente il trasferimento informativo.

## Variabili Aleatorie Continue

### Dal Discreto al Continuo
> [!ABSTRACT] 
> Nel continuo i numeri sono infiniti e attaccati. La probabilità che esca un numero spaccato esatto è matematicamente nulla. L'incertezza abbandona il singolo punto per abbracciare l'intervallo.
> [!QUOTE] 
> Proprietà continua: $P(X = x) = 0$ per ogni singolo $x \in \mathbb{R}$. La probabilità esiste solo su intervalli: $P(a \leq X \leq b)$.
> [!EXAMPLE] 
> Taglia un filo d'erba a caso. Qual è la probabilità che misuri esattamente, al millesimo di micron, 4,0000... centimetri? Zero assoluto. La domanda corretta è: "Qual è la probabilità che misuri tra i 3 e i 5 centimetri?".
> [!DANGER] 
> Assegnare una probabilità fissa a un singolo valore continuo. Il calcolo discreto applicato al continuo fa esplodere i paradossi. Tratta sempre intervalli, anche sottilissimi.

- Nodo Infinito: L'asse reale contiene una densità inesauribile di punti inseparabili.
- Nodo Zero: Il singolo valore assume una probabilità puntuale rigorosamente nulla.
- Nodo Intervallo: L'operatore sposta la misurazione fisica dai punti ai segmenti continui.

### Cumulative Distribution Function (CDF)
> [!ABSTRACT] 
> La CDF accumula la probabilità spazzando l'asse da sinistra verso destra. È la memoria progressiva di tutta l'incertezza raccolta finora.
> [!QUOTE] 
> Definizione: $F_X(x) = P(X \leq x)$. Condizioni: $F_X(-\infty) = 0$, $F_X(+\infty) = 1$. L'intervallo vale $P(a < X \leq b) = F_X(b) - F_X(a)$.
> [!EXAMPLE] 
> Riempi una piscina col tubo. L'asse orizzontale è il tempo. L'asse verticale è il livello dell'acqua. La CDF rappresenta esattamente l'altezza dell'acqua. Parte dal fondo e sale fino al bordo pieno. Non scende mai.
> [!DANGER] 
> Dimenticare che la CDF cresce monotonamente. Se disegni una CDF e la curva si abbassa anche solo di un millimetro, hai sbagliato clamorosamente l'integrale.

- Nodo Accumulo: La funzione somma integralmente tutta la probabilità pregressa sinistra.
- Nodo Monotonia: Il grafico sale inesorabilmente senza compiere passi indietro.
- Nodo Sottrazione: La differenza tra due punti fornisce la probabilità interna esatta.

### Probability Density Function (PDF)
> [!ABSTRACT] 
> La PDF mostra dove la probabilità si concentra spazialmente. Non misura una percentuale diretta, misura un peso per unità di lunghezza.
> [!QUOTE] 
> Definizione derivata: $f_X(x) = \frac{d}{dx} F_X(x)$. Area probabilistica: $P(a \leq X \leq b) = \int_a^b f_X(x) \, dx$. Normalizzazione: $\int_{-\infty}^{+\infty} f_X(x) \, dx = 1$.
> [!EXAMPLE] 
> Distribuisci sabbia su un lungo tavolo. L'altezza del mucchio in un punto esatto è la PDF. Non pesa nulla finché non raccogli un pezzetto di tavolo. L'altezza del mucchio può superare i due metri, ma la sabbia totale pesa invariabilmente un chilo spaccato.
> [!DANGER] 
> Spaventarsi se $f_X(x) > 1$. La PDF è una densità fisica. Come il piombo affonda, la PDF può superare uno se si concentra su una base cortissima.

- Nodo Derivata: La funzione traccia la pendenza istantanea della curva di riempimento.
- Nodo Densità: Il grafico misura la concentrazione spaziale materiale dell'incertezza.
- Nodo Integrale: L'area geometrica sottesa genera la percentuale probabilistica finale.

### Modelli Continui: Uniforme ed Esponenziale
> [!ABSTRACT] 
> L'Uniforme appiattisce le chance creando un blocco perfetto. L'Esponenziale è uno scivolo ripido che divora l'attesa ignorando il tempo già passato.
> [!QUOTE] 
> Uniforme $U(a,b)$: $f_X(x) = \frac{1}{b-a}$, Media $E[X] = \frac{a+b}{2}$. Esponenziale Exp$(\lambda)$: $f_X(x) = \lambda e^{-\lambda x}$ per $x \geq 0$, Media $E[X] = \frac{1}{\lambda}$.
> [!EXAMPLE] 
> L'Uniforme spalma la vernice in modo piatto su un muro delimitato. Nessun punto spicca. L'Esponenziale modella una lampadina accesa: il fatto che abbia già funzionato cento giorni non ti regala mezza informazione su quando si fulminerà.
> [!DANGER] 
> Confondere il parametro $\lambda$ con il valore medio. Nell'Esponenziale la media è il reciproco esatto $1/\lambda$. Se $\lambda$ aumenta, la curva si impenna e l'attesa media crolla a picco.

- Nodo Appiattimento: L'uniforme livella il peso geometricamente su tutto l'intervallo vincolato.
- Nodo Attesa: L'esponenziale modella il logoramento temporale verso l'evento finale.
- Nodo Amnesia: Il sistema distrugge irrimediabilmente tutta la storia passata pregressa.

### Modelli Continui: Laplace (Doppia Esponenziale)
> [!ABSTRACT] 
> Laplace incolla due rampe esponenziali schiena contro schiena. Modella gli scossoni improvvisi che esplodono casualmente in direzioni opposte.
> [!QUOTE] 
> Distribuzione Laplace$(\lambda)$: $f_X(x) = \frac{\lambda}{2} e^{-\lambda|x|}$. Media: $E[X] = 0$. Varianza: $\text{Var}(X) = \frac{2}{\lambda^2}$.
> [!EXAMPLE] 
> Ascolta la radio con fortissima interferenza elettrostatica (rumore atmosferico palese). Senti dei picchi acustici estremi, i "crack". La campana Gaussiana fatica a reggere questi sbalzi. Laplace li inquadra perfettamente allargando le "code".
> [!DANGER] 
> Dimenticare il modulo del valore assoluto nella formula esatta. La formula blocca l'incrocio con $|x|$ perché il rumore sbatte simmetricamente sia nell'emisfero positivo che in quello negativo.

- Nodo Specchio: La funzione simmetrizza il decadimento esponenziale incollato allo zero centrale.
- Nodo Impulso: Il modello inquadra perturbazioni esterne massicce e totalmente improvvise.
- Nodo Coda: La densità periferica mantiene una consistenza inattesa alle distanze massime.

### Variabili Bivariate: Densità Congiunta
> [!ABSTRACT] 
> Il mondo bivariato fa interagire due variabili innalzando una montagna volumetrica 3D sopra un tappeto piano bidimensionale.
> [!QUOTE] 
> PDF Congiunta: $f_{X,Y}(x, y) \geq 0$. Volume totale: $\iint f_{X,Y}(x, y) \, dx \, dy = 1$. Probabilità spaziale $C$: $P((X,Y) \in C) = \iint_C f_{X,Y}(x,y) \, dx\, dy$.
> [!EXAMPLE] 
> Modella un deserto quadrato. Soffia vento e crea una singola enorme duna di sabbia. L'altezza in ogni coordinate x,y è la densità congiunta locale. Puoi spostare la sabbia, ma il volume globale misura eternamente uno.
> [!DANGER] 
> Distrarsi sugli estremi degli integrali doppi incatenati. L'integrale non disegna quasi mai un quadrato comodo. Spesso $y$ dipenderà attivamente da $x$, tracciando confini triangolari o curvi. Vigila ossessivamente i limiti.

- Nodo Duna: La densità congiunta innalza un blocco tridimensionale compatto e unitario.
- Nodo Superficie: Il calcolo spaziale proietta il volume totale misurandolo sopra una regione vincolata.
- Nodo Schiacciamento: L'integrazione marginale pressa irrimediabilmente la montagna 3D sul singolo asse isolato.

### Densità Condizionale Continua
> [!ABSTRACT] 
> Prendi un coltello laser e affetta la montagna 3D da parte a parte. Conservi il profilo bidimensionale del taglio svelandone una nuova PDF purificata.
> [!QUOTE] 
> Formula di taglio: $f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$. Condizione stretta: si calcola solo se il denominatore supera strettamente lo zero.
> [!EXAMPLE] 
> Prendi la duna di sabbia 3D. Affonda una lastra di vetro verticale sull'asse Y (bloccando l'età a 25 anni esatti). Butta via tutto il resto del deserto. Il profilo di sabbia pressato sul vetro è la PDF condizionale dell'altezza. Riscalala verso l'alto per far valere uno la sua area.
> [!DANGER] 
> Dividere inavvertitamente per la variabile sbagliata. Al denominatore devi parcheggiare unicamente la densità marginale della specifica variabile che funge da condizione esatta e congelata.

- Nodo Lama: La condizione blocca una variabile tagliando trasversalmente il volume spaziale.
- Nodo Gonfiaggio: La divisione forza l'area della sezione compressa a gonfiarsi fino al valore base uno.
- Nodo Disconnessione: Il blocco congiunto si disintegra in frammenti isolati se le variabili sottostanti si ignorano.

## Vettori, Processi e Inferenza Statistica

### Vettore Gaussiano
> [!ABSTRACT] 
> Il vettore Gaussiano è un ecosistema compatto di variabili normali. Se le sue componenti smettono di rincorrersi linearmente, diventano matematicamente indipendenti in modo assoluto.
> [!QUOTE] 
> Parametri: Vettore media $\mathbf{\mu}$ e matrice di covarianza $K_X$. Formula: $f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{\sqrt{(2\pi)^n |K_X|}} \exp\left(-\frac{1}{2}(\mathbf{x}-\mathbf{\mu})^T K_X^{-1} (\mathbf{x}-\mathbf{\mu})\right)$.
> [!EXAMPLE] 
> Disegna un bersaglio circolare per le freccette. Se tiri bendato, i colpi si accumulano formando una campana tridimensionale concentrata al centro. Questa è una Gaussiana bivariata perfetta.
> [!DANGER] 
> Dimenticare la potenza distruttiva della matrice di covarianza. Se la matrice $K_X$ diventa puramente diagonale (covarianze zero), le variabili si scollegano immediatamente e la funzione esponenziale si spezza in blocchi autonomi.

- Nodo Ecosistema: Il vettore raggruppa campane singole in una rigida struttura multivariata.
- Nodo Matrice: La covarianza detta la rotazione spaziale e lo schiacciamento della campana 3D.
- Nodo Scorciatoia: L'incorrelazione garantisce automaticamente l'indipendenza statistica totale.

### Processi Casuali e Stazionarietà
> [!ABSTRACT] 
> Un processo casuale spara non un singolo numero, ma un intero film continuo nel tempo. La stazionarietà impone che la trama del film non cambi mai, indipendentemente da quando inizi a guardarlo.
> [!QUOTE] 
> Stazionarietà Senso Stretto (SSS): $f_{X}(x_1, \dots, x_n; t_1, \dots, t_n) = f_{X}(x_1, \dots, x_n; t_1+\tau, \dots, t_n+\tau)$. Stazionarietà Senso Lato (WSS): $\mu_X(t)$ costante, $R_X(t, t+\tau) = R_X(\tau)$.
> [!EXAMPLE] 
> Sintonizza una radio rotta sul rumore bianco. Ascolta il fischio oggi, o ascoltalo domani. Suona identico. Le statistiche del suono non invecchiano minimamente. Questo è un processo stazionario.
> [!DANGER] 
> Confondere SSS e WSS. La WSS blocca e stabilizza solo i primi due momenti base (media e autocorrelazione). La SSS blocca rigorosamente tutta la densità di probabilità infinita, rendendole identiche in ogni istante.

- Nodo Segnale: L'esperimento genera un'intera funzione imprevedibile variabile nel tempo continuo.
- Nodo Invecchiamento: Il processo stazionario congela temporalmente le leggi statistiche impedendone l'evoluzione.
- Nodo Rilassamento: La stazionarietà debole controlla esclusivamente media e forma dell'autocorrelazione.

### Ergodicità
> [!ABSTRACT] 
> L'ergodicità scambia miracolosamente il tempo con lo spazio. Osservare un singolo processo per un tempo infinito equivale a osservare infiniti processi diversi nello stesso istante.
> [!QUOTE] 
> Condizione Ergodica: La media temporale infinita del singolo segnale $\langle x(t) \rangle$ converge in probabilità alla media statistica canonica d'insieme $E[X(t)]$.
> [!EXAMPLE] 
> Vuoi calcolare il lancio medio di un dado per mille persone. Puoi chiedere a mille persone di lanciare un dado adesso. Oppure puoi chiudere una singola persona in una stanza e farle lanciare un dado mille volte di fila. Il risultato finale coincide.
> [!DANGER] 
> Assumere ergodicità automatica per sistemi bloccati. Se tiri una moneta truccata una volta sola e tieni in mano quel risultato per sempre (es. segnale costante $X(t)=A$), il segnale nel tempo non esplora il mondo circostante. Fallisce l'ergodicità.

- Nodo Scambio: L'infinito temporale della singola traccia sostituisce l'infinito spaziale dell'universo.
- Nodo Esplorazione: Il singolo segnale deve visitare fisicamente tutte le combinazioni probabilistiche possibili.
- Nodo Praticità: Il teorema sblocca il calcolo statistico teorico usando una singola misurazione empirica pratica.

### Inferenza Statistica: La Sfida
> [!ABSTRACT] 
> L'inferenza inverte il lavoro della probabilità classica. Non prevede i risultati avendo in mano il modello matematico, ma ricostruisce il modello cieco guardando i risultati fisici.
> [!QUOTE] 
> Elementi: Spazio dei parametri nascosti $\Theta$. Vettore osservazione concreta $\mathbf{x}$. Stimatore deduttivo $\hat{\theta}(\mathbf{x})$.
> [!EXAMPLE] 
> Trovi un dado scalfito per strada. Lo lanci cento volte e scrivi i numeri (dati). L'algoritmo di inferenza osserva i cento numeri e indovina esattamente i grammi di piombo nascosti nel dado (parametro).
> [!DANGER] 
> Confondere la stima calcolata con il parametro reale. Il parametro è la verità divina, fissa, statica e invisibile. La stima è la nostra congettura umana, calcolata, variabile e dipendente dal campione.

- Nodo Ricostruzione: L'algoritmo matematico deduce la causa invisibile direttamente dall'effetto visibile.
- Nodo Parametro: Il numero fisso governa segretamente l'intera generazione dei dati empirici.
- Nodo Stimatore: La funzione algoritmica tenta di indovinare chirurgicamente il parametro occulto.

### Distorsione (Bias) e Consistenza
> [!ABSTRACT] 
> Il Bias misura freddamente se la tua pistola spara storta di fabbrica. La Consistenza garantisce che, pompando infiniti dati, la stima distruggerà ogni incertezza collassando sul parametro perfetto.
> [!QUOTE] 
> Bias: $B(\hat{\theta}) = E[\hat{\theta}] - \theta$. Stimatore Corretto: $B(\hat{\theta}) = 0$. Consistenza asintotica in probabilità: $\lim_{n \to \infty} P(|\hat{\theta}_n - \theta| > \epsilon) = 0$.
> [!EXAMPLE] 
> Usa una bilancia collaudata male in fabbrica che aggiunge sempre un chilo netto. Pesa mille persone diverse e fai la media temporale. Otterrai una stima stabilissima, ma sbagliata inesorabilmente di un chilo. Questo è il Bias sistemico.
> [!DANGER] 
> Fissarsi rigidamente sul singolo campione empirico. Uno stimatore perfettamente corretto può sbagliare miseramente ogni singola misurazione pratica. Garantisce matematicamente solo che la media degli infiniti errori si annulli al centro.

- Nodo Distorsione: L'errore sistematico devia costantemente l'algoritmo dal centro esatto.
- Nodo Correttezza: L'operatore centra matematicamente il parametro occulto compensando infiniti tentativi.
- Nodo Consistenza: L'accumulo infaticabile di dati annienta inesorabilmente la varianza e l'incertezza residua.

### Errore Quadratico Medio (MSE)
> [!ABSTRACT] 
> L'MSE penalizza ferocemente gli errori grossolani. Valuta in un colpo solo sia la mira storta della pistola (Bias) sia il tremore insicuro della mano che spara (Varianza).
> [!QUOTE] 
> Definizione: $MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2]$. Scomposizione aurea infallibile: $MSE(\hat{\theta}) = \text{Var}(\hat{\theta}) + [B(\hat{\theta})]^2$.
> [!EXAMPLE] 
> Valuta un arciere. Non guardi solo se colpisce il centro in media (Bias nullo). Guardi anche se le frecce formano un gruppo strettissimo o cadono sparse a caso (Varianza elevata). L'MSE boccia inflessibilmente l'arciere incostante.
> [!DANGER] 
> Ignorare il fatale compromesso Bias-Varianza. Sovente conviene progettare uno stimatore leggermente fuori centro (piccolo Bias) ma d'acciaio (bassissima Varianza), rifiutando uno stimatore precisissimo ma totalmente inaffidabile.

- Nodo Penalità: Il quadrato punisce severamente e asimmetricamente gli scarti massicci.
- Nodo Scomposizione: Il punteggio somma matematicamente il difetto cronico di mira e l'instabilità del braccio.
- Nodo Bilanciamento: L'algoritmo sacrifica strategicamente la correttezza pura per abbattere la varianza distruttiva.

### Stima di Massima Verosimiglianza (MLE)
> [!ABSTRACT] 
> L'MLE abbraccia il parametro che rende i dati osservati la cosa meno sorprendente dell'universo. Sceglie l'ipotesi che massimizza brutalmente l'ovvietà dei fatti.
> [!QUOTE] 
> Funzione Likelihood: $L(\theta) = f_{\mathbf{X}}(\mathbf{x}; \theta)$. Calcolo log-MLE: $\hat{\theta}_{ML} = \arg\max_\theta \ln L(\theta)$.
> [!EXAMPLE] 
> Entri in salotto e vedi il vaso in frantumi. Opzione A: il gatto saltato sul tavolo. Opzione B: un meteorite. L'MLE seleziona istantaneamente il gatto, perché l'ipotesi "gatto" rende il vaso rotto infinitamente più probabile dell'ipotesi "meteorite".
> [!DANGER] 
> Trattare la verosimiglianza Likelihood come una probabilità diretta del parametro. Il parametro non oscilla, non è una variabile aleatoria in questo mondo frequentista. Tu calcoli la probabilità passata *dei dati* fissando il parametro, non il contrario.

- Nodo Ovvietà: Il calcolo seleziona l'ipotesi teorica che giustifica i dati inoppugnabili già raccolti.
- Nodo Logaritmo: L'operatore inietta la monotonia per trasformare scomodi prodotti in pratiche somme, disinnescando gli esponenziali.
- Nodo Gradiente: L'azzeramento della derivata prima individua matematicamente il picco massimo della collina.

### Stima MAP (Maximum A Posteriori) e MMSE
> [!ABSTRACT] 
> Il MAP aggiunge prepotentemente i tuoi antichi pregiudizi all'MLE. L'MMSE rinuncia ai picchi e si concentra sul baricentro dell'area probabilistica per minimizzare lo scarto quadrato.
> [!QUOTE] 
> Teorema Bayes: $f_{\Theta|\mathbf{X}}(\theta|\mathbf{x}) \propto f_{\mathbf{X}|\Theta}(\mathbf{x}|\theta) \cdot f_{\Theta}(\theta)$. Formula MAP: $\arg\max_\theta f_{\Theta|\mathbf{X}}(\theta|\mathbf{x})$. Formula MMSE: $\hat{\theta}_{MMSE} = E[\Theta | \mathbf{X} = \mathbf{x}]$.
> [!EXAMPLE] 
> Il radar individua un veicolo estremamente veloce in cielo. L'MLE grida: "Vola a Mach 3, è un UFO alieno". Il MAP analizza il registro di volo e risponde: "In quest'area testano aerei segreti (pregiudizio a priori massiccio). È solo un caccia militare".
> [!DANGER] 
> Ignorare l'impatto della PDF a priori $f_{\Theta}(\theta)$. Se il tuo pregiudizio iniziale è totalmente piatto (ignoranza completa e uniforme), il MAP perde la sua bussola a priori e collassa diventando l'ombra matematica esatta dell'MLE.

- Nodo Pregiudizio: L'informazione storica pregressa inquina volontariamente l'oggettività dei dati correnti.
- Nodo Vetta: L'algoritmo MAP scala e pianta la bandiera sul picco più alto della nuova probabilità a posteriori.
- Nodo Equilibrio: L'algoritmo MMSE calcola e inchioda il baricentro esatto della nuova massa probabilistica.
- Nodo Fusione: Il modello Gaussiano allinea magicamente il picco estetico MAP col baricentro solido MMSE.
