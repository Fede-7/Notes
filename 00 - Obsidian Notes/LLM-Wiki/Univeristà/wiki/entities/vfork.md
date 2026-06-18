---
type: entity
title: vfork()
tags: [processi, sistema-operativo]
related: [fork]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# vfork()

**vfork()** è una variante della chiamata `fork()` che permette al processo figlio di condividere lo spazio di indirizzi del padre senza utilizzare il meccanismo del *Copy-on-Write*. È tipicamente utilizzata quando il figlio esegue immediatamente una chiamata `exec()`.