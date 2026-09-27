---
banner: "[[Banner_n1.jpg]]"
aliases:
---

# Lezioni Semestre:
``` dataview
TABLE length(rows) as "Numero Lezioni"
FROM "00 - Obsidian Notes/3° Anno/1° Semestre"
WHERE file.folder != "00 - Obsidian Notes/3° Anno/1° Semestre"
GROUP BY regexreplace(file.folder, ".*\/", "") as "Corso"
```

![[DataView.base]]
