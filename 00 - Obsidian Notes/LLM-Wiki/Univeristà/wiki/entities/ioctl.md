---
type: entity
title: ioctl
tags: [kernel, device-driver, I/O]
related: [device-driver, interrupt-handler]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 25.txt"]
---
# ioctl
Il comando **ioctl** (input/output control) è un'interfaccia "passpartout" utilizzata per inviare bit arbitrari ai registri di controllo dei dispositivi per eseguire operazioni non standard che non possono essere gestite dalle chiamate di sistema comuni come `read` o `write`.