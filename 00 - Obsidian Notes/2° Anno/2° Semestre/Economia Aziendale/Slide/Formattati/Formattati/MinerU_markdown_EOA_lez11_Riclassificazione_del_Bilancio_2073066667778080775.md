# Lezione 11 - Riclassificare il bilancio

## 1. Introduzione alla riclassificazione del bilancio

Il concetto di **riclassificazione del bilancio** emerge dalla necessità di gestire la dinamicità delle risorse finanziarie e degli obiettivi di un'organizzazione nel tempo. In ambito informatico e gestionale, questo processo si traduce nella capacità di riallocare dati strutturati (budget, asset, debiti) tra diverse categorie o periodi in base a nuove priorità o variazioni di stato.

> [!important] Riclassificazione del Bilancio
> **Definizione**: È l'operazione di spostamento di una voce contabile o di un'allocazione di risorse da una categoria di destinazione (es. "Progetti in corso") a una diversa (es. "Riserve" o "Costi fissi"), mantenendo invariato il totale complessivo del bilancio ma modificandone la distribuzione interna.
> 
> **Formalizzazione**: Dato un bilancio $B$ espresso come un vettore di categorie $\mathbf{v} = [c_1, c_2, \dots, c_n]$, la riclassificazione è una trasformazione $\mathcal{R}$ tale che:
> $$\sum_{i=1}^{n} v_i = \sum_{i=1}^{n} \mathcal{R}(v)_i$$
> dove per ogni operazione di spostamento di un valore $\Delta$ dalla categoria $j$ alla categoria $k$:
> $$c_j' = c_j - \Delta$$
> $$c_k' = c_k + \Delta$$

### Perché serve
Senza la riclassificazione, un bilancio rimarrebbe statico e incapace di riflettere la realtà operativa. Se un progetto viene annullato o una risorsa viene spostata da un investimento a una spesa di manutenzione, il sistema deve essere in grado di aggiornare le etichette senza "perdere" i soldi dal conteggio totale. Serve quindi a garantire l'integrità del dato finanziario durante i cambiamenti di strategia.

### Esempio concreto
Immaginiamo un dipartimento IT che ha stanziato 10.000 € per l'acquisto di nuovi server (Categoria: *Hardware*). A metà anno, si decide di non acquistare i server fisici ma di migrare su un servizio Cloud. La riclassificazione consiste nel sottrarre 10.000 € dalla categoria *Hardware* e aggiungerli alla categoria *Servizi Cloud*. Il bilancio totale rimane invariato, ma la distribuzione delle voci riflette la nuova scelta tecnologica.

### Derivazione
Consideriamo un bilancio iniziale $B_0$ composto da $n$ categorie. Ogni categoria $i$ ha un valore $v_i$.
1. Si identifica la necessità di spostare una quantità $\Delta$ dalla categoria sorgente $j$ alla categoria destinazione $k$.
2. Si verifica che $\Delta \leq v_j$ per garantire che la categoria sorgente non diventi negativa (vincolo di consistenza).
3. Si applica l'operatore di aggiornamento:
   - Per ogni $i \neq j, k$, il valore rimane invariato: $v_i' = v_i$.
   - Per la categoria sorgente: $v_j' = v_j - \Delta$.
   - Per la categoria destinazione: $v_k' = v_k + \Delta$.
4. Si verifica l'invarianza della somma totale:
   $$\sum v_i' = (v_j - \Delta) + (v_k + \Delta) + \sum_{i \neq j, k} v_i = \sum v_i$$

### Formule chiave
> [!important] Riepilogo Operazioni
> $$c_j^{new} = c_j^{old} - \Delta$$
> $$c_k^{new} = c_k^{old} + \Delta$$
> $$\text{Vincolo: } \sum c_i^{old} = \sum c_i^{new}$$

### Collegamenti
Richiede: Concetti base di bilancio e vettori di allocazione. Usato in: Analisi delle varianze, pianificazione finanziaria dinamica e gestione dei progetti software.

> [!warning] Attenzione
> Un errore comune è confondere la **riclassificazione** con una **variazione di budget**. Nella riclassificazione il totale del bilancio non cambia; in una variazione di budget (es. aumento di fondi esterni), il totale complessivo aumenta o diminuisce. Inoltre, è fondamentale che $\Delta$ sia coerente con le unità di misura della categoria di destinazione.

> [!example] Esercizio 1
> Un'azienda ha un bilancio suddiviso in tre categorie: *Ricerca* (50.000 €), *Marketing* (30.000 €) e *Logistica* (20.000 €). Il totale è di 100.000 €. L'azienda decide di spostare 10.000 € dalla *Ricerca* al *Marketing*.
> 
> **Soluzione**:
> 1. Identificare $\Delta = 10.000$.
> 2. Categoria sorgente $j$ (*Ricerca*): $50.000 - 10.000 = 40.000$.
> 3. Categoria destinazione $k$ (*Marketing*): $30.000 + 10.000 = 40.000$.
> 4. Nuovo bilancio: *Ricerca* (40.000 €), *Marketing* (40.000 €), *Logistica* (20.000 €).
> 5. Verifica totale: $40.000 + 40.000 + 20.000 = 100.000$ (Invariato).

# Corso EOA

**Prof. Giuseppe Piccirillo**

!https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/965dd9f0ba4e47210558a6e47054fb082718dec7e6101f21e753ebe85ea5bb51.png

## 1. Riclassificazione del Conto Economico

La **riclassificazione** consiste nel riorganizzare i dati dello stato patrimoniale e del conto economico attraverso processi di disaggregazione, riaggregazione e riordinamento. L'obiettivo è rendere i dati più leggibili per favorire l'analisi e il confronto tra diverse voci.

> [!important] Riclassificazione del Conto Economico
> La riclassificazione del conto economico è la tecnica di riorganizzazione delle voci di ricavo e costo che permette di evidenziare, sia quantitativamente che qualitativamente, come l'azienda abbia generato il risultato d'esercizio, analizzando l'equilibrio reddituale dell'impresa.

**Perché serve**
Serve a superare la visione puramente contabile del conto economico per ottenere una visione gestionale. Senza di essa, sarebbe difficile distinguere se un profitto derivi dall'attività principale (core business) o da eventi isolati e non ripetibili.

**Esempio concreto**
Un'azienda che produce smartphone potrebbe avere un utile elevato in un anno grazie alla vendita di un terreno improduttivo (gestione straordinaria). La riclassificazione permette di vedere che, nonostante l'utile totale sia positivo, la produzione di smartphone (gestione caratteristica) potrebbe essere in perdita.

**Formule chiave**
| Schema | Componenti Principali |
|:---|:---|
| A fatturato e costo del venduto | Ricavi - Costi Diretti |
| A valore della produzione e valore aggiunto | Valore della Produzione - Consumi Intermedi |

**Collegamenti**
Richiede: Dati dello Stato Patrimoniale e Conto Economico standard. Usato in: Analisi dell'equilibrio reddituale.

> [!warning] Attenzione
> La riclassificazione non modifica i dati di partenza (i totali rimangono invariati), ma ne cambia solo la disposizione logica per fini analitici.

## 2. Aree di Gestione e Core Business

Partendo dal fatturato, il risultato complessivo viene suddiviso in quattro aree fondamentali che separano l'attività principale dalle attività accessorie o finanziarie.

### 2.1 Gestione caratteristica
> [!important] Gestione Caratteristica
> Comprende tutte le attività relative al **core business** dell'impresa, ovvero il processo produttivo principale (acquisto, trasformazione e vendita). Include i ricavi dalle vendite di beni/servizi prodotti e tutti i costi dei fattori produttivi (materie prime, macchinari, personale).

**Perché serve**
Serve a misurare la capacità dell'azienda di generare valore attraverso la sua funzione economica primaria. È l'indicatore principale della sostenibilità del modello di business nel lungo periodo.

**Esempio concreto**
In un'azienda tessile, la gestione caratteristica comprende la vendita dei capi di abbigliamento e i costi per il tessuto, le macchine da cucire e gli stipendi degli operai della produzione.

**Collegamenti**
Richiede: Definizione di Riclassificazione. Usato in: Valutazione del Risultato di Competenza.

### 2.2 Gestione accessoria
> [!important] Gestione Accessoria
> Riguarda le operazioni svolte con continuità che, pur non essendo il core business, sono complementari all'attività operativa principale.

**Perché serve**
Serve a isolare i margini derivanti da attività secondarie (es. affitto di spazi inutilizzati o servizi collaterali) per evitare che "distorcano" la valutazione della performance produttiva principale.

**Esempio concreto**
Un'azienda industriale che, oltre a produrre macchinari, affitta parte del proprio magazzino a terzi per lo stoccaggio merci. L'affitto è un ricavo accessorio.

### 2.3 Gestione finanziaria
> [!important] Gestione Finanziaria
> Comprende tutte le operazioni derivanti dalla raccolta e dall'investimento del capitale. Include oneri da indebitamento (interessi passivi) e proventi da titoli, partecipazioni societarie o depositi bancari.

**Perché serve**
Serve a distinguere il profitto generato dalle attività operative da quello generato dalla gestione dei flussi di cassa e degli investimenti finanziari.

**Collegamenti**
Richiede: Definizione di Riclassificazione.

### 2.4 Gestione straordinaria
> [!important] Gestione Straordinaria
> Riassume le operazioni che determinano proventi o costi non riferibili né alla gestione caratteristica né a quella finanziaria, come plusvalenze/minusvalenze eccezionali o eventi calamitosi (sopravvenienze passive).

**Perché serve**
Serve a "pulire" il risultato operativo da eventi non ripetibili che non riflettono la capacità gestionale ordinaria dell'azienda.

> [!warning] Attenzione
> Un'azienda che genera utili costanti solo tramite la gestione straordinaria è in una situazione di fragilità, poiché non è in grado di mantenersi attraverso la normale operatività.

## 3. Risultato di Competenza

!https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/aa32d2d06ee5c877722041b7a84672b9ca3f50dd682c3d62fe1e7cda512c9f17.jpg

> [!important] Risultato di Competenza
> È il risultato che valuta l'andamento della redditività dell'intera gestione aziendale in un determinato esercizio, al netto delle attività e operazioni che assumono carattere di eccezionalità.

**Perché serve**
È fondamentale per la valutazione della sostenibilità: un'azienda non può sopravvivere a lungo se il suo utile dipende da eventi straordinari frequenti invece che dalla sua normale operatività.

**Esempio concreto**
Se un'azienda ha un utile di 1 milione di euro, ma 900 mila derivano dalla vendita di un impianto obsoleto (straordinario) e solo 100 mila dalla vendita dei prodotti (caratteristico), il Risultato di Competenza evidenzia una criticità strutturale.

**Collegamenti**
Richiede: Gestione Caratteristica, Accessoria, Finanziaria e Straordinaria.

> [!example] Esercizio 1
> Un'azienda manifatturiera registra i seguenti dati in un anno:
> - Vendita prodotti: +500.000 €
> - Costi produzione: -300.000 €
> - Interessi passivi su mutuo: -20.000 €
> - Plusvalenza vendita vecchio ufficio: +100.000 €
> 
> Calcola il Risultato di Competenza e identifica la Gestione Caratteristica.
>
> *Suggerimento: Isola le voci che riguardano il core business e sottrai i costi diretti.*
>
> **Soluzione:**
> 1. Identificazione Gestione Caratteristica: Vendita prodotti (500.000 €) - Costi produzione (300.000 €) = +200.000 €.
> 2. Risultato di Competenza: Si focalizza sulla redditità ordinaria. In questo caso, il risultato derivante dall'attività operativa principale è di 200.000 €. La plusvalenza (100.000 €) e gli interessi (20.000 €) appartengono rispettivamente alla gestione straordinaria e finanziaria e non sono inclusi nel calcolo del risultato di competenza puro della produzione.

# Analisi della Redditività Operativa e Riclassificazione dei Costi

## 1. Il Risultato Operativo (Reddito Operativo)

Il **Risultato Operativo**, spesso denominato anche **Reddito Operativo**, rappresenta la misura della redditività derivante esclusivamente dalla gestione caratteristica dell'azienda. Esso quantifica quanto reddito rimane dopo aver sostenuto i costi operativi e remunerato i fattori produttivi impiegati, indipendentemente dalla struttura finanziaria (es. modalità di finanziamento) o da eventi straordinari.

> [!important] Definizione: Risultato Operativo
> Il **Risultato Operativo** è l'indicatore che misura la capacità dell'azienda di generare profitto attraverso il proprio *core business*. Esso viene calcolato isolando le componenti della gestione ordinaria e ricorrente, sottraendo i costi operativi dai ricavi prodotti dall'attività principale.

Perché serve: Questo indicatore permette di valutare l'efficienza intrinseca del modello di business. Senza di esso, non sarebbe possibile distinguere se un utile sia frutto di una buona gestione produttiva o semplicemente di vantaggi finanziari (es. bassi tassi di interesse) o eventi eccezionali (es. vendita di un immobile).

> [!example] Esempio concreto
> Un'azienda manifatturiera che produce componenti elettronici può avere un utile netto basso a causa di un elevato debito bancario con alti interessi. Tuttavia, se il suo **Risultato Operativo** è alto e positivo, significa che la produzione dei componenti è efficiente e redditizia; il problema risiede nella struttura finanziaria, non nel processo produttivo.

### Derivazione del Risultato Operativo
Il percorso di formazione del risultato operativo segue una logica di sottrazione progressiva dei costi legati alle diverse fasi dell'attività d'impresa:

1.  **Valore della Produzione - Costi della Produzione** = **Risultato Lordo Industriale** (misura la redditività della sola attività industriale).
2.  **Risultato Lordo Industriale - Costi Amministrativi, Distributivi e Commerciali** = **Risultato Operativo**.

> [!important] Formule chiave
> $$ \text{Risultato Lordo Industriale} = \text{Valore della Produzione} - \text{Costi della Produzione} $$
> $$ \text{Risultato Operativo} = \text{Risultato Lordo Industriale} - \text{Costi Amministrativi, Distributivi e Commerciali} $$

**Collegamenti**: Richiede la comprensione del *Valore della Produzione* e dei *Costi della Produzione*. Viene utilizzato per analizzare la redditività del core business prima di considerare gli oneri finanziari e le imposte.

> [!warning] Attenzione
> Non confondere il Risultato Operativo con l'Utile Netto. Il Risultato Operativo non tiene conto degli oneri finanziari (interessi), delle tasse e delle componenti straordinarie, che invece sono presenti nell'utile finale.

---

## 2. Costo del Venduto e Risultato Lordo Industriale

La determinazione del **Costo del Venduto** è il primo passo fondamentale per isolare la redditività industriale. Esso comprende tutte le voci relative al processo di produzione in senso stretto.

> [!important] Definizione: Costo del Venduto
> Il **Costo del Venduto** rappresenta l'insieme dei costi direttamente riconducibili alla trasformazione delle materie prime in prodotti finiti o semilavorati. Comprende la variazione delle scorte, la manodopera diretta, i consumi energetici di produzione e gli ammortamenti industriali.

Perché serve: Serve a determinare quanto costa effettivamente "produrre" un bene. Senza una corretta identificazione del costo del venduto, l'azienda non può conoscere il proprio margine industriale.

> [!example] Esempio concreto
> In una fabbrica di mobili, il costo del venduto include il legno (materie prime), lo stipendio dei falegnami (manodopera), l'elettricità per i macchinari (consumi energetici) e la quota di ammortamento degli impianti di taglio (ammortamenti industriali).

### Componenti del Costo del Venduto
Il costo del venduto è composto dalle seguenti voci:
1.  **Variazione delle scorte**: differenze tra materie prime, prodotti semilavorati e prodotti finiti.
2.  **Costo della manodopera**: salari e contributi del personale direttamente impiegato nella produzione.
3.  **Consumi energetici**: energia elettrica, gas o altri combustibili riconducibili alla produzione.
4.  **Ammortamenti industriali**: quote di costo per beni utilizzati in più esercizi (impianti, macchinari).
5.  **Altri costi diretti**: canoni di affitto/leasing degli impianti, costi dei lavori effettuati da terzi direttamente riferibili alla produzione.

> [!important] Definizione: Risultato Lordo Industriale
> Il **Risultato Lordo Industriale** è l'indicatore che misura la capacità di generare reddito proveniente dalla sola attività industriale, escludendo fattori finanziari, accessori o straordinari.

Perché serve: Permette di capire se il processo produttivo "da solo" è in grado di coprire i propri costi e generare un margine prima ancora di considerare le spese di vendita e amministrazione.

> [!example] Esempio concreto
> Se una fabbrica ha un Risultato Lordo Industriale positivo, significa che il prezzo di vendita dei prodotti copre i costi di produzione e genera un surplus. Se fosse negativo, l'azienda perderebbe soldi su ogni unità prodotta, indipendentemente da quanto bene gestisca la pubblicità o le vendite.

### Derivazione del Risultato Lordo Industriale
Il calcolo avviene sottraendo dal valore della produzione i costi direttamente legati alla creazione del prodotto:
$$ \text{Risultato Lordo Industriale} = \text{Valore della Produzione} - \text{Costi del Venduto} $$

> [!important] Formule chiave
> $$ \text{Risultato Lordo Industriale} = \text{Valore della Produzione} - \sum (\text{Scorte} + \text{Manodopera} + \text{Energia} + \text{Ammortamenti} + \text{Altri Costi Diretti}) $$

**Collegamenti**: Richiede la definizione di *Costo del Venduto*. È utilizzato come base per il calcolo del *Risultato Operativo*.

---

## 3. Analisi di Caso: Macchinari Industriali Spa

> [!example] Esempio 1 (Analisi Conto Economico)
> Si analizzi il conto economico della società **Macchinari Industriali Spa**, produttrice di macchinari manifatturieri.
>
> Dati rilevati:
> - Differenza positiva tra valore e costi della produzione: $25,8$ milioni di euro.
> - Operazioni straordinarie: `NIL`.
> - Utile di esercizio: $4,8$ milioni di euro.
>
> **Analisi dei dati**:
> 1. Il Risultato Lordo Industriale è pari a $25,8$ milioni di euro, indicando una forte capacità produttiva.
> 2. L'assenza di operazioni straordinarie permette di attribuire l'utile quasi interamente alla gestione ordinaria.
> 3. L'utile finale di $4,8$ milioni di euro è il risultato della sottrazione dei costi operativi (amministrativi, distributivi e commerciali) e degli oneri finanziari/fiscali dal Risultato Lordo Industriale.

> [!example] Esercizio 1
> Data una società con un Valore della Produzione di $100$ milioni, Costi del Venduto di $70$ milioni, Costi Amministrativi e Commerciali di $20$ milioni e Oneri Finanziari di $5$ milioni. Calcola il Risultato Lordo Industriale e il Risultato Operativo.
>
> *Suggerimento: Segui la gerarchia dei costi dal processo produttivo verso l'attività commerciale.*
>
> **Soluzione**:
> 1. **Risultato Lordo Industriale** = $100 - 70 = 30$ milioni di euro.
> 2. **Risultato Operativo** = $30 - 20 = 10$ milioni di euro.
> *Nota: Gli oneri finanziari non influenzano il Risultato Operativo, ma solo l'Utile Netto.*

# Analisi del Conto Economico e Riclassificazione

## 1. Margini di Redditività Industriale e Operativa

> [!important] Margine di Redditività
> Il **Margine di Redditività** rappresenta la percentuale di guadagno generata da un'attività specifica (lorda) o dall'intera attività caratteristica (operativa) rispetto al fatturato totale. 
> 
> Formalmente, il margine è il rapporto tra il risultato (utile) e il fatturato:
> $$ \text{Margine} = \frac{\text{Risultato}}{\text{Fatturato}} \times 100 $$

Il calcolo dei margini serve a misurare l'efficienza economica di un'azienda, permettendo di capire quanta parte di ogni euro incassato rimane effettivamente come profitto dopo aver coperto i costi diretti o operativi. Senza questi indicatori, non sarebbe possibile distinguere tra una crescita del fatturato dovuta a volumi elevati e una crescita reale dovuta all'efficienza dei processi.

> [!example] Esempio concreto
> In un'azienda di produzione meccanica, se il risultato lordo industriale pesa per il 16,87% sul fatturato e il risultato operativo per il 6,62%, l'azienda sta trattenendo circa 17 centesimi su ogni euro venduto a livello di produzione primaria e circa 6 centesimi a livello di gestione complessiva.

**Analisi del caso specifico:**
Il risultato lordo industriale appare basso (65 milioni su 390 di ricavi totali). L'analisi dettagliata della voce **Costo del Venduto** evidenzia che il problema risiede nella voce **Acquisti**, che dimezza gli incassi. Una politica di approvvigionamento più aggressiva potrebbe migliorare il margine, poiché a parità di ricavi, la riduzione delle spese di acquisto aumenta direttamente il fatturato netto e il profitto.

> [!quote] Osservazione
> Il risultato della gestione finanziaria è influenzato negativamente dal pagamento di interessi passivi: ciò indica che l'azienda *Macchinari Industriali* sta finanziando la propria attività industriale attraverso l'indebitamento.

**Formule chiave**
| Grandezza | Formula |
|:---|:---|
| Margine Lordo Industriale | $\frac{\text{Risultato Lordo Industriale}}{\text{Fatturato}} \times 100$ |
| Margine Operativo | $\frac{\text{Risultato Operativo}}{\text{Fatturato}} \times 100$ |

**Collegamenti**
Richiede: [Conto Economico Standard]. Usato in: [Analisi dei Costi e Riclassificazione a Valore Aggiunto].

> [!warning] Attenzione
> Non confondere il margine di redditività con il flusso di cassa. Un'azienda può avere un ottimo margine operativo ma trovarsi in difficoltà di liquidità a causa di ritardi nei pagamenti o eccessivo indebitamento (interessi passivi).

---

## 2. Riclassificazione a Valore della Produzione e Valore Aggiunto

### 2.1 Principio di Coerenza della Riclassificazione
L'essenza del processo di riclassificazione risiede nella corretta aggregazione delle voci di entrata e uscita di natura strettamente caratteristica. Se le voci sono aggregate correttamente e i calcoli sono esatti, il reddito operativo ottenuto tramite lo schema a "Valore della Produzione" deve coincidere con quello risultante dalla riclassificazione a "Fatturato e Costo del Venduto".

### 2.2 Valore della Produzione e Valore Aggiunto
> [!important] Valore della Produzione e Valore Aggiunto
> Il **Valore della Produzione** rappresenta il valore totale dei beni e servizi prodotti dall'azienda in un determinato periodo, mentre il **Valore Aggiunto** è la differenza tra il valore della produzione e i consumi intermedi (materie prime, energia, servizi esterni).
> 
> $$ \text{Valore Aggiunto} = \text{Valore della Produzione} - \text{Consumi Intermedi} $$

L'utilità di questo schema risiede nella capacità di quantificare il valore aggiunto dall'azienda: ovvero quanto valore viene creato trasformando le materie prime e i fattori esterni attraverso il processo produttivo caratteristico.

**Punti di forza dello schema (fino al reddito operativo):**
- Suddivisione dei costi operativi tra **costi esterni** e **costi interni**.
- Determinazione di tre grandezze intermedie fondamentali:
    1. Valore della produzione dell'esercizio.
    2. Valore aggiunto.
    3. Margine Operativo Lordo (MOL).

> [!example] Esercizio 1
> Un'azienda produce mobili con un valore di produzione di 1.000.000 €. I consumi intermedi (legno, colle, energia) ammontano a 600.000 €. Calcolare il Valore Aggiunto e il Margine Operativo Lordo se i costi interni sono di 250.000 €.
> 
> *Suggerimento: Ricorda che il Valore Aggiunto è ciò che resta dopo aver sottratto i consumi intermedi dal valore della produzione.*
> 
> **Soluzione:**
> 1. Valore Aggiunto = $1.000.000 - 600.000 = 400.000 €$.
> 2. Margine Operativo Lordo (MOL) = $\text{Valore Aggiunto} - \text{Costi Interni} = 400.000 - 250.000 = 150.000 €$.

**Collegamenti**
Richiede: [Riclassificazione a Fatturato e Costo del Venduto]. Usato in: [Analisi della Struttura dei Costi].

## 1. Valore della produzione e valore aggiunto

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/6dba11cc27dbe58b1f96c1d3f488ba1884055d9fab812261febe00326aece1b7.jpg)

### 1.1 Produzione dell'esercizio

> [!important] Produzione dell'esercizio
> La **Produzione dell'esercizio** è la misura quantitativa del valore di tutti i beni e servizi prodotti dall'azienda durante un determinato periodo contabile, indipendentemente dal fatto che siano stati venduti o meno.
> 
> In termini pratici, rappresenta il "volume di attività" trasformata dall'impresa. Ad esempio, se un'azienda produce 100 macchinari ma ne vende solo 80, la produzione dell'esercizio comprende il valore dei 100 macchinari prodotti.

**Perché serve**
Serve a isolare il contributo produttivo dell'azienda dal suo successo commerciale (vendite). Senza questo concetto, non sarebbe possibile distinguere tra un'azienda che produce molto ma vende poco e un'azienda che produce poco ma vende tutto ciò che realizza.

**Esempio concreto**
Un'azienda di produzione di mobili produce 50 tavoli in un mese. Anche se ne vengono spediti solo 40 ai clienti, il valore dei 50 tavoli costituisce la "Produzione dell'esercizio".

**Derivazione**
Il calcolo parte dal fatturato (vendite) e deve essere corretto per includere ciò che è stato prodotto ma non ancora venduto:
1. Si parte dalle **Vendite** (prodotto finito commercializzato).
2. Si aggiungono le **Variazioni di scorte di prodotti finiti e semilavorati** (se le scorte aumentano, significa che è stata prodotta più merce di quanta ne sia stata venduta).
3. Si aggiungono le **Costruzioni in economia** (lavori svolti per uso interno, come la costruzione di un magazzino aziendale, che non sono destinati alla vendita ma aumentano il valore dell'azienda).
4. Si sottraggono gli acquisti di prodotti finiti destinati alla rivendita (merce commerciale), poiché non hanno subito alcuna trasformazione produttiva.

**Formule chiave**
> [!important] Formula Produzione dell'esercizio
> $$ \text{Produzione dell'esercizio} = \text{Vendite} + \Delta\text{Scorte} + \text{Costruzioni in economia} - \text{Acquisti prodotti finiti per rivendita} $$

**Collegamenti**
Richiede: [Conto Economico Semplificato]. Usato in: [Valore Aggiunto].

> [!warning] Attenzione
> Non confondere la produzione dell'esercizio con il fatturato. Il fatturato misura lo scambio commerciale, la produzione misura l'attività industriale/produttiva.

### 1.2 Valore aggiunto

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/6dba11cc27dbe58b1f96c1d3f488ba1884055d9fab812261febe00326aece1b7.jpg)

> [!important] Valore Aggiunto
> Il **Valore Aggiunto** è il valore economico creato dall'azienda durante il processo produttivo, calcolato come differenza tra il valore della produzione e i costi esterni sostenuti.
> 
> In sintesi, rappresenta il reddito prodotto dall'azienda al netto dei fattori esterni che hanno concorso alla sua realizzazione (materie prime, energia, consulenze).

**Perché serve**
Serve a misurare l'efficienza del processo produttivo interno. Indica quanta ricchezza "nuova" l'azienda è in grado di generare partendo da input esterni. Se il valore aggiunto è basso rispetto alla produzione, significa che l'azienda sta solo "assemblando" componenti senza aggiungere un significativo valore trasformativo.

**Esempio concreto**
Un'azienda acquista acciaio per 100€ e lo trasforma in una struttura metallica venduta a 500€. Il valore aggiunto è di 400€ (il valore creato dalla lavorazione, dal design e dall'assemblaggio).

**Derivazione**
Il valore aggiunto si ricava sottraendo i costi esterni dal valore della produzione:
1. Si prende il **Valore della Produzione dell'esercizio**.
2. Si sottraggono gli **Acquisti di materie prime**.
3. Si sottraggono le **Spese per beni e servizi** (es. energia elettrica, consulenze esterne).

**Formule chiave**
> [!important] Formula Valore Aggiunto
> $$ \text{Valore Aggiunto} = \text{Produzione dell'esercizio} - \text{Costi Esterni} $$

**Collegamenti**
Richiede: [Produzione dell'esercizio]. Usato in: [Margine Operativo Lordo].

### 1.3 Margine Operativo Lordo (MOL) e Reddito Operativo

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/6dba11cc27dbe58b1f96c1d3f488ba1884055d9fab812261febe00326aece1b7.jpg)

> [!important] Margine Operativo Lordo (MOL)
> Il **Margine Operativo Lordo** è la misura della redditività della gestione caratteristica ottenuta sottraendo i costi del personale dal valore aggiunto.
> 
> È una misura fondamentale perché indica quanto l'azienda guadagna dalla sua attività principale prima di considerare gli ammortamenti e gli accantonamenti.

**Perché serve**
Serve a valutare la capacità dell'azienda di generare profitto operativo attraverso il suo core business, indipendentemente dalle scelte di investimento (ammortamenti) o dalle riserve di sicurezza (accantonamenti).

**Esempio concreto**
Un'azienda ha un valore aggiunto di 1.000.000€ e paga 400.000€ di stipendi e contributi al personale. Il MOL è di 600.000€. Questo indica che l'attività produttiva genera 600.000€ di margine prima di considerare come sono stati finanziati i macchinari o le riserve.

**Derivazione**
1. Si parte dal **Valore Aggiunto**.
2. Si sottraggono i **Costi del personale** (stipendi, contributi, premi).
3. Il risultato è il **MOL**.

**Formule chiave**
> [!important] Formula MOL
> $$ \text{MOL} = \text{Valore Aggiunto} - \text{Costi del Personale} $$

**Collegamenti**
Richiede: [Valore Aggiunto]. Usato in: [Reddito Operativo].

> [!quote] Osservazione
> Il MOL ha una valenza più finanziaria rispetto al reddito operativo perché indica la performance ottenuta prima che venga influenzata dagli ammortamenti, i quali alterano la redditività senza comportare reali uscite monetarie (sono costi non monetari).

### 1.4 Reddito Operativo

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/6dba11cc27dbe58b1f96c1d3f488ba1884055d9fab812261febe00326aece1b7.jpg)

> [!important] Reddito Operativo
> Il **Reddito Operativo** è il risultato della gestione caratteristica dell'azienda dopo aver sottratto dal Margine Operativo Lordo gli ammortamenti e gli accantonamenti.
> 
> Rappresenta la redditività "contabile" dell'attività operativa, includendo l'usura dei beni strumentali e le riserve di capitale.

**Perché serve**
Serve a fornire una visione completa della redditività che tiene conto del deterioramento dei mezzi di produzione (ammortamenti) e delle necessità di riserva dell'azienda, elementi essenziali per la sostenibilità a lungo termine.

**Esempio concreto**
Un'azienda ha un MOL di 600.000€. Durante l'anno, i macchinari si sono "consumati" per un valore di 100.000€ (ammortamenti) e l'azienda ha deciso di mettere da parte 50.000€ come riserva (accantonamenti). Il Reddito Operativo è di 450.000€.

**Derivazione**
1. Si parte dal **Margine Operativo Lordo**.
2. Si sottraggono gli **Ammortamenti** (deterioramento dei beni strumentali).
3. Si sottraggono gli **Accantonamenti** (riserve per rischi o scopi specifici).
4. Il risultato è il **Reddito Operativo**.

**Formule chiave**
> [!important] Formula Reddito Operativo
> $$ \text{Reddito Operativo} = \text{MOL} - (\text{Ammortamenti} + \text{Accantonamenti}) $$

**Collegamenti**
Richiede: [Margine Operativo Lordo].

> [!warning] Attenzione
> Ricorda la differenza fondamentale: il MOL include ammortamenti e accantonamenti, mentre il Reddito Operativo li esclude. Il MOL è una misura di performance "monetaria" (cash-flow oriented), il Reddito Operativo è una misura di performance "contabile".

### 1.5 Esempio Pratico: Macchinari Industriali Spa

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/4787498b3826fe160536dd8f5d2992d5d7db6428be243302f35bb15e8cf7696e.jpg)

> [!example] Esercizio 1 (Analisi Caso Studio)
> Analizzare il conto economico della società *Macchinari Industriali Spa* per identificare i componenti del valore aggiunto e del margine operativo.
> 
> *Nota: Il testo fornisce l'immagine del conto economico ma non i dati numerici nel chunk corrente.*
> 
> **Soluzione:**
> Per risolvere l'esercizio, è necessario identificare nel conto economico semplificato della società:
> 1. Le vendite e le variazioni di scorte per calcolare la *Produzione dell'esercizio*.
> 2. Gli acquisti di materie prime e i costi per servizi esterni per determinare il *Valore Aggiunto*.
> 3. I costi del personale per ricavare il *MOL*.
> 4. Gli ammortamenti e gli accantonamenti per arrivare al *Reddito Operativo*.

## **Valore aggiunto**

> [!important] Valore Aggiunto
> Il **Valore Aggiunto** rappresenta la differenza tra il valore della produzione effettuata dall'impresa e i costi dei beni e servizi acquistati da terzi per completare tale produzione. In termini contabili, indica la ricchezza netta generata dal processo produttivo interno prima di considerare i costi di distribuzione, amministrazione e finanziamento.

Perché serve — Serve a misurare quanto valore un'azienda "aggiunge" ai fattori produttivi esterni (materie prime, energia, servizi). Senza questa misura, non sarebbe possibile distinguere tra la capacità produttiva propria dell'impresa e il semplice "passaggio" di beni acquistati da fornitori.

Esempio concreto — In una fabbrica di macchinari industriali, se l'azienda acquista acciaio per 100 milioni e produce macchinari che vengono venduti per 200 milioni, il valore aggiunto è di 100 milioni (il valore creato dal lavoro, dalle macchine e dall'organizzazione interna).

Derivazione — Partendo dai Ricavi Totali ($R$), si sottrae il costo delle materie prime e dei servizi acquistati da terzi ($C_{esterni}$):
$$VA = R - C_{esterni}$$
Nel caso specifico analizzato, la Macchinari Industriali presenta un valore aggiunto di 188 milioni di euro, pari a circa il 48% dei ricavi. Ciò indica che la metà del fatturato viene assorbita dai costi esterni, lasciando l'altra metà per coprire i costi interni e le altre gestioni.

> [!important] Formule chiave
> $$VA = \text{Ricavi} - \text{Acquisti di materie prime e servizi}$$

Collegamenti — Richiede: [Ricavi]. Usato in: [Costo del venduto], [Margine Operativo Lordo].

> [!warning] Attenzione
> Spesso si confonde il valore aggiunto con l'utile. Il valore aggiunto non tiene conto dei costi interni (personale, affitti, ammortamenti) né degli oneri finanziari; è una misura di produzione, non di profitto finale. Inoltre, nella realtà, i ricavi e la produzione dell'esercizio potrebbero non equivalersi perfettamente a causa di scorte rimanenti o prodotti in corso di lavorazione.

## **Costo del venduto**

> [!important] Costo del Venduto
> Il **Costo del Venduto** (COGS - *Cost of Goods Sold*) rappresenta la somma dei costi diretti sostenuti per la produzione dei beni che sono stati effettivamente venduti durante il periodo di riferimento.

Perché serve — Serve a determinare il margine lordo e a capire quanto costa "produrre" ogni unità venduta. Senza questa distinzione, non si potrebbe sapere se un'azienda è inefficiente nella produzione o se ha semplicemente costi fissi amministrativi elevati.

Esempio concreto — Se un'azienda produce smartphone, il costo del venduto include i componenti elettronici, la manodopera di assemblaggio e l'energia consumata durante la fabbricazione dei modelli effettivamente spediti ai clienti.

Derivazione — Si ottiene sottraendo il Costo del Venduto dai Ricavi Totali per ottenere il Margine Lordo:
$$\text{Margine Lordo} = \text{Ricavi} - \text{Costo del Venduto}$$
Nel caso della Macchinari Industriali, la voce "Acquisti" dell'esercizio comprende i costi sostenuti per le materie prime, mentre gli acquisti di servizi sono stati riclassificati sotto "Altri oneri".

> [!important] Formule chiave
> $$\text{Costo del Venduto} = \sum \text{Costi diretti produzione beni venduti}$$

Collegamenti — Richiede: [Valore Aggiunto]. Usato in: [Margine Operativo Lordo].

## **Margine Operativo Lordo (EBITDA)**

> [!important] Margine Operativo Lordo
> Il **Margine Operativo Lordo** rappresenta il risultato della gestione caratteristica dell'impresa, calcolato sottraendo i costi operativi dai ricavi, ma escludendo gli ammortamenti e gli accantonamenti.

Perché serve — È fondamentale per valutare la capacità di generare cassa (cash flow) dall'attività principale. Poiché non include gli ammortamenti (che sono costi "non monetari"), permette di confrontare la redditività operativa tra aziende con diverse strutture di capitale o età degli impianti.

Esempio concreto — Due aziende che producono lo stesso macchinario potrebbero avere un utile netto diverso perché una ha macchinari vecchi (alti ammortamenti) e l'altra nuovi, ma il loro Margine Operativo Lordo potrebbe essere identico se la loro efficienza produttiva è la stessa.

Derivazione — Si ottiene partendo dal Risultato Lordo Industriale sottraendo i costi commerciali, distributivi, amministrativi e generali (non inclusi gli ammortamenti):
$$\text{Margine Operativo Lordo} = \text{Ricavi} - \text{Costi Operativi (esclusi ammortamenti)}$$

> [!important] Formule chiave
> $$\text{Margine Operativo Lordo} = \text{Risultato Lordo Industriale} - \text{Costi Amministrativi/Commerciali}$$

Collegamenti — Richiede: [Valore Aggiunto], [Costo del Venduto]. Usato in: [Analisi Comparativa della Redditività].

> [!warning] Attenzione
> Non confondere il Margine Operativo Lordo con il Risultato Operativo. Il Risultato Operativo include gli ammortamenti, che riducono l'utile ma non rappresentano un'uscita monetaria immediata. Due aziende possono avere margini operativi lordi simili ma risultati operativi molto diversi a causa della velocità di obsolescenza dei loro asset.

## **Analisi Comparativa della Redditività**

> [!quote] Osservazione
> Il confronto tra OmniTech Spa e Future Spa evidenzia come ricavi e utili netti simili possano nascondere stati di salute finanziaria profondamente diversi.

L'analisi mostra che, nonostante entrambe le società abbiano un utile netto vicino ai 50 milioni di euro su un fatturato di circa 430-500 milioni:
1. **OmniTech Spa**: Presenta un reddito operativo di 76 milioni di euro con un margine operativo del **17,43%**.
2. **Future Spa**: Presenta un reddito operativo di soli 21 milioni di euro con un margine operativo del **4,19%**.

Questa differenza indica che per Future Spa i costi operativi hanno un impatto molto più elevato sulla redditività della gestione caratteristica rispetto a OmniTech.

> [!example] Esercizio 1
> Un'azienda X ha ricavi di 100 milioni di euro, costi delle materie prime di 40 milioni e costi operativi (esclusi ammortamenti) di 50 milioni. Calcola il Valore Aggiunto e il Margine Operativo Lordo.
>
> *Soluzione:*
> 1. **Valore Aggiunto**: $VA = \text{Ricavi} - \text{Materie Prime} = 100 - 40 = 60$ milioni di euro.
> 2. **Margine Operativo Lordo**: $\text{MOL} = \text{Ricavi} - \text{Costi Operativi} = 100 - 50 = 50$ milioni di euro.

# Analisi Comparativa della Performance Industriale e Finanziaria

## Analisi dei Margini e della Struttura dei Costi

L'analisi comparativa tra le società **OmniTech** e **Futura** evidenzia una divergenza strutturale significativa nella gestione dell'attività industriale. Il dato principale risiede nel **Margine Industriale Lordo**, che per OmniTech si attesta al 51,83%, permettendo alla società di trattenere circa il 15% di ricavi in più rispetto alla concorrente dopo il processo produttivo.

### Analisi del Costo del Venduto e dei Costi Non Industriali

Il problema centrale della differenza di redditività risiede nel **Costo del Venduto**. Mentre la Futura registra un costo del venduto di 323 milioni di euro, OmniTech si ferma a 210 milioni. Al contrario, i costi non strettamente industriali (commerciali, distributivi e amministrativi) risultano quasi identici per entrambe le società:
- **Futura**: 157 milioni di euro (138 commerciali/distributivi + 19 amministrativi).
- **OmniTech**: 150 milioni di euro (94 commerciali/distributivi + 56 amministrativi).

> [!example] Esempio 1 (*Confronto Struttura Costi*)
> Consideriamo due aziende che vendono lo stesso prodotto. Se l'Azienda A ha costi di produzione molto più alti dell'Azienda B, ma entrambe spendono quasi uguale in marketing e amministrazione, la differenza di utile finale è imputabile esclusivamente all'efficienza del processo produttivo (Costo del Venduto). Nel caso in esame, OmniTech dimostra una superiorità operativa netta.

### Performance della Gestione Accessoria e Finanziaria

Oltre alla componente industriale, il confronto rivela differenze critiche nelle gestioni accessorie:
1. **Gestione Accessoria**: OmniTech ha prodotto un risultato di 18 milioni di euro, ovvero tre volte superiore ai 6 milioni di euro della Futura.
2. **Gestione Finanziaria**: La Futura ha registrato perdite per 65 milioni di euro, mentre OmniTech è riuscita a contenere le uscite a 34 milioni di euro.

![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/347c57a1f906396797a2b629746740d922fcbbb120fe75c35942eb11747f3510.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/d5b03305f44d01de9fafe9c765ba86fb358caa55f48920620545be74cf0ebbcc.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/347c57a1f906396797a2b629746740d922fcbbb120fe75c35942eb11747f3510.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/d5b03305f44d01de9fafe9c765ba86fb358caa55f48920620545be74cf0ebbcc.jpg)

### Impatto delle Operazioni Straordinarie

Il **Risultato di Competenza** mostra OmniTech in una posizione di chiusura positiva, mentre la Futura appare in territorio negativo. Tuttavia, l'analisi del conto economico rivela un ruolo determinante della **Gestione Straordinaria**:
- **Futura**: Ha ricevuto un apporto di 115 milioni di euro (circa il 23% dei ricavi), che ha permesso non solo di coprire le perdite operative ma anche di generare un utile finale di 46,8 milioni di euro.
- **OmniTech**: Il contributo straordinario è stato più contenuto e "normale", pari a 26 milioni di euro (5,96% del fatturato).

> [!warning] Attenzione
> Un utile finale positivo derivante prevalentemente da gestioni straordinarie (come nel caso della Futura) non indica una salute industriale robusta. Tale risultato è spesso non ripetibile e maschera un'inefficienza della gestione caratteristica-operativa, che non è in grado di sostenere l'azienda autonomamente.

![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/347c57a1f906396797a2b629746740d922fcbbb120fe75c35942eb11747f3510.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/d5b03305f44d01de9fafe9c765ba86fb358caa55f48920620545be74cf0ebbcc.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/347c57a1f906396797a2b629746740d922fcbbb120fe75c35942eb11747f3510.jpg)
![](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/67770900-bf35-4f4b-97d8-d1696454b9c0/d5b03305f44d01de9fafe9c765ba86fb358caa55f48920620545be74cf0ebbcc.jpg)

### Conclusioni e Strategie di Intervento

La **OmniTech** risulta essere l'azienda più sana, poiché è in grado di sostenersi attraverso la propria gestione caratteristica-operativa. La **Futura**, invece, mostra una dipendenza critica dai risultati straordinari per evitare il dissesto.

Per invertire la tendenza, la Futura deve agire sulle componenti della gestione caratteristica attraverso due leve principali:
1. **Taglio dei Costi**: Revisione dei contratti di fornitura, politiche di approvvigionamento, riduzione del costo del personale (licenziamenti o delocalizzazione) e aumento dell'efficienza produttiva.
2. **Aumento della Redditività**: Mantenimento dei costi fissi e incremento simultaneo della produttività degli impianti e del personale.

> [!example] Esercizio 1
> Calcolare il risparmio percentuale sul costo del venduto che OmniTech ottiene rispetto alla Futura, basandosi sui dati forniti nel testo.
>
> *Soluzione:*
> Il costo del venduto di Futura è 323 milioni, quello di OmniTech è 210 milioni.
> Differenza assoluta = $323 - 210 = 113$ milioni.
> Risparmio percentuale = $(113 / 323) \times 100 \approx 35\%$.
> Questo dato conferma che la superiorità di OmniTech è dovuta a un'efficienza produttiva superiore del 35% circa rispetto alla concorrente.