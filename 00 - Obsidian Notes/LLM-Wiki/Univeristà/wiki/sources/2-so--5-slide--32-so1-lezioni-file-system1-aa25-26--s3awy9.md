---
type: source
title: "Lezioni File System 1 - AA25-26"
tags: [file-system, lezione, SO1]
related: [file-system, inode, journaling, copy-on-write]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: ""
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Lezioni File System 1 - AA25-26

Questa fonte fornisce una panoramica dettagliata dei concetti fondamentali dei **File System** all'interno dei sistemi operativi. Il materiale copre:

- **Basi dei File**: Definizione di file come unità logiche, attributi (nome, dimensione, protezione, timestamp) e operazioni fondamentali (Create, Open, Read, Write, ecc.).
- **Gestione dei File Aperti**: Utilizzo di tabelle di sistema e per-processo, inclusi i concetti di [[file-descriptor]] e [[file-control-block-fcb]].
- **Strutture di Directory**: Evoluzione dalle strutture a livello singolo a quelle ad albero e a grafo (aciclico e generale).
- **Architettura Unix/Linux**: Il principio [[everything-is-a-file]], l'uso degli [[inode]] e la distinzione tra file ordinari e file speciali.
- **Allocazione dello Spazio**: Analisi delle strategie di allocazione (contigua, concatenata, indicizzata) e dei relativi compromessi tra prestazioni e frammentazione.
- **Sistemi di File Specifici**: Panoramica su FAT, UNIX UFS, serie EXT (EXT2, EXT3, EXT4) e NTFS.
- **Ottimizzazione e Consistenza**: Tecniche di caching, [[journaling]], [[copy-on-write]], e strategie di backup.