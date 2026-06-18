---
type: concept
title: Scrittura Sincrona vs Asincrona
tags: [file-system, prestazioni, I/O]
related: [journaling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt"]
---
# Scrittura Sincrona vs Asincrona
- **Scrittura Sincrona**: L'operazione di scrittura blocca il processo finché i dati non sono fisicamente scritti sul supporto di memoria secondaria. Può causare "convogli" di richieste se il disco è lento.
- **Scrittura Asincrona**: Il sistema operativo accetta la scrittura e la mette in un buffer, permettendo al processo di proseguire immediatamente. Il trasferimento fisico avviene in modo differito, ottimizzando l'uso delle risorse.