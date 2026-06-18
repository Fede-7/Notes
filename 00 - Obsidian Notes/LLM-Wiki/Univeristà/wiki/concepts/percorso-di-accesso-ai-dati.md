---
type: concept
title: Percorso di accesso ai dati
tags: [file-system, architecture]
related: [file-descriptor, inode]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 23.txt"]
---
Il percorso logico seguito dal sistema operativo per accedere ai dati di un file è strutturato gerarchicamente come segue:
1. **File Descriptor**: L'indice numerico nel processo.
2. **Tabella file aperti del processo**: Mappa il descrittore alla struttura di sistema.
3. **Tabella file aperti di sistema**: Contiene le entry condivise tra i processi.
4. **Inode**: Struttura contenente i metadati e i puntatori ai blocchi.
5. **Blocchi dati**: Posizione fisica sulla memoria di massa.