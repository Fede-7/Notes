# Sistemi Operativi — Stesura Unica (ordine di studio)

## Obiettivo
Raccogliere in un unico file tutti gli argomenti di Sistemi Operativi seguendo l'ordine di studio delle lezioni.

## Lezione 0 — Fondamenti
- Informazioni sul corso, riferimenti, esame e strumenti
- Cos'è un Sistema Operativo e obiettivi principali
- Struttura a strati del SO
- Kernel vs programmi di sistema
- Storia dei sistemi operativi (dalle origini al mobile)
- Architettura di base del calcolatore
- Meccanismo delle interruzioni

## Lezione 1 — Servizi del SO e system call
- Servizi del sistema operativo
- Interfacce utente
- Gerarchia API → ABI → System Call
- Passaggio parametri al kernel
- Struttura software del sistema
- Policy vs meccanismo
- Prime distinzioni sulla struttura del kernel

## Lezione 2 — Virtualizzazione, kernel e processi
- Emulazione software e virtualizzazione
- Hypervisor tipo 1 vs tipo 2
- Ring di protezione
- Paradigmi di progettazione del kernel (monolitico, stratificato, microkernel, modulare, ibrido)
- Processo: definizioni e layout di memoria
- Ciclo di vita dei processi
- PCB, context switch e introduzione alla schedulazione

## Lezione 3 — IPC e memoria condivisa
- Formato eseguibili e spazio di indirizzamento virtuale
- Operazioni sui processi: fork, exec, wait
- Processi zombie, orfani e terminazione
- Comunicazione tra processi (IPC)
- Problema produttore-consumatore
- Buffer bounded/circolare

## Lezione 4 — Shell Unix e compilazione
- Cos'è la shell e funzionamento
- Tipi di shell
- Variabili di shell e variabili d'ambiente
- Redirezione I/O e pipe
- Comandi fondamentali del file system
- Processo di compilazione da sorgente a eseguibile

## Lezione 5 — Thread e modelli di mapping
- Benefici dei thread
- Concorrenza vs parallelismo
- Legge di Amdahl
- User thread vs kernel thread
- Modelli many-to-one, one-to-one, many-to-many, two-level
- Lightweight process e upcall
- Libreria POSIX pthreads (funzioni principali)

## Lezione 6 — Scheduling CPU
- CPU scheduler e dispatcher
- Criteri di scheduling
- Algoritmi tradizionali: FCFS, SJF, SRTF, priorità, RR, code multiple, feedback
- Scheduling real-time: RMS, EDF
- Scheduling thread e multiprocessori
- Cenni a virtualizzazione e scheduling

## Lezione 7 — Signal handling e cancellazione thread
- Signal handling in contesto multithread
- Maschere segnali e comportamento dei thread
- Cancellazione thread e cancellation point
- TID user-level vs kernel-level
- Introduzione allo scheduling CPU

## Lezione 8 — Real-time e Linux scheduler
- Processi real-time
- Event latency e dispatch latency
- Task periodici
- RMS (con limite di utilizzo)
- EDF (anche con deadline ≠ periodo)
- Evoluzione scheduler Linux: O(n), O(1), CFS, EEVDF
- Scheduling multicore

## Lezione 9 — Scheduling avanzato
- Riepilogo SJF e media esponenziale
- SRTF (SJF preemptive)
- Scheduling a priorità
- Round-Robin e scelta del quanto
- Priorità + RR
- Multi-Level Queue e Multi-Level Feedback Queue
- Cenni multicore

## Lezione 10 — Valutazione scheduling e sincronizzazione
- Metodi di valutazione algoritmi di scheduling
- Motivazione del problema di sincronizzazione
- Problema della sezione critica
- Soluzione di Peterson (e generalizzazione)
- Memory barriers
- Supporto hardware: test-and-set, compare-and-swap

## Lezione 11 — Sincronizzazione avanzata
- Bounded waiting (ripasso)
- Increment lock-free con CAS
- Spin lock vs mutex
- Semafori (binari e contatori)
- Produttore-consumatore con semafori
- Monitor e variabili di condizione
- Deadlock e problemi di liveness
- Priority inversion e priority inheritance
- Strutture lock-free

## Lezione 12 — Condition variable, monitor e deadlock
- Condition variable: operazioni e invarianti
- Pattern monitor
- Problema dei 5 filosofi
- Soluzione con condition variable
- Signal vs broadcast
- Deadlock: definizione, cause e condizioni di Coffman
- Esempi di deadlock
- Strategie di prevenzione

## Lezione 13 — Thread, race condition e mutex
- Thread con pthread
- Race condition su contatore condiviso
- Sezione critica
- Mutex lock/unlock
- Implementazione corretta con mutua esclusione
- Esercitazione pratica e confronto con implementazione naive
