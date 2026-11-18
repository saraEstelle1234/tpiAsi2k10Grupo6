# -*- coding: utf-8 -*-
"""
update_deck_v9.py
Applies the exact user refinements:
1. Slide 7: Larger requirement fonts (.rf-summary, .rf-item, .rf-num).
2. Slide 9: DCU diagram maximized (grid 1fr 310px, 580px height), clean factual sidebar without chamuyo.
3. Slide 12: DCD diagram maximized (grid 1fr 310px, 580px height), clean factual sidebar of domain classes without chamuyo (no wall of text on reingreso).
4. Slide 13:
   - Much larger, spacious trace console (grid 400px 1fr, 560px min-height).
   - Removed awkward overflow scrollbars; clean thin scrollbar on list, overflow visible on dossier.
   - RF items in list have 15.5px bold readable font.
   - Clear visual link: RF -> Associated CU(s) -> DCD classes.
   - Removed 'garantía de integridad del 100%' footer.
"""

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update CSS for RF items and Trace console
# Find .rf-summary and .rf-item in CSS
old_rf_css = """.rf-summary {
  padding: 12px 18px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  font-weight: 700;
  color: #FFFFFF;
  user-select: none;
}"""

new_rf_css = """.rf-summary {
  padding: 14px 20px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
  font-weight: 700;
  color: #FFFFFF;
  user-select: none;
}"""

if old_rf_css in code:
    code = code.replace(old_rf_css, new_rf_css)

old_rf_item_css = """.rf-item {
  font-size: 13px;
  color: var(--text-light);
  padding: 6px 14px;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.03);
  display: flex;
  align-items: center;
  gap: 8px;
}

.rf-num {
  font-weight: 700;
  color: var(--blue-accent);
  font-size: 12px;
}"""

new_rf_item_css = """.rf-item {
  font-size: 15.5px;
  color: #F1F5F9;
  padding: 10px 16px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.035);
  display: flex;
  align-items: center;
  gap: 12px;
  line-height: 1.4;
}

.rf-num {
  font-weight: 800;
  color: #60A5FA;
  font-size: 14.5px;
}"""

if old_rf_item_css in code:
    code = code.replace(old_rf_item_css, new_rf_item_css)

# Update trace CSS
old_trace_css = """.trace-matrix-console {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 20px;
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 20px;
  padding: 24px;
}

.trace-rf-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 480px;
  overflow-y: auto;
  padding-right: 6px;
}

.trace-rf-item {
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 13.5px;
}

.trace-rf-item:hover, .trace-rf-item.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

.trace-impact-dossier {
  background: #0B172B;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}"""

new_trace_css = """.trace-matrix-console {
  display: grid;
  grid-template-columns: 400px 1fr;
  gap: 24px;
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 20px;
  padding: 24px 28px;
  min-height: 560px;
}

.trace-rf-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-height: 520px;
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 8px;
  scrollbar-width: thin;
  scrollbar-color: rgba(45, 127, 249, 0.4) transparent;
}

.trace-rf-list::-webkit-scrollbar {
  width: 6px;
}
.trace-rf-list::-webkit-scrollbar-thumb {
  background: rgba(45, 127, 249, 0.4);
  border-radius: 4px;
}

.trace-rf-item {
  padding: 14px 18px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 15px;
}

.trace-rf-item:hover, .trace-rf-item.active {
  background: rgba(45, 127, 249, 0.22);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

.trace-impact-dossier {
  background: #0B172B;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 24px 28px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 14px;
  min-height: 520px;
  overflow: visible;
}"""

if old_trace_css in code:
    code = code.replace(old_trace_css, new_trace_css)
else:
    print("Could not find exact old_trace_css")

# 2. Slide 9: Maximize DCU and Clean Sidebar
s9_old = """<!-- SLIDE 9: DCU GENERAL (AMPLIADO Y SECTORIZADO POR ACTOR) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.55fr 0.45fr; gap: 24px; align-items: stretch;">
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

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcu-img" src="{b64_dcu}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: zoom-in;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">42 Casos de Uso &bull; Fondo nativo sin bordes negros</span>
              <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar a pantalla completa <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
              </button>
            </div>
          </div>
        </div>

        <!-- UN SOLO CUADRO EXPLICATIVO GENERAL -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Límites y Concepción</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción General del Diagrama</h3>
            
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              El modelo define el límite completo del software mediante <strong>42 Casos de Uso</strong> numerados de forma unívoca y continua, satisfaciendo el proceso sustantivo (<em>Exponer obras de arte</em>) y el proceso de soporte crítico bajo estudio (<em>Gestionar incidentes y restauración</em>).
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">8 Actores del Sistema</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  7 roles humanos con accesos diferenciados y 1 temporizador de software (<em>Administrador Web</em>) que dispara la planificación de rondas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Separación Operativa / Gerencial</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia opera en terminal móvil (revisión y reporte), mientras que supervisores y administradores gestionan el catálogo patrimonial e informes.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Centralidad de la Vigilancia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El <strong>CU-15 (Registrar incidente)</strong> constituye el núcleo de integración entre la detección en sala y la custodia patrimonial.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Navegación Interactiva</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Utilizá los botones superiores para enfocar la sección de cada actor o hacé clic en el diagrama para explorar con zoom libre.
            </div>
          </div>
        </div>
      </div>
    </div>"""

s9_new = """<!-- SLIDE 9: DCU GENERAL (MAXIMIZADO Y LIMPIO) -->
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
                Ampliar <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
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
    </div>"""

if s9_old in code:
    code = code.replace(s9_old, s9_new)
    print("Replaced Slide 9 successfully!")
else:
    print("Could not find exact s9_old")

# 3. Slide 12: Maximize DCD and Clean Sidebar (No wall of text on reingreso)
s12_old = """<!-- SLIDE 12: DIAGRAMA DE CLASES -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.55fr 0.45fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">Clases, Atributos, Métodos y Multiplicidades del Dominio</span>
              <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
                Ampliar a pantalla completa <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
              </button>
            </div>
          </div>
        </div>

        <!-- UN SOLO CUADRO EXPLICATIVO GENERAL DE LA LÓGICA -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Lógica y Diseño OO</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción y Lógica del Modelo de Dominio</h3>
            
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              El modelo estático plasma la persistencia y la lógica de negocio requerida para la gestión patrimonial y el proceso de vigilancia, estructurando las entidades según directivas de cátedra.
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ciclo del Incidente y Tipificación</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  La clase <code>Incidente</code> captura fecha, hora del servidor y descripción. Se vincula con multiplicidad obligatoria <strong>1</strong> a <code>TipoIncidente</code> y a la <code>Obra</code> afectada.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Transición de Estado de Obra</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Al registrarse el incidente, el método <code>registrarIncidente()</code> en la clase <code>Obra</code> actualiza su puntero hacia <code>Estado</code> a <em>'Inactivo'</em> (Regla de Negocio 2).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Histórico de Rondas (SalaXGuardia)</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  La clase asociativa <code>SalaXGuardia</code> modela la relación 1 a muchos (1..*), preservando la fecha y hora de inspección de cada guardia por cada sala recorrida.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">4. Regla de Reingreso Obligatorio</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Sustento de la RN-1: toda obra reparada o no solo egresa de restauración mediante el método <code>registrarReingreso()</code> al depósito del museo.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Visor de Alta Resolución</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Hacé clic en el diagrama para examinar cada clase con zoom de rueda del mouse y desplazamiento panorámico libre.
            </div>
          </div>
        </div>
      </div>
    </div>"""

s12_new = """<!-- SLIDE 12: DIAGRAMA DE CLASES (MAXIMIZADO Y LIMPIO) -->
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
                Ampliar <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
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
    </div>"""

if s12_old in code:
    code = code.replace(s12_old, s12_new)
    print("Replaced Slide 12 successfully!")
else:
    print("Could not find exact s12_old")

# 4. Slide 13: Expand Traceability, Eliminate Awkward Overflow, Remove "garantía 100%"
s13_old = """<!-- SLIDE 13: TRAZABILIDAD COMPLETA (RF <-> CU <-> DCD) -->
    <div class="slide" id="slide-13" data-topic="13 · Trazabilidad de Requerimientos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Matriz completa de correspondencia: Requerimiento Funcional (RF) &rarr; Caso de Uso (CU) &rarr; Diagrama de Clases (DCD)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"/>
            <circle cx="6" cy="12" r="3"/>
            <circle cx="18" cy="19" r="3"/>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
          </svg>
        </div>
      </div>

      <!-- Filter Controls Bar -->
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 12px;">
        <input type="text" id="trace-search-input" class="search-input" placeholder="🔍 Filtrar trazabilidad (ej: RF-35, incidente, obra, sala, ronda, informe)..." oninput="filterTraceMatrix()" style="flex: 1; height: 42px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 0 16px; color: #FFF; font-size: 13.5px;">
        
        <div class="trace-module-pills" style="margin-bottom: 0; display: flex; gap: 6px;">
          <button class="trace-module-btn active" onclick="filterTraceModule(this, 'ALL')">Todos (34)</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'INCIDENTES')">Incidentes y Rondas</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'OBRAS')">Obras y Depósito</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'MAESTROS')">Salas y Maestros</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'REPORTES')">Informes</button>
        </div>
      </div>

      <!-- Interactive Trace Matrix Console -->
      <div class="trace-matrix-console reveal-item revealed" style="margin-bottom: 0;">
        <!-- Left Column: Scrollable List of All Mapped Requirements -->
        <div style="width: 38%; display: flex; flex-direction: column;">
          <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 8px;">
            Seleccionar Requerimiento Funcional:
          </div>
          <div class="trace-rf-list" id="trace-items-container" style="max-height: 440px; overflow-y: auto; padding-right: 6px;">
            <!-- Dynamically populated / hardcoded items -->
          </div>
        </div>

        <!-- Right Column: Detail Dossier of Selected Trace Link -->
        <div class="trace-impact-dossier" id="trace-dossier-panel" style="width: 62%; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 14px;">
              <div>
                <span style="font-size: 12px; font-weight: 700; color: #93C5FD; text-transform: uppercase;" id="td-rf-code">REQUERIMIENTO FUNCIONAL RF-35</span>
                <div style="font-size: 17px; font-weight: 800; color: #FFF; margin-top: 2px;" id="td-rf-name">Registrar incidente</div>
              </div>
              <span style="font-size: 12px; font-weight: 800; background: var(--blue-accent); color: #FFF; padding: 4px 12px; border-radius: 6px;" id="td-cu-badge">CU-15</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #60A5FA; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Caso de Uso Asociado (DCU)</span>
                <span id="td-cu-info" style="color: #FFF; font-weight: 600; font-size: 13.5px;">CU-15: Registrar incidente &bull; Actor: Encargado de vigilancia (EV)</span>
              </div>

              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #38BDF8; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Clases, Atributos y Métodos Afectados (DCD)</span>
                <span id="td-dcd-info" style="color: var(--text-light); line-height: 1.5;">
                  <strong>Clases:</strong> <code>Incidente</code>, <code>TipoIncidente</code>, <code>Obra</code>, <code>Estado</code>.<br>
                  <strong>Método invocado:</strong> <code>obra.registrarIncidente()</code> actualiza puntero a Estado 'Inactivo'.
                </span>
              </div>

              <div style="background: rgba(47,107,255,0.08); border-left: 3px solid var(--blue-accent); padding: 12px 14px; border-radius: 0 8px 8px 0;">
                <span style="color: #93C5FD; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Justificación de Trazabilidad y Lógica</span>
                <span id="td-rationale" style="color: var(--text-light); font-size: 12.5px; line-height: 1.55;">
                  El requerimiento exige documentar el daño in situ. El CU-15 materializa la interacción en tablet, y el DCD persiste el hecho en la entidad Incidente vinculada obligatoriamente a TipoIncidente, actualizando en la misma transacción el estado de la obra para su derivación por supervisión.
                </span>
              </div>
            </div>
          </div>

          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 14px; margin-top: 14px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 12px; color: var(--text-light-secondary);">
              Garantía de Integridad: Todo caso de uso implementa al menos un RF y se persiste en entidades del DCD.
            </span>
            <span style="font-size: 11px; font-weight: 700; background: rgba(16,185,129,0.2); color: #6EE7B7; padding: 3px 8px; border-radius: 4px;">TRAZABILIDAD 100%</span>
          </div>
        </div>
      </div>
    </div>"""

s13_new = """<!-- SLIDE 13: TRAZABILIDAD (AMPLIADA, LEGIBLE Y SIN CHAMUYO) -->
    <div class="slide" id="slide-13" data-topic="13 · Trazabilidad de Requerimientos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Correspondencia: Requerimiento Funcional (RF) &rarr; Caso(s) de Uso Asociado(s) &rarr; Clases del Dominio (DCD)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 6px;">
          <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"/>
            <circle cx="6" cy="12" r="3"/>
            <circle cx="18" cy="19" r="3"/>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
          </svg>
        </div>
      </div>

      <!-- Filter Controls Bar -->
      <div style="display: flex; gap: 14px; align-items: center; margin-bottom: 14px;">
        <input type="text" id="trace-search-input" class="search-input" placeholder="🔍 Filtrar trazabilidad (ej: RF-35, obra, sala, ronda, incidente)..." oninput="filterTraceMatrix()" style="flex: 1; height: 44px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0 18px; color: #FFF; font-size: 14px;">
        
        <div class="trace-module-pills" style="margin-bottom: 0; display: flex; gap: 8px;">
          <button class="trace-module-btn active" onclick="filterTraceModule(this, 'ALL')">Todos (34)</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'INCIDENTES')">Incidentes y Rondas</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'OBRAS')">Obras y Depósito</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'MAESTROS')">Salas y Maestros</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'REPORTES')">Informes</button>
        </div>
      </div>

      <!-- Interactive Trace Matrix Console -->
      <div class="trace-matrix-console reveal-item revealed" style="margin-bottom: 0;">
        <!-- Left Column: Requerimientos Funcionales -->
        <div style="display: flex; flex-direction: column;">
          <div style="font-size: 12px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 10px;">
            Requerimientos Funcionales del Sistema:
          </div>
          <div class="trace-rf-list" id="trace-items-container">
            <!-- Dynamically populated items -->
          </div>
        </div>

        <!-- Right Column: Detail Dossier of Selected Trace Link -->
        <div class="trace-impact-dossier" id="trace-dossier-panel">
          <div>
            <!-- Header of Selected RF -->
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 14px; margin-bottom: 16px;">
              <div>
                <span style="font-size: 12.5px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.05em;" id="td-rf-code">REQUERIMIENTO FUNCIONAL RF-35</span>
                <div style="font-size: 22px; font-weight: 800; color: #FFF; margin-top: 3px;" id="td-rf-name">Registrar incidente</div>
              </div>
              <span style="font-size: 13.5px; font-weight: 800; background: var(--blue-accent); color: #FFF; padding: 6px 14px; border-radius: 8px;" id="td-cu-badge">CU-15</span>
            </div>

            <!-- Concept clarification note on traceability -->
            <div style="font-size: 13px; color: #94A3B8; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.07); margin-bottom: 14px;">
              💡 <strong>Correspondencia en ASI:</strong> Cada requerimiento funcional se concreta a través de uno o más Casos de Uso del sistema, los cuales interactúan con las clases del dominio para capturar y persistir los datos.
            </div>

            <!-- 3 Clean Structured Cards -->
            <div style="display: flex; flex-direction: column; gap: 14px;">
              
              <!-- Card 1: Caso de Uso Asociado -->
              <div style="background: rgba(255,255,255,0.035); border-left: 3px solid #2D7FF9; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #60A5FA; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Caso de Uso Asociado (DCU)</span>
                <span id="td-cu-info" style="color: #FFF; font-weight: 700; font-size: 15px;">CU-15: Registrar incidente &bull; Actor: Encargado de vigilancia</span>
              </div>

              <!-- Card 2: Clases del Dominio Afectadas -->
              <div style="background: rgba(255,255,255,0.035); border-left: 3px solid #38BDF8; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #38BDF8; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Clases del Dominio Afectadas (DCD)</span>
                <span id="td-dcd-info" style="color: #E2E8F0; font-size: 14.5px; line-height: 1.55;">
                  <strong>Clases:</strong> <code>Incidente</code>, <code>TipoIncidente</code>, <code>Obra</code>, <code>Estado</code>.<br>
                  <strong>Método invocado:</strong> <code>obra.registrarIncidente()</code> actualiza puntero a Estado 'Inactivo'.
                </span>
              </div>

              <!-- Card 3: Justificación Concreta -->
              <div style="background: rgba(45,127,249,0.08); border-left: 3px solid #60A5FA; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #93C5FD; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Explicación de la Trazabilidad</span>
                <span id="td-rationale" style="color: #CBD5E1; font-size: 14px; line-height: 1.55;">
                  El requerimiento define el registro del daño. El CU-15 materializa el flujo en pantalla, y el DCD persiste el hecho en la entidad Incidente vinculada a TipoIncidente y a la Obra.
                </span>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>"""

if s13_old in code:
    code = code.replace(s13_old, s13_new)
    print("Replaced Slide 13 successfully!")
else:
    print("Could not find exact s13_old")

# 5. Update renderTraceMatrixItems in JS to generate larger, clearer items
old_render_item = """        div.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong style="color: var(--blue-accent);">${{item.rf}}</strong>
            <span style="font-size: 10.5px; font-weight: 700; background: rgba(47,107,255,0.18); color: #93C5FD; padding: 2px 6px; border-radius: 4px;">${{item.cu.split(' ')[0]}}</span>
          </div>
          <div style="font-size: 12.5px; color: #FFF; margin-top: 3px; font-weight: 600;">${{item.name}}</div>
        `;"""

new_render_item = """        div.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
            <strong style="color: #60A5FA; font-size: 14px; font-weight: 800; letter-spacing: 0.03em;">${{item.rf}}</strong>
            <span style="font-size: 12px; font-weight: 800; background: rgba(45, 127, 249, 0.22); color: #93C5FD; border: 1px solid rgba(45, 127, 249, 0.35); padding: 3px 8px; border-radius: 6px;">${{item.cu.split(' ')[0]}}</span>
          </div>
          <div style="font-size: 15px; color: #FFFFFF; font-weight: 600; line-height: 1.35;">${{item.name}}</div>
        `;"""

if old_render_item in code:
    code = code.replace(old_render_item, new_render_item)
    print("Replaced renderTraceMatrixItems innerHTML successfully!")
else:
    print("Could not find exact old_render_item")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_v8_deck.py with v9 improvements!")
