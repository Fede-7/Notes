## Pagina 1

File System

---

## Pagina 2

File System e Memoria di Massa

□ I File System forniscono metodi efficienti di accesso ai file

□ Organizzano l’informazione in termini di File

□ Il file system risiede permanentemente in memoria di massa

□ Tipicamente questa memoria è fornita dai dischi:

□ Possono essere letti e scritti localmente (scarico un blocco in memoria, scrivo il blocco, ricarico il blocco)

□ Permettono l’accesso, sia sequenziale che diretto, ai blocchi fisici di memoria che memorizzano i diversi file.

□ La dimensione dei blocchi varia da dispositivo in dispositivo

□ Da 512 a 4096 Byte

□ Solitamente 4096 per NVM

---

## Pagina 3

Concetto di File

□ Unità logica di immagazzinamento in memoria secondaria
□ Vista uniforme sull’informazione memorizzata in mem non volatile
□ Spazio contiguo di indirizzi logici
□ Diversi tipi di dato:
  □ Dati
    ▶ numerico
    ▶ caratteri
    ▶ binari
    ▶ programmi (sorgente, eseguibile, etc.)

□ Contenuti definiti dal creatore del file
  □ Diversi tipi
    ▶ Considera text file, source file, executable file

---

## Pagina 4

Attributi del File

Un file è associato ad un insieme di attributi

- **Name** – denominazione (per utente umano)
- **Identifier** – tag unico (numero) che identifica il file nel file system
- **Type** – necessario per sistemi che supportano tipi diversi
- **Location** – pointer alla locazione del file sul device
- **Size** – dimensione corrente
- **Protection** – chi può fare reading, writing, executing
- **Time, date, and user identification** – dati per protection, security e usage monitoring (creazione, modifica, uso)

Diverse variazione ed extensioni

Su disco viene mantenuto un indice del file (**inode** in Uninx/Linux) con i metadata del file
- non il nome del file delegato alle directory entries

---

## Pagina 5

Operazioni File

□ File è un tipo di dato astratto
□ Occorre definire il tipo di operazioni (associate a system call)

□ Create – creazione del file
□ Open($F_i$) – cerca il file su disco con nome $F_i$, controlla i permessi, restituisce un riferimento per le altre operazioni
□ Close ($F_i$) – chiude il file
□ Write – per la scrittura mantiene un write pointer
□ Read – mantiene un read pointer
□ Reposition within file - seek
□ Delete – cancellazione del file
□ Truncate – cancellazione del contenuto del file mantenendo gli attribute (size diventa zero)

---

## Pagina 6

Open File

□ Per evitare di scorrere ogni volta il File System si apre il file prima di usare altre operazioni (non create e delate)

□ Con open si mantengono in memoria principale le info sul file aperto

□ Open-File Table: SO traccia tutti file aperti, i processi hanno info sui loro file aperti (due tabelle, una per-processo e una di sistema)

▶ Entry nella tabella per-processo
  – File descriptor: numero intero indice nella tabella dei file aperti per processo assegnato quando il file viene aperto
  – Punta alla entry dei file aperti nella tabella di sistema

▶ Ently nella tabella di sistema:
  – Descrive come viene aperto il file e dove sta leggendo/scrivendo un processo
  – Punta al File Control Block

□ File Control Block (FBC):
  ▶ Contiene i metadati dei file
    – Attributi del file
    – Locazione del file su disco: informazione per l’accesso diretto al file, senza dover cercare attraverso le directory

---

## Pagina 7

Strutture del File System

Strutture del file system in memoria (Linux)

FCB

process table
open file table
active i-node
file status flag
current offset
active i-node ptr

process table
open file table
active i-node
file status flag
current offset
active i-node ptr

process table
open file table
active i-node
file status flag
current offset
active i-node ptr

---

## Pagina 8

Strutture del File System

Strutture del file system in memoria (linux)

---

## Pagina 9

Tipo di File, Nomi, Estensioni

| file type | usual extension | function |
| :--- | :--- | :--- |
| executable | exe, com, bin or none | ready-to-run machine-language program |
| object | obj, o | compiled, machine language, not linked |
| source code | c, cc, java, pas, asm, a | source code in various languages |
| batch | bat, sh | commands to the command interpreter |
| text | txt, doc | textual data, documents |
| word processor | wp, tex, rtf, doc | various word-processor formats |
| library | lib, a, so, dll | libraries of routines for programmers |
| print or view | ps, pdf, jpg | ASCII or binary file in a format for printing or viewing |
| archive | arc, zip, tar | related files grouped into one file, sometimes compressed, for archiving or storage |
| multimedia | mpeg, mov, rm, mp3, avi | binary file containing audio or A/V information |

---

## Pagina 10

Open File Locking

□ Fornito da alcuni SO e file system
  □ Simile a read-write locks
  □ **Shared lock** simile a reader lock – molti processi possono acquisire concorrentemente
  □ **Exclusive lock** simile a writer lock

□ In generale sul write(fd, data, n) ci può essere race condition, va gentita dal processo

□ Es.  fd = open("shared.txt", O_WRONLY | O_APPEND);

  flock(fd, LOCK_EX);

  write(fd, "AAA\n", 4);

  flock(fd, LOCK_UN);

  Il file locking è molto più costoso di un mutex:
    - system call
    - attraverso kernel
    - gestione VFS/file system

  un mutex tra thread:
    - quasi tutto user-space
    - molto veloce

---

## Pagina 11

Open File Locking

□ Fornito da alcuni SO e file system
  □ Simile a read-write locks
  □ Shared lock simile a reader lock – molti processi possono acquisire concorrentemente
  □ Exclusive lock simile a writer lock

□ In generale sul write(fd, data, n) ci può essere race condition, va gentita dal processo

□ Es. Syscall fcntl(fd, comando, argomento) (file control), write lock, read lock

```c
struct flock lock = {
  .l_type = F_WRLCK,
  .l_whence = SEEK_SET,
  .l_start = 0,
  .l_len = 0
};
fcntl(fd, F_SETLKW, &lock);

struct flock lock = {
  .l_type = F_RDLCK,
  .l_whence = SEEK_SET,
  .l_start = 0,
  .l_len = 0
};
fcntl(fd, F_SETLKW, &lock);
```

---

## Pagina 12

Struttura dei File

□ Se si assumono diverse strutture di file, ogni tipo richiede algoritmi diversi

□ Struttura minimale (UNIX/Linux)

□ UNIX/Linux – sequenza lineare di bytes (programmi gestiscono da soli)
  □ Ogni byte del file viene indirizzato con offset,
  □ Ogni blocco logico è 1 byte che è contenuto su un blocco del disco

□ I file si definiscono in blocchi logici, ma si mappano su blocchi del disco
  □ Se file di 1949 byte con blocchi di 512 byte su disco, si allocano 4 blocchi, cioè 2048 byte con spreco di 99 (frammentazione interna)

□ Il file system Linux/Unix poi distingue diversi tipi di file: ordinari, directory, speciali, link, etc. (tutti di base sono sequenze lineari di byte)

---

## Pagina 13

Metodi di Accesso

- Diverse possono essere le modalità di accesso di un file
- Accesso sequenziale (modello del nastro)
  - read next
  - write next
  - reset
- Funziona sia su dispositivi ad accesso sequenziale, sia random

---

## Pagina 14

Metodi di Accesso

□ Diverse possono essere le modalità di accesso di un file
□ Accesso sequenziale
  read next
  write next
  reset

□ Accesso diretto (relativo) – modello disco
file è assunto di lunghezza fissata composto di logical records
  read n
  write n
  position to n
    read next
    write next
  rewrite n
  n = numero di blocco relativo

---

## Pagina 15

Simulazione di accesso sequenziale su Direct-access File

- Diverse possono essere le modalità di accesso di un file
- Accesso sequenziale simulato con l’accesso diretto

| sequential access | implementation for direct access |
| :--- | :--- |
| reset | cp = 0; |
| read next | read cp; cp = cp + 1; |
| write next | write cp; cp = cp + 1; |

---

## Pagina 16

Altri Metodi di Accesso

- Con accesso diretto si possono definire altri metodi di accesso

- Creazione di indici per i file
  - Mantiene indici in memoria per un veloce determinazione della locazione dei blocchi da processare (puntatori ai blocchi)
  - Prima cerca indice, poi blocco, poi record
  - Ricerca veloce per file grandi senza troppi accessi
  - Se troppo grande, indice (in memoria) dell’indice (su disco)

---

## Pagina 17

Struttura della Directory

- Le directory possono essere viste come tavole dei simboli per tradurre i nomi dei file nei loro file control block
- Una collezione di nodi contenente informazione su tutti i file

Directory

Files

F 1
F 2
F 3
F 4
F n

La directory structure e il files residente su disco

---

## Pagina 18

Operazioni su Directory

- Le directory possono essere viste come tavole dei simboli per tradurre i nomi dei file nei loro file control block

- La directory devono permettere diverse operazioni:
  - Ricerca di un file
  - Creazione di un file
  - Cancellazione di file
  - Lista del contenuto di una directory
  - Rename di un file
  - Spostamenti sul file system

---

## Pagina 19

Organizzazione Directory

La struttura delle directory può essere organizzata logicamente per ottenere

□ **Efficienza** – locazione veloce dei file

□ **Naming** – utile per gli utenti
  □ Due utenti possono avere stesso nome per file differenti
  □ Lo stesso file con nomi differenti

□ **Grouping** – raggruppamento logico di files per proprietà, (e.g., tutti i programmi Java, tutti i game, etc. …)

---

## Pagina 20

Single-Level Directory

□ Una singola directory per tutti gli utenti

□ Problema del naming
□ Problema del Grouping

---

## Pagina 21

Two-Level Directory

- Directory separate per ogni user

- Path name
- Si può avere lo stesso nome di file name per utenti differenti
- Ricerca efficiente
- Non si può fare grouping

---

## Pagina 22

Tree-Structured Directory

root
- spell
- bin
- programs

stat
- mail
- dist

find
- count
- hex
- reorder

p
- e
- mail

prog
- copy
- prt
- exp

reorder
- list
- find

hex
- count

list
- obj
- spell
- all
- last
- first

---

## Pagina 23

Tree-Structured Directory

- Ricerca efficiente
- Capacità di grouping
- Directory attuale (working directory)
  - cd /spell/mail/prog
  - type list

---

## Pagina 24

Tree-Structured Directories

- path name *assoluti* o *relativi*
- Creazione di un nuovo file fatta nella directory corrente
- Cancellazione di file
  - rm <file-name>
- Creazione di una nuova subdirectory è fatto nella directory corrente
  - mkdir <dir-name>
  Esempio: se la directory corrente è `/mail`
  - mkdir count

Cancellando “mail” $\Rightarrow$ si cancella l’intero subtree con radice in “mail”

Accesso di utenti nelle directory di altri consentita

---

## Pagina 25

Acyclic-Graph Directory

Ha sub-directory e file condivisi

---

## Pagina 26

Acyclic-Graph Directory

□ Due nomi differenti (aliasing)

□ Nuovo tipo di entry per directory
  □ Link – un altro nome (pointer) ad un file esistente
  □ Risolvere il link – segue il pointer per localizzare il file

□ Se si cancellano i file subito ⇒ dangling pointer per i link
  □ Se si mantengono accesso a file non esistenti possibili problemi
    ► Per link simbolici si lasciano i link rotti e SO si accorge del problema
  □ Si possono cercare tutti i link associati ad un file ed eliminarli
    ► Occorre memorizzare per ogni file i riferimenti al file, costoso
  □ Soluzione con contatore
    ► Si contano i link per file, quando il contatore va a zero si può concellare il file

---

## Pagina 27

General Graph Directory

---

## Pagina 28

General Graph Directory

Se cicli la situazione è più complessa
- Ogni ciclo è un nuovo riferimento allo stesso file
- Ricerca di un file che non termina
- Per cancellazione contatore può non essere zero anche se tutti i link cacellati per conteggio di auto-riferimenti

Come garantiamo che non si hanno cicli?

- Garbage collection
  - Scansione del file system per verificare l’accessibilità, tutto quello che non è accessible diventa free
  - Costoso

- Mantenere stuttura aciclica
  - Ogni volta che un nuovo link è aggiunto usa un algoritmo di cycle detection per determinare se è OK
  - Costoso, si evita il ciclo

- Ignorare/bypassare i link a directory durante le operazioni
  - Problematici soprattutti i link simbolici

---

## Pagina 29

File System UNIX: Caratteristiche

- Struttura gerarchica
- Files senza struttura (byte streams)
- Protezione da accessi non autorizzati
- Semplicità di struttura

"On a UNIX system, everything is a file; if something is not a file, it is a process."

---

## Pagina 30

File Unix

I tipi principali di File sono:

- File ordinari
- Directory
- File Speciali

Il sistema assegna biunivocamente a ciascun file un identificatore numerico, detto

i-number ("index-number"), che gli permette di rintracciarlo nel file system.

---

## Pagina 31

File Ordinari

- Sono sequenze di byte (byte streams)
- Possono contenere informazioni qualsiasi (dati, programmi sorgente, programmi oggetto,...)
- Il sistema non impone alcuna struttura

| R | O | M | A | eoln | M |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |
| text file | | | | | |
| 00110101 | 01000000 | 11111111 | 01110111 | 11110000 | binary file |

---

## Pagina 32

Organizzazione dei File in UNIX

Per consentire all’utente di rintracciare facilmente i propri files, Unix permette di raggrupparli in cartelle, dette **Directories**, organizzate in una (unica) struttura gerarchica:

- : directory
- : file ordinario directory (vuota) file speciale

---

## Pagina 33

Directories in Unix

- Sono sequenze di bytes come i file ordinari;
- Differiscono dai file ordinari solo perché non possono essere scritte da programmi ordinari
- Il loro contenuto è una serie di directory entries: associazione fra gli i-number (usati dal sistema) e i filename mnemonici (usati dall'utente):

![Diagram of directory entries in Unix](image)

In System V (SV), in Linux ext3 solitamente i-num 4 byte e filename fino a 255 byte

---

## Pagina 34

Esempio

Almeno due entry: la directory stessa “.”, la directory padre “..”

---

## Pagina 35

Files Sinonimi in UNIX

Un file può avere più filename (ma sempre un solo i-number)

Esempio:

Il file 107 ha 3 links

---

## Pagina 36

Il comando “link”: In

In name1 name2 "link"

associa il nuovo nome (link) name2 al file (esistente) name1, che non può essere una directory

---

## Pagina 37

Numero links in UNIX

- Numero links e’ un attributo gestito dal sistema

Per vedere:
Is -l

---

## Pagina 38

Pathnames

Ogni file viene identificato univocamente specificando il suo **pathname**, che individua il cammino dalla root-directory al file:

```text
/dir/dir/.../dir/filename
root separatori
bin etc usr dev
mario roberto prog
/prog/a
/usr/mario/prog
/usr/roberto/prog/a
```

---

## Pagina 39

Link Simbolici

- In -s name1 name2
- Permette di creare link a directory;
- Permette di creare link fra file o directory che stanno su file system diversi;
- Viene creato un file name2 che contiene il link simbolico (i.e. il path di name1)

---

## Pagina 40

Tipiche Directories in Linux

- /bin: comandi eseguibili
- /dev: file speciali (I/O devices)
- /etc: file per l’amministrazione del sistema, ad esempio: /etc/passwd
- /lib: librerie di programmi
- /tmp: area temporanea usata dal sistema
- /home: home directories
- /usr: Programmi, librerie, doc. etc. per i programmi user-related.

---

## Pagina 41

Tipi di File

- File regolari
- Directory file
- Link file
- Character special file
- Block special file
- Socket file
- Named pipe file

---

## Pagina 42

Files Speciali: vantaggi

- Trattamento uniforme di files e devices
- In Unix i programmi non sanno se operano su un file o su un device

Diagram showing the UNIX File System with components such as Dischi, Stampanti, Nastri, Terminali, Linee di comunicazione, and Pipes. The UNIX File System is connected to the Comandi UNIX and Programmi utente via a stessa interfaccia per ogni tipo di file.

---

## Pagina 43

Implementazione File

Directory
PIPPC 102

102
attributi del file

Blocchi dati del file

Tabella dei descrittori dei file (i-node)

---

## Pagina 44

Attributi di un File in UNIX

Per ogni file (ordinario, directory, speciale) Unix mantiene le seguenti informazioni nel descrittore del file:

| Tipo | ordinario, directory, speciale? |
| :--- | :--- |
| Posizione | dove si trova? |
| Dimensione | quanto è grande? |
| Numero di links | quanti nomi ha? |
| Proprietario | chi lo possiede? |
| Permessi | chi può usarlo e come? |
| Creazione | quando è stato creato? |
| Modifica | quando è stato modificato più di recente? |
| Accesso | quando è stato l'accesso più recente? |

---

## Pagina 45

Linux File System

- Inode
- Directory entry
- Block addresses

Figure 1: Relationship between the directory entry, an inode, and blocks of an allocated file.

---

## Pagina 46

Protezioni

- I possessori/creatori di File devono controllare:
  - Cosa può essere fatti
  - Da chi

- Tipi di accesso
  - Read
  - Write
  - Execute
  - Append
  - Delete
  - List

---

## Pagina 47

Accessi a Liste e Gruppi

Lista di accessi:
- Per ogni file e directory mantieni una lista di utenti abilitati
- La tecnica non è efficiente (lunghe liste da mantenere con utenti variabili)
- Versione condensata con gruppi di utenti

Modelli di accesso: read, write, execute

Tre classi di utenti in Unix / Linux

a) **owner access** 7 ⇒ RWX
b) **group access** 6 ⇒ RWX
c) **public access** 1 ⇒ RWX

Chiedi al manager di creare un gruppo (nome unico), diciamo G, e aggiungi qualche utente al gruppo

Per un file particolare (es., *game*) o subdirectory si definisce un accesso appropriato (es., Solaris)

---

## Pagina 48

Accessi a Liste e Gruppi

□ Modelli di accesso: read, write, execute
□ Tre classi di utenti in Unix / Linux

a) **owner access** 7 ⇒ RWX
b) **group access** 6 ⇒ RWX
c) **public access** 1 ⇒ RWX

□ Chiedi al manager di creare un gruppo (nome unico), diciamo G, e aggiungi qualche utente al gruppo.

□ Per un file particolare (es., *game*) o subdirectory si definisce un accesso appropriato.

Attacca un gruppo ad un file
chgrp G game

---

## Pagina 49

Esempio UNIX Directory Listing

-rw-rw-r-- 1 pbg staff 31200 Sep 3 08:30 intro.ps
drwx----- 5 pbg staff 512 Jul 8 09.33 private/
drwxrwxr-x 2 pbg staff 512 Jul 8 09:35 doc/
drwxrwx--- 2 pbg student 512 Aug 3 14:13 student-proj/
-rw-r--r-- 1 pbg staff 9423 Feb 24 2003 program.c
-rwxr-xr-x 1 pbg staff 20471 Feb 24 2003 program
drwx--x--x 4 pbg faculty 512 Jul 31 10:31 lib/
drwx----- 3 pbg staff 1024 Aug 29 06:52 mail/
drwxrwxrwx 3 pbg staff 512 Jul 8 09:35 test/

Primo campo protezione di file o directory. La d indica directory, - indica file regolare. Indicato poi il numero di link, il proprietario (owner), il gruppo (group), il size in bytes, la date di ultima modifica modification, quindi il file name (con estenzione opzionale).

---

## Pagina 50

Protezioni di un File in UNIX

A ciascun file (normale, speciale, directory) sono associati alcuni attributi:

- **Proprietario (owner):** l'utente che ha creato il file
- **Gruppo (group):** il gruppo a cui il proprietario appartiene
- **Permessi (permissions)** Il tipo di operazioni che il proprietario, i membri del suo gruppo o gli altri utenti possono compiere sul file

Proprietario, gruppo e permessi iniziali sono assegnati dal sistema al file al momento della sua creazione.

Il proprietario può successivamente modificare tali attributi con appositi comandi (chown, chgrp, chmod)

---

## Pagina 51

Identificazione Utenti

- Ogni utente viene identificato da uno **user name** assegnato dall'amministratore del sistema. Adesso corrisponde biunivocamente uno **userid** numerico, assegnato dal sistema
- **User name** e user-id sono pubblici

---

## Pagina 52

GRUPPI

Ogni utente può far parte di uno o più gruppi, definiti dall'amministratore del sistema

Ogni gruppo è identificato da un group name di al più 8 caratteri, associato biunivocamente a un group-id numerico

Esempio:

---

## Pagina 53

Metodi di Allocazione

Lo storage ad accesso diretto permette di implementare diversi metodo di allocazione di file

- Un metodo di allocazione è il modo in cui i blocchi sono allocati per i file
- Criteri:
  - Spazio: memoria utilizzata in modo efficiente
  - Tempo: accesso veloce

Tre metodi principali:
- Allocazione contigua
- Allocazione lincata
- Allocazione indicizzata

---

## Pagina 54

Metodi di Allocazione - Contigua

☐ Allocazione Contigua – ogni file occupa un insieme di blocchi contigui

□ Miglior performance in molti casi
□ Semplice
  ► richiesta locazione di partenza (numero del blocco) e lunghezza (numero di blocchi)
□ Pro:
  ► spostamenti della testina richiesti per accedere a tutti i blocchi di un file è trascurabile
  ► Semplice anche l’accesso diretto
□ Contro:
  ► Trovare spazio per il file (buchi)
  ► Sapere a priori la dimensione del file
  ► Frammentazione esterna
  ► Necessità di compattare
    – off-line è downtime
    – on-line è lento
□ Allocazione contigua estesa
  ► Aree contigue collegate (base, numero blocchi, base ext, numero blocchi ext)

---

## Pagina 55

Allocazione Contigua

- Mapping da logica a blocchi
- Logical Address/Block

$$\begin{array}{c}
\text{LA/512} \\
\text{R}
\end{array}$$

Blocco da accedere = Q + indirizzo di inizio
Dislocazione nel blocco = R

---

## Pagina 56

Metodi di Allocazione - Contigua

Pro: l’accesso ai file può essere eseguito semplicemente sia in modo sequenziale che diretto (meno veloce)

Contro 1: è necessario trovare lo spazio libero per allocare il file

Diversi algoritmi
- First-fit: primo buco abbastanza grande
- Best-fit: il buco che approssima meglio la dimensione (per eccesso)

Si presenta il problema della frammentazione esterna
- Può essere risolta tramite la compattazione
- Si spostano i dati su un altro disco
- Si crea una una zona contigua di spazi libero
- Si riportano i file su disco originale allogandoli in modo contiguo
- La compattazione richiede molto tempo e può essere fatta
  - Off line: non è possibile usare il volume
  - On line: peggiora le prestazioni

---

## Pagina 57

Metodi di Allocazione - Contigua

Pro: l’accesso ai file può essere eseguito semplicemente sia in modo sequenziale che diretto (meno veloce)

Contro 2: è necessario stimare quanto spazio allocare ad un file

- Quando un file finisce lo spazio disponibile
  - Il processo può essere interrotto
  - Il file può essere spostato in una zona di memoria più grande

- Allocare più spazio di quello inizialmente necessario può portare alla frammentazione interna
  - Specialmente nel caso di file che crescono lentamente

- Alcuni sistemi usano l’allocazione contigua estesa
  - Quando un file necessita di spazio gli viene assegnata una seconda area contigua
  - Ogni area è caratterizzata da: blocco d’inizio, numero blocchi, area successiva
    - base, numero blocchi, base ext, numero blocchi ext

---

## Pagina 58

Sistema basato su Allocazione Estesa

- File system più moderni (i.e., Veritas File System) usano uno schema di allocazione contiguo modificato
- Extent-based file system allocano blocchi di disco in locazioni contigue estese

- Un extent è un blocco contiguo di memoria
  - Extents sono allocati per allocazione di file
  - Un file consiste di uno o più estensioni
    - Prima viene allocato un chunk, poi vengono aggiunti altri
    - base, numero blocchi, base ext, numero blocchi ext

---

## Pagina 59

Metodi di Allocazione - Concatenata

☐ Allocazione Concatenata – ogni file è una lista linkata di blocchi

☐ Ogni blocco contiene un pointer al prossimo blocco
  ► File finisce al nil pointer

☐ La directory memorizza per ogni file
  ► Puntatore al primo e ultimo blocco

Il puntatore non è visibile all’utente, quindi lo spazio per l’utente è ridotto:
- Blocco da 512 Byte
- puntatore da 4 Byte
- Spazio utile: 508 Byte

---

## Pagina 60

Allocazione Concatenata

Ogni file è una lista concatenata di blocchi del disco: i blocchi possono essere sparsi ovunque su disco

$$\text{block} = \text{pointer}$$

Il puntatore non è visibile all’utente, quindi “prende” spazio:
- Blocco da 512 Byte
- puntatore da 4 Byte
- Spazio utile: 508 Byte
- 0.78% disco usato da puntatore

Per accesso si fa riferimento al Q-esimo blocco nella lista concatenate che rappresenta il file, quindi si accede riferimento al record nel blocco

---

## Pagina 61

Allocazione Concatenata

□ Creazione di un file:
  □ Si aggiunge un elemento alla directory con Puntatore al primo blocco settato a null dimensione pari a 0

□ Scrittura di un file:
  □ Si cerca un blocco libero e si effettua la scrittura dei dati
  □ Lo si concatena all’ultimo blocco del file (se presente)
  □ Si aggiornano i puntatori della directory all’ultimo e al primo blocco (nel caso il file sia ancora vuoto)

□ Lettura di un file:
  □ Si scorrono in sequenza i blocchi seguendo la concatenazione

---

## Pagina 62

Metodi di Allocazione - Concatenata

□ L’allocazione concatenata risolve i problemi dell’allocazione contigua:
  □ Non c’è frammentazione esterna, non serve la compattazione
  □ Non è necessario conoscere la dimensione del file al momento della creazione

□ Problemi:
  □ È efficiente solo per l’accesso sequenziale (a causa dei puntatori)
  □ Richiede più spostamenti della testina
  □ I puntatori consumano spazio
    ► Una soluzione è quella di allocare cluster di blocchi anziché singoli blocchi
    ► Meno spazio sprecato per i puntatori, meno spostamenti della testina
    ► Aumenta però la frammentazione interna
  □ Perdita o danneggiamento di un puntatore
    ► Potrebbe puntare ad un blocco vuoto o un blocco di un altro file
    ► Possibile soluzione: liste doppiamente concatenate

---

## Pagina 63

File-Allocation Table

Variante importante della lincata è FAT (File Allocation Table) - MSDOS

- Nella prima parte del disco si istanzia un tabella
  - Contenente tanti elementi quanti sono i blocchi
  - Ordinata in base al numero del blocco
- La directory contiene per ogni file il puntatore al suo primo elemento nella FAT
- Seguendo i puntatori nella FAT si ricavano gli indici dei blocchi fisici di un file

---

## Pagina 64

File-Allocation Table

directory entry
test 217
name start block

0
217 618
339
618 339
no. of disk blocks -1
FAT

---

## Pagina 65

File-Allocation Table

Variante importante è FAT (File Allocation Table)

- Nella prima parte del disco si istanzia un tabella
  - Contenente tanti elementi quanti sono i blocchi
  - Ordinata in base al numero del blocco

- La directory contiene per ogni file il puntatore al suo primo elemento nella FAT
  - Ogni elemento ha un numero di blocco ed è concatenato al blocco successivo nel file
  - L’ultimo elemento contiene un valore end of file
  - L’elemento di un blocco che non è associato a nessun file contiene uno 0

- Seguendo i puntatori nella FAT si ricavano gli indici dei blocchi fisici di un file

---

## Pagina 66

File-Allocation Table

Variante importante è FAT (File Allocation Table)

---

## Pagina 67

File-Allocation Table

□ Variante importante è FAT (File Allocation Table)
□ Per essere efficiente la FAT richiede l’uso di una cache
  □ Altrimenti la testina del disco deve continuamente spostarsi tra l’inizio del disco e la locazione del blocco successivo
□ Migliora le prestazioni nel caso di accesso diretto
  □ La testina del disco scandisce la FAT e poi si fa uno spostamento grande per accedere al blocco voluto
□ La differenza fra FAT12, FAT16 e FAT32 consiste in quanti bit sono allocati per numerare i blocchi del disco
  □ Con 12 bit, il file system può indirizzare al massimo 2^12 = 4096 blocchi, mentre con 32 bit si possono gestire 2^32 = 4.294.967.296 blocchi
  □ L'aumento del numero di bit di indirizzo dei blocchi e la dimensione stessa del blocco sono stati resi necessari per gestire unità a disco sempre più grandi e capienti

---

## Pagina 68

File-Allocation Table

□ Variante importante è FAT (File Allocation Table)
□ Dimensione del blocco e FAT influenza la dimensione massima della partizione

| Block size | FAT-12 | FAT-16 | FAT-32 |
| :--- | :--- | :--- | :--- |
| 0.5 KB | 2 MB | | |
| 1 KB | 4 MB | | |
| 2 KB | 8 MB | 128 MB | |
| 4 KB | 16 MB | 256 MB | 1 TB |
| 8 KB | | 512 MB | 2 TB |
| 16 KB | | 1024 MB | 2 TB |
| 32 KB | | 2048 MB | 2 TB |

---

## Pagina 69

Metodi di Allocazione - Indicizzata

☐ Allocazione indicizzata

☐ Ogni file possiede un indice dei blocchi memorizzato in un blocco indice
  ► Questo blocco contiene un array di puntatori agli altri blocchi del file
  ► L’i-simo elemento dell’array punta all’i-simo blocco del file

☐ La directory memorizza per ogni file un puntatore al suo blocco indice

☐ Questo risolve il problema dell’accesso diretto presente nell’allocazione concatenata ed evita la frammentazione esterna

index table

---

## Pagina 70

Esempio di Allocazione Indicizzata

- Ogni file possiede un indice dei blocchi memorizzato in un blocco indice
  - Questo blocco contiene un array di puntatori agli altri blocchi del file
  - L’i-simo elemento dell’array punta all’i-simo blocco del file
- La directory memorizza per ogni file un puntatore al suo blocco indice

![Directory diagram](image_link)

---

## Pagina 71

Allocazione Indicizzata

- Creazione di un file:
  - Si crea un blocco indice con tutti gli elementi settati a null
  - Si aggiunge un elemento alla directory con puntatore ad un blocco indice

- Scrittura di un file:
  - Si cerca un blocco libero e si effettua la scrittura dei dati
  - Si aggiorna il blocco indice

- Lettura di un file:
  - si scorrono in sequenza i blocchi seguendo l’array dell’indice

---

## Pagina 72

Allocazione Indicizzata

Problema:
□ l’indice richiede l’uso di un intero blocco, quindi nel caso di un file piccolo si ha frammentazione interna

□ Si dovrebbero usare blocchi piccoli in modo da ridurre la frammentazione
□ Problemi con i file grandi
□ Diverse soluzioni

---

## Pagina 73

Allocazione Indicizzata

Soluzioni:

- Schema concatenato: si usano blocchi piccoli e nel caso di file grandi l’indice è composto da più blocchi concatenati

---

## Pagina 74

Allocazione Indicizzata

Soluzioni:

- Schema a più livelli: si ha un indice di primo livello che punta ad un insieme di indici di secondo livello, i quali puntano ai blocchi del file
- Con blocchi da 4 KByte e puntatori da 4 byte si hanno 1024 puntatori; con 2 livelli 2^20 puntatori, quindi si possono indicizzare file da 4GB (4 x 2^10 x 2^20)
- È possibile estendere lo schema a 3-4 livelli

---

## Pagina 75

Allocazione indicizzata – Mapping

outer-index

index table

file

---

## Pagina 76

Schema Combinato: UNIX UFS

Schema combinato: usato nei sistemi Unix:
- II FCB contiene 15 elementi per indicizzare i file
- I primi 12 sono puntatore diretti a dei blocchi
- II 13° punta ad un blocco contenente un indice
- II 14° punta ad un indice a due livelli
- II 15° punta ad un indice a tre livelli

---

## Pagina 77

Schema Combinato: UNIX UFS

Assumendo indirizzi a 32-bit

Con questo metodo più blocchi indicizzati di quanti possono essere indirizzati con puntatori di file a 32-bit

---

## Pagina 78

Scelta Metodo Allocazione

La scelta del metodo di allocazione deve considerare due fattori:
- Efficienza di memorizzazione
- Tempo di accesso ai dati

La scelta è influenzata dalla modalità di accesso al file
- L’allocazione contigua richiede un solo accesso al disco qualsiasi sia il tipo di accesso (sequenziale o diretto)
  - Anche con l’accesso diretto, noto l’indirizzo del primo blocco fisico e l’indirizzo del blocco logico desiderato, è possibile calcolare l’indirizzo fisico di accesso
- L’allocazione concatenata invece è efficiente per l’accesso sequenziale, ma non per quello diretto
  - Accesso all’i-esimo blocco porta all’accesso di i blocchi intermedi

---

## Pagina 79

Scelta Metodo Allocazione

Per questo motivo alcuni sistemi gestiscono
- File ad accesso sequenziale con allocazione concatenata
- File ad accesso random con l’allocazione contigua
  - È necessario specificare l’uso del file a tempo di creazione
  - Si dichiara anche la dimensione massima del file
  - È sempre possibile convertire il formato del file
- Le prestazione dell’allocazione indicizzata invece dipendono
  - Dalla profondità dell’indice (quanti blocchi indice)
  - Dalla dimensione del file (se grande occorre scorrere molti blocchi indice)
  - Occorre in memoria principale il blocco indice per essere efficienti

Alcuni sistemi usano
- Allocazione contigua per file piccoli (più comuni)
- Allocazione indicizzata per file grandi

Altre ottimizzazione per ridurre i tempi di seek, ma solo per HDD, non per NVM

---

## Pagina 80

Gestione dello Spazio Libero

- Trovare in modo veloce un insieme di blocchi da allocare ad un file
  - Tener traccia dei blocchi non allocati
  - Lista dello spazio libero (non necessariamente implementata come lista)

- Creazione di un file:
  - Si cerca nella lista il numero di blocchi necessari
  - Si allocano al file
  - Si rimuovono dalla lista

- Eliminazione di un file
  - I blocchi associati al file vengono deallocati
  - Si aggiungono alla lista

---

## Pagina 81

Gestione dello Spazio Libero

Diverse possibili implementazioni:
- Vettore di bit
- Lista concatenata
- Raggruppamento
- Conteggio

---

## Pagina 82

Vettore di Bit o BitMap

□ Si memorizza un array di lunghezza pari al numero dei blocchi
□ Il valore delle celle indica la disponibilità di un blocco
  □ 1 libera
  □ 0 occupata
□ Per creare un file
  □ Ricerca del primo bit a 1 (allocazione concatenata o indicizzata)
  □ Ricerca di un blocco di bit a 1 sufficientemente grande (allocazione contigua)

□ Pro: semplice ed efficiente
□ Contro:
  □ Per essere efficiente deve però essere mantenuta in memoria centrale
  □ Dischi grandi richiedono vettori di bit molto grandi

---

## Pagina 83

Vettore di Bit

Bit map richiede spazio extra
Esempi:
disk size = 1.3 GB
block size = 512 byte
bitmap = 332 KB
se cluster di 4 -> 83 KB

block size = 4KB = $2^{12}$ bytes
disk size = $2^{40}$ bytes (1 terabyte)
$n = 2^{40}/2^{12} = 2^{28}$ bits (o 32MB)
se cluster di 4 blocchi -> 8MB of memory

Dischi aumentano di dimensioni quindi aumenta il problema

---

## Pagina 84

Lista Concatenata

- Si memorizza in memoria centrale un puntatore al primo blocco libero
- Ogni blocco libero viene poi concatenato al successivo
- Contro: è poco efficiente in quanto scorrere l’intera lista richiede molti accessi alla memoria
- Fortunatamente lo scorrimento della lista è un evento raro
- II SO si limita a cercare il primo blocco libero per allocarlo ad un file
- Allocato il blocco si aggiorna il puntatore al primo blocco libero in memoria centrale
- FAT contiene link a blocchi liberi

---

## Pagina 85

Raggruppamento e Conteggio

Raggruppamento
- Modifica dell’approccio a free-list
- Il primo blocco contiene gli indirizzi di n blocchi liberi
  - Al primo accesso subito info sui blocchi liberi
- n-1 sono effettivamente liberi
- L’ultimo contiene a sua volta n indirizzi di blocchi liberi

Conteggio
- Sfrutta il fatto che tipicamente si ha più di un blocco contiguo libero
- Si usa un array in cui ogni elemento contiene
  - Indirizzo del primo blocco libero
  - Conteggio degli n blocchi contigui liberi

---

## Pagina 86

Linux File System

Evoluzione

Il file system EXT (Extended) sviluppato da Rémy Card e rilasciato in Linux nel 1992 per superare le limitazioni di Minix filesystem

- metadati basati su Unix filesystem (UFS) o Berkeley Fast File System (FFS)
- BSD FFS (Fast File System) introduce la località tra inode e dati (cylinder groups)
- Superato rapidamente da EXT2 filesystem

EXT2 organizza il disco in block groups contenenti metadati e dati

- L’organizzazione in block groups mantiene vicini inode e blocchi dati, riducendo la frammentazione e migliorando l’efficienza degli accessi.

---

## Pagina 87

Linux ext File System

ext2
- Organizzazione a block groups per migliorare la locality dei dati
- inode e blocchi dati vengono mantenuti vicini sul disco;

Ext2 on a disk consists of many groups of disk blocks (of the same size, located sequentially one after the other). Block groups reduce file fragmentation.

Source: https://computing.ece.vt.edu/~changwoo/ECE-LKP-2019F/l/lec21-fs.pdf

---

## Pagina 88

Linux File System

Evoluzione

□ Il file system EXT (Extended) sviluppato da Rémy Card e rilasciato in Linux nel 1992 per superare le limitazioni di Minix filesystem
  ▶ metadati basati su Unix filesystem (UFS) o Berkeley Fast File System (FFS)
  ▶ Superato rapidamente da EXT2 filesystem

□ Come Minix, EXT2 ha un boot sector nel primo settore del HDD su cui è installato
  ▶ Ha uno small boot record e una partition table
  ▶ block groups contengono metadati e dati, inode e blocchi restano vicini e gli accessi diventano più efficienti.

□ EXT3 ha il journal che dichiara le modifiche sul FS
  ▶ Per il resto è simile ad EXT2

□ EXT4 filesystem migliora le performance, leggibilità e capacità
  ▶ FS di dimensioni fino a 1 exbibyte e file di dimensioni fino a 16 tebibyte
  ▶ I file di grandi dimensioni vengono suddivisi in più estensioni
  ▶ Allocazione multiblocco
  ▶ Meno frammentazione
  ▶ Dimensione di inode più grande (256 byte)

---

## Pagina 89

File System NTFS

New Technology File System (sostituisce FAT)
- usa cluster come unità di allocazione del disco
- introduce metadati ricchi e journaling
- Basato su Master File Table (MFT)

Master File Table (MFT)
- contiene le informazioni sui file e sul filesystem
- una o più entry per ogni file
- include anche file speciali:
  - log/journal
  - bitmap spazio libero
  - root directory
  - boot metadata

---

## Pagina 90

Efficienza e Prestazioni

□ I dischi sono tipicamente conosciuti come il collo di bottiglia di ogni sistema
  □ A causa della loro velocità di accesso
  □ Anche NVM sono lente rispetto a CPU

□ Gli algoritmi di allocazione dei blocchi e gestione delle directory devono essere scelti con cura al fine di ottimizzare
  □ Efficienza nell’uso dei dischi
  □ Prestazioni

---

## Pagina 91

Efficienza

Diverse scelte influenzano l’efficienza del disco

Allocazione dei FCB:
- alcuni SO, es.Unix, allocano preventivamente i FCB e li distribuiscono nel file system
- Anche un disco senza file ha una certa quantità di spazio occupata dai FCB
- Questa scelta può migliorare le prestazioni del file system

Scelta degli attributi da memorizzare per ogni file:
- Salvare le date di accesso ai file può essere utile per fornire informazioni all’utente
- Tuttavia questo richiede due accessi al disco ogni volta che si legge un file
- Uno in lettura e uno in scrittura per modificare la directory
- Gli attributi da memorizzare vanno scelti con cura

Lunghezza dei puntatori per accedere ai dati:
- Più bit si usano per i puntatori più grandi possono essere i file (32 è bit 2^32=4GB)
- Tuttavia puntatori grandi richiedono più spazio per eseguire gli algoritmi di allocazione e gestione dello spazio libero (è spazio non usabile dall’utente)

---

## Pagina 92

Prestazioni

- Una volta scelti gli algoritmi per la gestione del file system si possono adottare diverse tecniche per migliorare le prestazioni

- Cache del disco (buffer cache): area riservata della memoria centrale dove vengono mantenuti i blocchi usati di recente
  - … che probabilmente verranno riusati a breve
  - memoria fisica (non virtualizzata) riservata al Kernel

- Cache delle pagine: area riservata della memoria centrale (kernel) per la gestione ottimizzata dell’accesso ai file tramite pagine
  - memoria virtuale non solo per la gestione dei processi, ma anche per l’accesso ai file (più veloce)
  - Utile per gestire in modo efficiente l’accesso ai file (memoria virtuale unificata)

---

## Pagina 93

Page Cache vs Buffer Cache

- Accesso in memoria sia tramite le chiamate di sistema read() e write() sia con file mapping
- Se non si usa la cache unificata
- Le chiamata di sistema usano direttamente la buffer cache (FS cache)
- Il sistema di memoria virtuale non può interfacciarsi direttamente con la buffer cache
- È necessario copiare nella cache delle pagine il contenuto del file presente nella buffer cache
- Fenomeno del double caching: doppio passaggio di cache
- Spreco di memoria, CPU e I/O
- Possibili inconsistenze

---

## Pagina 94

Buffer Cache Unificata

- Con la FS cache unificata il problema del double caching viene risolto
- Il sistema di memoria virtuale può interfacciarsi direttamente con la cache del file system

Diagram showing the flow of data between memory-mapped I/O, buffer cache, and file system.

---

## Pagina 95

Sostituzione Pagine

Accesso ai File e sostituzione pagine

- Il metodo di accesso al file influenza la scelta dell’algoritmo di sostituzione delle pagine
- In caso di accesso sequenziale LRU non è ottimale
  - la pagina più recente non è quella che sarà usata prima
- Rilascio indietro (free-behind):
  - Rimossa la pagina al riferimento alla pagina successiva (voltare pagina)
- Lettura anticipata (read-ahead):
  - Si copiano nella cache la pagina richiesta le successive
- Utilizzando queste tecniche si ha un notevole risparmio di tempo

---

## Pagina 96

Scritture di File

- Scritture sincrone e asincrone:
  - Influenzano le prestazioni di I/O
- Scrittura sincrona: le scritture su disco avvengono nell’ordine in cui il driver riceve le richieste
  - Il chiamante è bloccato fino a quando il dato non viene scritto
- Scritture asincrone: le scritture avvengono sulla cache del disco
  - Il driver del dispositivo si occupa poi di trasferire i dati sul disco
  - Il chiamante non resta bloccato
- Le scritture asincrone sono usate più frequentemente
  - Per i metadati le scritture posso essere sincrone per evitare problemi di consistenza

---

## Pagina 97

Recupero

- Operazioni eseguite molto frequentemente, come la creazione di un file, comportano molti cambiamenti nelle strutture dati del file system
  - Struttura della directory
  - Lista dello spazio libero
  - FCB

- Se un crollo del sistema avviene prima che tutte queste operazioni siano completate possono crearsi delle incoerenze

- Es., un nuovo FCB potrebbe essere stato allocato ma la struttura delle directory potrebbe non contenere il puntatore ad esso

- II SO adotta diverse tecniche per risolvere le incoerenze

---

## Pagina 98

Controllo di Consistenza

- Per scoprire eventuali errori è necessario analizzare i meta-dati
- Questo richiede molto tempo
  - Si analizzano solo i cambiamenti
  - Prima di modificare i meta-dati il SO mette un bit di modifica a 1
  - Se le modifiche terminano con successo il bit viene rimesso a 0
  - Se resta ad un 1 significa che c’è stato un crollo e al riavvio viene eseguito il verificatore della coerenza

- Consistency checker confronta i dati nelle directory e altri metadata con i dati memorizzati e prova a correggere:
  - Con l’allocazione concatenata i puntatori permettono di ricostruire un file
    - Si possono ricreare i file in una directory
  - Con allocazione indicizzazione grave la perdita della dir che punta all’indice
    - I blocchi infatti non contengono informazioni sugli altri blocchi del file
    - In scrittura si aggiornano le directory in modo sincrono (non sempre risolve)

---

## Pagina 99

Registrazione Modifiche (log)

La verifica della coerenza comporta alcuni problemi
- Non sempre le incoerenze sono risolvibili
- In alcuni casi la risoluzione richiede l’intervento umano
- Richiede molto tempo

Si adottano degli algoritmi usati nelle basi di dati
- Si mantiene un log dove salvare in modo sequenziale le modifiche ai metadati
  - log-based transaction-oriented file systems (journaling)
- Quando si opera su un file l’operazione è considerata committed quando
  - Tutte le modifiche da apportare ai meta-dati sono state salvate nel log (transazione)
- La chiamata di sistema restituisce il controllo all’utente
- SO si occupa di aggiornare in modo asincrono i meta-dati come indicato dal log
- Quando tutti i metadati sono stati aggiornati le modifiche vengono tolte dal log
  - Implementato come un buffer circolare (sovrascrive i vecchi valori)
- Usato NTFS, Veritas, UFS su Solaris, ext3, ext4, ZFS

---

## Pagina 100

Registrazione Modifiche (log)

- Se il sistema crolla, al momento del riavvio
  - Si analizza il log e si eseguono tutte le transazioni registrate
  - queste modifiche non erano ancora state fatte sui metadati

- Problema quando la transazione non è committed al momento del crash
  - Tutti i cambiamenti fatti al FS annullati per mantenere consistenza
    - unico ripristino necessario

- Il log è tipicamente salvato in un’area dedicata del disco
  - Accedere in modo sequenziale e sincrono al log per salvare le transazioni
    - È più veloce che accedere in modo diretto e sincrono ai blocchi contenenti i meta-dati

- Questa tecnica diminuisce il tempo in cui un processo resta bloccato in attesa dell’aggiornamento dei metadati

---

## Pagina 101

Registrazione Modifiche (log)

Quando si scrive sul journal

Molte write
↓
cache RAM
↓
journal transaction
↓
flush batchato

---

## Pagina 102

Journaling (Linux)

ext3/ext4 implements journaling, with file system updates first written to a log file in the form of transactions

Once in log file, considered committed

Over time, log file transactions replayed over file system to put changes in place

Journal is logically a fixed-size, circular array.

• Implemented as a special file with a hard-coded inode number.
• Each journal transaction is composed of a begin marker, log, and end marker.

Source: https://computing.ece.vt.edu/~changwoo/ECE-LKP-2019F/I/lec21-fs.pdf

---

## Pagina 103

Altri Metodi

- Un alternativa consiste nel non sovrascrivere i metadati (WAFL e Solaris ZFS)

- Quando è necessario aggiornarli
  - Si scrivono i nuovi valori in un nuovo blocco del disco
  - Si aggiorna il puntatore ai metadati
  - Si dealloca il blocco contenente i vecchi meta-dati

---

## Pagina 104

Backup e Recupero

- Le tecniche viste finora permettono di recuperare eventuali inconsistenze fra metadata e file
- Esistono anche delle tecniche che permettono di recuperare i file in caso di guasti irreparabili ai dischi (backup e ripristino)

- Il backup può essere
  - Assoluto: ogni volta si copia l’intero disco
  - Incrementale: la prima volta si copia l’intero disco, le volte successive solo i file modificati
    - Si basa sui valori degli attributi
    - Se data_ultima_modifica > data_backup è nuovo backup del file

- Il metodo di ripristino varia in base al tipo di backup

---

## Pagina 105

Backup e Recupero

□ Giorno 1. Copia in un mezzo di backup tutti i file del file system
  □ This is called a full backup.

□ Giorno 2. Copia su un altro mezzo tutti i file cambiati dal giorno 1.
  □ This is an incremental backup.

□ Giorno 3. Copia su altro mezzo tutti i file cambiati dal giorno 2.
  □ ..

□ Giorno N. Copia su altro mezzo tutti i file cambiati dal giorno N−1.
  □ vai al giorno 1.

□ Per diminuire il numero di mezzi che devono essere letti per un ripristino:
  □ eseguire un backup completo
  □ poi ogni giorno eseguire il backup di tutti i file che sono stati modificati dal backup completo.

---

