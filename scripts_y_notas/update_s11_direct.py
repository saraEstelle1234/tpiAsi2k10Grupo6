# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_s11 = '''<!-- SLIDE 11: PROTOTIPO DE PANTALLA -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo UI</div>
      <h1 class="giant-title">Prototipo de Interfaz</h1>
      <p class="editorial-subtitle">
        Interfaz táctil para tablet de guardia y correspondencia con la plantilla (Sección 2.8 del TPI)
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

new_s11 = '''<!-- SLIDE 11: PROTOTIPO DE PANTALLA CON HOTSPOTS INTERACTIVOS -->
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

if old_s11 in text:
    text = text.replace(old_s11, new_s11)
    print("Replaced old_s11 with new_s11!")
else:
    print("WARNING: old_s11 exact match not found!")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated generate_v8_deck.py.")
