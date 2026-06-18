---
type: concept
title: socket-non-bloccante
tags: [socket, networking]
related: [MSG_DONTWAIT]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# socket-non-bloccante

In modalità non bloccante, le chiamate di sistema per la lettura o la scrittura su un socket restituiscono immediatamente, anche se il buffer è vuoto o non è possibile scrivere immediatamente. Questo comportamento è attivato tramite l'uso di flag come `MSG_DONTWAIT`. È essenziale per applicazioni che devono gestire molte connessioni simultanee senza bloccare il thread principale.