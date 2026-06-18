---
type: entity
title: init / systemd
tags: [linux, system-processes]
related: [processi-zombie-e-orfani.md]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione4-5-6-AA25-26.txt"]
---
# init / systemd
In molti sistemi Linux, `init` (o il suo successore `systemd`) è il primo processo avviato dal kernel (PID 1). È responsabile della gestione dei processi orfani, adottandoli quando il loro processo padre termina.