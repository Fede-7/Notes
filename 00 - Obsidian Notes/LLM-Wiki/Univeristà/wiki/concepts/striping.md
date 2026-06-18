---
type: concept
title: Striping
tags: [raid, performance]
related: [mirroring, raid]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-massa-AA25-26.txt"]
---
# Striping

Lo **striping** è una tecnica di distribuzione dei dati in cui i blocchi di un file vengono suddivisi e scritti su più unità fisiche contemporaneamente.

- **Vantaggi**: Aumento significativo del throughput (velocità di trasferimento) poiché più dischi lavorano in parallelo.
- **Svantaggi**: Nessuna ridondanza intrinseca; se un disco nell'array fallisce, i dati distribuiti su di esso vanno persi (a meno che non sia combinato con il mirroring).