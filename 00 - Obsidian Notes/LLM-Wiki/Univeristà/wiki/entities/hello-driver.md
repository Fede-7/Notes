---
type: entity
title: hello_driver
tags: [kernel, driver, esempio]
related: [insmod, rmmod, printk, file_operations]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# hello_driver

Il modulo **hello_driver** è un modulo kernel di esempio ("Hello World") utilizzato durante le esercitazioni per illustrare i concetti base della programmazione di driver.

Il modulo dimostra come:
1. Registrare un driver nel kernel.
2. Creare un nodo di dispositivo in `/dev`.
3. Implementare le funzioni di callback per le operazioni standard (come `read`).
4. Utilizzare `printk` per il logging all'interno dello spazio kernel.
