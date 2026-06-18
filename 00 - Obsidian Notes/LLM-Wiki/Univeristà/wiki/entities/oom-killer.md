---
type: entity
title: OOM killer
tags: [linux, kernel]
related: [memoria-virtuale]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-mem-virtuale-AA25-26.txt"]
---
# OOM killer

L'**OOM killer** è un meccanismo del kernel Linux che interviene quando il sistema esaurisce la memoria disponibile. Il kernel seleziona e termina un processo (solitamente quello che consuma più risorse o ha il punteggio di "colpevolezza" più alto) per prevenire il blocco totale del sistema.