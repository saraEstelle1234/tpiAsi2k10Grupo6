with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    deck = f.read()

s5_start = deck.find('<!-- SLIDE 5: BPMN DESCRIPTIVO -->')
s7_start = deck.find('<!-- SLIDE 7: REQUERIMIENTOS')

if s5_start == -1 or s7_start == -1:
    raise Exception("Could not find Slide 5 or 7 boundaries!")

new_s5_s6 = """<!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
        <!-- Diagrama a tamaño maximizado en marco blanco limpio -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 620px; display: flex; flex-direction: column; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo (4 Carriles)')" alt="BPMN Nivel 1 Descriptivo" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; 4 Carriles Formalizados</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo (4 Carriles)')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- Síntesis en 4 carriles (sin cuadritos negros) -->
        <div class="card-dark reveal-item revealed" style="padding: 24px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Nivel 1 &bull; Alcance Global</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 10px; letter-spacing: -0.01em;">Estructura en 4 Carriles</h3>
            <p style="font-size: 12.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              El modelo formaliza la interacción y responsabilidades entre los cuatro roles del proceso (Sección 2.5 del TPI):
            </p>

            <div style="display: flex; flex-direction: column; gap: 13px; padding-left: 2px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">1. Guardia del museo</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Ronda presencial, consulta de planificación y reporte in situ de novedades en sala.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">2. Admin de sistema</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Tipificación del daño (accidental, provocado, natural) y acciones sugeridas de mitigación.
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">3. Encargado de supervisión</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Evaluación consolidada del informe y determinación de derivación a restauración o baja.
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">4. Encargado de restauración</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Intervención técnica en taller y reingreso obligatorio a depósito conforme a la Regla 1.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 11.5px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Clic en el diagrama o en 'Ampliar' para navegarlo con zoom libre en alta resolución.</em>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: BPMN OPERATIVO (NUEVO DIAGRAMA CORREGIDO CON 4 CARRILES) -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Flujo de control, 4 carriles, alimentación de datos y estados del proceso (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Diagrama a tamaño máximo horizontal en marco blanco limpio sin bordes negros -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')" alt="BPMN Nivel 2 Corregido">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida (1682 &times; 798 px)</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')">
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
              Separación formal en 4 carriles: <em>Guardia del museo</em>, <em>Admin de sistema</em>, <em>Encargado de supervisión</em> y <em>Encargado de restauración</em>, con la actividad <strong>'Restaurar obra'</strong>.
            </div>
          </div>

        </div>
      </div>
    </div>
"""

deck = deck[:s5_start] + new_s5_s6 + deck[s7_start:]

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(deck)

print("Slide 5 and Slide 6 updated successfully in generate_v8_deck.py!")
