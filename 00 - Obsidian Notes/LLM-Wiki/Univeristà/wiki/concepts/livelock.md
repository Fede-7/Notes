---
type: concept
title: Livelock
tags: [sistemi-operativi, concorrenza, liveness]
related: [deadlock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione-deadlock-AA25-26.txt"]
---
# Livelock

Il **livelock** è un fenomeno di fallimento della *liveness* in cui i thread non sono bloccati (non sono in stato di attesa passiva), ma non riescono a procedere perché rispondono continuamente a un'azione che fallisce.

Un esempio classico è quello di due persone in un corridoio che cercano di evitarsi a vicenda, spostandosi simultaneamente a destra e poi a sinistra, rimanendo bloccate nel tentativo di passare. A differenza del deadlock, i thread continuano a consumare risorse di CPU.

In alcuni casi, il livelock può essere risolto introducendo della **randomizzazione** (es. periodi di *backoff* casuali nei protocolli di rete).
