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

Strutture del File System

- Strutture necessarie del file system fornite dal SO
  - apertura di un file
  - lettura di un file

Figure (a): Directory structure with kernel memory and secondary storage.
Figure (b): Per-process open-file table, system-wide open-file table, data blocks, file-control block, and secondary storage.

---

## Pagina 47

Implementazione Directory

- Implementazione delle directory impatta molto sulle perstazioni
  - Algoritmi di allocazione e gestione delle directory

- Modo più semplice di implementare le directory è con una lista lineare un array contenente identificatore del file e puntatore al FCB
  - Facile da programmare (si cerca il file e si accede)
  - Poco efficiente da eseguire
    - Tempo di ricerca proporzionale alla dimensione
    - Lista ordinata per fare ricerca binaria, ma costi di gestione

- Hash Table – lista lineare con struttura dati ad hash table
  - Abbassa i tempi di ricerca su directory
  - Collisioni – situazioni dove due file name hanno hash sulla stessa locazione location
    - Metodo chained-overflow

---

## Pagina 48

Implementazione Directory

- Hash Table – lista lineare con struttura dati ad hash table
  - Chiave filename mappati su indici della tabella (funzione hash)
  - Abbassa i tempi di ricerca su directory
  - Collisioni – situazioni dove due filename mappati sulla stessa locazione
    - Metodo chained-overflow

---

## Pagina 49

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

## Pagina 50

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

## Pagina 51

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

## Pagina 52

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

## Pagina 53

Protezioni di un File in UNIX

A ciascun file (normale, speciale, directory) sono associati alcuni attributi:

- **Proprietario (owner):** l'utente che ha creato il file
- **Gruppo (group):** il gruppo a cui il proprietario appartiene
- **Permessi (permissions)** Il tipo di operazioni che il proprietario, i membri del suo gruppo o gli altri utenti possono compiere sul file

Proprietario, gruppo e permessi iniziali sono assegnati dal sistema al file al momento della sua creazione.

Il proprietario può successivamente modificare tali attributi con appositi comandi (chown, chgrp, chmod)

---

## Pagina 54

Identificazione Utenti

- Ogni utente viene identificato da uno **user name** assegnato dall'amministratore del sistema. Adesso corrisponde biunivocamente uno **userid** numerico, assegnato dal sistema
- **User name** e user-id sono pubblici

---

## Pagina 55

GRUPPI

Ogni utente può far parte di uno o più gruppi, definiti dall'amministratore del sistema

Ogni gruppo è identificato da un group name di al più 8 caratteri, associato biunivocamente a un group-id numerico

Esempio:

---

