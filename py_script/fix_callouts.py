import re
import sys

with open(sys.argv[1], 'r') as f:
    content = f.read()

# Trova tutti i "> [!" che non sono preceduti da una riga vuota
# Se la riga precedente non è vuota (non finisce con \n\n), aggiungi un \n in più
# Pattern: \n + un carattere che non è \n + \n + "> [!" -> ma questo richiede attenzione.
# Facciamo: sostituisci r"([^\n])\n> \[!" con r"\1\n\n> [!"
content = re.sub(r'([^\n])\n> \[!', r'\1\n\n> [!', content)

# Inoltre, vediamo se ci sono > [! all'inizio di una riga con spazi che potremmo aver perso,
# ma qui sono sempre "> [!".
# Salviamo il file
with open(sys.argv[1], 'w') as f:
    f.write(content)

print("Done")
