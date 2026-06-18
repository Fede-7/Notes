---
type: source
title: "SO1 Lezione 2b - Servizi e Chiamate di Sistema"
tags: [SO1, sistemi-operativi, system-calls, servizi]
related: [system-call, posix-api, kernel, passaggio-parametri, abi, wrapper-di-libreria]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2b-AA25-26.txt"]
authors: []
year: 2025
url: ""
venue: ""
---
# SO1 Lezione 2b - Servizi e Chiamate di Sistema

Questa lezione approfondisce i servizi forniti dai sistemi operativi e i meccanismi tecnici attraverso cui i programmi utente interagiscono con il kernel.

## Servizi del Sistema Operativo
Il sistema operativo fornisce un ambiente per l'esecuzione di programmi e servizi per utenti e applicazioni. I principali servizi includono:
- **Interfaccia Utente**: CLI (Command-Line Interface), GUI (Graphics User Interface), interfacce touch-screen e comandi vocali.
- **Esecuzione di Programmi**: Caricamento in memoria, esecuzione, terminazione (normale o anomala).
- **Operazioni I/O**: Astrazione della complessità dell'hardware per fornire interfacce uniformi.
- **Gestione File-system**: Lettura, scrittura, creazione, eliminazione e gestione dei permessi.
- **Comunicazione**: Scambio di informazioni tra processi (locale o in rete).
- **Rilevamento di Errori**: Monitoraggio di CPU, memoria, dispositivi I/O e programmi utente.
- **Allocazione delle Risorse**: Gestione di cicli CPU, memoria principale, file e dispositivi I/O.
- **Contabilità (Accounting)**: Tracciamento dell'utilizzo delle risorse da parte degli utenti.
- **Protezione e Sicurezza**: Controllo degli accessi interni (protezione) e difesa da accessi esterni (sicurezza/autenticazione).

## Accesso ai Servizi e System Call
I processi utente accedono ai servizi del kernel tramite **System Call**. Il flusso tipico di esecuzione è:
`Programma Utente` $\rightarrow$ `API (es. POSIX)` $\rightarrow$ `Libreria (es. libc)` $\rightarrow$ `System Call` $\rightarrow$ `Kernel`.

### API e ABI
- **API (Application Programming Interface)**: Specifica le funzioni disponibili per il programmatore (es. `read()`).
- **ABI (Application Binary Interface)**: Interfaccia a livello binario tra i programmi utente e il sistema operativo.

### Passaggio dei Parametri
Esistono tre metodi principali per trasmettere dati al kernel:
1. **Registri**: Passaggio diretto (es. architettura x86-64).
2. **Blocchi di Memoria**: Indirizzo del blocco passato in un registro (usato in Linux e Solaris).
3. **Stack**: Parametri inseriti nello stack dal programma e estratti dal SO.

## Dettagli Tecnici x86-64
In sistemi moderni come GNU/Linux su x86-64, le system call utilizzano i registri per efficienza:
- `rax`: Numero della syscall o valore di ritorno.
- `rdi`, `rsi`, `rdx`, `r10`, `r8`, `r9`: Argomenti da 0 a 5.

Esempio di flusso per `read()`:
1. Il programma C chiama `read()` (utilizzando lo stack per la chiamata alla funzione della libreria).
2. Il **wrapper di libreria** (`libc`) sposta i parametri nei registri corretti.
3. Viene eseguita l'istruzione `syscall`.
4. Il kernel esegue l'operazione e restituisce il risultato in `rax`.