---
type: concept
title: Condizioni di Coffman
tags: [deadlock, teoria]
related: [deadlock, prevenzione-del-deadlock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Condizioni di Coffman

Perché si verifichi un deadlock, devono essere soddisfatte contemporaneamente quattro condizioni:

1.  **Mutual Exclusion (Esclusione reciproca)**: Almeno una risorsa deve essere utilizzabile da un solo processo alla volta.
2.  **Hold and Wait (Mantenimento e attesa)**: Un processo deve poter detenere almeno una risorsa mentre ne richiede un'altra già detenuta da un altro processo.
3.  **No Preemption (Assenza di prelazione)**: Le risorse non possono essere sottratte forzatamente ai processi che le detengono; possono essere rilasciate solo volontariamente dal processo stesso.
4.  **Circular Wait (Attesa circolare)**: Deve esistere una catena di processi $P_0, P_1, \dots, P_n$ tale che $P_0$ attende una risorsa detenuta da $P_1$, $P_1$ da $P_2$, e così via, fino a $P_n$ che attende una risorsa detenuta da $P_0$.
