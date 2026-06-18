---
type: concept
title: System Call
tags: ["interfaccia", "kernel", "so", "api", "trap-exception", "dual-mode", "user-mode", "kernel-mode", "posix-api.md", "libc", "trap"]
related: ["trap-exception", "dual-mode", "user-mode", "kernel-mode", "posix-api.md", "libc", "trap"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione1-AA25-26.txt", "SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# Chiamate di Sistema (System Calls)

Le **chiamate di sistema** costituiscono l'interfaccia fondamentale tra i programmi in *user mode* e i servizi gestiti dal **Kernel**. Sono istruzioni specifiche che richiedono al sistema operativo di eseguire operazioni privilegiate, come l'accesso a file, la gestione della rete o l'interazione con i dispositivi.

Ogni chiamata di sistema genera un'interruzione del processo che passa il controllo dal programma utente al kernel in modalità privilegiata tramite un *Trap* hardware.

## Gerarchia di Accesso
L'accesso ai servizi segue una gerarchia di astrazione che permette ai programmi di interagire con l'hardware in modo sicuro e portabile:

1. **Programma Utente**: L'applicazione che richiede il servizio.
2. **API / Librerie**: Forniscono funzioni portabili e semplici (es. `libc`, POSIX) che astraggono le chiamate di sistema.
3. **System Call**: L'interfaccia effettiva che genera il *Trap* hardware per passare il controllo al kernel.
4. **Kernel**: Esegue l'operazione effettiva e restituisce il risultato al programma.

## Tipi di System Call
Le system call sono generalmente categorizzate in tre aree principali:

- **Controllo di processi**: Creazione (`fork`, `vfork`), terminazione, attendere (`wait`), gestione attributi, allocazione memoria e debug.
- **Gestione di File**: Creazione, eliminazione, apertura, chiusura, lettura, scrittura e manipolazione degli attributi.
- **Gestione di Dispositivi**: Richiesta, rilascio, lettura, scrittura e gestione degli attributi dei dispositivi hardware.