# Lezione 04-05 Requirements Engineering — Specification e Validation

## Specificazione dei requisiti

> [!def] Specificazione dei requisiti
> **Processo** di scrittura degli user e system requirements in un documento dei requisiti.

- Gli **user requirements** devono essere comprensibili a utenti finali e clienti senza background tecnico.
- I **system requirements** sono più dettagliati e possono includere informazioni tecniche.
- I requisiti possono far parte di un contratto per lo sviluppo del sistema: è quindi importante che siano completi e dettagliati il più possibile.

### Requisiti e design

In linea di principio i requisiti dicono **cosa** il sistema deve fare e il design descrive **come** lo fa; in pratica requisiti e design sono inseparabili.

- I requisiti possono essere strutturati e organizzati sulla base di un'architettura di sistema ad alto livello.
- Il sistema può interoperare con altri sistemi che generano requisiti di design.
- L'uso di un'architettura specifica per soddisfare requisiti non funzionali può essere un requisito di dominio.

## Approcci di specificazione

Sono possibili approcci diversi, con formalità crescente.

- **Linguaggio naturale**: requisiti come frasi numerate, una frase per requisito; espressivo, intuitivo e universale, comprensibile a utenti e clienti, può esprimere requisiti funzionali e non.
- **Linguaggio naturale strutturato**: uso di un form o template standardizzato.
- **Notazioni semi-formali e modelli**: UML use case diagram e altri modelli di dominio, tipicamente integrati da annotazioni in linguaggio naturale.
- **Formal specification**: notazioni basate su concetti matematici come macchine a stati (finite e infinite) e logiche temporali.

Approcci diversi si usano in domini diversi: nei sistemi safety-critical è comune usare specifiche formali e linguaggio naturale strutturato; in un'applicazione piccola si può usare linguaggio naturale non strutturato; nei sistemi informativi di media-grande taglia le notazioni semi-formali sono un buon compromesso.

## Linee guida per la specifica in linguaggio naturale

Il linguaggio naturale rende difficile la precisione, quindi servono linee guida di scrittura.

- Definire un formato "standard" e usarlo per tutti i requisiti (es. `shall`).
- Usare il linguaggio in modo consistente: `shall` per i requisiti obbligatori, `should` per quelli desiderabili.
- Usare l'evidenziazione del testo per identificare le parti chiave del requisito.
- Evitare il gergo informatico.
- Includere una spiegazione (**rationale**) del perché un requisito è necessario.

### Problemi del linguaggio naturale

La specifica in linguaggio naturale soffre di tre problemi tipici.

- **Lack of clarity**: la precisione è difficile senza rendere il documento difficile da leggere.
- **Requirements confusion**: i requisiti funzionali e non funzionali tendono a mescolarsi.
- **Requirements amalgamation**: requisiti diversi possono essere espressi insieme nella stessa frase.

## Specificazioni strutturate

> [!def] Specificazione strutturata
> **Approccio** in cui la libertà del redattore dei requisiti è limitata e un modo standardizzato di scriverli è imposto; funziona bene per certi tipi di requisiti (es. sistemi embedded di controllo) ma a volte è troppo rigida per i requisiti di sistemi aziendali.

Esempio classico di form strutturato (software di controllo di una pompa insulinica, requisito 3.3.2 del SRS).

| Campo | Contenuto |
| --- | --- |
| Funzione | Calcolo della dose di insulina: livello di zucchero sicuro |
| Descrizione | Calcola la dose di insulina da erogare quando il livello di zucchero misurato è tra 3 e 7 unità |
| Input | Lettura corrente `r_2`, le due letture precedenti `r_0` e `r_1` |
| Sorgente | Lettura corrente dal sensore; le altre letture dalla memoria |
| Output | `CompDose`: la dose di insulina da erogare |
| Azione | `CompDose` è zero se il livello è stabile o in calo, o se cresce con ritmo in diminuzione; se livello e ritmo crescono, si calcola la differenza tra livello attuale e precedente divisa per 4, arrotondata; se il risultato è zero, si imposta la dose minima erogabile |
| Richieste | Le due letture precedenti, per calcolare il tasso di variazione del livello di zucchero |
| Precondizione | Il serbatoio di insulina contiene almeno la dose singola massima consentita |
| Postcondizione | In memoria `r_0` è sostituito da `r_1`, poi `r_1` da `r_2` |
| Effetti collaterali | Nessuno |

## Use case diagram

I **use case** descrivono le interazioni tra utenti e sistema usando un modello grafico e testo in linguaggio naturale strutturato; sono una parte chiave dell'UML (Unified Modelling Language) e rappresentano l'insieme dei requisiti funzionali di un sistema.

- Identificano **attori** (categorie di utenti, non necessariamente umane) e **use case** (tipi di interazioni o feature offerte dal sistema).
- Informazioni aggiuntive sulle interazioni si forniscono con descrizioni testuali (strutturate) o modelli semi-formali (es. UML sequence diagram o statechart).
- Supportano la comunicazione con il cliente per definire le funzionalità: vanno tenuti il più semplici possibile, definiscono cosa il sistema deve fare e non come è implementato, dal punto di vista degli utenti (il sistema è una black box).
- Sono spesso documentati con un use case diagram ad alto livello.

### Attori

> [!def] Attore
> **Entità** esterna che interagisce con il sistema in sviluppo (SUD): classi di utenti umani, altri sistemi, ambiente fisico. È rappresentato con uno stick figure e ha un nome unico.

Gli attori sono più a grana grossa delle personas: un attore può essere associato a più personas. Per identificarli ci si può chiedere:

- quali gruppi di utenti sono supportati dal SUD nel loro lavoro?
- quali gruppi eseguono le funzioni principali offerte dal SUD?
- quali gruppi eseguono le funzioni secondarie, come l'amministrazione?
- il SUD interagirà con sistemi o software esterni? Ogni sistema esterno con cui il SUD interagisce sarà un attore.

Un attore non corrisponde a una singola entità: rappresenta una classe di utenti con lo stesso ruolo. Un utente può avere ruoli diversi nello stesso sistema: l'amministratore di un sito può anche visitarvisi come utente non autenticato.

### Use case ed ellissi

Gli use case sono rappresentati come **ellissi nominate** e corrispondono a feature del sistema che offrono beneficio o utilità agli attori; modellano i requisiti funzionali.

- Un use case astrae molti possibili **scenari** (sequenze di azioni) per una data feature: uno scenario è un'istanza di un use case.
- Uno use case rappresenta una classe di scenari che mirano a usare la stessa funzionalità (es. ci possono essere più modi di iscriversi a un corso).

### Associazioni

Un'**associazione** tra un attore e uno use case indica che l'attore può eseguire quel use case; graficamente è una linea che collega l'attore e l'ellisse.

### Attori secondari

Uno use case può essere associato a più attori: la semantica è che gli attori devono **collaborare** in qualche modo per eseguirlo. Le cardinalità sono supportate in UML 2.5: un attore esterno può partecipare in modo opzionale (es. cardinalità `0..1`).

![[1791c4a3782ba4f8b5798c45e4e492d97fa71469b10f4458e3d0494158514cee.jpg|350]]

Ad esempio, Customer e Cashier devono cooperare per eseguire il checkout, e opzionalmente può essere coinvolto un Bank Payment Processor (sistema esterno), ad esempio quando si paga con carta.

I diagrammi UCD non hanno strumenti per specificare come gli attori coinvolti interagiscono e le diverse responsabilità: servono descrizioni aggiuntive.

### Generalizzazione di attori

La **generalizzazione** tra attori si applica quando un attore è sotto-tipo di un altro: stesso concetto e notazione dei class diagram UML, graficamente una freccia con punta "vuota". L'attore specializzato può eseguire tutti gli use case che il padre può eseguire.

![[fa0f06dccbf1581305c7cd2dd9365da3ed7a2071634248e950eb2aab31d65d09.jpg|300]]

### Errori comuni nei use case diagram

> [!error] Errori da principianti
> - Gli use case devono dare un beneficio all'attore o aiutarlo a raggiungere un obiettivo: i nomi degli use case dovrebbero contenere un verbo, quelli degli attori un sostantivo.
> - Due attori associati allo stesso use case con cardinalità non nulla sono coinvolti (e devono collaborare) in ogni istanza dello use case: non significa che entrambi possano eseguirlo indipendentemente.
> - Attenzione alle generalizzazioni improprie: ogni attore dovrebbe avere use case propri, oltre a quelli ereditati; se l'attore specializzato non ha use case propri, la generalizzazione è inutile o mancano use case.
> - I diagrammi non devono diventare troppo complessi: relazioni tra use case e generalizzazioni con moderazione, modellazione a un grado di astrazione sufficientemente alto, ordine grafico (evitare linee che si incrociano). Un diagramma complesso è l'indicazione di un analista scarso.

## Formati dei use case

I use case si scrivono in formati e livelli di formalità diversi.

- **Brief**: riassunto stringato in un paragrafo, di solito dello scenario di successo principale.
- **Casual**: formato a paragrafi informale; più paragrafi che coprono scenari vari.
- **Fully-dressed**: tutti i passi e le variazioni scritti in dettaglio, con sezioni di supporto come precondizioni e garanzie di successo.

Brief e casual si usano nelle fasi iniziali della specifica per farsi un'idea rapida di soggetto e scope; i fully-dressed si sviluppano più avanti, come base di un contratto e per specificare in maggiore dettaglio il comportamento del sistema da sviluppare.

### Descrizioni testuali di uno use case

Una descrizione testuale include in genere quattro parti.

1. Cosa si aspettano sistema e utenti quando lo use case inizia.
2. Il flusso normale degli eventi (**main scenario**).
3. Cosa può causare errori e come i problemi risultanti vengono gestiti.
4. Lo stato del sistema al completamento dello use case.

## Il template di Cockburn

Per le descrizioni fully-dressed esistono formati diversi; un riferimento è il template proposto da Alistair Cockburn.

| Campo | Contenuto |
| --- | --- |
| `USE CASE #` | Numero e nome dello use case |
| `Goal in Context` | Obiettivo dello use case |
| `Preconditions` | Condizioni che devono valere per avviarlo |
| `Success End Condition` | Stato del sistema se lo use case ha successo |
| `Failed End Condition` | Stato del sistema se lo use case fallisce |
| `Primary Actor` | Attore principale |
| `Trigger` | Azione dell'attore principale che avvia lo use case |
| `Main Scenario` | Tabella dei passi: numero, azioni degli attori, risposta del sistema |
| `Extensions` | Varianti ed errori, in tabelle analoghe al main scenario |
| `Open Issues` | Aspetti ancora da chiarire; alla consegna del documento deve essere vuota |

### Scenario principale ed estensioni

> [!def] Scenario principale
> **Sequenza** di azioni che si verifica quando tutto nello use case procede come previsto (main success scenario).

Non tutto però procede sempre come previsto.

> [!def] Estensione
> **Descrizione** di una sequenza alternativa di azioni che può verificarsi nello use case: un'altra via per eseguirlo o un errore a un certo punto.

Gli utenti possono eseguire lo use case in modi diversi (es. autenticazione con PIN o con impronta) e può verificarsi un errore; nel definire il comportamento funzionale del sistema vanno descritte anche queste sequenze alternative tramite estensioni. Tipicamente c'è molto più testo nelle estensioni che nello scenario principale.

Un esempio completo mostra la struttura: use case "Withdraw money" di un ATM, con attore primario Customer.

| Passo | Customer | System |
| --- | --- | --- |
| 1 | Tocca lo schermo | |
| 2 | | Mostra M1 |
| 3 | Inserisce la carta | |
| 4 | | Mostra M2 |
| 5 | Tocca il pulsante "PIN" | |
| 6 | | Mostra M3 |
| 7 | Inserisce il PIN | |
| 8 | | Mostra M4 |
| 9 | Tocca il pulsante "Withdraw" | |
| 10 | | Mostra M5 |
| 11 | Tocca il pulsante "50 €" | |
| 12 | | Eroga il denaro, espelle la carta, mostra M6 |

Le estensioni coprono gli errori e le varianti: PIN non corretto, saldo insufficiente, contanti insufficienti nell'ATM, carta rubata o illeggibile, autenticazione biometrica al posto del PIN, ricevuta cartacea opzionale.

| Passo | Customer | System |
| --- | --- | --- |
| 7a `<PIN errato inserito>` | Inserisce il PIN | |
| 8a | | Mostra M7 e termina lo use case |

Il messaggio M7 informa che l'autenticazione è fallita e invita a recuperare la carta; altre estensioni, come il saldo insufficiente, possono chiudersi tornando a un passo dello scenario principale.

## Validazione dei requisiti

La validazione si preoccupa di dimostrare che i requisiti definiscano il sistema che il cliente vuole davvero.

> [!warning] Costo degli errori nei requisiti
> I costi degli errori nei requisiti sono alti: correggere un errore di requisito dopo la consegna può costare fino a 100 volte la correzione di un errore di implementazione, quindi la validazione è molto importante.

### Controlli sui requisiti

La validazione esamina cinque proprietà dell'insieme dei requisiti.

- **Validità**: il sistema fornisce le funzioni che supportano al meglio i bisogni del cliente?
- **Consistenza**: ci sono requisiti in conflitto tra loro?
- **Completezza**: tutte le funzioni richieste dal cliente sono incluse?
- **Realismo**: i requisiti sono implementabili con il budget e la tecnologia disponibili?
- **Verificabilità**: i requisiti possono essere controllati?

### Tecniche di validazione

- **Requirements reviews**: analisi manuale sistematica dei requisiti; review regolari durante la formulazione della definizione, con coinvolgimento sia dello staff del cliente sia dell'appaltatore; le review possono essere formali (con documenti completati) o informali, e una buona comunicazione tra sviluppatori, clienti e utenti risolve i problemi in stadio iniziale.
- **Prototyping**: uso di un modello eseguibile semplificato del sistema per controllare i requisiti; anche visual prototyping, con mockup o wireframe.
- **Test-case generation**: sviluppo di test per i requisiti per verificarne la testabilità.

### Controlli in review

Durante una review si controllano quattro proprietà di ogni requisito.

- **Verificabilità**: il requisito è realisticamente testabile?
- **Comprensibilità**: il requisito è compreso correttamente?
- **Tracciabilità**: l'origine del requisito è dichiarata chiaramente?
- **Adattabilità**: il requisito può cambiare senza un grande impatto sugli altri requisiti?