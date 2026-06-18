---
type: overview
title: Index
tags: [index]
related: []
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Index

## Entities
- [[alberto-finzi]] — Docente responsabile del corso SO1.
- [[file-system]] — Sistema per l'accesso efficiente ai file in memoria di massa.
- [[inode]] — Struttura Unix/Linux che contiene i metadati di un file (escluso il nome).
- [[file-control-block-fcb]] — Blocco contenente metadati e posizione fisica del file.
- [[file-descriptor]] — Indice numerico assegnato a un processo per identificare un file aperto.
- [[open-file-table]] — Struttura di sistema (e per-processo) utilizzata dal kernel per tracciare i file aperti.
- [[fat]] — Struttura di tabella utilizzata in MSDOS per gestire l'allocazione concatenata.
- [[unix-ufs]] — Schema combinato di allocazione utilizzato nei sistemi Unix.
- [[ext2]] — File system Linux che utilizza block groups per migliorare la località dei dati.
- [[ext3]] — Evoluzione di EXT2 con supporto per il journaling.
- [[ext4]] — File system moderno con supporto per file grandi (16 TiB), allocazione multiblocco e inode da 256 byte.
- [[ntfs]] — File system di Windows basato su cluster, journaling e Master File Table (MFT).
- [[master-file-table-mft]] — Struttura di metadati di NTFS che contiene informazioni su file, log e bitmap.
- [[lwp]] — Lightweight Process, struttura intermedia per la gestione dei thread.
- [[openmp]] — Framework per la programmazione parallela in ambienti shared-memory.
- [[grand-central-dispatch]] — Framework di gestione dei task sviluppato da Apple.
- [[clone]] — Chiamata di sistema utilizzata da Linux per creare nuovi task (processi o thread).
- [[task_struct]] — Struttura dati del kernel Linux che rappresenta un processo o un thread.
- [[ethread]] — Blocco di dati del thread nello spazio utente in Windows.
- [[kthread]] — Blocco di dati del thread nello spazio kernel in Windows.
- [[teb]] — Thread Environment Block, struttura dati nello spazio utente di Windows.
- [[vmware]] — Strumento software per la creazione di macchine virtuali.
- [[wsl]] — Windows Subsystem for Linux.
- [[fork()]] — Chiamata di sistema per duplicare il processo corrente.
- [[exec()]] — Chiamata di sistema per sostituire il corpo del programma in esecuzione.
- [[wait()]] — Costrutto di sincronizzazione per permettere a un processo padre di attendere la fine di un processo figlio.
- [[bash]] — Shell di comando utilizzata come standard per le esercitazioni.
- [[posix]] — Standard *Portable Operating System Interface* per sistemi Unix-like.
- [[java-api]] — Interfaccia di alto livello per il linguaggio Java, che aggiunge un ulteriore strato di astrazione sopra le chiamate di sistema.

## Concepts
- [[ambiente-posix]] — Requisiti tecnici e standard per l'ambiente di lavoro del corso.
- [[allocazione-contigua]] — I blocchi di un file sono adiacenti; offre alte prestazioni ma soffre di frammentazione esterna.
- [[allocazione-concatenata]] — I blocchi sono collegati tramite puntatori; evita la frammentazione esterna ma è inefficiente per l'accesso diretto.
- [[allocazione-indicizzata]] — Ogni file ha un blocco indice contenente puntatori ai blocchi di dati; permette accesso diretto ma può causare frammentazione interna per file piccoli.
- [[block-groups]] — Organizzazione del disco in gruppi per mantenere vicini inode e blocchi dati, riducendo la frammentazione.
- [[buffer-cache-unificata]] — Integrazione della cache del file system con il sistema di memoria virtuale per eliminare il double caching.
- [[copy-on-write]] — Tecnica di consistenza che evita la sovrascrittura dei metadati scrivendo i nuovi valori in blocchi nuovi.
- [[everything-is-a-file]] — Filosofia Unix che fornisce un'interfaccia uniforme per file e dispositivi.
- [[journaling]] — Meccanismo di consistenza che registra le modifiche ai metadati in un log sequenziale (transazioni) prima di applicarle effettivamente.
- [[parallelismo-di-dati]] — Distribuzione di sottoinsiemi di dati su più core con la stessa operazione.
- [[parallelismo-di-task]] — Distribuzione di operazioni diverse su thread differenti.
- [[programmazione-parallela-shared-memory]] — Modello di parallelismo dove i thread condividono lo stesso spazio di memoria.
- [[strutture-di-directory]] — Evoluzione da Single-level a Tree-structured e Graph (Acyclic/General).
- [[segnali-standard]] — Segnali collassati utilizzati per comunicazioni semplici.
- [[segnali-real-time]] — Segnali accodati in FIFO per comunicazioni più complesse.
- [[signal-handling]] — Meccanismo di comunicazione asincrona tramite "interruzioni software".
- [[thread-switching]] — Cambio di contesto tra thread, con overhead inferiore rispetto al context switching tra processi.
- [[threading-implicito]] — Gestione dei thread delegata a compilatori o runtime, dove il programmatore definisce task anziché thread.
- [[thread-pool]] — Struttura di thread pre-creati che attendono task, ottimizzando la velocità di risposta e limitando le risorse.
- [[thread-specific-data]] — Area di memoria privata per ogni thread, indicizzata da chiavi.
- [[unificazione-task-thread]] — Approccio del kernel Linux che tratta processi e thread come entità uniformi.
- [[cancellazione-thread]] — Meccanismi per terminare un thread (Asincrona vs Differita).
- [[cancellation-point]] — Punti specifici nel codice dove un thread può essere interrotto.
- [[programma-corso-so1]] — Roadmap didattica e obiettivi del corso di Sistemi Operativi I.
- [[livelli-di-astrazione]] — Gerarchia che separa le applicazioni dall'hardware tramite API, librerie e chiamate di sistema.
- [[file-locking]] — Meccanismo di sincronizzazione (Shared vs. Exclusive) per prevenire race condition durante l'accesso concorrente; più costoso di un mutex poiché coinvolge il kernel e il VFS.
- [[accesso-sequenziale-vs-diretto]] — Modelli di accesso: il primo segue un ordine lineare (nastro), il secondo permette di saltare a posizioni specifiche (disco).
- [[link-simbolici-vs-hard-link]] — I link simbolici puntano a un percorso (path), mentre i link "hard" (comandi `link`) condividono lo stesso i-number.
- [[file-speciali]] — In Unix, dispositivi (carattere, blocchi, socket, pipe) sono trattati come file per fornire un'interfaccia uniforme.
- [[protezioni-e-permessi]] — Modello di accesso basato su tre classi: Proprietario (Owner), Gruppo, Pubblico (Public).
- [[identificazione-utenti-e-gruppi]] — Identificazione degli utenti tramite UID e dei gruppi tramite GID per la gestione della sicurezza.

## Sources
- [[2-so--5-slide--25-so1-presentazione-aa25-26--tete96]] — Presentazione introduttiva del corso SO1 AA25-26.
- [[SO/Trascrizioni/Lezione 1.txt]] — Trascrizione della prima lezione sui fondamenti dei sistemi operativi.
- [[2-so--5-slide--23-so1-lezione-fs1-aa25-26--5anxnm]] — Slide sulla lezione dei File System.

## Current Overview
---
type: overview
title: Project Overview
tags: [SO1, Sistemi Operativi]
related: []
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 0.txt", "SO/Slide/Nuova cartella/SO1-Presentazione-AA25-26.txt", "SO/Trascrizioni/Lezione 11.txt", "SO/Trascrizioni/Lezione 14.txt", "SO/Trascrizioni/Lezione 16.txt", "SO/Slide/SO1-Lezione-deadlock-AA25-26.txt", "SO/Slide/SO1-Lezione1-AA25-26.txt", "SO/Slide/SO1-Presentazione-AA25-26.txt", "SO/Trascrizioni/Lezione 10.txt", "SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Overview

Questo wiki documenta lo studio del corso di Sistemi Operativi I (SO1), tenuto da Alberto Finzi. L'obiettivo è comprendere i concetti fondamentali dei sistemi operativi, come la gestione dei processi, la memoria virtuale e il deadlock, utilizzando testi accademici standard (Silberschatz et al., Tanenbaum & Bos) e materiali forniti dal corso stesso.

Il wiki copre la teoria dei deadlock, inclusa la caratterizzazione tramite le Condizioni di Coffman, le rappresentazioni grafiche (RAG e Wait-for Graph), e le diverse strategie di gestione: prevenzione (es. Lock Ordering), evitamento (es. Algoritmo del Banchiere e Stato Sicuro) e rilevamento/ripristino. 

Inoltre, il wiki include le basi storiche e architettoniche dei sistemi operativi:
- **Evoluzione Storica**: Dalle valvole e sistemi batch (IBM 7094) alla multiprogrammazione, fino ai moderni sistemi mobili.
- **Concetti Architetturali**: Il Sistema Operativo come allocatore di risorse e "Macchina Estesa", la gestione delle interruzioni (Interrupt Driven, Interrupt Vector), e le tecniche di I/O come Buffering e Spooling.
- **Protezione e Modalità**: Il funzionamento della Dual Mode (User vs Kernel Mode) e l'uso delle System Call per l'accesso alle risorse.
- **Strumenti Pratici**: L'uso di standard POSIX, mutex e strumenti di monitoraggio come il BCC toolkit su sistemi Linux.

**Nuovi contenuti aggiunti**:
- **Struttura del Corso**: Definizione del programma di massima suddiviso in 5 macro-aree (Introduzione, Processi, Memoria, Sistemi I/O, Dati permanenti).
- **Requisiti di Ambiente**: Specifiche sull'ambiente POSIX e sull'uso di strumenti come WSL e VMware per la compatibilità tra piattaforme.
- **Riferimenti Bibliografici**: Inclusione dei testi di Silberschatz, Galvin e Gagne e Tanenbaum e Bos come pilastri teorici del corso.
- **Sincronizzazione e Schedulazione**: Analisi delle metodologie di valutazione della schedulazione (deterministica, modelli di coda, real-time) e dei meccanismi di sincronizzazione dei thread (sezione critica, problema produttore-consumatore, istruzioni atomiche come *compare-and-swap*).
- **Sincronizzazione Avanzata e Priorità**: Studio delle istruzioni atomiche `test-and-set`, dei `spin-lock` e del *busy waiting*, dei semafori di Dijkstra (binari e contatori), dei monitor e delle variabili di condizione. Analisi dei problemi di *priority inversion* e della soluzione tramite *priority inheritance*, oltre alle proprietà di *liveness* (*bounded waiting* e *starvation*).
- **File Systems**: Studio dei concetti di file come unità logiche, attributi, operazioni standard, strutture delle directory (alberi, grafi), link simbolici vs hard link, e meccanismi di locking e protezione.