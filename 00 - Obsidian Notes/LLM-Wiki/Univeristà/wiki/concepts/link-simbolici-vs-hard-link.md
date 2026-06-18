---
type: concept
title: Link Simbolici vs. Hard Link
tags: [file-system, unix]
related: [inode]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-FS1-AA25-26.txt"]
---
# Link Simbolici vs. Hard Link

In sistemi Unix/Linux, è possibile creare più nomi per lo stesso file. Esistono due modalità principali:

## Hard Link
- Crea un nuovo nome che punta allo stesso [[inode]] del file originale.
- Il sistema mantiene un contatore di link; il file viene eliminato solo quando il contatore raggiunge zero.
- Non può essere utilizzato per collegare directory.

## Link Simbolici (Symbolic Link)
- Crea un file speciale che contiene il percorso (*path*) del file o della directory di destinazione.
- Permette di creare link verso directory e verso file su file system diversi.
- **Dangling Pointers**: Se il file originale viene eliminato, il link simbolico rimane ma punta a un percorso inesistente (link rotto).