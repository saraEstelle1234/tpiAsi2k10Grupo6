# -*- coding: utf-8 -*-
"""
apply_flawless_fit.py
Elimina cualquier recorte de imagen en Slide 06 (BPMN), Slide 09 (DCU) y Slide 12 (DCD):
- Utiliza max-width: 100%; max-height: 100%; object-fit: contain en las 3 imágenes.
- En scale(1), la imagen completa se ve 100% entera sin NINGÚN corte arriba, abajo o a los lados.
- Aplica los transforms de zoom directamente a cada <img> para máxima fidelidad de traslación.
"""

import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original length:", len(html))

# ==============================================================================
# 1. SLIDE 06: BPMN Operativo (Uncropped, Full view in scale(1))
# ==============================================================================
idx_s6 = html.find('id="slide-6"')
idx_s6_end = html.find('id="slide-7"')
s6_chunk = html[idx_s6:idx_s6_end]

# Find diagram frame in s6
old_s6_frame_start = s6_chunk.find('<div class="diagram-frame-clean')
idx_s6_img = s6_chunk.find('class="diagram-preview-img"', old_s6_frame_start)
if idx_s6_img == -1:
    idx_s6_img = s6_chunk.find('b64_bpmn_oper', old_s6_frame_start)

# Clean up s6 diagram container:
# Replace from old_s6_frame_start up to <img ... src="data:image/png;base64,...
idx_img_src = s6_chunk.find('src="data:image/png;base64,', old_s6_frame_start)
idx_img_close = s6_chunk.find('>', idx_img_src)
idx_act_bar = s6_chunk.find('<div class="diagram-action-bar"', idx_img_close)

# Extract b64 src
src_start = s6_chunk.find('data:image/png;base64,', old_s6_frame_start)
src_end = s6_chunk.find('"', src_start)
b64_bpmn_src = s6_chunk[src_start:src_end]

new_s6_frame = f"""<div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: clamp(380px, 54vh, 580px); display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
          <div class="cinematic-viewport frame-white-canvas" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; background: #FFFFFF; display: flex; align-items: center; justify-content: center;">
            <img id="bpmn-img" src="{b64_bpmn_src}" style="max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block; cursor: zoom-in;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')" alt="BPMN Nivel 2 Corregido">
          </div>
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida (1682 &times; 798 px)</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')">
              Ampliar <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
            </button>
          </div>
        </div>"""

idx_card_after = s6_chunk.find('<!-- Card dinámico explicativo del paso activo -->', old_s6_frame_start)
if idx_card_after == -1:
    idx_card_after = s6_chunk.find('<div class="tour-step-card"', old_s6_frame_start)

s6_chunk = s6_chunk[:old_s6_frame_start] + new_s6_frame + '\n\n        ' + s6_chunk[idx_card_after:]
html = html[:idx_s6] + s6_chunk + html[idx_s6_end:]
print("Slide 06 perfectly restructured!")

# ==============================================================================
# 2. SLIDE 09: Casos de Uso (Uncropped, Full view in scale(1), Large 1fr 320px)
# ==============================================================================
idx_s9 = html.find('id="slide-9"')
idx_s9_end = html.find('id="slide-10"')
s9_chunk = html[idx_s9:idx_s9_end]

src_start_dcu = s9_chunk.find('data:image/png;base64,')
src_end_dcu = s9_chunk.find('"', src_start_dcu)
b64_dcu_src = s9_chunk[src_start_dcu:src_end_dcu]

# Find diagram frame in s9
idx_s9_df = s9_chunk.find('<div class="card-dark reveal-item revealed"')
idx_s9_right_col = s9_chunk.find('<!-- Columna Derecha')

new_s9_diagram_box = f"""<div class="card-dark reveal-item revealed" style="height: clamp(480px, 68vh, 720px); padding: 10px; display: flex; flex-direction: column; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); background: #0A1128;">
            <div class="cinematic-viewport dark-bg" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: #060B14;">
              <img id="dcu-img" src="{b64_dcu_src}" style="max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block; cursor: zoom-in;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
              <span style="font-size: 12px; font-weight: 600; color: #CBD5E1;">42 CUs &bull; Clic para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 34px; padding: 0 14px; font-size: 12px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
              </button>
            </div>
          </div>

          <!-- Card dinámico explicativo del Actor y CUs activos -->
          <div class="tour-step-card" id="dcu-tour-card" style="margin-top: 10px; margin-bottom: 0;">
            <div class="tour-step-tag" id="dcu-tour-tag">VISTA COMPLETA</div>
            <div class="tour-step-title" id="dcu-tour-title" style="font-size: 13px;">Vista Panorámica de los 42 Casos de Uso</div>
            <div class="tour-step-desc" id="dcu-tour-desc" style="font-size: 12px;">Estructura completa de casos de uso numerados del 1 al 42, organizados según los actores del museo.</div>
          </div>
        </div>

        """

# Replace in s9
idx_s9_col_start = s9_chunk.find('<div style="display: flex; flex-direction: column;">')
if idx_s9_col_start != -1 and idx_s9_right_col != -1:
    s9_chunk = s9_chunk[:idx_s9_col_start + len('<div style="display: flex; flex-direction: column;">')] + '\n          ' + s9_chunk[s9_chunk.find('<div class="guided-tour-bar" id="dcu-tour-bar"'):s9_chunk.find('</div>', s9_chunk.find('<div class="guided-tour-bar" id="dcu-tour-bar"')) + len('</div>')] + '\n\n          ' + new_s9_diagram_box + s9_chunk[idx_s9_right_col:]
    print("Slide 09 cleanly restructured without any inner wrapping bugs!")

html = html[:idx_s9] + s9_chunk + html[idx_s9_end:]

# ==============================================================================
# 3. SLIDE 12: Clases DCD (Uncropped, Full view in scale(1))
# ==============================================================================
idx_s12 = html.find('id="slide-12"')
idx_s12_end = html.find('id="slide-13"')
s12_chunk = html[idx_s12:idx_s12_end]

src_start_dcd = s12_chunk.find('data:image/png;base64,')
src_end_dcd = s12_chunk.find('"', src_start_dcd)
b64_dcd_src = s12_chunk[src_start_dcd:src_end_dcd]

# Clean up s12 diagram frame
idx_s12_df = s12_chunk.find('<div class="diagram-frame-clean')
idx_s12_right_col = s12_chunk.find('<!-- Columna Derecha')

new_s12_diagram_box = f"""<div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: clamp(480px, 68vh, 720px); display: flex; flex-direction: column; padding: 10px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); background: #0A1128;">
          <div class="cinematic-viewport dark-bg" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: #121212;">
            <img id="dcd-img" src="{b64_dcd_src}" style="max-width: 100%; max-height: 100%; width: auto; height: auto; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
          </div>
          <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
            <span style="font-size: 12px; font-weight: 600; color: #CBD5E1;">12 Clases del Dominio &bull; Clic para zoom interactivo</span>
            <button class="btn-primary" style="min-height: 34px; padding: 0 14px; font-size: 12px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
              Ampliar <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
            </button>
          </div>
        </div>

        """

s12_chunk = s12_chunk[:idx_s12_df] + new_s12_diagram_box + s12_chunk[idx_s12_right_col:]
html = html[:idx_s12] + s12_chunk + html[idx_s12_end:]
print("Slide 12 cleanly restructured!")

# ==============================================================================
# 4. JS FUNCTIONS UPDATE: Directly target img elements
# ==============================================================================
# Ensure setBpmnTour targets document.getElementById('bpmn-img')
js_set_bpmn = """    function setBpmnTour(stepIdx, btn) {
      document.querySelectorAll('#bpmn-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('bpmn-img');
      const data = BPMN_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('bpmn-tour-tag');
        const titleEl = document.getElementById('bpmn-tour-title');
        const descEl = document.getElementById('bpmn-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }"""
html = re.sub(r'function setBpmnTour\(stepIdx, btn\) \{.*?\}', js_set_bpmn, html, flags=re.DOTALL)

# Ensure setDcuSector targets document.getElementById('dcu-img')
js_set_dcu = """    function setDcuSector(sector, btn) {
      const img = document.getElementById('dcu-img');
      if (!img) return;
      if (btn) {
        const btns = btn.parentElement.querySelectorAll('.tour-btn, .preset-btn');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }
      
      const key = (sector === 'guardia') ? 'vigilancia' : ((sector === 'supervisor') ? 'supervision' : sector);
      const data = DCU_ACTOR_STEPS[key] || DCU_ACTOR_STEPS['all'];
      
      img.style.transform = data.transform;
      const tagEl = document.getElementById('dcu-tour-tag');
      const titleEl = document.getElementById('dcu-tour-title');
      const descEl = document.getElementById('dcu-tour-desc');
      if (tagEl) tagEl.innerText = data.tag;
      if (titleEl) titleEl.innerText = data.title;
      if (descEl) descEl.innerText = data.desc;
    }"""
html = re.sub(r'function setDcuSector\(sector, btn\) \{.*?\}', js_set_dcu, html, flags=re.DOTALL)

# Ensure setDcdTour targets document.getElementById('dcd-img')
js_set_dcd = """    function setDcdTour(stepIdx, btn) {
      document.querySelectorAll('#dcd-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('dcd-img');
      const data = DCD_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('dcd-tour-tag');
        const titleEl = document.getElementById('dcd-tour-title');
        const descEl = document.getElementById('dcd-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }"""
html = re.sub(r'function setDcdTour\(stepIdx, btn\) \{.*?\}', js_set_dcd, html, flags=re.DOTALL)

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Synchronized presentacion.html and index.html with flawless fit!")
