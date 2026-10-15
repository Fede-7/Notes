# Lezione 4-5 Requirements Engineering — Elicitation e Analysis

## Il posto della RE nel ciclo di vita

La Requirements Engineering è la prima fase del modello a cascata: i requisiti si raccolgono tramite interviste con stakeholder, personas e storie/scenari, e si specificano con use case, linguaggio naturale e modelli di dominio. L'output alimenterà il system design.

## I requisiti software

> [!def] Requisito
> **Descrizione** di ciò che il sistema dovrebbe fare: i servizi che il sistema deve fornire ai suoi utenti e i vincoli operativi.

Esempi tipici: permettere di cercare corsi per parola chiave o iscriversi a corsi, implementare le interfacce come app native Android e iOS, gestire almeno 10k utenti concorrenti, autenticare anche con sensori di impronta digitali.

> [!quote] Fred P. Brooks
> «The hardest single part of building a software system is deciding precisely what to build. No other part of the conceptual work is so difficult as establishing the detailed technical requirements [...]. No other part of the work so cripples the resulting system if done wrong. No other part is more difficult to rectify later.»

## Livelli di requisiti

Il termine "requisito" è usato in modo incoerente nell'industria del software: a volte indica una descrizione astratta, a volte una definizione formale e dettagliata.

> [!def] User requirements
> **Descrizione** astratta e di alto livello di un servizio che il sistema deve fornire o di un vincolo sul sistema, nella prospettiva degli utenti finali.

Lo stesso bisogno, visto dalla parte del sistema, diventa una definizione formale.

> [!def] System requirements
> **Definizione** più dettagliata e formale di una funzione di sistema, nella prospettiva del sistema da costruire.

Il rapporto tra i livelli è di progressivo dettaglio: come user requirement "il sistema deve generare un report mensile delle iscrizioni ai corsi" si espande in system requirements che specificano il giorno di generazione, il contenuto per ogni corso e la restrizione dell'accesso ai soli course manager.

### Ruolo contrattuale

L'ambiguità tra i livelli è inevitabile perché i requisiti servono a una doppia funzione.

- **User requirements**: possono essere la base di un'offerta per un contratto; il cliente definisce requisiti generali e contraenti diversi propongono modi diversi di soddisfarli.
- **System requirements**: possono essere la base del contratto stesso; una volta aggiudicata la commessa, l'appaltatore formula una serie dettagliata di system requirements perché il cliente capisca esattamente cosa farà il software e possa validare la proposta; una volta accettati e validati, entrano nel contratto finale e sono vincolanti.

Il costo relativo di correzione di un errore cresce lungo il ciclo di vita del progetto, quindi un errore nei requisiti è il più costoso da rettificare.

![[f019e3ec0a3179b28c6cdf75801b74a073f1e203722d861d4ae6d79eeba49c33.png|400]]

> [!def] Requirements Engineering
> **Sotto-area** dell'ingegneria del software che si occupa del processo di definizione dei requisiti di un software da sviluppare; fornisce a ingegneri del software metodi, tecniche e strumenti per capire e documentare cosa un sistema deve fare.

## Requisiti funzionali e non funzionali

I requisiti sono spesso classificati in due grandi famiglie.

> [!def] Requisiti funzionali
> **Servizi** che il sistema deve fornire, e come il sistema deve reagire a particolari input o comportarsi in determinate situazioni.

I primi descrivono i servizi, i secondi i vincoli su quei servizi.

> [!def] Requisiti non funzionali
> **Vincoli** sui servizi o sulle funzioni offerte dal sistema: includono vincoli temporali, di processo o imposti da standard; spesso si applicano all'intero sistema più che a singole feature o servizi.

In pratica la distinzione non è netta: un requisito apparentemente non funzionale, sviluppato in maggiore dettaglio, genera requisiti chiaramente funzionali ("solo utenti autorizzati possono accedere" → login e autenticazione). I requisiti non sono indipendenti: uno spesso genera o vincola altri requisiti.

Espressi come requisiti utente, i requisiti funzionali si scrivono in linguaggio naturale per essere capiti da non tecnici (utenti, manager); come system requirements vanno dettagliati con accuratezza, descrivendo input, output ed eccezioni, così che gli ingegneri sappiano esattamente cosa implementare.

### Criticità dei requisiti non funzionali

I requisiti non funzionali non riguardano servizi specifici: specificano o vincolano caratteristiche del sistema nel suo insieme, come implementarlo (es. usare il linguaggio Java) o altre proprietà (tempi di risposta, uso di memoria).

> [!warning] Criticità
> Gli utenti possono trovare un modo per aggirare un'implementazione sub-ottimale di un requisito funzionale, ma non rispettare un requisito non funzionale può rendere il sistema inutilizzabile: un sistema non conforme al GDPR non può essere distribuito in Europa.

Per questo i requisiti non funzionali sono spesso più critici di quelli funzionali.

### Tipi di requisiti non funzionali

I requisiti non funzionali possono derivare da tre fonti.

- **Product requirements**: caratteristiche richieste del prodotto (quanto deve essere veloce, quanta memoria richiedere, requisiti di usabilità, tassi di fallimento accettabili).
- **Organizational requirements**: organizzazioni del cliente e degli sviluppatori (processi operativi che descrivono come il sistema sarà usato, linguaggi di programmazione richiesti, requisiti sull'ambiente operativo).
- **External requirements**: fonti esterne (cosa serve per l'approvazione di un regulator di terze parti, requisiti legali, requisiti etici perché il sistema sia accettabile per utenti e pubblico).

### Requisiti di dominio

> [!def] Requisiti di dominio
> **Requisiti** derivanti dallo scopo particolare o dal contesto industriale in cui un software è usato; possono essere funzionali o non funzionali.

Un esempio: il software di controllo di un dispositivo medico deve garantire la sicurezza secondo lo standard IEC 60601-1 (Medical Electrical Equipment). Il requisito vincola sia il design del sistema sia il processo di sviluppo: un software perfettamente funzionale ma non sviluppato secondo lo standard non sarebbe utilizzabile in pratica.

## Proprietà dei buoni requisiti

Un buon requisito dovrebbe avere le seguenti proprietà.

- **Chiaro e facile da capire**: in particolare per gli user requirements.
- **Non ambiguo**: l'ambiguità porta a dispute con i clienti.
- **Completo**.
- **Consistente**: non deve entrare in conflitto con altri requisiti.
- **Testabile**: deve essere possibile determinare senza ambiguità se il sistema lo soddisfa; la mancanza di testabilità porta a dispute con i clienti.

### I demoni dell'ambiguità

Un requisito apparentemente chiaro nasconde spesso interpretazioni multiple. Due tecniche per far emergere le aree sfumate:

- **Dissezionare la descrizione**: le parole sono aperte a interpretazioni diverse (un'espressione innocua può ammettere più letture molto diverse tra loro).
- **Poke at the borders**: i termini mappano imperfettamente l'uno sull'altro, quindi occorre trovare le aree sfumate (come si controlla che un servizio remoto sia in esecuzione? Si legge un flag? Il flag può essere impostato anche a servizio non attivo?).

### Requisiti e testabilità

Se non è possibile determinare senza ambiguità se il sistema soddisfa un requisito, gli sviluppatori possono ritenerlo soddisfatto mentre il cliente non è affatto d'accordo. Per questo:

- i **system functional requirements** devono essere il più dettagliati possibile e non lasciare spazio a interpretazioni;
- i **system non-functional requirements** devono includere indicatori quantitativi quando possibile.

Non testabili: "il sistema deve essere affidabile", "facile da usare", "veloce e reattivo". Le stesse esigenze in forma testabile:

- **Uptime**: disponibilità mensile del 99,9%.
- **Facilità d'uso**: tutte le funzioni usabili dopo al massimo due ore di training, con non più di due errori utente in media per ora d'uso.
- **Reattività**: tempo medio di risposta non superiore a 100 ms.

### Metriche per requisiti non funzionali

Alle proprietà tipiche si associano metriche quantitative.

| Proprietà | Metriche |
| --- | --- |
| Performance | Operazioni elaborate al secondo, tempo di risposta a utenti/eventi, frequenza di refresh dello schermo |
| Size | Megabyte |
| Ease of use | Tempo di training richiesto, tasso di errori utente, numero di richieste di supporto |
| Reliability | Tempo al guasto, tasso di disponibilità (uptime) |
| Robustness | Tempo di ripristino dopo un guasto, probabilità di perdita dati in caso di guasto |

## Il processo di Requirements Engineering

Il processo ha tre attività chiave.

1. **Elicitation e analisi**: scoprire i requisiti interagendo con gli stakeholder.
2. **Specification**: convertire i requisiti in una forma standardizzata.
3. **Validation**: controllare che i requisiti definiscano davvero il sistema che il cliente vuole.

In pratica il processo non è lineare: le attività sono intrecciate in un processo **iterativo** a diversi livelli di granularità.

- Prima iterazione: **requisiti di business** (perché serve il progetto? chi ne beneficia? quando e dove avrà luogo?).
- Poi: **user requirements**.
- Infine: **system requirements**.

Ogni iterazione include fasi di elicitation e analisi, specification e validation; le iterazioni si appoggiano su feasibility study, prototyping e review.

## Elicitation e analisi dei requisiti

L'obiettivo è scoprire cosa i clienti vogliono e di cui hanno bisogno: più facile a dirsi che a farsi. L'elicitation è considerata la parte più critica della RE perché coinvolge la collaborazione tra stakeholder diversi.

> [!def] Stakeholder
> **Persone** o gruppi affetti in qualche modo da un progetto di sviluppo software: utenti finali (anche un gruppo eterogeneo, ad es. vendita, logistica e customer care per un order management system), chi usa gli output del software, management ed executive del cliente, staff tecnico del cliente che opera il sistema quotidianamente.

### Sfide dell'elicitation

Gli stakeholder pongono sfide peculiari al processo.

- Non sanno cosa vogliono dal software se non nei termini più generali, non sanno cosa è fattibile e possono fare richieste irrealistiche.
- Sono esperti del proprio dominio: esprimono i requisiti nel proprio gergo, con conoscenza implicita del loro lavoro, dando per scontati dettagli che non lo sono.
- Stakeholder diversi esprimono requisiti diversi in modi diversi: l'ingegnere dei requisiti deve districare comunanze e conflitti.
- Fattori politici possono influenzare il processo: manager possono chiedere requisiti che accrescano la loro influenza nell'organizzazione.
- Hanno visioni diverse (e a volte in conflitto) su importanza e priorità dei requisiti; chi si sente ignorato può cercare deliberatamente di minare il processo.
- I requisiti cambiano durante l'elicitation: nuovi requisiti emergono da stakeholder non inizialmente considerati.

### Il processo di elicitation e analisi

Il processo si articola in quattro passi.

1. **Discovery e understanding**: interagire con gli stakeholder per scoprire i requisiti.
2. **Classificazione e organizzazione**: i requisiti correlati vengono raggruppati e organizzati.
3. **Prioritizzazione e negoziazione**: risolvere i conflitti derivanti da bisogni contrastanti di stakeholder diversi.
4. **Documentazione**: tenere traccia dei requisiti scoperti per l'iterazione successiva del processo.

## Tecniche di elicitation

Approcci diversi possono essere usati e combinati per scoprire i requisiti: interviste con stakeholder, osservazione ed etnografia, personas, storie e scenari, mock-up e prototipi.

### Interviste con gli stakeholder

Le interviste formali o informali sono fondamentali in RE: il team chiede agli stakeholder del loro lavoro, del sistema attualmente usato e del sistema da sviluppare; i requisiti derivano dalle risposte.

- **Closed**: lo stakeholder risponde a una lista di domande predefinite.
- **Open**: non c'è un'agenda predefinita.
- In pratica si combinano: le interviste completamente aperte raramente funzionano bene; meglio partire da domande definite in anticipo, che portano ad altri temi discussi in modo meno strutturato.

Le persone parlano volentieri del proprio lavoro, ma il loro tempo va rispettato minimizzando l'impatto delle interviste. Sfide tipiche:

- gli stakeholder usano gergo e danno per scontati alcuni requisiti;
- conoscono il proprio lavoro ma possono avere una visione parziale o distorta di quello dei colleghi di altre aree o dipartimenti;
- possono essere riluttanti a discutere requisiti e vincoli organizzativi per sottili dinamiche di potere nell'organizzazione.

### Etnografia

> [!def] Etnografia
> **Tecnica** osservativa per capire i processi operativi: l'ingegnere dei requisiti si immerge nell'ambiente di lavoro degli utenti finali, dove il sistema sarà usato, osservando il lavoro quotidiano e annotando i task effettivi e i partecipanti coinvolti.

Il software raramente esiste in isolamento: è usato in un ambiente sociale e organizzativo che genera o vincola i requisiti; spesso i processi realmente usati in un'organizzazione differiscono da quelli formali che dovrebbero essere usati. L'etnografia è particolarmente efficace per scoprire:

- requisiti derivanti da come le persone lavorano realmente, non da come le definizioni dei processi dicono che dovrebbero lavorare;
- requisiti derivanti dalla cooperazione e dalla consapevolezza delle attività altrui (es. prima di inviare un sondaggio, un dipendente verifica con i colleghi che l'ordine sia stato consegnato).

### Personas

Conoscere gli utenti è importante per scoprire i requisiti e, in seguito, per progettare interfacce efficaci. A volte gli utenti sono noti (es. strumenti per altri ingegneri del software), ma in generale il software è sviluppato per altre persone con bisogni diversi: gli utenti reali sono diversi da chi sviluppa, e l'esperienza personale non fornisce un quadro completo.

> [!def] Persona
> **Archetipo** ipotetico di utenti reali: non è una persona reale, ma la rappresenta; sebbene immaginaria, è definita con rigore e precisione e viene scoperta come sottoprodotto del processo di elicitation, non inventata di sana pianta.

Non esiste un modo standard per rappresentarla; gli elementi comunemente usati sono i seguenti.

- **Personalizzazione**: nome, età, breve biografia.
- **Informazioni lavorative**: qual è il lavoro dell'individuo.
- **Educazione**: dettagli di formazione ed esperienza.
- **Goals**: qual è il suo interesse nel software.
- **Frustrazioni/pain point**: difficoltà che il software può contribuire a risolvere.

Le personas sono uno strumento per acquisire una comprensione completa degli utenti e promuovere l'empatia. Sono particolarmente utili quando non ci sono stakeholder specifici da intervistare: sviluppo di software off-the-shelf per il pubblico generale, o software custom i cui end-user sono il pubblico. Dall'analisi di una persona possono emergere requisiti nuovi non scoperti con le interviste.

### Storie

> [!def] Storia
> **Descrizione** di come il sistema può essere usato per un particolare task: cosa fa l'utente, quali informazioni usa, di quale output ha bisogno.

Le storie si scrivono come testo narrativo e presentano una descrizione di alto livello dell'uso del sistema.

- È più facile relazionarsi a esempi di vita reale che ad astrazioni.
- Gli stakeholder non sono bravi a enunciare requisiti di sistema, ma descrivono efficacemente come fanno le cose o come le vorrebbero fare con un nuovo modo di lavorare.
- Sono efficaci nel presentare goal di "quadro generale" a cui è facile relazionarsi.

### Mockup a bassa fedeltà

> [!def] Low-fidelity mockup (wireframe)
> **Schizzo** semplificato delle interfacce utente del sistema: modo rapido ed economico per visualizzare struttura e flussi di base; l'attenzione è su funzionalità e flusso, non sull'estetica.

I mockup a bassa fedeltà portano benefici concreti al processo.

- **Facilitano la comprensione**: aiutano gli stakeholder a afferrare la funzionalità di base e sono un punto di partenza per la discussione.
- **Aiutano a scoprire nuovi requisiti**: è più facile ragionare su interfacce concrete che su affermazioni astratte.
- **Engagement e feedback iterativo**: promuovono il coinvolgimento degli stakeholder e permettono iterazione e feedback rapidi senza investimenti significativi nel design.
- **Fondazione per lo sviluppo**: base solida per evolvere verso design a fedeltà maggiore e per lo sviluppo finale.

Strumenti possibili: carta e matita per gli schizzi iniziali; strumenti digitali commerciali come Balsamiq o Figma; alternative open-source come mydraft.cc, draw.io e Pencil Project.