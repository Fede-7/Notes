---
type: concept
title: Exponential Averaging
tags: [scheduling, prediction]
related: [cpu-i-o-burst]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# Exponential Averaging

L'**Exponential Averaging** è una tecnica utilizzata per predire la durata del prossimo CPU burst basandosi sulla storia dei burst precedenti. La formula utilizza un fattore $\alpha$ (spesso $1/2$) per dare più peso ai burst più recenti rispetto a quelli più vecchi, permettendo al sistema di adattarsi rapidamente ai cambiamenti nel carico di lavoro.