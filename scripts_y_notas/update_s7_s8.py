# -*- coding: utf-8 -*-
"""
update_s7_s8.py
Applies exact corrections requested:
1. Slide 7:
   - Split 15 RF groups into 2 independent flex columns (Column 1: 8 groups, Column 2: 7 groups)
   - Exclusive accordion behavior: when any group opens, ONLY that group opens; all others close
   - Independent columns ensure the opposite column NEVER stretches empty
2. Slide 8:
   - ONLY 2 RNFs from Section 2.4 of the TPI (RNF 1 and RNF 2). Zero invented RNFs!
   - 2 large, beautiful editorial cards with exact TPI wording and technical breakdown
3. JavaScript:
   - setupExclusiveAccordion() to guarantee single-open behavior on click
   - filterRequirements() and expand/collapse handling
"""

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    deck_code = f.read()

# 1. New Slide 7 & Slide 8 replacement code
new_s7_s8 = """<!-- SLIDE 7: REQUERIMIENTOS FUNCIONALES -->
    <div class="slide" id="slide-7" data-topic="07 · Requerimientos Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">07 &bull; Especificación de Requerimientos</div>
          <h1 class="giant-title">Requerimientos Funcionales</h1>
          <p class="editorial-subtitle">
            Catálogo estructurado por paquetes funcionales del sistema (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="display: flex; gap: 10px; align-items: center; padding-top: 10px;">
          <button class="btn-secondary" onclick="expandAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Expandir todos
          </button>
          <button class="btn-secondary" onclick="collapseAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Colapsar todos
          </button>
        </div>
      </div>

      <div style="margin-bottom: 14px;">
        <input type="text" id="rf-search-input" class="search-input" placeholder="🔍 Filtrar requerimientos por palabra clave (ej: obra, sala, incidente, ronda, informe)..." oninput="filterRequirements()" style="width: 100%; height: 46px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0 18px; color: #FFF; font-size: 14px;">
      </div>

      <!-- 15 Global Bold Categories from TPI in 2 Independent Separate Columns -->
      <div id="rf-accordion-list" style="display: flex; gap: 18px; max-height: 520px; overflow-y: auto; padding-right: 6px; align-items: flex-start;">
        
        <!-- Columna Izquierda (Grupos 1 a 8) -->
        <div class="rf-col" id="rf-col-left" style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
          
          <!-- 1. Administrar Obras de Arte -->
          <details class="rf-group" open>
            <summary class="rf-summary">
              <span>Administrar Obras de Arte <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 1.</span> Registrar ingreso de obra</div>
              <div class="rf-item"><span class="rf-num">RF 2.</span> Consultar obra</div>
              <div class="rf-item"><span class="rf-num">RF 3.</span> Registrar baja de obra</div>
            </div>
          </details>

          <!-- 2. Administrar Tipos de Obra -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Tipos de Obra <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 4.</span> Registrar tipo de obra</div>
              <div class="rf-item"><span class="rf-num">RF 5.</span> Consultar tipo de obra</div>
              <div class="rf-item"><span class="rf-num">RF 6.</span> Registrar baja de tipo de obra</div>
            </div>
          </details>

          <!-- 3. Administrar Tipos de Material -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Tipos de Material <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 7.</span> Registrar tipo de material</div>
              <div class="rf-item"><span class="rf-num">RF 8.</span> Consultar tipo de material</div>
              <div class="rf-item"><span class="rf-num">RF 9.</span> Registrar baja de tipo de material</div>
            </div>
          </details>

          <!-- 4. Administrar Salas -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Salas <span class="rf-badge">4 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 10.</span> Registrar sala</div>
              <div class="rf-item"><span class="rf-num">RF 11.</span> Consultar sala</div>
              <div class="rf-item"><span class="rf-num">RF 12.</span> Modificar sala</div>
              <div class="rf-item"><span class="rf-num">RF 13.</span> Registrar baja de sala</div>
            </div>
          </details>

          <!-- 5. Administrar Guías -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Guías <span class="rf-badge">4 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 14.</span> Registrar guía</div>
              <div class="rf-item"><span class="rf-num">RF 15.</span> Consultar guía</div>
              <div class="rf-item"><span class="rf-num">RF 16.</span> Registrar modificación de guía</div>
              <div class="rf-item"><span class="rf-num">RF 17.</span> Registrar baja de guía</div>
            </div>
          </details>

          <!-- 6. Administrar Estilos de Obra -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Estilos de Obra <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 18.</span> Registrar estilo de obra</div>
              <div class="rf-item"><span class="rf-num">RF 19.</span> Consultar estilo de obra</div>
              <div class="rf-item"><span class="rf-num">RF 20.</span> Registrar baja de estilo de obra</div>
            </div>
          </details>

          <!-- 7. Administrar Tipos de Incidentes -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Tipos de Incidentes <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 21.</span> Registrar tipo de incidente</div>
              <div class="rf-item"><span class="rf-num">RF 22.</span> Consultar tipo de incidente</div>
              <div class="rf-item"><span class="rf-num">RF 23.</span> Registrar baja de tipo de incidente</div>
            </div>
          </details>

          <!-- 8. Gestionar Exposiciones -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Exposiciones <span class="rf-badge">2 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 24.</span> Registrar programación de exposiciones</div>
              <div class="rf-item"><span class="rf-num">RF 25.</span> Consultar programación de exposiciones</div>
            </div>
          </details>

        </div>

        <!-- Columna Derecha (Grupos 9 a 15) -->
        <div class="rf-col" id="rf-col-right" style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
          
          <!-- 9. Gestionar Visitas Guiadas -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Visitas Guiadas <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 26.</span> Registrar planificación de visitas guiadas</div>
              <div class="rf-item"><span class="rf-num">RF 27.</span> Consultar planificación de visitas guiadas</div>
              <div class="rf-item"><span class="rf-num">RF 28.</span> Consultar agenda de guías</div>
            </div>
          </details>

          <!-- 10. Gestionar Venta de Entradas -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Venta de Entradas <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 29.</span> Registrar venta de entrada</div>
              <div class="rf-item"><span class="rf-num">RF 30.</span> Registrar contratación de servicio adicional de guía</div>
              <div class="rf-item"><span class="rf-num">RF 31.</span> Consultar venta de entrada</div>
            </div>
          </details>

          <!-- 11. Gestionar Planificación y Rondas de Vigilancia -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Planificación y Rondas <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 32.</span> Generar planificación de rondas de vigilancia</div>
              <div class="rf-item"><span class="rf-num">RF 33.</span> Consultar planificación de rondas de vigilancia</div>
              <div class="rf-item"><span class="rf-num">RF 34.</span> Registrar revisión de sala</div>
            </div>
          </details>

          <!-- 12. Gestionar Incidentes -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Incidentes <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 35.</span> Registrar incidente (CU-15)</div>
              <div class="rf-item"><span class="rf-num">RF 36.</span> Consultar incidentes</div>
              <div class="rf-item"><span class="rf-num">RF 37.</span> Registrar seguimiento de resolución de incidente</div>
            </div>
          </details>

          <!-- 13. Gestionar Restauración -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Restauración <span class="rf-badge">2 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 40.</span> Registrar obra a restaurar</div>
              <div class="rf-item"><span class="rf-num">RF 41.</span> Registrar reingreso de obra</div>
            </div>
          </details>

          <!-- 14. Generar Informes y Reportes -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Generar Informes y Reportes <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 42.</span> Generar informe diario de vigilancia</div>
              <div class="rf-item"><span class="rf-num">RF 43.</span> Generar reporte de patrones de incidentes</div>
              <div class="rf-item"><span class="rf-num">RF 44.</span> Emitir historial de incidentes</div>
            </div>
          </details>

          <!-- 15. Administrar Sesión -->
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Administrar Sesión <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 45.</span> Iniciar sesión</div>
              <div class="rf-item"><span class="rf-num">RF 46.</span> Cerrar sesión</div>
              <div class="rf-item"><span class="rf-num">RF 47.</span> Modificar contraseña</div>
            </div>
          </details>

        </div>

      </div>
    </div>

    <!-- SLIDE 8: REQUERIMIENTOS NO FUNCIONALES (ESTRICTAMENTE 2 SEGÚN TPI) -->
    <div class="slide" id="slide-8" data-topic="08 · Requerimientos No Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px;">
        <div>
          <div class="breadcrumb-tag">08 &bull; Restricciones de Calidad y Arquitectura</div>
          <h1 class="giant-title">Requerimientos No Funcionales</h1>
          <p class="editorial-subtitle">
            Criterios de arquitectura técnica y soporte operativo especificados formalmente en la Sección 2.4 del TPI
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 6px;">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
      </div>

      <!-- 2 Clean, Generous Editorial Cards Side-by-Side (Exactly 2 RNFs from TPI) -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 20px;">
        
        <!-- RNF 1: Módulo Web de Soporte -->
        <div class="card-dark reveal-item revealed" style="border-top: 4px solid var(--blue-accent); padding: 32px 28px; background: rgba(14, 31, 58, 0.75); border-radius: 14px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #93C5FD; background: rgba(45, 127, 249, 0.16); border: 1px solid rgba(45, 127, 249, 0.32); padding: 5px 12px; border-radius: 6px; text-transform: uppercase;">
                Arquitectura &bull; Acceso Web Ubicuo
              </span>
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>

            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.01em;">
              RNF 1 &bull; Módulo Web de Soporte
            </div>

            <div style="font-size: 15px; line-height: 1.7; color: #F1F5F9; background: rgba(255,255,255,0.04); border-left: 3px solid #2D7FF9; padding: 18px 20px; border-radius: 0 10px 10px 0; margin-bottom: 22px;">
              "El sistema deberá implementarse bajo una <strong>arquitectura web cliente-servidor</strong> accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo."
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 18px;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Arquitectura Web Cliente-Servidor:</strong> Servicios centralizados y persistencia relacional.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Navegadores Modernos:</strong> Acceso universal sin dependencias de plugins o runtime local.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Zero-Install:</strong> Mantenimiento centralizado con cero sobrecarga en terminales del museo.</span>
            </div>
          </div>
        </div>

        <!-- RNF 2: Interfaz móvil para rondas -->
        <div class="card-dark reveal-item revealed" style="border-top: 4px solid #38BDF8; padding: 32px 28px; background: rgba(14, 31, 58, 0.75); border-radius: 14px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #38BDF8; background: rgba(56, 189, 248, 0.16); border: 1px solid rgba(56, 189, 248, 0.32); padding: 5px 12px; border-radius: 6px; text-transform: uppercase;">
                Usabilidad &bull; Terminal Táctil para Guardias
              </span>
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="2" width="16" height="20" rx="2" ry="2"/>
                <line x1="12" y1="18" x2="12.01" y2="18"/>
              </svg>
            </div>

            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.01em;">
              RNF 2 &bull; Interfaz móvil para rondas
            </div>

            <div style="font-size: 15px; line-height: 1.7; color: #F1F5F9; background: rgba(255,255,255,0.04); border-left: 3px solid #38BDF8; padding: 18px 20px; border-radius: 0 10px 10px 0; margin-bottom: 22px;">
              "La aplicación deberá contar con una <strong>interfaz responsiva y táctil adaptada para tablets</strong>, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia."
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 18px;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Interfaz Táctil en Tablet:</strong> Ergonomía y botones de alto contraste para rondas en movimiento.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #38BDF8; font-weight: bold; font-size: 14px;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Plano Interactivo:</strong> Navegación espacial de salas para selección y verificación visual in situ.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #38BDF8; font-weight: bold; font-size: 14px;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Reporte Inmediato:</strong> Registro en caliente que alimenta al instante la base de datos (RN-2).</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Reference Bar -->
      <div style="padding: 14px 22px; background: rgba(14, 31, 58, 0.55); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          <span style="font-size: 13px; color: #94A3B8;">
            <strong style="color: #60A5FA;">Fidelidad al TPI:</strong> La Sección 2.4 define formalmente estos dos requerimientos no funcionales como condicionantes rectores de despliegue y usabilidad.
          </span>
        </div>
        <span style="font-size: 11px; font-weight: 700; color: #93C5FD; background: rgba(45, 127, 249, 0.15); border: 1px solid rgba(45, 127, 249, 0.3); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">
          Sección 2.4 &bull; 2 RNFs Formales
        </span>
      </div>

    </div>
"""

# Replace in deck_code
idx_s7 = deck_code.find('<!-- SLIDE 7: REQUERIMIENTOS FUNCIONALES -->')
idx_s9 = deck_code.find('<!-- SLIDE 9: DCU GENERAL')

assert idx_s7 != -1 and idx_s9 != -1, "Could not find s7/s9 markers in generate_v8_deck.py"

updated_deck = deck_code[:idx_s7] + new_s7_s8 + "\n    " + deck_code[idx_s9:]

# 2. Update JavaScript in deck_code for Accordion behavior
# Let's inspect where JS functions are
old_js_rf = """function expandAllRf() {
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = true);
    }

    function collapseAllRf() {
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = false);
    }

    function filterRequirements() {
      const query = document.getElementById('rf-search-input').value.toLowerCase();
      const groups = document.querySelectorAll('#rf-accordion-list .rf-group');
      groups.forEach(g => {
        const text = g.innerText.toLowerCase();
        if (text.includes(query)) {
          g.style.display = 'block';
          if (query.length > 1) g.open = true;
        } else {
          g.style.display = 'none';
        }
      });
    }"""

# In generate_v8_deck.py, braces are doubled {{ }} because it's inside an f-string
old_js_rf_doubled = """function expandAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = true);
    }}

    function collapseAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = false);
    }}

    function filterRequirements() {{
      const query = document.getElementById('rf-search-input').value.toLowerCase();
      const groups = document.querySelectorAll('#rf-accordion-list .rf-group');
      groups.forEach(g => {{
        const text = g.innerText.toLowerCase();
        if (text.includes(query)) {{
          g.style.display = 'block';
          if (query.length > 1) g.open = true;
        }} else {{
          g.style.display = 'none';
        }}
      }});
    }}"""

new_js_rf_doubled = """let rfExclusiveMode = true;

    function initExclusiveAccordion() {{
      const allGroups = document.querySelectorAll('.rf-group');
      allGroups.forEach(group => {{
        const summary = group.querySelector('.rf-summary');
        if (!summary) return;
        summary.addEventListener('click', function(e) {{
          if (!rfExclusiveMode) return;
          // If group is currently closed, opening it will close all others
          const willOpen = !group.open;
          if (willOpen) {{
            allGroups.forEach(other => {{
              if (other !== group) other.open = false;
            }});
          }}
        }});
      }});
    }}

    function expandAllRf() {{
      rfExclusiveMode = false;
      document.querySelectorAll('.rf-group').forEach(g => {{
        g.style.display = 'block';
        g.open = true;
      }});
      setTimeout(() => {{ rfExclusiveMode = true; }}, 300);
    }}

    function collapseAllRf() {{
      document.querySelectorAll('.rf-group').forEach(g => {{
        g.open = false;
      }});
    }}

    function filterRequirements() {{
      const query = document.getElementById('rf-search-input').value.toLowerCase().trim();
      const groups = document.querySelectorAll('.rf-group');
      if (!query) {{
        groups.forEach(g => {{
          g.style.display = 'block';
        }});
        return;
      }}
      rfExclusiveMode = false;
      groups.forEach(g => {{
        const text = g.innerText.toLowerCase();
        if (text.includes(query)) {{
          g.style.display = 'block';
          g.open = true;
        }} else {{
          g.style.display = 'none';
          g.open = false;
        }}
      }});
      setTimeout(() => {{ rfExclusiveMode = true; }}, 300);
    }}"""

if old_js_rf_doubled in updated_deck:
    updated_deck = updated_deck.replace(old_js_rf_doubled, new_js_rf_doubled)
    print("Replaced JS functions with doubled braces successfully!")
else:
    print("WARNING: Could not find exact doubled JS block, searching...")
    # Find definition of expandAllRf
    idx_exp = updated_deck.find('function expandAllRf')
    print("expandAllRf index:", idx_exp)

# Also ensure initExclusiveAccordion() is called when DOM loads or document is ready
init_call = "initExclusiveAccordion();"
if init_call not in updated_deck:
    # Find DOMContentLoaded or init call
    idx_dom = updated_deck.find('initTraceMatrix();')
    if idx_dom != -1:
        updated_deck = updated_deck.replace('initTraceMatrix();', 'initTraceMatrix();\n      initExclusiveAccordion();')
        print("Hooked initExclusiveAccordion() into initTraceMatrix()!")
    else:
        # Check window.addEventListener('DOMContentLoaded'
        idx_load = updated_deck.find("window.addEventListener('DOMContentLoaded'")
        if idx_load != -1:
            updated_deck = updated_deck.replace("window.addEventListener('DOMContentLoaded', () => {",
                                                "window.addEventListener('DOMContentLoaded', () => {\n      initExclusiveAccordion();")
            print("Hooked initExclusiveAccordion() into DOMContentLoaded!")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(updated_deck)

print("Updated generate_v8_deck.py successfully!")
