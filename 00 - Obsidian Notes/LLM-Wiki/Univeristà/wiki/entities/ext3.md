---
type: entity
title: EXT3
tags: [linux, file-system, journaling]
related: [ext2, ext4, journaling]
created: 2026-06-17
updated: 2026-06-17
sources: ["SO/Slide/SO1-Lezioni-file-system1-AA25-26.txt"]
---
# EXT3

**EXT3** è l'evoluzione di EXT2 che introduce il meccanismo di **Journaling**.

### Journaling
- Registra le modifiche ai metadati in un log sequenziale prima di applicarle effettivamente.
- Riduce drasticamente il tempo di recupero del file system dopo un crash di sistema.
