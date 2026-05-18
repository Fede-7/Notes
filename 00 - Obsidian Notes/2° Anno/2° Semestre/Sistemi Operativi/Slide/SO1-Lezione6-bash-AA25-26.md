## Pagina 1

Shell Bash

---

## Pagina 2

Shell

• Programma che interpreta il linguaggio a linea di comando attraverso il quale l'utente utilizza le risorse del sistema.
• Permette la gestione di variabili e dispone di costrutti per il controllo del flusso delle operazioni.
• https://tldp.org/LDP/Bash-Beginners-Guide/html

• Viene generalmente eseguito in modalità interattiva, all'atto del login, restando attivo per tutta la durata della sessione di lavoro ed effettuando le seguenti operazioni:
  – Gestione del “main command loop”;
  – Analisi sintattica;
  – Esecuzione di comandi (“built-in”, file eseguibili) e programmi in linguaggio di shell (script);
  – Gestione dello standard I/O e dello standard error;
  – Gestione dei processi da terminale.

---

## Pagina 3

Ciclo Esecuzione Shell

operazioni di start-up
acquisizione di un comando
EOF?
Si
No
"macro espansione" del comando
operazioni di terminazione
esecuzione del comando

---

## Pagina 4

Shell

• Shell interattiva
  – **interattiva, non login** → legge ~/.bashrc
  – **interattiva, login** → legge uno tra
    • /etc/profile
    • ~/.bash_profile
    • ~/.bash_login
    • ~/.profile
  • Es., bash –login (exit per tornare interattivi)

---

## Pagina 5

Abilitare WSL in Win

• Menu Start
• Cerca PowerShell
• Clic destro su “Windows PowerShell”
• Selezionare Esegui come amministratore

• wsl --install
  abilita WSL e installa WSL2

• Riavviare il computer
• Creare utente linux

• Verificare istallazione con: wsl -l –v

• In win installare anche Visual Studio Code

---

## Pagina 6

Variabili di Shell

• Esistono delle variabili di shell predefinite (variabili di ambiente), che permettono di caratterizzare il comportamento della shell.

• Per convenzione, il nome di tali variabili è in caratteri tutti maiuscoli:
  – **HOME**: argomento di default per il comando `cd`, inizializzato da login con il path della home directory, letto dal file `/etc/passwd`;
  – **PATH**: il path di ricerca degli eseguibili;
  – **PS1**: stringa del prompt, di default $ per l'utente normale e # per il super-user;
  – **HOSTNAME**: nome del computer
  – **SHELL**: la shell corrente

---

## Pagina 7

Variabili predefinite

• PATH percorso di ricerca eseguibili
• USER nome utente
• HOME directory home dell'utente
• PS1 il prompt
• HOSTNAME nome computer
• SHELL la shell corrente
• ...

---

## Pagina 8

Shell Interattiva

• Comunicazione tra utente e shell avviene tramite comandi o script:
• Nome comando built-in oppure
• Nome di un file eseguibile oppure
• Nome di Script, cioè file ASCII presente nel sistema dotato del premesso di esecuzione.

---

## Pagina 9

Sintassi dei comandi

comando [argomento ...]

Gli argomenti possono essere:

• opzioni o flag (-)
• parametri

separati da almeno un separatore

Nota: Il separatore di default è il carattere spazio; per alcune shell può essere modificato grazie alla ridefinizione di una variabile d'ambiente opportuna (cfr. seg.).

Una volta interpretata la prima parola sulla linea di comando, la shell ricerca nel file system un file con il nome uguale a tale prima parola.

La ricerca avviene ordinatamente all'interno delle directory elencate nella variabile d'ambiente PATH

---

## Pagina 10

Listing di Processi

ps = process status → mostra i processi attivi.

Senza opzioni, elenca solo i processi collegati al terminale corrente e all’utente attivo (effective user).

Permette di osservare:
- PID (Process ID) → identificativo univoco del processo
- TTY → identificativo del terminale
- TIME → indica il tempo (hh:mm:ss) cumulato di utilizzo CPU
- CMD → comando che ha generato il processo

ps -f full information (comando Unix style)
UID, PID, PPID, C, STIME, TTY, TIME, CMD
(C sta per percentuale di utilizzo CPU)

ps -e (oppure -A) info su tutti i processi indipendentemente dal terminale
info su tutti processi con dettagli

ps -ef info su tutti processi con terminale, non demoni (BSD style)
STAT indica lo stato (Running, Sleeping, Zombi, etc.)

ps aux x senza terminale, u in formato utente

---

## Pagina 11

Listing di Processi

Albero dei processi (Process Tree)

• pstree → mostra padre/figli
• ps --forest → albero con ps

---

## Pagina 12

Listing di Processi

top – visualizza in tempo reale i processi e l’uso delle risorse (CPU, RAM, tempo). Versione dinamica di ps, con possibilità di interazione.

• PR → priority: priorità del processo (gestita dal kernel).
• NI → nice value: valore “nice” impostato dall’utente (influenza PR).
• VIRT → virtual memory: memoria virtuale totale usata dal processo (RAM + swap + lib).
• RES → resident memory: memoria realmente occupata in RAM.
• SHR → shared memory: memoria condivisa con altri processi (es. librerie).
• S → state: stato del processo (R=running, S=sleeping, T=stopped, Z=zombie).
• %CPU → percentuale di CPU usata.
• %MEM → percentuale di RAM usata.
• TIME+ → tempo totale di CPU consumato.
• COMMAND → nome/programma eseguito.

htop modalità interattiva

us = processi utente
sy = kernel
ni = processi “nice”
id = inattiva
wa = attesa I/O
hi/si = interrupt HW/SW
st = tempo rubato (VM)

---

## Pagina 13

Esempio

• Comando vmstat …
  • Proc: r (processi attivi), b (processi bloccati)
  • Mem: free, swap, buff
  • System: in (interrupt), cs (context switch), us (%user mode), sy (%kernel mode)
  • CPU: id (%idle time), wa (%I/O waiting time), st (%stolen time da hypervision)
  • Comando:
    – ls /proc/
    – cat /proc/interrupts
    – watch –n 1 cat /proc/interrupts

• timer: interrupt del timer di sistema
• i8042: tastiera o il touchpad.
• eth0: interfaccia di rete.
• ahci: Il controller del disco
• LOC local timer interrupt (per CPU)

IO-APIC: gestione avanzata degli interrupt nei sistemi x86

---

## Pagina 14

Variabili

• Scrittura/definizione: a=3 (senza spazi)
• Lettura: ${a} o semplicemente $a

Esempi:
> a=3
> echo $a
3
> echo $aa
> echo ${a}a
3a
> a=ciao pippo
bash: pippo: command not found
> echo “ecco: $a”
ecco: 3
> echo 'ecco: $a'
ecco: $a

---

## Pagina 15

Comando echo

echo [argomenti]

Visualizza gli argomenti in ordine, separati da singoli blank

Esempio:

```bash
echo $SHELL
echo $PATH
% echo uno due tre
uno due tre
%
```

---

## Pagina 16

(Ri)definizione di variabili di shell

La shell offre all'utente sia la possibilità di ridefinire alcune variabili d'ambiente, sia di definire delle nuove variabili a proprio piacimento.

Esempio 1

$$\text{frutto}=mela$$
$$\text{verbo}=mangia$$
$$\text{nome}=\text{Stefania}$$
$$\text{echo } \text{$nome} \text{ verbo una } \text{frutto}$$

Stefania mangia una mela

$$\$

---

## Pagina 17

(Ri)definizione di variabili di shell

Esempio 2

$ echo $PATH
$ /usr/bin:/home/gio:.
$ ps
sh: ps: No such file or directory
$ PATH=$PATH:/bin
$ ps
PID TTY TIME CMD
2487 ttyp1 00:00:00 sh
2488 ttyp1 00:00:00 ps
$

---

## Pagina 18

(Ri)definizione di variabili di shell

Esempio 3

$ frutto=mela
$ frutto=${frutto}banana
$ echo $frutto
melabanana
$ tipo="mela banana"
$ echo $tipo
mela banana
$

---

## Pagina 19

# File Standard

Normalmente, un programma (comando) opera su più file

In Unix esiste il concetto di **file standard**:

| File standard | Che cos'è |
| :--- | :--- |
| standard input | il file da cui normalmente il programma acquisisce i suoi input |
| standard output | il file su cui normalmete un programma produce i suoi output |
| standard error | il file su cui normalmente un programma invia i messaggi di errore |

---

## Pagina 20

Redirezione std I/O

• I programmi dispongono di 3 canali di comunicazione:
  – Standard input (codice 0), per input
  – Standard output (1), per output
  – Standard error (2), per errore

Normalmente:

Standard input = tastiera

Standard output= schermo

---

## Pagina 21

Redirezione File Standard

La shell può variare queste associazioni di default **redirigendo** i files standard su qualsiasi file nel sistema

---

## Pagina 22

Ridirezione Stn Output

comando argomenti > file

Redirige lo standard output del comando sul file:
• se file non esiste, viene creato
• se file non esiste, viene riscritto (>) oppure il nuovo output viene accodato (>>)

~>ls -a > listaFile.txt
~>echo $PATH >> listaFile.txt

---

## Pagina 23

Ridirezione Stn Input

command arg1 ... argn < file

Il file file viene redirettto sullo standard input del comando

---

## Pagina 24

Ridirezione Stn Error

comando argomenti 2> file
2>>

(Analogo a > e >>)

Esempio:

> echho “ciao!”
bash: echho: command not found
> echho “ciao!” 2> /dev/null

---

## Pagina 25

Ridirezione

comando (codiceA)>&(codiceB)  redirige il canale A sul canale B

– esempio: comando > file 2>&1

---

## Pagina 26

Ridirezione

Per redigere correttamente, è necessario conoscere, di ogni comando:

• come usa lo standard input
• come usa lo standard output
• come usa l'error output
• come usa eventuali altri files

---

## Pagina 27

Esempio

1. Lista oppure msg di errore per directory non trovata
2. Msg di errore per operazioni illegali (usage: ...)

Non ha standard input

Inoltre accede ai files di sistema:

/etc/passwd per trovare lo user name

---

## Pagina 28

Pipe (tubo)

comando1 | comando2

Pipeline di due o più comandi:
Lo standard output di com1 funge da input a com2...

• com1 [arg ..] | com2 [arg ..]..|...

Esempi di comandi concatenabili: cat, sort, wc

~> cat file | sort
~> ls | less

---

## Pagina 29

Esercizi

• Creare un file che si chiami come l'utente corrente
• Creare un file che si chiami come l'host corrente, e che contenga il nome dell'host corrente

---

## Pagina 30

Command substitution

• Il pattern $(comando) viene sostituito con l'output del comando

• Esempi:
  - $(ls) equivale a *
  - $(echo ciao) equivale a ciao
  - $(cat nomefile) equivale all'intero contenuto del file
  - a=$$(ls) assegna ad a l'elenco dei file nella dir corrente
  - touch “$(date)” crea un file chiamato come la data attuale

---

## Pagina 31

Metacaratteri

• La shell riconosce alcuni caratteri speciali, chiamati **metacaratteri**, che possono comparire nei comandi.
• Quando l’utente invia un commando, la shell lo scandisce alla ricerca di metacratteri che processa in modo speciale
• Esempio:

```java
user> ls *.java
Albero.java div.java ProvaAlbero.java
AreaTriangolo.java EasyIn.java ProvaAlbero1.java
AreaTriangolo1.java IntQueue.java

Il metacarattere * nel pathname è un’abbreviazione per un nome di file. Il pathname *.java viene espando dalla shell con tutti I nome di file che terminano con .java. Il commando ls fronisce la lista di tutti i file con tale estensione
```

---

## Pagina 32

Abbreviazione pathname

• I seguenti metacaratteri, detti wildcard sono usati per abbreviare il nome di un file in un path name:

| Metacarattere | Significato |
| :--- | :--- |
| * | stringa di 0 o più caratteri |
| ? | singolo carattere |
| [ ] | singolo carattere tra quelli elencati |
| { } | stringa tra quelle elencate |

Esempi:

```bash
user> cp /JAVA/Area*.java /JAVA_backup
copia tutti i files il cui nome inizia con la stringa Area e termina con l'estensione
.java nella directory JAVA_backup.

user> ls /dev/tty?
/dev/ttya /dev/ttyb
```

---

## Pagina 33

Abbreviazione pathname

• I seguenti metacaratteri, detti wildcard sono usati per abbreviare il nome di un file in un path name:

```bash
user> ls /dev/tty?[234]
/dev/ttyp2 /dev/ttyp4 /dev/ttyq3 /dev/ttyr2 /dev/ttyr4
/dev/ttyp3 /dev/ttyq2 /dev/ttyq4 /dev/ttyr3

user> ls /dev/tty?[2-4]
/dev/ttyp2 /dev/ttyp4 /dev/ttyq3 /dev/ttyr2 /dev/ttyr4
/dev/ttyp3 /dev/ttyq2 /dev/ttyq4 /dev/ttyr3

user> mkdir /user/studenti/rossi/{bin,doc,lib}
crea le directory bin, doc, lib .
```

---

## Pagina 34

Quoting

Il meccanismo del **quoting** è utilizzato per inibire l’effetto dei metacaratteri. I metacaratteri a cui è applicato il quoting perdono il loro significato speciale e la shell li tratta come caratteri ordinari.

Ci sono tre meccanismi di quoting:

• il metacarattere di **escape** \ inibisce l’effetto speciale del metacarattere che lo segue:
  user> cp file file\?
  user> ls file*
  file    file?

• tutti i metacaratteri presenti in una stringa racchiusa tra **singoli apici** perdono l’effetto speciale:
  user> cat ’file*?’
  …

• i metacaratteri per l’abbreviazione del pathname presenti in una stringa racchiusa tra **doppi apici** perdono l’effetto speciale (ma non tutti i metacaratteri della shell):
  user> cat "file*?"

---

## Pagina 35

<table><thead><tr><th>Simbolo</th><th>Significato</th><th>Esempio d’uso</th></tr></thead><tbody><tr><td>&gt;</td><td>Ridirezione dell’output</td><td>ls &gt;temp</td></tr><tr><td>&gt;&gt;</td><td>Ridirezione dell’output (append)</td><td>ls &gt;&gt;temp</td></tr><tr><td>&lt;</td><td>Ridirezione dell’input</td><td>wc -l &lt;text</td></tr><tr><td>&lt;&lt;delim</td><td>ridirezione dell’input da linea di comando (here document)</td><td>wc -l &lt;&lt;delim</td></tr><tr><td>*</td><td>Wildcard: stringa di 0 o più caratteri, ad eccezione del punto (.)</td><td>ls *.c</td></tr><tr><td>?</td><td>Wildcard: un singolo carattere, ad eccezione del punto (.)</td><td>ls ?.c</td></tr><tr><td>[...]</td><td>Wildcard: un singolo carattere tra quelli elencati</td><td>ls [a-zA-Z].bak</td></tr><tr><td>{...}</td><td>Wildcard: le stringhe specificate all’interno delle parentesi</td><td>ls {prog,doc}*.txt</td></tr></tbody></table>

---

## Pagina 36

<table><thead><tr><th>Simbolo</th><th>Significato</th><th>Esempio d’uso</th></tr></thead><tbody><tr><td>|</td><td>Pipe</td><td>ls | more</td></tr><tr><td>;</td><td>Sequenza di comandi</td><td>pwd;ls;cd</td></tr><tr><td>||</td><td>Esecuzione condizionale. Esegue un comando se il precedente fallisce.</td><td>cc prog.c || echo errore</td></tr><tr><td>&amp;&amp;</td><td>Esecuzione condizionale. Esegue un comando se il precedente termina con successo.</td><td>cc prog.c && a.out</td></tr><tr><td>(...)</td><td>Raggruppamento di comandi</td><td>(date;ls;pwd)>out.txt</td></tr><tr><td>#</td><td>Introduce un commento</td><td>ls # lista di file</td></tr><tr><td>\</td><td>Fa in modo che la shell non interpreti in modo speciale il carattere che segue.</td><td>ls file.\*</td></tr><tr><td>!</td><td>Ripetizione di comandi memorizzati nell’history list</td><td>!ls</td></tr></tbody></table>

---

## Pagina 37

Shell expansions and substitutions

disabled by:

- Tilde expansion
- Variable substitution $a$
- Arithmetic substitution $((...))$
- Command substitution $((...))$
- Filename expansion (wildcards)
- Word splitting
- Execute command

Warning: Quoting works differently with assignments

---

## Pagina 38

Word splitting

L’ultima fase prima di eseguire un comando consiste nella suddivisione in parole

La variabile IFS (internal field separator) definisce i separatori
Di default, IFS=”<space><tab><newline>”

Come effetto collaterale, il word splitting sostituisce i newline con spazi
In una directory con molti file, confrontare l'output di “Is” con quello di “echo $(ls)”

---

## Pagina 39

Altri Comandi

---

## Pagina 40

pwd (print working directory)

pwd "printworking directory"
stampa il path della directory corrente

Esempio:

```bash
% pwd
/usr/mariog
%
```

---

## Pagina 41

cd (change directory)

cd [directory]
Cambia la directory corrente a quella indicata.
Se non viene passato nessun argomento, la directory corrente diventa la home directory.

Esempio:
1so:~>cd
1so:~>pwd
/home/1so
1so:~>cd esempio/esempiocd
1so:~>pwd
/home/1so/esempio/esempiocd

---

## Pagina 42

ls (list)

ls [options] [directory]
Elenca i file contenuti nella directory specificata.
Se la directory non e' indicata, viene elencato il contenuto della directory corrente.
Alcune opzioni:
-a Elenca anche i file nascosti
-l Formato esteso con informazioni su modo, proprietario, dimensione, etc dei file
-s fornisce la dimensione in blocchi dei file
-t lista i file nell'ordine di modifica (prima il file modificato per ultimo)
-1 elenca i file in una singola colonna
-F aggiunge / al nome delle directory e * al nome dei file eseguibili
-R si chiama ricorsivamente su ogni subdirectory

---

## Pagina 43

Is – campi del formato esteso

Totale dimensione occupata (in blocchi)

Riferimenti al file

Dimensione (byte)

Nome

sol1:~>ls -l
total 12
-rw-rw-r-- 1 lso lso 10 Mar 4 13:29 a
-rw-rw-r-- 1 lso lso 10 Mar 4 14:12 b
drwxrwxr-x 2 lso lso 4096 Mar 4 14:29 c

Proprietario

Gruppo primario

Data ultima modifica

Tipo

Permessi

(r)ead, (w)rite, e(x)ecute, (s)et uid bit

(d)directory, (l)ink, (c)haracter special file, (b)lock special file, (-) ordinary file

---

## Pagina 44

cp (copy)

cp [options] source... target

copia un file in un altro file oppure uno o più file in una directory

Se vengono specificati solo i nomi di due file, il primo viene copiato sul secondo

Se vengono specificati solo due nomi, e se il secondo nome indicato è una directory, source viene copiato con lo stesso nome nella directory target. Se source è una directory, la copia avviene solo con opzioni particolari.

Se vengono indicati più di due nomi, il file target deve essere una directory e vengono generate le copie dei source in target. In mancanza di opzioni particolari, le directory non vengono copiate.

Alcune opzioni

-r se source e target sono directory, copia ricorsivamente source, i suoi file e le sue subdirectory in target

-i opera in modo interattivo, chiedendo una conferma se la copia comporta la cancellazione di un target preesistente

---

## Pagina 45

Esempi

• Copia il file pippo nella directory corrente nel file /tmp/pippo.back
  cp pippo /tmp/pippo.back

• Copia il file /tmp/pippo.back e la directory dir nella directory nuovadir
  cp -r /tmp/pippo.back dir nuovadir

• Copia il file pippo nel file pippo2
  cp pippo pippo2

---

## Pagina 46

mv (move)

mv [options] source... destination
rinomina (sposta) file o directory.

Se vengono specificati solo i nomi di due elementi, source viene rinominato in destination, oppure in destination/source, a seconda che destination indichi un file o una directory. Qualora destination denoti un file preesistente, questo non sarà più accessibile come tale, e non sarà più accessibile in alcun modo se destination era il suo unico nome.

Se vengono indicati più di due elementi, destination deve essere una directory, e source_1...source_n vengono rinominati come destination/source_1...destination/source_n.

Nel caso che source e destination appartengono a due diversi file system, il comando effettua un vero e proprio spostamento dati tra i due file system. In tal caso vengono spostati solo i file ordinari, quindi: né collegamenti, né directory.

Alcune opzioni:

-i il comando chiede conferma all'utente qualora destination è un file preesistente

---

## Pagina 47

rm (remove)

rm [options] file...
elimina i file o le directory indicati come argomento.

Alcune opzioni:
-i chiede conferma prima di rimuovere ogni file
-R rimuove ricorsivamente i file e le sottodirectory

Esempi d'uso
Elimina i file pippo nella directory corrente e /tmp/pippo.back
rm pippo /tmp/pippo.back
Elimina la directory nuovadir e tutto il suo contenuto
rm -R nuovadiru
Elimina tutti i file nella directory corrente
rm *

---

## Pagina 48

wc (word count)

wc [options] [file...]

fornisce il numero dei codici di interruzione di riga (in pratica il numero delle righe), delle parole o dei caratteri contenuti in file. Senza opzioni fornisce, nell'ordine suddetto, ciascuna delle precedenti informazioni.

Alcune opzioni:
-c emette solo il numero complessivo di caratteri di file.
-w emette solo il numero complessivo di parole in file.
-1 emette solo il numero di righe in file.

Esempi di esecuzione

gio$ wc which_manpage
132 239 2083 which_manpage

gio$ wc -c which_manpage
2083 which_manpage
gio$

---

## Pagina 49

cat (concatenate)

cat [options] [file...]

concatena i file indicati come argomento, visualizzandoli attraverso lo standard output

Alcune opzioni:

-n fa precedere ogni linea di ouput dal numero progressivo che identifica la posizione della linea nel file concatenato

-b come l'opzione precedente, ma omette la numerazione delle linee bianche

-v mostra anche i caratteri non stampabili, ad eccezione dei caratteri di tabulazione, nuova linea e ritorno a capo

---

## Pagina 50

Comando cat

cat file...

"concatenate"

Concatena i file e li scrive sullo standard output...

% cat file1 file2 file1 ei fu
ei fu file2 siccome immobile
siccome immobile

% cat file1 file2 > file3

%

... a meno che manchino gli argomenti, nel qual caso scrive lo standard input sullo standard output

---

## Pagina 51

cut

cut [options] [file...]

estrae delle colonne specifiche dalle linee di testo che compongono file.

Alcune opzioni:
-c char_list
-f field_list
  definisce gli intervalli da estrarre espressi in caratteri.
  definisce gli intervalli da estrarre espressi in campi.
  I campi sono distinti in base a un certo carattere usato

  come delimitatore. Quello predefinito è il carattere di tabulazione.
  definisce un delimitatore alternativo al carattere di tabulazione.

Esempi d'uso
Estrae la prima e la quinta colonna del file /etc/passwd
cut -d: -f1,5 /etc/passwd

Estrae i primi dieci caratteri da ogni riga del file /etc/passwd
cut -c1-10 /etc/passwd

---

## Pagina 52

Sort

sort [options] [file…]

permette di (ri)ordinare o fondere insieme il contenuto dei file passati come parametri, oppure di (ri)ordinare le linee passategli in input.

In assenza di opzioni che definiscano diversi criteri di ordinamento, quest'ultimo avviene in base al primo campo ed è alfabetico.

Alcune opzioni:
-f ignora le differenze tra lettere minuscole e maiuscole
-n considera numerica anzichè testuale la chiave di ordinamento
-r ordina in senso decrescente anzichè crescente
-o fileout invia l'output a fileout anzichè sull'output standard
-t s usa s come separatore di campo
-k s1,s2 usa i campi da s1 a s2-1 come chiavi di ordinamento

---

## Pagina 53

sort – Esempi d'uso

Ordina le linee del file /etc/passwd in base al valore del terzo campo (UID)

sort -t: -k3,4 /etc/passwd

Come prima, solo che ora l'ordinamento è numerico anzichè alfabetico

sort -t: -n -k3,4 /etc/passwd

Come prima, ma seguendo l'ordinamento inverso (prima l'UID maggiore)

sort -t: -n -k3,4 -r /etc/passwd

Come prima, ma ora l'output è memorizzato in passwd_reordered

sort -t: -n -k3,4 -r /etc/passwd -o passwd_reordered

---

## Pagina 54

# Esempio

## # sort senza < (argomento file)
sort dati.txt
# a
# b
# c

## # sort con < (stdin da file)
sort < dati.txt
# a
# b
# c

## #word counter
wc 0< dati.txt
# 3 3 6

---

## Pagina 55

head & tail

| Comando/Sintassi | Descrizione |
| :--- | :--- |
| head [-numero] file | visualizza le prime 10 (o -numero) linee di un file |
| tail [-numero] file | visualizza le ultime 10 (o -numero) linee di un file |

Esempio d’uso head:
head -40 filename
oppure
head -n 40 filename

Esempio d’uso tail:
tail -30 filename

---

## Pagina 56

find

find [pathname...] [expression]

discende ricorsivamente le directory specificate (pathname...), cercando tutti i file che rendono vera expression.

Molto flessibile:

• ricerca file di specificati attributi (nome, tipo, permessi, proprietario, gruppo, numero di link, dimensione, data di ultima modifica/accesso …)
• and, or, not di attributi
• può eseguire automaticamente, o previa conferma, uno o più comandi sui file individuati
• le espressioni si ottengono combinando flag, parametri e gli operatori booleani;
• le espressioni costituite solo da un flag e da un parametro (opzionale) si dicono espressioni elementari;

---

## Pagina 57

Esempi

Ricerca in /home/lso di file la cui dimensione è maggiore di 100 blocchi

find /home/lso -size +100

Ricerca dalla working dir (ricorsivamente) dei file con nome “pattern”

find . -type f -name “pattern”

Es.

find . -type f -name "*.txt"
find . -maxdepth 1 -type f -name "*.txt"

---

