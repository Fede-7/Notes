---
type: concept
title: Signal Handling
tags: [unix, segnali, concorrenza]
related: [segnali-standard, segnali-real-time]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Signal Handling

Il **signal handling** è il meccanismo attraverso il quale il kernel comunica eventi asincroni ai processi (come interruzioni hardware o azioni di altri processi). In ambiente Unix, i segnali possono essere gestiti in modo diverso a seconda che il processo sia single-threaded o multi-threaded. In sistemi multi-thread, è necessario gestire correttamente la consegna dei segnali per evitare condizioni di gara o comportamenti imprevedibili.