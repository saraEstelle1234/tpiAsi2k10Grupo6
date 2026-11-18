# -*- coding: utf-8 -*-
"""
apply_final_polish.py
1. Slide 2: Replace redundant "Regla de reingreso" card 03 with "Proceso Esencial del Negocio" (Sección 2.1 del TPI).
2. Slide 4: Add "Observaciones: No aplica" to the official process table.
3. Slide 5: Remove redundant RN-1 bottom card from BPMN Descriptivo.
4. Slide 12: Make DCD diagram even larger (grid 1fr 265px, height 610px).
5. Slide 14:
   - Giant "¡Muchas Gracias!"
   - Institutional block: UTN FRC, Cátedra ASI, Curso 2K10, Año 2026.
   - Evaluator Professors: Cattaneo, Turanzas, Sanchez, Padilla.
   - 9 Members in compact, elegant 3x3 cards with legajos.
   - Aesthetic SVG logo and action buttons.
"""

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# ========================================================
# 1. SLIDE 2 UPDATE
# ========================================================
s2_old_target = """        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">03</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Regla de Reingreso Obligatorio a Depósito</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Luego de restauradas las obras reingresan al depósito del museo y quedan disponibles para lo que se las requiera.
          </div>
          <div class="card-extra-content">
            Texto textual del enunciado y TPI: Aún si las obras no pueden restaurarse son ingresadas nuevamente al depósito para luego decidir el momento para retirarla del museo, es decir, darle de baja. Ninguna pieza retorna directamente a sala de exhibición.
          </div>
        </div>"""

s2_new_target = """        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">03</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Proceso Esencial del Negocio</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Exponer obras de arte: proceso clave que entrega valor a la comunidad y cliente del proceso de vigilancia.
          </div>
          <div class="card-extra-content">
            Definido en la Sección 2.1 del TPI: la exposición artística es el proceso sustantivo sobre el cual se articulan las rondas de inspección física y la custodia del patrimonio cultural.
          </div>
        </div>"""

if s2_old_target in code:
    code = code.replace(s2_old_target, s2_new_target)
    print("Slide 2 updated successfully!")
else:
    print("WARNING: s2_old_target not found")

# ========================================================
# 2. SLIDE 4 OBSERVACIONES
# ========================================================
s4_old_table_end = """                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">2.</td>
                      <td style="font-weight: 600; color: #FFF;">Registro inmediato de incidente</td>
                      <td>El guardia debe registrar el incidente de la obra de forma inmediata, indicando detalles del incidente.</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>"""

s4_new_table_end = """                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">2.</td>
                      <td style="font-weight: 600; color: #FFF;">Registro inmediato de incidente</td>
                      <td>El guardia debe registrar el incidente de la obra de forma inmediata, indicando detalles del incidente.</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Observaciones</td>
              <td class="tpi-col-content" style="color: var(--text-light-secondary); font-style: italic;">
                &mdash; (No aplica)
              </td>
            </tr>
          </tbody>
        </table>"""

if s4_old_table_end in code:
    code = code.replace(s4_old_table_end, s4_new_table_end)
    print("Slide 4 (Observaciones: No aplica) added successfully!")
else:
    print("WARNING: s4_old_table_end not found")

# ========================================================
# 3. SLIDE 5 CLEANUP (Remove redundant RN-1 box)
# ========================================================
s5_old_box = """          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Regla Fundamental de Integridad</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Toda obra restaurada reingresa obligatoriamente al depósito del museo antes de definir cualquier nuevo destino o exhibición (RN-1).
            </div>
          </div>"""

s5_new_box = """          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD;">
              💡 <em>Podés hacer clic en el diagrama o en "Ampliar" para verlo en pantalla completa con zoom libre.</em>
            </div>
          </div>"""

if s5_old_box in code:
    code = code.replace(s5_old_box, s5_new_box)
    print("Slide 5 cleaned up successfully!")
else:
    print("WARNING: s5_old_box not found")

# ========================================================
# 4. SLIDE 12 DCD ENLARGED (grid 1fr 265px, height 610px)
# ========================================================
s12_old_grid = """      <div style="display: grid; grid-template-columns: 1fr 310px; gap: 20px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 580px; display: flex; flex-direction: column;">"""

s12_new_grid = """      <div style="display: grid; grid-template-columns: 1fr 265px; gap: 16px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 610px; display: flex; flex-direction: column;">"""

if s12_old_grid in code:
    code = code.replace(s12_old_grid, s12_new_grid)
    print("Slide 12 DCD diagram enlarged to 610px and 1fr 265px successfully!")
else:
    print("WARNING: s12_old_grid not found")

# ========================================================
# 5. SLIDE 14 COMPLETE REDESIGN
# ========================================================
# Find slide 14
idx_s14 = code.find('<!-- SLIDE 14: CIERRE & AGRADECIMIENTO')
idx_s14_end = code.find('<!-- Hotspot trigger zone at bottom', idx_s14)
if idx_s14_end == -1:
    idx_s14_end = code.find('<!-- macOS Style Dock', idx_s14)
if idx_s14_end == -1:
    idx_s14_end = code.find('<!-- DOCK', idx_s14)

s14_original = code[idx_s14:idx_s14_end]

s14_redesigned = """<!-- SLIDE 14: CIERRE & AGRADECIMIENTO (ESTÉTICO, INSTITUCIONAL Y COMPACTO) -->
    <div class="slide" id="slide-14" data-topic="14 · Cierre y Agradecimiento">
      
      <!-- Top Hero Header -->
      <div class="card-dark" style="margin-bottom: 18px; position: relative; overflow: hidden; padding: 32px 36px; text-align: center;">
        <div style="position: absolute; right: -30px; top: -30px; opacity: 0.06; pointer-events: none;">
          <svg width="280" height="280" viewBox="0 0 200 200" fill="none">
            <circle cx="100" cy="100" r="90" stroke="#2F6BFF" stroke-width="12"/>
            <path d="M40 100 L85 145 L160 65" stroke="#2F6BFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <div class="breadcrumb-tag" style="display: inline-flex; margin-bottom: 10px;">
          {svg_check} Defensa Oral Finalizada &bull; Trabajo Práctico Integrador
        </div>
        <h1 class="giant-title" style="margin-bottom: 8px; font-size: 56px; letter-spacing: -0.02em;">¡Muchas Gracias!</h1>
        <p class="editorial-subtitle" style="max-width: 720px; margin: 0 auto 18px auto; font-size: 15px;">
          Sistema de Gestión y Vigilancia Museológica &bull; Museo de Historia Natural
        </p>

        <div style="display: flex; justify-content: center; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="goToSlide(1)" style="min-height: 44px; padding: 0 22px; font-size: 13.5px;">
            Volver al inicio ↺
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()" style="min-height: 44px; padding: 0 20px; font-size: 13.5px;">
            {svg_grid} Ver los 14 slides
          </button>
        </div>
      </div>

      <!-- Main Split: Institutional & Professors (Left) vs Compact Team Members (Right) -->
      <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 18px;">
        
        <!-- Columna Izquierda: Cátedra, Comisión y Docentes -->
        <div class="card-dark" style="padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 14px;">
              <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(45, 127, 249, 0.15); border: 1px solid rgba(45, 127, 249, 0.35); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                  <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
                </svg>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.06em;">Marco Académico</div>
                <div style="font-size: 16px; font-weight: 800; color: #FFFFFF;">UTN &bull; Facultad Regional Córdoba</div>
                <div style="font-size: 12px; color: var(--text-light-secondary);">Ingeniería en Sistemas de Información</div>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px;">
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px 12px;">
                <span style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; display: block;">Cátedra</span>
                <strong style="font-size: 13.5px; color: #FFF;">Análisis de Sistemas (ASI)</strong>
              </div>
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px 12px;">
                <span style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; display: block;">Comisión y Ciclo</span>
                <strong style="font-size: 13.5px; color: #FFF;">Curso 2K10 &bull; Año 2026</strong>
              </div>
            </div>

            <!-- Docentes Evaluadores -->
            <div>
              <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">
                Equipo Docente Evaluador:
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid var(--blue-accent);">
                  Ing. Cattaneo, Marcela F.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #60A5FA;">
                  Ing. Turanzas, Susana B.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #38BDF8;">
                  Ing. Sanchez, Claudia E.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #818CF8;">
                  Padilla, Tomas Lautaro
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 14px; padding: 10px 14px; background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; font-size: 12px; color: #93C5FD;">
            🎓 <em>Agradecemos a la cátedra por el acompañamiento y las devoluciones formativas durante el ciclo lectivo.</em>
          </div>
        </div>

        <!-- Columna Derecha: 9 Integrantes (Compacto, Prolijo y Elegante) -->
        <div class="card-dark" style="padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                  <circle cx="9" cy="7" r="4"/>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
                <span style="font-size: 15px; font-weight: 800; color: #FFFFFF;">Equipo de Trabajo &bull; Grupo 6</span>
              </div>
              <span style="font-size: 11px; font-weight: 800; background: rgba(45, 127, 249, 0.2); color: #93C5FD; border: 1px solid rgba(45, 127, 249, 0.35); padding: 3px 10px; border-radius: 12px;">
                9 Integrantes
              </span>
            </div>

            <!-- 3x3 Compact Member Grid -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
              
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Tarditti, Juan S.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 400212</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Thomas Rapp, F.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 408990</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Abad, Francisco</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 423269</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Molina, Tobias</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419749</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Moyano, Lucas U.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 410975</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Pereyra, Kevin</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 418201</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Marcuzzi, Tomas</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 403382</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Cufre, Agustín</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419166</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Jastrzebski, E.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 402760</div>
              </div>

            </div>
          </div>

          <div style="margin-top: 14px; padding: 10px 14px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; text-align: center; font-size: 12px; color: var(--text-light-secondary);">
            Quedamos a total disposición de la mesa evaluadora para responder a sus preguntas.
          </div>
        </div>

      </div>
    </div>\n\n    """

code = code[:idx_s14] + s14_redesigned + code[idx_s14_end:]
print("Slide 14 redesigned successfully!")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_v8_deck.py updated with all polish changes!")
