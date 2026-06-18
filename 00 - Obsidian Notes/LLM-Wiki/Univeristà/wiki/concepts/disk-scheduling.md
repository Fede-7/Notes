---
type: concept
title: Disk Scheduling
tags: ["storage", "algorithms", "memoria-di-massa", "performance", "i-o", "hdd"]
related: ["hard-disk-drive", "solid-state-drive", "hdd", "ssd", "mapping-indirizzi", "seek-time", "sstf", "scan", "c-scan", "look", "cluk"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 21.txt", "SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt", "SO/Trascrizioni/Lezione 20.txt"]
---
# Disk Scheduling
Il [[disk-scheduling]] è il processo di gestione dell'ordine delle richieste di lettura e scrittura per ottimizzare le prestazioni dei dispositivi di memoria di massa meccanici (HDD). L'obiettivo principale è minimizzare il [[seek-time]].

Gli algoritmi principali includono:
- [[sstf]] (Shortest Seek Time First): serve la richiesta più vicina alla posizione attuale della testina.
- [[scan]] (Elevator): la testina si muove da un estremo all'altro del disco servendo le richieste lungo il percorso.
- [[c-scan]] (Circular Scan): variante di SCAN che si muove in una sola direzione e torna rapidamente all'inizio.
- [[look]] e [[cluk]]: varianti di SCAN e C-SCAN che si fermano all'ultima richiesta effettiva invece di percorrere l'intero raggio del disco.