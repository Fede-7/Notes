---
type: entity
title: File Control Block (FCB)
tags: ["os", "file-system", "kernel"]
related: ["file-descriptor", "file-system", "fat", "inode"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt", "SO/Trascrizioni/Lezione 24.txt"]
---
# File Control Block (FCB)

Il **File Control Block (FCB)** è una struttura dati utilizzata dal kernel per mantenere le informazioni necessarie per gestire un file. Essa contiene i metadati di un file e la sua posizione fisica.

### Caratteristiche e Informazioni Dinamiche
Mentre l'[[inode]] contiene i metadati persistenti memorizzati sul disco, l'FCB è progettato per contenere informazioni dinamiche necessarie durante l'esecuzione del sistema, come:
- Puntatore alla posizione attuale di lettura/scrittura.
- Stato del file (ad esempio, se è aperto, condiviso, ecc.).
- Buffer di caching associati.

### Implementazioni Specifiche
In sistemi di file basati su **FAT**, l'FCB funge da punto di ingresso per individuare la prima entry della tabella di allocazione.