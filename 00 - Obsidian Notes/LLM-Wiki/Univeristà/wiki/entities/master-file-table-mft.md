---
type: entity
title: Master File Table (MFT)
tags: [windows, ntfs, file-system]
related: [ntfs]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt", "SO/Trascrizioni/Lezione 24.txt"]
---
# Master File Table (MFT)

La **Master File Table (MFT)** è la struttura di metadati centrale del file system NTFS. Essa funge da database per il file system, contenendo informazioni su ogni file e directory nel volume.

### Funzioni e Contenuti
La MFT memorizza una vasta gamma di informazioni necessarie alla gestione del volume, tra cui:
- **Metadati dei file:** nome, dimensione, permessi, timestamp e puntatori ai dati fisici.
- **Strutture di sistema:** log e bitmap.

### File Residenti
In NTFS, quasi tutto è memorizzato nella MFT. Tuttavia, se un file è molto piccolo, i suoi dati possono essere memorizzati direttamente all'interno della MFT; in questo caso, il file è definito **residente**.