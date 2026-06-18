---
type: entity
title: Grand Central Dispatch (GCD)
tags: [apple, threading, task-management]
related: [threading-implicito, thread-pool]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# Grand Central Dispatch (GCD)

**Grand Central Dispatch** è un framework di gestione dei task sviluppato da Apple per i sistemi macOS e iOS. GCD permette ai programmatori di inviare blocchi di codice (task) a code di esecuzione, che vengono poi eseguite da un pool di thread gestito dal sistema. È un esempio di [[threading-implicito]] che abstrae la gestione dei thread a favore di un modello basato sui task.