---
type: entity
title: Mars Pathfinder
tags: [caso-studio, inversione-di-priorità, storia-informatica]
related: ["inversione-di-priorità"]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione12-13-AA25-26.txt"]
---
Il `Mars Pathfinder` è un celebre caso studio di fallimento sistemico dovuto all'inversione di priorità. Durante la missione spaziale, il software del rover (basato su `VxWorks`) ha subito continui reset a causa di un conflitto di sincronizzazione in cui un processo a bassa priorità bloccava un processo ad alta priorità, venendo a sua volta prelazionato da un processo a priorità intermedia.