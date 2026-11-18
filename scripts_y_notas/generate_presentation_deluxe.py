# -*- coding: utf-8 -*-
"""
Generator script for the Deluxe Interactive Presentation for TPI ASI 2K10 - Grupo 6.
Builds presentacion.html with 14 high-end slides, pan & zoom modals, base64 images, and zero external dependencies.
"""
import os
import base64

def get_b64(path):
    if not os.path.exists(path):
        print(f"Warning: File {path} not found!")
        return ""
    with open(path, "rb") as f:
        ext = path.split('.')[-1].lower()
        if ext == 'jpg': ext = 'jpeg'
        data = base64.b64encode(f.read()).decode('ascii')
        return f"data:image/{ext};base64,{data}"

print("Encoding image assets...")
b64_mapa = get_b64("media_presentacion/page_3_img_0_16.png")
b64_p4 = get_b64("media_presentacion/rendered_page_4.png")
b64_bpmn_desc = get_b64("media_presentacion/page_7_img_0_26.png")
b64_bpmn_oper = get_b64("media_presentacion/page_8_img_0_29.png")
b64_dcu = get_b64("media_presentacion/page_9_img_0_32.png")
b64_p13 = get_b64("media_presentacion/rendered_page_13.png")
b64_proto = get_b64("media_presentacion/page_14_img_0_47.jpeg")
b64_dcd = get_b64("media_presentacion/page_15_img_0_50.png")
print("All assets successfully encoded.")

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Defensa TPI ASI 2K10 - Grupo 6 | Museo de Historia Natural</title>
  <style>
    :root {{
      --bg: #07090e;
      --surface: #0f172a;
      --card-bg: rgba(17, 24, 39, 0.72);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-border-glow: rgba(56, 189, 248, 0.35);
      --primary: #38bdf8;
      --primary-hover: #0ea5e9;
      --accent: #818cf8;
      --purple: #c084fc;
      --emerald: #34d399;
      --amber: #fbbf24;
      --rose: #f43f5e;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background: radial-gradient(circle at 50% -10%, #1e1b4b 0%, #07090e 70%, #030508 100%);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      user-select: none;
    }}

    /* Top Navigation Header */
    header {{
      height: 64px;
      padding: 0 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--card-border);
      background: rgba(7, 9, 14, 0.88);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 50;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .inst-badge {{
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(129, 140, 248, 0.15));
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .inst-badge::before {{
      content: "";
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 8px #38bdf8;
    }}

    .header-title {{
      font-size: 15px;
      font-weight: 600;
      color: var(--text);
      letter-spacing: 0.02em;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.25); }}
    .badge-indigo {{ background: rgba(129, 140, 248, 0.12); color: #818cf8; border: 1px solid rgba(129, 140, 248, 0.25); }}
    .badge-purple {{ background: rgba(192, 132, 252, 0.12); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.25); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.12); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.25); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.12); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.25); }}
    .badge-rose {{ background: rgba(244, 63, 94, 0.12); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.25); }}

    .btn-icon {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 7px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .btn-icon:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--primary);
      color: #fff;
    }}

    /* Progress bar */
    .progress-bar-container {{
      width: 100%;
      height: 3px;
      background: rgba(255, 255, 255, 0.04);
      position: sticky;
      top: 64px;
      z-index: 49;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
      width: 7.14%;
      transition: width 0.35s ease;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.7);
    }}

    /* Main Container */
    main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px 32px;
      max-width: 1440px;
      margin: 0 auto;
      width: 100%;
    }}

    .slide {{
      display: none;
      width: 100%;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.35s ease, transform 0.35s ease;
    }}

    .slide.active {{
      display: block;
      opacity: 1;
      transform: translateY(0);
    }}

    /* Glass Cards */
    .glass-card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 28px;
      box-shadow: 0 20px 45px -15px rgba(0, 0, 0, 0.6);
      transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }}
    .glass-card:hover {{
      border-color: rgba(255, 255, 255, 0.14);
    }}

    /* Typography */
    .hero-title {{
      font-size: 36px;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.15;
      background: linear-gradient(135deg, #ffffff 40%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}

    .slide-subtitle {{
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 22px;
    }}

    .section-tag {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      margin-bottom: 6px;
    }}

    /* Grid Layouts */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 24px;
      align-items: start;
    }}
    .grid-2-even {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      align-items: start;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 18px;
    }}
    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }}

    /* Interactive Diagram Card Container */
    .diagram-container {{
      position: relative;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
    }}
    .diagram-container:hover {{
      border-color: var(--primary);
      box-shadow: 0 12px 35px rgba(56, 189, 248, 0.2);
      transform: translateY(-2px);
    }}
    .diagram-img {{
      width: 100%;
      height: auto;
      max-height: 480px;
      object-fit: contain;
      display: block;
      transition: transform 0.3s ease;
      background: #000;
    }}
    .diagram-container:hover .diagram-img {{
      transform: scale(1.015);
    }}
    .diagram-overlay-badge {{
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #fff;
      padding: 6px 14px;
      border-radius: 30px;
      font-size: 12px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
      pointer-events: none;
    }}

    /* Feature Lists & Specs */
    .spec-item {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 12px;
      transition: background 0.2s ease, border-color 0.2s ease;
    }}
    .spec-item:hover {{
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(255, 255, 255, 0.12);
    }}
    .spec-title {{
      font-size: 14px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .spec-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Table styles */
    .styled-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    .styled-table th {{
      background: rgba(255, 255, 255, 0.05);
      text-align: left;
      padding: 10px 14px;
      font-weight: 700;
      color: var(--primary);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
    }}
    .styled-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: var(--text-muted);
      vertical-align: top;
    }}
    .styled-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
      color: var(--text);
    }}

    /* Roster Cards (Slide 1) */
    .roster-card {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 14px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: all 0.25s ease;
      position: relative;
      overflow: hidden;
    }}
    .roster-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--primary);
      opacity: 0.4;
      transition: opacity 0.2s ease, width 0.2s ease;
    }}
    .roster-card:hover {{
      background: rgba(255, 255, 255, 0.06);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-2px);
    }}
    .roster-card:hover::before {{
      opacity: 1;
      width: 6px;
    }}
    .roster-name {{
      font-size: 14px;
      font-weight: 700;
      color: #fff;
    }}
    .roster-legajo {{
      font-size: 12px;
      color: var(--primary);
      font-family: monospace;
      font-weight: 600;
    }}
    .roster-role {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.35;
      margin-top: 2px;
    }}

    /* Bottom Control Bar */
    footer {{
      height: 72px;
      padding: 0 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--card-border);
      background: rgba(7, 9, 14, 0.92);
      backdrop-filter: blur(16px);
      position: sticky;
      bottom: 0;
      z-index: 50;
    }}

    .nav-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #fff;
      padding: 9px 18px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .nav-btn:hover:not(:disabled) {{
      background: rgba(56, 189, 248, 0.2);
      border-color: var(--primary);
      transform: translateY(-1px);
    }}
    .nav-btn:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}

    .slide-dots {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .dot {{
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .dot.active {{
      background: var(--primary);
      box-shadow: 0 0 10px var(--primary);
      width: 22px;
      border-radius: 6px;
    }}
    .dot:hover:not(.active) {{
      background: rgba(255, 255, 255, 0.45);
    }}

    .counter-text {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      font-variant-numeric: tabular-nums;
    }}

    /* Pan & Zoom Modal */
    .zoom-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(5, 7, 11, 0.95);
      backdrop-filter: blur(20px);
      z-index: 9999;
      display: none;
      flex-direction: column;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}
    .zoom-modal.active {{
      display: flex;
      opacity: 1;
    }}

    .modal-header {{
      height: 60px;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(15, 23, 42, 0.85);
      border-bottom: 1px solid var(--card-border);
    }}
    .modal-title {{
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .modal-toolbar {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .tool-btn {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #fff;
      width: 36px;
      height: 36px;
      border-radius: 8px;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tool-btn:hover {{
      background: var(--primary);
      color: #000;
      border-color: var(--primary);
    }}
    .zoom-display {{
      font-size: 12px;
      font-weight: 700;
      color: var(--primary);
      min-width: 55px;
      text-align: center;
      font-family: monospace;
    }}

    .modal-viewport {{
      flex: 1;
      width: 100%;
      height: calc(100vh - 60px);
      overflow: hidden;
      position: relative;
      cursor: grab;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #111827 0%, #05070c 100%);
    }}
    .modal-viewport.dragging {{
      cursor: grabbing;
    }}
    .zoomable-content {{
      position: absolute;
      transform-origin: center center;
      transition: transform 0.06s linear;
      will-change: transform;
      user-select: none;
    }}
    .zoomable-content img {{
      max-width: 90vw;
      max-height: 85vh;
      object-fit: contain;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
      border-radius: 8px;
      display: block;
      pointer-events: none;
    }}

    .modal-hint {{
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.8);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 12px;
      color: var(--text-muted);
      pointer-events: none;
    }}

    /* Pulse effect */
    @keyframes pulseGlow {{
      0%, 100% {{ box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }}
      50% {{ box-shadow: 0 0 30px rgba(56, 189, 248, 0.45); }}
    }}
    .pulse-glow {{
      animation: pulseGlow 3s infinite ease-in-out;
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header>
    <div class="header-left">
      <div class="inst-badge">UTN FRC &bull; ASI 2K10</div>
      <div class="header-title">Museo de Historia Natural &bull; Grupo 6</div>
    </div>
    <div class="header-right">
      <span class="badge badge-cyan" id="topic-badge">1.1 Introducción</span>
      <button class="btn-icon" onclick="toggleFullscreen()" title="Pantalla Completa (F11)">
        <span>⛶</span> Pantalla Completa
      </button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="progress-bar"></div>
  </div>

  <!-- Main Slides Stage -->
  <main>

    <!-- SLIDE 1: PORTADA & EQUIPO -->
    <div class="slide active" id="slide-1" data-topic="Equipo & Portada">
      <div class="glass-card" style="margin-bottom: 24px;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
          <div>
            <span class="section-tag">Universidad Tecnológica Nacional &bull; Facultad Regional Córdoba</span>
            <h1 class="hero-title">Sistema de Gestión y Vigilancia Museológica</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">
              Análisis y Modelado Integral de Sistemas de Información &bull; Cátedra ASI &bull; Curso 2K10 &bull; Grupo 6
            </p>
          </div>
          <div style="text-align: right;">
            <span class="badge badge-purple" style="font-size: 13px; padding: 6px 14px;">Defensa Oral TPI</span>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;">Ciclo Lectivo 2026</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px; margin-top: 14px; flex-wrap: wrap;">
          <span class="badge badge-cyan">45 Requerimientos Funcionales</span>
          <span class="badge badge-indigo">45 Casos de Uso (1..42 + Sesión)</span>
          <span class="badge badge-emerald">BPMN Descriptivo & Operativo</span>
          <span class="badge badge-amber">CU-15 Registrar Incidente</span>
          <span class="badge badge-rose">Diagrama de Clases del Dominio</span>
        </div>
      </div>

      <!-- 9 Members Grid -->
      <div class="grid-3">
        <div class="roster-card">
          <div class="roster-name">Abad, Francisco</div>
          <div class="roster-legajo">Legajo: 423269</div>
          <div class="roster-role">Dominio bajo estudio y Objetivos estratégicos del Negocio</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Cufre, Agustín</div>
          <div class="roster-legajo">Legajo: 419166</div>
          <div class="roster-role">Mapa de Procesos de Negocio y Clasificación Arquitectónica</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Marcuzzi, Tomas</div>
          <div class="roster-legajo">Legajo: 403382</div>
          <div class="roster-role">Ficha Técnica del Proceso Crítico y Reglas de Negocio (RN1 / RN2)</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Jastrzebski, Emiliano</div>
          <div class="roster-legajo">Legajo: 402760</div>
          <div class="roster-role">Modelado de Procesos BPMN: Nivel Descriptivo y Operativo</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Molina, Tobias</div>
          <div class="roster-legajo">Legajo: 419749</div>
          <div class="roster-role">Especificación de Requerimientos y Trazabilidad N a M</div>
        </div>
        <div class="roster-card" style="border-color: rgba(56, 189, 248, 0.4);">
          <div class="roster-name">Thomas Rapp, Francisco</div>
          <div class="roster-legajo">Legajo: 408990</div>
          <div class="roster-role">Vista Externa: Diagrama de Casos de Uso del Sistema (DCU)</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Moyano, Lucas Uriel</div>
          <div class="roster-legajo">Legajo: 410975</div>
          <div class="roster-role">Caso de Uso Esencial: Plantilla CU-15 Registrar Incidente</div>
        </div>
        <div class="roster-card" style="border-color: rgba(129, 140, 248, 0.4);">
          <div class="roster-name">Tarditti, Juan Sebastián</div>
          <div class="roster-legajo">Legajo: 400212</div>
          <div class="roster-role">Vista Interna: Diagrama de Clases del Dominio y Multiplicidades</div>
        </div>
        <div class="roster-card">
          <div class="roster-name">Pereyra, Kevin</div>
          <div class="roster-legajo">Legajo: 418201</div>
          <div class="roster-role">Prototipo de Interfaz Web Tablet y Trazabilidad Punta a Punta</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide" id="slide-2" data-topic="Dominio & Negocio">
      <div class="glass-card">
        <span class="section-tag">Capítulo 1 &bull; Contexto Organizacional</span>
        <h1 class="hero-title">Dominio bajo Estudio y Objetivos del Negocio</h1>
        <p class="slide-subtitle">Museo Provincial de Historia Natural: Gestión patrimonial, exhibición y custodia activa de obras.</p>

        <div class="grid-2">
          <div>
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Problemática</span> Gestión Fragmentada y Riesgo Patrimonial</div>
              <div class="spec-desc">
                El museo resguarda piezas biológicas, fósiles y obras históricas de altísimo valor. Los métodos tradicionales basados en bitácoras físicas de guardia producían demoras críticas en la comunicación de incidentes de deterioro o caídas, falta de trazabilidad en restauraciones y dificultad para coordinar agendas de guías.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Misión</span> Preservación, Divulgación y Seguridad Activa</div>
              <div class="spec-desc">
                Garantizar la integridad de las colecciones bajo custodia y maximizar la experiencia educativa de los visitantes mediante una operación controlada, ágil y digitalizada.
              </div>
            </div>
          </div>

          <div>
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-purple">Objetivo 1</span> Estandarización de Incidentes en Tiempo Real</div>
              <div class="spec-desc">
                Dotar al personal de vigilancia de herramientas web móviles para tipificar y asentar deterioros de piezas en la sala de forma instantánea.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-amber">Objetivo 2</span> Control de Restauración y Depósito Obligatorio</div>
              <div class="spec-desc">
                Asegurar que toda obra intervenida retorne inexcusablemente a depósito seguro antes de cualquier nueva reubicación o baja formal.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-rose">Objetivo 3</span> Automatización de Rondas y Visitas Guiadas</div>
              <div class="spec-desc">
                Planificar dinámicamente guardias en salas y coordinar agendas de guías especializadas para escuelas y contingentes.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: MAPA DE PROCESOS -->
    <div class="slide" id="slide-3" data-topic="2.2 Mapa de Procesos">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.1 y 2.2 &bull; Vista Externa Organizacional</span>
            <h1 class="hero-title">Mapa de Procesos de Negocio</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Arquitectura de la cadena de valor: Procesos Estratégicos, Clave y de Soporte.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio (Vista Externa)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio (Vista Externa)')">
            <img src="{b64_mapa}" class="diagram-img" alt="Mapa de Procesos">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-purple">Estratégicos</span> Gestión Institucional y Curaduría</div>
              <div class="spec-desc">Planificación de exhibiciones temporales, adquisición de piezas, convenios científicos y relaciones interinstitucionales.</div>
            </div>
            <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.4);">
              <div class="spec-title"><span class="badge badge-cyan">Clave / Esenciales</span> Núcleo Operativo del Museo</div>
              <div class="spec-desc">
                &bull; Gestión y Catalogación de Obras de Arte<br>
                &bull; Planificación y Ejecución de Visitas Guiadas<br>
                &bull; <strong>Rondas de Vigilancia y Gestión de Incidentes (Proceso Crítico Seleccionado)</strong>
              </div>
            </div>
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">De Soporte</span> Apoyo a la Operación</div>
              <div class="spec-desc">Mantenimiento de infraestructura y climatización de salas, administración de personal de guardia, soporte de TI.</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: FICHA TÉCNICA DEL PROCESO & REGLAS -->
    <div class="slide" id="slide-4" data-topic="2.3 Proceso Crítico">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.3 &bull; Ficha Técnica & Reglas de Negocio</span>
            <h1 class="hero-title">Descripción del Proceso Crítico Seleccionado</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Proceso: Realizar Ronda de Vigilancia y Gestión de Incidentes.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_p4', 'Planilla Oficial del Proceso y Reglas de Negocio')">
            <span>📄</span> Ver Planilla Oficial del TPI
          </button>
        </div>

        <div class="grid-2">
          <div>
            <div class="spec-item" style="border-color: rgba(52, 211, 153, 0.35);">
              <div class="spec-title"><span class="badge badge-emerald">Formularios y Registros</span></div>
              <div class="spec-desc">
                &bull; <strong>Formulario / Informe de Ronda:</strong> Registro consolidado de salas recorridas.<br>
                &bull; <strong>Planificación de Ronda:</strong> Hoja de ruta asignada al guardia por turno.<br>
                &bull; <strong>Registro de Incidente:</strong> Acta electrónica con tipificación, pieza y hora.
              </div>
            </div>

            <div class="spec-item" style="border-color: rgba(251, 191, 36, 0.35);">
              <div class="spec-title"><span class="badge badge-amber">Reglas de Negocio Fundamentales</span></div>
              <div class="spec-desc" style="display: flex; flex-direction: column; gap: 8px;">
                <div>
                  <strong style="color: #fff;">RN1: Reingreso Obligatorio a Depósito:</strong><br>
                  Toda obra enviada a restauración, se haya podido reparar con éxito o no, debe ingresar obligatoriamente al depósito del museo antes de definir su destino final o su baja formal.
                </div>
                <div>
                  <strong style="color: #fff;">RN2: Registro Inmediato de Incidente:</strong><br>
                  El guardia debe registrar el incidente de la obra de forma inmediata ante el hallazgo en sala, indicando obligatoriamente los datos exactos del incidente, la pieza y la hora actual.
                </div>
              </div>
            </div>
          </div>

          <div class="diagram-container" onclick="openZoomModal('b64_p4', 'Planilla Oficial del Proceso y Reglas de Negocio')">
            <img src="{b64_p4}" class="diagram-img" style="max-height: 420px;" alt="Planilla Proceso Pág 4">
            <div class="diagram-overlay-badge"><span>📄</span> Ficha Oficial del PDF (Click para ampliar)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="2.5 BPMN Descriptivo">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.5 &bull; Vista Interna Macro</span>
            <h1 class="hero-title">BPMN a Nivel Descriptivo (Nivel 1)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Flujo macro del proceso de vigilancia y respuesta ante novedades.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')">
            <img src="{b64_bpmn_desc}" class="diagram-img" alt="BPMN Descriptivo">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Objetivo Metodológico</span></div>
              <div class="spec-desc">
                Representar la visión de negocio gerencial de punta a punta, identificando los límites de responsabilidad de los actores sin sobrecargar detalles computacionales de compuertas secundarias.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-purple">Carriles de Responsabilidad (Lanes)</span></div>
              <div class="spec-desc">
                &bull; <strong>Encargado de Vigilancia:</strong> Inicia la jornada, consulta la asignación y realiza la inspección física.<br>
                &bull; <strong>Sistema / Servidor:</strong> Valida estados de salas, registra marcas temporales y genera consolidados.<br>
                &bull; <strong>Supervisor:</strong> Recibe el informe diario y audita incidentes pendientes.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Hito de Cierre</span></div>
              <div class="spec-desc">
                Emisión obligatoria del informe de ronda con salas recorridas y bitácora de novedades.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide" id="slide-6" data-topic="2.6 BPMN Operativo">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.6 &bull; Vista Interna Detallada</span>
            <h1 class="hero-title">BPMN a Nivel Operativo (Nivel 2)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Lógica de control, bifurcación XOR y disparo del subproceso de incidentes.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')">
            <img src="{b64_bpmn_oper}" class="diagram-img" alt="BPMN Operativo">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item" style="border-color: rgba(251, 191, 36, 0.4);">
              <div class="spec-title"><span class="badge badge-amber">Compuerta Exclusiva (XOR) &bull; Detección de Incidentes</span></div>
              <div class="spec-desc">
                Durante la ronda, tras inspeccionar la sala, el flujo evalúa la existencia de anomalías:
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Camino del NO (Sin Novedades)</span></div>
              <div class="spec-desc">
                Se registra la sala como 'Sin novedades', se actualiza el contador de salas verificadas y continúa hacia la siguiente sala asignada en la planificación.
              </div>
            </div>

            <div class="spec-item" style="border-color: rgba(244, 63, 94, 0.4);">
              <div class="spec-title"><span class="badge badge-rose">Camino del SÍ (Anomalía Detectada)</span></div>
              <div class="spec-desc">
                La sala pasa a estado 'Observación pendiente', disparándose en forma inmediata el registro de incidente con identificación de pieza y tipo de daño (disparador del Caso de Uso 15).
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 7: REQUERIMIENTOS & TRAZABILIDAD -->
    <div class="slide" id="slide-7" data-topic="2.4 Requerimientos">
      <div class="glass-card">
        <span class="section-tag">Capítulo 2.4 &bull; Ingeniería de Requerimientos</span>
        <h1 class="hero-title">Especificación de Requerimientos & Trazabilidad N a M</h1>
        <p class="slide-subtitle">Consistencia metodológica: Mapeo analítico no 1 a 1 entre necesidades del negocio y casos de uso.</p>

        <div class="grid-2">
          <div>
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Alcance Funcional</span> 45 Requerimientos Funcionales</div>
              <div class="spec-desc">
                Estructurados en subsistemas cohesivos: Administración de Obras, Tipos de Obra, Materiales, Estilos, Salas, Tipos de Incidente, Guías, Visitas Guiadas, Venta de Entradas, Rondas y Auditoría.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-indigo">Requerimientos No Funcionales</span></div>
              <div class="spec-desc">
                &bull; <strong>RNF-1 Usabilidad & Portabilidad Móvil:</strong> El módulo de rondas debe operar fluidamente en tablets táctiles ligeras con tiempos de respuesta bajo 2 segundos.<br>
                &bull; <strong>RNF-2 Seguridad e Integridad:</strong> Bitácora inmutable de incidentes con sellado de tiempo del servidor y bloqueo de edición no autorizada.
              </div>
            </div>
          </div>

          <div>
            <div class="spec-item" style="border-color: rgba(192, 132, 252, 0.4);">
              <div class="spec-title"><span class="badge badge-purple">Defensa de la Trazabilidad N a M</span></div>
              <div class="spec-desc" style="display: flex; flex-direction: column; gap: 8px;">
                <p>
                  <strong>1. No acoplamiento 1-a-1:</strong> Un caso de uso no es un simple requerimiento con otro nombre. Es una transacción completa de extremo a extremo que agrega valor al actor.
                </p>
                <p>
                  <strong>2. Requerimientos agrupados:</strong> RFs complementarios de validación, búsqueda y catálogo se satisfacen dentro de un único caso de uso transaccional (ej: búsqueda de obra integrada en CU-15).
                </p>
                <p>
                  <strong>3. Requerimientos sin caso de uso directo:</strong> Ciertas restricciones de integridad y auditoría son resueltas por la arquitectura del backend sin interacción directa con el usuario final.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 8: DIAGRAMA DE CASOS DE USO -->
    <div class="slide" id="slide-8" data-topic="2.7 Casos de Uso">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.7 &bull; Vista Externa del Software &bull; Francisco Thomas Rapp</span>
            <h1 class="hero-title">Diagrama de Casos de Uso del Sistema (DCU)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Frontera del sistema, 42 casos de uso del dominio continuo y 3 de gestión de sesión.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso Completo (DCU 1..42)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso Completo (DCU 1..42)')">
            <img src="{b64_dcu}" class="diagram-img" alt="Diagrama de Casos de Uso">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Numeración Continua y Consistente</span></div>
              <div class="spec-desc">
                Secuencia estricta 1..42 para las operaciones del negocio y 43..45 para seguridad (Iniciar sesión, Cerrar sesión, Modificar contraseña), garantizando correspondencia con la tabla de objetivos.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-indigo">Casos de Uso Críticos del Proceso</span></div>
              <div class="spec-desc">
                &bull; <strong>CU-13:</strong> Generar planificación de rondas<br>
                &bull; <strong>CU-14:</strong> Consultar planificación de rondas<br>
                &bull; <strong>CU-15:</strong> Registrar incidente (Caso de estudio esencial)<br>
                &bull; <strong>CU-16:</strong> Registrar revisión de la sala
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Frontera del Sistema (System Boundary)</span></div>
              <div class="spec-desc">
                Delimita con exactitud qué componentes residen en la plataforma de software del museo frente a entidades externas y actores humanos.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 9: ARQUITECTURA DE ACTORES Y RELACIONES DCU -->
    <div class="slide" id="slide-9" data-topic="2.7 Relaciones DCU">
      <div class="glass-card">
        <span class="section-tag">Capítulo 2.7 &bull; Análisis de Actores y Relaciones UML &bull; Francisco Thomas Rapp</span>
        <h1 class="hero-title">Arquitectura de Actores & Relaciones en el DCU</h1>
        <p class="slide-subtitle">Fundamentación de roles y modelado formal de dependencias &laquo;extend&raquo; e &laquo;include&raquo;.</p>

        <div class="grid-2">
          <div>
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-purple">Actores Principales del Dominio</span></div>
              <div class="spec-desc">
                &bull; <strong>Responsable de Ingreso de Obras:</strong> Gestiona alta, reingreso y derivación a restauración.<br>
                &bull; <strong>Administrador del Museo:</strong> Programa exposiciones y aprueba bajas patrimoniales.<br>
                &bull; <strong>Responsable de Atención al Cliente:</strong> Venta de entradas y asignación de guías.<br>
                &bull; <strong>Encargado de Vigilancia (EV):</strong> Ejecuta rondas, constata salas y emite reportes de incidente.<br>
                &bull; <strong>Encargado de Supervisión:</strong> Emite informes consolidados y gestiona patrones de seguridad.<br>
                &bull; <strong>Admin del Sistema / Usuario:</strong> Soporte de catálogos y gestión de credenciales.
              </div>
            </div>
          </div>

          <div>
            <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.4);">
              <div class="spec-title"><span class="badge badge-cyan">Relación &laquo;extend&raquo; (Condicional)</span></div>
              <div class="spec-desc">
                <strong>CU-15 Registrar incidente &rarr; CU-16 Registrar revisión de la sala:</strong><br>
                La revisión de sala es el caso de uso base. Solo se extiende a 'Registrar incidente' cuando el guardia constata una anomalía física en alguna pieza. No se ejecuta en todas las revisiones.
              </div>
            </div>

            <div class="spec-item" style="border-color: rgba(52, 211, 153, 0.4);">
              <div class="spec-title"><span class="badge badge-emerald">Relación &laquo;include&raquo; (Mandatoria)</span></div>
              <div class="spec-desc">
                <strong>CU-11 Contratar servicio de guía &rarr; CU-12 Consultar agenda de guías:</strong><br>
                Es técnicamente imposible contratar un servicio de guía sin antes comprobar e incluir obligatoriamente la disponibilidad de agenda del personal calificado.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: PLANTILLA CU-15 REGISTRAR INCIDENTE -->
    <div class="slide" id="slide-10" data-topic="2.8 Plantilla CU-15">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.8 &bull; Especificación Detallada de Caso de Uso &bull; Lucas Moyano</span>
            <h1 class="hero-title">Caso de Uso Esencial: Registrar Incidente (CU-15)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Plantilla formal, cursos normales/alternativos e integridad de datos.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_p13', 'Plantilla Oficial CU-15 (Página 13 del TPI)')">
            <span>📄</span> Ver Plantilla del PDF
          </button>
        </div>

        <div class="grid-2">
          <div style="display: flex; flex-direction: column; gap: 10px;">
            <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.5); background: rgba(56, 189, 248, 0.05);">
              <div class="spec-title"><span class="badge badge-cyan">Consistencia y Requisito de Cátedra &bull; Paso 4 Explícito</span></div>
              <div class="spec-desc" style="color: #fff; font-size: 13.5px; line-height: 1.5;">
                <em>"4. El sistema busca la obra por el código ingresado y muestra sus datos: <strong>título/nombre de la obra, sala asignada y ubicación física dentro de la sala</strong>."</em><br>
                <span style="font-size: 12px; color: var(--text-muted); margin-top: 4px; display: block;">
                  Cumplimiento estricto de la regla de no ambigüedad: se definen con precisión los atributos visualizados por el operador.
                </span>
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Flujo Normal de 14 Pasos</span></div>
              <div class="spec-desc">
                Ingreso de código &rarr; Búsqueda e identificación &rarr; Confirmación de pieza &rarr; Selección de tipo de incidente (Deterioro natural, provocado o caída) &rarr; Revisión final &rarr; Registro con hora de servidor &rarr; Actualización de estado de la obra a <strong>"Inactivo"</strong>.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-amber">Cursos Alternativos</span></div>
              <div class="spec-desc">
                &bull; <strong>A1 (Paso 11):</strong> Cancelación de confirmación final &rarr; Fin sin cambios.<br>
                &bull; <strong>A2 (Paso 4):</strong> Código de pieza no encontrado &rarr; Solicita reingreso.<br>
                &bull; <strong>A3 (Paso 6):</strong> Disconformidad con el objeto mostrado &rarr; Cancelación.
              </div>
            </div>
          </div>

          <div class="diagram-container" onclick="openZoomModal('b64_p13', 'Plantilla Oficial CU-15 (Página 13 del TPI)')">
            <img src="{b64_p13}" class="diagram-img" style="max-height: 440px;" alt="Plantilla Pág 13">
            <div class="diagram-overlay-badge"><span>📄</span> Plantilla Oficial Pág. 13 (Click para ampliar)</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 11: PROTOTIPO DE INTERFAZ -->
    <div class="slide" id="slide-11" data-topic="2.8 Prototipo UI">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.8 &bull; Interfaz de Usuario &bull; Kevin Pereyra</span>
            <h1 class="hero-title">Prototipo de Pantalla: Módulo Web en Tablet</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Diseño ergonómico táctil para el Encargado de Vigilancia en recorrido.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla (Tablet - Reportar Incidente)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla (Tablet - Reportar Incidente)')">
            <img src="{b64_proto}" class="diagram-img" alt="Prototipo Tablet">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Mapeo Pantalla vs Plantilla de Caso de Uso</span></div>
              <div class="spec-desc">
                Cada sección visual del prototipo responde exactamente a los pasos de la especificación:
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-purple">1. Input de Búsqueda</span> (Pasos 2 y 3)</div>
              <div class="spec-desc">Campo táctil de entrada rápida para el código de inventario de la obra.</div>
            </div>

            <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.4);">
              <div class="spec-title"><span class="badge badge-cyan">2. Card de Datos de la Pieza</span> (Paso 4)</div>
              <div class="spec-desc">Despliega de inmediato: <strong>Título de la Obra, Sala Asignada, Ubicación Física y Estado Actual</strong>.</div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-amber">3. Selector y Confirmación</span> (Pasos 7 a 12)</div>
              <div class="spec-desc">Desplegable con tipos de incidentes catalogados, sello automático de hora y botones táctiles de confirmación / cancelación.</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 12: DIAGRAMA DE CLASES DEL DOMINIO -->
    <div class="slide" id="slide-12" data-topic="2.9 Clases del Dominio">
      <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="section-tag">Capítulo 2.9 &bull; Vista Interna Orientada a Objetos &bull; Juan Tarditti</span>
            <h1 class="hero-title">Diagrama de Clases del Dominio (DCD)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Estructura estática, entidades del modelo y encapsulamiento de métodos.</p>
          </div>
          <button class="btn-icon" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio (DCD)')">
            <span>🔍</span> Ampliar / Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="diagram-container" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio (DCD)')">
            <img src="{b64_dcd}" class="diagram-img" alt="Diagrama de Clases">
            <div class="diagram-overlay-badge"><span>🔍</span> Click para interactuar (Pan & Zoom)</div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-cyan">Clases Fundamentales</span></div>
              <div class="spec-desc">
                &bull; <strong>Incidente:</strong> Entidad transaccional con fecha, hora, descripción y estado.<br>
                &bull; <strong>TipoIncidente:</strong> Clasificador tipológico normalizado.<br>
                &bull; <strong>ObraDeArte:</strong> Entidad central con código, título, estado y relaciones.<br>
                &bull; <strong>Sala & Guardia:</strong> Infraestructura física y personal de custodia.
              </div>
            </div>

            <div class="spec-item">
              <div class="spec-title"><span class="badge badge-emerald">Encapsulamiento y Métodos</span></div>
              <div class="spec-desc">
                Operaciones del dominio modeladas: <code>buscarObraPorCodigo()</code>, <code>actualizarEstado("Inactivo")</code>, <code>registrarIncidente()</code>, <code>obtenerDatosUbicacion()</code>.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 13: MULTIPLICIDADES E INTEGRIDAD EN EL DCD -->
    <div class="slide" id="slide-13" data-topic="2.9 Multiplicidades">
      <div class="glass-card">
        <span class="section-tag">Capítulo 2.9 &bull; Análisis de Integridad &bull; Juan Tarditti</span>
        <h1 class="hero-title">Multiplicidades & Consistencia Estructural en el DCD</h1>
        <p class="slide-subtitle">Resolución estricta de las observaciones de cátedra sobre asociaciones del modelo.</p>

        <div class="grid-2-even">
          <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.45);">
            <div class="spec-title"><span class="badge badge-cyan">Corrección 1</span> Incidente &rarr; (1) TipoIncidente</div>
            <div class="spec-desc" style="display: flex; flex-direction: column; gap: 10px; font-size: 13.5px;">
              <p>
                <strong>Multiplicidad Unívoca Obligatoria:</strong><br>
                Todo objeto de la clase <code>Incidente</code> debe estar indefectiblemente vinculado a <strong>exactamente un (1)</strong> <code>TipoIncidente</code> (Deterioro natural, deterioro provocado o caída accidental).
              </p>
              <p style="color: var(--text-muted); font-size: 13px;">
                No se admiten incidentes anónimos o no tipificados. Esto garantiza la integridad referencial requerida para los reportes estadísticos y patrones de supervisión.
              </p>
            </div>
          </div>

          <div class="spec-item" style="border-color: rgba(129, 140, 248, 0.45);">
            <div class="spec-title"><span class="badge badge-indigo">Corrección 2</span> Sala &rarr; (1..*) SalaXGuardia</div>
            <div class="spec-desc" style="display: flex; flex-direction: column; gap: 10px; font-size: 13.5px;">
              <p>
                <strong>Descomposición de la Relación Muchos a Muchos:</strong><br>
                La relación entre <code>Sala</code> y <code>Guardia</code> está intermediada por la clase asociativa <code>SalaXGuardia</code>.
              </p>
              <p style="color: var(--text-muted); font-size: 13px;">
                Una sala registra a lo largo del tiempo <strong>múltiples (1..*) asignaciones</strong> de guardias en turnos distintos, preservando el historial temporal y permitiendo auditar qué guardia custodiaba la sala en el momento exacto del incidente.
              </p>
            </div>
          </div>
        </div>

        <div class="spec-item" style="margin-top: 14px; border-color: rgba(52, 211, 153, 0.3);">
          <div class="spec-title"><span class="badge badge-emerald">Patrón de Cambio de Estado de la Obra</span></div>
          <div class="spec-desc">
            Al registrarse el incidente en el método <code>registrarIncidente()</code>, la clase controladora envía el mensaje <code>setEstado("Inactivo")</code> al objeto <code>ObraDeArte</code>, inhabilitándola para exhibición pública hasta su posterior análisis curatorial o envío a taller de restauración.
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 14: TRAZABILIDAD PUNTA A PUNTA & CIERRE -->
    <div class="slide" id="slide-14" data-topic="Trazabilidad & Cierre">
      <div class="glass-card">
        <span class="section-tag">Síntesis Final &bull; Integridad de Punta a Punta &bull; Grupo 6</span>
        <h1 class="hero-title">Trazabilidad Integral: El Camino del Dato</h1>
        <p class="slide-subtitle">Demostración de la coherencia metodológica total entre todas las etapas del TPI.</p>

        <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; margin-bottom: 22px;">
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">🏢</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--primary);">1. Proceso</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Ronda detecta anomalía</div>
          </div>
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">⚙️</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--accent);">2. BPMN</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">XOR desvía a subproceso</div>
          </div>
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">📋</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--emerald);">3. Requerimiento</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">RF de registro de novedades</div>
          </div>
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">🎯</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--amber);">4. DCU</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">CU-15 extiende CU-16</div>
          </div>
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">📱</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--rose);">5. Pantalla UI</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Tablet: título, sala, ubic.</div>
          </div>
          <div class="spec-item" style="text-align: center; padding: 14px 8px;">
            <div style="font-size: 22px; margin-bottom: 4px;">🧩</div>
            <div style="font-size: 12px; font-weight: 700; color: var(--purple);">6. Dominio DCD</div>
            <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Obra pasa a Inactiva</div>
          </div>
        </div>

        <div class="grid-2-even">
          <div class="spec-item">
            <div class="spec-title"><span class="badge badge-cyan">Conclusiones del Análisis</span></div>
            <div class="spec-desc" style="line-height: 1.5;">
              El modelo logra acoplar rigurosamente la operación física de los guardias con las necesidades gerenciales de auditoría y preservación cultural. Cada elemento analizado responde a una regla de negocio explícita y verificada.
            </div>
          </div>

          <div class="spec-item" style="border-color: rgba(56, 189, 248, 0.4); text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="font-size: 18px; font-weight: 800; color: #fff; margin-bottom: 6px;">¡Muchas Gracias!</div>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px;">Quedamos a disposición de los profesores y del ayudante de cátedra para preguntas.</p>
            <div style="display: flex; gap: 8px;">
              <span class="badge badge-cyan">UTN FRC</span>
              <span class="badge badge-indigo">Curso 2K10</span>
              <span class="badge badge-purple">Grupo 6</span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Bottom Controls Footer -->
  <footer>
    <button class="nav-btn" id="btn-prev" onclick="prevSlide()">
      <span>&larr;</span> Anterior
    </button>

    <div style="display: flex; align-items: center; gap: 16px;">
      <div class="slide-dots" id="dots-container"></div>
      <div class="counter-text" id="slide-counter">Slide 1 de 14</div>
    </div>

    <button class="nav-btn" id="btn-next" onclick="nextSlide()">
      Siguiente <span>&rarr;</span>
    </button>
  </footer>

  <!-- Pan & Zoom Inspector Modal -->
  <div class="zoom-modal" id="zoom-modal">
    <div class="modal-header">
      <div class="modal-title">
        <span class="badge badge-cyan">Visor de Alta Definición</span>
        <span id="modal-diagram-title">Diagrama</span>
      </div>
      <div class="modal-toolbar">
        <button class="tool-btn" onclick="zoomIn()" title="Acercar (Zoom In)">+</button>
        <button class="tool-btn" onclick="zoomOut()" title="Alejar (Zoom Out)">&minus;</button>
        <span class="zoom-display" id="zoom-level">100%</span>
        <button class="tool-btn" onclick="resetZoom()" title="Restablecer Posición">↺</button>
        <button class="tool-btn" onclick="closeZoomModal()" style="color: #f43f5e; font-weight: 800;" title="Cerrar (Esc)">&times;</button>
      </div>
    </div>

    <div class="modal-viewport" id="modal-viewport">
      <div class="zoomable-content" id="zoomable-content">
        <img id="modal-img" src="" alt="Diagrama en Detalle">
      </div>
      <div class="modal-hint">
        💡 Usa la <strong>rueda del mouse</strong> para Zoom &bull; <strong>Arrastra</strong> con el click presionado para Pan &bull; Tecla <strong>Esc</strong> para salir
      </div>
    </div>
  </div>

  <script>
    // Asset Map
    const assets = {{
      b64_mapa: "{b64_mapa}",
      b64_p4: "{b64_p4}",
      b64_bpmn_desc: "{b64_bpmn_desc}",
      b64_bpmn_oper: "{b64_bpmn_oper}",
      b64_dcu: "{b64_dcu}",
      b64_p13: "{b64_p13}",
      b64_proto: "{b64_proto}",
      b64_dcd: "{b64_dcd}"
    }};

    // Slide Management
    let currentSlide = 1;
    const totalSlides = 14;

    function buildDots() {{
      const container = document.getElementById('dots-container');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {{
        const dot = document.createElement('div');
        dot.className = 'dot' + (i === currentSlide ? ' active' : '');
        dot.title = 'Ir al Slide ' + i;
        dot.onclick = () => goToSlide(i);
        container.appendChild(dot);
      }}
    }}

    function updateSlide() {{
      for (let i = 1; i <= totalSlides; i++) {{
        const el = document.getElementById('slide-' + i);
        if (el) {{
          if (i === currentSlide) {{
            el.classList.add('active');
            const topic = el.getAttribute('data-topic') || '';
            document.getElementById('topic-badge').innerText = topic;
          }} else {{
            el.classList.remove('active');
          }}
        }}
      }}

      // Progress bar
      const pct = (currentSlide / totalSlides) * 100;
      document.getElementById('progress-bar').style.width = pct + '%';
      document.getElementById('slide-counter').innerText = 'Slide ' + currentSlide + ' de ' + totalSlides;

      // Buttons
      document.getElementById('btn-prev').disabled = (currentSlide === 1);
      document.getElementById('btn-next').disabled = (currentSlide === totalSlides);

      // Dots
      const dots = document.querySelectorAll('.dot');
      dots.forEach((d, idx) => {{
        if (idx + 1 === currentSlide) {{
          d.classList.add('active');
        }} else {{
          d.classList.remove('active');
        }}
      }});
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        currentSlide++;
        updateSlide();
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        currentSlide--;
        updateSlide();
      }}
    }}

    function goToSlide(n) {{
      if (n >= 1 && n <= totalSlides) {{
        currentSlide = n;
        updateSlide();
      }}
    }}

    // Fullscreen Toggle
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{
          console.log(err);
        }});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // Pan & Zoom Implementation
    let scale = 1;
    let translateX = 0;
    let translateY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    const modal = document.getElementById('zoom-modal');
    const viewport = document.getElementById('modal-viewport');
    const content = document.getElementById('zoomable-content');
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-diagram-title');
    const zoomDisplay = document.getElementById('zoom-level');

    function applyTransform() {{
      content.style.transform = `translate(${{translateX}}px, ${{translateY}}px) scale(${{scale}})`;
      zoomDisplay.innerText = Math.round(scale * 100) + '%';
    }}

    function openZoomModal(assetKey, title) {{
      if (assets[assetKey]) {{
        modalImg.src = assets[assetKey];
        modalTitle.innerText = title;
        modal.classList.add('active');
        resetZoom();
      }}
    }}

    function closeZoomModal() {{
      modal.classList.remove('active');
    }}

    function zoomIn() {{
      scale = Math.min(scale * 1.3, 5);
      applyTransform();
    }}

    function zoomOut() {{
      scale = Math.max(scale / 1.3, 0.4);
      applyTransform();
    }}

    function resetZoom() {{
      scale = 1;
      translateX = 0;
      translateY = 0;
      applyTransform();
    }}

    // Mouse Wheel Zoom
    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY > 0 ? 0.85 : 1.18;
      const newScale = Math.min(Math.max(scale * delta, 0.4), 6);
      scale = newScale;
      applyTransform();
    }}, {{ passive: false }});

    // Drag to Pan
    viewport.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;
      isDragging = true;
      viewport.classList.add('dragging');
      startX = e.clientX - translateX;
      startY = e.clientY - translateY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      translateX = e.clientX - startX;
      translateY = e.clientY - startY;
      applyTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
      viewport.classList.remove('dragging');
    }});

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
      if (modal.classList.contains('active')) {{
        if (e.key === 'Escape') {{
          closeZoomModal();
        }} else if (e.key === '+' || e.key === '=') {{
          zoomIn();
        }} else if (e.key === '-' || e.key === '_') {{
          zoomOut();
        }} else if (e.key === '0' || e.key === 'r' || e.key === 'R') {{
          resetZoom();
        }}
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        goToSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        goToSlide(totalSlides);
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }}
    }});

    // Initialize
    buildDots();
    updateSlide();
  </script>
</body>
</html>
'''

with open("presentacion.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Deluxe presentation written to presentacion.html ({len(html_content)} bytes).")
