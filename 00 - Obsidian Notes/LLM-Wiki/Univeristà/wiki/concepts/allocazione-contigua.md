---
type: concept
title: Allocazione Contigua
tags: [file-system, storage]
related: [allocazione-concatenata, allocazione-indicizzata]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Allocazione Contigua

L'**allocazione contigua** è una strategia in cui i blocchi di un file vengono allocati in posizioni adiacenti sul supporto di memoria di massa.

### Vantaggi
- **Prestazioni elevate**: L'accesso diretto è molto veloce poiché l'indirizzo fisico può essere calcolato matematicamente (Base + Offset).
- **Efficienza di lettura**: Ottimale per la lettura sequenziale grazie alla vicinanza fisica dei dati.

### Svantaggi
- **Frammentazione Esterna**: Con il tempo, lo spazio libero si frammenta in piccoli "buchi" non utilizzabili per file grandi.
- **Difficoltà di espansione**: Se lo spazio adiacente è occupato, il file non può crescere anche se c'è spazio libero altrove.
