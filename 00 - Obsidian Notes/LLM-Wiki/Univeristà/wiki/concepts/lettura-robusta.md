---
type: concept
title: lettura-robusta
tags: [socket, networking, programmazione]
related: [lettura-parziale, recv]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# lettura-robusta

La lettura robusta è una tecnica di programmazione utilizzata per garantire che un intero messaggio venga ricevuto correttamente nonostante il fenomeno della lettura parziale. Consiste nell'utilizzare un ciclo `while` che continua a chiamare `recv` finché non sono stati letti tutti i byte previsti, aggiornando correttamente l'offset nel buffer di destinazione per evitare sovrascritture.