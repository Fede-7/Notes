---
type: entity
title: POSIX API
tags: [api, posix, portabilità]
related: [posix, system-call]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione3-AA25-26.txt"]
---
# POSIX API
La **POSIX API** (*Portable Operating System Interface*) è uno standard di programmazione che fornisce un'interfaccia uniforme per sistemi operativi basati su Unix, Linux e MacOS. 

A differenza delle system call dirette, che sono specifiche del kernel, le API POSIX forniscono portabilità. Esse incapsulano le system call del kernel in funzioni standard (es. `read()`, `fork()`, `write()`), permettendo ai programmi di essere eseguiti su diverse piattaforme con modifiche minime.
