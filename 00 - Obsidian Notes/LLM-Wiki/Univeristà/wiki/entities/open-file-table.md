---
type: entity
title: Open-File Table
tags: [kernel, file-system, unix]
related: [file-descriptor, file-control-block-fcb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Open-File Table

L'**Open-File Table** è una struttura dati utilizzata dal kernel del sistema operativo per tracciare tutti i file attualmente aperti nel sistema. Per ottimizzare le prestazioni e gestire la concorrenza, il sistema utilizza una struttura a due livelli:

1.  **Tabella per-processo**: Ogni processo mantiene una tabella privata che mappa i [[file-descriptor]] (indici numerici) alle voci della tabella di sistema. Questa tabella contiene informazioni specifiche per il processo, come il puntatore di lettura/scrittura corrente (*offset*).
2.  **Tabella di sistema**: Contiene le informazioni globali sul file aperto, inclusi i metadati del file e il puntatore al [[file-control-block-fcb]].

Questa architettura permette di evitare scansioni ripetute del disco per ogni operazione di I/O, poiché le informazioni necessarie sono mantenute in memoria principale una volta che il file è stato aperto.