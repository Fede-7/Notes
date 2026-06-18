---
type: entity
title: Inode
tags: [linux, unix, file-system]
related: [file-system, everything-is-a-file]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Inode

In architetture Unix e Linux, l'**inode** (index node) è una struttura dati che contiene tutti i metadati di un file, ad eccezione del suo nome.

### Caratteristiche
- **Contenuto**: Include informazioni come il proprietario, i permessi, la dimensione del file, i timestamp (accesso, modifica, creazione) e i puntatori ai blocchi di dati fisici.
- **Identificazione**: Ogni file o directory ha un numero di inode univoco all'interno di una partizione.
- **Separazione Nome-Metadati**: Il nome di un file è memorizzato all'interno di una struttura di directory, che mappa il nome all'ID dell'inode corrispondente.
