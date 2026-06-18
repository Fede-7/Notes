---
type: source
title: "Lezione 23 - Chiamate di Sistema I/O e Gestione File"
tags: [so1, i/o, file-system]
related: [open, read, write, close, lseek, pipe, stat, ereditarietà-dei-file-descriptor, offset-condiviso, dimensione-logica-vs-fisica, file-hole]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
Questa trascrizione della Lezione 23 del corso di Sistemi Operativi I analizza le chiamate di sistema POSIX fondamentali per l'I/O di basso livello e la gestione dei file. 

I temi principali includono:
- **Chiamate di Sistema POSIX**: Analisi dettagliata di `open()`, `read()`, `write()`, `close()` e `lseek()`.
- **Gestione dei File Descriptor**: Il comportamento dei descrittori di file durante la duplicazione dei processi tramite `fork()`, con particolare attenzione all'ereditarietà e alla condivisione degli offset.
- **Struttura e Accesso ai Dati**: Il percorso gerarchico dal file descriptor ai blocchi fisici sul disco.
- **Proprietà dei File**: Distinzione tra dimensioni logiche e fisiche, gestione dei "buchi" (holes) nei file e rappresentazione dei permessi in formato ottale.
- **Confronto IPC**: Analisi delle differenze tra la comunicazione tramite file (sincronizzazione esplicita) e tramite `pipe` (sincronizzazione implicita).