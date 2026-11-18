# -*- coding: utf-8 -*-
"""
apply_bpmn_and_size_corrections.py
1. Slide 05 (BPMN Descriptivo):
   - Grid 1fr 240px (diagram gets maximum width).
   - Right-side card: short, brief description of how it was designed (Planteo del modelo en 3 carriles).
2. Slide 06 (BPMN Operativo):
   - Full-width large diagram (height 480px).
   - Below diagram: 3 short cards explicitly documenting the professor's BPMN corrections:
     (1. Datos de entrada Obras y Salas; 2. Estados explícitos 'Inactivo' / 'Sin novedades' / 'Observación pendiente'; 3. Roles separados y derivación a Restaurador RN-1).
3. Slide 09 (DCU):
   - Enormous diagram space! Grid 1fr 240px, frame height 670px, no max-width choking the inner container.
   - Right-side card: brief, clean description of the 42 CUs and actor scopes.
4. Slide 12 (DCD):
   - Enormous diagram space! Grid 1fr 240px, frame height 650px (image renders at ~1000px wide, perfectly legible).
   - Right-side card: brief, clean description of domain classes.
"""

import re

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# -------------------------------------------------------------------------
# 1. UPDATE SLIDE 5 (BPMN DESCRIPTIVO)
# -------------------------------------------------------------------------
old_s5 = '''    <!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="display: flex; flex-direction: column;">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1" style="flex: 1; object-fit: contain;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; Vista General</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Nivel 1 &bull; Alcance de Negocio</div>
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción del Modelo Descriptivo</h3>
            <p style="font-size: 13.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              Flujo global de negocio entre los tres actores clave: <strong>Guardia del Museo</strong>, <strong>Módulo Web</strong> y <strong>Supervisor</strong> (Sección 2.5 del TPI).
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ronda y Verificación Física</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia recorre las salas asignadas según la planificación y constata visualmente el estado de las obras expuestas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Detección y Registro Inmediato</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Al detectar cualquier anomalía, el guardia accede al Módulo Web y registra el incidente en el momento exacto (Regla de Negocio 2).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Evaluación y Decisión del Supervisor</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El supervisor analiza el incidente consolidado en el sistema y define el curso de acción: traslado a restauración externa o baja de la obra.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD;">
              💡 <em>Podés hacer clic en el diagrama o en "Ampliar" para verlo en pantalla completa con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>
    </div>'''

new_s5 = '''    <!-- SLIDE 5: BPMN DESCRIPTIVO (DIAGRAMA MAXIMIZADO) -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 240px; gap: 16px; align-items: stretch;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 600px; display: flex; flex-direction: column;">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1" style="flex: 1; width: 100%; object-fit: contain;">
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
            <h3 style="font-size: 16px; font-weight: 800; color: #FFF; margin-bottom: 8px;">Planteo del Modelo</h3>
            <p style="font-size: 12.5px; line-height: 1.5; color: var(--text-light); margin-bottom: 12px;">
              Coreografía del proceso de vigilancia entre los 3 carriles clave (Sección 2.5 del TPI):
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Guardia</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Recorrido físico por salas y reporte en tablet.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Módulo Web</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Validación de datos y consolidación de rondas.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Supervisor</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Análisis de incidentes y derivación a taller o baja.</div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 8px 10px; margin-top: 12px;">
            <div style="font-size: 11.5px; color: #93C5FD;">
              💡 <em>Clic en el diagrama para pantalla completa con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>
    </div>'''

if old_s5 in code:
    code = code.replace(old_s5, new_s5)
    print("Replaced Slide 5 with maximized diagram & compact description.")
else:
    print("WARNING: old_s5 exact match not found!")

# -------------------------------------------------------------------------
# 2. UPDATE SLIDE 6 (BPMN OPERATIVO CON CORRECCIONES DEL PROFESOR)
# -------------------------------------------------------------------------
old_s6 = '''<!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Compuerta exclusiva, bifurcación ante incidentes y eventos del flujo (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="max-height: 480px;">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="max-height: 380px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')" alt="BPMN Nivel 2">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Compuertas y Flujos</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Compuerta Exclusiva: Bifurcación en Sala</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              &bull; <strong>Camino Normal:</strong> Si todo está en orden, registra la sala con 'Sin novedades'.<br>
              &bull; <strong>Camino de Anomalía:</strong> Si detecta daño o anomalía, registra la sala con 'Observación pendiente' y ejecuta el registro del incidente.
            </div>
          </div>
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Consolidación de Datos y Cierre de Ronda</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Al completar el recorrido por todas las salas asignadas, el sistema consolida automáticamente el informe diario con el resumen de siniestros para análisis de supervisión.
            </div>
          </div>
        </div>
      </div>
    </div>'''

new_s6 = '''<!-- SLIDE 6: BPMN OPERATIVO (MAXIMIZADO + CORRECCIONES DEL PROFESOR) -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Flujo de control, alimentación de datos y estados del proceso (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Diagrama a tamaño máximo horizontal -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 440px; display: flex; flex-direction: column;">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')" alt="BPMN Nivel 2">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Compuertas, Datos y Estados</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- 3 Puntos concretos que explican cómo se planteó resolviendo las correcciones del profe -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
          
          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #2D7FF9;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">1. Alimentación de Datos</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              La tarea <em>Registrar incidente</em> consume datos maestros de <strong>Obras</strong> y <strong>Salas</strong>, recuperando acciones sugeridas según el material.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #60A5FA;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">2. Estados Explícitos</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              Compuerta bifurca a <strong>'Sin novedades'</strong> o <strong>'Observación pendiente'</strong>. El registro asienta la obra formalmente en estado <strong>'Inactivo'</strong>.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #38BDF8;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">3. Carriles y Derivación</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              El guardia solo reporta en tablet; los ABMs son de administración. La restauración se delega al <strong>Restaurador</strong> con reingreso a depósito (<strong>RN-1</strong>).
            </div>
          </div>

        </div>
      </div>
    </div>'''

if old_s6 in code:
    code = code.replace(old_s6, new_s6)
    print("Replaced Slide 6 with maximized diagram & 3 professor-corrections cards.")
else:
    print("WARNING: old_s6 exact match not found!")

# -------------------------------------------------------------------------
# 3. UPDATE SLIDE 9 (DCU - MAXIMIZAR ESPACIO DEL DIAGRAMA)
# -------------------------------------------------------------------------
old_s9 = '''    <!-- SLIDE 9: DCU GENERAL (MAXIMIZADO, SIN BANDAS NEGRAS Y ZOOM PRECISO) -->
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
            <button class="preset-btn active" onclick="setDcuSector('all', this)">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDcuSector('guardia', this)">Guardia (CU-14 / CU-15)</button>
            <button class="preset-btn" onclick="setDcuSector('supervisor', this)">Supervisor</button>
            <button class="preset-btn" onclick="setDcuSector('ingreso', this)">Ingreso y Obras</button>
            <button class="preset-btn" onclick="setDcuSector('admin', this)">Administrador</button>
          </div>

          <!-- Marco del diagrama: navy unificado, sin bandas negras laterales -->
          <div class="card-dark reveal-item revealed" style="height: 620px; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 20px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; background: #121212; border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.08); max-width: 580px; width: 100%; margin: 0 auto;">
              <img id="dcu-img" src="{b64_dcu}" style="height: 100%; width: auto; max-width: 100%; object-fit: contain; cursor: zoom-in; transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar" style="margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px;">
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
    </div>'''

new_s9 = '''    <!-- SLIDE 9: DCU GENERAL (MAXIMIZADO AL MÁXIMO ESPACIO) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 240px; gap: 16px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Sectorizar por Actor:</span>
            <button class="preset-btn active" onclick="setDcuSector('all', this)">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDcuSector('guardia', this)">Guardia (CU-14 / CU-15)</button>
            <button class="preset-btn" onclick="setDcuSector('supervisor', this)">Supervisor</button>
            <button class="preset-btn" onclick="setDcuSector('ingreso', this)">Ingreso y Obras</button>
            <button class="preset-btn" onclick="setDcuSector('admin', this)">Administrador</button>
          </div>

          <!-- Marco del diagrama: navy unificado, máxima amplitud visual -->
          <div class="card-dark reveal-item revealed" style="height: 670px; padding: 12px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 18px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; background: #121212; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.08); width: 100%; height: 100%;">
              <img id="dcu-img" src="{b64_dcu}" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in; transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
              <span style="font-size: 12.5px; font-weight: 600; color: #CBD5E1;">42 Casos de Uso &bull; Click para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 36px; padding: 0 14px; font-size: 12.5px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- CUADRO LATERAL CONCISO (BREVE DESCRIPCIÓN) -->
        <div class="card-dark reveal-item revealed" style="padding: 20px 18px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Frontera del Software</div>
            <h3 style="font-size: 16px; font-weight: 800; color: #FFF; margin-bottom: 8px;">42 Casos de Uso</h3>
            <p style="font-size: 12.5px; line-height: 1.5; color: var(--text-light); margin-bottom: 12px;">
              Estructurados por actor y módulo funcional según la Sección 2.7 del TPI:
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Guardia (CU 13–17)</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Rondas e incidentes en sala.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Supervisor (CU 18–23)</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Patrones, seguimiento e informes.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Obras (CU 1–4)</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Ingreso, restauración y depósito.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Admin / Tablas (CU 24–42)</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Salas, materiales, tipos de daño.</div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 8px 10px; margin-top: 12px;">
            <div style="font-size: 11.5px; color: #93C5FD;">
              💡 <em>Usá los botones superiores para enfocar por actor o click para ampliar.</em>
            </div>
          </div>
        </div>
      </div>
    </div>'''

if old_s9 in code:
    code = code.replace(old_s9, new_s9)
    print("Replaced Slide 9 with maximized diagram & compact description.")
else:
    print("WARNING: old_s9 exact match not found!")

# -------------------------------------------------------------------------
# 4. UPDATE SLIDE 12 (DCD - MAXIMIZAR ESPACIO DEL DIAGRAMA)
# -------------------------------------------------------------------------
old_s12 = '''    <!-- SLIDE 12: DIAGRAMA DE CLASES (CON CICLO DE VIDA DE OBRA RN-1) -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 310px; gap: 20px; align-items: stretch;">
        <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 560px; display: flex; flex-direction: column;">
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

        <!-- CUADRO LATERAL CONCRETO Y SIN RELLENO -->
        <div class="card-dark reveal-item revealed" style="padding: 24px 20px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Estructura de Datos</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px;">Clases del Sistema</h3>
            
            <p style="font-size: 13.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              Estructura estática de entidades, atributos, visibilidad y relaciones según la Sección 2.10 del TPI.
            </p>

            <div style="display: flex; flex-direction: column; gap: 10px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Incidente y TipoIncidente</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Registro con fecha, hora, descripción y puntero al catálogo de tipos.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Obra y Estado</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Patrón Estado para transición entre Activa, Inactiva y En Restauración.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Ronda de Vigilancia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Planificación y revisiones efectivas asociadas a cada sala del museo.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 10px 12px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Depósito y Reingreso (RN-1)</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 2px;">
                  Toda obra restaurada debe reingresar obligatoriamente a depósito.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD;">
              💡 <em>Hacé clic en el diagrama para explorar con zoom interactivo.</em>
            </div>
          </div>
        </div>
      </div>'''

new_s12 = '''    <!-- SLIDE 12: DIAGRAMA DE CLASES (MAXIMIZADO AL MÁXIMO ESPACIO) -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 240px; gap: 16px; align-items: stretch;">
        <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 650px; display: flex; flex-direction: column; padding: 12px;">
          <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%;">
            <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
          </div>
          <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
            <span style="font-size: 12.5px; font-weight: 600; color: #CBD5E1;">Clases, Atributos y Métodos &bull; Click para zoom interactivo</span>
            <button class="btn-primary" style="min-height: 36px; padding: 0 14px; font-size: 12.5px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
              Ampliar {svg_expand}
            </button>
          </div>
        </div>

        <!-- CUADRO LATERAL CONCISO (BREVE DESCRIPCIÓN) -->
        <div class="card-dark reveal-item revealed" style="padding: 20px 18px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Modelo de Dominio</div>
            <h3 style="font-size: 16px; font-weight: 800; color: #FFF; margin-bottom: 8px;">Clases del Sistema</h3>
            <p style="font-size: 12.5px; line-height: 1.5; color: var(--text-light); margin-bottom: 12px;">
              Entidades y responsabilidades según la Sección 2.10 del TPI:
            </p>

            <div style="display: flex; flex-direction: column; gap: 8px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Incidente y Tipo</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Fecha, hora, descripción y catálogo.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Obra y Estado</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Patrón estado y material para acciones sugeridas.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Sala y Ronda</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Interacción SalaXGuardia y revisiones.</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 7px 10px; border-radius: 0 6px 6px 0;">
                <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Depósito (RN-1)</div>
                <div style="font-size: 12px; color: var(--text-light); margin-top: 1px;">Reingreso obligatorio post restauración.</div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 8px 10px; margin-top: 12px;">
            <div style="font-size: 11.5px; color: #93C5FD;">
              💡 <em>Clic en el diagrama para explorar con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>'''

if old_s12 in code:
    code = code.replace(old_s12, new_s12)
    print("Replaced Slide 12 with maximized diagram & compact description.")
else:
    print("WARNING: old_s12 exact match not found!")

# Write updated generate_v8_deck.py
with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_v8_deck.py successfully!")
