---
type: entity
title: PCB
tags: [processi, kernel]
related: ["memoria-virtuale"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# PCB (Process Control Block)

Il **PCB** è la struttura dati utilizzata dal kernel per mantenere le informazioni di stato di un processo. Nel contesto della gestione della memoria virtuale, il PCB contiene i riferimenti alle tabelle delle pagine del processo, permettendo al sistema operativo di verificare la validità dei riferimenti durante la gestione dei page-fault.