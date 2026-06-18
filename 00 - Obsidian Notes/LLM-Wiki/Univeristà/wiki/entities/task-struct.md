---
type: entity
title: task_struct
tags: [linux, kernel, thread]
related: [clone, unificazione-task-thread]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione7-8-AA25-26.txt"]
---
# task_struct

**task_struct** è la struttura dati principale del kernel Linux utilizzata per rappresentare ogni processo e ogni thread. Poiché Linux tratta processi e thread in modo uniforme come "tasks", la `task_struct` contiene tutte le informazioni necessarie per la schedulazione, la gestione delle risorse e l'identificazione del task.