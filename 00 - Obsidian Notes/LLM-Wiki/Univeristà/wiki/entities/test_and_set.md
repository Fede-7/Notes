---
type: entity
title: test_and_set
tags: [hardware, istruzioni-atomiche, sincronizzazione]
related: [istruzioni-atomiche, barriere-di-memoria, mutex-lock]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
`test_and_set` è un'istruzione hardware atomica fondamentale per la sincronizzazione dei processi. Essa restituisce il valore attuale di una variabile e la imposta simultaneamente a TRUE (o 1). Grazie alla sua natura atomica, garantisce che l'operazione non possa essere interrotta, permettendo di implementare primitive di lock di base.