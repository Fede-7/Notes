---
type: source
title: "Lezione 25 - Architettura File System e I/O"
tags: [SO1, file-system, I/O, kernel]
related: [file-system, journaling, device-driver, io-stratification]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
# Lezione 25 - Architettura File System e I/O

Questa lezione approfondisce l'architettura interna dei sistemi di file e la gestione del sottosistema I/O nel kernel.

## Architettura dei File System
Vengono discussi i meccanismi per garantire la consistenza dei dati e le prestazioni:
- **Gestione della Memoria**: Differenze tra algoritmi di sostituzione pagina per la memoria anonima e per i file.
- **Scrittura Sincrona vs Asincrona**: Analisi dei vantaggi delle scritture asincrone per ottimizzare i tempi di trasferimento.
- **Journaling**: Tecniche di "registrazione anticipata" delle modifiche ai metadati (es. in EXT3, EXT4, NTFS) per facilitare il recupero in caso di crash.
- **Stratificazione**: L'architettura a livelli del file system (Logical File System, File Organization Module, Basic File System, I/O Control) che permette la modularità e l'astrazione.

## Gestione dei File nel Kernel
Analisi del flusso delle chiamate di sistema `open`, `close` e `read`, con particolare attenzione a:
- **Tabelle dei File Aperti**: Distinzione tra tabelle per-processo e tabelle system-wide.
- **File Control Block (FCB)**: Ruolo nella cache dei file.
- **Separazione Nomi-Attributi**: Il concetto che il nome sia un collegamento mantenuto dalla directory, mentre il file possiede un identificatore interno.

## Sottosistema I/O e Driver
Studio dell'astrazione hardware:
- **Classificazione Dispositivi**: Distinzione tra dispositivi a blocco, a carattere, di rete e timer.
- **Device Driver**: Ruolo dei driver nel kernel (Ring 0) e la loro funzione di incapsulamento delle differenze hardware.
- **Meccanismi di Comunicazione**: Uso di interrupt, DMA, MMU e il comando `ioctl`.
- **Terminali e Socket**: Gestione di TTY, pseudo-terminali (PTY), line discipline e primitive di comunicazione di rete.

## Logistica dell'Esame
Il docente chiarisce che l'esame scritto si concentrerà sulla teoria e su compiti di programmazione pratica ("to-do"), mentre il progetto di laboratorio non sarà il focus principale.