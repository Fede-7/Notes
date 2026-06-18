---
type: entity
title: strace
tags: [strumento, kernel, tracciamento]
related: [openat, everything-is-a-file]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# strace

**strace** è uno strumento utilizzato per tracciare le chiamate di sistema eseguite da un processo. È fondamentale per analizzare come le applicazioni interagiscono con il kernel, mostrando ad esempio la serie di chiamate `openat` necessarie per accedere a dispositivi come `/dev/null` o `/dev/random`.
