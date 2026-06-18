---
type: concept
title: File Locking
tags: [sincronizzazione, file-system, kernel]
related: [open-file-table, file-control-block-fcb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# File Locking

Il **File Locking** è un meccanismo di sincronizzazione fornito dal sistema operativo per prevenire *race condition* durante l'accesso concorrente a un file da parte di più processi.

## Tipi di Lock
- **Shared Lock (Lettura)**: Simile a un *reader lock*, permette a più processi di accedere contemporaneamente al file in modalità lettura.
- **Exclusive Lock (Scrittura)**: Simile a un *writer lock*, garantisce l'accesso esclusivo a un solo processo per le operazioni di scrittura.

## Confronto con i Mutex
Il file locking è significativamente più costoso di un mutex tra thread per diverse ragioni:
- **Spazio di esecuzione**: I mutex operano quasi interamente nello *user-space*, mentre il file locking richiede una *system call*.
- **Intervento del Kernel**: Il locking coinvolge il kernel e la gestione del VFS (*Virtual File System*).
- **Granularità**: Il locking è necessario per la sicurezza tra processi indipendenti, mentre i mutex sono ottimizzati per la velocità all'interno di un singolo processo.

In sistemi Unix, il locking può essere gestito tramite syscall come `flock()` o `fcntl()`.