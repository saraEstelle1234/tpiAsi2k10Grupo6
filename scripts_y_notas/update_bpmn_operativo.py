import base64
import os

img_path = 'media/bpmn_operativo_corregido.png'

with open(img_path, 'rb') as f:
    raw_bytes = f.read()

b64_str = f"data:image/png;base64,{base64.b64encode(raw_bytes).decode('ascii')}"

# Update build_editorial_html.py
with open('scripts_y_notas/build_editorial_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace b64_bpmn_oper line
import re
new_content, count = re.subn(
    r'b64_bpmn_oper\s*=\s*"data:image/png;base64,[^"]+"',
    f'b64_bpmn_oper = "{b64_str}"',
    content
)

if count > 0:
    with open('scripts_y_notas/build_editorial_html.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("build_editorial_html.py updated successfully with new b64_bpmn_oper!")
else:
    print("WARNING: b64_bpmn_oper regex replacement failed!")

# Also update Slide 6 in generate_v8_deck.py to fine-tune height and text cards
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    deck_code = f.read()

s6_start = deck_code.find('<!-- SLIDE 6: BPMN OPERATIVO')
s7_start = deck_code.find('<!-- SLIDE 7: REQUERIMIENTOS')

if s6_start != -1 and s7_start != -1:
    new_s6 = """<!-- SLIDE 6: BPMN OPERATIVO (NUEVO DIAGRAMA CORREGIDO CON 4 CARRILES) -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Flujo de control, 4 carriles, alimentación de datos y estados del proceso (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Diagrama a tamaño máximo horizontal en marco blanco limpio sin bordes negros -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 480px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida)')" alt="BPMN Nivel 2 Corregido">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida)')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- 3 Puntos concretos que explican cómo se plantearon las correcciones del profesor -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
          
          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #2D7FF9;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">1. Alimentación y Almacenes</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              La tarea <em>Registrar incidente</em> se alimenta de los almacenes maestros de <strong>Incidente</strong>, <strong>Salas</strong> y <strong>Obras</strong>, asociando las acciones sugeridas de acuerdo al tipo de daño.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #60A5FA;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">2. Estados Explícitos</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              Cada actividad explicita su estado: sala en <strong>'Incidente activo'</strong> o <strong>'Sin novedades'</strong>; y la obra pasa a <strong>'Inactivo'</strong> ante daño y retorna a <strong>'Activo'</strong> tras su resolución.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #38BDF8;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">3. 4 Carriles y Restauración</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              Separación formal en 4 carriles: <em>Guardia</em>, <em>Encargado Web</em>, <em>Supervisor</em> y <em>Restaurador</em>, reflejando formalmente la actividad <strong>'Restaurar obra'</strong> en su carril.
            </div>
          </div>

        </div>
      </div>
    </div>
"""
    deck_code = deck_code[:s6_start] + new_s6 + deck_code[s7_start:]
    with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
        f.write(deck_code)
    print("generate_v8_deck.py updated successfully with new Slide 06!")
else:
    print("WARNING: Could not find Slide 6 boundaries in generate_v8_deck.py!")
