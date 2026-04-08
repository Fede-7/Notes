---
banner: "[[Banner_n1.jpg]]"
aliases:
---

# Lezioni Semestre:
``` dataview
TABLE length(rows) as "Numero Lezioni"
FROM "00 - Obsidian Notes/2° Anno/2° Semestre"
WHERE file.folder != "00 - Obsidian Notes/2° Anno/2° Semestre"
GROUP BY regexreplace(file.folder, ".*\/", "") as "Corso"

```

![[DataView.base]]
