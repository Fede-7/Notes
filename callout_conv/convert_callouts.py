#!/usr/bin/env python3
"""
Script per convertire automaticamente i callout markdown.

Conversioni:
  [!definition] → [!info]
  [!summary] → [!abstract]
  [!quote] → [!info]
  [!note] → [!info]

Uso:
  python3 convert_callouts.py input.md > output.md
  python3 convert_callouts.py input.md --inplace
  cat input.md | python3 convert_callouts.py
"""

import sys
from pathlib import Path


class CalloutConverter:
    """Converte callout markdown."""
    
    # Mappa sostituzione diretta
    CALLOUT_MAP = {
        '[!definition]': '[!info]',
        '[!summary]': '[!abstract]',
        '[!quote]': '[!info]',
        '[!note]': '[!info]',
    }
    
    def convert_callouts(self, content):
        """Converte tutti i callout nel contenuto."""
        for old, new in self.CALLOUT_MAP.items():
            content = content.replace(old, new)
        return content
    
    def process(self, content):
        """Processa il contenuto."""
        return self.convert_callouts(content)


def main():
    """Funzione principale."""
    converter = CalloutConverter()
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ('--help', '-h'):
            print(__doc__)
            return
        
        filepath = sys.argv[1]
        inplace = '--inplace' in sys.argv
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Errore: file non trovato: {filepath}", file=sys.stderr)
            sys.exit(1)
        
        converted = converter.process(content)
        
        if inplace:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(converted)
            print(f"✓ Aggiornato: {filepath}", file=sys.stderr)
        else:
            print(converted)
    else:
        content = sys.stdin.read()
        converted = converter.process(content)
        print(converted)


if __name__ == '__main__':
    main()
