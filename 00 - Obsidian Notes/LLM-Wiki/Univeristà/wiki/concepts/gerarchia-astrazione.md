---
type: concept
title: Gerarchia di Astrazione
tags: [so, architettura]
related: [system-call, posix-api.md]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# Gerarchia di Astrazione
Il sistema operativo opera attraverso diversi livelli di astrazione che permettono ai programmatori di interagire con l'hardware senza conoscerne i dettagli fisici.

La gerarchia tipica è la seguente:
1. **Programma Utente**: Scrive codice utilizzando funzioni di alto livello.
2. **API (Application Programming Interface)**: Fornisce un'interfaccia standard e portabile (es. POSIX).
3. **Librerie di Sistema (Wrapper)**: Funzioni come quelle in `libc` che mappano le chiamate API alle system call specifiche.
4. **Chiamate di Sistema (System Calls)**: L'interfaccia di basso livello che attiva il passaggio al kernel tramite *Trap*.
5. **Kernel**: Gestisce le risorse e le operazioni hardware.
6. **Hardware**: L'hardware fisico (CPU, memoria, dispositivi I/O).

È importante notare che le API non sempre mappano uno a uno con le system call; alcune funzioni API possono eseguire operazioni complesse senza generare un *Trap* del kernel.
