# -*- coding: utf-8 -*-
"""
update_deck_v10.py
Applies:
1. DCU (Slide 9):
   - Larger, sharper frame (height: 620px)
   - Snug image container (max-width: 580px, background: #121212) inside navy card (#0D1B33), eliminating black side borders.
   - Perfect mathematical sector zoom (setDcuSector) for Guardia, Supervisor, Ingreso, Admin, Ver Todo.
2. Idea 1 (Slide 11):
   - Interactive hotspots on tablet mockup for Steps 1, 2, 3 with electric blue glow, badges, and mutual card highlight.
3. Idea 3 (Slide 12):
   - Obra Domain Lifecycle Strip: Activa (En Sala) -> Inactiva (Incidente) -> En Restauración -> En Depósito (RN-1).
4. Idea 2 (Slide 13):
   - Dynamic 3-node connected visual pipeline: [ RF ] -> [ CU ] -> [ Clases DCD ] updating in real time.
5. Idea 4 (Global UI):
   - Floating keycap pill "⌨ Atajos" + macOS glassmorphism shortcuts modal with 3D mechanical keycaps.
"""

import re
import os

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# -------------------------------------------------------------------------
# 1. ADD CSS FOR HOTSPOTS, LIFECYCLE, PIPELINE, KEYCAPS & SHORTCUTS MODAL
# -------------------------------------------------------------------------
extra_css = '''
    /* --- IDEA 1: TABLET HOTSPOTS (SLIDE 11) --- */
    .tablet-mockup-wrapper {
      position: relative;
      display: inline-block;
      width: 100%;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.5);
    }
    .proto-hotspot {
      position: absolute;
      border: 2px dashed rgba(45, 127, 249, 0.45);
      background: rgba(45, 127, 249, 0.08);
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      z-index: 10;
    }
    .proto-hotspot:hover, .proto-hotspot.active {
      border: 2px solid #2D7FF9;
      background: rgba(45, 127, 249, 0.28);
      box-shadow: 0 0 22px rgba(45, 127, 249, 0.85);
      transform: scale(1.02);
    }
    .hotspot-badge {
      position: absolute;
      top: -11px;
      right: -11px;
      background: #2D7FF9;
      color: #FFFFFF;
      font-size: 11px;
      font-weight: 800;
      padding: 2px 9px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
      pointer-events: none;
      letter-spacing: 0.03em;
    }
    .proto-step-card {
      transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
      cursor: pointer;
    }
    .proto-step-card:hover {
      border-color: rgba(45, 127, 249, 0.5) !important;
      background: rgba(45, 127, 249, 0.08) !important;
    }
    .proto-step-card.active {
      border-color: #2D7FF9 !important;
      background: rgba(45, 127, 249, 0.16) !important;
      box-shadow: 0 0 18px rgba(45, 127, 249, 0.35);
      transform: translateX(6px);
    }

    /* --- IDEA 2: TRACE PIPELINE (SLIDE 13) --- */
    .trace-pipeline-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 14px;
    }
    .pipeline-node {
      flex: 1;
      border-radius: 8px;
      padding: 9px 12px;
      text-align: center;
      transition: all 0.3s ease;
    }
    .pipeline-arrow {
      color: #60A5FA;
      display: flex;
      align-items: center;
      justify-content: center;
      animation: pulseArrow 2s infinite ease-in-out;
    }
    @keyframes pulseArrow {
      0%, 100% { opacity: 0.6; transform: translateX(0); }
      50% { opacity: 1; transform: translateX(3px); }
    }

    /* --- IDEA 4: SHORTCUTS PILL & 3D KEYCAPS --- */
    .shortcuts-pill-btn {
      position: fixed;
      bottom: 24px;
      right: 28px;
      background: rgba(13, 27, 51, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #CBD5E1;
      padding: 8px 16px;
      border-radius: 24px;
      font-size: 13px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      transition: all 0.25s ease;
      z-index: 990;
    }
    .shortcuts-pill-btn:hover {
      background: rgba(45, 127, 249, 0.25);
      border-color: #2D7FF9;
      color: #FFFFFF;
      box-shadow: 0 0 20px rgba(45, 127, 249, 0.5);
      transform: translateY(-2px);
    }
    .shortcuts-modal {
      position: fixed;
      inset: 0;
      background: rgba(6, 13, 24, 0.78);
      backdrop-filter: blur(16px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 10000;
      animation: modalFadeIn 0.25s ease-out forwards;
    }
    .shortcuts-modal.active {
      display: flex;
    }
    .keycap {
      background: #1E293B;
      color: #F8FAFC;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
      font-size: 12.5px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.18);
      border-bottom: 3px solid #0B132B;
      box-shadow: 0 3px 6px rgba(0,0,0,0.4);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 28px;
    }
'''

# Insert extra_css right before </style>
if '.shortcuts-pill-btn' not in code:
    code = code.replace('  </style>', extra_css + '\n  </style>')
    print("Inserted extra CSS.")

# -------------------------------------------------------------------------
# 2. UPDATE SLIDE 9 (DCU)
# -------------------------------------------------------------------------
# Replace the slide-9 block with the upgraded version:
old_s9_pattern = r'(    <!-- SLIDE 9: DCU GENERAL.*?)(?=    <!-- SLIDE 10: PLANTILLA CU-15)'

new_s9 = '''    <!-- SLIDE 9: DCU GENERAL (MAXIMIZADO, SIN BANDAS NEGRAS Y ZOOM PRECISO) -->
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
    </div>\n\n'''

code = re.sub(old_s9_pattern, new_s9, code, flags=re.DOTALL)
print("Updated Slide 9 markup.")

# -------------------------------------------------------------------------
# 3. UPDATE SLIDE 11 (HOTSPOTS INTERACTIVOS EN PROTOTIPO TABLET)
# -------------------------------------------------------------------------
old_s11_pattern = r'(    <!-- SLIDE 11: PROTOTIPO DE PANTALLA.*?)(?=    <!-- SLIDE 12: DIAGRAMA DE CLASES)'

new_s11 = '''    <!-- SLIDE 11: PROTOTIPO DE PANTALLA CON HOTSPOTS INTERACTIVOS -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo UI</div>
      <h1 class="giant-title">Prototipo de Interfaz</h1>
      <p class="editorial-subtitle">
        Interfaz táctil para tablet de guardia y correspondencia interactiva con la plantilla (Sección 2.8 y 2.9 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; align-items: center;">
        <div class="diagram-frame-clean frame-proto-canvas reveal-item revealed" style="padding: 16px;">
          
          <!-- Tablet Mockup con Hotspots Activos -->
          <div class="tablet-mockup-wrapper">
            <img src="{b64_proto}" class="diagram-preview-img" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')" alt="Prototipo Tablet" style="width: 100%; height: auto; display: block;">

            <!-- Hotspot 1: Búsqueda de Obra (Pasos 2 a 4) -->
            <div id="hotspot-1" class="proto-hotspot" style="left: 12%; top: 22%; width: 44%; height: 27%;" onclick="highlightProtoStep(1)" onmouseenter="highlightProtoStep(1)" title="Paso 1: Búsqueda y Validación">
              <div class="hotspot-badge">Paso 1</div>
            </div>

            <!-- Hotspot 2: Tipificación del Siniestro (Pasos 7 y 8) -->
            <div id="hotspot-2" class="proto-hotspot" style="left: 12%; top: 51%; width: 76%; height: 23%;" onclick="highlightProtoStep(2)" onmouseenter="highlightProtoStep(2)" title="Paso 2: Tipificación del Siniestro">
              <div class="hotspot-badge">Paso 2</div>
            </div>

            <!-- Hotspot 3: Confirmación y Registro (Pasos 9 a 12) -->
            <div id="hotspot-3" class="proto-hotspot" style="left: 56%; top: 76%; width: 32%; height: 12%;" onclick="highlightProtoStep(3)" onmouseenter="highlightProtoStep(3)" title="Paso 3: Confirmación y Registro">
              <div class="hotspot-badge">Paso 3</div>
            </div>
          </div>

          <div class="diagram-action-bar" style="margin-top: 12px;">
            <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Interactuá con los hotspots o tarjetas para resaltar los pasos</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
              Ampliar pantalla {svg_expand}
            </button>
          </div>
        </div>

        <!-- 3 Tarjetas de Pasos Vinculadas a los Hotspots -->
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark proto-step-card reveal-item revealed" id="proto-step-card-1" onclick="highlightProtoStep(1)" onmouseenter="highlightProtoStep(1)">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">1. Búsqueda y Validación (Pasos 2 a 4)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Campo numérico para ingresar el código de la pieza y visualización inmediata del nombre, sala y ubicación física.
            </div>
          </div>

          <div class="card-dark proto-step-card reveal-item revealed" id="proto-step-card-2" onclick="highlightProtoStep(2)" onmouseenter="highlightProtoStep(2)">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">2. Tipificación del Siniestro (Pasos 7 y 8)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Selector desplegable con los tipos reglamentarios (Deterioro provocado, Caída accidental, Deterioro natural) y caja de texto para observaciones.
            </div>
          </div>

          <div class="card-dark proto-step-card reveal-item revealed" id="proto-step-card-3" onclick="highlightProtoStep(3)" onmouseenter="highlightProtoStep(3)">
            <div style="font-size: 12px; font-weight: 700; color: #38BDF8; text-transform: uppercase; margin-bottom: 6px;">3. Confirmación y Registro (Pasos 9 a 12)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El sistema solicita confirmación del incidente, el guardia confirma y la obra pasa a estado 'Inactivo' con registro de hora del servidor.
            </div>
          </div>
        </div>
      </div>
    </div>\n\n'''

code = re.sub(old_s11_pattern, new_s11, code, flags=re.DOTALL)
print("Updated Slide 11 markup.")

# -------------------------------------------------------------------------
# 4. UPDATE SLIDE 12 (DCD CON CICLO DE VIDA DE LA OBRA)
# -------------------------------------------------------------------------
old_s12_pattern = r'(    <!-- SLIDE 12: DIAGRAMA DE CLASES.*?)(?=    <!-- SLIDE 13: TRAZABILIDAD)'

new_s12 = '''    <!-- SLIDE 12: DIAGRAMA DE CLASES (CON CICLO DE VIDA DE OBRA RN-1) -->
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
      </div>

      <!-- IDEA 3: TIRA HORIZONTAL DE CICLO DE VIDA DE LA OBRA (ESTADOS DCD) -->
      <div style="margin-top: 16px; background: rgba(13, 27, 51, 0.85); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 12px 20px; display: flex; align-items: center; justify-content: space-between; gap: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.25);">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 11.5px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap;">Ciclo de Vida de Obra:</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; flex: 1; justify-content: space-around;">
          
          <div style="display: flex; align-items: center; gap: 8px; background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 6px 14px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #10B981; display: inline-block;"></span>
            <div>
              <div style="font-size: 12px; font-weight: 800; color: #6EE7B7;">Activa (En Sala)</div>
              <div style="font-size: 10.5px; color: #94A3B8;">Exhibición / Disponible</div>
            </div>
          </div>

          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>

          <div style="display: flex; align-items: center; gap: 8px; background: rgba(245, 158, 11, 0.1); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 6px 14px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #F59E0B; display: inline-block;"></span>
            <div>
              <div style="font-size: 12px; font-weight: 800; color: #FCD34D;">Inactiva (Incidente)</div>
              <div style="font-size: 10.5px; color: #94A3B8;">CU-15: Registro de daño</div>
            </div>
          </div>

          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>

          <div style="display: flex; align-items: center; gap: 8px; background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 6px 14px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #A855F7; display: inline-block;"></span>
            <div>
              <div style="font-size: 12px; font-weight: 800; color: #D8B4FE;">En Restauración</div>
              <div style="font-size: 10.5px; color: #94A3B8;">Taller / CU-04</div>
            </div>
          </div>

          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>

          <div style="display: flex; align-items: center; gap: 8px; background: rgba(45, 127, 249, 0.15); border: 1.5px solid #2D7FF9; border-radius: 8px; padding: 6px 14px;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #2D7FF9; display: inline-block;"></span>
            <div>
              <div style="font-size: 12px; font-weight: 800; color: #93C5FD;">En Depósito (RN-1)</div>
              <div style="font-size: 10.5px; color: #CBD5E1;">Reingreso obligatorio</div>
            </div>
          </div>

        </div>
      </div>
    </div>\n\n'''

code = re.sub(old_s12_pattern, new_s12, code, flags=re.DOTALL)
print("Updated Slide 12 markup.")

# -------------------------------------------------------------------------
# 5. UPDATE SLIDE 13 (PIPELINE GRÁFICO DINÁMICO DE TRAZABILIDAD)
# -------------------------------------------------------------------------
old_dossier_inner_pattern = r'(            <!-- Concept clarification note on traceability -->.*?)(?=            <!-- 3 Clean Structured Cards -->)'

new_dossier_pipeline = '''            <!-- IDEA 2: DYNAMIC TRACE PIPELINE (3 CONNECTED NODES) -->
            <div class="trace-pipeline-container">
              <div class="pipeline-node" style="background: rgba(45, 127, 249, 0.12); border: 1.5px solid #2D7FF9;">
                <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase;">1. Requerimiento (RF)</div>
                <div id="pipe-rf" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">RF-35: Registrar incidente</div>
              </div>

              <div class="pipeline-arrow">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </div>

              <div class="pipeline-node" style="background: rgba(56, 189, 248, 0.12); border: 1.5px solid #38BDF8;">
                <div style="font-size: 11px; font-weight: 800; color: #7DD3FC; text-transform: uppercase;">2. Caso de Uso (DCU)</div>
                <div id="pipe-cu" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">CU-15 (Guardia)</div>
              </div>

              <div class="pipeline-arrow">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </div>

              <div class="pipeline-node" style="background: rgba(129, 140, 248, 0.12); border: 1.5px solid #818CF8;">
                <div style="font-size: 11px; font-weight: 800; color: #C7D2FE; text-transform: uppercase;">3. Clases Dominio (DCD)</div>
                <div id="pipe-dcd" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Incidente &bull; Obra</div>
              </div>
            </div>

            <!-- Concept clarification note on traceability -->
            <div style="font-size: 13px; color: #94A3B8; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.07); margin-bottom: 14px;">
              💡 <strong>Correspondencia en ASI:</strong> Cada requerimiento funcional se concreta a través de uno o más Casos de Uso del sistema, los cuales interactúan con las clases del dominio para capturar y persistir los datos.
            </div>\n'''

code = re.sub(old_dossier_inner_pattern, new_dossier_pipeline, code, flags=re.DOTALL)
print("Updated Slide 13 markup.")

# -------------------------------------------------------------------------
# 6. ADD IDEA 4: SHORTCUTS PILL BUTTON & MODAL MARKUP
# -------------------------------------------------------------------------
shortcuts_markup = '''  <!-- IDEA 4: FLOATING QUICK-ACCESS SHORTCUTS PILL -->
  <button class="shortcuts-pill-btn" onclick="openShortcutsModal()" title="Ver atajos de teclado (o presiona ?)">
    <span>⌨</span> Atajos
  </button>

  <!-- IDEA 4: SHORTCUTS MODAL CON TECLAS 3D TIPO MAC -->
  <div class="shortcuts-modal" id="shortcuts-modal" onclick="if(event.target===this)closeShortcutsModal()">
    <div style="max-width: 520px; width: 90%; padding: 28px 32px; background: #0D1B33; border: 1px solid rgba(255,255,255,0.15); border-radius: 20px; box-shadow: 0 24px 60px rgba(0,0,0,0.7);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 14px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 22px;">⌨</span>
          <h3 style="font-size: 20px; font-weight: 800; color: #FFF; margin: 0;">Atajos de Teclado</h3>
        </div>
        <button class="modal-close-btn" onclick="closeShortcutsModal()">{svg_close}</button>
      </div>
      
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
          <span style="font-size: 13.5px; color: #E2E8F0;">Siguiente diapositiva</span>
          <div style="display: flex; gap: 6px;">
            <kbd class="keycap">&rarr;</kbd>
            <kbd class="keycap">Espacio</kbd>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
          <span style="font-size: 13.5px; color: #E2E8F0;">Diapositiva anterior</span>
          <kbd class="keycap">&larr;</kbd>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
          <span style="font-size: 13.5px; color: #E2E8F0;">Pantalla completa</span>
          <kbd class="keycap">F</kbd>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
          <span style="font-size: 13.5px; color: #E2E8F0;">Ver los 14 slides (Overview)</span>
          <kbd class="keycap">O</kbd>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: rgba(255,255,255,0.03); border-radius: 8px;">
          <span style="font-size: 13.5px; color: #E2E8F0;">Cerrar modal / Salir de zoom</span>
          <kbd class="keycap">Esc</kbd>
        </div>
      </div>

      <div style="margin-top: 20px; text-align: center; font-size: 12px; color: #94A3B8;">
        Presiona <kbd class="keycap" style="padding: 2px 7px; font-size: 11px;">?</kbd> o haz clic fuera para cerrar este panel
      </div>
    </div>
  </div>
'''

if 'id="shortcuts-modal"' not in code:
    code = code.replace('  <!-- Onboarding Mini-Tutorial Modal -->', shortcuts_markup + '\n  <!-- Onboarding Mini-Tutorial Modal -->')
    print("Inserted Shortcuts Modal markup.")

# -------------------------------------------------------------------------
# 7. UPDATE JAVASCRIPT FUNCTIONS:
#    - setDcuSector (Slide 9)
#    - highlightProtoStep (Slide 11)
#    - updateTraceDossier pipeline sync (Slide 13)
#    - openShortcutsModal / closeShortcutsModal / key listener (Global)
# -------------------------------------------------------------------------
js_extra = '''
    // ========================================================
    // PRECISE DCU SECTOR ZOOM (MATHEMATICALLY CENTERED)
    // ========================================================
    function setDcuSector(sector, btn) {{
      const img = document.getElementById('dcu-img');
      if (!img) return;
      if (btn) {{
        const btns = btn.parentElement.querySelectorAll('.preset-btn');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }}
      if (sector === 'guardia') {{
        // Guardia de vigilancia: act_vigilancia (CU 13, 14, 15, 16, 17)
        img.style.transformOrigin = '19% 62%';
        img.style.transform = 'scale(2.5)';
      }} else if (sector === 'supervisor') {{
        // Supervisor: act_seguridad (CU 18, 19, 20, 21, 22, 23)
        img.style.transformOrigin = '19% 86%';
        img.style.transform = 'scale(2.4)';
      }} else if (sector === 'ingreso') {{
        // Responsable de ingreso de obra: act_obras (CU 1, 2, 3, 4)
        img.style.transformOrigin = '19% 11%';
        img.style.transform = 'scale(2.4)';
      }} else if (sector === 'admin') {{
        // Admin de sistema: act_admin_sist (CU 24..42 Tablas Maestras)
        img.style.transformOrigin = '74% 18%';
        img.style.transform = 'scale(2.3)';
      }} else {{
        // Ver Todo (42 CUs)
        img.style.transformOrigin = 'center center';
        img.style.transform = 'scale(1)';
      }}
    }}

    // ========================================================
    // INTERACTIVE TABLET HOTSPOTS (SLIDE 11)
    // ========================================================
    function highlightProtoStep(step) {{
      for (let i = 1; i <= 3; i++) {{
        const hs = document.getElementById('hotspot-' + i);
        const card = document.getElementById('proto-step-card-' + i);
        if (hs) hs.classList.toggle('active', i === step);
        if (card) card.classList.toggle('active', i === step);
      }}
    }}

    // ========================================================
    // SHORTCUTS MODAL CONTROLS (IDEA 4)
    // ========================================================
    function openShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.add('active');
    }}
    function closeShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.remove('active');
    }}
'''

# Replace setDiagramPreset with js_extra
old_set_preset = r'    function setDiagramPreset\(imgId, scale, tx, ty\) \{.*?    \}'
code = re.sub(old_set_preset, js_extra, code, flags=re.DOTALL)
print("Replaced setDiagramPreset with precise setDcuSector and new JS handlers.")

# Update updateTraceDossier to also update pipeline nodes
old_update_dossier = r'(function updateTraceDossier\(item\) \{.*?document\.getElementById\(\'td-rationale\'\)\.innerText = item\.rationale;\s*\})'

new_update_dossier = '''function updateTraceDossier(item) {
      document.getElementById('td-rf-code').innerText = 'REQUERIMIENTO FUNCIONAL ' + item.rf;
      document.getElementById('td-rf-name').innerText = item.name;
      document.getElementById('td-cu-badge').innerText = item.cu.split(' ')[0];
      document.getElementById('td-cu-info').innerHTML = `<strong>${item.cu}</strong> &bull; Actor: ${item.actor}`;
      document.getElementById('td-dcd-info').innerHTML = `<strong>Clases DCD:</strong> ${item.dcd}<br><strong>Métodos / Lógica:</strong> <code>${item.methods}</code>`;
      document.getElementById('td-rationale').innerText = item.rationale;

      // Update Dynamic Pipeline Nodes (Idea 2)
      const pipeRf = document.getElementById('pipe-rf');
      const pipeCu = document.getElementById('pipe-cu');
      const pipeDcd = document.getElementById('pipe-dcd');
      if (pipeRf) pipeRf.innerText = item.rf + ': ' + item.name;
      if (pipeCu) pipeCu.innerText = item.cu.split(' ')[0] + ' (' + item.actor + ')';
      if (pipeDcd) pipeDcd.innerText = item.dcd.replace(/<[^>]+>/g, '').split(',').slice(0, 2).join(', ');
    }'''

code = code.replace(
'''    function updateTraceDossier(item) {{
      document.getElementById('td-rf-code').innerText = 'REQUERIMIENTO FUNCIONAL ' + item.rf;
      document.getElementById('td-rf-name').innerText = item.name;
      document.getElementById('td-cu-badge').innerText = item.cu.split(' ')[0];
      document.getElementById('td-cu-info').innerHTML = `<strong>${{item.cu}}</strong> &bull; Actor: ${{item.actor}}`;
      document.getElementById('td-dcd-info').innerHTML = `<strong>Clases DCD:</strong> ${{item.dcd}}<br><strong>Métodos / Lógica:</strong> <code>${{item.methods}}</code>`;
      document.getElementById('td-rationale').innerText = item.rationale;
    }}''',
'''    function updateTraceDossier(item) {{
      document.getElementById('td-rf-code').innerText = 'REQUERIMIENTO FUNCIONAL ' + item.rf;
      document.getElementById('td-rf-name').innerText = item.name;
      document.getElementById('td-cu-badge').innerText = item.cu.split(' ')[0];
      document.getElementById('td-cu-info').innerHTML = `<strong>${{item.cu}}</strong> &bull; Actor: ${{item.actor}}`;
      document.getElementById('td-dcd-info').innerHTML = `<strong>Clases DCD:</strong> ${{item.dcd}}<br><strong>Métodos / Lógica:</strong> <code>${{item.methods}}</code>`;
      document.getElementById('td-rationale').innerText = item.rationale;

      // Update Dynamic Pipeline Nodes (Idea 2)
      const pipeRf = document.getElementById('pipe-rf');
      const pipeCu = document.getElementById('pipe-cu');
      const pipeDcd = document.getElementById('pipe-dcd');
      if (pipeRf) pipeRf.innerText = item.rf + ': ' + item.name;
      if (pipeCu) pipeCu.innerText = item.cu.split(' ')[0] + ' (' + item.actor + ')';
      if (pipeDcd) pipeDcd.innerText = item.dcd.replace(/<[^>]+>/g, '').split(',').slice(0, 2).join(', ');
    }}'''
)
print("Updated updateTraceDossier for dynamic pipeline.")

# Also add '?' key to toggle shortcuts modal in keydown listener
if 'openShortcutsModal' not in code or "e.key === '?'" not in code:
    code = code.replace(
        "if (e.key === 'Escape') {",
        "if (e.key === '?' || e.key === 'h' || e.key === 'H') { openShortcutsModal(); return; }\n      if (e.key === 'Escape') { closeShortcutsModal();"
    )
    print("Added ? key handler.")

# Write updated generate_v8_deck.py
with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_v8_deck.py updated successfully!")
