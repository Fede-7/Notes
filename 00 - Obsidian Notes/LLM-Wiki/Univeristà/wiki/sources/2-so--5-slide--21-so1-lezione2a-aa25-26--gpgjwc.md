---
type: source
title: "Slide Lezione 2a - AA25-26"
tags: [SO1, lezione, slide]
related: [fork, waitpid, execve, exit, gerarchia-di-memorie, buffering-vs-spooling, caching, astrazione-archiviazione, process-tree, gestione-risorse]
created: 2026-06-17
updated: 2026-06-17
authors: []
year: 2025
url: ""
venue: ""
sources: ["SO/Slide/SO1-Lezione2a-AA25-26.txt"]
---
# Slide Lezione 2a - AA25-26

Questa fonte contiene le slide della lezione 2a del corso di Sistemi Operativi I (SO1). Il materiale copre i seguenti argomenti principali:

## Gestione dei Processi
- Definizione di **processo** come entità attiva (rispetto al programma come entità passiva).
- Risorse necessarie: CPU, memoria, I/O, file e dati di inizializzazione.
- Meccanismi di gestione: creazione, cancellazione, sospensione, sincronizzazione, comunicazione e gestione del deadlock.
- Chiamate di sistema fondamentali: `fork()`, `waitpid()`, `execve()` e `exit()`.
- Rappresentazione gerarchica tramite il **Process Tree**.

## Gestione della Memoria e Archiviazione
- **Gerarchia di Memorie**: Analisi dei diversi livelli di memorizzazione basata su velocità, costo, volatilità e tecnologia (dai registri ai dischi magnetici).
- **Caching**: Principi di migrazione dei dati dalle memorie lente a quelle veloci e problematiche di gestione (dimensione e politiche di replicazione).
- **Astrazione dell'Archiviazione**: Fornitura di una rappresentazione logica uniforme (il file) che nasconde le proprietà fisiche del supporto.
- **File-System**: Organizzazione gerarchica, controllo degli accessi, mapping sulla memoria secondaria e backup.

## Sistemi I/O
- Interfaccia uniforme per i dispositivi hardware.
- Tecniche di gestione: **Buffering** (memorizzazione temporanea durante il trasferimento) e **Spooling** (sovrapposizione dell'accesso a periferica da parte di più job).