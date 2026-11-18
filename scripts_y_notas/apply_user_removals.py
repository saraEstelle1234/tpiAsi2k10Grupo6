# -*- coding: utf-8 -*-
"""
apply_user_removals.py
Reverts:
1. Slide 11: Removes tablet hotspots, badges, dashed borders and hover interactions.
   Keeps the clean, high-definition tablet mockup and the 3 concise step cards.
2. Global UI: Removes the floating "⌨ Atajos" pill button and the shortcuts modal.
"""

import re

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# -------------------------------------------------------------------------
# 1. CLEAN SLIDE 11 (REVERT TO CRISP, CLEAN TABLET MOCKUP)
# -------------------------------------------------------------------------
old_s11_full = '''<!-- SLIDE 11: PROTOTIPO DE PANTALLA CON HOTSPOTS INTERACTIVOS -->
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
    </div>'''

clean_s11 = '''<!-- SLIDE 11: PROTOTIPO DE PANTALLA (CLEAN MOCKUP) -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo UI</div>
      <h1 class="giant-title">Prototipo de Interfaz</h1>
      <p class="editorial-subtitle">
        Interfaz táctil para tablet de guardia y correspondencia con la plantilla (Sección 2.8 y 2.9 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; align-items: center;">
        <div class="diagram-frame-clean frame-proto-canvas reveal-item revealed">
          <img src="{b64_proto}" class="diagram-preview-img" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')" alt="Prototipo Tablet">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Pantalla Táctil &bull; Tablet de Guardia</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
              Ampliar pantalla {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">1. Búsqueda y Validación (Pasos 2 a 4)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Campo numérico para ingresar el código de la pieza y visualización inmediata del nombre, sala y ubicación física.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">2. Tipificación del Siniestro (Pasos 7 y 8)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Selector desplegable con los tipos reglamentarios (Deterioro provocado, Caída accidental, Deterioro natural) y caja de texto para observaciones.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #38BDF8; text-transform: uppercase; margin-bottom: 6px;">3. Confirmación y Registro (Pasos 9 a 12)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El sistema solicita confirmación del incidente, el guardia confirma y la obra pasa a estado 'Inactivo' con registro de hora del servidor.
            </div>
          </div>
        </div>
      </div>
    </div>'''

if old_s11_full in code:
    code = code.replace(old_s11_full, clean_s11)
    print("Replaced Slide 11 with clean mockup.")
else:
    print("WARNING: old_s11_full exact match not found!")

# -------------------------------------------------------------------------
# 2. REMOVE SHORTCUTS PILL BUTTON & MODAL MARKUP
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
  </div>'''

if shortcuts_markup in code:
    code = code.replace(shortcuts_markup, '')
    print("Removed shortcuts button and modal markup.")
else:
    print("WARNING: shortcuts_markup exact match not found!")

# -------------------------------------------------------------------------
# 3. REMOVE JS FUNCTIONS FOR HOTSPOTS AND SHORTCUTS MODAL
# -------------------------------------------------------------------------
js_to_remove = '''    // ========================================================
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
    }}'''

if js_to_remove in code:
    code = code.replace(js_to_remove, '')
    print("Removed JS functions for hotspots and shortcuts modal.")
else:
    print("WARNING: js_to_remove exact match not found!")

# Clean keydown listener
code = code.replace(
    "if (e.key === '?' || e.key === 'h' || e.key === 'H') { openShortcutsModal(); return; }\n      if (e.key === 'Escape') { closeShortcutsModal();",
    "if (e.key === 'Escape') {"
)

# -------------------------------------------------------------------------
# 4. REMOVE CSS FOR HOTSPOTS AND SHORTCUTS
# -------------------------------------------------------------------------
css_hotspots_pattern = r'    /\* --- IDEA 1: TABLET HOTSPOTS \(SLIDE 11\) ---\s*\*/.*?/\* --- IDEA 2: TRACE PIPELINE'
code = re.sub(css_hotspots_pattern, '    /* --- IDEA 2: TRACE PIPELINE', code, flags=re.DOTALL)

css_shortcuts_pattern = r'    /\* --- IDEA 4: SHORTCUTS PILL & 3D KEYCAPS ---\s*\*/.*?</style>'
code = re.sub(css_shortcuts_pattern, '</style>', code, flags=re.DOTALL)
print("Removed CSS for hotspots and shortcuts.")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate_v8_deck.py successfully!")
