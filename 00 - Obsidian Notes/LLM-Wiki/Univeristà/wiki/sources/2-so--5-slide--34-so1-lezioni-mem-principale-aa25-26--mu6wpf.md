---
type: source
title: "SO1 - Lezioni Memoria Principale"
tags: [SO1, memoria, architettura]
related: [mmu, tlb, paginazione, segmentazione, swapping]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: ""
sources: ["SO/Slide/SO1-Lezioni-mem-principale-AA25-26.txt"]
---
# SO1 - Lezioni Memoria Principale

Questa fonte fornisce una panoramica dettagliata della gestione della memoria principale nei sistemi operativi moderni. I temi principali includono:

- **Binding degli Indirizzi**: Analisi delle tecniche di associazione tra indirizzi logici e fisici a tempi diversi (compilazione, caricamento, esecuzione).
- **Gestione della Memoria Fisica**: Discussione sulla frammentazione (interna ed esterna) e sugli algoritmi di allocazione contigua (First-fit, Best-fit, Worst-fit).
- **Paginazione**: Meccanismi di allocazione non contigua, inclusi i frame, le pagine, le tabelle delle pagine (gerarchiche, hash, invertite) e il ruolo della MMU.
- **Accelerazione dell'Accesso**: Studio della TLB (Translation Look-aside Buffer), dei registri associativi, degli ASID e del calcolo del Tempo di Accesso Effettivo (EAT).
- **Segmentazione**: Visione logica della memoria (codice, stack, dati) e integrazione con la paginazione (segmentazione paginata).
- **Swapping e Memoria Virtuale**: Differenze tra swapping di interi processi e paging (page-in/page-out), con particolare attenzione ai limiti dei sistemi mobili.
- **Architetture Hardware**: Specifiche tecniche per x86-64 (PAE, Flat Mode) e ARMv8 (Translation Granules).