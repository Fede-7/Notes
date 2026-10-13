# Lezione 2 — Dal processo di elicitazione ai diagrammi dei casi d'uso

## Ripasso: requisiti e processo

Il software è un **sistema socioeconomico**: c'è una componente tecnica, ma dentro ci sono persone, e questo rende l'ingegneria dei requisiti qualcosa di più della sola tecnica. I requisiti si organizzano su tre livelli: i **business requirements** (l'obiettivo dell'azienda committente, ad esempio migliorare la velocità di un processo), che si traducono in **user requirements** (rapporto non uno-a-uno: un requisito di business ne alimenta tipicamente più d'uno), che a loro volta — ancora troppo astratti — si dettagliano in **system requirements**. Nel progetto del corso, tipicamente vengono forniti requisiti utente e ci si aspetta che gli studenti producano i requisiti di sistema.

Resta centrale il problema dell'**ambiguità** del linguaggio naturale: capire cosa un requisito sta davvero esprimendo. Un requisito può descrivere una funzionalità, una qualità desiderata, o un vincolo (anche tecnologico) sotto cui il sistema deve funzionare. Requisiti di qualità e vincoli prendono collettivamente il nome di **requisiti non funzionali**; le funzionalità sono i **requisiti funzionali**.

### Le proprietà dei requisiti

I requisiti devono essere **chiari** da comprendere (soprattutto per il cliente, che ragiona con noi nella fase iniziale), **non ambigui**, **completi** (devono coprire tutto ciò che c'è da fare), **consistenti** (nessun conflitto tra loro), **necessari** (solo ciò che serve davvero) e **tracciabili**. La tracciabilità ha un aspetto sottile: è importante capire **chi** ha espresso un requisito e perché, perché un requisito messo da una persona senza potere decisionale reale, o messo per guadagnare visibilità aziendale o per accedere a dati a cui non si dovrebbe accedere, può non servire; in fase di definizione dell'offerta economica, la sorgente aiuta a capire se un requisito costa e vale quanto serve.

[!def] Verificabilità
La proprietà più importante di tutte: chiunque deve poter rispondere in modo oggettivo sì o no alla domanda "il sistema soddisfa questo requisito?". Un requisito come "il software deve essere rapido, usabile, mantenibile" non è un requisito: è una chiacchiera totalmente inutile, e viene trattata come tale sia nel progetto sia allo scritto.

Per rendere un requisito verificabile, gli attributi di qualità vanno espressi sotto forma di **numeri**: "il software deve gestire 1000 transazioni concorrenti su questa tipologia di hardware" ammette una risposta sì/no univoca, a differenza di "deve essere veloce".

## Il processo di elicitazione

L'ingegneria dei requisiti comprende tre macro-fasi che si ripetono in ciclo: **analisi** (parlo col cliente e ottengo un accordo su ciò che inizio a strutturare), **specifica** (torno in azienda, dettaglio, costruisco modelli e formalizzo) e **validazione** (i dubbi emersi si risolvono col team o richiedono una nuova interazione col cliente). Si itera — raccolgo, classifico, organizzo, do priorità, costruisco il documento — finché non si arriva a un documento **stabile e completo**.

L'**iterazione implica il concetto di cambiamento**: nel momento in cui raccolgo informazioni, ci ragiono e riparlando con lo stakeholder può emergere "hai ragione, non era così, lo volevo fare in modo completamente diverso". Il cambiamento è parte costitutiva dell'elicitazione.

>[!warnings] Gli stakeholder non sanno cosa vogliono
>L'esperimento con tre studenti intervistati era un best case scenario: erano informatici, con una visione di massima del dominio. Con persone lontane dall'informatica, la qualità dei requisiti che emergono è ancora più bassa. E se neanche gli stakeholder sanno cosa vogliono, non ci si può fermare alla prima versione raccolta.

### Approcci di sviluppo: a strati o a fette

Data la sequenza di passi dello sviluppo software (requisiti → progettazione → implementazione → testing → rilascio), esistono due modi macroscopicamente diversi di percorrerla:

- **per strati** (modello a cascata): tutta l'analisi, tutta la progettazione, tutta l'implementazione, tutto il testing, e infine il rilascio dell'intero sistema;
- **a fette**, per funzionalità (approccio agile): oggi progetto, implemento, testo e rilascio la fetta "prenotazione", domani la fetta "pagamento", e così via.

Entrambi gli approcci sono **correttissimi**: non esiste quello giusto e quello sbagliato, dipende dalla tipologia di software e da cosa vuole il cliente (se vuole subito qualcosa di funzionante, si procede a fette). Ma ragionare per singola funzionalità, dove ogni rilascio aggiunge una funzionalità, crea un **problema architetturale**: il codice deve essere modulare, pensato con pattern architetturali adeguati, e soprattutto chi progetta ha **informazioni limitate**, progetta un ottimo locale senza visione dell'insieme; se dopo sei mesi salta fuori che il sistema deve funzionare anche su smartwatch, l'architettura può bloccarsi completamente. Chi procede a strati progetta invece avendo la visione totale di tutto ciò che va fatto. I due modelli (a cascata e agile) saranno visti in dettaglio a fine corso.

### Priorità dei requisiti

Il ragionamento a fette ha una conseguenza fondamentale: se rilascio una funzionalità alla volta, la prima che consegno è quella che il cliente ritiene più urgente. I requisiti non sono quindi una lista piatta, ma una **lista ordinata per priorità**: il cliente deve definire un **ranking** che dichiari quali funzionalità sono cruciali. Per un e-commerce come Amazon, la priorità suprema è permettere al cliente di finalizzare l'acquisto (è lì che si guadagna); recensioni, stelline, AI che riassume le recensioni, bonus e sconti possono arrivare in un secondo, terzo, quarto momento.

Conoscere il ranking permette anche scelte più informate sulla **qualità**: la "coperta corta" impone di non poter ottimizzare tutte le qualità; capire le funzionalità prioritarie aiuta a capire quali fattori del software devono avere qualità maggiore.

### Interviste

Le interviste — già viste come supporto all'elicitazione — possono essere **chiuse** (lo stakeholder risponde a un set predefinito di domande) o **aperte** (si parla a ruota libera). Le chiuse garantiscono che tutti rispondano sugli stessi fattori, ma **precludono opzioni**: se chi fa le domande non pensa alla cosa giusta, quell'informazione non emergerà mai. Le aperte sono un brainstorming in cui lo stakeholder racconta ciò che gli passa per la testa, con granularità molto variabile da persona a persona. Si combinano: prima interviste aperte, poi la riflessione e specificazione genera l'insieme di domande fisse da porre a tutti.

In pratica gli stakeholder sono **poco disponibili**: persone impegnate nel loro lavoro, per cui le interviste sono tempo sottratto; va minimizzato e ottimizzato il loro impegno, e ci sono aspetti psicologici da tenere in considerazione.

>[!info] La terminologia del dominio
>Ogni organizzazione ha un proprio insieme di termini ignoti al di fuori del suo dominio, e il cliente dà per scontato che chiunque li conosca. Esempio raccontato di un tirocinio all'ufficio finanza di un Comune: "l'operatore invia la lettura per un dato anno e contribuente, inserisce la lettura in una maschera che calcola l'imponibile, stampa le ingiunzioni di pagamento; notificata l'ingiunzione, ci sono 60 giorni per pagare; se non paga, si procede all'iscrizione a ruolo coattivo inserendo i dati in una maschera che genera il tracciato 290". Un esempio simile da un progetto di gestione di un cinema: il cuore del sistema non era la biglietteria, ma la stampa del **borderò**, il documento da consegnare alla SIAE. L'informatica, da questo punto di vista, è un mestiere curioso: si è costantemente esposti a problemi di cui non si sa nulla, e a forza di iterazioni se ne impara il dominio. Serve in genere tempo (un mese, nel caso dell'esempio comunale) per trasformare quel racconto in una specifica.

### Studi etnografici

Alternativa (o complemento) alle interviste: l'**osservazione**. L'ingegnere si mette accanto a chi lavora (es. in segreteria), guarda come lavora, e da questo capisce come il sistema può inserirsi in un ecosistema sociale e organizzativo più ampio. Osservare come viene oggi gestito un nuovo contribuente con file Excel serve a bypassare il racconto dello stakeholder e capire direttamente il processo.

>[!warnings] Il rischio della mera trasposizione
>Lo studio etnografico rischia di produrre una mera trasposizione digitale di un processo cartaceo. La digitalizzazione è invece un'occasione di efficientamento: si può fare la mera parità (stessi campi, in una schermata con qualche controllo), oppure si possono derivare alcuni campi da dati già noti (far inserire solo due campi invece di quattro) ottimizzando il tempo di lavoro. Attenzione però: se il software non è nostro, chi lo aggiorna sei lo sviluppatore, e trovare un modo più efficiente dello stesso lavoro può essere compito nostro.

## Personas

Strumento chiave della raccolta dei requisiti: provare a formalizzare **chi userà il software**, non come persona reale ma come **categoria di utente**. Definire le categorie fa emergere punti di vista e prospettive utili, e si costruisce come un gioco di ruolo con gli stakeholder: "immaginiamo che arrivi lo studente di informatica a chiedere un'informazione: qual è lo stereotipo?".

Le personas **non sono persone reali**: sono una rappresentazione di una classe di persone reali, con nome, età, foto e dettagli immaginari. Non sono nemmeno figure che fanno cose diverse: dentro la categoria "studente" convivono lo smanettone, chi non ne capisce niente, chi ha disabilità visive. L'idea di fondo è che **immedesimandosi in ciascuna classe di utenti** si ragiona meglio sulle aspettative dell'interfaccia. Non c'è uno standard: si scelgono nome, foto, background per rendere viva la rappresentazione.

Esempi: per il sistema della segreteria, lo studente di informatica (bravo con i sistemi, aggiornato, contento di usare la tecnologia) versus lo studente umanistico (computer vecchio, risoluzione piccola, Windows XP, browser di dieci anni fa): classe di utenti di cui tener conto nel progetto. Per TikTok la fascia tipica è dai 10 ai 30 anni, con ulteriori sotto-categorie (smanettoni e non); per Amazon diventa importante l'utente anziano con problemi di vista, che potrebbe non vedere il font piccolo — considerazione che può **modificare i requisiti** o generare una domanda agli stakeholder per quella categoria.

>[!info] Quando le personas sono essenziali
>Sono utilissime per i software general-purpose, dove non ci sono stakeholder reali da intervistare: per progettare la nuova versione di Office devo immaginare chi lo può usare — la nonnina di 80 anni che scrive la ricetta della torta, i bambini che fanno le scritte colorate con Word. Le personas sono un punto di partenza della raccolta dei requisiti perché permettono di ragionare, soprattutto in fase di mockup, in modo informato: non faccio il mockup "a volo", lo faccio per la persona di un certo tipo.

Le dimensioni contano: in un team di tre persone tutto si fa insieme; il requirement engineering è a cavallo tra informatica, psicologia e sociologia, e serve capire il profilo sociologico degli utenti. In aziende grandi i team di requirement engineering sono multidisciplinari, con psicologi inclusi.

### Storie utente

Nelle interviste si chiede allo stakeholder di **raccontare una storia**: "come vorresti interagire col sistema?". Uno stakeholder difficilmente produce una specifica formale ("premo questo bottone, il sistema mostra questa schermata"), ma può narrare il flusso come una storiella: "arrivo in ufficio la mattina, accendo il computer, mi loggo, inserisco queste informazioni, vorrei vedere questo...". Le **storie** sono un modo narrativo di organizzare le interviste e ciò che ne esce, descrivendo l'interazione per una particolare funzionalità. Domande circostanziali ("raccontami come faresti domattina la virtualizzazione di un esame con uno studente con un'esigenza particolare") producono risposte narrative.

## Mockup e wireframing

Il **mockup** è uno strumento eccezionale per togliere ambiguità: parlo e, soprattutto, faccio vedere — un'immagine vale più delle parole. Devono però essere quanto più **semplici** possibile: si parla di **wireframe** (in inglese, "filo di ferro"): solo il bordo, **niente colori**. Non si deve portare la discussione sulla componente estetica; l'unica finalità del mockup è capire **quali schermate servono** e, per ogni schermata, **quali informazioni mostrare o ricevere** dall'utente, strutturando il flusso senza pensare all'estetica.

Il mockup è uno strumento che chiunque conosce: lo si mette davanti al cliente ("guarda, vorresti il software fatto così?") e riduce enormemente l'ambiguità, aiuta a far emergere nuovi requisiti e genera engagement negli stakeholder.

### Strumenti per realizzarli

Tre strumenti principali:

- **Figma**: lo strumento top, usato dalle aziende con più budget; non è un giocattolo didattico. Acquisita da Adobe, ha un piano gratuito con mail istituzionale studentesca. Permette di rendere i mockup **interattivi**: premo un bottone e mi si apre un'altra schermata, simulando la sequenza di funzionamento del sistema — impatto totale diverso davanti al cliente. Alcuni strumenti realizzano l'interattività tramite PDF che cambiano pagina, altri con vere applicazioni web; con l'aggiunta di step si arriva quasi a un prototipo di applicazione.
- **Balsamiq**: il più noto in assoluto per i mockup, con piano gratuito a 30 giorni.
- **Penpot**: gratuito, utilizzabile.

L'interfaccia è un ambiente di disegno libero con librerie aggiuntive (es. wireframing) che offrono palette di controlli standard (bottoni, icone, text field, checkbox, form, switch, header, menù); si scelgono dimensioni predefinite (smartphone, tablet, pagina web, TV, formati per social) e si disegnano le schermate componendo gli oggetti. Le risorse per imparare abbondano sul web.

>[!info] Tecnologia libera
>Nel corso non viene mai imposta una tecnologia: viene dato un problema e trovare la soluzione è parte del lavoro — come nello scenario reale in cui un cliente arriva con un problema e il fornitore propone una soluzione. I tre strumenti sono suggeriti, ma anche sceglierne un altro va bene; per il progetto si vuole un mockup fatto con strumenti professionali (almeno due sono gratuiti per studenti), non disegnato a mano.

## UML e diagrammi

La specifica dei requisiti parte tipicamente da un diagramma **UML**. UML è un **contenitore** di circa una ventina di tipi di diagrammi, ognuno dei quali descrive un aspetto diverso del sistema; ne vedremo almeno quattro, i fondamentali: **class diagram** (già noto), **sequence diagram**, **activity diagram** e **use case diagram**.

Lo scopo di UML è **comunicare**: pensare e parlare col collega facendo uno sketch dà un boost immenso di produttività rispetto al solo parlare. Il class diagram descrive la **struttura statica** (quali classi esistono e come sono collegate): è un'astrazione — mostrare tre classi collegate fa capire in un secondo ciò che in 6000 righe di codice richiederebbe una settimana. Ma è statico: non dice quando parte il `main`, chi chiama chi; per vedere il flusso di chiamate tra classi serve il sequence diagram ("chiamo questo metodo, mi restituisce un valore, lo passo a quell'altra classe...").

## Use case diagram

Il **diagramma dei casi d'uso** ha una sola finalità: **trasmettere a colpo d'occhio quali funzionalità offre il sistema, per ogni tipologia di utente**. Quanto più lo si tiene semplice, tanto più è comunicativo; nel documento dei requisiti fa da indice: "questo software mi permette di fare quattro funzionalità, tre per una tipologia di utente e una per un'altra", e i mockup racconteranno poi come funzionano.

Caratteristiche fondamentali: il diagramma **non definisce come il sistema è implementato** — il sistema è una **black box** — dà solo l'elenco delle funzionalità.

### Attori

L'omino stilizzato (**stickman**) è l'**attore**: una categoria di utente. Ogni attore ha un nome **unico** nel diagramma (due attori con lo stesso nome ma significato diverso non sono ammessi).

>[!info] Attori e personas
>Le personas servono a ragionare su interfaccia e dettagli; più personas possono fare le stesse cose e quindi essere rappresentate dallo **stesso attore**. Un certo numero di personas può convergere in un attore: "studente smanettone" e "studente umanistico", su SegrePass, fanno le stesse cose — sono entrambi l'attore *studente*. L'attore è la classe di utenti; la persona è il raffinamento che serve a ragionare sull'interfaccia.

Un attore non è necessariamente umano: può essere un **altro sistema**, un sensore fisico o un elemento fisico che fa partire una funzionalità (una sveglia che scatta all'ora impostata è un attore).

### Casi d'uso e scenari

I casi d'uso sono rappresentati come **ellissi** collegate con linee all'attore. Dentro l'ellisse si scrive una funzionalità: un caso d'uso esprime **esclusivamente requisiti funzionali** — qui non c'è modo di dire "deve gestire 1000 transazioni". La funzionalità va espressa con **un verbo e un complemento**, così che risulti una frase di senso compiuto ("visualizza prenotazioni", "paga tasse").

>[!def] Scenario di esecuzione
>Le varie declinazioni — i vari flussi che una funzionalità può prendere, positivi e negativi — si chiamano scenari di esecuzione: "pago le tasse e va tutto bene", "pago e non ho abbastanza soldi sulla carta", "pago e il server esterno non risponde". Il caso d'uso rappresenta una **macrofunzionalità** in tutte le sue derivazioni; gli scenari si raccontano poi a parte. Lo scenario che va bene si chiama **main scenario** (o scenario di successo).

#### Il box di sistema

Si può racchiudere il sistema da sviluppare in un **box**: dentro va tutto ciò che va aggiunto al sistema in corso di sviluppo. Le linee collegano ogni attore alle funzionalità che può usare. Funzionalità come "paga tasse" possono coinvolgere un **attore esterno** (es. il sistema PagoPA) verso cui il nostro sistema si appoggia e da cui riceve risposta.

### Generalizzazione tra attori: esempio e-commerce

Provando a elencare i casi d'uso di un banale sito di e-commerce emergono le complicazioni: "login" non sembra un vero caso d'uso (cosa fa? autentica: è un **mezzo** per accedere ad azioni riservate, non un fine); "visualizza prodotti" è invece un caso d'uso valido, e per certi versi "carica prodotti" del gestore è ad esso collegabile. Ragionando sul login si scopre che esistono (almeno) **due classi di utenti**: l'utente normale e il gestore, che può fare tutto ciò che fa l'utente normale più qualcosa in più. Se tutti e due possono "visualizza prodotti", questo caso d'uso è utilizzabile da due classi di utenti.

Questa è una **specializzazione**: il gestore può fare tutto ciò che fa l'utente e qualcosa in più, esattamente come nell'ereditarietà dei linguaggi di programmazione. In UML la relazione si rappresenta con il **triangolino** su una linea tratteggiata (generalizzazione/specializzazione), così che il gestore erediti anche i casi d'uso collegati all'utente senza ridisegnarli con linee che intasano il diagramma. La si introduce **per semplificare**: la finalità resta comunicare a colpo d'occhio chi può fare cosa. Se un diagramma diventa troppo affollato (es. decine di attori e casi d'uso per un progetto tipo Amazon), si può **spezzare su più pagine**: un diagramma per gli utenti e uno affiancato per l'operatore back-office.

### Funzionalità o passo? L'euristica del beneficio

Come capire se qualcosa è un caso d'uso autonomo o solo un passo verso una funzionalità più ampia? "Aggiungi prodotto al carrello" è un caso d'uso o un mezzo? L'**euristica** è porsi la domanda *perché*: qual è la conseguenza, il beneficio per l'attore? "Effettua acquisto" ha un chiaro beneficio per l'utente (è un vero user requirement: "voglio fare un acquisto"); "aggiungi prodotto al carrello" lo si fa sempre in funzione di qualcos'altro (equivalente a una wishlist), e difficilmente esiste uno user requirement "voglio aggiungere prodotti al carrello" che non sia finalizzato all'acquisto. Lo stesso vale per "salva carta di credito" durante l'acquisto: sono **passi** — magari con tanto coding e più schermate — verso la funzionalità vera, che invece ha dignità di user requirement. La difficoltà principale del disegno dei casi d'uso è distinguere i mezzi dai fini: la linea guida è ragionare su quale sia la finalità finale per l'utente.