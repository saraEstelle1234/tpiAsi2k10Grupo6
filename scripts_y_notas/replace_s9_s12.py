# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

s9_idx = code.find('<!-- SLIDE 9: DCU GENERAL')
s10_idx = code.find('<!-- SLIDE 10: PLANTILLA CU-15')

s9_replacement = """<!-- SLIDE 9: DCU GENERAL (MAXIMIZADO Y LIMPIO) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 310px; gap: 20px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Sectorizar por Actor:</span>
            <button class="preset-btn active" onclick="setDiagramPreset('dcu-img', 1, 0, 0)">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.3, -20, -22)">Guardia (CU-14 / CU-15)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.0, 18, -16)">Supervisor</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.1, -20, 22)">Ingreso y Obras</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 1.9, 20, 20)">Administrador</button>
          </div>

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 580px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcu-img" src="{b64_dcu}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">42 Casos de Uso &bull; Click para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- CUADRO LATERAL CONCRETO Y SIN RELLENO -->
        <div class="card-dark reveal-item revealed" style="padding: 24px 20px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Alcance Funcional</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px;">Casos de Uso del Sistema</h3>
            
            <p style="font-size: 13.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              Modelado de los <strong>42 Casos de Uso</strong> del software y sus actores según la Sección 2.7 del TPI.
            </p>

            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Guardia de Vigilancia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Revisión de sala (CU-14) y registro de incidente (CU-15).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Supervisor</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Consulta de incidentes, seguimiento e informes diarios y mensuales.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Encargado de Obras</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Ingreso de obras, derivación a restauración y reingreso a depósito.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Administrador y Guía</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Maestros, exposiciones, visitas guiadas y boletería.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD;">
              💡 <em>Usá los botones superiores para enfocar por actor o hacé clic para pantalla completa.</em>
            </div>
          </div>
        </div>
      </div>
    </div>\n\n    """

code = code[:s9_idx] + s9_replacement + code[s10_idx:]

# Now find slide 12 and slide 13
s12_idx = code.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
s13_idx = code.find('<!-- SLIDE 13: TRAZABILIDAD')

s12_replacement = """<!-- SLIDE 12: DIAGRAMA DE CLASES (MAXIMIZADO Y LIMPIO) -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 310px; gap: 20px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 580px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">Clases, Atributos y Métodos &bull; Click para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
                Ampliar {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- CUADRO LATERAL CONCRETO Y SIN CHAMUYO -->
        <div class="card-dark reveal-item revealed" style="padding: 24px 20px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Estructura del Dominio</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px;">Clases del Sistema</h3>
            
            <p style="font-size: 13.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              El diagrama modela la estructura estática de entidades del museo y sus relaciones (Sección 2.10 del TPI).
            </p>

            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Patrimonio y Obras</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  <code>Obra</code>, <code>Autor</code>, <code>Estilo</code>, <code>Material</code>, <code>TipoObra</code>, <code>TipoIngreso</code> y <code>Estado</code>.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Incidentes y Seguridad</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  <code>Incidente</code> y <code>TipoIncidente</code>, vinculados a la <code>Obra</code> afectada.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Rondas de Guardia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  <code>Guardia</code> y <code>Sala</code>, conectadas por la clase asociativa <code>SalaXGuardia</code>.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Atención y Servicios</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  <code>Exposicion</code>, <code>VisitaGuiada</code>, <code>Guia</code>, <code>Entrada</code>, <code>Tarifa</code> y <code>Visitante</code>.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD;">
              💡 <em>Hacé clic en el diagrama o en "Ampliar" para examinar atributos y métodos con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>
    </div>\n\n    """

code = code[:s12_idx] + s12_replacement + code[s13_idx:]

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Slide 9 and Slide 12 replaced successfully in generate_v8_deck.py!")
