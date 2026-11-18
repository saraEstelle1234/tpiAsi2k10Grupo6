with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate Slide 5
s5_start = content.find('<!-- SLIDE 5: BPMN DESCRIPTIVO -->')
s6_start = content.find('<!-- SLIDE 6: BPMN OPERATIVO')

if s5_start != -1 and s6_start != -1:
    current_s5 = content[s5_start:s6_start]
    
    new_s5 = """<!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 240px; gap: 16px; align-items: stretch;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 600px; display: flex; flex-direction: column;">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1" style="flex: 1; object-fit: contain; cursor: zoom-in;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; Vista General</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 20px 18px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Nivel 1 &bull; Alcance</div>
            <h3 style="font-size: 16px; font-weight: 800; color: #FFF; margin-bottom: 8px;">Diseño del Proceso</h3>
            <p style="font-size: 12.5px; line-height: 1.5; color: var(--text-light); margin-bottom: 12px;">
              Flujo global estructurado en 3 carriles clave (Sección 2.5 del TPI):
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ronda Física</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Guardia recorre salas y constata estado de obras.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Registro en Tablet</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Ante anomalía, registro inmediato en el Módulo Web.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Decisión Supervisor</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Evaluación: traslado a restauración externa o baja.</div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 8px 10px; margin-top: 12px;">
            <div style="font-size: 11.5px; color: #93C5FD;">
              💡 <em>Clic en el diagrama para explorar con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>
    </div>
"""
    content = content[:s5_start] + new_s5 + content[s6_start:]
    with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Slide 5 updated successfully!")
else:
    print("Could not locate boundaries for Slide 5")
