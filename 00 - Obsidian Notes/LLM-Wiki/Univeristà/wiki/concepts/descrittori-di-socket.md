---
type: concept
title: Descrittori di Socket
tags: [socket, file-descriptor]
related: [socket, accept, everything-is-a-file]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Trascrizioni/Lezione 29.txt"]
---
# Descrittori di Socket

In sistemi Unix-like, i socket sono trattati come file. Il kernel assegna un identificatore numerico, chiamato **descrittore di socket**, per ogni connessione aperta. Questo permette ai programmatori di utilizzare le stesse primitive di sistema (`read`, `write`, `close`) per interagire con i socket come farebbero con i file o le pipe.