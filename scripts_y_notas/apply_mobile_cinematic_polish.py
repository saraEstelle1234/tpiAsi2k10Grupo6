# -*- coding: utf-8 -*-
"""
apply_mobile_cinematic_polish.py
Perfecciona la responsividad en móviles para las 4 innovaciones cinemáticas:
- Tour bar con scroll horizontal táctil
- Pipeline nodal de trazabilidad swipeable con tarjetas consistentes
- Detalle de nodo apilado verticalmente en pantallas pequeñas
- Drawer de notas del orador a una sola columna y altura óptima
- Altura adaptable para marcos de 500px en celulares
"""

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

mobile_css = """
      /* --- CINEMATIC INNOVATIONS MOBILE OPTIMIZATIONS --- */
      .guided-tour-bar {
        overflow-x: auto !important;
        flex-wrap: nowrap !important;
        -webkit-overflow-scrolling: touch !important;
        padding: 6px 8px !important;
        gap: 6px !important;
      }
      .tour-btn {
        flex-shrink: 0 !important;
        font-size: 11px !important;
        padding: 4px 10px !important;
      }
      .cinematic-viewport {
        min-height: 250px !important;
      }
      .diagram-frame-clean[style*="height: 500px"] {
        height: clamp(280px, 46vh, 420px) !important;
      }

      /* Traceability nodal pipeline swipeable on mobile */
      .traza-pipeline-card {
        padding: 14px 14px !important;
      }
      .traza-nodes-grid {
        display: flex !important;
        overflow-x: auto !important;
        gap: 10px !important;
        padding-bottom: 8px !important;
        -webkit-overflow-scrolling: touch !important;
      }
      .traza-connecting-line {
        display: none !important;
      }
      .traza-node {
        min-width: 125px !important;
        max-width: 135px !important;
        flex-shrink: 0 !important;
        padding: 10px 8px !important;
      }
      .traza-node-thumb-box {
        height: 62px !important;
      }
      .traza-mono-code {
        font-size: 16px !important;
      }
      .traza-node-detail-card {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
        padding: 12px 14px !important;
      }
      .traza-detail-right {
        border-left: none !important;
        border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
        padding-left: 0 !important;
        padding-top: 8px !important;
        align-items: flex-start !important;
        text-align: left !important;
        flex-direction: row !important;
        justify-content: space-between !important;
      }

      /* Speaker Notes Drawer Mobile Optimization */
      .speaker-notes-drawer {
        max-height: 55vh !important;
      }
      .notes-content {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
        padding: 12px 14px 20px 14px !important;
      }
      .notes-header {
        padding: 10px 14px !important;
        gap: 8px !important;
        flex-wrap: wrap !important;
      }
"""

target = """.diagram-frame-clean[style*="height: 480px"] {
        height: clamp(260px, 44vh, 400px) !important;
      }"""

if target in html:
    html = html.replace(target, target + "\n" + mobile_css)
    print("Mobile cinematic CSS injected inside @media (max-width: 640px)!")
else:
    print("Warning: target not found in html!")

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Synchronized presentacion.html and index.html successfully.")
