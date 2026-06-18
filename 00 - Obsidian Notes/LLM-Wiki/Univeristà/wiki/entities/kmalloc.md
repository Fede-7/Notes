---
type: entity
title: kmalloc
tags: [linux, kernel, memoria]
related: [vmalloc, kernel-space-vs-user-space]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt", "SO/Trascrizioni/Lezione 26.txt"]
---
# kmalloc

**kmalloc** è la funzione di allocazione della memoria specifica per il kernel Linux (spesso indicata come chiamata di sistema del kernel). A differenza di `malloc`, utilizzata nello spazio utente, `kmalloc` è progettata per allocare blocchi di memoria nello spazio di indirizzamento del kernel che devono essere sia fisicamente che virtualmente contigui. È particolarmente adatta per piccoli oggetti e strutture dati che richiedono un accesso diretto.