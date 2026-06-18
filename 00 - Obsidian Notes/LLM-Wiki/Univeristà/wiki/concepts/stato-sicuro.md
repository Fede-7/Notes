---
type: concept
title: Stato Sicuro
tags: [deadlock, evitamento]
related: [evitamento-del-deadlock, algoritmo-del-banchiere]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Stato Sicuro

Un sistema è in uno **Stato Sicuro** se esiste una sequenza di tutti i processi nel sistema $<P_1, P_2, \dots, P_n>$ tale che, per ogni $P_i$, le risorse richieste da $P_i$ possono essere soddisfatte dalle risorse correntemente disponibili più le risorse tenute dai processi $P_j$ con $j < i$.

In pratica, significa che esiste un ordine di esecuzione in cui ogni processo può completare il proprio compito, rilasciando le risorse per i successivi. Se un sistema è in stato sicuro, non può verificarsi un deadlock.
