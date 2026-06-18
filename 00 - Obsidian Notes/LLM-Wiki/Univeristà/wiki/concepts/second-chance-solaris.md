---
type: concept
title: Second Chance (Solaris)
tags: [memoria-virtuale, paging, solaris]
related: [hand-spread, scan-rate]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 20.txt"]
---
# Second Chance (Solaris)
Il meccanismo [[second-chance-solaris]] è un algoritmo di sostituzione delle pagine utilizzato da Solaris. Si basa su una scansione a due lancette (*front-end* e *back-end*) dove la "seconda possibilità" di una pagina dipende dalla distanza tra le lancette ([[hand-spread]]) e dalla velocità di scansione ([[scan-rate]]) del demone di *page out*.