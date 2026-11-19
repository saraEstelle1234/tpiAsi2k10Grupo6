# -*- coding: utf-8 -*-
"""
fix_all_user_requests.py
Implementa las 4 correcciones solicitadas por el usuario:
1. Elimina el texto filtrado y 'CTYPE html>' al inicio del archivo HTML.
2. Elimina todos los cartelitos 'Expone: ...' de los breadcrumbs de todas las slides.
3. Sectoriza por ACTOR el Diagrama de Casos de Uso (Slide 09) con coordenadas y zoom exactos por cámara 2D.
4. Ajusta y calibra los sectores del Diagrama de Clases DCD (Slide 12) con precisión milimétrica en Incidente, Sala, Obra y Multiplicidades Corregidas.
"""

import re
import json

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original length:", len(html))

# -------------------------------------------------------------
# 1. FIX TOP OF FILE: Remove leaked card and CTYPE html>
# -------------------------------------------------------------
idx_doctype = html.find('<!DOCTYPE html>')
if idx_doctype != 0:
    # Check if there is corrupted text before <html
    idx_html_tag = html.find('<html lang="es">')
    if idx_html_tag != -1:
        html = '<!DOCTYPE html>\n' + html[idx_html_tag:]
        print("Fixed top of file! Clean <!DOCTYPE html> restored.")
    else:
        print("Warning: <html lang='es'> not found!")
else:
    print("Top of file was already clean.")

# Double check no stray CTYPE html>
html = re.sub(r'CTYPE html>\s*', '', html)

# -------------------------------------------------------------
# 2. REMOVE ALL "Expone: ..." PILLS FROM SLIDES
# -------------------------------------------------------------
pattern_speaker_pill = r'<span class="speaker-pill"[^>]*>.*?</span>'
matches = re.findall(pattern_speaker_pill, html)
print(f"Found {len(matches)} speaker-pill elements to remove.")
html = re.sub(pattern_speaker_pill, '', html)

# -------------------------------------------------------------
# 3. UPGRADE SLIDE 09: CASOS DE USO BY ACTOR
# -------------------------------------------------------------
# Look for Slide 9 focus bar
old_dcu_bar_pattern = r'<div class="preset-focus-bar"[^>]*>.*?</div>\s*</div>'
# Let's inspect where preset-focus-bar is in Slide 09
idx_s9 = html.find('id="slide-9"')
idx_s9_end = html.find('id="slide-10"')
s9_chunk = html[idx_s9:idx_s9_end]

new_dcu_bar = """<!-- Presets Sectorizados por Actor con Zoom de Cámara Cinematográfica -->
          <div class="guided-tour-bar" id="dcu-tour-bar" style="margin-bottom: 10px;">
            <span class="tour-label">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>
              Sectorizar por Actor:
            </span>
            <button class="tour-btn active" onclick="setDcuSector('all', this)">① Ver Todo (42 CUs)</button>
            <button class="tour-btn" onclick="setDcuSector('vigilancia', this)">② Vigilancia (CU 13-17)</button>
            <button class="tour-btn" onclick="setDcuSector('supervision', this)">③ Supervisión (CU 18-23)</button>
            <button class="tour-btn" onclick="setDcuSector('ingreso', this)">④ Ingreso Obras (CU 1-4)</button>
            <button class="tour-btn" onclick="setDcuSector('atencion', this)">⑤ Atención & Visitas (CU 8-11)</button>
            <button class="tour-btn" onclick="setDcuSector('admin', this)">⑥ Admin Sistema (CU 24-42)</button>
          </div>"""

# Find old preset-focus-bar in s9
idx_bar_start = s9_chunk.find('<div class="preset-focus-bar"')
idx_bar_end = s9_chunk.find('</div>', idx_bar_start) + len('</div>')
if idx_bar_start != -1:
    s9_chunk = s9_chunk[:idx_bar_start] + new_dcu_bar + s9_chunk[idx_bar_end:]
    print("Slide 09 actor tour bar replaced.")
else:
    print("Warning: preset-focus-bar not found in Slide 09!")

# Add dcu-tour-card below the diagram frame in Slide 09
dcu_tour_card_html = """
            <!-- Card dinámico explicativo del Actor y CUs activos -->
            <div class="tour-step-card" id="dcu-tour-card" style="margin-top: 10px; margin-bottom: 0;">
              <div class="tour-step-tag" id="dcu-tour-tag">VISTA COMPLETA</div>
              <div class="tour-step-title" id="dcu-tour-title" style="font-size: 13px;">Vista Panorámica de los 42 Casos de Uso</div>
              <div class="tour-step-desc" id="dcu-tour-desc" style="font-size: 12px;">Estructura completa de casos de uso numerados del 1 al 42, organizados según los actores del museo.</div>
            </div>"""

# Ensure dcu-img has exact transform styling
old_dcu_img_tag = 'id="dcu-img"'
idx_dcu_img = s9_chunk.find(old_dcu_img_tag)
if idx_dcu_img != -1:
    # replace style of dcu-img
    tag_end = s9_chunk.find('>', idx_dcu_img)
    old_tag = s9_chunk[idx_dcu_img-5:tag_end+1] # <img id="dcu-img"...>
    
    # Check if style is inside old_tag
    new_tag = re.sub(r'style="[^"]*"', 'style="max-width: 100%; max-height: 100%; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block;"', old_tag)
    if 'style=' not in new_tag:
        new_tag = new_tag.replace('id="dcu-img"', 'id="dcu-img" style="max-width: 100%; max-height: 100%; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block;"')
    s9_chunk = s9_chunk.replace(old_tag, new_tag)
    print("Slide 09 dcu-img style updated.")

# Insert dcu_tour_card_html right after the diagram action bar or before the closing </div> of left column
idx_act_bar = s9_chunk.find('<div class="diagram-action-bar"')
if idx_act_bar != -1:
    # find closing of diagram-action-bar
    idx_act_bar_end = s9_chunk.find('</div>', idx_act_bar)
    idx_act_bar_end = s9_chunk.find('</div>', idx_act_bar_end + 1) + len('</div>')
    s9_chunk = s9_chunk[:idx_act_bar_end] + dcu_tour_card_html + s9_chunk[idx_act_bar_end:]
    print("Slide 09 dcu-tour-card inserted.")

html = html[:idx_s9] + s9_chunk + html[idx_s9_end:]

# -------------------------------------------------------------
# 4. UPGRADE SLIDE 12: DCD SECTOR TOUR & CARD
# -------------------------------------------------------------
idx_s12 = html.find('id="slide-12"')
idx_s12_end = html.find('id="slide-13"')
s12_chunk = html[idx_s12:idx_s12_end]

# Ensure tour card is properly placed inside Slide 12 right below #dcd-tour-bar
dcd_tour_card_html = """
      <!-- Card dinámico explicativo del foco de Clases activo -->
      <div class="tour-step-card" id="dcd-tour-card" style="margin-bottom: 12px; margin-top: 0;">
        <div class="tour-step-tag" id="dcd-tour-tag">VISTA COMPLETA DCD</div>
        <div class="tour-step-title" id="dcd-tour-title" style="font-size: 13px;">Estructura Completa del Dominio</div>
        <div class="tour-step-desc" id="dcd-tour-desc" style="font-size: 12px;">Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.</div>
      </div>"""

# Remove any existing dcd-tour-card if present in s12_chunk
s12_chunk = re.sub(r'<div class="tour-step-card" id="dcd-tour-card".*?</div>\s*</div>', '', s12_chunk, flags=re.DOTALL)

# Insert right after #dcd-tour-bar
idx_dcd_bar = s12_chunk.find('id="dcd-tour-bar"')
if idx_dcd_bar != -1:
    idx_dcd_bar_end = s12_chunk.find('</div>', idx_dcd_bar) + len('</div>')
    s12_chunk = s12_chunk[:idx_dcd_bar_end] + '\n' + dcd_tour_card_html + s12_chunk[idx_dcd_bar_end:]
    print("Slide 12 dcd-tour-card inserted cleanly after dcd-tour-bar.")

# Ensure dcd-img has exact transform styling
idx_dcd_img = s12_chunk.find('id="dcd-img"')
if idx_dcd_img != -1:
    tag_end = s12_chunk.find('>', idx_dcd_img)
    old_tag = s12_chunk[idx_dcd_img-5:tag_end+1]
    new_tag = re.sub(r'style="[^"]*"', 'style="max-width: 100%; max-height: 100%; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block;"', old_tag)
    if 'style=' not in new_tag:
        new_tag = new_tag.replace('id="dcd-img"', 'id="dcd-img" style="max-width: 100%; max-height: 100%; object-fit: contain; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform; display: block;"')
    s12_chunk = s12_chunk.replace(old_tag, new_tag)
    print("Slide 12 dcd-img style updated.")

html = html[:idx_s12] + s12_chunk + html[idx_s12_end:]

# -------------------------------------------------------------
# 5. JAVASCRIPT: UPDATE setDcuSector, setDcdTour, DCD_TOUR_STEPS
# -------------------------------------------------------------
# Replace DCD_TOUR_STEPS and setDcdTour
js_dcd_new = """
    const DCD_TOUR_STEPS = [
      {
        title: "Vista Completa del Diagrama de Clases",
        desc: "Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.",
        tag: "VISTA COMPLETA DCD",
        transform: "scale(1) translate(0%, 0%)"
      },
      {
        title: "Sector 1: Núcleo Incidente & Sala",
        desc: "La clase Incidente registra fecha, hora y descripción, asociándose a Sala (1). Conoce al guardia de turno a través de la relación histórica SalaXGuardia.",
        tag: "SECTOR 1 · INCIDENTE & SALA",
        transform: "scale(2.1) translate(21%, -2%)"
      },
      {
        title: "Sector 2: Obra, Material y Componentes",
        desc: "Obra encapsula registrarObraInactiva() y registrarObraActiva(), vinculándose con Material (para evaluar sensibilidad física), TipoObra y Autor.",
        tag: "SECTOR 2 · OBRA & MATERIAL",
        transform: "scale(2.0) translate(-13%, 8%)"
      },
      {
        title: "Sector 3: Clase Tipo de Incidente",
        desc: "TipoIncidente tipifica el evento (accidental, provocado o natural), orientando las acciones de mitigación inmediata y contingencia.",
        tag: "SECTOR 3 · TIPO DE INCIDENTE",
        transform: "scale(2.4) translate(32%, 13%)"
      },
      {
        title: "Sector 4: Multiplicidades Críticas Corregidas",
        desc: "Enfoque en las correcciones del docente: Incidente ➔ (1) TipoIncidente (obligatoria) y Sala ➔ (*) SalaXGuardia (historial de asignaciones).",
        tag: "CORRECCIONES CÁTEDRA",
        transform: "scale(2.05) translate(31%, -3%)"
      }
    ];

    function setDcdTour(stepIdx, btn) {
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
    }
"""

# Replace old DCD_TOUR_STEPS & setDcdTour
html = re.sub(r'const DCD_TOUR_STEPS = \[.*?\];\s*function setDcdTour\(.*?\)\s*\{.*?\}\s*\}', js_dcd_new.strip(), html, flags=re.DOTALL)

# Replace setDcuSector
js_dcu_new = """
    const DCU_ACTOR_STEPS = {
      'all': {
        tag: 'VISTA COMPLETA',
        title: 'Vista Panorámica de los 42 Casos de Uso',
        desc: 'Estructura completa de casos de uso numerados del 1 al 42, organizados según los roles y fronteras del software.',
        transform: 'scale(1) translate(0%, 0%)'
      },
      'vigilancia': {
        tag: 'ACTOR PRINCIPAL DEL TPI',
        title: 'Encargado de Vigilancia (CU 13 a 17)',
        desc: 'Realiza rondas en salas, registra revisiones (CU 14) y registra incidentes ante anomalías detectadas (CU 15 - caso central del TPI).',
        transform: 'scale(2.2) translate(30%, -12.5%)'
      },
      'supervision': {
        tag: 'CONTROL Y REPORTES',
        title: 'Encargado de Supervisión (CU 18 a 23)',
        desc: 'Genera patrones de incidentes (CU 18), informes diarios de vigilancia (CU 20) y seguimiento de resolución de obras dañadas (CU 23).',
        transform: 'scale(2.15) translate(32%, -35%)'
      },
      'ingreso': {
        tag: 'CATÁLOGO Y RESTAURACIÓN',
        title: 'Responsable de Ingreso de Obra (CU 1 a 4)',
        desc: 'Registra ingreso/reingreso de obras, consulta catálogo de piezas y deriva obras dañadas a restauración (CU 4).',
        transform: 'scale(2.25) translate(32%, 39%)'
      },
      'atencion': {
        tag: 'OPERACIÓN COMERCIAL & VISITAS',
        title: 'Atención al Cliente & Visitas (CU 8 a 11)',
        desc: 'Registra venta de entradas (CU 9), contratación de guías (CU 10) y consulta agenda de visitas guiadas (CU 11).',
        transform: 'scale(2.1) translate(24%, 6%)'
      },
      'admin': {
        tag: 'DATOS MAESTROS DEL SISTEMA',
        title: 'Admin de Sistema (CU 24 a 42)',
        desc: 'Administra tablas maestras del sistema: salas, materiales, tipos de incidentes, guías, estilos y baja de obras.',
        transform: 'scale(1.95) translate(-20%, 33%)'
      }
    };

    function setDcuSector(sector, btn) {
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
    }
"""

# Replace old setDcuSector
html = re.sub(r'function setDcuSector\(.*?\)\s*\{.*?\}\s*\}', js_dcu_new.strip(), html, flags=re.DOTALL)

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished! presentacion.html and index.html successfully updated.")
