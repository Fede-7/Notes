---
type: concept
title: Mutua Esclusione
tags: ["sincronizzazione", "requisiti", "thread"]
related: ["sezione-critica", "progresso", "bounded-waiting"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
# Mutua Esclusione

La [[mutua-esclusione]] è la proprietà e il requisito fondamentale per la sincronizzazione che stabilisce che, in ogni momento, non più di un solo processo o thread alla volta possa eseguire la propria [[sezione-critica]]. 

Essa rappresenta il requisito minimo necessario per prevenire le corse critiche in sistemi che utilizzano la memoria condivisa.