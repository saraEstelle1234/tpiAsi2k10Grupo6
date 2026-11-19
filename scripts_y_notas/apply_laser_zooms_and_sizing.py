# -*- coding: utf-8 -*-
"""
apply_laser_zooms_and_sizing.py
Aplica las mejoras solicitadas por el usuario:
1. Slide 06 (BPMN Operativo): Agranda el marco del diagrama (640px) y calibra los 5 zooms con precisión láser.
2. Slide 09 (Casos de Uso): Reestructura el layout a 1fr 320px (diagrama gigante ~1100px x 740px), elimina bandas negras, e implementa zooms por actor 100% exactos con el wrapper de proporción nativa.
3. Slide 12 (Clases DCD): Reemplaza "Multiplicidades Corregidas" por "⑤ Asignación Sala y Guardia" con zoom exacto en Sala, SalaXGuardia y Guardia.
"""

import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original length:", len(html))

# ==============================================================================
# 1. SLIDE 06 (BPMN Operativo): Enlarge frame & set laser coordinates
# ==============================================================================
idx_s6 = html.find('id="slide-6"')
idx_s6_end = html.find('id="slide-7"')
s6_chunk = html[idx_s6:idx_s6_end]

# Change height 500px to 640px in diagram-frame-clean of slide 6
s6_chunk = re.sub(
    r'<div class="diagram-frame-clean frame-white-canvas[^"]*" style="height:\s*500px;',
    r'<div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 640px;',
    s6_chunk
)

# Ensure #bpmn-oper-inner has aspect-ratio: 1682 / 798 so translate coordinates are 100% mathematically exact
if 'aspect-ratio' not in s6_chunk:
    s6_chunk = s6_chunk.replace(
        'id="bpmn-oper-inner">',
        'id="bpmn-oper-inner" style="height: 100%; aspect-ratio: 1682 / 798; display: flex; align-items: center; justify-content: center; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform;">'
    )

html = html[:idx_s6] + s6_chunk + html[idx_s6_end:]
print("Slide 06 markup updated.")

# ==============================================================================
# 2. SLIDE 09 (Casos de Uso): Enlarge layout (1fr 320px), frame (740px), no black bars
# ==============================================================================
idx_s9 = html.find('id="slide-9"')
idx_s9_end = html.find('id="slide-10"')
s9_chunk = html[idx_s9:idx_s9_end]

# Change grid layout from 620px 1fr to 1fr 320px
s9_chunk = re.sub(
    r'grid-template-columns:\s*620px\s*1fr;',
    'grid-template-columns: 1fr 320px;',
    s9_chunk
)

# Replace diagram frame in slide 9 to be 740px high and use cinematic-viewport + dcu-inner
old_dcu_frame_pattern = r'<div class="diagram-frame-clean frame-white-canvas[^>]*>.*?<div class="diagram-action-bar"'
# Let's inspect the exact markup of slide 9 diagram container
idx_df_start = s9_chunk.find('<div class="diagram-frame-clean')
idx_df_img = s9_chunk.find('id="dcu-img"', idx_df_start)
idx_df_action = s9_chunk.find('<div class="diagram-action-bar"', idx_df_img)

# New diagram frame container
new_dcu_viewport_html = """<div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 740px; display: flex; flex-direction: column; padding: 10px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); background: #0B132B;">
          <div class="cinematic-viewport dark-bg" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: #080D1A;">
            <div id="dcu-inner" style="height: 100%; aspect-ratio: 1455 / 1675; display: flex; align-items: center; justify-content: center; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform;">
              <img id="dcu-img" style="width: 100%; height: 100%; object-fit: fill; display: block;" """

if idx_df_start != -1 and idx_df_img != -1:
    # replace up to `style="` of dcu-img
    old_part = s9_chunk[idx_df_start:idx_df_img + len('id="dcu-img" ')]
    s9_chunk = s9_chunk[:idx_df_start] + new_dcu_viewport_html + s9_chunk[idx_df_img + len('id="dcu-img" '):]
    # close the extra div before diagram-action-bar
    idx_act = s9_chunk.find('<div class="diagram-action-bar"')
    s9_chunk = s9_chunk[:idx_act] + '</div>\n          </div>\n          ' + s9_chunk[idx_act:]
    print("Slide 09 viewport and dcu-inner updated to 740px widescreen!")

html = html[:idx_s9] + s9_chunk + html[idx_s9_end:]

# ==============================================================================
# 3. SLIDE 12 (Clases DCD): Update Tour Button 5 to "Asignación Sala y Guardia"
# ==============================================================================
idx_s12 = html.find('id="slide-12"')
idx_s12_end = html.find('id="slide-13"')
s12_chunk = html[idx_s12:idx_s12_end]

s12_chunk = s12_chunk.replace(
    '⑤ Multiplicidades Corregidas',
    '⑤ Asignación Sala y Guardia'
)
s12_chunk = s12_chunk.replace(
    '⑤ Multiplicidades Corre',
    '⑤ Asignación Sala y Guardia'
)

# Ensure #dcd-inner has aspect-ratio: 1422 / 904
if 'id="dcd-inner"' not in s12_chunk:
    s12_chunk = s12_chunk.replace(
        '<div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; background: #121212; border-radius: 10px;">',
        '<div class="cinematic-viewport dark-bg" style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; background: #121212; border-radius: 10px;">\n            <div id="dcd-inner" style="height: 100%; aspect-ratio: 1422 / 904; display: flex; align-items: center; justify-content: center; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform;">'
    )
    idx_btn_act = s12_chunk.find('<div class="diagram-action-bar"')
    s12_chunk = s12_chunk[:idx_btn_act] + '</div>\n          ' + s12_chunk[idx_btn_act:]
    print("Slide 12 #dcd-inner wrapper added.")

html = html[:idx_s12] + s12_chunk + html[idx_s12_end:]

# ==============================================================================
# 4. JAVASCRIPT: LASER-PRECISE STEPS & TRANSFORMS
# ==============================================================================

# 4.1 BPMN_TOUR_STEPS
js_bpmn_laser = """
    const BPMN_TOUR_STEPS = [
      {
        title: "Visión General del Proceso Operativo",
        desc: "Flujo completo de 4 carriles (Guardia, Encargado Web, Supervisor, Restaurador) con compuertas, almacenes de datos y cambios de estado.",
        tag: "VISTA GENERAL",
        transform: "scale(1) translate(0%, 0%)"
      },
      {
        title: "Fase 1: Inicio de Ronda y Vigilancia Física",
        desc: "El guardia consulta su asignación de ronda e inicia la recorrida en las salas de exhibición, verificando estado físico y registrando observación pendiente.",
        tag: "PASO 1 DE 4 · RONDA Y VIGILANCIA",
        transform: "scale(2.1) translate(25%, 37%)"
      },
      {
        title: "Fase 2: Detección y Registro del Incidente",
        desc: "Al constatar daño, se alimentan los almacenes 'Obras' y 'Salas', pasa la sala a 'Incidente activo' y registra hora y tipología del evento.",
        tag: "PASO 2 DE 4 · DETECCIÓN Y REGISTRO",
        transform: "scale(2.3) translate(13%, 30%)"
      },
      {
        title: "Fase 3: Consulta de Acciones Sugeridas",
        desc: "El sistema propone inmediatamente la acción preventiva según el material del objeto (deterioro provocado, caída accidental o deterioro natural).",
        tag: "PASO 3 DE 4 · ACCIONES SUGERIDAS",
        transform: "scale(2.05) translate(-6%, 0%)"
      },
      {
        title: "Fase 4: Supervisión y Actividad 'Restaurar Obra'",
        desc: "El supervisor resuelve el destino de la pieza. Si requiere reparación, se activa la tarea explícita 'Restaurar obra' en el carril del Restaurador.",
        tag: "PASO 4 DE 4 · RESTAURACIÓN DE OBRA",
        transform: "scale(2.2) translate(28%, -32%)"
      }
    ];

    function setBpmnTour(stepIdx, btn) {
      document.querySelectorAll('#bpmn-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const inner = document.getElementById('bpmn-oper-inner');
      const data = BPMN_TOUR_STEPS[stepIdx];
      if (inner && data) {
        inner.style.transform = data.transform;
        const tagEl = document.getElementById('bpmn-tour-tag');
        const titleEl = document.getElementById('bpmn-tour-title');
        const descEl = document.getElementById('bpmn-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }
"""

html = re.sub(
    r'const BPMN_TOUR_STEPS = \[.*?\];\s*function setBpmnTour\(.*?\)\s*\{.*?\}\s*\}',
    js_bpmn_laser.strip(),
    html,
    flags=re.DOTALL
)

# 4.2 DCD_TOUR_STEPS
js_dcd_laser = """
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
        title: "Sector 4: Asignación de Sala y Guardia",
        desc: "La clase Sala se vincula con SalaXGuardia (1..*) registrando el historial de rondas presenciales y el Guardia asignado a cada revisión de sala.",
        tag: "ASIGNACIÓN SALA Y GUARDIA",
        transform: "scale(2.05) translate(31%, -27.5%)"
      }
    ];

    function setDcdTour(stepIdx, btn) {
      document.querySelectorAll('#dcd-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const inner = document.getElementById('dcd-inner') || document.getElementById('dcd-img');
      const data = DCD_TOUR_STEPS[stepIdx];
      if (inner && data) {
        inner.style.transform = data.transform;
        const tagEl = document.getElementById('dcd-tour-tag');
        const titleEl = document.getElementById('dcd-tour-title');
        const descEl = document.getElementById('dcd-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }
"""

html = re.sub(
    r'const DCD_TOUR_STEPS = \[.*?\];\s*function setDcdTour\(.*?\)\s*\{.*?\}\s*\}',
    js_dcd_laser.strip(),
    html,
    flags=re.DOTALL
)

# 4.3 DCU_ACTOR_STEPS & setDcuSector
js_dcu_laser = """
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
        transform: 'scale(2.45) translate(31.5%, -13%)'
      },
      'supervision': {
        tag: 'CONTROL Y REPORTES',
        title: 'Encargado de Supervisión (CU 18 a 23)',
        desc: 'Genera patrones de incidentes (CU 18), informes diarios de vigilancia (CU 20) y seguimiento de resolución de obras dañadas (CU 23).',
        transform: 'scale(2.45) translate(37.5%, -35%)'
      },
      'ingreso': {
        tag: 'CATÁLOGO Y RESTAURACIÓN',
        title: 'Responsable de Ingreso de Obra (CU 1 a 4)',
        desc: 'Registra ingreso/reingreso de obras, consulta catálogo de piezas y deriva obras dañadas a restauración (CU 4).',
        transform: 'scale(2.45) translate(37.5%, 39.5%)'
      },
      'atencion': {
        tag: 'OPERACIÓN COMERCIAL & VISITAS',
        title: 'Atención al Cliente & Visitas (CU 8 a 11)',
        desc: 'Registra venta de entradas (CU 9), contratación de guías (CU 10) y consulta agenda de visitas guiadas (CU 11).',
        transform: 'scale(2.25) translate(24.5%, 8.5%)'
      },
      'admin': {
        tag: 'DATOS MAESTROS DEL SISTEMA',
        title: 'Admin de Sistema (CU 24 a 42)',
        desc: 'Administra tablas maestras del sistema: salas, materiales, tipos de incidentes, guías, estilos y baja de obras.',
        transform: 'scale(2.15) translate(-25.5%, 32.5%)'
      }
    };

    function setDcuSector(sector, btn) {
      const inner = document.getElementById('dcu-inner') || document.getElementById('dcu-img');
      if (!inner) return;
      if (btn) {
        const btns = btn.parentElement.querySelectorAll('.tour-btn, .preset-btn');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }
      
      const key = (sector === 'guardia') ? 'vigilancia' : ((sector === 'supervisor') ? 'supervision' : sector);
      const data = DCU_ACTOR_STEPS[key] || DCU_ACTOR_STEPS['all'];
      
      inner.style.transform = data.transform;
      const tagEl = document.getElementById('dcu-tour-tag');
      const titleEl = document.getElementById('dcu-tour-title');
      const descEl = document.getElementById('dcu-tour-desc');
      if (tagEl) tagEl.innerText = data.tag;
      if (titleEl) titleEl.innerText = data.title;
      if (descEl) descEl.innerText = data.desc;
    }
"""

html = re.sub(
    r'const DCU_ACTOR_STEPS = \{.*?\};\s*function setDcuSector\(.*?\)\s*\{.*?\}\s*\}',
    js_dcu_laser.strip(),
    html,
    flags=re.DOTALL
)

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished! presentacion.html and index.html successfully updated with laser precision.")
