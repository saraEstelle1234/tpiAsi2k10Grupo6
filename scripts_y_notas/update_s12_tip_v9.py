with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

old_tip = """            <div style="font-size: 12px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Hacé clic en el diagrama o en 'Ampliar' para explorar todas las clases, atributos y métodos en alta resolución.</em>
            </div>"""

new_tip = """            <div style="font-size: 12px; color: #6EE7B7; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 10px 14px; margin-top: 14px; line-height: 1.45;">
              ✨ <strong>Multiplicidades Verificadas:</strong> <code>Incidente &rarr; (1) TipoIncidente</code> | <code>Sala &rarr; (1..*) SalaXGuardia</code>. Clic en 'Ampliar' para explorar atributos y métodos.
            </div>"""

print('old_tip found:', old_tip in text)
if old_tip in text:
    text = text.replace(old_tip, new_tip)
    with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated Slide 12 tip in generate_v9_color_deck.py')
