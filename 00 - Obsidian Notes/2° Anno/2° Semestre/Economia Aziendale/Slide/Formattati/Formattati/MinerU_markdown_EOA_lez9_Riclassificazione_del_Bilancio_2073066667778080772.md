# Lezione 9 - Riclassificare il bilancio

## Introduzione alla riclassificazione del bilancio

Il concetto di **riclassificazione del bilancio** si riferisce alla procedura di riassegnazione delle voci contabili o dei flussi finanziari all'interno di una struttura di bilancio preesistente. In ambito informatico e gestionale, questo processo è fondamentale per garantire che le risorse siano allocate correttamente in base a criteri dinamici (come la priorità del progetto, il centro di costo o la tipologia di spesa) piuttosto che rimanere vincolate a categorie statiche iniziali.

> [!important] Riclassificazione del Bilancio
> **Definizione**: È l'operazione di modifica della destinazione d'uso di una risorsa finanziaria già allocata, spostandola da una voce di spesa/entrata $A$ a una voce $B$, mantenendo invariato il totale complessivo del bilancio ma alterandone la distribuzione interna.
> 
> **Formalizzazione**: Dato un bilancio iniziale $B = \sum_{i=1}^{n} x_i$, dove $x_i$ rappresenta l'allocazione alla categoria $i$, una riclassificazione è una trasformazione $B' = \sum_{i=1}^{n} x'_i$ tale che $\sum x_i = \sum x'_i$, con la condizione che per ogni operazione di spostamento tra categorie $j$ e $k$:
> $$x'_j = x_j - \Delta$$
> $$x'_k = x_k + \Delta$$
> dove $\Delta > 0$ è l'ammontare della riclassificazione.

**Perché serve**
Senza la possibilità di riclassificare, un bilancio diventerebbe rigido e incapace di adattarsi a cambiamenti imprevisti (es. un aumento dei costi di hardware o una variazione nelle priorità di sviluppo software). La riclassificazione permette di ottimizzare l'uso delle risorse esistenti senza richiedere nuove approvazioni per l'aumento del budget totale, garantendo flessibilità operativa.

> [!example] Esempio concreto
> In un progetto di sviluppo software, il bilancio iniziale prevede 10.000€ per la "Documentazione" e 50.000€ per lo "Sviluppo Backend". Durante la fase di test, emerge la necessità di integrare una libreria di sicurezza critica che costa 2.000€. Poiché il budget totale è bloccato, si procede a una **riclassificazione**: si sottraggono 2.000€ dalla voce "Documentazione" e si aggiungono alla voce "Sviluppo Backend". Il bilancio totale rimane invariato (60.000€), ma la distribuzione interna è aggiornata per riflettere le necessità tecniche reali.

**Derivazione**
La logica della riclassificazione segue il principio di conservazione del valore monetario nel sistema chiuso del bilancio:
1. Si identifica la voce sorgente $x_{src}$ e la voce destinazione $x_{dest}$.
2. Si definisce l'entità dello spostamento $\Delta$.
3. Si verifica che $\Delta \leq x_{src}$ (non si può riclassificare più di quanto sia presente nella voce sorgente).
4. Si aggiornano i valori:
   - $x'_{src} = x_{src} - \Delta$
   - $x'_{dest} = x_{dest} + \Delta$
5. Si verifica la coerenza del bilancio totale: $\sum x'_i = (\sum x_i) - \Delta + \Delta = \sum x_i$.

> [!important] Formule chiave
> | Parametro | Formula |
> |:---|:---|
> **Variazione Sorgente** | $x'_{src} = x_{src} - \Delta$ |
> **Variazione Destinazione** | $x'_{dest} = x_{dest} + \Delta$ |
> **Invarianza Totale** | $\sum x_i = \sum x'_i$ |

**Collegamenti**
Richiede: [Concetti base di Bilancio e Allocazione]. Usato in: [Gestione Progetti, Contabilità Gestionale, Ottimizzazione delle Risorse].

> [!warning] Attenzione
> Una riclassificazione non è un aumento di budget. Un errore comune è confondere il "trasferimento di fondi" (riclassificazione) con l' "approvazione di nuovi fondi" (incremento). La riclassificazione deve sempre rispettare il vincolo di somma costante; se la somma finale differisce da quella iniziale, l'operazione non è una riclassificazione ma una modifica del budget totale.

> [!example] Esercizio 1
> Un dipartimento IT ha un bilancio per "Manutenzione Server" di 15.000€ e uno per "Formazione Personale" di 5.000€. A causa di un guasto hardware improvviso, è necessario spostare 3.000€ dalla formazione alla manutenzione.
> 1. Calcola il nuovo valore della voce "Manutenzione Server".
> 2. Calcola il nuovo valore della voce "Formazione Personale".
> 3. Verifica che il bilancio totale sia rimasto invariato.
>
> *Suggerimento: Identifica prima $\Delta$ e applica le formule di variazione.*
>
> **Soluzione**:
> 1. $x'_{manut} = 15.000€ + 3.000€ = 18.000€$ (Nota: qui la manutenzione è destinazione, quindi $\Delta$ viene sommato).
> 2. $x'_{form} = 5.000€ - 3.000€ = 2.000€$.
> 3. Totale iniziale: $15.000 + 5.000 = 20.000€$. Totale finale: $18.000 + 2.000 = 20.000€$. Il bilancio è invariato.

# Corso EOA

**Prof. Giuseppe Piccirillo**

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-03/6c129d73-2956-4f9e-bdb2-e951cc30db9e/965dd9f0ba4e47210558a6e47054fb082718dec7e6101f21e753ebe85ea5bb51.png)

## 1. Riclassificazione del Bilancio

La **riclassificazione di bilancio** è una procedura tecnica fondamentale per l'analisi finanziaria, poiché il bilancio d'esercizio standard, pur essendo completo, può risultare complesso e poco immediato da interpretare per valutare rapidamente la salute creditizia di un'impresa.

> [!important] Riclassificazione di Bilancio
> La riclassificazione di bilancio è una procedura che consiste nel rielaborare e riorganizzare le diverse voci incluse nel bilancio aziendale, in modo da renderne più semplice e veloce l’analisi e la valutazione. Essa consiste nell'associare e categorizzare ogni voce contabile in una classe di appartenenza specifica tramite schemi standardizzati e appositi **indici di bilancio**.
>
> **Esempio concreto**: Un'azienda potrebbe avere diverse tipologie di debiti (fornitori, mutui, tasse). La riclassificazione permette di raggrupparli non solo per "natura", ma per "scadenza", permettendo a un analista di capire immediatamente quanta liquidità servirà nei prossimi 12 mesi.

**Perché serve**: Senza la riclassificazione, l'analisi del bilancio richiederebbe tempi eccessivi e procedure manuali ripetitive. La procedura permette di ottenere una mappatura riassuntiva dello stato di salute finanziario, economico e contabile, facilitando il confronto tra imprese diverse.

La riclassificazione prevede due operazioni principali:
1. Riclassificazione dello stato patrimoniale.
2. Riclassificazione del conto economico.

Questi schemi mettono in luce aspetti diversi come il complesso dei debiti aziendali, il reddito operativo e la provenienza/forma di incassi e spese.

> [!example] Esercizio 1
> Un'impresa presenta un debito verso una banca per un mutuo di 1.000.000 € con rate annuali di 100.000 €. Quale parte del debito va inserita nelle passività correnti e quale nelle consolidate?
>
> *Suggerimento: Considera il criterio della scadenza entro i 12 mesi.*
>
> **Soluzione**: La quota di 100.000 € che scade entro l'anno corrente deve essere inserita nelle **passività correnti**. Il restante debito (900.000 €) deve essere inserito nelle **passività consolidate**, poiché la scadenza è superiore ai 12 mesi.

## 2. Riclassificazione dello Stato Patrimoniale

La riclassificazione dello stato patrimoniale si focalizza sull'organizzazione dei dati relativi alle attività (impieghi) e passività (fonti di capitale).

> [!important] Criterio Finanziario
> La riclassificazione dello stato patrimoniale segue principalmente un **criterio finanziario**, che organizza le voci in base alla velocità di trasformazione in moneta.
>
> - Per le **attività**: si utilizza il **grado di liquidità** (capacità di essere trasformate in moneta nel breve o lungo termine).
> - Per le **passività**: si utilizza il **grado di esigibilità** (tempo entro cui devono avvenire i pagamenti).

**Perché serve**: Serve a fornire una fotografia chiara della consistenza del patrimonio, distinguendo tra ciò che è disponibile immediatamente per far fronte agli impegni e ciò che rappresenta la struttura solida e di lungo periodo dell'azienda.

**Esempio concreto**: Distinguere tra le rimanenze di magazzino (che possono essere vendute rapidamente) e un macchinario industriale (che serve alla produzione ma non è liquido).

### 2.1 Classificazione delle Attività
In base al criterio finanziario, le attività si distinguono in:
- **Attività o impieghi di capitale correnti o circolanti**: liquidabili in breve termine (entro 12 mesi). Esempi: BOT semestrali, titoli negoziabili a vista, rimanenze di magazzino.
- **Attività consolidate**: trasformabili in moneta gradualmente nel lungo termine. Esempi: immobilizzazioni immateriali, materiali e finanziarie, investimenti di durata pluriennale.

### 2.2 Classificazione delle Passività
Le passività vengono suddivise in base alla scadenza dei pagamenti:
- **Passività correnti**: debiti da saldare a breve termine (entro 12 mesi).
- **Passività consolidate**: finanziamenti pluriennali e forme di capitale di credito con scadenza superiore a 12 mesi.

> [!warning] Attenzione
> Nel caso di rimborsi con rate periodiche, è fondamentale non inserire l'intero debito nelle passività correnti solo perché "scade". Bisogna separare rigorosamente la quota che scade entro i 12 mesi (corrente) da quella successiva (consolidata). Lo stesso meccanismo va applicato ai fondi per le spese in preventivo.

**Collegamenti**: Richiede: [Concetti base di Stato Patrimoniale]. Usato in: [Analisi del Conto Economico Riclassificato].

# Capitolo X - Analisi del Bilancio d'Esercizio

## Riclassificazione del Conto Economico

Il **Capitale Netto** (o proprio) rappresenta il capitale di proprietà dell’imprenditore utilizzabile come fonte di finanziamento aziendale all'interno dello stato patrimoniale riclassificato.

### Riclassificazione del conto economico
La procedura di riclassificazione del conto economico ha come obiettivo quello di riorganizzare e confrontare i costi e i ricavi aziendali, separando il reddito derivante dalla gestione ordinaria (o corrente) da quello straordinario. Nel conto economico riclassificato vengono elencati dettagliatamente i costi generali di sede, il costo dei fattori produttivi, i costi di produzione, vendita, ricerca e sviluppo, i costi per la pubblicità, ecc.

> [!important] Punto di Pareggio (*Break-even Point*)
> **Definizione**: Il livello di produzione e vendita che un’azienda deve superare per iniziare a generare profitti (ovvero il punto in cui i ricavi totali sono uguali ai costi totali).
>
> **Perché serve**: Permette di identificare la soglia minima di attività necessaria per coprire tutti i costi sostenuti, evitando perdite operative.
>
> **Esempio concreto**: Un'azienda che produce smartphone deve vendere un numero minimo di unità per coprire sia i costi variabili (componenti) sia i costi fissi (affitto della fabbrica, stipendi). Il punto in cui la vendita dell'unità $n$ copre esattamente il costo totale è il punto di pareggio.
>
> **Formule chiave**:
> $$ \text{Punto di Pareggio} = \frac{\text{Costi Fissi}}{\text{Prezzo di Vendita} - \text{Costo Variabile Unitario}} $$
>
> **Collegamenti**: Richiede: [Conto Economico Riclassificato]. Usato in: [Analisi della redditività].

!https://cdn-mineru.openxlab.org.cn/result/2026-07-03/6c129d73-2956-4f9e-bdb2-e951cc30db9e/e14262d45a368bd52e4b1783c6ac3f7b1ea46f0bd19d3095fb4fc3d9a993421d.jpg(https://example.com/image)
Figura 1: Rappresentazione del punto di pareggio nel conto economico riclassificato.

Grazie al conto economico riclassificato, un’impresa può determinare se e come un eventuale utile provenga da una **gestione ordinaria** (che rappresenta un congruo profitto) oppure da una **gestione straordinaria**. Quest'ultima presenta il limite che l'utile derivante da fenomeni eccezionali difficilmente potrà ripetersi nell'anno successivo.

### Tipologie di gestione ordinaria
La gestione ordinaria comprende le normali operazioni aziendali e si suddivide in:

- **Gestione caratteristica, tipica o operativa**: evidenzia la differenza tra costi e ricavi relativi all’attività tipica dell’azienda;
- **Gestione patrimoniale, accessoria o atipica**: riassume i proventi e gli oneri derivanti da attività secondarie rispetto a quelle tipiche (es. locazione di beni);
- **Gestione finanziaria**: mette in luce la differenza tra ricavi e costi finanziari necessari per lo svolgimento dell’attività e l’impiego delle risorse eccedenti;
- **Gestione fiscale**: schematizza le uscite dovute per il pagamento delle imposte.

### Gestione straordinaria
> [!important] Gestione Straordinaria
> **Definizione**: Differenza tra ricavi e costi derivanti da fenomeni di carattere episodico ed eccezionale.
>
> **Perché serve**: Serve a isolare eventi non ricorrenti (come furti, incendi o vendite di impianti) per non distorcere l'analisi della capacità produttiva costante dell'azienda.
>
> **Esempio concreto**: La vendita di un vecchio macchinario ammortizzato o il risarcimento ricevuto per un incendio accidentale sono eventi straordinari che non riflettono la performance operativa quotidiana.
>
> **Attenzione**: Un utile derivante da gestione straordinaria non è indice di efficienza operativa e non deve essere considerato come base per la pianificazione dei profitti futuri.

### Modelli di riclassificazione
Per riorganizzare il conto economico non esiste uno schema unico; generalmente si utilizzano tre modelli principali:

1. **A valore aggiunto**: calcola la differenza tra il valore della produzione di un esercizio e i costi operativi (materie prime, servizi, impianti) interni ed esterni sostenuti per ottenere quella produzione.
2. **A margine di contribuzione**: suddivide i costi operativi in costi variabili e fissi, permettendo di valutare l’incidenza dei costi variabili sul totale dei costi aziendali.
3. **A costo del venduto**: suddivide i costi operativi in costi diretti e indiretti per offrire una panoramica della situazione economica aziendale.

### Il modello a valore aggiunto
> [!important] Valore Aggiunto
> **Definizione**: La differenza tra il valore della produzione ottenuta e i costi delle materie prime e delle risorse acquistate da terzi.
>
> **Perché serve**: Permette di valutare quanto valore un’impresa è riuscita ad "aggiungere" ai fattori produttivi esterni attraverso il proprio processo produttivo. È fondamentale per la redazione del Bilancio Sociale.
>
> **Esempio concreto**: Se un'azienda acquista legno per 100€ e produce mobili che vengono venduti per 500€, il valore aggiunto è di 400€. Questo indica l'efficienza della trasformazione e del lavoro umano/tecnologico applicato.
>
> **Formule chiave**:
> $$ \text{Valore Aggiunto} = \text{Valore della Produzione} - \text{Consumi Intermedi} $$
>
> **Collegamenti**: Richiede: [Modelli di riclassificazione]. Usato in: [Bilancio Sociale, Analisi del Margine Operativo Lordo].
>
> **Note aggiuntive**: Il conto economico riclassificato a valore aggiunto permette di evidenziare anche il reddito operativo, il margine operativo lordo e il valore aggiunto caratteristico.

> [!example] Esercizio 1
> Un'azienda produce componenti elettronici. In un anno, il valore della produzione totale è di 1.000.000€. I costi delle materie prime acquistate da fornitori esterni sono pari a 400.000€. Calcolare il Valore Aggiunto e commentare brevemente il risultato.
>
> *Suggerimento: Utilizza la formula del valore aggiunto definita nel testo.*
>
> **Soluzione**:
> $$ \text{Valore Aggiunto} = 1.000.000€ - 400.000€ = 600.000€ $$
> Il valore aggiunto di 600.000€ rappresenta la ricchezza generata dall'azienda attraverso il proprio processo produttivo (lavoro, tecnologia, gestione) trasformando le materie prime in prodotti finiti.

# Analisi della Performance Economica: Il Conto Economico a Valore Aggiunto

## 1. Riclassificazione del conto economico
La **riclassificazione del conto economico** è un processo di riorganizzazione dei dati contabili che permette di superare la semplice visione fiscale o storica per focalizzarsi sulla gestione e sulla creazione di valore.

> [!important] Definizione: Riclassificazione del Conto Economico
> La riclassificazione consiste nel raggruppare i costi e i ricavi in base alla loro finalità (funzionale, gestionale, finanziaria) anziché per natura contabile pura. Questo permette di evidenziare parametri critici come il valore aggiunto o il reddito operativo.

**Perché serve**
Serve a trasformare un documento puramente legale/fiscale in uno strumento di analisi manageriale. Senza questa riclassificazione, sarebbe difficile distinguere quanto valore l'azienda crea effettivamente attraverso i propri processi produttivi rispetto a quanto semplicemente "spende" per mantenere la struttura o servire il debito.

**Esempio concreto**
Un'azienda manifatturiera che produce mobili può usare la riclassificazione per capire se il calo del profitto è dovuto a un aumento dei costi delle materie prime (area operativa) o a un eccessivo costo degli interessi sul debito contratto per l'acquisto dei macchinari (area finanziaria).

**Formule chiave**
| Obiettivo | Risultato Intermedio |
|:---|:---|
| Analisi Gestionale | Valore Aggiunto, MOL, Reddito Operativo |
| Analisi Finanziaria | Reddito Ante Imposte, Reddito d'Esercizio |

**Collegamenti**
Richiede: Conto Economico standard. Usato in: Analisi della performance economica (EVA).

> [!warning] Attenzione
> La riclassificazione non cambia i dati di partenza (i costi totali rimangono gli stessi), ma ne cambia l'ordine e la raggruppazione per rendere leggibili le dinamiche aziendali.

> [!example] Esercizio 1
> Un'azienda ha un fatturato di 100.000€. I costi sono: materie prime 30.000€, stipendi 20.000€, ammortamenti 5.000€ e interessi passivi 2.000€.
> Calcola il Valore Aggiunto e il Margine Operativo Lordo (MOL).
>
> *Soluzione:*
> 1. **Valore Aggiunto** = Fatturato - Costi Materie Prime = $100.000€ - 30.000€ = 70.000€$.
> 2. **Margine Operativo Lordo (MOL)** = Valore Aggiunto - Costi del Personale = $70.000€ - 20.000€ = 50.000€$.

## 2. Conto Economico a Valore Aggiunto
Il **conto economico a valore aggiunto** è lo schema specifico che isola la capacità dell'impresa di produrre ricchezza trasformando le risorse acquisite da terzi in prodotti finiti o servizi.

### 2.1 Area Operativa e Area Finanziaria
La struttura del conto economico a valore aggiunto divide i risultati in due macro-aree:
1. **Area Operativa**: Comprende il Valore Aggiunto, il Margine Operativo Lordo (MOL) e il Reddito Operativo (EBIT). Rappresenta la "salute" della produzione.
2. **Area Finanziaria**: Comprende il reddito ante imposte e il reddito d'esercizio. Rappresenta come l'azienda gestisce le risorse finanziarie, i debiti e gli obblighi fiscali.

### 2.2 Valore Aggiunto
> [!important] Definizione: Valore Aggiunto
> Il valore aggiunto è la differenza tra il valore della produzione e i costi diretti monetari sostenuti per la produzione dei beni (es. materie prime).
>
> $$ \text{Valore Aggiunto} = \text{Valore della Produzione} - \text{Costi Monetari Diretti} $$

**Perché serve**
Serve a misurare quanto "plusvalore" l'azienda apporta ai beni acquistati dall'esterno. Indica l'efficienza dei processi produttivi interni prima di considerare i costi del lavoro o degli investimenti.

**Esempio concreto**
Un panificio acquista farina e lievito (costi monetari diretti). Il valore aggiunto è la differenza tra il prezzo di vendita del pane e il costo della farina acquistata. Non include ancora il costo dei fornai, ma solo il valore creato dalla trasformazione della materia prima.

**Derivazione**
Il calcolo avviene sottraendo al valore totale della produzione i costi monetari diretti (materie prime, energia per la produzione, ecc.). In questa fase non si sottraggono ancora i costi del personale.

**Formule chiave**
> [!important] Formula
> $$ \text{Valore Aggiunto} = \text{Produzione} - \text{Costi Materie Prime/Diretti} $$

**Collegamenti**
Richiede: Riclassificazione Conto Economico. Usato in: Margine Operativo Lordo (MOL).

### 2.3 Margine Operativo Lordo (MOL / EBITDA)
> [!important] Definizione: Margine Operativo Lordo (MOL)
> Il MOL (EBITDA - *Earnings Before Interest, Taxes, Depreciation and Amortization*) è il guadagno derivante dall'attività operativa prima di considerare interessi, tasse, svalutazioni e ammortamenti.
>
> $$ \text{MOL} = \text{Valore Aggiunto} - \text{Costi del Personale} $$

**Perché serve**
Il MOL è l'indicatore principale della redditività operativa. Indica se l'azienda è in grado di coprire tutti i costi diretti (materie prime + lavoro) e generare un margine positivo dalla sua attività principale.

**Esempio concreto**
Se un'azienda ha un valore aggiunto di 100.000€ ma deve pagare 80.000€ di stipendi ai dipendenti, il suo MOL è di soli 20.000€. Questo indica che l'attività operativa è "stretta" e poco capace di generare surplus per coprire altri costi (come gli ammortamenti o i debiti).

**Derivazione**
1. Si parte dal Valore Aggiunto.
2. Si sottraggono i costi del personale interno (costi operativi monetari).
3. Il risultato è il MOL, che include tutti i costi diretti (materie prime + lavoro).

**Formule chiave**
> [!important] Formula
> $$ \text{MOL} = \text{Valore Aggiunto} - \text{Costi del Personale} $$

**Collegamenti**
Richiede: Valore Aggiunto. Usato in: Reddito Operativo Lordo (ROL).

### 2.4 Reddito Operativo Lordo (ROL / EBIT)
> [!important] Definizione: Reddito Operativo Lordo (ROL)
> Il ROL (EBIT - *Earnings Before Interest and Tax*) è il guadagno prima di pagare interessi e imposte, spesso definito come Margine Operativo Netto (al netto degli ammortamenti).
>
> $$ \text{ROL} = \text{MOL} - \text{Costi Operativi Non Monetari} $$

**Perché serve**
Serve a capire quanto l'azienda produce di profitto considerando anche il "consumo" dei beni strumentali (ammortamenti) e le svalutazioni, senza però considerare come questo profitto venga poi ripartito tra Stato, banche e soci.

**Esempio concreto**
Un'azienda ha un MOL di 50.000€, ma i macchinari usati per produrre si svalutano ogni anno di 10.000€. Il ROL sarà di 40.000€. Questo valore rappresenta il vero "guadagno" generato dall'attività produttiva nel periodo.

**Derivazione**
1. Si parte dal Margine Operativo Lordo (MOL).
2. Si sottraggono i costi operativi non monetari: ammortamenti, svalutazioni e accantonamenti.
3. Il risultato è il ROL/EBIT.

**Formule chiave**
> [!important] Formula
> $$ \text{ROL} = \text{MOL} - (\text{Ammortamenti} + \text{Svalutazioni} + \text{Accantonamenti}) $$

**Collegamenti**
Richiede: Margine Operativo Lordo (MOL). Usato in: Reddito d'Esercizio.

> [!warning] Attenzione
> Il ROL non tiene conto degli interessi e delle imposte. Questo significa che un'azienda può avere un ROL positivo ma un utile netto negativo se il debito bancario è troppo elevato o se le tasse sono eccessive.

> [!example] Esercizio 2
> Un'azienda presenta i seguenti dati:
> - Valore della Produzione: 500.000€
> - Costi Materie Prime: 150.000€
> - Costi del Personale: 100.000€
> - Ammortamenti e Svalutazioni: 30.000€
> Calcola il Valore Aggiunto, il MOL e il ROL.
>
> *Soluzione:*
> 1. **Valore Aggiunto** = $500.000€ - 150.000€ = 350.000€$.
> 2. **MOL** = $350.000€ - 100.000€ = 250.000€$.
> 3. **ROL** = $250.000€ - 30.000€ = 220.000€$.

# Riclassificazione del Conto Economico a Valore Aggiunto

## Analisi dei risultati operativi e finanziari

Con la determinazione del **Reddito Operativo Lordo** si conclude la parte operativa della riclassificazione del conto economico a valore aggiunto e inizia quella finanziaria.

### Reddito Ante Imposte (EBT)

> [!important] Reddito Ante Imposte (RAI / EBT)
> Il reddito ante imposte rappresenta il risultato economico dell'azienda derivante dalle attività operative e finanziarie, prima che venga applicata la tassazione dello Stato.
> 
> In termini pratici, indica quanto l'azienda ha effettivamente guadagnato o perso considerando i costi del capitale (interessi), ma senza ancora considerare il prelievo fiscale.
> 
> $$RAI = \text{Reddito Operativo} - \text{Interessi Passivi} + \text{Interessi Attivi}$$

**Perché serve**
Serve a isolare l'effetto della struttura del debito e delle attività finanziarie sul risultato finale, permettendo di capire se l'azienda è redditizia "prima" degli obblighi fiscali.

**Esempio concreto**
Un'azienda che genera un reddito operativo di 100.000€ ma ha debiti bancari che le costano 10.000€ di interessi passivi avrà un RAI di 90.000€. Se possiede anche depositi che generano 2.000€ di interessi attivi, il RAI finale sarà di 92.000€.

**Formule chiave**
| Parametro | Formula |
|:---|:---|
| **Reddito Ante Imposte (RAI)** | $RAI = \text{Reddito Operativo} - \text{Interessi Passivi} + \text{Interessi Attivi}$ |

**Collegamenti**
Richiede: [Reddito Operativo]. Usato in: [Reddito di Esercizio].

### Reddito di Esercizio (RE)

> [!important] Reddito di Esercizio (RE)
> Il reddito di esercizio, o utile di esercizio, è il risultato finale netto dell'attività economica dell'impresa in un determinato periodo, calcolato dopo la deduzione delle imposte.
> 
> $$RE = RAI - \text{Imposte}$$

**Perché serve**
È l'indicatore definitivo della capacità dell'azienda di generare ricchezza netta per i soci o per il reinvestimento, rappresentando la base per la formazione del patrimonio netto.

**Esempio concreto**
Se un'azienda ha un RAI di 92.000€ e deve pagare 23.000€ di imposte sul reddito, il Reddito di Esercizio sarà di 69.000€. Questa cifra verrà poi trasferita nello Stato Patrimoniale.

**Formule chiave**
| Parametro | Formula |
|:---|:---|
| **Reddito di Esercizio (RE)** | $RE = RAI - \text{Imposte}$ |

**Collegamenti**
Richiede: [Reddito Ante Imposte]. Usato in: [Stato Patrimoniale (Patrimonio Netto)].

> [!quote] Osservazione
> Il Reddito di Esercizio viene inserito nello Stato Patrimoniale alla sezione del patrimonio netto, poiché rappresenta la quota di ricchezza che rimane in azienda a disposizione dei proprietari.

---

## Conto Economico a Margine di Contribuzione

Il conto economico a **Margine di Contribuzione** si basa sulla distinzione fondamentale tra costi fissi e variabili. Questo modello è particolarmente utile per determinare rapidamente il punto di pareggio (*break-even point*).

> [!warning] Attenzione
> La costruzione di questo modello può essere complessa poiché, nella realtà aziendale, la distinzione netta tra costi variabili e fissi non è sempre immediata (es. costi semi-variabili come l'energia elettrica o i consulenti).

### Classificazione dei Costi

Per comprendere il margine di contribuzione, è necessario distinguere correttamente le componenti del **Costo Totale**.

> [!important] Costo Totale
> Il costo totale è la somma algebrica dei costi fissi e dei costi variabili.
> 
> $$CT = CF + CV$$

**Perché serve**
Permette di analizzare come variano i costi al variare del volume di produzione o vendita, facilitando le decisioni su prezzi e volumi.

**Esempio concreto**
In una fabbrica di scarpe, l'affitto del capannone rimane uguale sia che si producano 100 paia, sia che se ne producano 10.000 (Costo Fisso). Al contrario, la pelle e il collante necessari per ogni paio variano direttamente con la produzione (Costo Variabile).

**Definizioni di base**
- **Costi Fissi (CF)**: Costi che non variano al variare delle quantità prodotte o vendute (es. stipendi fissi, ammortamenti, fitti, spese generali e di amministrazione come marketing e formazione).
- **Costi Variabili (CV)**: Costi direttamente e proporzionalmente legati alla quantità di beni e servizi prodotti (es. materie prime, carburante, manutenzioni dirette).

**Tabella 1: Esempi di Classificazione dei Costi**
| **VOCE DI COSTO** | **CLASSIFICAZIONE** |
|:---|:---|
| Materie Prime | Variabile |
| Energia Elettrica | Variabile/Fisso |
| Gas | Variabile |
| Riscaldamento | Variabile/Fisso |
| Acqua | Variabile/Fisso |
| Telefono | Variabile/Fisso |
| Carburante | Variabile |
| Manutenzioni | Variabile |
| Consulenti | Variabile/Fisso |
| Ammortamenti | Fisso |
| Affitti e noleggi | Variabile/Fisso |
| Personale | Fisso |
| Imposte non sul reddito | Fisso |

Tabella 1: Esempi di Classificazione dei Costi

> [!example] Esercizio 1
> Un'azienda produce gadget. I costi fissi mensili sono di 5.000€. Il costo variabile unitario è di 10€. Se il prezzo di vendita unitario è di 25€, calcola il margine di contribuzione unitario e il numero di unità da vendere per raggiungere il punto di pareggio (Break-even Point).
> 
> *Suggerimento: Il margine di contribuzione unitario è la differenza tra prezzo di vendita e costo variabile unitario.*
> 
> **Soluzione:**
> 1. Calcolo Margine di Contribuzione Unitario ($MC$):
>    $$MC = \text{Prezzo} - CV_{unitario} = 25€ - 10€ = 15€$$
> 2. Calcolo Punto di Pareggio ($Q_{BEP}$):
>    Il punto di pareggio si raggiunge quando il margine di contribuzione totale copre i costi fissi.
>    $$Q_{BEP} = \frac{CF}{MC} = \frac{5.000€}{15€} \approx 333,33$$
> L'azienda deve vendere almeno 334 unità per non andare in perdita.

# Analisi degli Indici di Bilancio

## Introduzione agli indici di bilancio

Gli **indici di bilancio** sono indicatori sintetici derivanti dall'elaborazione di grandezze patrimoniali, finanziarie ed economiche estratte dallo stato patrimoniale e dal conto economico. La loro funzione primaria è permettere un confronto agevole tra bilanci di annualità differenti o tra imprese diverse appartenenti allo stesso settore.

L'analisi tramite questi indici permette di osservare tre dimensioni fondamentali:
- **Redditività**: la capacità dell'impresa di produrre reddito (utile). Serve all'azienda per monitorare il rapporto ricavi/costi e agli investitori per prevedere i ritorni economici.
- **Liquidità**: informazioni sulla situazione finanziaria e sui flussi monetari durante l'esercizio.
- **Solvibilità**: la capacità dell'impresa di onorare i propri debiti entro le scadenze previste.

## Indicatori di Redditività e Gestione

### ROE (Return On Equity)

> [!important] ROE (Return On Equity)
> Il ROE è un indice economico che misura il tasso di remunerazione del capitale proprio, ovvero quanto rende il capitale conferito ai soci rispetto all'utile generato.
> 
> **Formula:**
> $$ROE = \frac{\text{Utile Netto}}{\text{Capitale Proprio}} \times 100$$

**Perché serve**
Serve a valutare l'efficacia del management nel gestire i mezzi propri per generare utili. Fornisce agli azionisti una misura diretta del rendimento del loro investimento di rischio.

**Esempio concreto**
Un'azienda con un capitale proprio di 1.000.000 € che genera un utile netto di 100.000 € ha un ROE del 10%. Se il tasso di interesse di mercato per investimenti simili fosse del 5%, l'investimento nell'azienda è considerato remunerativo.

**Collegamenti**
Richiede: [Utile Netto], [Capitale Proprio]. Usato in: Analisi della gestione finanziaria e patrimoniale.

> [!warning] Attenzione
> Il ROE non dipende solo dalla gestione caratteristica (produzione/vendite), ma è influenzato pesantemente dalle decisioni di gestione finanziaria (es. livello di indebitamento) e patrimoniale. Un ROE molto alto potrebbe essere dovuto a un eccessivo indebitamento piuttosto che a una reale efficienza operativa.

### ROI (Return on Investment)

> [!important] ROI (Return on Investment)
> Il ROI è un indicatore che misura la redditività della gestione caratteristica rispetto all'intero finanziamento aziendale, ovvero la capacità di generare profitto dall'utilizzo efficiente delle risorse investite.
> 
> **Formula:**
> $$ROI = \frac{\text{Reddito Operativo}}{\text{Capitale Investito Netto Operativo}}$$

**Perché serve**
Serve a capire quanta quantità di denaro un'impresa è in grado di generare dopo aver investito in qualsiasi attività, indipendentemente dalla fonte di finanziamento utilizzata (debiti o capitale proprio).

**Esempio concreto**
Un'azienda acquista un macchinario industriale per 500.000 € (Capitale Investito Netto Operativo). Se tale investimento genera un reddito operativo annuo di 50.000 €, il ROI è del 10%.

**Collegamenti**
Richiede: [Reddito Operativo], [Capitale Investito Netto Operativo].

### ROS (Return on Sale)

> [!important] ROS (Return on Sale)
> Il ROS, o redditività delle vendite, misura l'efficienza operativa di un'azienda valutando quanto profitto viene prodotto per ogni euro incassato dalle vendite.
> 
> **Formula:**
> $$ROS = \frac{\text{Utile Operativo (EBIT)}}{\text{Vendite Nette}}$$

**Perché serve**
Serve a capire la capacità dell'azienda di trasformare il volume delle vendite in profitto effettivo, evidenziando l'efficienza dei processi produttivi e commerciali.

**Esempio concreto**
Un'azienda che vende prodotti per 1.000.000 € e ottiene un utile operativo (EBIT) di 200.000 € ha un ROS del 20%. Ciò significa che per ogni euro di vendita, l'azienda trattiene 20 centesimi come profitto operativo.

**Collegamenti**
Richiede: [EBIT], [Vendite Nette].

### ROA (Return on Asset)

> [!important] ROA (Return on Asset)
> Il ROA misura la redditività degli asset aziendali, ovvero l'efficienza con cui l'azienda utilizza tutto il suo attivo (immobilizzazioni, liquidità, attività finanziarie, crediti, materie prime e rimanenze) per generare utile.
> 
> **Formula:**
> $$ROA = \frac{\text{Utile Operativo}}{\text{Totale Attivo}} \times 100$$

**Perché serve**
Serve a valutare quanto bene l'azienda stia utilizzando le proprie risorse materiali e immateriali per produrre reddito. È un indicatore di efficienza nell'uso dei beni.

**Esempio concreto**
Un'impresa con un totale attivo di 2.000.000 € che genera un utile operativo di 160.000 € ha un ROA dell'8%. Questo indica il rendimento generato da ogni euro investito nell'attivo aziendale.

**Collegamenti**
Richiede: [Utile Operativo], [Totale Attivo].

### EBIT (Earnings before Interest & Tax)

> [!important] EBIT (Earnings before Interest & Tax)
> L'EBIT rappresenta il reddito o utile operativo, ovvero l'utile di una società prima della deduzione degli interessi passivi e delle imposte sul reddito.
> 
> **Formule:**
> $$EBIT = \text{Reddito Netto} + \text{Interessi} + \text{Tasse}$$
> $$EBIT = \text{Ricavi} - \text{Costi dei beni venduti} - \text{Spese operative}$$

**Perché serve**
L'EBIT è fondamentale perché permette di valutare la redditività del "core business" dell'impresa, isolando il risultato dalla struttura finanziaria (interessi) e dal carico fiscale.

**Derivazione**
L'EBIT si ricava partendo dal Reddito Netto aggiungendo le componenti sottratte per arrivare al risultato operativo:
1. Si parte dal *Reddito Netto* (risultato finale dopo tasse e interessi).
2. Si sommano gli *Interessi Passivi* (costi del debito).
3. Si sommano le *Tasse* (imposte sul reddito).
Il risultato è il profitto generato puramente dalle attività operative dell'azienda.

**Collegamenti**
Richiede: [Reddito Netto], [Ricavi]. Usato in: [ROS], [ROA].

> [!example] Esercizio 1
> Un'azienda presenta i seguenti dati di bilancio:
> - Vendite Nette: 500.000 €
> - Utile Netto: 40.000 €
> - Interessi Passivi: 10.000 €
> - Tasse: 20.000 €
> - Totale Attivo: 800.000 €
>
> Calcolare l'EBIT, il ROS e il ROA.
>
> *Soluzione:*
> 1. **EBIT**: $40.000 + 10.000 + 20.000 = 70.000 €$
> 2. **ROS**: $\frac{70.000}{500.000} \times 100 = 14\%$
> 3. **ROA**: $\frac{70.000}{800.000} \times 100 = 8,75\%$

# Indici di Bilancio

## 1. EBITDA (Margine Operativo Lordo)

> [!important] **EBITDA** (o **Margine Operativo Lordo**)
> L'EBITDA (*Earnings Before Interest, Taxes, Depreciation and Amortization*) rappresenta la capacità di un'impresa di generare flussi di cassa operativi prima che vengano dedotti gli oneri finanziari, le imposte e i costi non monetari come ammortamenti e svalutazioni.
> 
> In termini pratici, indica quanto profitto "puro" produce l'attività principale dell'azienda. Ad esempio, se un'azienda produttrice di smartphone vende prodotti per 1 milione di euro e spende 600.000 euro per componenti, produzione e personale, il suo EBITDA riflette la redditività operativa prima di considerare come quel profitto viene finanziato (interessi) o tassato.
> 
> Formalmente, l'EBITDA può essere calcolato partendo dall'utile netto aggiustandolo per le voci non operative:
> $$ \text{EBITDA} = \text{Utile Netto} + \text{Tasse} + \text{Interessi Passivi} + \text{Ammortamenti e Svalutazioni} $$
> 
> In alternativa, può essere calcolato direttamente dai ricavi e dai costi operativi:
> $$ \text{EBITDA} = \text{Fatturato} - \text{Costi di Produzione} - \text{Costi Generali} - \text{Costi del Personale} $$

**Perché serve**
L'EBITDA è fondamentale per confrontare la redditività operativa di aziende diverse, indipendentemente dalle loro strutture di debito (interessi), dalle politiche fiscali o dai diversi metodi di ammortamento degli asset. Permette di capire se il "core business" è effettivamente profittevole.

**Derivazione**
La formula che parte dall'utile netto deriva dalla struttura del Conto Economico. Poiché l'Utile Netto è il risultato finale dopo la sottrazione di tutte le voci, per risalire alla redditività operativa bisogna "sommare nuovamente" (reintegrare) quelle voci che non riguardano direttamente la produzione ma la gestione finanziaria e fiscale:
1. Partenza: $\text{Utile Netto}$
2. Aggiunta tasse: $\rightarrow \text{Utile prima delle imposte}$
3. Aggiunta interessi: $\rightarrow \text{Risultato Operativo (EBIT)}$
4. Aggiunta ammortamenti/svalutazioni: $\rightarrow \text{EBITDA}$

> [!important] **Formule Chiave**
> | Variabile | Formula di Calcolo |
> |:---|:---|
> | **EBITDA (via Utile)** | $\text{Utile Netto} + \text{Tasse} + \text{Interessi} + \text{Ammortamenti}$ |
> | **EBITDA (via Ricavi)** | $\text{Fatturato} - \text{Costi Operativi Totali}$ |

**Collegamenti**
Richiede: [Utile Netto]. Usato in: Analisi della capacità di generazione di cassa e valutazione d'azienda.

> [!warning] **Attenzione**
> L'EBITDA non è un indicatore di profitto assoluto né di liquidità immediata. Poiché non sottrae gli ammortamenti (che sono costi reali di usura del capitale), un EBITDA molto alto potrebbe nascondere una necessità critica di reinvestimento in macchinari o infrastrutture che si stanno deteriorando rapidamente.

> [!example] **Esercizio 1**
> Un'azienda ha un fatturato di 500.000 €, costi di produzione di 200.000 €, costi del personale di 100.000 € e costi generali di 50.000 €. Calcolare l'EBITDA.
> 
> *Soluzione:*
> Utilizzando la formula basata sui ricavi:
> $\text{EBITDA} = 500.000 - 200.000 - 100.000 - 50.000$
> $\text{EBITDA} = 150.000 \text{ €}$

## 2. Utile Netto

> [!important] **Utile Netto** (o Reddito Netto)
> L'utile netto è la cifra finale che rimane a disposizione dei soci o dell'imprenditore dopo aver sottratto dal fatturato tutte le spese sostenute, le tasse pagate e gli interessi passivi.
> 
> È il dato strategico per eccellenza: rappresenta la "linea finale" della redditività di una società in un determinato periodo. Se un'azienda vende molti prodotti ma ha costi fissi troppo alti o debiti eccessivi, l'utile netto potrebbe essere negativo (perdita), nonostante un EBITDA positivo.
> 
> Formalmente è espresso come:
> $$ \text{Utile Netto} = \text{Ricavi Totali} - \text{Spese} - \text{Tasse} $$

**Perché serve**
Serve a determinare se l'attività economica è sostenibile nel lungo periodo. È la base per la distribuzione dei dividendi ai soci e per la creazione di riserve di capitale per investimenti futuri.

**Esempio concreto**
Immaginiamo un ristorante: i ricavi sono le vendite dei pasti. Le spese includono gli ingredienti, l'affitto, gli stipendi dei camerieri, le bollette e le tasse sul valore aggiunto. Ciò che resta nel conto corrente del proprietario alla fine del mese, dopo aver pagato tutto, è l'utile netto.

**Derivazione**
L'utile netto si ricava dalla successione logica del Conto Economico:
1. $\text{Ricavi Totali} - \text{Costi Operativi (COGS)} = \text{Margine Lordo}$
2. $\text{Margine Lordo} - \text{Spese Generali/Amministrative} = \text{Utile Operativo (EBIT)}$
3. $\text{EBIT} - \text{Ammortamenti} = \text{Utile prima delle imposte}$
4. $\text{Utile prima delle imposte} - \text{Tasse e Interessi} = \text{Utile Netto}$

> [!important] **Formule Chiave**
> $$ \text{Utile Netto} = \text{Ricavi Totali} - \text{Spese} - \text{Tasse} $$

**Collegamenti**
Richiede: [Fatturato], [Costi]. Usato in: Calcolo dell'EBITDA e analisi della redditività finale.

![](https://cdn-mineru.openxlab.org.cn/result/2026-07-03/6c129d73-2956-4f9e-bdb2-e951cc30db9e/d762f8e7f0db08b359d5ced532c1034bb21baef6d14a0810c5fbab1d4ce07b0c.jpg)
Figura 1: Rappresentazione grafica degli indici di bilancio.