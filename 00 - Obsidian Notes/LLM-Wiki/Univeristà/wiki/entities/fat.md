---
type: entity
title: FAT (File Allocation Table)
tags: [msdos, file-system, history, storage]
related: [unix-ufs, allocazione-concatenata, file-control-block-fcb, ntfs]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt", "SO/Trascrizioni/Lezione 24.txt"]
---
# FAT (File Allocation Table)

La **File Allocation Table (FAT)** è una struttura di tabella utilizzata per mappare la posizione dei blocchi dei file. È stata storicamente utilizzata nei sistemi MS-DOS, nelle versioni precedenti di Windows e rimane comune in molti dispositivi di memoria rimovibile (es. chiavette USB).

### Meccanismo
- Utilizza un modello di **allocazione concatenata**: ogni voce nella tabella contiene il numero del blocco successivo.
- Se un file termina, la voce della tabella contiene un valore speciale (es. `EOF`).

### Caratteristiche e Limiti
- Sebbene semplice, la FAT può soffrire di frammentazione.
- Non è efficiente per l'accesso diretto ai dati.