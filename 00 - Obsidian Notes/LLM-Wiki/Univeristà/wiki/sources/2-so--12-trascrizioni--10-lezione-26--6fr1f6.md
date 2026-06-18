---
type: source
title: "Lezione 26: Driver di dispositivo, TTY/PTY e Moduli Kernel"
tags: [SO1, kernel, driver, TTY, PTY]
related: [tty, pty, hello-driver, kernel-space-vs-user-space, vfs-abstraction]
created: 2026-06-17
updated: 2026-06-17
authors: [Alberto Finzi]
year: 2026
url: ""
venue: "Corso Sistemi Operativi I"
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# Lezione 26: Driver di dispositivo, TTY/PTY e Moduli Kernel

Questa lezione approfondisce il funzionamento dei driver di dispositivo all'interno del kernel Linux, la gestione dei terminali (TTY e PTY) e le basi della programmazione di moduli kernel.

## Argomenti Principali
- **Rappresentazione dei Dispositivi**: Analisi di come i dispositivi siano trattati come file tramite il Virtual File System (VFS).
- **Tipologie di Dispositivi**: Distinzione tra dispositivi a carattere (Character Devices) e dispositivi a blocco (Block Devices).
- **Identificazione dei Driver**: Meccanismo dei *Major* e *Minor numbers* per distinguere i driver e le loro istanze.
- **Architettura dei Terminali**: Studio dei dispositivi TTY, dei Pseudo-Terminali (PTY) e del loro accoppiamento master-slave.
- **Line Discipline**: Il ruolo degli interpreti software nell'elaborazione dei flussi di dati dei terminali.
- **Kernel vs User Space**: Isolamento degli spazi di indirizzamento e necessità di funzioni di copia esplicite (`copy_to_user`, `copy_from_user`).
- **Sviluppo di Moduli Kernel**: Compilazione, registrazione (`insmod`) e rimozione (`rmmod`) di moduli dinamici.
- **Interfacce di Callback**: Come il kernel mappa le operazioni standard sui file (read, write, ecc.) alle funzioni specifiche del driver tramite la struttura `file_operations`.
