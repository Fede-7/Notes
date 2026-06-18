---
type: concept
title: File Hole (Buco)
tags: [file-system, storage]
related: [lseek, dimensione-logica-vs-fisica]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
Un "buco" (*hole*) in un file è una rappresentazione logica di un vuoto all'interno di un file che non occupa spazio fisico sul disco. 

Viene creato spostando la testina del file con `lseek()` oltre la fine attuale senza scrivere dati. Il sistema operativo registra la dimensione logica aggiornata, ma non alloca blocchi fisici per la porzione vuota, ottimizzando l'uso dello spazio di archiviazione.