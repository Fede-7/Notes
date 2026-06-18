---
type: concept
title: Major e Minor Numbers
tags: [kernel, driver, dispositivi]
related: [mknod, dmesg, dispositivi-a-carattere-vs-a-blocco.md]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 26.txt"]
---
# Major e Minor Numbers

Il kernel utilizza un sistema di numerazione per identificare i driver e le loro istanze:
- **Major Number**: Identifica il driver specifico nel kernel. Ogni driver ha un numero Major unico.
- **Minor Number**: Identifica l'istanza o il comportamento specifico del driver. Lo stesso driver può gestire più dispositivi (es. `/dev/null` e `/dev/zero`) assegnando loro Minor numbers differenti.
