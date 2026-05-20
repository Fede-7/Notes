import urllib.request
import urllib.parse
import json
import time

def translate_batch(texts):
    if not texts: return []
    combined = "\n".join(texts)
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=it&dt=t&q={urllib.parse.quote(combined)}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        result = "".join([part[0] for part in data[0] if part[0]])
        # Fix possible missing newlines if Google squashed them
        return result.split("\n")
    except Exception as e:
        print(f"Error: {e}")
        return texts

file_path = "/home/fede/Scrivania/ed/Obsidian/00 - Obsidian Notes/2° Anno/2° Semestre/Metodi Statistici dell' Informazione/Slide/Statistical_Inference.md"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

out_lines = []
batch = []
batch_indices = []

for i, line in enumerate(lines):
    stripped = line.strip()
    if not stripped or stripped.startswith("## Pagina") or stripped.startswith("---") or stripped.startswith("$$") or stripped.startswith("lops@") or stripped.startswith("https://") or stripped.startswith("$$") or stripped.startswith("="):
        out_lines.append(line)
    else:
        # Check if line contains letters
        if not any(c.isalpha() for c in stripped):
            out_lines.append(line)
        else:
            batch.append(line.rstrip('\n'))
            batch_indices.append(i)
            out_lines.append("") # placeholder
            
            if sum(len(x) for x in batch) > 1000 or len(batch) >= 15:
                translated = translate_batch(batch)
                # Sometimes split returns more or fewer lines, pad or truncate
                while len(translated) < len(batch):
                    translated.append(batch[len(translated)])
                for j, t in zip(batch_indices, translated):
                    out_lines[j] = t + "\n"
                batch = []
                batch_indices = []
                time.sleep(1)

if batch:
    translated = translate_batch(batch)
    while len(translated) < len(batch):
        translated.append(batch[len(translated)])
    for j, t in zip(batch_indices, translated):
        out_lines[j] = t + "\n"

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

print("Translation completed successfully.")
