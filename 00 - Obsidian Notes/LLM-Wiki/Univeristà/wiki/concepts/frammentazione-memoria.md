---
type: concept
title: Frammentazione della Memoria
tags: [memoria, allocazione]
related: [paginazione, algoritmi-di-allocazione]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# Frammentazione della Memoria

La frammentazione è il problema per cui la memoria non può essere utilizzata efficacemente a causa della sua organizzazione.

- **Frammentazione Esterna**: Si verifica quando c'è memoria totale sufficiente per soddisfare una richiesta, ma non è disponibile in un blocco contiguo. Può essere risolta tramite la compattazione o la paginazione.
- **Frammentazione Interna**: Si verifica quando la memoria allocata a un processo è superiore a quella effettivamente richiesta (tipico dell'allocazione a blocchi fissi come nel paging).

Per gestire la memoria contigua, si utilizzano algoritmi come **First-fit**, **Best-fit** e **Worst-fit**.