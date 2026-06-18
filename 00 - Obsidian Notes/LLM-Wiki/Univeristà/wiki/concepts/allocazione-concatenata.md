---
type: concept
title: Allocazione Concatenata
tags: [file-system, storage]
related: [allocazione-contigua, allocazione-indicizzata]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Allocazione Concatenata

L'**allocazione concatenata** prevede che ogni blocco di un file contenga un puntatore al blocco successivo.

### Vantaggi
- **Nessuna frammentazione esterna**: Può utilizzare qualsiasi blocco libero sul disco.
- **Facilità di espansione**: Un file può crescere semplicemente aggiungendo un nuovo blocco alla fine della catena.

### Svantaggi
- **Accesso Diretto inefficiente**: Per leggere il blocco $n$, il sistema deve scorrere tutti i puntatori dai blocchi precedenti.
- **Affidabilità**: Se un puntatore viene danneggiato, la parte successiva del file diventa irrecuperabile.
