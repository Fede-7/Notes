---
type: source
title: "Lezione 24: Allocazione File System e Bootstrapping"
tags: [file-system, bootstrapping, architettura-computer]
related: [file-system, block-groups, journaling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 24.txt"]
authors: []
year: 2026
url: ""
venue: ""
---
# Lezione 24: Allocazione File System e Bootstrapping

Questa lezione approfondisce i meccanismi di allocazione dei blocchi di file su memoria secondaria, analizzando i compromessi tra prestazioni, frammentazione e complessità di gestione.

## Argomenti Principali
- **Metodi di Allocazione**:
    - **Contigua**: Blocchi adiacenti; offre alte prestazioni per l'accesso diretto ma soffre di frammentazione esterna.
    - **Concatenata**: Blocchi collegati tramite puntatori; evita la frammentazione esterna ma rende l'accesso diretto inefficiente (problema della "caccia al tesoro").
    - **Indicizzata**: Ogni file ha un blocco indice; permette l'accesso diretto e viene utilizzata dai sistemi Unix/Linux.
- **Strutture di Tabella**: Analisi della **File Allocation Table (FAT)**, utilizzata in MS-DOS e dispositivi USB, e della **Master File Table (MFT)** di NTFS.
- **Gestione dello Spazio Libero**: Tecniche come `bit-vector-allocation`, `linked-list-allocation` e `grouping-allocation`.
- **Bootstrapping**: Processo di inizializzazione dell'hardware tramite BIOS/UEFI e strutture di partizionamento come MBR e GPT.
- **Ottimizzazioni del File System**:
    - **Block Groups**: Organizzazione dei dati per migliorare la località spaziale.
    *   **Journaling**: Meccanismi di consistenza per i metadati.
    *   **Caching**: Risoluzione del *double caching* tramite `buffer-cache-unificata`.
    *   **Write-back**: Scrittura asincrona per migliorare le prestazioni.