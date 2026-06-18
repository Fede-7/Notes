---
type: entity
title: libc
tags: ["libreria", "c", "wrapper", "syscall"]
related: ["system-call"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# libc

La **libc** (Standard C Library) è la libreria standard del linguaggio C. In contesti Unix-like, funge da fondamentale **wrapper** per le chiamate di sistema.

## Funzionamento Tecnico
La `libc` gestisce la preparazione dei parametri necessari nei registri della CPU e dello stack. Quando un programmatore chiama una funzione come `read()`, la libreria prepara il contesto e invoca l'istruzione `syscall` per passare il controllo al kernel.

## Funzionalità
Oltre a gestire le interazioni di basso livello con il sistema operativo, la `libc` offre una vasta gamma di funzioni di alto livello per lo sviluppo software, tra cui:
- `printf`
- `write`
- `open`
- `fopen`