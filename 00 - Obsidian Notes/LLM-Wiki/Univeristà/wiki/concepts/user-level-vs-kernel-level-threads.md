---
type: concept
title: User-level vs. Kernel-level threads
tags: [threads, architecture]
related: [lwp, many-to-one, many-to-many]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezione9-10-11-AA25-26.txt"]
---
# User-level vs. Kernel-level threads

- **User-level threads**: Gestiti da una libreria nel runtime dell'applicazione. Il kernel non è consapevole della loro esistenza. Sono veloci da creare ma non possono sfruttare il multi-core se la libreria non è progettata per farlo.
- **Kernel-level threads**: Gestiti direttamente dal kernel. Il kernel può schedulare ogni thread indipendentemente. Sono più pesanti da creare ma permettono il vero parallelismo su sistemi multi-processore.