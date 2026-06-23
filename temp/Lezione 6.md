# Tipi di Chiamate di Sistema

## Gestione Informazione
- **get time or date**, set time or date
- **get system data**, set system data
- **get and set process**, file, or device attributes

## Comunicazione
- **create, delete communication connection**
- **send, receive messages** if message passing model to host name or process name
  - da client a server
- **Shared-memory**: creazione ed accesso a regioni di memoria condivisa
- **trasferire informazione di stato**
- **Installare/disinstallare dispositivo remoti**

## Protezione
- **Controllo accesso a risorse**
- **Gestione dei permessi**
- **Gestione accesso utenti**

## Funzioni Dettagliate delle Chiamate di Sistema

### Controllo dei processi
- creazione e arresto di un processo
- caricamento, esecuzione
- terminazione normale e anormale
- esame e impostazione degli attributi di un processo
- attesa per il tempo indicato
- attesa e segnalazione di un evento
- assegnazione e rilascio di memoria

### Gestione dei file
- creazione e cancellazione di file
- apertura, chiusura
- lettura, scrittura, posizionamento
- esame e impostazione degli attributi di un file

### Gestione dei dispositivi
- richiesta e rilascio di un dispositivo
- lettura, scrittura, posizionamento
- esame e impostazione degli attributi di un dispositivo
- inserimento logico ed esclusione logica di un dispositivo

### Gestione delle informazioni
- esame e impostazione dell’ora e della data
- esame e impostazione dei dati del sistema
- esame e impostazione degli attributi dei processi, file e dispositivi

### Comunicazione
- creazione e chiusura di una connessione
- invio e ricezione di messaggi
- informazioni sullo stato di un trasferimento
- inserimento ed esclusione di dispositivi remoti

### Protezione
- visualizzazione dei permessi di un file
- impostazione dei permessi di un file

*Figura 2.8 Tipi di chiamate di sistema.*

---

# Esempi chiamate di sistema in Windows e Unix

**Controllo dei processi**
- Windows: `CreateProcess()`
- UNIX: `fork()`

**Processi**
- Windows: `ExitProcess()`
- UNIX: `exit()`
- Windows: `WaitForSingleObject()`
- UNIX: `wait()`

**Gestione dei file**
- Windows: `CreateFile()`
- UNIX: `open()`
- Windows: `ReadFile()`
- UNIX: `read()`
- Windows: `WriteFile()`
- UNIX: `write()`
- Windows: `CloseHandle()`
- UNIX: `close()`

**Gestione dei dispositivi**
- Windows: `SetConsoleMode()`
- UNIX: `ioctl()`
- Windows: `ReadConsole()`
- UNIX: `read()`
- Windows: `WriteConsole()`
- UNIX: `write()`

**Gestione delle informazioni**
- Windows: `GetCurrentProcessID()`
- UNIX: `getpid()`
- Windows: `SetTimer()`
- UNIX: `alarm()`
- Windows: `Sleep()`
- UNIX: `sleep()`

**Comunicazione**
- Windows: `CreatePipe()`
- UNIX: `pipe()`
- Windows: `CreateFileMapping()`
- UNIX: `shm_open()`
- Windows: `MapViewOfFile()`
- UNIX: `mmap()`

**Protezione**
- Windows: `SetFileSecurity()`
- UNIX: `chmod()`
- Windows: `InitializeSecurityDescriptor()`
- UNIX: `umask()`
- Windows: `SetSecurityDescriptorGroup()`
- UNIX: `chown()`

---

# Standard C Library

Un programma in C invoca una chiamata di **libreria standard** `printf()` che chiama la **chiamata di sistema** `write()`.

```c
#include <stdio.h>
int main ()
{
    printf ("Greetings");
    return 0;
}
```

**Flusso di esecuzione:**
user mode
$\downarrow$
kernel mode
$\downarrow$
standard C library
$\downarrow$
`write ()`
$\downarrow$
`write ()`
$\downarrow$
system call

---

# Programmi di Sistema

I programmi di sistema forniscono un **ambiente conveniente** per lo sviluppo e l'esecuzione del programma.

**Gerarchia dei componenti:**
- Programmi applicativi
- Sistema base
- Kernel

**Componenti del Kernel:**
- Driver dei dispositivi
- Gestore I/O
- Gestore dei Processi
- Gestore del file system
- Gestore della memoria
- IPC

**Componenti del Sistema:**
- Librerie di sistema
- Caricatore dinamico
- Sistema di init
- Comandi di sistema
- Shell
- Terminale

*2.30*

---

# Panoramica dei Programmi di Sistema

- I programmi di sistema forniscono un ambiente conveniente per lo sviluppo e l'esecuzione di programmi.

- Possono essere suddivisi in:
  - Manipolazione di file
  - Informazioni sullo stato
  - Supporto del linguaggio di programmazione
  - Caricamento ed esecuzione del programma
  - Comunicazioni
  - Servizi in background
  - Programmi applicativi

- La **maggior parte degli utenti** di un SO usa soprattutto i programmi di sistema, meno le effettive chiamate di sistema.

---

# Caratteristiche dei Programmi di Sistema

□ Forniscono un ambiente conveniente per lo sviluppo e l'esecuzione di programmi.
□ Alcuni di essi sono semplicemente **interface utente** per le chiamate di sistema; altri sono notevolmente più complessi.

□ **Gestione dei file**:
crea, elimina, copia, rinomina, stampa, scarica, elenca e generalmente manipola file e directory.

□ **Informazioni sullo stato**:
- Informazioni al sistema: data, ora, quantità di memoria disponibile, spazio su disco, numero di utenti.
- Informazioni dettagliate su prestazioni, registrazione e debug.
- In genere, questi programmi formattano e stampano l'output sul terminale o su altri dispositivi di output.

---

# Funzionalità Specifiche dei Programmi di Sistema

□ **Modifica file**
- Editor di testo per creare e modificare file.
- Comandi speciali per cercare contenuti di file o eseguire trasformazioni del testo.

□ **Supporto del linguaggio di programmazione**
- compilatori, assemblatori, debugger ed interpreti.

□ **Caricamento ed esecuzione del programma**
- Una volta assemblato o compilato un programma, deve essere caricato in memoria per essere eseguito.
- Il sistema fornisce strumenti come **dynamic loader**, **linker**, sistemi di debug, etc.

□ **Comunicazioni**
- Meccanismi per creare connessioni virtuali tra processi, utenti e sistemi informatici.

---

# Servizi di Background

- **Lanciati a tempo di boot**
  - Alcuni per lo startup, poi terminate.
  - Altri continuano a girare.

- I programmi di sistema in **costante esecuzione** si dicono servizi, sottosistemi, **demoni**.

- Esempi sono monitoraggio di errori, servizi di stampa, etc.

- **Eseguiti in contesto user**, non kernel.

---

# Progettazione ed Implementazione di un SO

- La struttura di un SO può variare molto da sistema a sistema.
- La progettazione parte da obiettivi e specifiche.
- Dipende da hardware e tipo di sistema.

**Distinguiamo obiettivi utente e obiettivi di sistema:**

- **Utente**
  - comodo da usare, facile da imparare, affidabile, sicuro e veloce.
- **Sistema**
  - facile da progettare, implementare e mantenere, nonché flessibile, affidabile, privo di errori ed efficiente.

*Es. Windows Server vs VxWorks*

---

# Politica vs Meccanismo

Distinguere:
- **Politica**: cosa fare?
- **Meccanismo**: come fare?

*Es., il timer serve per la protezione della CPU, il timer è un meccanismo, ma la lunghezza del timer è una politica.*

La **separazione della politica dal meccanismo** consente flessibilità se le decisioni politiche devono essere modificate in un secondo momento:
- Il meccanismo deve supportare più politiche.
- La politica si può definire settando parametri dei meccanismi.
- *Es., approcci a microkernel favoriscono la separazione.*

Specificare e progettare un sistema operativo è un compito altamente creativo per l’ingegneria del software.

---

# Implementazione del Sistema Operativo

□ Diverse modalità:
- Primi SO in assembly.
- Poi linguaggi di programmazione di sistema come Algol, PL/1.
- Ora linguaggi come **C, C++**.

□ Di solito un mix di linguaggi:
- Parti più basse in assembly.
- Corpo principale in C.
- Programmi di sistema in C, C++, linguaggi di scripting come PERL, Python, shell scripts.

□ Più è alto il livello del linguaggio più facile è il **porting** su altro hardware, ma meno performante.

□ L’**emulazione** permette ad un OS di girare su hardware non-native.

□ La **virtualizzazione** permette l’esecuzione di più sistemi operativi contemporaneamente.

---

# Emulazione vs Virtualizzazione

## Emulazione
- Riproduco un’architettura hardware diversa da quella reale.
- Così posso eseguire programmi compilati per un’altra CPU.
- → **Lenta** perché il codice viene interpretato/convertito.
- Esempio: QEMU (Quick EMUulator) che emula ARM su x86.
- → Grande flessibilità, bassa efficienza.

## Virtualizzazione
- Faccio girare più sistemi operativi della stessa architettura sull’hardware reale.
- Non simula la CPU → i guest girano nativamente.
- → **Molto più veloce** dell’emulazione.

---

# Tipi di Virtualizzazione

## Virtualizzazione completa (full)
- Il guest non sa di essere virtualizzato.
- Pensa di parlare con hardware reale → massima compatibilità.
- → **Overhead maggiore** a causa della gestione trasparente dell’hardware.
- Esempio: **VMware**.

## Paravirtualizzazione
- Il guest sa di essere virtualizzato e collabora con l’VMM tramite API speciali.
- Meno overhead, ma richiede OS modificati.
- Esempio storico: Xen paravirtualizzato.
- Oggi la parav viene usata come ottimizzazione (es. virtio), non come modello puro.

## Virtualizzazione assistita da hardware
- Le CPU (**Intel VT-x, AMD-V, ARM Virt. Ext.**) forniscono istruzioni speciali che rendono la virtualizzazione più efficiente.
- → È la base della virtualizzazione moderna.
- → Riduce costi di gestione del guest.
- Oggi **quasi tutte** le VM usano questo modello.

---

# Architettura della Virtualizzazione

- Permette di eseguire più sistemi operativi sulla stessa macchina fisica.
- Ogni SO esegue le proprie applicazioni come se avesse hardware dedicato.

- **Virtualizzazione** – sistema operativo compilato in modo nativo per la CPU, che esegue anche sistemi operativi guest compilati in modo nativo.
- **VMM (Virtual Machine Manager/Monitor)** fornisce servizi di virtualizzazione.

- **Tipo 1**:
  - VMM come Sistema operativo host, comunica direttamente con hardware (es. VMware ESXi, Xen, Hyper-V, KVM).
- **Tipo 2**:
  - VMM installato sopra un SO host (es. VMWare, Oracle VirtualBox).

**Livelli di privilegio:**
- Ring -1 Hyp
- Ring 0-2 Kernel (si usa solo 0)
- Ring 3 User

---

# VMM e Hypervisor

Virtualizzazione – VMM/Hypervisor fornisce servizi di virtualizzazione per eseguire guest compilati nativamente.

**VMM (Virtual Machine Manager/Monitor)** fornisce servizi di virtualizzazione.

- **Tipo 1**:
  - VMM come Sistema operativo host, comunica direttamente con hardware (es. VMware ESXi, Xen, Hyper-V, KVM).
- **Tipo 2**:
  - VMM installato sopra un SO host (es. VMWare, Oracle VirtualBox).

*Figura 1.16 Un computer che ha in esecuzione (a) un singolo sistema operativo e (b) tre macchine virtuali.*

---

# Casi di Studio: Linux, Windows e macOS

## Caso Linux
- Hypervisor: **KVM (Kernel-based Virtual Machine)**.
- È integrato direttamente nel kernel Linux (hyp tipo 1).
- Si attiva solo quando una VM lo usa.
- Le VM sono processi user-space che accedono a KVM.

## Caso Windows 11
- **Hyper-V** è un hypervisor di tipo 1.
- Windows è una VM privilegiata chiamata **root partition**, le altre VM (es. WSL2) sono **guest partitions**.

**Attivazione (PowerShell):**
- `wsl --install`
- `wsl --status`

**Gerarchia Hardware:**
1. Hyper-V Hypervisor (TYPE 1)
2. Windows (Root VM / Parent Partition)
3. Linux WSL2 VM (Guest)

---

# Caso macOS (Apple Silicon)

- Non ha un hypervisor nel kernel.
- Le VM sono gestite da **applicazioni user-space** che usano `Hypervisor.framework` (API user-space).

---

# Strutture di un Sistema Operativo

- Un Sistema Operativo è un software molto complesso.

**Vari modi di strutturarlo:**
- **Sistemi monolitici**
  - Struttura semplice -- MS-DOS
  - Più complessa -- UNIX
- **Sistemi Stratificati**
- **Sistemi a micro-kernel**
- **Sistemi ibridi**

---

# Sistemi Monolitici

- Il Sistema Operativo è costituito da una collezione di procedure ognuna delle quali può chiamare qualsiasi altra.
- Un sistema monolitico viene anche chiamato **sistema strettamente accoppiato (tightly coupled)**.
  - Collezione di procedure linkate in un unico eseguibile.
  - Ogni procedura può chiamare l’altra (**efficace ed efficiente**).
  - **Poca modularità** (difficili da sviluppare ed estendere).
  - Struttura basata su chiamate di sistema.

*Tanenbaum & Bo, Modern Operating Systems:4th ed., (c) 2013 Prentice-Hall, Inc. All rights reserved.*

---

# Struttura Semplice - MS-DOS

**MS-DOS – funzionalità nel minimo spazio**
- Monoutente e monotask (Windows 3.1 multitask cooperativo).
- Non suddiviso in moduli.
- Sebbene MS-DOS abbia una struttura, interfacce e livelli di funzionalità non sono ben separati.
- **Programmi utente accedono a tutti i livelli** (controllo completo della macchina).

**BIOS (Basic Input Output System)**
- avvio, interfaccia HW, interrupt.

---

# Struttura non Semplice - UNIX

- UNIX: limitato dalla funzionalità hardware, il sistema operativo UNIX originale aveva una strutturazione limitata.
- Il sistema operativo UNIX è costituito da due parti separabili:
  - **Programmi di sistema**
  - **Kernel**
    - Tutto ciò che si trova al di sotto dell'interfaccia di chiamata di sistema e al di sopra dell'hardware fisico.
    - Fornisce il file system, schedulazione della CPU, gestione della memoria e altre funzioni del sistema operativo (alto numero di funzioni in un livello).
    - **Interfaccia standard per chiamate di sistema (POSIX)**.

---

# Struttura di un Sistema UNIX

**Gerarchia del Sistema:**

1. **Users**
2. **Shells and commands**
3. **Compilers and interpreters**
4. **System libraries**
5. **System-call interface to the kernel**
6. **Signals, terminal handling, character I/O system, terminal drivers**
7. **File system, swapping, block I/O system, disk and tape drivers**
8. **CPU scheduling, page replacement, demand paging, virtual memory**
9. **Kernel interface to the hardware**
10. **Terminal controllers, terminals**
11. **Device controllers, disks and tapes**
12. **Memory controllers, physical memory**

---

# Struttura di un Sistema Linux

**Gerarchia del Sistema:**

- **GNU C Library**: core lib del GNU system per interagire con il kernel linux.

*Figure 2.13 Linux system structure.*

---

# Approccio Stratificato

- Il sistema operativo è suddiviso in un numero di livelli (**levels**), ciascuno costruito sopra i livelli inferiori (THE, MULTICS).
- Lo strato inferiore (**layer 0**) è l'hardware; il più alto (**layer N**) è l'interfaccia utente.
- Con la modularità ciascuno layer utilizza funzioni (operazioni) e servizi dei layer inferiori.

**Schema dei Livelli:**
- Layer 5: The operator
- Layer 4: User programs
- Layer 3: Input/output management
- Layer 2: Operator-process communication
- Layer 1: Memory and drum management
- Layer 0: Processor allocation and multiprogramming

*THE realizzato alla Technische Hogelschool Eindhoven in Olanda da Dijkstra nel 1968 per il computer Electrologica X8.*

---

# Struttura a Microkernel (Mach)

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto **orientamento a microkernel**.
□ macOS kernel (Darwin) parzialmente basato su Mach.

□ **Spostare più possibile servizi dal kernel allo spazio utente**.
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente – **comunicazione message-passer** tramite kernel.

*2.51*

---

# Struttura a Microkernel (Dettagli)

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto orientamento a microkernel.
□ macOS kernel (Darwin) parzialmente basato su Mach.

□ **Spostare più possibile dal kernel allo spazio utente**.
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente.

□ **Kernel minimale:**
- Meccanismo di comunicazione tra processi (**message-passer**).
- Gestione della memoria e dei processi.
- Gestione dell’hardware di basso livello.
- Tutto il resto gestito da processi in spazio utente (e.g., politiche di gestione file system, scheduling, memoria sono implementate da processi utente) che comunicano passando per il kernel.

---

# Confronto Architetture

□ Verso metà anni ’80 realizzato Mach con kernel strutturato in moduli secondo il cosiddetto orientamento a microkernel.
□ macOS kernel parzialmente basato su Mach (e su BSD).

□ **Spostare più possibile dal kernel allo spazio utente**.
□ Funzioni di comunicazione tra i programmi client e i vari servizi in esecuzione nello spazio utente.

□ **Kernel minimale:**
*(Vedi sezione precedente)*

**Confronto Strutturale:**

- **Monolithic Kernel based Operating System**
  - Application
  - System Call
  - VFS
  - IPC, File System
  - Scheduler, Virtual Memory
  - Device Drivers, Dispatcher, ...
  - Hardware

- **Microkernel based Operating System**
  - Application
  - IPC
  - UNIX Server
  - Device Driver
  - File Server
  - Basic IPC, Virtual Memory, Scheduling
  - Hardware

---

# Vantaggi e Svantaggi del Microkernel

- Spostare più possibile dal kernel allo spazio utente.
- Comunicazione tra moduli utente mediante **message passing**.

**Vantaggi:**
- Facilità di estensione microkernel.
- Facilità di trasferimento dell’SO su nuove architetture.
- Meno codice eseguito in modalità kernel.
- **Sicuro**.

**Svantaggi:**
- **Sovraccarico delle prestazioni** della comunicazione tra lo spazio utente e lo spazio del kernel (**context switch**).

---

# Evoluzione Windows NT

- Prima release a microkernel.
- Prestazioni povere rispetto a Windows 95.
- Si passa a Windows NT 4.0 muovendo servizi da utente a kernel.
- Windows XP torna **più monolitico** che microkernel.

---

# Moduli del Kernel

- Molti sistemi operativi moderni implementano moduli del kernel caricabili.
- **Loadable kernel modules (LKMs)** - Linux, Solaris, macOS, Win, etc.
- Ogni componente principale è separato.
- Servizi linkati dinamicamente mentre il kernel è in esecuzione o caricamento.
- Ciascuno parla con gli altri tramite interfacce conosciute.
- Ciascuno è caricabile secondo necessità all'interno del kernel.

- Simile al sistema a livelli (core ha interfacce con altri moduli) ma con **più flessibilità**.
- Simile a microkernel, ma meno message passing.

---

# Sistemi Ibridi

La maggior parte dei sistemi operativi moderni non sono in realtà un modello puro.

- Il sistema ibrido **combina più approcci** per soddisfare le esigenze di prestazioni, sicurezza e usabilità.
- **Kernel Linux e Solaris**: in un singolo spazio di indirizzi, quindi monolitico, ma modulari per il caricamento dinamico di funzionalità.
- **Windows**: per lo più monolitico, microkernel per diverse parti del sottosistema.
- **Apple macOS**: ibrido (microkernel, monolitico).

---

# Struttura Ibrida: macOS (Kernel XNU)

Il sistema operativo macOS di Apple si basa su **Kernel XNU**.

**XNU kernel**
- **Mach**:
  - scheduling
  - IPC
  - virtual memory
- **BSD**:
  - POSIX layer
  - networking
  - file systems
  - process model
- **IOKit**:
  - alcuni driver

**User space**
- applicazioni
- framework di sistema
- Driver Kit drivers
- servizi di sistema

**Kernel XNU (X is Not Unix)**
- Combina Mach e BSD (microkernel e monolitico).
- memoria, IPC, I/O (variante mach).
- protezioni, virtual file system, rete, POSIX (BSD).

---

# Architettura Android

- SO basato su Linux kernel (modificato) quindi **monolitico**.
- Sopra il kernel (user space) è presente un ambiente software composto:
  - framework Android e runtime ART per eseguire le applicazioni.
  - strato **HAL (hardware abstraction layer)** astrae l’hardware dei diversi dispositivi.

**Gerarchia Software Android:**
Applicazioni
$\downarrow$
Application Framework
$\downarrow$
Android Runtime (ART) + Native Libraries
$\downarrow$
HAL (hardware abstraction layer)
$\downarrow$
Linux Kernel
$\downarrow$
Hardware