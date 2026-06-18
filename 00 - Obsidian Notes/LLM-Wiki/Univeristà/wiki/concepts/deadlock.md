---
type: concept
title: Deadlock
tags: [sistemi-operativi, concorrenza, risorse, sincronizzazione, liveness]
related: [livelock, condizioni-di-coffman, grafo-di-allocazione-delle-risorse, prevenzione-del-deadlock, evitamento-del-deadlock, rilevamento-e-ripristino-del-deadlock, attesa-circolare, self-deadlock, starvation]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt", "SO/Trascrizioni/Lezione 11.txt"]
---
# Deadlock

Un **deadlock** è una situazione in cui un insieme di thread (o processi) rimane bloccato permanentemente perché ogni elemento del gruppo attende una risorsa detenuta da un altro elemento della catena. In questo stato, nessuno dei thread può procedere, portando a una paralisi del sistema o di una parte di esso.

### Proprietà e Condizioni
Il deadlock è considerato una violazione della proprietà di *liveness* del sistema. Affinché si verifichi, devono essere soddisfatte simultaneamente le quattro **Condizioni di Coffman**.