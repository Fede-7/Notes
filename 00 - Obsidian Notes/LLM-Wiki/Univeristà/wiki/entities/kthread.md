---
type: entity
title: KTHREAD
tags: [windows, kernel, thread]
related: [ethread, teb]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# KTHREAD

In Windows, **KTHREAD** è il blocco di dati del thread nello spazio kernel (kernel space). Contiene le informazioni necessarie per la schedulazione del kernel, come lo stato del thread, i priorità e i puntatori ai blocchi di contesto. Mentre `ETHREAD` è visibile all'utente, `KTHREAD` è gestito esclusivamente dal sistema operativo.