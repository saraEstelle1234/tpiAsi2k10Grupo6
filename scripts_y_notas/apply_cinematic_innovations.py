# -*- coding: utf-8 -*-
"""
apply_cinematic_innovations.py
Aplica las 4 innovaciones inspiradas en museo-tpi.vercel.app sobre presentacion.html:
1. Pipeline Nodal de Trazabilidad E2E en Slide 13 con recortes reales de diagramas.
2. Modo "Recorrido Guiado con Zoom Cinematográfico" en BPMN (Slide 06) y Clases (Slide 12).
3. Atenuación Inteligente en la Matriz de Trazabilidad (Slide 13).
4. Panel Sincronizado de Notas del Orador (Tecla N y botón en dock).
"""

import os
import re
import json
import base64

def get_base64_img(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

b64_traza_bpmn = get_base64_img('media/traza_node_bpmn.png')
b64_traza_dcu = get_base64_img('media/traza_node_dcu.png')
b64_traza_proto = get_base64_img('media/traza_node_proto.png')
b64_traza_dcd = get_base64_img('media/traza_node_dcd.png')

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original presentacion.html length:", len(html))

# =========================================================================
# 1. CSS INJECTION (Before </style>)
# =========================================================================
css_to_add = """
    /* ========================================================
       FEATURE 1 & 2: GUIDED TOUR & SPOTLIGHT CAMERA
       ======================================================== */
    .guided-tour-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 12px;
      border-radius: 10px;
      margin-bottom: 10px;
    }
    .tour-label {
      font-size: 11px;
      font-weight: 800;
      color: #38BDF8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-right: 4px;
    }
    .tour-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #CBD5E1;
      font-size: 11.5px;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.25s ease;
      white-space: nowrap;
    }
    .tour-btn:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      color: #BAE6FD;
      transform: translateY(-1px);
    }
    .tour-btn.active {
      background: linear-gradient(135deg, rgba(45, 127, 249, 0.35) 0%, rgba(2, 132, 199, 0.45) 100%);
      border-color: #38BDF8;
      color: #FFFFFF;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
    }
    .tour-step-card {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-left: 4px solid #38BDF8;
      border-radius: 10px;
      padding: 10px 16px;
      margin-top: 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.3s ease;
    }
    .tour-step-tag {
      font-size: 10px;
      font-weight: 800;
      color: #38BDF8;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .tour-step-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #FFFFFF;
    }
    .tour-step-desc {
      font-size: 12px;
      line-height: 1.5;
      color: #94A3B8;
    }

    .cinematic-viewport {
      position: relative;
      overflow: hidden;
      width: 100%;
      height: 100%;
      border-radius: 10px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .cinematic-viewport.dark-bg {
      background: #121212;
    }
    .cinematic-inner {
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      transform-origin: center center;
      transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1);
      will-change: transform;
    }

    /* ========================================================
       FEATURE 1: TRACEABILITY E2E NODAL PIPELINE (SLIDE 13)
       ======================================================== */
    .traza-pipeline-card {
      background: linear-gradient(145deg, rgba(15, 23, 42, 0.95) 0%, rgba(8, 16, 32, 0.98) 100%);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 14px;
      padding: 18px 22px;
      margin-bottom: 20px;
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.5);
      position: relative;
      overflow: hidden;
    }
    .traza-pipeline-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .traza-pipeline-badge {
      font-size: 10.5px;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.15);
      color: #38BDF8;
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 2px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .traza-pipeline-controls {
      display: flex;
      gap: 8px;
    }
    .traza-pipe-play-btn {
      background: linear-gradient(135deg, #2D7FF9 0%, #0284C7 100%);
      border: none;
      color: #FFFFFF;
      font-size: 11.5px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 12px rgba(45, 127, 249, 0.3);
      transition: all 0.25s ease;
    }
    .traza-pipe-play-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(45, 127, 249, 0.45);
    }
    .traza-pipe-reset-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #CBD5E1;
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .traza-pipe-reset-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      color: #FFFFFF;
    }

    .traza-nodes-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
      position: relative;
      margin-bottom: 16px;
    }
    .traza-connecting-line {
      position: absolute;
      top: 68px;
      left: 8%;
      right: 8%;
      height: 3px;
      background: linear-gradient(90deg, #38BDF8 0%, #818CF8 50%, #34D399 100%);
      opacity: 0.35;
      z-index: 1;
      pointer-events: none;
    }
    .traza-node {
      background: rgba(15, 23, 42, 0.9);
      border: 1.5px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
      position: relative;
      z-index: 2;
      opacity: 0.45;
      filter: grayscale(40%);
    }
    .traza-node:hover {
      opacity: 0.9;
      filter: grayscale(0%);
      transform: translateY(-2px);
      border-color: rgba(56, 189, 248, 0.5);
    }
    .traza-node.active {
      opacity: 1;
      filter: grayscale(0%);
      border-color: #38BDF8;
      background: linear-gradient(160deg, rgba(16, 32, 62, 0.95) 0%, rgba(8, 16, 32, 0.98) 100%);
      box-shadow: 0 0 20px rgba(56, 189, 248, 0.35), 0 8px 24px rgba(0, 0, 0, 0.5);
      transform: translateY(-3px);
    }
    .traza-node-step {
      font-size: 9.5px;
      font-weight: 800;
      color: #94A3B8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }
    .traza-node.active .traza-node-step {
      color: #38BDF8;
    }
    .traza-node-thumb-box {
      width: 100%;
      height: 76px;
      border-radius: 8px;
      overflow: hidden;
      background: #000;
      border: 1px solid rgba(255, 255, 255, 0.1);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .traza-node-thumb-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }
    .traza-node:hover .traza-node-thumb-box img {
      transform: scale(1.08);
    }
    .traza-node-mono-box {
      background: linear-gradient(135deg, rgba(8, 16, 32, 0.95) 0%, rgba(15, 23, 42, 0.95) 100%);
      flex-direction: column;
      gap: 2px;
      border: 1px solid rgba(56, 189, 248, 0.35);
    }
    .traza-mono-code {
      font-family: 'Courier New', Courier, monospace;
      font-size: 20px;
      font-weight: 800;
      color: #38BDF8;
      letter-spacing: 0.05em;
    }
    .traza-mono-sub {
      font-size: 9.5px;
      color: #94A3B8;
      text-transform: uppercase;
    }
    .traza-node-title {
      font-size: 12px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 3px;
      line-height: 1.3;
    }
    .traza-node-sub {
      font-size: 10.5px;
      color: #94A3B8;
      line-height: 1.3;
    }

    .traza-node-detail-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 10px;
      padding: 14px 18px;
      display: grid;
      grid-template-columns: 1fr 220px;
      gap: 16px;
      align-items: center;
      margin-bottom: 12px;
    }
    .traza-detail-badge {
      font-size: 10px;
      font-weight: 800;
      color: #38BDF8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }
    .traza-detail-heading {
      font-size: 14px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 4px;
    }
    .traza-detail-text {
      font-size: 12.5px;
      color: #CBD5E1;
      line-height: 1.5;
    }
    .traza-detail-right {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      text-align: right;
      border-left: 1px solid rgba(255, 255, 255, 0.08);
      padding-left: 16px;
    }
    .traza-detail-metric-label {
      font-size: 10px;
      color: #94A3B8;
      text-transform: uppercase;
    }
    .traza-detail-metric-val {
      font-size: 18px;
      font-weight: 800;
      color: #34D399;
      margin: 2px 0 4px 0;
    }
    .traza-detail-link-tag {
      font-size: 10.5px;
      color: #38BDF8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 2px 8px;
      border-radius: 4px;
    }

    .traza-scope-card {
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-left: 3.5px solid #F59E0B;
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 11.5px;
      color: #FDE68A;
      line-height: 1.5;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }
    .traza-scope-badge {
      font-size: 10px;
      font-weight: 800;
      background: rgba(245, 158, 11, 0.2);
      color: #FCD34D;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      white-space: nowrap;
      margin-top: 1px;
    }

    /* ========================================================
       FEATURE 3: SMART MATRIX ROW DIMMING
       ======================================================== */
    .trace-item {
      transition: opacity 0.3s ease, filter 0.3s ease, transform 0.25s ease !important;
    }
    .trace-item.row-dimmed {
      opacity: 0.18 !important;
      filter: grayscale(70%) !important;
      transform: scale(0.99) !important;
    }
    .trace-item.row-highlighted {
      opacity: 1 !important;
      filter: grayscale(0%) !important;
      border-left: 4px solid #38BDF8 !important;
      background: rgba(56, 189, 248, 0.12) !important;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.2) !important;
      transform: scale(1.01) !important;
    }

    /* ========================================================
       FEATURE 4: SPEAKER NOTES DRAWER
       ======================================================== */
    .speaker-notes-drawer {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(10, 20, 38, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1px solid rgba(56, 189, 248, 0.35);
      box-shadow: 0 -12px 40px rgba(0, 0, 0, 0.65);
      z-index: 9999;
      transform: translateY(105%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      max-height: 42vh;
      display: flex;
      flex-direction: column;
      border-radius: 16px 16px 0 0;
    }
    .speaker-notes-drawer.open {
      transform: translateY(0);
    }
    .notes-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(15, 23, 42, 0.6);
      border-radius: 16px 16px 0 0;
    }
    .notes-badge {
      font-size: 10px;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.18);
      color: #38BDF8;
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 2px 8px;
      border-radius: 4px;
      letter-spacing: 0.05em;
    }
    .notes-speaker {
      font-size: 13.5px;
      font-weight: 800;
      color: #FFFFFF;
    }
    .notes-time-pill {
      font-size: 11px;
      font-weight: 700;
      color: #FCD34D;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.3);
      padding: 2px 7px;
      border-radius: 4px;
    }
    .notes-slide-pill {
      font-size: 11px;
      color: #94A3B8;
      font-family: monospace;
    }
    .notes-close-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #CBD5E1;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      transition: all 0.2s ease;
    }
    .notes-close-btn:hover {
      background: rgba(239, 68, 68, 0.3);
      border-color: #EF4444;
      color: #FFFFFF;
    }
    .notes-content {
      padding: 16px 22px 24px 22px;
      overflow-y: auto;
      display: grid;
      grid-template-columns: 1.3fr 0.9fr;
      gap: 20px;
    }
    .notes-speech-box {
      font-size: 13px;
      line-height: 1.6;
      color: #E2E8F0;
      background: rgba(0, 0, 0, 0.25);
      padding: 12px 16px;
      border-radius: 8px;
      border-left: 3px solid #38BDF8;
    }
    .notes-bullets-box {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .notes-bullet-item {
      font-size: 12px;
      line-height: 1.45;
      color: #CBD5E1;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }
    .notes-bullet-item::before {
      content: '•';
      color: #38BDF8;
      font-weight: 800;
      font-size: 14px;
      line-height: 1;
    }
"""

if '</style>' in html:
    html = html.replace('</style>', css_to_add + '\n</style>')
    print("Injected CSS styles.")

# =========================================================================
# 2. SLIDE 06: BPMN GUIDED TOUR
# =========================================================================
bpmn_tour_html = """
      <!-- Recorrido Guiado BPMN Operativo (Cámara Cinematográfica) -->
      <div class="guided-tour-bar" id="bpmn-tour-bar">
        <span class="tour-label">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>
          Recorrido Guiado:
        </span>
        <button class="tour-btn active" onclick="setBpmnTour(0, this)">① Todo el Proceso</button>
        <button class="tour-btn" onclick="setBpmnTour(1, this)">② Ronda del Guardia</button>
        <button class="tour-btn" onclick="setBpmnTour(2, this)">③ Detección & Registro</button>
        <button class="tour-btn" onclick="setBpmnTour(3, this)">④ Acciones Sugeridas</button>
        <button class="tour-btn" onclick="setBpmnTour(4, this)">⑤ Restauración de Obra</button>
      </div>

      <div style="display: flex; flex-direction: column; gap: 10px;">
        <!-- Diagrama en marco blanco con cámara 2D -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 500px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
          <div class="cinematic-viewport">
            <div class="cinematic-inner" id="bpmn-oper-inner">
"""

old_s6_start = """      <div style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Diagrama a tamaño máximo horizontal en marco blanco limpio sin bordes negros -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">"""

if old_s6_start in html:
    html = html.replace(old_s6_start, bpmn_tour_html)
    html = html.replace('<div class="diagram-action-bar">\n            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida', '</div>\n          </div>\n          <div class="diagram-action-bar">\n            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida')
    tour_card_bpmn = """
        <!-- Card dinámico explicativo de la fase activa -->
        <div class="tour-step-card" id="bpmn-tour-card">
          <div class="tour-step-tag" id="bpmn-tour-tag">VISTA GENERAL</div>
          <div class="tour-step-title" id="bpmn-tour-title">Visión General del Proceso Operativo</div>
          <div class="tour-step-desc" id="bpmn-tour-desc">Flujo completo de 4 carriles (Guardia, Encargado Web, Supervisor, Restaurador) con compuertas, almacenes de datos y cambios de estado destino explícitos.</div>
        </div>
"""
    marker_s6_cards = '<!-- 3 Tarjetas de Correcciones Clave del Docente -->'
    html = html.replace(marker_s6_cards, tour_card_bpmn + '\n        ' + marker_s6_cards)
    print("Slide 06 Guided Tour injected successfully.")
else:
    print("WARNING: Could not find old_s6_start")

# =========================================================================
# 3. SLIDE 12: DCD GUIDED TOUR
# =========================================================================
dcd_tour_html = """
      <!-- Recorrido Guiado DCD (Cámara Cinematográfica de Clases) -->
      <div class="guided-tour-bar" id="dcd-tour-bar">
        <span class="tour-label">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>
          Foco de Clases:
        </span>
        <button class="tour-btn active" onclick="setDcdTour(0, this)">① Vista Global DCD</button>
        <button class="tour-btn" onclick="setDcdTour(1, this)">② Incidente & Sala</button>
        <button class="tour-btn" onclick="setDcdTour(2, this)">③ Obra & Material</button>
        <button class="tour-btn" onclick="setDcdTour(3, this)">④ Tipos & Sugerencias</button>
        <button class="tour-btn" onclick="setDcdTour(4, this)">⑤ Multiplicidades Corregidas</button>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
"""

old_s12_start = """      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">"""

pos_s12 = html.find('id="slide-12"')
idx_s12_grid = html.find(old_s12_start, pos_s12)
if idx_s12_grid != -1:
    html = html[:idx_s12_grid] + dcd_tour_html + html[idx_s12_grid + len(old_s12_start):]
    tour_card_dcd = """
            <!-- Card dinámico explicativo del foco activo -->
            <div class="tour-step-card" id="dcd-tour-card" style="margin-bottom: 12px; margin-top: 0;">
              <div class="tour-step-tag" id="dcd-tour-tag">VISTA GENERAL DCD</div>
              <div class="tour-step-title" id="dcd-tour-title" style="font-size: 12.5px;">Estructura Completa del Dominio</div>
              <div class="tour-step-desc" id="dcd-tour-desc" style="font-size: 11.5px;">Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.</div>
            </div>
"""
    pos_dcd_col_right = html.find('<!-- Columna Derecha: Tarjetas analíticas y lecciones aprendidas -->', pos_s12)
    pos_insert_dcd_card = html.find('<div>', pos_dcd_col_right) + 5
    html = html[:pos_insert_dcd_card] + tour_card_dcd + html[pos_insert_dcd_card:]
    html = html.replace('id="dcd-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABY4AAAOICAIAAAD+efKdAAAACXBIWXMAAA7EAAAOxAGVKw4bAAD0dUlEQVR4nOzd658cRd3Hff+GQZCDieAVQAQFI4cooJwuREEiyEGjyMnAIoKcRENYEEXADLCAAiuHBFg',
                        'id="dcd-img" style="transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABY4AAAOICAIAAAD+efKdAAAACXBIWXMAAA7EAAAOxAGVKw4bAAD0dUlEQVR4nOzd658cRd3Hff+GQZCDieAVQAQFI4cooJwuREEiyEGjyMnAIoKcRENYEEXADLCAAiuHBFg')
    print("Slide 12 Guided Tour injected successfully.")
else:
    print("WARNING: Could not find old_s12_start")

# =========================================================================
# 4. SLIDE 13: TRACEABILITY E2E NODAL PIPELINE + SCOPE NOTE
# =========================================================================
traza_pipeline_html = f"""
      <!-- ========================================================
           PIPELINE NODAL DE TRAZABILIDAD E2E (5 ESTACIONES)
           ======================================================== -->
      <div class="traza-pipeline-card">
        <div class="traza-pipeline-header">
          <div style="display: flex; align-items: center; gap: 10px;">
            <span class="traza-pipeline-badge">TRAZABILIDAD E2E</span>
            <h3 style="margin: 0; font-size: 15px; font-weight: 800; color: #FFF;">Hilo Conductor Integral: Caso Crítico «Registrar Incidente en Sala»</h3>
          </div>
          <div class="traza-pipeline-controls">
            <button class="traza-pipe-play-btn" onclick="playTrazaPipeline()">⚡ Recorrido Paso a Paso</button>
            <button class="traza-pipe-reset-btn" onclick="resetTrazaPipeline()">Ver Todos Activos</button>
          </div>
        </div>

        <!-- 5 Nodos Conectados Horizontalmente con Línea Continua -->
        <div class="traza-nodes-grid" id="traza-nodes-grid">
          <div class="traza-connecting-line" id="traza-connecting-line"></div>

          <!-- Nodo 1: BPMN -->
          <div class="traza-node active" id="traza-node-1" onclick="selectTrazaNode(1)">
            <div class="traza-node-step">1 · PROCESO BPMN</div>
            <div class="traza-node-thumb-box">
              <img src="data:image/png;base64,{b64_traza_bpmn}" alt="BPMN">
            </div>
            <div class="traza-node-title">BPMN Operativo</div>
            <div class="traza-node-sub">Gestionar incidentes</div>
          </div>

          <!-- Nodo 2: RF -->
          <div class="traza-node active" id="traza-node-2" onclick="selectTrazaNode(2)">
            <div class="traza-node-step">2 · REQUERIMIENTO</div>
            <div class="traza-node-thumb-box traza-node-mono-box">
              <span class="traza-mono-code">RF45</span>
              <span class="traza-mono-sub">Registrar Incidente</span>
            </div>
            <div class="traza-node-title">Requerimiento Funcional</div>
            <div class="traza-node-sub">Regla de Negocio RN-02</div>
          </div>

          <!-- Nodo 3: CU -->
          <div class="traza-node active" id="traza-node-3" onclick="selectTrazaNode(3)">
            <div class="traza-node-step">3 · CASO DE USO</div>
            <div class="traza-node-thumb-box">
              <img src="data:image/png;base64,{b64_traza_dcu}" alt="CU">
            </div>
            <div class="traza-node-title">CU-15 Registrar Incidente</div>
            <div class="traza-node-sub">Actor Guardia («extend»)</div>
          </div>

          <!-- Nodo 4: Prototipo UI -->
          <div class="traza-node active" id="traza-node-4" onclick="selectTrazaNode(4)">
            <div class="traza-node-step">4 · PROTOTIPO UI</div>
            <div class="traza-node-thumb-box">
              <img src="data:image/png;base64,{b64_traza_proto}" alt="UI">
            </div>
            <div class="traza-node-title">Pantalla de Carga</div>
            <div class="traza-node-sub">1 control por paso</div>
          </div>

          <!-- Nodo 5: Clases DCD -->
          <div class="traza-node active" id="traza-node-5" onclick="selectTrazaNode(5)">
            <div class="traza-node-step">5 · CLASES DCD</div>
            <div class="traza-node-thumb-box">
              <img src="data:image/png;base64,{b64_traza_dcd}" alt="DCD">
            </div>
            <div class="traza-node-title">6 Clases del Dominio</div>
            <div class="traza-node-sub">Incidente, Sala, Obra...</div>
          </div>
        </div>

        <!-- Card Dinámico Explicativo de la Etapa Seleccionada -->
        <div class="traza-node-detail-card" id="traza-node-detail-card">
          <div class="traza-detail-left">
            <div class="traza-detail-badge" id="traza-detail-badge">Etapa 1 · Proceso de Negocio</div>
            <div class="traza-detail-heading" id="traza-detail-heading">BPMN Operativo: Tarea «Registrar tipo de incidente y estado de sala»</div>
            <div class="traza-detail-text" id="traza-detail-text">
              El guardia detecta anomalías durante su ronda de vigilancia. Si constata daño, el flujo se bifurca hacia 'Deterioro provocado', 'Caída accidental' o 'Deterioro natural', pasando la sala a 'Incidente activo' y solicitando al sistema la sugerencia de acción preventiva.
            </div>
          </div>
          <div class="traza-detail-right">
            <div class="traza-detail-metric-label">Trazabilidad software</div>
            <div class="traza-detail-metric-val" id="traza-detail-metric">100% Cobertura</div>
            <div class="traza-detail-link-tag" id="traza-detail-link">Vinculado a RF45 &bull; CU-15 &bull; DCD</div>
          </div>
        </div>

        <!-- Nota de Alcance Metodológico -->
        <div class="traza-scope-card">
          <span class="traza-scope-badge">Nota de Alcance Metodológico</span>
          <span>
            El prototipo y el diagrama de clases modelan en profundidad el caso crítico <strong>Registrar Incidente</strong> por indicación directa de la cátedra de ASI. Las operaciones de Entrada, Guías y Exposiciones se mantienen en el nivel analítico de Procesos y RFs para no dispersar el alcance de la defensa.
          </span>
        </div>
      </div>
"""

pos_s13 = html.find('id="slide-13"')
pos_s13_insert = html.find('<!-- Filter Controls Bar -->', pos_s13)
if pos_s13_insert != -1:
    html = html[:pos_s13_insert] + traza_pipeline_html + '\n      ' + html[pos_s13_insert:]
    print("Slide 13 Nodal Pipeline injected successfully.")
else:
    print("WARNING: Could not find Slide 13 filter controls insertion point")

# =========================================================================
# 5. DOCK BUTTON FOR SPEAKER NOTES
# =========================================================================
dock_notes_btn = """
    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" id="dock-btn-notes" onclick="handleDockClick(this, toggleSpeakerNotes)" aria-label="Notas del Orador" title="Notas del orador (Tecla N)">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
      </button>
      <div class="dock-tooltip">Notas del Orador (N)</div>
    </div>
"""

pos_dock_insert = html.find('<div class="dock-item-wrapper">\n      <button class="dock-icon-btn" onclick="handleDockClick(this, openOverviewModal)"')
if pos_dock_insert != -1:
    html = html[:pos_dock_insert] + dock_notes_btn + '\n    ' + html[pos_dock_insert:]
    print("Dock notes button injected successfully.")
else:
    print("WARNING: Could not find dock overview button")

# =========================================================================
# 6. SPEAKER NOTES DRAWER MARKUP (Before </body>)
# =========================================================================
notes_drawer_html = """
  <!-- ========================================================
       SPEAKER NOTES DRAWER (TECLA 'N' O BOTÓN DOCK)
       ======================================================== -->
  <div id="speaker-notes-drawer" class="speaker-notes-drawer">
    <div class="notes-header">
      <div style="display: flex; align-items: center; gap: 10px;">
        <span class="notes-badge">🎙️ NOTAS DEL ORADOR</span>
        <span class="notes-speaker" id="notes-speaker-name">Agustín Cufre</span>
        <span class="notes-time-pill" id="notes-time-estimate">⏱️ 1:45 min</span>
        <span class="notes-slide-pill" id="notes-slide-indicator">Slide 01 / 14</span>
      </div>
      <div style="display: flex; align-items: center; gap: 10px;">
        <span style="font-size: 11px; color: #94A3B8;">Atajo de teclado: <strong>[N]</strong></span>
        <button class="notes-close-btn" onclick="toggleSpeakerNotes()" title="Cerrar notas">&times;</button>
      </div>
    </div>
    <div class="notes-content">
      <div class="notes-speech-box" id="notes-speech-text">
        <strong>Speech sugerido:</strong> "Buenas tardes profesores. Somos el Grupo 6 del curso 2K10..."
      </div>
      <div class="notes-bullets-box" id="notes-bullets-list">
        <!-- Bullets injected dynamically -->
      </div>
    </div>
  </div>
"""

html = html.replace('</body>', notes_drawer_html + '\n</body>')
print("Speaker notes drawer markup injected successfully.")

# =========================================================================
# 7. JAVASCRIPT LOGIC INJECTION (Before </script>)
# =========================================================================
# Prepare notes dict cleanly without f-string brackets collision
notes_dict_json = json.dumps({
    1: {
        "speaker": "Agustín Cufre",
        "time": "1:45 min",
        "title": "Portada y Equipo del Grupo 6",
        "speech": "Buenas tardes profesores. Somos el Grupo 6 del curso 2K10 y hoy presentamos nuestro Trabajo Práctico Integrador: el Sistema de Gestión y Vigilancia Museológica para el Museo de Historia Natural. Nuestro equipo está compuesto por 8 integrantes activos, coordinando cada etapa metodológica desde el negocio hasta las clases del software.",
        "bullets": [
            "Presentación institucional del equipo y cátedra de ASI.",
            "Encuadre del proyecto: Sistema de Gestión y Vigilancia Museológica.",
            "Duración total de la defensa: 15 minutos cronometrados."
        ]
    },
    2: {
        "speaker": "Agustín Cufre",
        "time": "1:45 min",
        "title": "Dominio Bajo Estudio y Objetivos",
        "speech": "Analizamos el dominio bajo estudio. El museo expone colecciones de arte y paleontología de artistas locales e internacionales, sustentándose mediante el cobro de entradas generales y el arancel optativo de visitas guiadas. Como se observa en la fotografía oficial de las salas de exhibición, el museo cuenta con objetos animados y piezas de alto valor patrimonial sensibles a la temperatura, humedad e iluminación según su material. Nuestro alcance se centra en dar soporte integral a las rondas de inspección física y al congelamiento inmediato del daño cuando ocurre un incidente.",
        "bullets": [
            "Misión: Exponer obras y preservar el patrimonio con control de incidentes.",
            "Proceso Esencial: 'Exponer obras de arte' (cliente directo del software).",
            "Proceso de Soporte Bajo Estudio: 'Gestionar incidentes y restauración de obras'."
        ]
    },
    3: {
        "speaker": "Kevin Pereyra",
        "time": "1:30 min",
        "title": "Mapa de Procesos de Negocio",
        "speech": "Presentamos la vista externa organizacional a través del Mapa de Procesos. Clasificamos los procesos en tres niveles: Estratégicos (Planificar exposiciones, Planificar visitas, Definir precios de guía y Definir precios de entrada); Esencial (Exponer obras de arte, corazón del museo); y Soporte (Gestionar ingreso de obras, Administrar RRHH y Gestionar incidentes y restauración de obras). Mantuvimos 'Definir precios de guía' y 'Definir precios de entrada' separados respetando la literalidad del enunciado, pero señalamos que en un modelo optimizado de granularidad pueden unificarse en 'Definir tarifas y servicios', complementado con la diagramación de horarios de guías.",
        "bullets": [
            "Procesos Estratégicos, Esenciales y de Soporte según Porter.",
            "Alineación con la observación docente: Granularidad en tarifas de entrada y guía.",
            "Identificación del cliente del proceso de incidentes: Exponer obras de arte."
        ]
    },
    4: {
        "speaker": "Tobias Molina",
        "time": "1:30 min",
        "title": "Plantilla de Descripción de Proceso",
        "speech": "Formalizamos la Plantilla de Descripción del Proceso de Soporte: Gestionar incidentes y restauración de obras. El objetivo es gestionar incidentes y restauración mediante rondas de vigilancia, registrando en el Módulo Web para que los supervisores resuelvan el destino de las piezas. Su cliente es el proceso esencial 'Exponer obras de arte' y su producto es el informe de salas recorridas y las obras derivadas a reparación. Destacamos dos Reglas de Negocio fundamentales: RN-01 (Prioridad de rondas en salas críticas según sensibilidad del material) y RN-02 (Prohibición de registrar incidentes si la obra no pertenece a la sala asignada en la ronda).",
        "bullets": [
            "Ficha normalizada del proceso crítico bajo estudio.",
            "Regla de Negocio RN-01: Rondas prioritarias según material animado.",
            "Regla de Negocio RN-02: Integridad estricta entre Guardia, Sala y Obra."
        ]
    },
    5: {
        "speaker": "Tomas Marcuzzi",
        "time": "1:00 min",
        "title": "BPMN Nivel Descriptivo (4 Carriles)",
        "speech": "En las diapositivas 5 y 6 modelamos la vista interna del proceso con BPMN. Iniciamos con el Nivel Descriptivo, estructurado en cuatro carriles que reflejan fielmente los roles reales de la organización: Encargado de Vigilancia (ronda física y novedades), Encargado Web (registro administrativo y tipos de incidentes), Encargado de Supervisión (evaluación y destino) y Restaurador (reparación física de la obra). Cada rol tiene responsabilidades acotadas, evitando sobrecargar al guardia de tareas administrativas que corresponden a la supervisión.",
        "bullets": [
            "Estructura en 4 carriles: Guardia, Encargado Web, Supervisor y Restaurador.",
            "Separación clara entre ronda física y administración web.",
            "Comprensión de alto nivel del flujo de negocio sin detalles técnicos."
        ]
    },
    6: {
        "speaker": "Tomas Marcuzzi",
        "time": "1:00 min",
        "title": "BPMN Nivel Operativo Corregido",
        "speech": "Pasamos al Nivel Operativo, donde aplicamos las correcciones metodológicas solicitadas por el docente: 1) Actividad explícita 'Restaurar obra' en el carril del Restaurador cuando el supervisor resuelve la reparación; 2) Almacenes de datos 'Obras' y 'Salas' que alimentan la actividad de registro de incidentes; 3) Carril administrativo del 'Encargado Web' para tipos de incidentes; y 4) Notación estricta en las actividades de cambio de estado indicando el estado destino: 'Incidente activo' en Sala y 'En restauración' o 'Inactivo' en Obra.",
        "bullets": [
            "Corrección 1: Actividad 'Restaurar obra' en carril Restaurador.",
            "Corrección 2: Objetos de datos Obras y Salas alimentando el registro.",
            "Corrección 3: Estados destino explícitos en cada actividad ('Incidente activo', 'Inactivo').",
            "Usa los botones del Recorrido Guiado para hacer foco en cada sector."
        ]
    },
    7: {
        "speaker": "Lucas Moyano",
        "time": "1:00 min",
        "title": "Requerimientos Funcionales (45 RFs)",
        "speech": "Detallamos la especificación de Requerimientos Funcionales. Identificamos 45 RFs clasificados en 9 módulos del dominio: Rondas y Vigilancia, Gestión de Incidentes, Administración de Obras, Salas, Tipos de Incidentes, Exposiciones, Visitas Guiadas, Venta de Entradas y Seguridad. Destacamos especialmente los RFs del caso de estudio: RF43 (consultar planificación de ronda), RF44 (registrar revisión de sala), RF45 (registrar incidente con validación de pertenencia de obra), RF46 (sugerencia inmediata de acciones según material) y RF50 (cambio de estado de obra a inactiva y derivación a restauración).",
        "bullets": [
            "45 Requerimientos Funcionales categorizados en 9 módulos de negocio.",
            "Trazabilidad completa con las actividades del BPMN Operativo.",
            "Foco en RF43 a RF50 que sustentan el caso crítico de incidentes."
        ]
    },
    8: {
        "speaker": "Lucas Moyano",
        "time": "0:45 min",
        "title": "Requerimientos No Funcionales (RNF)",
        "speech": "Complementamos con los Requerimientos No Funcionales que garantizan la calidad del software según ISO/IEC 25010: RNF-01 (Seguridad y Control de Acceso basado en Roles: RBAC con token JWT y HTTPS, limitando qué pantallas puede operar el guardia frente al supervisor) y RNF-02 (Rendimiento y Disponibilidad en Rondas: tiempo de respuesta sub-segundo <1.5s y disponibilidad del 99.5% durante el horario de exhibición al público).",
        "bullets": [
            "RNF-01: Seguridad, RBAC y confidencialidad de novedades patrimoniales.",
            "RNF-02: Disponibilidad 99.5% y latencia <1.5s en rondas de vigilancia.",
            "Conformidad con el estándar internacional ISO/IEC 25010."
        ]
    },
    9: {
        "speaker": "Francisco Thomas Rapp",
        "time": "1:30 min",
        "title": "Diagrama de Casos de Uso General",
        "speech": "En la diapositiva 9 presentamos el Diagrama de Casos de Uso General que traduce los requerimientos funcionales en interacciones del usuario con el sistema. Identificamos 5 actores del sistema: Encargado de Vigilancia, Administrador Web, Encargado de Supervisión, Responsable de Atención al Cliente y Usuario General. El núcleo de nuestra solución articula el caso de uso base CU-14 'Registrar revisión de la sala' con una relación «extend» hacia el CU-15 'Registrar Incidente', el cual solo se dispara si el guardia detecta una anomalía o daño físico en su ronda.",
        "bullets": [
            "5 Actores organizacionales modelados en el sistema.",
            "Relación clave: CU-14 'Registrar revisión' extiende a CU-15 'Registrar incidente'.",
            "Separación entre vigilancia presencial y administración centralizada."
        ]
    },
    10: {
        "speaker": "Francisco Abad",
        "time": "1:00 min",
        "title": "Plantilla CU-15: Registrar Incidente",
        "speech": "Profundizamos en el caso de uso central: CU-15 Registrar Incidente. Especificamos el flujo normal paso a paso: el guardia selecciona la sala, busca el objeto dañado, el sistema muestra sus datos verificando que pertenezca a la sala, el guardia selecciona el tipo de incidente, el sistema presenta en solo lectura las acciones sugeridas de mitigación según el material y solicita confirmación. Como observó el docente en sus correcciones: eliminamos la ambigüedad de 'mostrar datos' especificando exactamente qué atributos se visualizan: Código, Título, Autor, Material y Ubicación.",
        "bullets": [
            "Plantilla detallada: Flujo básico de 11 pasos y flujos alternativos.",
            "Corrección docente aplicada: 'Mostrar datos' reemplazado por atributos concretos.",
            "Integridad de negocio: Verificación estricta de Obra perteneciente a la Sala."
        ]
    },
    11: {
        "speaker": "Francisco Abad",
        "time": "0:45 min",
        "title": "Prototipo de Pantalla UI (Página 13)",
        "speech": "Mostramos el Prototipo de Pantalla diseñado para el CU-15. La interfaz refleja el principio 'un control por paso': cuadro de búsqueda de objeto con botón Buscar, ficha de solo lectura con los datos confirmados del objeto (Nombre, Sala, Ubicación), selector desplegable de Tipo de Incidente, campo de hora automática y panel de acciones sugeridas con diálogo de confirmación final.",
        "bullets": [
            "Fiel reflejo de la maqueta oficial de la página 13 del TPI.",
            "Diseño ergonómico para uso ágil en dispositivos móviles o tablets de ronda.",
            "Controles bloqueados en solo lectura para preservar la integridad patrimonial."
        ]
    },
    12: {
        "speaker": "Juan Sebastián Tarditti",
        "time": "1:45 min",
        "title": "Diagrama de Clases del Dominio (DCD)",
        "speech": "Exponemos el Diagrama de Clases del Dominio completo, estructurado en torno al caso Registrar Incidente. La clase central 'Incidente' encapsula fecha, hora y descripción, asociándose con 'Obra', 'TipoIncidente' y 'Sala'. Destacamos las multiplicidades corregidas expresamente solicitadas por el docente: 1) Incidente ➔ (1) TipoIncidente: cada incidente tiene obligatoriamente un único tipo tipificado; 2) Sala ➔ (*) SalaXGuardia: una sala participa en múltiples asignaciones históricas de ronda con el guardia. 'Obra' delega en 'Material' para conocer las reacciones ante estímulos, y 'TipoIncidente' proporciona las acciones sugeridas.",
        "bullets": [
            "Corrección 1: Multiplicidad estricta Incidente ➔ (1) TipoIncidente.",
            "Corrección 2: Multiplicidad Sala ➔ (*) SalaXGuardia para histórico de rondas.",
            "Encapsulamiento de métodos: registrarObraInactiva() y registrarObraActiva().",
            "Usa los botones de Foco de Clases para navegar cada sector del DCD."
        ]
    },
    13: {
        "speaker": "Agustín Cufre",
        "time": "1:30 min",
        "title": "Trazabilidad Integral y Pipeline E2E",
        "speech": "Presentamos la Trazabilidad Integral del software. En el nuevo Hilo Conductor de 5 Estaciones pueden comprobar cómo cada decisión de diseño se encadena sin fisuras: 1) La tarea del BPMN Operativo 'Registrar tipo de incidente' da origen al 2) Requerimiento RF45 y la regla RN-02, que a su vez se implementa en el 3) Caso de Uso CU-15; este define cada control del 4) Prototipo UI y se materializa en las clases 5) Incidente, Sala, Obra y TipoIncidente del DCD. Como nota de alcance, el DCD modela con máxima granularidad este caso crítico por indicación de la cátedra, garantizando una arquitectura robusta y consistente.",
        "bullets": [
            "Hilo E2E de 5 Estaciones: BPMN ➔ RF ➔ CU ➔ UI ➔ DCD.",
            "Matriz de Cobertura con atenuación inteligente de módulos no relacionados.",
            "Nota de alcance: Foco exhaustivo en el caso crítico de incidentes."
        ]
    },
    14: {
        "speaker": "Agustín Cufre",
        "time": "1:00 min",
        "title": "Conclusiones y Cierre de la Defensa",
        "speech": "Para concluir, el Sistema de Gestión y Vigilancia Museológica brinda una respuesta tecnológica integral al Museo de Historia Natural, protegiendo su patrimonio y garantizando la trazabilidad entre el negocio y el código. Agradecemos a los profesores de la cátedra por sus observaciones y devoluciones, y quedamos a su entera disposición para responder cualquier pregunta.",
        "bullets": [
            "Cierre formal de la defensa oral grupal.",
            "Agradecimiento a los docentes y apertura de ronda de preguntas.",
            "Créditos finales a los 8 integrantes activos del Grupo 6."
        ]
    }
}, ensure_ascii=False)

js_script_content = """
    // ========================================================
    // SPEAKER NOTES DATASET & DRAWER CONTROLS
    // ========================================================
    const SPEAKER_NOTES = """ + notes_dict_json + """;
    let notesDrawerOpen = false;

    function toggleSpeakerNotes() {
      const drawer = document.getElementById('speaker-notes-drawer');
      if (!drawer) return;
      notesDrawerOpen = !notesDrawerOpen;
      if (notesDrawerOpen) {
        drawer.classList.add('open');
        updateSpeakerNotes(currentSlide);
      } else {
        drawer.classList.remove('open');
      }
    }

    function updateSpeakerNotes(slideNum) {
      const note = SPEAKER_NOTES[slideNum];
      if (!note) return;
      const speakerEl = document.getElementById('notes-speaker-name');
      const timeEl = document.getElementById('notes-time-estimate');
      const slideEl = document.getElementById('notes-slide-indicator');
      const speechEl = document.getElementById('notes-speech-text');
      const bulletsEl = document.getElementById('notes-bullets-list');

      if (speakerEl) speakerEl.innerText = note.speaker;
      if (timeEl) timeEl.innerText = '⏱️ ' + note.time;
      if (slideEl) slideEl.innerText = `Slide ${String(slideNum).padStart(2, '0')} / 14`;
      if (speechEl) speechEl.innerHTML = `<strong>Speech sugerido:</strong> "${note.speech}"`;
      if (bulletsEl) {
        bulletsEl.innerHTML = note.bullets.map(b => `<div class="notes-bullet-item">${b}</div>`).join('');
      }
    }

    // Keyboard shortcut [N]
    window.addEventListener('keydown', e => {
      if (e.key === 'n' || e.key === 'N') {
        if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) return;
        toggleSpeakerNotes();
      }
    });

    // ========================================================
    // FEATURE 1: TRAZABILIDAD E2E NODAL PIPELINE
    // ========================================================
    const TRAZA_NODES_DATA = {
      1: {
        badge: "Etapa 1 · Proceso de Negocio",
        heading: "BPMN Operativo: Tarea «Registrar tipo de incidente y estado de sala»",
        desc: "El guardia detecta anomalías durante su ronda de vigilancia. Si constata daño, el flujo se bifurca hacia 'Deterioro provocado', 'Caída accidental' o 'Deterioro natural', pasando la sala a 'Incidente activo' y solicitando al sistema la sugerencia de acción preventiva.",
        metric: "100% Cobertura",
        link: "Vinculado a RF45 · CU-15 · DCD"
      },
      2: {
        badge: "Etapa 2 · Requerimiento Funcional",
        heading: "RF45: Registrar Incidente en Sala & Regla RN-02",
        desc: "Especifica los datos de entrada requeridos (Fecha, Hora, Sala, Obra, Tipo de Incidente). Aplica la Regla de Negocio RN-02: integridad estricta entre la ronda asignada al guardia y la sala donde se ubica la obra.",
        metric: "Regla RN-02",
        link: "Origen BPMN Tarea 4 ➔ CU-15"
      },
      3: {
        badge: "Etapa 3 · Caso de Uso del Sistema",
        heading: "CU-15: Registrar Incidente (Extensión de CU-14)",
        desc: "El actor 'Encargado de Vigilancia' opera el caso de uso base CU-14 'Registrar revisión de sala'. Cuando se constata novedad, se dispara la relación «extend» hacia el CU-15 para registrar la tipología y recibir las acciones sugeridas.",
        metric: "Actor: Guardia",
        link: "Extiende CU-14 ➔ Prototipo UI"
      },
      4: {
        badge: "Etapa 4 · Prototipo de Interfaz UI",
        heading: "Pantalla de Carga y Validación (Página 13 del TPI)",
        desc: "Diseñada bajo el principio 'un control por paso': caja de búsqueda OBJ-408, ficha de solo lectura con datos verificados (Nombre, Sala, Ubicación), lista desplegable de tipo de incidente y ventana modal de confirmación.",
        metric: "Ergonomía UI",
        link: "Reflejo del Flujo CU-15 ➔ DCD"
      },
      5: {
        badge: "Etapa 5 · Diagrama de Clases del Dominio",
        heading: "Modelo de Objetos: Incidente, Sala, Obra y TipoIncidente",
        desc: "La clase Incidente encapsula el evento asociándose con Sala (1), Obra (1) y TipoIncidente (1). Incorpora las multiplicidades corregidas solicitadas por la cátedra e implementa los métodos registrarObraInactiva() y registrarObraActiva().",
        metric: "Multiplicidades OK",
        link: "Realización completa en software"
      }
    };

    let activeTrazaNode = 1;
    let trazaPlayTimer = null;

    function selectTrazaNode(nodeIdx) {
      activeTrazaNode = nodeIdx;
      for (let i = 1; i <= 5; i++) {
        const node = document.getElementById(`traza-node-${i}`);
        if (node) {
          if (i === nodeIdx) {
            node.classList.add('active');
          } else {
            node.classList.remove('active');
          }
        }
      }
      const data = TRAZA_NODES_DATA[nodeIdx];
      if (data) {
        document.getElementById('traza-detail-badge').innerText = data.badge;
        document.getElementById('traza-detail-heading').innerText = data.heading;
        document.getElementById('traza-detail-text').innerText = data.desc;
        document.getElementById('traza-detail-metric').innerText = data.metric;
        document.getElementById('traza-detail-link').innerText = data.link;
      }
    }

    function resetTrazaPipeline() {
      if (trazaPlayTimer) clearInterval(trazaPlayTimer);
      for (let i = 1; i <= 5; i++) {
        const node = document.getElementById(`traza-node-${i}`);
        if (node) node.classList.add('active');
      }
      selectTrazaNode(1);
      for (let i = 1; i <= 5; i++) {
        const node = document.getElementById(`traza-node-${i}`);
        if (node) node.classList.add('active');
      }
    }

    function playTrazaPipeline() {
      if (trazaPlayTimer) clearInterval(trazaPlayTimer);
      let step = 1;
      selectTrazaNode(step);
      trazaPlayTimer = setInterval(() => {
        step++;
        if (step > 5) {
          clearInterval(trazaPlayTimer);
          resetTrazaPipeline();
        } else {
          selectTrazaNode(step);
        }
      }, 2400);
    }

    // ========================================================
    // FEATURE 2: GUIDED TOURS (BPMN & DCD)
    // ========================================================
    const BPMN_TOUR_STEPS = [
      {
        title: "Visión General del Proceso Operativo",
        desc: "Flujo completo de 4 carriles (Guardia, Encargado Web, Supervisor, Restaurador) con compuertas, almacenes de datos y cambios de estado.",
        tag: "VISTA GENERAL",
        transform: "scale(1) translate(0, 0)"
      },
      {
        title: "Fase 1: Inicio de Ronda y Vigilancia Física",
        desc: "El guardia consulta su asignación de ronda e inicia la recorrida en las salas de exhibición verificando el estado de las obras expuestas.",
        tag: "PASO 1 DE 4",
        transform: "scale(2.2) translate(28%, 22%)"
      },
      {
        title: "Fase 2: Detección y Registro del Incidente",
        desc: "Al constatar daño o novedad, se alimenta de los almacenes 'Obras' y 'Salas', pasa la sala a 'Incidente activo' y registra la tipología correspondiente.",
        tag: "PASO 2 DE 4",
        transform: "scale(2.4) translate(0%, -5%)"
      },
      {
        title: "Fase 3: Consulta de Acciones Sugeridas",
        desc: "El sistema propone inmediatamente la acción preventiva según el material del objeto (ej. cubrir obra, corte térmico o aislamiento acústico).",
        tag: "PASO 3 DE 4",
        transform: "scale(2.4) translate(-22%, -12%)"
      },
      {
        title: "Fase 4: Supervisión y Actividad 'Restaurar Obra'",
        desc: "El supervisor resuelve el destino de la pieza. Si requiere reparación, se activa la tarea explícita 'Restaurar obra' en el carril del Restaurador.",
        tag: "PASO 4 DE 4",
        transform: "scale(2.3) translate(-36%, -22%)"
      }
    ];

    function setBpmnTour(stepIdx, btn) {
      document.querySelectorAll('#bpmn-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const inner = document.getElementById('bpmn-oper-inner');
      const data = BPMN_TOUR_STEPS[stepIdx];
      if (inner && data) {
        inner.style.transform = data.transform;
        document.getElementById('bpmn-tour-tag').innerText = data.tag;
        document.getElementById('bpmn-tour-title').innerText = data.title;
        document.getElementById('bpmn-tour-desc').innerText = data.desc;
      }
    }

    const DCD_TOUR_STEPS = [
      {
        title: "Vista Completa del Diagrama de Clases",
        desc: "Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.",
        tag: "VISTA GENERAL DCD",
        transform: "scale(1) translate(0, 0)"
      },
      {
        title: "Sector 1: Núcleo Incidente & Sala",
        desc: "La clase Incidente registra fecha, hora y descripción, vinculándose con Sala (1) y recuperando al Guardia a través de la relación histórica SalaXGuardia.",
        tag: "SECTOR 1 · INCIDENTE & SALA",
        transform: "scale(2.05) translate(20%, 8%)"
      },
      {
        title: "Sector 2: Obra, Material y Objetos Animados",
        desc: "Obra encapsula registrarObraInactiva() y registrarObraActiva(), asociándose con Material para evaluar reacciones y sensibilidad física.",
        tag: "SECTOR 2 · OBRA & MATERIAL",
        transform: "scale(1.95) translate(-10%, 6%)"
      },
      {
        title: "Sector 3: Tipos de Incidente y Acciones Sugeridas",
        desc: "TipoIncidente conoce las conductas inmediatas de mitigación recomendadas ante deterioro provocado, accidental o natural.",
        tag: "SECTOR 3 · TIPOS & ACCIONES",
        transform: "scale(2.35) translate(26%, -24%)"
      },
      {
        title: "Sector 4: Multiplicidades Críticas Corregidas",
        desc: "Multiplicidades requeridas por el docente incorporadas: Incidente ➔ (1) TipoIncidente (obligatoria) y Sala ➔ (*) SalaXGuardia (historial).",
        tag: "CORRECCIÓN CÁTEDRA",
        transform: "scale(2.2) translate(16%, -4%)"
      }
    ];

    function setDcdTour(stepIdx, btn) {
      document.querySelectorAll('#dcd-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('dcd-img');
      const data = DCD_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        document.getElementById('dcd-tour-tag').innerText = data.tag;
        document.getElementById('dcd-tour-title').innerText = data.title;
        document.getElementById('dcd-tour-desc').innerText = data.desc;
      }
    }

    // ========================================================
    // FEATURE 3: SMART MATRIX ROW DIMMING
    // ========================================================
    function applySmartMatrixDimming(activeCategory) {
      const rows = document.querySelectorAll('.trace-item');
      rows.forEach(row => {
        if (!activeCategory || activeCategory === 'all') {
          row.classList.remove('row-dimmed');
          row.classList.remove('row-highlighted');
        } else {
          const rowCategory = row.getAttribute('data-cat') || '';
          if (rowCategory.includes(activeCategory)) {
            row.classList.remove('row-dimmed');
            row.classList.add('row-highlighted');
          } else {
            row.classList.remove('row-highlighted');
            row.classList.add('row-dimmed');
          }
        }
      });
    }
"""

# Insert JS logic and hook updateSlide for notes
html = html.replace('function updateSlide() {', 'function updateSlide() {\n      if (notesDrawerOpen) updateSpeakerNotes(currentSlide);')
html = html.replace('function filterTraceModule(btn, cat) {', 'function filterTraceModule(btn, cat) {\n      applySmartMatrixDimming(cat);')
html = html.replace('// Initialize View', js_script_content + '\n    // Initialize View')

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("presentacion.html successfully compiled with all 4 innovations!")
