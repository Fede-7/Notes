---
type: concept
title: ABI (Application Binary Interface)
tags: [so, sistema-operativo, architettura]
related: [system-call, posix-api, wrapper-di-libreria]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione2b-AA25-26.txt"]
---
# ABI (Application Binary Interface)

L'**ABI** rappresenta l'interfaccia a livello binario tra i programmi utente e il sistema operativo (o l'hardware). Mentre l'API definisce come un programmatore scrive il codice (es. chiamando una funzione in C), l'ABI definisce come il codice compilato interagisce effettivamente con il sistema.

### Differenze chiave con le API
- **Livello di astrazione**: L'API è orientata al codice sorgente; l'ABI è orientata al codice macchina.
- **Contenuto**: L'ABI specifica la convenzione di chiamata (calling convention), la disposizione dei parametri nei registri o nello stack, il formato dei tipi di dati binari e i meccanismi di gestione della memoria.

In un sistema moderno, quando un programma utilizza una libreria come `libc` per effettuare una system call, la libreria funge da ponte tra l'API (che il programmatore vede) e l'ABI (che il kernel esegue).