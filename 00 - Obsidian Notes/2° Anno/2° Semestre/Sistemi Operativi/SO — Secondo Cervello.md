# Sistemi Operativi (SO)

## Fondamenti e Architettura

### Il Sistema Operativo
> [!ABSTRACT] 
> Il Sistema Operativo è il primo strato software isolante. Nasconde la complessità dell'hardware grezzo e distribuisce equamente le risorse fisiche tra le applicazioni concorrenti.
> [!QUOTE] 
> Struttura: $\text{SO} = \text{Kernel} + \text{Programmi di Sistema}$. Il Kernel opera in modalità privilegiata (Ring 0), i programmi di sistema estendono le funzioni in user mode.
> [!EXAMPLE] 
> Considera un direttore d'orchestra. I musicisti (hardware) sanno suonare, ma senza il direttore (SO) che dà i tempi e gestisce gli spazi, il risultato è rumore caotico.
> [!DANGER] 
> Confondere il Kernel con l'intero SO. La shell o la GUI sono programmi utente (software di sistema), non fanno parte del Kernel isolato.

- Nodo Intermediario: Il software maschera l'hardware fisico sottostante all'utente finale.
- Nodo Allocatore: Il sistema risolve conflitti assegnando democraticamente risorse limitate.
- Nodo Kernel: Il nucleo esegue operazioni hardware esclusive in regime di massimo privilegio.

### Storia ed Evoluzione
> [!ABSTRACT] 
> I sistemi operativi evolvono per massimizzare l'uso della CPU. L'hardware più potente spinge il software a gestire più task simultaneamente.
> [!QUOTE] 
> Generazioni: Valvole (singolo utente) $\to$ Transistor (Batch) $\to$ Circuiti Integrati (Multiprogrammazione) $\to$ PC (GUI) $\to$ Mobile.
> [!EXAMPLE] 
> Immagina una lavanderia. Prima si lavava un calzino alla volta. Poi si è passati ai lotti (batch). Oggi la lavanderia lava, asciuga e stira capi di cento persone diverse contemporaneamente saltando da uno all'altro (Time Sharing).
> [!DANGER] 
> Sottovalutare l'impatto del disco rigido. Il passaggio dal nastro sequenziale al disco ad accesso casuale ha sbloccato fisicamente lo spooling e la multiprogrammazione reale.

- Nodo Batch: L'operatore raggruppa lavori simili per ottimizzare i tempi morti.
- Nodo Multiprogrammazione: La memoria ospita simultaneamente processi multipli in esecuzione alternata.
- Nodo Time Sharing: Il timer suddivide matematicamente l'uso CPU garantendo interattività continua.

### Architettura Hardware e Cicli Macchina
> [!ABSTRACT] 
> La CPU non agisce nel vuoto, ma orchestra un flusso continuo di dati attraverso il bus di sistema. Il ciclo di vita di un'istruzione è una sequenza meccanica e immutabile di fasi hardware.
> [!QUOTE] 
> Bus Principale: PCIe (Peripheral Component Interconnect Express) gestisce la concorrenza tra CPU e Controller per l'accesso alla memoria condivisa.
> Ciclo Macchina: Fetch (PC punta alla memoria, porta l'istruzione nell'IR) $\to$ Decode (Unità di controllo interpreta) $\to$ Execute (ALU calcola) $\to$ Store.
> [!EXAMPLE] 
> Il Bus PCIe è l'autostrada a più corsie. Il ciclo Fetch-Decode-Execute è il casellante: legge la targa (Fetch nel PC), capisce la classe del veicolo (Decode nell'IR), alza la sbarra (Execute).
> [!DANGER] 
> Credere che la CPU gestisca l'I/O direttamente byte per byte. Il Controller DMA (Direct Memory Access) sul bus PCIe ruba cicli di memoria (Cycle Stealing) trasferendo blocchi in RAM senza disturbare la CPU, avvisandola solo alla fine con un Interrupt.

- Nodo Interconnessione: Il bus PCIe multiplexa l'accesso fisico concorrente verso la RAM.
- Nodo Acquisizione: Il Program Counter (PC) indirizza inesorabilmente la prossima istruzione da caricare.
- Nodo Decodifica: L'Instruction Register (IR) trattiene il codice operativo durante l'interpretazione fisica.

### Interruzioni (Interrupt)
> [!ABSTRACT] 
> L'interruzione spezza il normale flusso del processore. Permette al sistema di reagire immediatamente a eventi esterni senza sprecare cicli in attese cieche (polling).
> [!QUOTE] 
> Tre varianti: Hardware Interrupt (asincrono da periferiche), Exception (sincrono da errori CPU), Trap (sincrono volontario da software).
> [!EXAMPLE] 
> Stai leggendo un libro. Se controlli la porta ogni secondo (polling) non leggi nulla. Se metti un campanello (interrupt), leggi in pace e alzi la testa solo quando suona.
> [!DANGER] 
> Lasciare il vettore delle interruzioni in user space. Un hacker potrebbe sovrascrivere l'indirizzo e dirottare la CPU verso codice maligno ad ogni click del mouse.

- Nodo Asincronia: Il segnale hardware interrompe imprevedibilmente il codice in esecuzione.
- Nodo Servizio: L'hardware esegue istantaneamente la routine specifica puntata dal vettore.
- Nodo Trap: L'applicazione software invoca deliberatamente l'intervento del Kernel privilegiato.

### Modalità Duale (Dual Mode) e Transizioni di Stato
> [!ABSTRACT] 
> La modalità duale blinda il sistema con un muro hardware. Divide l'universo in cittadini comuni (User Mode) e dittatori assoluti (Kernel Mode). Il passaggio di confine è regolato da rigidi protocolli di sicurezza.
> [!QUOTE] 
> Meccanismo hardware: Un bit di stato nella CPU (Mode Bit). 
> Dinamica del passaggio (Trap/Syscall): 1) Salvataggio completo dello stato utente nei registri del kernel. 2) Impostazione del Mode Bit a 0 (Kernel). 3) Consultazione della Tabella dei Vettori di Interruzione per saltare all'indirizzo sicuro della routine. 4) Ritorno a User Mode (Mode Bit a 1).
> [!EXAMPLE] 
> Entri in banca. Tu (User Mode) puoi compilare moduli nella hall. Se vuoi prendere i soldi dal caveau, chiedi al cassiere (Trap). Il cassiere fotografa la tua richiesta (salvataggio stato), consulta un registro blindato (Vettore Interruzioni) per sapere chi ha le chiavi, entra nel caveau (Kernel Mode) e torna da te coi soldi.
> [!DANGER] 
> Usare MS-DOS come riferimento. MS-DOS mancava del bit di modalità: un programma utente poteva formattare il disco direttamente aggirando ogni controllo.

- Nodo Barriera: Il bit hardware isola fisicamente l'esecuzione non sicura.
- Nodo Privilegio: Il Kernel Mode sblocca istruzioni macchina altrimenti inibite.
- Nodo Passaggio: L'eccezione controllata trasferisce temporaneamente il potere al sistema tramite vettori sicuri.

### Gerarchia delle Chiamate: API, ABI e Syscall
> [!ABSTRACT] 
> Le chiamate di sistema (Syscall) sono i portoni fisici del Kernel. Le API e le ABI sono i traduttori che rendono il passaggio comodo per i programmatori umani.
> [!QUOTE] 
> Stack: Codice C $\to$ API POSIX (funzione standard) $\to$ ABI (registri CPU) $\to$ Syscall (Trap). Argomenti passati tramite registri hardware.
> [!EXAMPLE] 
> Usi `printf` (API). La libreria standard traduce in `write` (POSIX). L'assembly carica `1` nel registro RAX (ABI) e spara il comando `syscall`. Il Kernel si sveglia e legge i registri.
> [!DANGER] 
> Credere che l'API coincida col Kernel. Una API come `printf` esplode in decine di piccole system call sottostanti o nessuna, operando puro formatting in user space.

- Nodo Astrazione: L'API POSIX standardizza brutalmente interfacce diverse tra sistemi operativi.
- Nodo Passaggio: L'architettura inietta parametri direttamente nei registri CPU fisici.
- Nodo Trap: L'istruzione macchina innesca la commutazione forzata di privilegio.

### Policy e Meccanismo
> [!ABSTRACT] 
> Il Meccanismo costruisce l'ingranaggio fisico. La Policy decide quando e come quell'ingranaggio deve girare.
> [!QUOTE] 
> Teorema del Design: Separare rigorosamente "Cosa" (Meccanismo) dal "Come" (Policy) garantisce flessibilità assoluta.
> [!EXAMPLE] 
> Il timer hardware (Meccanismo) scatta e blocca la CPU. Dare 10 millisecondi al Gioco e 2 millisecondi al Browser è la Policy.
> [!DANGER] 
> Cablare la policy nel codice sorgente del meccanismo. Invalida l'intero modulo per usi futuri o prioritizzazioni differenti.

- Nodo Strumento: L'hardware offre funzionalità grezze totalmente agnostiche.
- Nodo Decisione: L'algoritmo distribuisce logicamente i pesi sulle funzionalità grezze.

## Virtualizzazione e Struttura del Kernel

### Emulazione vs Virtualizzazione
> [!ABSTRACT] 
> L'emulazione finge l'hardware via software riga per riga. La virtualizzazione aggancia il sistema operativo ospite direttamente ai circuiti reali sfruttando supporti hardware.
> [!QUOTE] 
> Tipi: Virtualizzazione Tipo 1 (Bare Metal, Hypervisor domina l'HW) e Tipo 2 (Hosted, Hypervisor gira su un OS preesistente). Ring -1 inventato per Hypervisor.
> [!EXAMPLE] 
> Emulare è leggere uno spartito e cantare i suoni degli strumenti a bocca (lentissimo). Virtualizzare è mettere i musicisti veri nella stanza affittata, guidati dal tuo direttore.
> [!DANGER] 
> Dimenticare il Ring -1. Lo hypervisor Bare Metal deve comandare persino sui Kernel guest (che si credono Ring 0). Serve un livello fisico sotterraneo superiore.

- Nodo Emulazione: Il software traduce chirurgicamente ogni singola istruzione macchina incompatibile.
- Nodo Bare-Metal: L'ipervisore soppianta il SO originario prendendo controllo hw totale.
- Nodo Hosted: L'applicazione virtuale sfrutta pesantemente il sistema operativo ospitante.

### Architetture del Kernel
> [!ABSTRACT] 
> Il design del Kernel è una lotta eterna tra velocità brutale (Monolitico) e stabilità compartimentata (Microkernel).
> [!QUOTE] 
> Monolitico (Linux): tutto in kernel mode, massima velocità, alto rischio crash. Microkernel (Mach): solo IPC e scheduling in kernel, alta stabilità, pessimo overhead. Modulare: caricamento dinamico nel kernel.
> [!EXAMPLE] 
> Monolitico: un enorme palazzo di cemento armato; se cede un pilastro (driver audio), cade tutto. Microkernel: un villaggio di tende; se brucia una tenda, le altre restano, ma scambiarsi il sale richiede un messo postale (IPC).
> [!DANGER] 
> Ignorare i Kernel Ibridi. macOS unisce Mach (microkernel) con BSD (monolitico) per bilanciare i due estremi fallimentari in produzione.

- Nodo Monolitico: Il blocco unito massimizza spietatamente le prestazioni d'esecuzione.
- Nodo Microkernel: Il sistema espelle servizi superflui proteggendo blindatamente il nucleo.
- Nodo Modulare: Il blocco accetta estensioni dinamiche in runtime mantenendo privilegi massimi.

## Gestione dei Processi

### Il Concetto di Processo (RAM vs Eseguibile)
> [!ABSTRACT] 
> Un programma è un cadavere formattato su disco (ELF). Il processo è la sua resurrezione dinamica in memoria, dove il layout statico si trasforma in un'entità viva dotata di stack e heap.
> [!QUOTE] 
> Eseguibile Statico: Sezioni `.text` (RAW code) e `.rodata` (costanti Read-Only). 
> Layout in RAM: Text $\to$ Data $\to$ BSS $\to$ Heap (sale) $\to \dots \leftarrow$ Stack (scende). Il Loader in User Space legge la sezione `.dynamic` per agganciare le librerie condivise a runtime.
> [!EXAMPLE] 
> Il programma statico è un mobile IKEA nello scatolone (RAW/RODATA). Il processo è il mobile montato (RAM), ma per aggiungere i cassetti (librerie dinamiche), il Loader legge le istruzioni `.dynamic` e li monta all'ultimo secondo.
> [!DANGER] 
> Confondere le sezioni del file con la memoria in esecuzione. Lo Stack e l'Heap NON esistono nel file su disco; vengono creati dal Kernel solo durante il caricamento in RAM.

- Nodo Mappatura: Il Loader traduce il file statico ELF proiettandone le sezioni in memoria logica.
- Nodo Dinamismo: La direttiva `.dynamic` innesca il caricamento ritardato delle dipendenze a runtime.
- Nodo Espansione: L'allocazione contrapposta di heap e stack ottimizza lo spazio virtuale residuo.

### Ciclo di Vita del Processo e Stati Linux
> [!ABSTRACT] 
> Un processo non vive in uno stato eterno. Alterna raffiche di calcolo matematico a lunghi letarghi, governato spietatamente dallo Scheduler.
> [!QUOTE] 
> Stati generici: New $\to$ Ready $\leftrightarrow$ Running $\to$ Waiting $\to$ Terminated.
> Flag Linux reali (`top`/`ps`): `R` (Running/Runnable), `S` (Interruptible Sleep), `D` (Uninterruptible Sleep, I/O critico), `T` (Stopped da segnale), `Z` (Zombie).
> [!EXAMPLE] 
> Sei in pizzeria. `R`: Mangi o sei in fila. `S`: Aspetti la pizza ma puoi andartene (Ctrl+C). `D`: Hai già pagato e non puoi andartene finché non ti danno la ricevuta. `T`: Un vigile ti ha immobilizzato.
> [!DANGER] 
> Confondere Ready e Running in Linux. Linux li accorpa entrambi sotto il flag `R`. Se vedi 100 processi `R`, non stanno girando tutti, 99 sono in coda Ready e 1 solo è nella CPU.

- Nodo Coda: Lo scheduler confina il processo pronto nel limbo della lista Runnable.
- Nodo Sospensione: Il blocco I/O sgancia il processo scaraventandolo nello stato Sleep (S/D).
- Nodo Interdizione: Il segnale SIGSTOP congela brutalmente il task forzando lo stato Stopped (T).

### PCB e Context Switch
> [!ABSTRACT] 
> Il Process Control Block è la scatola nera del processo. Conserva esattamente i pensieri della CPU al momento in cui al processo viene strappata la parola.
> [!QUOTE] 
> Contenuto PCB: PID, State, Program Counter, Registri CPU, Limiti Memoria, File Aperti. Il Context Switch salva tutto e ripristina un altro PCB nel Kernel Stack.
> [!EXAMPLE] 
> Stai leggendo un libro e squilla il telefono. Metti un segnalibro (salvi PC e Registri nel PCB). Parli al telefono. Torni al libro aprendolo esattamente dal segnalibro (ripristini PCB).
> [!DANGER] 
> Sottovalutare l'overhead. Il Context Switch brucia tempo macchina reale. Durante lo scambio, la CPU produce zero lavoro utile per i programmi.

- Nodo Registro: Il blocco strutturato mappa l'intera anatomia funzionale del programma.
- Nodo Salvataggio: Lo scheduler fotografa brutalmente lo stato istantaneo dei registri HW.
- Nodo Spreco: L'operazione di scambio dissolve preziosi cicli macchina in logistica pura.

### Fork, Exec e Wait
> [!ABSTRACT] 
> La trinità della riproduzione dei processi POSIX. Fork clona il corpo, Exec fa il lavaggio del cervello, Wait raccoglie il testamento.
> [!QUOTE] 
> `fork()`: 1 chiamata, 2 ritorni (0 al figlio, PID al padre). Il figlio riceve una copia esatta dello spazio logico, ma da quel momento modificano variabili in percorsi separati e indipendenti. 
> `exec()`: Il Kernel distrugge Text, Heap e Stack attuali. Interviene il Loader (in User Space) che prepara la memoria e il nuovo Stack prima di chiamare il `main()`.
> [!EXAMPLE] 
> Fork: Il padre ha $X=5$. Fa la fork. Ora padre e figlio hanno entrambi $X=5$. Se il figlio fa $X++$, solo il suo diventerà 6. La memoria è fisicamente disaccoppiata (spesso tramite Copy-on-Write).
> [!DANGER] 
> Dimenticare il ruolo del Loader post-exec. L'eseguibile lanciato dall'exec non parte da solo: è il Loader in spazio utente che inietta gli argomenti `argc`/`argv` nello stack vergine prima di passare l'esecuzione al nuovo `main()`.

- Nodo Clonazione: La chiamata biforca chirurgicamente l'albero d'esecuzione in due coscienze logiche parallele e asincrone.
- Nodo Sostituzione: L'istruzione `exec` annienta l'identità operativa mentre il Loader innesca la nuova istanza.
- Nodo Sincronizzazione: L'attesa genitoriale recupera l'informazione finale prevenendo la generazione di Zombie.

### Zombie e Orfani
> [!ABSTRACT] 
> Un processo morto non sparisce immediatamente. Deve passare i suoi ultimi dati al padre. Se il padre ignora il cadavere, il processo infesta il sistema.
> [!QUOTE] 
> Equazione Zombie: $Zombie = \text{Stato Terminated} \land \text{Padre non ha chiamato } wait()$. 
> Il processo occupa 0 byte di memoria dati, ma trattiene ostinatamente la sua entry nel PCB per l'Exit Status. Orfano: padre morto prima, figlio adottato da `init/systemd` (PID 1).
> [!EXAMPLE] 
> Mangi una caramella (figlio termina). La carta vuota è lo Zombie. Finché non la butti nel cestino (`wait`), occupa fisicamente spazio nella tua tasca (tabella processi).
> [!DANGER] 
> Pensare che uno Zombie usi CPU. Non esegue nulla, ma consuma uno slot critico nella tabella del Kernel (PID exhaustion). Se i PID finiscono, il sistema si paralizza: non puoi più lanciare nemmeno `kill`.

- Nodo Relitto: Il kernel preserva forzatamente il PCB guscio per la lettura differita.
- Nodo Adozione: Il demone radice (PID 1) eredita l'orfano spazzando i residui tramite `wait()` automatica.

## Comunicazione Inter-Processo (IPC)

### Shared Memory vs Message Passing
> [!ABSTRACT] 
> O due processi scrivono sulla stessa lavagna, rischiano di scontrarsi, ma vanno veloci (Shared Memory). O si spediscono lettere formali tramite il postino del Kernel (Message Passing).
> [!QUOTE] 
> Shared Memory: zona RAM condivisa, setup syscall, dopo no overhead kernel, richiede sincronizzazione. Message Passing: syscall per ogni invio, lento ma sicuro.
> [!EXAMPLE] 
> Shared Memory: condividi l'accesso a un Google Doc. Message Passing: invii un allegato via email al collega.
> [!DANGER] 
> Dimenticare la sincronizzazione in Shared Memory. Due processi che alterano simultaneamente un contatore si corrompono a vicenda. Il Kernel si fa da parte e lascia esplodere il conflitto.

- Nodo Lavagna: Il kernel dischiude un'area RAM annullando l'isolamento nativo.
- Nodo Messaggero: L'operatore intercetta sistematicamente e bufferizza ogni singolo pacchetto in transito.
- Nodo Contesa: La memoria condivisa scarica drammaticamente l'onere sincronizzativo sugli attori.

### Produttore e Consumatore
> [!ABSTRACT] 
> Il modello classico di cooperazione. Uno sputa dati nel tubo, l'altro li beve. Il tubo ha una fine e un inizio (Bounded Buffer circolare).
> [!QUOTE] 
> Implementazione: buffer circolare size N. Indici `in` (dove scrivo) e `out` (dove leggo). Pieno se `(in+1)%N == out`. Vuoto se `in == out`.
> [!EXAMPLE] 
> Un nastro trasportatore di sushi. Il cuoco (Produttore) lo riempie ma si ferma se non c'è spazio. Il cliente (Consumatore) mangia ma si ferma se non ci sono piattini.
> [!DANGER] 
> Utilizzare il Busy Waiting (while vuoto) per attendere lo spazio. Blocca il processo in un ciclo infinito che divora CPU al 100% senza generare alcun dato utile.

- Nodo Ciclicità: L'operatore modulo incolla la fine dell'array all'inizio fisico.
- Nodo Saturazione: Il sistema blocca brutalmente l'inserimento escludendo l'ultimo slot utile.
- Nodo Spreco: L'attesa attiva brucia aggressivamente risorse preziose.

### API POSIX Shared Memory e Permessi Binari
> [!ABSTRACT] 
> L'API POSIX manipola la memoria RAM come se fosse un file invisibile. Crei il file virtuale e lo dimensioni, imponendo rigidi permessi crittografici di accesso in stile Unix.
> [!QUOTE] 
> Flusso: `shm_open("nome", O_CREAT | O_RDWR, 0666)` $\to$ `ftruncate(FD, size)` $\to$ `mmap()`.
> Permessi POSIX (Ottali/Binari): $0666$ significa `rw-rw-rw-` (User=4+2, Group=4+2, Others=4+2).
> [!EXAMPLE] 
> È come noleggiare un magazzino. `shm_open` crea la stanza con un lucchetto (0666 = tutti possono leggere e scriverci), `ftruncate` butta giù i muri per allargarlo, `mmap` ti crea una porta teletrasporto dal tuo salotto.
> [!DANGER] 
> Dimenticare che i puntatori ritornati da mmap sono diversi. Se il Processo A mette un puntatore assoluto nella shared memory, il Processo B lo leggerà, cercherà quell'indirizzo nel SUO spazio e causerà un SegFault. Usa solo offset (interi).

- Nodo Creazione: La chiamata `shm_open` alloca l'oggetto persistente applicando la maschera ottale dei permessi.
- Nodo Espansione: L'operatore dilata violentemente la dimensione del segmento grezzo.
- Nodo Proiezione: La primitiva `mmap` incastra stabilmente i blocchi fisici nel layout virtuale locale.

### Message Passing: Diretta vs Indiretta e Buffering
> [!ABSTRACT] 
> Nei messaggi puoi parlare a una persona precisa, oppure appendere il messaggio a una bacheca pubblica (Mailbox). E puoi aspettare risposte (Sincrono) o fuggire (Asincrono).
> [!QUOTE] 
> Diretta: `send(P, msg)`. Indiretta: `send(Porta_A, msg)`. Sincrono: bloccante (Rendezvous se entrambi bloccati). Capacità canale: Zero (forza Rendezvous), Bounded, Unbounded.
> [!EXAMPLE] 
> Diretta: metti la lettera in mano a Marco. Indiretta: lasci la lettera nella buca delle lettere 101, chi passa la prende. Asincrono Unbounded: infili lettere nella buca all'infinito e te ne vai.
> [!DANGER] 
> Sbagliare la capacità del canale in progettazione. Un canale Unbounded (illimitato) in presenza di un produttore molto più veloce del consumatore causerà un letale esaurimento (OOM) della RAM del sistema.

- Nodo Esplicito: L'invio incatena rigidamente l'identità crittografica di emittente e destinatario.
- Nodo Mailbox: La porta astratta disaccoppia ferocemente chi scrive da chi legge.
- Nodo Rendezvous: Il blocco bidirezionale paralizza la coppia forzando la sincronizzazione assoluta.

## Interfacce Utente e Shell

### La Shell Unix e le Variabili
> [!ABSTRACT] 
> La Shell non è il sistema operativo, è un traduttore. Legge il testo umano, lo analizza e orchestra chiamate di sistema per conto dell'utente, fornendo un micro-ambiente di esecuzione programmabile.
> [!QUOTE] 
> Esecuzione: Loop principale $\to$ Parse $\to$ Se Built-in (eseguito internamente) $\to$ Se Esterno (fork + exec usando la variabile d'ambiente `$PATH`).
> Variabili: Locali (valide solo nella shell corrente) vs Ambiente (`export`, ereditate da tutti i processi figli).
> [!EXAMPLE] 
> Definire `X=5` crea una variabile locale: un programma C lanciato da shell non vedrà mai $X$. Fare `export X=5` la eleva ad Ambiente, rendendola visibile al programma tramite le API di sistema.
> [!DANGER] 
> Confondere il comando `cd` con gli eseguibili. Il comando `cd` deve essere un Built-in che manipola la shell stessa. Se fosse esterno (eseguito tramite fork), cambierebbe la directory di un processo figlio fantasma che poi morirebbe, lasciando la shell originaria inalterata.

- Nodo Ciclo: L'interprete intercetta, analizza ed esegue ciclicamente i comandi testuali.
- Nodo Interno: Le funzioni built-in manipolano direttamente lo stato del processo shell (es. `cd`).
- Nodo Ereditarietà: Il comando export inietta forzatamente le configurazioni nello spazio dei processi discendenti.

### Redirezione e Pipeline
> [!ABSTRACT] 
> L'ecosistema Unix si basa su processi monouso connessi tra loro come tubi idraulici. L'output di uno diventa l'input vitale del successivo.
> [!QUOTE] 
> File Descriptors standard: 0 (stdin), 1 (stdout), 2 (stderr). Operatori: `>` (sovrascrive), `>>` (appende), `<` (legge), `2>` (errori), `|` (pipe).
> [!EXAMPLE] 
> `ls -la | grep ".c" > output.txt`. Il listato non appare a schermo, entra nel tubo `|`, viene filtrato da `grep`, e il risultato cade definitivamente nel file `>`.
> [!DANGER] 
> Usare `>` invece di `>>` per i log. Un singolo `>` distrugge irreparabilmente l'intero contenuto precedente del file ripartendo da zero.

- Nodo Standard: Il sistema alloca tre flussi primari ad ogni nuovo task lanciato.
- Nodo Concatenazione: La pipe fonde l'output sorgente con l'input destinazione in RAM.
- Nodo Deviazione: L'operatore sovrascrive fisicamente il flusso verso l'archivio permanente.

## Compilazione e Linking

### La Pipeline del Compilatore (GCC)
> [!ABSTRACT] 
> Il compilatore non è una scatola nera magica, ma una catena di montaggio a quattro stadi. Il codice passa da testo umano a linguaggio macchina puro.
> [!QUOTE] 
> Fasi: Preprocessore (risolve `#include`/`#define`, `.i`) $\to$ Compilatore (traduce in Assembly, `.s`) $\to$ Assemblatore (codice macchina, `.o`) $\to$ Linker (risolve riferimenti e librerie, `a.out`).
> [!EXAMPLE] 
> Preprocessore: inserisce la farina. Compilatore: impasta (assembly). Assemblatore: cuoce il pane (oggetto). Linker: ci mette dentro il prosciutto (librerie esterne) e chiude il panino (eseguibile).
> [!DANGER] 
> Confondere errore di compilazione con errore di linking. Syntax error = colpa del compilatore (fase 2). `Undefined reference to` = colpa del linker (fase 4), manca la libreria!

- Nodo Espansione: Il preprocessore ingloba spietatamente macro e librerie testuali.
- Nodo Traduzione: Il compilatore degrada il sorgente ad architettura mnemonica assembly.
- Nodo Saldatura: Il linker fonde oggetti disparati in un'unica entità eseguibile.

### Formato ELF e Librerie
> [!ABSTRACT] 
> I file eseguibili su Linux parlano la lingua ELF. Un dizionario rigoroso che insegna al loader come mappare le sezioni in memoria RAM.
> [!QUOTE] 
> Sezioni ELF: `.text` (istruzioni), `.data` (globali inizializzate), `.bss` (globali vuote). Librerie: Statiche (`.a`, copiate dentro) vs Dinamiche (`.so`, caricate a runtime).
> [!EXAMPLE] 
> Statico: Ti stampi la mappa di Roma su carta e la metti nello zaino (pesante, ma sicura). Dinamico: Usi Google Maps sul telefono (leggero, ma se manca la connessione/libreria, sei perso).
> [!DANGER] 
> L'inferno delle dipendenze (Dependency Hell). Aggiornare una libreria dinamica `.so` incompatibile distrugge istantaneamente tutti i programmi del sistema che vi fanno affidamento.

- Nodo Mappatura: L'header eseguibile istruisce il sistema operativo sull'allocazione spaziale.
- Nodo Statico: Il linker ingoia brutalmente l'intero codice dipendente nell'output.
- Nodo Dinamico: Il sistema risolve i puntatori di libreria esclusivamente in esecuzione.

### Automazione con Make
> [!ABSTRACT] 
> Make è uno strumento intelligente che compila solo il minimo indispensabile. Risparmia ore di attesa ricompilando unicamente i file modificati.
> [!QUOTE] 
> Logica: Legge il `Makefile`. Analizza il grafo delle dipendenze confrontando i Timestamp (data di modifica). Sintassi: `target: dipendenze \n \t comandi`.
> [!EXAMPLE] 
> Se cambi i tergicristalli, il meccanico (Make) cambia solo i tergicristalli, non rismonta l'intero motore.
> [!DANGER] 
> Indentare con gli spazi. La regola di Make esige un TAB reale e fisico. Uno spazio manderà in crash incomprensibile la build.

- Nodo Dipendenza: Il motore controlla ossessivamente le date di modifica dei sorgenti.
- Nodo Ricompilazione: Lo script innesca selettivamente i comandi sui nodi alterati.

## Comunicazione Avanzata

### Pipe Anonime e Named Pipe (FIFO)
> [!ABSTRACT] 
> Le pipe sono tubazioni idrauliche tra processi. Le anonime servono solo a parenti stretti (padre-figlio). Le FIFO sono canali pubblici nel filesystem.
> [!QUOTE] 
> Pipe: Array `[0]` per lettura, `[1]` per scrittura (Half-Duplex). FIFO: file fisico creato con `mkfifo`, vi si accede tramite `open` standard.
> [!EXAMPLE] 
> Pipe anonima: un walkie-talkie lasciato a tuo figlio. Named Pipe: la cassetta della posta fuori casa, accessibile da chiunque sappia l'indirizzo.
> [!DANGER] 
> Dimenticare di chiudere i lati inutilizzati. Se il padre non chiude il suo lato di lettura, la pipe non emetterà mai EOF e il lettore si bloccherà in attesa infinita.

- Nodo Flusso: Il kernel bufferizza i dati veicolandoli rigidamente in modo unidirezionale.
- Nodo Parentela: La pipe anonima richiede stretta discendenza biologica dei processi.
- Nodo Persistenza: La FIFO sopravvive nel filesystem garantendo accessi estranei.

## Thread e Concorrenza

### Processi vs Thread
> [!ABSTRACT] 
> Il processo è egoista: tiene la memoria per sé. I thread sono coinquilini: dividono tutto (Codice, Dati, File) tranne lo spazzolino (Registri e Stack).
> [!QUOTE] 
> Thread = flusso di controllo. Condivide col processo genitore: Memoria Virtuale, Text, Data, Heap. Ha di privato: Program Counter, CPU Registers, Stack.
> [!EXAMPLE] 
> Processo: Due cucine separate, due chef separati. Thread: Uno chef che taglia le carote e uno che bolle l'acqua nella STESSA cucina. Se uno sbaglia, brucia la cucina di entrambi.
> [!DANGER] 
> Conflitti in Heap. Poiché le variabili globali sono condivise, due thread che scrivono simultaneamente sulla stessa variabile generano una Race Condition mortale.

- Nodo Coabitazione: Il filo esecutivo respira l'identico spazio d'indirizzamento genitoriale.
- Nodo Privatizzazione: L'architettura riserva stack esclusivi per le variabili locali thread.
- Nodo Leggerezza: Il context switch tra thread polverizza l'overhead d'un cambio processo.

### Concorrenza, Parallelismo e Amdahl
> [!ABSTRACT] 
> Aggiungere mille processori non rende un programma mille volte più veloce, perché la parte che va eseguita in fila indiana fa da collo di bottiglia.
> [!QUOTE] 
> Concorrenza: task intercalati nel tempo (anche 1 core). Parallelismo: esecuzione fisica simultanea (N core). Legge di Amdahl: $Speedup = 1 / (S + (1-S)/N)$ dove S è la frazione Seriale.
> [!EXAMPLE] 
> 9 donne incinte (9 core in parallelo) non partoriscono un bambino in 1 mese (limite seriale incompressibile).
> [!DANGER] 
> Illusione multicore. Spendere soldi in hardware a 64 core per un algoritmo intrinsecamente seriale ($S=1$) restituisce uno speedup matematico identico a 1.

- Nodo Sovrapposizione: Lo scheduler illude l'utente con scambi d'esecuzione fulminei.
- Nodo Simultaneità: L'hardware fisico macina flussi istruttivi su silicio distinto.
- Nodo Limite: La componente algoritmica sequenziale strozza il potenziale scalare.

### Mapping: User Thread e Kernel Thread
> [!ABSTRACT] 
> Il Sistema Operativo non sa nulla dei thread creati puramente in user space. Per sfruttare il parallelismo reale, serve un ponte verso il Kernel.
> [!QUOTE] 
> Many-to-One: N user su 1 kernel. One-to-One: 1 user su 1 kernel (costoso ma parallelo). Many-to-Many: N user su M kernel. 
> Two-Level Model (Ibrido): Permette sia il many-to-many, sia di legare indissolubilmente ("Bound") uno specifico user-thread critico a un kernel-thread dedicato (es. Solaris/HP-UX).
> [!EXAMPLE] 
> Many-to-One: Un biglietto dell'autobus per 10 persone. One-to-One: Ognuno compra il suo. Two-Level: Ognuno compra il suo (1:1 per VIP), ma la plebe condivide i biglietti (M:N).
> [!DANGER] 
> La proliferazione (One-to-One). Generare migliaia di thread costringe il Kernel a creare migliaia di Kernel-Thread, causando collasso sistemico da overhead (esaurimento risorse Kernel).

- Nodo Oscurità: La libreria utente occulta i thread leggeri alla vista del sistema.
- Nodo Trasparenza: Il modello diretto accoppia ogni entità utente ad un'istanza kernel.
- Nodo Ibridazione: Il modello a due livelli protegge i thread prioritari con canali hw dedicati.

### Lightweight Process (LWP) e Upcall
> [!ABSTRACT] 
> Nel modello Many-to-Many, il Kernel non può parlare direttamente con la libreria utente. Serve una struttura dati intermedia e un citofono speciale per gestire i blocchi.
> [!QUOTE] 
> LWP (Lightweight Process): Struttura dati virtuale fornita dal kernel che funge da "processore virtuale" per gli user-thread.
> Upcall: Il citofono bottom-up. Quando un LWP si blocca su I/O, il Kernel fa una "Upcall" allo Scheduler User-Space dicendogli: "L'LWP è fermo, sgancia il thread e dammene un altro su un nuovo LWP!".
> [!EXAMPLE] 
> LWP è il cameriere. Se il cuoco (thread) si blocca perché manca il sale (I/O), il direttore del ristorante (Kernel) chiama il capo cuoco con l'Upcall dicendo: "Manda qualcun altro a fare i dolci su un altro bancone!".
> [!DANGER] 
> Ignorare le Upcall nel Many-to-Many. Senza l'Upcall, l'intero processo andrebbe in deadlock se tutti gli LWP si bloccassero su I/O, perché la libreria utente non saprebbe mai di dover rimpiazzare i thread bloccati.

- Nodo Interfaccia: Il Lightweight Process disaccoppia la libreria di user-space dal thread fisico del Kernel.
- Nodo Inversione: L'Upcall sovverte la direzione comunicativa classica notificando eventi dal Kernel all'Utente.

### Libreria POSIX (pthreads) e la Trappola della Fork
> [!ABSTRACT] 
> Le API `pthreads` creano e distruggono flussi esecutivi. Ma mescolare thread e processi (`fork`) crea mostri logici che distruggono la coerenza della memoria.
> [!QUOTE] 
> `pthread_create()` lancia thread; `pthread_join()` aspetta. 
> Regola della Fork: Se un thread chiama `fork()`, viene duplicato SOLO IL THREAD CHIAMANTE, creando un processo figlio single-threaded. L' `exec()` invece pialla l'intero processo sovrascrivendo l'area Text.
> [!EXAMPLE] 
> Un processo ha 4 thread (4 chef). Se uno chef fa `fork`, crea un ristorante clone con LUI SOLO dentro. Le 3 pentole degli altri chef rimangono sul fuoco (Lock bloccati) nel nuovo ristorante, senza nessuno a spegnerle.
> [!DANGER] 
> Chiamare `fork` in un thread ignorando le risorse condivise. Il figlio clonato eredita tutti i Mutex bloccati dagli altri thread (che non esistono nel figlio). Deadlock immediato alla prima chiamata al Mutex. Serve la funzione di pulizia `pthread_atfork()` prima di duplicare.

- Nodo Instanziazione: L'invocazione distacca un frammento asincrono sul puntatore funzione.
- Nodo Amputazione: La duplicazione tramite fork esclude ferocemente i rami esecutivi fratelli, copiandone però gli stati di blocco.
- Nodo Sostituzione: La chiamata exec annienta totalmente il multithreading rimpiazzando l'intero spazio di memoria.

## CPU Scheduling (Breve e Medio Termine)

### Scheduler e Dispatcher
> [!ABSTRACT] 
> Lo Scheduler decide democraticamente chi sarà il prossimo a sedersi sul trono. Il Dispatcher è il boia che esegue lo sfratto fisico.
> [!QUOTE] 
> Scheduler (Short-term): sceglie da coda Ready. Preemptive (interrompe a forza) vs Non-preemptive. Dispatcher: esegue Context Switch, cambia in User Mode, fa saltare il PC.
> [!EXAMPLE] 
> L'infermiera del triage (Scheduler) decide l'ordine dei pazienti. Il barelliere (Dispatcher) sposta materialmente i letti. Se il barelliere è lento (Dispatch Latency), l'ospedale si blocca.
> [!DANGER] 
> Sottovalutare la Latenza di Dispatch. Se lo scheduler assegna 1 millisecondo a task, ma il context switch costa 1 millisecondo, l'efficienza reale della CPU crolla a zero.

- Nodo Selezione: L'algoritmo scruta la coda individuando il candidato ottimale.
- Nodo Materializzazione: L'operatore inietta forzatamente il contesto nei registri fisici.
- Nodo Prelazione: Il timer spodesta tirannicamente il processo dominante.

### Metriche di Scheduling
> [!ABSTRACT] 
> Non esiste l'algoritmo perfetto, solo compromessi. Massimizzare i lavori completati danneggia il tempo di reazione dell'utente, e viceversa.
> [!QUOTE] 
> CPU Util (%), Throughput (task/s). Da minimizzare: Turnaround (tempo totale vita), Waiting time (attesa fissa in Ready), Response time (tempo primissima reazione).
> [!EXAMPLE] 
> Batch server $\to$ Punta al Throughput, non importa se risponde dopo 2 ore. Desktop UI $\to$ Punta al Response time, il mouse deve muoversi all'istante (bassa varianza).
> [!DANGER] 
> Fissarsi sulla media del Response Time ignorando la varianza. Un lag di 5 secondi una volta al minuto manda ai matti un utente desktop molto più di un ritardo costante di 100ms.

- Nodo Occupazione: Il parametro satura i cicli disponibili annientando i tempi morti.
- Nodo Conclusione: Il ciclo cronometra brutalmente nascita e morte del task.
- Nodo Reazione: La tolleranza utente impone risposte nervose immediate.

### Algoritmi Tradizionali ed Exponential Averaging
> [!ABSTRACT] 
> La storia dello scheduling è la ricerca della formula magica per indovinare il futuro. L'SJF è ottimale ma incalcolabile, quindi si usano modelli matematici predittivi che sfumano il passato.
> [!QUOTE] 
> FCFS (Effetto convoglio). SJF (Ottimale, stima necessaria). Round Robin (Time sharing, $q$ critica).
> Formula Exponential Averaging (per SJF): $\tau_{n+1} = \alpha t_n + (1 - \alpha)\tau_n$.
> ($\tau_{n+1}$ è il burst previsto, $t_n$ l'ultimo burst reale, $\alpha$ il peso della storia recente).
> [!EXAMPLE] 
> Se $\alpha = 1$, guardiamo solo l'ultima operazione (mi baso solo sull'istante fa). Se $\alpha = 0$, guardiamo solo il passato remoto (sono sordo ai cambiamenti recenti). L'esponenziale fa decadere il peso del passato lontano rapidamente, seguendo i cambi di fase I/O del processo.
> [!DANGER] 
> Round Robin con $q$ minuscolo. Genera un letale trashing di contesto (Dispatch Latency dominante) dove la CPU spende più tempo a cambiare processo che a eseguire codice matematico utile.

- Nodo Ordine: La coda ingenua FCFS privilegia ciecamente il primo arrivato, causando il letale Effetto Convoglio.
- Nodo Previsione: La media esponenziale interpola dinamicamente i burst bilanciando l'attualità.
- Nodo Alternanza: Il quanto circolare trancia inesorabilmente i monopoli prolungati.
- Nodo Promozione: L'invecchiamento artificiale (Aging) aumenta la priorità e scongiura la Starvation.

### Code Multiple (Multilevel Queue e Feedback)
> [!ABSTRACT] 
> Non tutti i processi nascono uguali. I processi di sistema vanno nell'attico VIP, i processi background in cantina. Il Feedback Queue li fa salire e scendere.
> [!QUOTE] 
> Multilevel Queue: Code stagne con policy diverse (RR per foreground, FCFS per background). Multilevel Feedback Queue: Dinamica. Se usi troppa CPU cadi in basso, se aspetti troppo sali in alto.
> [!EXAMPLE] 
> Un videogioco è nel girone VIP per reattività. Se il videogioco comincia a compilare shader al 100% CPU, lo Scheduler Feedback lo sbatte nel girone dei minatori (background) per far respirare il mouse.
> [!DANGER] 
> Usare code statiche fisse. Rischiano di affamare permanentemente i task background se il foreground è incessantemente saturo. Il feedback è obbligatorio.

- Nodo Segregazione: Il recinto partiziona le categorie operative in silos invalicabili.
- Nodo Dinamismo: L'algoritmo declassa brutalmente gli ingordi promuovendo gli affamati.

### Real-Time CPU Scheduling
> [!ABSTRACT] 
> Nel mondo Real-Time, completare un calcolo in ritardo non è "lento", è "sbagliato". Un airbag che si apre in ritardo è mortale.
> [!QUOTE] 
> Soft Real-Time (Priorità garantita, no certezza matematica) vs Hard Real-Time (Deadline garantita o fallimento). Algoritmi: RMS (priorità statica su Periodo) vs EDF (priorità dinamica su Deadline Imminente).
> [!EXAMPLE] 
> Soft RT: Streaming video (un frame perso fa scattare l'immagine). Hard RT: Pilota automatico di un Boeing (un frame perso fa schiantare l'aereo).
> [!DANGER] 
> Rate Monotonic (RMS) su carichi superiori al 69%. Oltre quella soglia di utilizzo teorica, l'assegnazione statica fallisce matematicamente e le deadline vengono violate. Serve EDF.

- Nodo Flessibilità: Il compromesso tollera scostamenti ritardando l'esecuzione critica.
- Nodo Assolutezza: Il vincolo temporale spezza irrevocabilmente la computazione tardiva.
- Nodo Imminenza: L'algoritmo premia dinamicamente i task vicini alla scadenza (EDF).

### Multiprocessor e Affinità
> [!ABSTRACT] 
> Schedulare su un core è un cruciverba, schedulare su multicore è una partita a scacchi su tre tavoli. Spostare processi da un core all'altro svuota preziosissime memorie cache.
> [!QUOTE] 
> SMP (Symmetric): Ogni core si auto-schedula su coda privata. Load Balancing: Push (spingo via) e Pull (rubo task). Processor Affinity: Tendenza a non cambiare core per non invalidare la Cache (cruciale per NUMA).
> [!EXAMPLE] 
> Coda privata: 4 casse al supermercato. Pull migration: Se la mia cassa finisce i clienti, vado a pescarne uno dalla coda lunghissima del collega.
> [!DANGER] 
> Bilanciare troppo. Spostare ossessivamente un task da Core 0 a Core 1 per "equilibrio" distrugge l'hit-rate della Cache L1/L2, paralizzando le prestazioni per colpa del miss-rate di memoria.

- Nodo Simmetria: L'architettura clona i decisori rendendo ogni chip autonomo.
- Nodo Bilanciamento: I migratori intercettano gli squilibri travasando carichi computazionali.
- Nodo Radicamento: L'affinità inchioda il task al processore preservando la cache locale.

### Sistemi Operativi Moderni
> [!ABSTRACT] 
> Linux e Windows hanno abbandonato i tempi fissi ingenui per modelli probabilistici e calcoli virtuali complessi per garantire equità suprema.
> [!QUOTE] 
> Linux (CFS $\to$ EEVDF): Usa il Vruntime (tempo virtuale). Chi ha lavorato meno, gira per primo. Windows: 32 livelli di priorità Preemptive (boost interattivi, real-time in alto).
> [!EXAMPLE] 
> Linux CFS: Un registro dei debiti. Il processo in esecuzione matura debiti di CPU. Appena un processo in attesa risulta meno indebitato, prende il posto.
> [!DANGER] 
> Confondere i thread utente con lo scheduling reale. I moderni SO (SCS - System Contention Scope) schedulano ESCLUSIVAMENTE Kernel-Threads. Il concetto di "Processo" è solo un contenitore per il SO.

- Nodo Equità: Il cronometro virtuale pesa implacabilmente il tempo d'uso pregresso (Linux).
- Nodo Prioritizzazione: I livelli stratificati sorpassano le code imponendo gerarchie militari (Windows).

## Segnali e Terminazione (Thread)

### Segnali in Contesto Multi-Thread
> [!ABSTRACT] 
> In un processo multi-thread, i segnali inviati al PID globale colpiscono un thread a caso che non li ha bloccati. Per avere il controllo, ogni thread deve gestire esplicitamente la propria maschera.
> [!QUOTE] 
> Comportamento: `pthread_sigmask(HOW, &set, &oldset)` modifica la maschera del singolo thread. Se chiamata PRIMA della `pthread_create`, i thread figli ereditano la maschera.
> Accodamento (Pending): I segnali ordinari (es. `SIGUSR1`) NON si accodano. Se ne arrivano 3 mentre sono mascherati, quando si sbloccano l'handler scatta UNA sola volta. I segnali Real-Time (`SIGRTMIN` a `SIGRTMAX`) invece vengono accodati e smaltiti in sequenza.
> [!EXAMPLE] 
> Se invii 5 email a un collega con la casella piena (segnali ordinari), lui vede "Hai nuove email" e legge l'ultima. Se sono pacchi postali tracciati (Real-Time), il corriere gli consegna 5 pacchi in fila.
> [!DANGER] 
> Confondere l'ereditarietà delle maschere. Impostare la maschera prima di lanciare i thread silenzia l'intero programma: nessun thread gestirà il segnale e rimarrà in pending perpetuo. L'ordine di dichiarazione è vitale.

- Nodo Isolamento: La maschera locale scherma chirurgicamente il singolo flusso d'esecuzione ignorando lo stato globale.
- Nodo Ereditarietà: La clonazione del thread duplica inesorabilmente la configurazione dei segnali del genitore.
- Nodo Accorpamento: Il kernel collassa istanze multiple dello stesso segnale ordinario in un unico evento pending.

### Cancellazione dei Thread e Identificatori (TID)
> [!ABSTRACT] 
> Uccidere brutalmente un thread lascia risorse appese (lock, socket). La terminazione deve essere cooperativa, concordando dei punti sicuri (cancellation points) in cui il thread accetta di morire.
> [!QUOTE] 
> Cancellazione: `pthread_cancel(tid)`. Stati: Asynchronous (morte istantanea, pericolosa), Deferred (default, aspetta un cancellation point), Disabled (richiesta in pending).
> Cancellation points: Syscall bloccanti (`sleep`, I/O, `wait`). Punto artificiale: `pthread_testcancel()`.
> TID User vs Kernel: `pthread_self()` restituisce il TID enorme della libreria POSIX. `syscall(SYS_gettid)` restituisce l'intero progressivo del Kernel LWP. Visibile in bash con `ps -T -p <PID>` o in `/proc/<PID>/task/`.
> [!EXAMPLE] 
> Asynchronous è un cecchino che ti spara mentre cucini (il gas rimane aperto). Deferred è un cameriere che ti chiede di uscire, e tu accetti solo dopo aver spento i fornelli (cancellation point).
> [!DANGER] 
> Cicli CPU-bound senza `pthread_testcancel`. Un thread che calcola $\pi$ per ore in stato Deferred non incontrerà mai una syscall bloccante. La `pthread_cancel` verrà ignorata all'infinito e il programma non riuscirà mai a terminare.

- Nodo Differimento: La libreria posticipa la terminazione letale fino all'invocazione di istruzioni di sistema bloccanti.
- Nodo Iniezione: La funzione testcancel introduce artificialmente un varco di terminazione nei cicli puramente matematici.
- Nodo Dualismo: L'architettura Linux mappa 1:1 l'identificatore utente virtuale sul Lightweight Process fisico del kernel.

### Valutazione degli Algoritmi di Scheduling
> [!ABSTRACT] 
> La matematica non basta per giudicare uno scheduler. Un algoritmo perfetto sulla carta può devastare le performance a causa dei costi nascosti di esecuzione nel sistema operativo.
> [!QUOTE] 
> Metodi: Deterministico (valutazione su un set di arrivi noto, es. Gantt), Modelli a Code (formula di Little $N = \lambda W$), Simulazione (generatori casuali).
> La Verità: L'unico vero test è l'implementazione intra-Kernel. L'algoritmo vive nell'ecosistema reale con overhead di Context Switch, Cache Miss e Contention.
> [!EXAMPLE] 
> Il modello deterministico è testare un'auto in galleria del vento (perfetta ma finta). Il kernel è testare l'auto in autostrada in mezzo al traffico, ai sassi e alla pioggia (l'unica metrica che conta).
> [!DANGER] 
> L'ossessione teorica per il turnaround. Disegnare uno scheduler super-intelligente (O(n)) che però impiega millisecondi per decidere chi mandare in CPU causa Trashing: la potenza globale viene bruciata solo per prendere decisioni, non per calcolare.

- Nodo Astrazione: Il modello a code semplifica matematicamente flussi statistici astratti.
- Nodo Pragmatismo: L'immersione nel nucleo espone l'algoritmo all'imponderabile latenza architetturale fisica.

## Sincronizzazione e Lock

### Il Problema: Race Condition e Atomicità
> [!ABSTRACT] 
> I thread condividono la memoria globale. Se due tentano di modificare contemporaneamente la stessa variabile senza protezione, i loro calcoli si incrociano distruggendo la coerenza del dato.
> [!QUOTE] 
> Il problema: L'istruzione ad alto livello `counter++` esplode in 3 istruzioni macchina (Atomicità mancante): 1) Load registro, 2) Incrementa registro, 3) Store memoria.
> Il Context Switch fatale: Se il Dispatcher interrompe il Thread A subito dopo la Load, il Thread B leggerà il valore vecchio. Quando A riprende, sovrascrive il lavoro di B.
> [!EXAMPLE] 
> Due persone aggiornano il saldo del conto leggendo l'estratto conto cartaceo. Entrambi leggono 100€, entrambi aggiungono 50€. Entrambi scrivono 150€. Il totale reale doveva essere 200€, ma un versamento è svanito nel nulla (Race Condition).
> [!DANGER] 
> Testare il codice multi-thread credendo sia sicuro perché "funziona 99 volte su 100". Le Race Condition sono insetti stocastici: si manifestano solo quando lo Scheduler taglia i tempi esecutivi nell'esatto nanosecondo tra una Load e una Store assembly.

- Nodo Disgregazione: L'istruzione software unitaria si scompone in un micro-ciclo hardware vulnerabile alle interruzioni.
- Nodo Interfogliamento: La prelazione dello scheduler incrocia caoticamente i registri fisici sovrascrivendo l'avanzamento logico.
- Nodo Incoerenza: L'accesso parallelo non sincronizzato corrompe irreversibilmente le strutture dati globali.

### La Sezione Critica (Le Tre Proprietà)
> [!ABSTRACT] 
> Per evitare le Race Condition, il codice che tocca dati condivisi viene isolato in un bunker (Sezione Critica). Ma il bunker deve seguire regole matematiche per non paralizzare l'intero sistema.
> [!QUOTE] 
> Proprietà obbligatorie: 
> 1) Mutua Esclusione: Max 1 processo nel bunker. 
> 2) Progresso: Se il bunker è vuoto e qualcuno vuole entrare, la decisione avviene in tempo finito e partecipano solo i richiedenti. 
> 3) Bounded Waiting: Limite massimo al numero di volte che altri possono sorpassare un processo in attesa (niente Starvation).
> [!EXAMPLE] 
> 1) Mutua esclusione: Nel bagno entra uno alla volta. 2) Progresso: Se il bagno è vuoto, non serve il voto di tutto l'ufficio per decidere chi entra. 3) Bounded Waiting: Non puoi farti superare da 100 VIP all'infinito, prima o poi tocca a te.
> [!DANGER] 
> Progettare algoritmi che garantiscono solo la Mutua Esclusione. L'approccio ingenuo che blocca tutto rispetta l'esclusione, ma viola il Bounded Waiting (affama i task deboli) o il Progresso (Deadlock perpetuo dove nessuno decide chi deve entrare).

- Nodo Isolamento: La barriera logica confina spietatamente le operazioni di mutazione condivisa.
- Nodo Risoluzione: L'algorithm sblocca le contese escludendo dalla decisione le entità estranee al conflitto.
- Nodo Equità: Il limite superiore di sorpasso garantisce matematicamente l'accesso differito eliminando la fame da risorse.

### Soluzione di Peterson e Memory Barriers
> [!ABSTRACT] 
> La soluzione di Peterson è l'algoritmo teorico perfetto per sincronizzare due processi usando solo software. Sfrutta il concetto di "gentilezza aggressiva" per evitare collisioni.
> [!QUOTE] 
> Codice: Variabili condivise `int turn` e `bool flag[2]`. 
> Per entrare: `flag[i] = true; turn = j; while(flag[j] && turn == j);`
> Il fallimento moderno: L'algoritmo fallisce sui processori attuali perché il compilatore riordina le istruzioni (`flag=true` e `turn=j`) rompendo la logica. 
> Soluzione: Memory Barriers (`__atomic_thread_fence`), istruzioni HW che impediscono al compilatore e alla CPU di riordinare le memorie oltre il recinto.
> [!EXAMPLE] 
> La regola è: "Voglio entrare (flag), ma prego prima tu (turn)". Se entrambi arrivano insieme, l'ultimo che dice "prego prima tu" sovrascrive il turno, bloccandosi e facendo passare l'altro.
> [!DANGER] 
> Fidarsi della logica sequenziale del codice C. Il compilatore considera `flag` e `turn` variabili indipendenti e, per ottimizzare l'uso dei registri, inverte le assegnazioni riga per riga, disintegrando completamente l'algoritmo di Peterson a runtime.

- Nodo Intenzione: Il marcatore booleano dichiara irrevocabilmente la volontà d'accesso alla zona contesa.
- Nodo Concessione: Il passaggio di turno sblocca gli stalli garantendo matematicamente il progresso esecutivo.
- Nodo Barriera: L'istruzione di recinzione blocca l'ottimizzatore hardware imponendo l'ordine cronologico assoluto delle scritture.

### Supporto Hardware: Test-And-Set e CAS
> [!ABSTRACT] 
> Il software non può garantire l'atomicità senza aiuto fisico dal silicio. I processori moderni forniscono istruzioni hardware speciali che bloccano il bus di memoria, eseguendo lettura e scrittura in un singolo ciclo inscindibile.
> [!QUOTE] 
> Istruzione `Test-And-Set`: Setta un booleano a `True` e restituisce il valore vecchio atomicamente.
> Istruzione `Compare-And-Swap (CAS)`: (x86 `LOCK CMPXCHG`) Confronta un indirizzo col valore atteso; se corrispondono, inietta il nuovo valore. Restituisce sempre il valore originario.
> [!EXAMPLE] 
> Immagina un lucchetto fisico. Il CAS è un ingranaggio: "Se la combinazione è 0 (libero), metti a 1 (chiuso) in un solo scatto". Se provano in 10 nello stesso nanosecondo, l'hardware garantisce che solo uno scatta.
> [!DANGER] 
> Il Bounded Waiting non garantito. I lock base costruiti su CAS o Test-And-Set proteggono la Sezione Critica (Mutua Esclusione), ma se 100 processi fanno polling nel `while`, l'hardware sceglie pseudo-casualmente chi passa. Serve un array circolare `waiting[N]` esplicito (CAS generalizzato) per forzare il Bounded Waiting ed evitare starvation fatali.

- Nodo Atomicità: L'hardware fonde inesorabilmente la lettura e la mutazione bloccando l'interferenza esterna.
- Nodo Confronto: L'architettura inietta il dato nuovo esclusivamente se la precondizione logica combacia perfettamente.
- Nodo Stallo: L'attesa attiva (Spinning) costringe il processore a interrogare ossessivamente la memoria bruciando cicli macchina.

### Spin Lock, Mutex e Semafori
> [!ABSTRACT] 
> Non tutti i lucchetti sono uguali. L'hardware fornisce atomicità grezza, su cui i Sistemi Operativi costruiscono gerarchie di sincronizzazione con trade-off opposti tra spreco di CPU (Spinning) e costo di Context Switch (Sleeping).
> [!QUOTE] 
> Spin Lock: Busy waiting puro (`while(CAS(lock,0,1)!=0)`). Zero context switch, ma brucia cicli. Usato internamente nel Kernel sui Multicore per attese piccolissime. Dannoso in Single-core.
> Mutex: Locking con sospensione. Se chiuso, il SO fa una `sleep()` al thread (Context Switch costoso) e lo parcheggia in una Wait Queue.
> Semaforo Contatore (Dijkstra): Variabile $S$ con `wait()` (se $S < 0$ blocca) e `signal()` (se $S \leq 0$ sveglia un bloccato). Se inizializzato a $k>1$, permette $k$ accessi simultanei.
> [!EXAMPLE] 
> Spin lock è tenere il motore su di giri al semaforo aspettando il verde (consumi benzina ma scatti subito). Mutex è spegnere il motore, farsi svegliare dal clacson e riaccendere (risparmi benzina ma ci metti un secondo a ripartire).
> [!DANGER] 
> Usare Spin Lock in user space. Un processo utente prelazionato mentre tiene uno Spin Lock paralizzerà tutti gli altri thread core in attesa attiva fino al ritorno del suo time slice, azzerando le prestazioni della CPU.

- Nodo Spinning: Il ciclo di interrogazione continua elimina la latenza di riattivazione a costo di paralisi architetturale temporanea.
- Nodo Sospensione: Il mutex delega l'attesa allo scheduler disattivando forzatamente l'esecuzione del processo richiedente.
- Nodo Sequenzializzazione: Inizializzando un semaforo a 0, si impone matematicamente a un thread di non procedere prima della `signal` di un altro.

### Ottimizzazione della Contention e Lock-Free
> [!ABSTRACT] 
> Sincronizzare è lento. L'ossessione per i mutex su operazioni ad alta frequenza devasta il parallelismo. Esistono tecniche per minimizzare le contese o eliminarle alla radice tramite algoritmi Lock-Free.
> [!QUOTE] 
> Accumulo Locale: Invece di fare 100.000 `lock()` su una variabile globale, si incrementa un `local_counter` privato e si fa 1 sola `lock()` per sommare il totale alla fine.
> Lock-Free Increment: `do { temp = *v; } while(CAS(v, temp, temp+1) != temp)`. Zero lock. Il thread "ruba il tempo": se il CAS fallisce, ricarica il valore nuovo e riprova.
> [!EXAMPLE] 
> Accumulo: Non vai in banca (mutex) ogni volta che trovi 1€ a terra. Li metti nel salvadanaio (locale) e vai in banca una volta al mese.
> [!DANGER] 
> Lock-Free sotto alta contesa. Se 10 thread fanno push su uno stack lock-free contemporaneamente, 9 falliranno il CAS e riproveranno in loop. Il throughput crolla sotto il livello di un singolo Mutex classico a causa dei continui retry falliti (Starvation).

- Nodo Elusione: La privatizzazione del contatore disaccoppia il calcolo massivo dall'aggiornamento critico ritardato.
- Nodo Tentativo: L'algoritmo non bloccante proietta speculativamente la modifica e la commit atomica annullando i conflitti.
- Nodo Degrado: L'eccesso di concorrenza sui sistemi CAS-based innesca tempeste di collisioni e ritentativi perpetui.

### Monitor, Condition Variables e 5 Filosofi
> [!ABSTRACT] 
> Il Monitor è una classe ad alto livello che garantisce strutturalmente la Mutua Esclusione. Le Variabili di Condizione colmano una lacuna: permettere a un thread di "uscire temporaneamente dal bunker" se la risorsa non è pronta, senza bloccare gli altri.
> [!QUOTE] 
> Operazioni CV: `pthread_cond_wait(&cond, &mutex)` (rilascia atomicamente il mutex e dorme), `signal` (sveglia 1), `broadcast` (sveglia tutti).
> Invariante d'uso: Chiamare la wait sempre dentro un `while(!condizione)`, per difendersi dai **Spurious Wakeups** (sveglie fantasma dal SO).
> Pattern 5 Filosofi: Array `State state[5]`. La `test(i)` controlla: `if(state[i]==HUNGRY && left!=EATING && right!=EATING)`. Senza condizione, il codice naïve (`lock(left), lock(right)`) provoca deadlock simmetrico garantito.
> [!EXAMPLE] 
> Entri nel Monitor della cucina (Mutex preso), ma non c'è il pane. Invece di restare fermo paralizzando il fornaio, fai `cond_wait`: esci dalla cucina e ti metti in sala d'attesa (Mutex rilasciato). Il fornaio entra, fa il pane, e chiama `signal`. Tu rientri in cucina con il Mutex.
> [!DANGER] 
> Signal vs Broadcast distruttivi. Nel problema dei filosofi, avere UNA singola condition variable per tutti e usare `signal` è letale: il filosofo A potrebbe finire di mangiare e svegliare il filosofo C (invece dei suoi vicini), condannando B alla starvation. Serve `broadcast` o array di condition.

- Nodo Rilascio: L'operazione di attesa inietta una deroga alla mutua esclusione per disinnescare vicoli ciechi operativi.
- Nodo Risveglio: Il broadcast irradia globalmente lo sblocco costringendo i riceventi a rivalutare individualmente il proprio predicato.
- Nodo Spurio: L'iterazione condizionale `while` filtra a basso livello i risvegli involontari generati dal controller hardware.

### Deadlock e Priority Inversion
> [!ABSTRACT] 
> Il parallelismo genera patologie incurabili. Il Deadlock è lo stallo circolare immortale; la Priority Inversion è il paradosso in cui un processo spazzatura paralizza il sistema vitale tenendo in ostaggio un lock.
> [!QUOTE] 
> Condizioni Deadlock (Coffman): 1) Mutua esclusione 2) Hold-and-wait 3) Non-preemption 4) Attesa circolare (Es. Thread1 ha M1, vuole M2; Thread2 ha M2, vuole M1).
> Priority Inversion: Thread H (Alta prio) aspetta un Mutex tenuto da Thread L (Bassa prio). Nel frattempo, Thread M (Media prio) entra, prelaziona L (perché M > L). Risultato: H è bloccato indirettamente da M.
> Soluzioni: Deadlock prevenuto con *Ordinamento Totale dei Lock* (prendere sempre M1 prima di M2). Prio Inversion prevenuta attivando la *Priority Inheritance* nel RTOS.
> [!EXAMPLE] 
> Prio Inversion (Caso Pathfinder, Marte 1997): Il task Meteo (L) legge i sensori e blocca il Bus Dati. Il task di Sistema Vitale (H) non può usare il Bus e va in panico, mentre un task secondario di Comunicazione (M) prelaziona beatamente il task Meteo. H muore per colpa di M.
> [!DANGER] 
> Progettare gerarchie di Lock non ordinate. Scrivere codice in cui il Modulo A prende il Lock 1 e poi il 2, e il Modulo B prende il Lock 2 e poi l'1, garantisce matematicamente che l'applicativo congelerà in produzione non appena lo scheduler interleaverà le chiamate.

- Nodo Interdipendenza: Il ciclo di attesa incatena reciprocamente le risorse in un collasso logico insanabile.
- Nodo Allineamento: La standardizzazione sequenziale delle richieste spezza a priori la chiusura del grafo delle assegnazioni.
- Nodo Ereditarietà: L'innalzamento temporaneo della priorità di esecuzione (Inheritance) scherma il possessore del lock dalle prelazioni intermedie.

## Gestione della Memoria e Paging

### Binding degli Indirizzi e MMU
> [!ABSTRACT] 
> Un programma non sa dove risiederà in RAM. Usare indirizzi fisici assoluti limiterebbe l'esecuzione a un singolo blocco predefinito. La CPU ragiona in uno spaziotempo fittizio, mentre l'hardware piega la realtà fisica.
> [!QUOTE] 
> Fasi di Binding: Compilazione (Codice assoluto), Caricamento (Codice rilocabile, offset base), Esecuzione (Indirizzi Logici/Virtuali).
> MMU (Memory Management Unit): L'hardware che traduce in tempo reale (runtime) l'indirizzo logico CPU nell'indirizzo fisico RAM.
> [!EXAMPLE] 
> L'indirizzo logico è il "capitolo 5" di un libro. L'indirizzo fisico è "lo scaffale 3, ripiano B" della biblioteca. La MMU è il bibliotecario velocissimo che sa in ogni istante su quale scaffale ha temporaneamente appoggiato il capitolo 5.
> [!DANGER] 
> Credere che array `malloc` adiacenti logicamente lo siano anche fisicamente. Grazie alla MMU, un array gigante contiguo nello spazio virtuale (logico) potrebbe essere frammentato in blocchi distanti chilometri sulla RAM di silicio reale.

- Nodo Astrazione: Il binding dinamico scinde inesorabilmente l'identificatore simbolico dalla coordinata elettronica effettiva.
- Nodo Traduzione: La circuiteria integrata della MMU intercetta silenziosamente ogni operazione sul bus dati.
- Nodo Illusione: Il processo viene ingannato ricevendo una mappa di memoria perfettamente contigua e azzerata.

### Allocazione e Frammentazione
> [!ABSTRACT] 
> Gestire la memoria come un lungo nastro continuo è un fallimento matematico. Allocare e deallocare processi di dimensioni diverse bucherella irreparabilmente lo spazio utilizzabile.
> [!QUOTE] 
> Frammentazione Esterna: Buchi vuoti troppo piccoli tra i processi. Con algoritmo *First Fit*, fino al 50% della memoria va sprecata. Compattare (spostare tutto) bloccherebbe il SO.
> Frammentazione Interna: Lo spreco *dentro* un blocco allocato, se il programma non lo riempie totalmente.
> [!EXAMPLE] 
> Frammentazione Esterna: Nel parcheggio ci sono 10 posti liberi sparsi, ma arriva un autobus che occupa 3 posti adiacenti e non può parcheggiare.
> [!DANGER] 
> Allocazione contigua nei sistemi moderni. Nessun SO di questo secolo alloca memoria fisica in modo sequenziale puro, perché il blocco del sistema per la De-frammentazione della RAM sarebbe inaccettabile.

- Nodo Dispersione: L'allocazione eterogenea lacera il nastro di memoria creando inservibili micro-segmenti vuoti.
- Nodo Spreco: L'assegnazione rigida di blocchi genera fisiologicamente avanzi invisibili al sistema (frammentazione interna).

### Paging e Indirizzamento (Matematica Hardware)
> [!ABSTRACT] 
> Il Paging annienta la frammentazione esterna tagliando l'universo in cubetti microscopici identici. La memoria fisica e quella logica vengono separate brutalmente in griglie sovrapponibili.
> [!QUOTE] 
> Page (Logica) e Frame (Fisica): Entrambi hanno la stessa identica grandezza fissa (potenze di 2, es. 4 KB o Huge Pages 2MB).
> Traduzione Hardware: Indirizzo logico diviso in `p` (Page Number, che diventa indice per la Page Table) e `d` (Offset). La Page Table mappa `p` $\to$ `f` (Frame). L'indirizzo fisico finale è `f` incollato a `d`.
> Formula Bit: Spazio Logico $2^m$, Pagina $2^n$. L'offset occupa $n$ bit. Il numero pagina $p$ occupa $m-n$ bit. La Page table ha $2^{m-n}$ entries.
> [!EXAMPLE] 
> Dividere un libro in dispense da 4 pagine. L'indice logico dice "Pagina 1, Riga 10". La Page Table dice che la dispensa 1 si trova nel faldone fisico 8. L'indirizzo fisico sarà "Faldone 8, Riga 10". (La riga, l'offset `d`, non cambia mai).
> [!DANGER] 
> La trappola delle Huge Pages. Usare pagine da 1GB rimpicciolisce enormemente la Page Table, alleggerendo la cache della TLB, ma massimizza la Frammentazione Interna: se un processo alloca solo 10 byte, butterà via interi 1GB di RAM.

- Nodo Scissione: Il partizionamento geometrico frantuma lo spazio fisico in unità di archiviazione standardizzate.
- Nodo Corrispondenza: La tabella di routing in memoria accoppia la coordinata virtuale al quadrante in silicio (p $\to$ f).
- Nodo Invarianza: Lo scostamento relativo (offset) scavalca la traduzione hardware conservando intatta l'indicizzazione intra-pagina.
