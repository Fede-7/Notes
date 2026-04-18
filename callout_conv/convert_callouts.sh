#!/bin/bash
#
# Script bash per convertire automaticamente i callout markdown
#
# Conversioni supportate:
#   [!definition] → [!info]
#   [!summary] → [!abstract]
#   [!quote] → [!info]
#   [!note] → [!info]
#
# Uso:
#   ./convert_callouts.sh input.md > output.md
#   ./convert_callouts.sh input.md --inplace
#   ./convert_callouts.sh *.md --batch
#   cat input.md | ./convert_callouts.sh

convert_file() {
    local file="$1"
    
    # Sostituzione con sed
    sed \
        -e 's/\[!definition\]/[!info]/g' \
        -e 's/\[!summary\]/[!abstract]/g' \
        -e 's/\[!quote\]/[!info]/g' \
        -e 's/\[!note\]/[!info]/g' \
        "$file"
}

show_help() {
    cat << 'EOF'
Script per convertire callout markdown automaticamente

USO:
  ./convert_callouts.sh FILE              # Stampa conversione a stdout
  ./convert_callouts.sh FILE --inplace    # Modifica il file in-place
  ./convert_callouts.sh *.md --batch      # Converte tutti i file

CONVERSIONI:
  [!definition] → [!info]
  [!summary]    → [!abstract]
  [!quote]      → [!info]
  [!note]       → [!info]

OPZIONI:
  --inplace     Modifica il file invece di stampare stdout
  --batch       Processa tutti i file e salva con suffisso _converted
  --help        Mostra questo messaggio

ESEMPI:
  # Converte e stampa
  ./convert_callouts.sh appunti.md

  # Modifica il file direttamente
  ./convert_callouts.sh appunti.md --inplace

  # Processa tutti i .md nella cartella
  for f in *.md; do
    ./convert_callouts.sh "$f" --inplace
  done
EOF
}

main() {
    # Nessun argomento: leggi da stdin
    if [[ $# -eq 0 ]]; then
        cat | sed \
            -e 's/\[!definition\]/[!info]/g' \
            -e 's/\[!summary\]/[!abstract]/g' \
            -e 's/\[!quote\]/[!info]/g' \
            -e 's/\[!note\]/[!info]/g'
        return
    fi
    
    # Flag --help
    if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]]; then
        show_help
        return
    fi
    
    # Batch mode: tutti i file
    if [[ "$2" == "--batch" ]]; then
        for file in "$@"; do
            [[ "$file" == "--batch" ]] && continue
            [[ ! -f "$file" ]] && continue
            
            output="${file%.md}_converted.md"
            echo "Convertendo: $file → $output" >&2
            convert_file "$file" > "$output"
        done
        return
    fi
    
    # Single file
    local file="$1"
    local inplace="$2"
    
    if [[ ! -f "$file" ]]; then
        echo "Errore: file non trovato: $file" >&2
        return 1
    fi
    
    if [[ "$inplace" == "--inplace" ]]; then
        local temp_file=$(mktemp)
        convert_file "$file" > "$temp_file"
        mv "$temp_file" "$file"
        echo "✓ Aggiornato: $file" >&2
    else
        convert_file "$file"
    fi
}

main "$@"
