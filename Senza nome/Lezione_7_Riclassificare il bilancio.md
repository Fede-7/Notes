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
Figura 1: Rappresentazione grafica degli indici di bilancio.# Lezione 10 - Riclassificare il bilancio

## Introduzione alla riclassificazione del bilancio

Il concetto di **riclassificazione del bilancio** si riferisce all'operazione contabile e analitica di riassegnare delle voci di spesa o di entrata da una categoria a un'altra, al fine di riflettere con maggiore precisione la natura economica o l'obiettivo strategico dell'utilizzo dei fondi.

> [!important] Riclassificazione del Bilancio
> **Definizione:** Processo di riallocazione sistematica di elementi finanziari tra diverse classi di costo o centri di profitto all'interno di un bilancio preesistente, effettuato per correggere errori di imputazione iniziale o per adattare la struttura contabile a nuove priorità operative.

**Perché serve**
Senza una riclassificazione periodica, il bilancio rischia di diventare una fotografia distorta della realtà aziendale: spese fondamentali potrebbero essere sottostimate perché erroneamente catalogate come "accessorie", rendendo difficile per il management prendere decisioni basate su dati accurati.

> [!example] Esempio concreto
> In un'azienda di telecomunicazioni, una spesa inizialmente inserita come "Manutenzione Ordinaria" (costo operativo corrente) potrebbe essere riclassificata come "Investimento in Infrastruttura" (CapEx) se l'intervento ha esteso la vita utile del server o ne ha aumentato la capacità di banda. Questa distinzione è cruciale per il calcolo dell'ammortamento e della redditività a lungo termine.

**Derivazione**
La riclassificazione segue un processo logico-formale basato sulla verifica della destinazione d'uso:
1. Identificazione della voce di spesa/entrata oggetto di revisione.
2. Analisi della natura economica (es. è un costo ricorrente o un investimento?).
3. Verifica della conformità alle norme contabili vigenti (es. principi di competenza).
4. Registrazione dell'estorno dalla categoria originale e l'imputazione nella nuova classe.
5. Aggiornamento dei saldi e generazione del bilancio rettificato.

**Formule chiave**
> [!important] Riepilogo Formule
> $$ \text{Bilancio}_{\text{Rettificato}} = \sum (\text{Voci}_{\text{Originali}}) - \Delta_{\text{Estorno}} + \Delta_{\text{Imputazione}} $$
> Dove $\Delta$ rappresenta la variazione netta dovuta alla riclassificazione.

**Collegamenti**
Richiede: [Bilancio Preventivo]. Usato in: [Analisi delle Varianze], [Reporting Finanziario].

> [!warning] Attenzione
> Una riclassificazione non deve mai essere utilizzata per "nascondere" debiti o spese eccessive spostandole in categorie meno visibili. La distinzione tra errore di imputazione (corretto dalla riclassificazione) e manipolazione contabile è fondamentale per la conformità legale.

> [!example] Esercizio 1
> Un'azienda ha registrato una spesa di $50.000$ per l'acquisto di nuovi software gestionali sotto la voce "Materiali di Consumo". Sapendo che il software è un bene immateriale destinato a durare più di un anno, riclassifica la voce.
>
> *Soluzione:*
> La spesa deve essere spostata dalla categoria "Costi Variabili/Consumabili" alla categoria "Attività Immateriali / Investimenti". 
> 1. Estorno: $-50.000$ da Materiali di Consumo.
> 2. Imputazione: $+50.000$ in Software e Licenze.
> Il bilancio rettificato riflette correttamente l'investimento tecnologico anziché un semplice consumo di materiali.

# Corso EOA

**Prof. Giuseppe Piccirillo**

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/965dd9f0ba4e47210558a6e47054fb082718dec7e6101f21e753ebe85ea5bb51.png)

## Riclassificazione dello Stato Patrimoniale e del Conto Economico

### Riclassificazione dei dati finanziari

> [!important] Riclassificazione
> La **riclassificazione** consiste nel disporre i dati di partenza contenuti nello stato patrimoniale e nel conto economico in una struttura diversa, attraverso processi di disaggregazione, riaggregazione e riordinamento. L'obiettivo è evidenziare specifiche voci per favorire il confronto o l'analisi tecnica dei flussi finanziari.

La riclassificazione serve a trasformare una rappresentazione puramente contabile (spesso orientata alla cronologia delle operazioni) in una rappresentazione funzionale o finanziaria, permettendo di identificare immediatamente la capacità dell'azienda di generare liquidità e di onorare i propri impegni.

> [!example] Esempio concreto
> In un'azienda di telecomunicazioni (come Alfa S.p.A.), la riclassificazione permette di distinguere tra gli investimenti in infrastrutture (attività consolidate) e le scorte di componenti o i crediti verso i clienti (attività correnti), facilitando il calcolo della capacità di copertura dei debiti a breve termine.

### Struttura dello Stato Patrimoniale Riclassificato

Lo stato patrimoniale riclassificato mantiene la separazione tra attività e passività, ma le ordina in maniera decrescente in funzione della loro **liquidità** (per le attività) o **esigibilità** (per le passività). Le voci che si trasformano in denaro più rapidamente sono poste nella parte alta dello schema.

#### Attività
Le attività sono classificate in base al momento in cui genereranno un flusso di cassa:
- **Attività correnti**: quelle che possono essere monetizzate entro 12 mesi.
- **Attività consolidate (o immobilizzate)**: quelle con una scadenza o durata superiore ai 12 mesi. Queste sono ulteriormente suddivise per natura in:
    - Materiali;
    - Immateriali;
    - Finanziarie.

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/d3846d07a6d631100f216a91d4d9eb8f9efcb36b3884232ae85591745a003a94.png)

#### Passività
Le passività sono classificate prima in base alla loro provenienza:
- **Capitale proprio**: fonti di finanziamento interne all'azienda.
- **Capitale di terzi**: fonti di finanziamento esterne all'azienda.

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/5dd681117a714d7c0b99f7dc55e3adc9e194b37758cbed37dc42234f6f43c415.png)

### Analisi della Corrispondenza Temporale (Criterio Finanziario)

L'aggregazione delle voci in correnti e consolidate permette di verificare la corrispondenza tra le scadenze temporali degli investimenti e dei finanziamenti.

> [!warning] Attenzione
> Una situazione critica si verifica quando le **passività a breve termine sono maggiori delle attività correnti**. 
> In questo caso, l'azienda non dispone di risorse sufficienti (monetizzabili entro 12 mesi) per coprire i debiti che scadono nello stesso periodo. Ciò genera forti tensioni finanziarie che possono essere risolte solo tramite:
> 1. Operazioni straordinarie di vendita o dismissione di attività consolidate (spesso a prezzi svantaggiosi);
> 2. Rinegoziazione e allungamento delle passività in scadenza, con relativi costi finanziari.

![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/e861275957592463d208b090fb529be732dfecad37ca162ef5173f3335eeba7e.jpg)

### Esercizio di applicazione: Alfa S.p.A.

Si considerino i dati della società Alfa S.p.A. (settore telecomunicazioni) per l'esercizio 2009.

> [!example] Esercizio 1
> **Testo**: Collocare le voci fornite nel prospetto dello Stato Patrimoniale riclassificato secondo il "criterio finanziario".
> 
> **Dati da collocare**:
> - 12.205
> - 1.000
> - 215
> - 17.600 (sottolineato)
> - 17.815 (sottolineato)
> - 265
> - 18.080 (sottolineato)
> - 27.058
> - 55.640
> - 32.412
> - 8.978 (grassetto/sottolineato)
> - 9.243 (grassetto/sottolineato)
> - 23.228 (grassetto/sottolineato)
> 
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/a01864a06ecac2a827c2bdeaf2c868d0731c3cb306c0a4d97d70f4aa01e46685.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/106b194820abc58dcae6789a196b0d62a6eb6b6868346baf9327b19cf3a79cd9.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/4ff7469567a1465558d717f3e69dfda7ec1a04cacc3c60c587759a238b747677.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/a206157603c361b858656710a1a9faa79d6f6cfc4f33bc97cbe7fb571013552d.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/2904b9e27feb5b744fa26f636163b1601fb70082645379ed609fed4eaae01cfe.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/a206157603c361b858656710a1a9faa79d6f6cfc4f33bc97cbe7fb571013552d.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/2904b9e27feb5b744fa26f636163b1601fb70082645379ed609fed4eaae01cfe.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/a206157603c361b858656710a1a9faa79d6f6cfc4f33bc97cbe7fb571013552d.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/2904b9e27feb5b744fa26f636163b1601fb70082645379ed609fed4eaae01cfe.png)
> 
> **Soluzione**: 
> *Nota: La soluzione richiede la disposizione dei valori nelle categorie correnti/consolidate e capitale proprio/terzi basandosi sulla liquidità e provenienza indicata dai dati del bilancio.*

### Riclassificazione del Conto Economico

Il Conto Economico viene riclassificato secondo il criterio "ricavi e costo del venduto".

> [!example] Esercizio 2
> **Testo**: Collocare le voci fornite nel prospetto di Conto Economico riclassificato a “ricavi e costo del venduto” per la società Alfa S.p.A. ed esprimere un giudizio sul contributo delle varie "aree di gestione" alla formazione del risultato economico.
> 
> **Dati da collocare**:
> - 900
> - 14 (valore associato a IMGPATH_0014)
> - 15 (valore associato a IMGPATH_0015)
> - 16 (valore associato a IMGPATH_0016)
> 
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/f99cfc108997b4172c99a7a480d950c80e9ab2a3a8cb099d3f5785245cfa41c4.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/94b7b6683ab955b0157d5aa8ebf4dcf6eaeb433e869cf62909bd5332e398cce3.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/22f39229c81bad883e28f0e1b4dbbcd8c1400547ddea427391b82768c9cd03d7.png)
> ![alt](https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/28eb66f3379248f31165968d7713b481302e6d62b61eb9b878746a90bbd73500.png)
> 
> **Soluzione**:
> *Il giudizio deve analizzare come le diverse aree (es. vendita, produzione, servizi) contribuiscano positivamente o negativamente al margine operativo e al risultato finale.*

## Analisi dei Risultati Finanziari

### Analisi dell'Utile di Esercizio e Indicatori Relativi

L'analisi di un singolo dato isolato, come l'utile netto di un esercizio (ad esempio 2,8 milioni), fornisce una visione statica della performance aziendale ma non permette di valutarne la solidità o l'efficienza operativa. Per trasformare un dato assoluto in informazione utile per il processo decisionale, è necessario contestualizzarlo attraverso analisi comparative o indicatori di intensità.

> [!important] **Analisi Percentuale dei Ricavi**
> L'analisi percentuale consiste nel calcolare il peso relativo di ogni voce del conto economico (costi, margini, utili) rispetto al totale dei ricavi di vendita. 
>
> Formalmente, per una determinata grandezza $G$ presente nel conto economico e per i ricavi totali $R$, il peso percentuale $P_G$ è definito come:
> $$P_G = \left( \frac{G}{R} \right) \times 100$$

**Perché serve**
Questa analisi permette di misurare l'efficienza della struttura dei costi e la redditività reale. Senza il confronto con i ricavi, non è possibile capire se un utile di 2,8 milioni sia il risultato di una gestione eccellente su volumi elevati o se sia un valore marginale per un'azienda con fatturati molto più alti.

**Esempio concreto**
Consideriamo due aziende:
1. Azienda A: Utile 2,8 milioni su Ricavi 5 milioni $\rightarrow$ Margine di profitto del 56%.
2. Azienda B: Utile 2,8 milioni su Ricavi 100 milioni $\rightarrow$ Margine di profitto del 2,8%.
Sebbene l'utile assoluto sia identico, la struttura operativa e la capacità di generare valore rispetto alle vendite sono drasticamente diverse.

**Formule chiave**
> [!important] Indicatori di Redditività
> $$P_G = \frac{G}{R} \times 100$$
> Dove:
> - $G$: Grandezza del conto economico (es. Costo del Venduto, Utile Operativo, Utile Netto).
> - $R$: Ricavi di vendita totali.

**Collegamenti**
Richiede: [Dati del Conto Economico]. Usato in: [Analisi Comparativa tra Concorrenti], [Valutazione della Struttura dei Costi].

> [!warning] Attenzione
> L'analisi percentuale non sostituisce l'analisi comparativa. Un'azienda può avere un ottimo peso percentuale rispetto ai ricavi ma trovarsi comunque in una posizione di svantaggio competitivo rispetto a un concorrente che opera con margini più elevati o volumi superiori.

> [!example] Esercizio 1
> Una società presenta i seguenti dati nel conto economico:
> - Ricavi di vendita: 12.000.000 €
> - Costi operativi: 8.400.000 €
> - Utile di esercizio: 3.600.000 €
>
> Calcolare il peso percentuale dell'utile rispetto ai ricavi e la percentuale dei costi operativi sui ricavi.
>
> *Suggerimento: Applica la formula $P_G = (G/R) \times 100$ per entrambe le voci.*
>
> **Soluzione:**
> 1. Peso dell'utile: $P_{Utile} = (3.600.000 / 12.000.000) \times 100 = 30\%$.
> 2. Peso dei costi operativi: $P_{Costi} = (8.400.000 / 12.000.000) \times 100 = 70\%$.
> L'azienda trattiene il 30% del proprio fatturato come utile netto dopo aver coperto i costi operativi.

!https://cdn-mineru.openxlab.org.cn/result/2026-07-02/810e3547-925c-4af2-9359-0fe00aeefce2/4b2749577e3c2a5d0b947cef91eb925e734bb510ab44dccd76af93cd2aac08b6.png(Figura 1: Rappresentazione dei dati del conto economico)# Lezione 11 - Riclassificare il bilancio

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