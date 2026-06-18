---
type: entity
title: FIFO
tags: [algoritmi, memoria-virtuale]
related: [page-replacement, anomalia-di-belady]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# FIFO (First-In, First-Out)

L'algoritmo **FIFO** è una strategia di [[page-replacement]] che sostituisce la pagina che è stata caricata per prima nella memoria. Sebbene semplice da implementare, soffre dell'[[anomalia-di-belady]], dove l'aggiunta di frame di memoria può paradossalmente aumentare il numero di page fault.