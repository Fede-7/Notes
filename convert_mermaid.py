#!/usr/bin/env python3
"""
Script per convertire i diagrammi Mermaid nei file markdown della cartella 2° Semestre.
Aggiunge uno stile uniforme e ottimizzazione per formato A4.
"""

import os
import re
from pathlib import Path

# Configurazione
BASE_DIR = Path(__file__).parent / "00 - Obsidian Notes" / "2° Anno" / "2° Semestre"

MERMAID_CONFIG = """%%{init: {'flowchart': {'curve': 'linear', 'useMaxWidth': true, 'htmlLabels': true}, 'theme': 'base', 'themeVariables': {'fontSize': '14px', 'primaryColor': '#e1f5fe', 'primaryBorderColor': '#01579b'}}}%%"""

MERMAID_STYLE = """    %% Definizione dello stile per adattarsi all'A4
    classDef default fill:#e1f5fe,stroke:#01579b,stroke-width:2px,rx:10,ry:10;"""


def add_style_to_mermaid(mermaid_content: str) -> str:
    """
    Aggiunge la configurazione A4, converte LR→TD e applica lo stile di default.
    """
    lines = mermaid_content.strip().split('\n')
    
    # Verifica e converte graph/flowchart LR → TD
    first_line = lines[0].strip()
    if 'LR' in first_line or 'LR' in first_line.upper():
        # Converte graph LR → graph TD e flowchart LR → flowchart TD
        lines[0] = re.sub(r'(graph|flowchart)\s+LR\b', r'\1 TD', first_line, flags=re.IGNORECASE)
    
    # Aggiunge la configurazione se non presente
    has_config = any('init' in line for line in lines)
    has_classdef = any('classDef' in line for line in lines)
    
    if not has_config:
        lines.insert(0, MERMAID_CONFIG)
    
    # Aggiunge la definizione dello stile se non presente
    if not has_classdef:
        # Trova la prima linea che non è un commento o config
        insert_index = 0
        for i, line in enumerate(lines):
            if line.strip() and not line.strip().startswith('%') and 'init' not in line:
                insert_index = i
                break
        
        if insert_index < len(lines):
            lines.insert(insert_index + 1, MERMAID_STYLE)
    
    # Applica la classe :::default ai nodi
    result_lines = []
    for line in lines:
        if ':::' in line or 'classDef' in line or 'style' in line or 'init' in line:
            result_lines.append(line)
        else:
            if re.search(r'\[[^\]]*\]|\{[^\}]*\}|\([^\)]*\)', line):
                if not re.search(r'\s+:::\w+\s*$', line):
                    line = re.sub(
                        r'(\[[^\]]*\]|\{[^\}]*\}|\([^\)]*\))(?!\s*:::)',
                        r'\1 :::default',
                        line
                    )
            result_lines.append(line)
    
    return '\n'.join(result_lines)


def process_file(filepath: Path) -> bool:
    """
    Processa un file markdown e converte i diagrammi mermaid.
    Ritorna True se il file è stato modificato, False altrimenti.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Usa re.sub con una funzione per processare ogni match
        def replace_mermaid(match):
            mermaid_content = match.group(1)
            converted = add_style_to_mermaid(mermaid_content)
            return f'```mermaid\n{converted}\n```'
        
        pattern = r'```mermaid\n(.*?)\n```'
        content = re.sub(pattern, replace_mermaid, content, flags=re.DOTALL)
        
        # Scrive il file solo se è stato modificato
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"❌ Errore durante la lettura/scrittura di {filepath}: {e}")
        return False


def main():
    """Funzione principale."""
    if not BASE_DIR.exists():
        print(f"❌ Cartella non trovata: {BASE_DIR}")
        return
    
    # Raccoglie tutti i file .md ricorsivamente
    md_files = list(BASE_DIR.rglob("*.md"))
    
    if not md_files:
        print(f"❌ Nessun file .md trovato in {BASE_DIR}")
        return
    
    print(f"📁 Trovati {len(md_files)} file markdown in {BASE_DIR}")
    print()
    
    modified_count = 0
    file_with_mermaid = 0
    
    pattern = r'```mermaid\n(.*?)\n```'
    
    for filepath in sorted(md_files):
        # Calcola il percorso relativo per una visualizzazione migliore
        rel_path = filepath.relative_to(BASE_DIR.parent.parent.parent)
        
        # Estrae i blocchi mermaid per contarli
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = list(re.finditer(pattern, content, re.DOTALL))
        if matches:
            file_with_mermaid += 1
            if process_file(filepath):
                modified_count += 1
                print(f"✅ {rel_path}")
                print(f"   └─ {len(matches)} diagramma(i) aggiornato(i)")
    
    print()
    print("=" * 60)
    print(f"📊 Risultati:")
    print(f"   • File totali: {len(md_files)}")
    print(f"   • File con mermaid: {file_with_mermaid}")
    print(f"   • File modificati: {modified_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
