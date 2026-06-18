---
type: concept
title: Gestione NAND Flash
tags: [hardware, ssd, nand-flash]
related: [ftl]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Gestione NAND Flash

La **gestione NAND Flash** riguarda le tecniche necessarie per gestire le limitazioni fisiche della memoria flash, che non permette la sovrascrittura diretta dei dati.

### Tecniche Chiave
- **Garbage Collection**: Spostamento dei dati validi da blocchi "sporchi" a blocchi liberi per permettere la cancellazione del blocco.
- **Wear Leveling**: Distribuzione uniforme delle operazioni di scrittura su tutte le celle della memoria per evitare il deterioramento precoce di aree specifiche.
- **Overprovisioning**: Riserva di spazio non accessibile all'utente per migliorare le prestazioni della garbage collection e la longevità del dispositivo.