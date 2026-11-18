# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = """          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 6px;">3. Confirmación Segura (Pasos 9 a 14)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Botón de confirmación con diálogo modal que previene registros involuntarios antes de impactar en la base de datos.
            </div>
          </div>"""

replacement = """          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #38BDF8; text-transform: uppercase; margin-bottom: 6px;">3. Confirmación y Registro (Pasos 9 a 12)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El sistema solicita confirmación del incidente, el guardia confirma y la obra pasa a estado 'Inactivo' con registro de hora del servidor.
            </div>
          </div>"""

assert target in code, "Target not found in generate_v8_deck.py"
code = code.replace(target, replacement)

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated Slide 11 successfully!")
