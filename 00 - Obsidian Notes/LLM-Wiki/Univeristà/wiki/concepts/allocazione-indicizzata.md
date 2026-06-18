---
type: concept
title: Allocazione Indicizzata
tags: [file-system, storage]
related: [allocazione-contigua, allocazione-concatenata]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# Allocazione Indicizzata

L'**allocazione indicizzata** utilizza un blocco speciale, chiamato **indice** (o inode), che contiene puntatori a tutti i blocchi di dati del file.

### Vantaggi
- **Accesso Diretto efficiente**: È possibile saltare direttamente al blocco desiderato tramite l'indice.
- **Flessibilità**: Supporta file di varie dimensioni senza i limiti della concatenazione.

### Svantaggi
- **Frammentazione Interna**: Può verificarsi se i blocchi di indice sono grandi e il file è piccolo.
- **Overhead**: Richiede spazio aggiuntivo per memorizzare gli indici.
