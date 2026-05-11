# TEXOR_Konverter.py
import re

def konvertiere_texor(input_datei, output_datei):
    # Mapping der DDR/KC85-Sonderzeichen
    ersetzungen = {
        '[': 'Ä', '\\': 'Ö', ']': 'Ü',
        '{': 'ä', '|': 'ö', '}': 'ü',
        '~': 'ß', '@': '§', 'Ã‰': ' ', 'Âº': ' ', 'Ã®': 'n'
    }
    
    with open(input_datei, 'r', encoding='latin-1') as f:
        inhalt = f.read()

    # Sonderzeichen ersetzen
    for alt, neu in ersetzungen.items():
        inhalt = inhalt.replace(alt, neu)

    # Einfache Markdown-Strukturen (Überschriften erkennen)
    inhalt = re.sub(r'(\d\.)__', r'### \1 ', inhalt)
    
    with open(output_datei, 'w', encoding='utf-8') as f:
        f.write(inhalt)
    print(f"Fertig! Die Datei wurde als '{output_datei}' gespeichert.")

# Nutze den Namen deiner Datei hier:
konvertiere_texor('Handbuch_03-1990.txt', 'Handbuch_03-1990-1.md')
