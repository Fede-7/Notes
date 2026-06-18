---
type: concept
title: Indirizzi Logici vs Fisici
tags: [memoria, architettura]
related: [binding-indirizzi, mmu, paginazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Indirizzi Logici vs Fisici

È fondamentale distinguere tra i due tipi di indirizzi:

- **Indirizzi Logici (Virtuali)**: Sono gli indirizzi generati dalla CPU durante l'esecuzione di un programma. Ogni processo vede uno spazio di indirizzamento proprio e isolato.
- **Indirizzi Fisici**: Sono gli indirizzi reali che corrispondono alle posizioni fisiche nella memoria principale (RAM).

La separazione tra questi due mondi permette l'isolamento dei processi e la gestione della memoria virtuale.