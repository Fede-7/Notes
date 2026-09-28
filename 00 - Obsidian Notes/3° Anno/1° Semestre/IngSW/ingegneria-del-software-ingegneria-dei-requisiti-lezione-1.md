# Lezione 1 — Ingegneria dei requisiti: concetti e processo

## Perché i requisiti sono il punto critico dello sviluppo

Il **prodotto software**, a differenza di un semplice programma scritto per sé stessi, nasce da un processo industriale articolato in fasi, ognuna con competenze precise. Prima di affrontare la raccolta dei requisiti, va ricordato che la **qualità** è un concetto ampio e inclusivo: nessun software può massimizzare tutti gli attributi di qualità contemporaneamente, e il bravo software engineer è chi, per il problema che ha davanti, individua quali attributi massimizzare.

Una delle citazioni più celebri dell'ingegneria del software, tratta da uno dei primissimi libri della disciplina (Fred Brooks), afferma che la parte più difficile del costruire un sistema software è decidere *cosa* costruire: nessun'altra parte del lavoro è concettualmente tanto complessa quanto definire i requisiti tecnici dettagliati e, soprattutto, nessun'altra parte rovina tanto il sistema risultante se fatta male. Se un algoritmo subottimale si può sistemare modificandolo, un requisito capito male — o peggio, un attributo di qualità stimato male — può rende più conveniente buttare l'intero progetto e ricominciare da zero, con un danno enorme per la software house.

>[!info] Il paradosso della parte "facile"
>Per certi versi il coding è più facile rispetto alla parte più difficile del mestiere: capire cosa vuole davvero un altro essere umano, soprattutto quando quel essere umano è il primo a non avere un'idea chiara di ciò che vuole.

## Terminologia: cosa sono i requisiti

I **requisiti** (*requirements*) sono una descrizione di ciò che il sistema dovrebbe fare, in termini di **servizi da offrire** e di **vincoli** sotto cui offrirli. Ad esempio: il sistema deve permettermi di iscrivermi a un appello d'esame (servizio), ma devo poterlo fare in un ambiente web, solo se sono studente di quel ateneo, magari anche da smartphone, e l'elenco degli iscritti deve essere trattato secondo la GDPR (vincoli). Non è quindi solo *cosa* il sistema fa, ma anche *come* e *sotto quali vincoli* deve farlo.

La parte dei vincoli è spesso nuova per chi proviene da corsi di programmazione: finora i vincoli ricevuti erano principalmente tecnologie obbligatorie (usare un database, un linguaggio, una struttura controller-based). Ma esistono vincoli ben più delicati, come quelli di **performance**: il sistema deve reggere, ad esempio, 10.000 accessi concorrenti, come richiederebbero i siti di grandi enti pubblici o i servizi di vendita di biglietti in presenza di eventi molto richiesti. Per far fronte a questi carichi esiste la **scalabilità**: la capacità di far partire nuovi server (tipicamente in cloud, sfruttando le infrastrutture di Amazon, Google o Microsoft) man mano che il carico cresce.

### Livelli di astrazione: user e system requirements

Un requisito può essere espresso a livelli di dettaglio molto diversi. Lo **user requirement** è la descrizione generica dal punto di vista dell'utente ("vorrei poter prenotare un appello d'esame"). Da solo non basta: deve essere trasformato, da chi fa ingegneria dei requisiti, in **system requirements**, cioè descrizioni più operative, strutturate e formalizzate, che il team di sviluppo possa effettivamente implementare. La trasformazione richiede un accordo con il cliente su cosa verrà costruito: se il requisito resta vago ("voglio prenotarmi a un appello"), implementare anche un sistema perfetto può finire in un contenzioso, perché il cliente magari si aspettava qualcosa di completamente diverso.

Esempio di trasformazione: dallo user requirement "il sistema dovrebbe generare un report mensile degli iscritti a un corso" si passa a requisiti di sistema come:

- il report va generato l'ultimo giorno lavorativo di ogni mese;
- deve mostrare, per ogni corso, il totale degli iscritti nel mese corrente e statistiche correlate;
- l'accesso al report deve essere ristretto al solo gestore del corso.

Gli user requirements servono come base per contrattare il costo del software; una volta raggiunto l'accordo, i system requirements diventano il contratto reale. Nella pubblica amministrazione il documento dei requisiti può diventare parte integrante del contratto, firmato da entrambe le parti. Questo documento è l'output dell'ingegneria dei requisiti: si lavora ancora lontani dal software, in fase di pura specifica testuale.

### Classificazione: funzionali, qualità, vincoli

Oltre al livello di dettaglio, esiste una visione ortogonale: *cosa* la frase del cliente sta descrivendo. Si distinguono tre tipologie:

- **Requisiti funzionali** (*functional requirements*): descrivono le funzionalità, cioè cosa il sistema deve fare.
- **Requisiti di qualità** (*quality requirements*): definiscono quanto bene il sistema deve funzionare (performance, affidabilità, ecc.), e vanno discussi col cliente in modo realistico: non si può chiedere un software che regge un miliardo di connessioni con un budget di mille euro.
- **Vincoli** (*constraints*): limitazioni non necessariamente legate alla qualità, come vincoli tecnologici ("il nuovo sistema deve usare il DB Oracle già in casa" o "deve essere deployato su Amazon AWS") o vincoli legali (in Europa, qualunque software tratti dati sensibili deve essere **compliant alla GDPR**, che disciplina chi accede ai dati, come si conservano, quali dati biometrici si possono raccogliere).

Sui libri di testo, requisiti di qualità e vincoli vengono spesso raggruppati sotto l'etichetta di **requisiti non funzionali** (*non-functional requirements*): tutto ciò che non è "cosa fa il sistema".

>[!warnings] Il confine è grigio
>La distinzione funzionale/non funzionale sembra netta ma non lo è. "Il sistema può far accedere solo gli studenti della Federico II" è insieme una funzionalità e un vincolo: alcune affermazioni si etichettano chiaramente, altre restano in una zona grigia.

### Fonti dei requisiti non funzionali

I requisiti non funzionali non vengono solo dal prodotto: possono venire dall'organizzazione o da **regolatori esterni** (*third-party regulators*). In ambiti come quello aeronautico o aerospaziale il software deve essere scritto, testato e documentato secondo specifiche di certificazione (ad esempio la DO-178 per il software che va sugli aerei civili); in ambito automotive, chi sviluppa software per i quadri di bordo delle vetture è soggetto a regole analoghe. Esistono poi gli **organizational requirements**: convenzioni interne alla software house su come si scrive il codice (nomenclatura di variabili, classi e metodi, stile), non richieste dal cliente né dalla legge, ma regole affinché tutto il codice prodotto dall'azienda sia coerente; è noto il caso di standard interni che, ad esempio, vietano la ricorsione. Anche i vincoli contabili esistono: un software che trasmette dati all'Agenzia delle Entrate deve rispettare formati di interscambio precisi.

In sintesi, i requisiti non funzionali possono derivare dal prodotto (specifici del sistema in sé), dall'organizzazione o da fonti esterne (leggi, regolamenti, requisiti etici).

>[!info] Due pubblici, due linguaggi
>Gli user requirements sono scritti col cliente e devono essere comprensibili a persone non tecniche: non si può descrivere il sistema col salumiere usando un automa a stati. I system requirements, pur restando leggibili dal cliente, sono pensati principalmente per chi dovrà implementare. Esiste quindi un doppio livello di linguaggio.

## Le proprietà che un requisito deve avere

Un buon insieme di requisiti deve essere:

- **chiaro e comprensibile**, soprattutto al cliente;
- **non ambiguo**;
- **completo**: copre tutto ciò che c'è da fare;
- **consistente**: nessun requisito in contrasto con un altro;
- **necessario**: niente cose inutili o fuori contesto;
- **realizzabile**: implementabile realisticamente con i vincoli di budget e tecnologia disponibili;
- **tracciabile**: si deve poter risalire alla sorgente di ogni requisito;
- **verificabile**: la proprietà più importante.

### Verificabilità e quantificazione

Un requisito deve poter essere valutato in modo **booleano**: chiunque deve poter rispondere oggettivamente sì o no alla domanda "il sistema rispetta questo requisito?", senza che per lo sviluppatore la risposta sia sì e per il cliente no. Non si può dire "voglio un sistema veloce" o "scalabile": gli aggettivi qualitativi non bastano, servono **metriche quantitative** (throughput, tempo medio di risposta, FPS di riferimento, percentuali). "Il software deve girare a 30 fps su una macchina con una certa GPU" è un requisito; "il sistema deve essere veloce" è aria fritta. Un requisito non funzionale deve sempre essere espresso tramite una definizione quantitativa che porti a una valutazione oggettiva.

>[!example] Il cartello americano e i "demoni dell'ambiguità"
>Negli Stati Uniti i cartelli scolastici usano frasi in linguaggio naturale invece di pittogrammi: ad esempio un limite di velocità di 20 miglia orarie quando i bambini sono presenti. Tradurre quella frase in un algoritmo per un sistema di guida automatica apre un ventaglio di ambiguità: "presenti" in quale raggio? Basta rilevare un bambino a 300 metri in un campo? "Children" fino a che età? Il limite si applica solo nei giorni di scuola, a tutte le ore, anche a mezzanotte? Il cartello, interpretato col buon senso da un guidatore umano, diventa assurdamente complicato da mappare su un algoritmo deterministico e ripetibile. È l'esempio classico degli articoli sui "demoni dell'ambiguità" del linguaggio naturale: un enunciato che a buon senso sembra chiaro, espresso in linguaggio naturale, è un punto di partenza, non di arrivo.

#### Esempio: avviare/fermare un servizio remoto

Anche una richiesta apparentemente semplice ("un utente deve poter avviare o fermare un servizio su una macchina remota") genera subito domande: la macchina è locale o in cloud? Cosa succede se si invia *start* a un servizio già in esecuzione, o *stop* a uno già fermo (rifiutare, riavviare, notificare l'utente)? Cosa succede se il servizio si ferma all'improvviso, o se due utenti mandano segnali diversi in contemporanea, o se ci sono problemi di connessione? Il sistema deve partire all'avvio della macchina? Le situazioni limite sono le più rovinose: vanno esplorate a monte, non scoperte a valle.

## La gerarchia dei requisiti: business, user, system

Oltre alla coppia user/system, esiste un livello superiore: i **business requirements**, gli obiettivi dell'azienda committente. Esempio classico: uno studio dentistico vuole ridurre del 30%, l'anno successivo, gli appuntamenti mancati perché i pazienti se li dimenticano. Questo obiettivo di business si traduce in uno user requirement ("i pazienti devono ricevere un promemoria per gli appuntamenti in arrivo"), che a sua volta viene dettagliato in system requirements quantificati: il sistema deve mandare il reminder 24 ore prima, il 99% dei reminder deve partire entro 5 minuti dal momento schedulato (l'1% può uscire dalla finestra per effetto delle code di messaggi), e così via. Il rapporto tra i livelli non è uno-a-uno: un requisito di business ne alimenta tipicamente più di uno utente, e ogni requisito utente si espande in parecchi requisiti di sistema.

## Il processo di ingegneria dei requisiti

Il processo si articola in macro-fasi che si ripetono in **ciclo iterativo**:

1. **Elicitazione** (*requirement elicitation*, "raccolta/esplitazione dei requisiti*"): parlare con cliente e persone coinvolte per capire cosa vogliono.
2. **Analisi e specifica**: lavorare sul materiale raccolto per produrre i system requirements, validare che non ci siano contraddizioni.
3. **Validazione**: verificare costantemente che i requisiti non siano in contrasto tra loro. Intervistare dieci persone che non si contraddicano l'un l'altra è praticamente impossibile: il bravo requirement engineer va costantemente alla ricerca di contraddizioni e, quando ne trova una, torna dal cliente ("tu hai detto A, lui ha detto B: come facciamo?").

Il ciclo si ripete fino a convergenza: dopo n iterazioni si arriva al documento finale dei requisiti, con funzionali e non funzionali descritti a livello di sistema, firmato dal fornitore e dal cliente. Il punto cruciale è che è un processo **iterativo**, che coinvolge più volte il cliente, e a metà strada tra informatica e psicologia: serve empatia per tirare fuori dalla testa del cliente ciò che vuole davvero.

>[!info] Dipende dalla dimensione dell'azienda
>Il processo è di massima e dipende molto dalla dimensione dell'azienda: in una multinazionale come Microsoft possono esserci centinaia di ingegneri dei requisiti dedicati, con un background specialistico; in una software house di cinque persone il ruolo è ricoperto da chiunque. È un ruolo multidisciplinare, a cavallo tra informatica e psicologia.

## Stakeholder ed elicitazione

L'elicitazione parte dagli **stakeholder**: tutte le persone o i gruppi coinvolti, tipicamente gli end user del software, ma anche il management e, eventualmente, il technical staff. Persone con ruoli diversi hanno visioni molto diverse e spesso **contraddittorie**: per una nuova funzionalità di SegrePass, l'addetto alla segreteria chiederà di automatizzare il più possibile il proprio lavoro, mentre il suo capo che gestisce il budget vorrà automatizzare il meno possibile per spendere meno.

Il punto ancora più critico è che gli stakeholder spesso **non sanno cosa vogliono**, soprattutto quando si deve informatizzare un servizio del tutto nuovo: se la funzionalità non è mai esistita, nessuno ha esperienza di come dovrebbe funzionare, e se la dovesse inventare domattina TikTok o Instagram, anche loro se la dovrebbero inventare di sana pianta.

>[!example] Elicitazione simulata: gestione dei tirocini su SegrePass
>La funzionalità ipotizzata è la gestione informatica dei tirocini del corso di laurea, oggi gestita porta a porta dai docenti o via mail con le aziende. Tre studenti intervistati separatamente (interviste aperte, senza domande predefinite) hanno prodotto tre visioni divergenti: un catalogo di contatti e-mail con ricerca e filtro, con link ai siti delle aziende; una sezione con elenco di argomenti e conferma dell'attivazione; una vera e propria area personale nel piano di studi, visibile solo dopo il superamento degli esami del secondo anno, con elenchi di docenti disponibili per i tirocini interni e di aziende convenzionate per gli esterni, form di richiesta con dati anagrafici modificabili e caricamento del curriculum. Nessuno conosce a fondo il processo reale dei tirocini e ciascuno ha usato termini diversi per gli stessi concetti: riconciliare i punti di vista è compito dell'ingegnere. Il costo stimato delle tre alternative è molto diverso, e sono emerse anche contraddizioni verie e proprie: uno vuole la sezione tirocini sempre visibile (per informarsi in anticipo, col bottone di invio disabilitato finché non si hanno i requisiti), l'altro la vuole visibile solo al raggiungimento dei requisiti. In dieci minuti di interviste per una singola funzionalità, con tre stakeholder della stessa categoria, il risultato è già un puzzle di prospettive da ricucire: immaginate decine di funzionalità con categorie di utenti diverse.

### Interviste aperte e chiuse

Nell'**intervista aperta** lo stakeholder racconta liberamente, in brainstorming, tutto ciò che gli passa per la testa. Nell'**intervista chiusa** l'ingegnere arriva con un set predefinito di domande e ottiene risposte precise su ciascuna. Le interviste aperte fanno emergere anche ciò che non si era pensato di chiedere; le chiuse danno risposte confrontabili. I due approcci si combinano: dalle interviste aperte iniziali nascono le domande fisse da porre poi a tutti gli stakeholder.

### Dall'analisi alla decisione: il product owner

La fase di analisi trasforma le interviste in system requirements. Il testo raccolto è ancora troppo vago: dalle stesse descrizioni potrebbero uscire tre o quattro interfacce grafiche completamente diverse. Per questo durante l'analisi conviene abbozzare **mockup** (se si presenta al cliente un solo mockup, probabilmente lo rifiuta e ricama infinite modifiche; se gliene si presentano due alternative tra cui scegliere, lo si vincola a una decisione), affiancati a una descrizione testuale, e riconvocare gli stakeholder per riconciliare le versioni. Serve infine una persona che sappia decidere quando gli stakeholder non si accordano: una figura, tipicamente chiamata **product owner** (il "proprietario del prodotto"), dal potere reale di sciogliere i dubbi.