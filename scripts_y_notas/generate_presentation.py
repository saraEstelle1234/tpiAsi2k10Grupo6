# -*- coding: utf-8 -*-
"""
Script to generate a presentation HTML file for UTN FRC - ASI 2K10 - Grupo 6
"""
import os
import base64

def get_base64_img(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            ext = path.split('.')[-1]
            return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('ascii')
    return ""

proto_b64 = get_base64_img("media/page13_prototipo.png")
dcd_b64 = get_base64_img("scripts_y_notas/page15_new_dcd.png")
dcu_b64 = get_base64_img("scripts_y_notas/page9_pdf_current.png")
bpmn_b64 = get_base64_img("media/page6_bpmn1.png")

html_code = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Defensa TPI ASI 2K10 - Grupo 6 | Museo de Historia Natural</title>
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: rgba(17, 24, 39, 0.75);
      --card-border: rgba(255, 255, 255, 0.08);
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.25);
      --accent: #818cf8;
      --emerald: #34d399;
      --amber: #fbbf24;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}
    body {{
      background: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #090d16 65%, #05070c 100%);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
    }}
    /* Top Header */
    header {{
      height: 60px;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--card-border);
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-indigo {{ background: rgba(129, 140, 248, 0.15); color: #818cf8; border: 1px solid rgba(129, 140, 248, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }}
    
    /* Progress bar */
    .progress-bar-container {{
      width: 100%;
      height: 3px;
      background: rgba(255, 255, 255, 0.05);
      position: relative;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #a855f7);
      width: 9%;
      transition: width 0.35s ease;
      box-shadow: 0 0 8px rgba(56, 189, 248, 0.6);
    }}

    /* Main Slide Area */
    main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px;
      max-width: 1400px;
      margin: 0 auto;
      width: 100%;
    }}
    .slide {{
      display: none;
      width: 100%;
      animation: fadeIn 0.4s ease forwards;
    }}
    .slide.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .glass-card {{
      background: var(--card-bg);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5);
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
      gap: 16px;
    }}

    h1.hero-title {{
      font-size: 38px;
      font-weight: 800;
      line-height: 1.15;
      background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }}
    h2.slide-title {{
      font-size: 26px;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 6px;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 14px;
      margin-bottom: 20px;
    }}

    /* Speaker Pill */
    .speaker-pill {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(56, 189, 248, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 12px;
      padding: 10px 16px;
      margin-bottom: 20px;
    }}
    .speaker-avatar {{
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: linear-gradient(135deg, #0284c7, #6366f1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 15px;
      color: white;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.4);
    }}
    .speaker-info h4 {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
    }}
    .speaker-info p {{
      font-size: 12px;
      color: var(--primary);
    }}

    /* Speaker Script / Speech Box */
    .speech-box {{
      background: rgba(15, 23, 42, 0.9);
      border-left: 4px solid var(--accent);
      border-radius: 0 12px 12px 0;
      padding: 18px 20px;
      margin-top: 16px;
    }}
    .speech-box-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 8px;
    }}
    .speech-box-text {{
      font-size: 13.5px;
      line-height: 1.6;
      color: #e2e8f0;
      font-style: italic;
    }}

    /* Image zoom container */
    .img-card {{
      background: #020617;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
    }}
    .img-card img {{
      width: 100%;
      height: auto;
      max-height: 520px;
      object-fit: contain;
      cursor: zoom-in;
      transition: transform 0.25s ease;
    }}
    .img-card img:hover {{
      transform: scale(1.02);
    }}
    .img-caption {{
      padding: 8px 14px;
      font-size: 11px;
      color: var(--text-muted);
      border-top: 1px solid var(--card-border);
      width: 100%;
      background: rgba(15, 23, 42, 0.7);
      text-align: center;
    }}

    /* Key-value Cards */
    .kv-card {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 14px 16px;
      margin-bottom: 10px;
    }}
    .kv-card h5 {{
      font-size: 13px;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 4px;
    }}
    .kv-card p {{
      font-size: 12.5px;
      color: #cbd5e1;
      line-height: 1.45;
    }}

    /* Bottom Navigation Bar */
    footer {{
      height: 70px;
      background: rgba(9, 13, 22, 0.95);
      border-top: 1px solid var(--card-border);
      backdrop-filter: blur(16px);
      padding: 0 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      bottom: 0;
      z-index: 50;
    }}
    .nav-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: white;
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--primary);
      color: var(--primary);
      box-shadow: 0 0 12px var(--primary-glow);
    }}
    .nav-btn.primary {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border-color: transparent;
    }}
    .nav-btn.primary:hover {{
      background: linear-gradient(135deg, #38bdf8, #3b82f6);
      color: white;
    }}
    .slide-counter {{
      font-size: 13px;
      font-weight: 700;
      color: var(--text-muted);
      background: rgba(255, 255, 255, 0.04);
      padding: 6px 16px;
      border-radius: 20px;
      border: 1px solid var(--card-border);
    }}

    /* Fullscreen Modal for Diagram Zoom */
    .modal {{
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.92);
      z-index: 999;
      justify-content: center;
      align-items: center;
      padding: 24px;
    }}
    .modal.active {{ display: flex; }}
    .modal img {{
      max-width: 95vw;
      max-height: 92vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 0 40px rgba(56, 189, 248, 0.3);
    }}
    .modal-close {{
      position: absolute;
      top: 20px;
      right: 28px;
      color: white;
      font-size: 32px;
      font-weight: bold;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header>
    <div style="display: flex; align-items: center; gap: 12px;">
      <span class="badge badge-cyan">UTN - FRC</span>
      <span style="font-size: 13px; font-weight: 700; color: #cbd5e1;">ASI 2K10 | Grupo 6</span>
      <span style="font-size: 13px; color: #64748b;">•</span>
      <span style="font-size: 13px; color: #94a3b8;">Museo de Historia Natural</span>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
      <button class="nav-btn" style="padding: 6px 12px; font-size: 12px;" onclick="toggleNotesDrawer()">
        🎙️ Guion General (9 Integrantes)
      </button>
      <button class="nav-btn" style="padding: 6px 12px; font-size: 12px;" onclick="toggleFullscreen()">
        ⛶ Pantalla Completa [F11]
      </button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div id="progressBar" class="progress-bar-fill"></div>
  </div>

  <!-- Main Slides Container -->
  <main>

    <!-- ================= SLIDE 1: PORTADA ================= -->
    <div class="slide active" id="slide-1">
      <div class="glass-card" style="text-align: center; max-width: 1050px; margin: 0 auto; padding: 48px 36px;">
        <div style="display: inline-flex; gap: 8px; margin-bottom: 16px;">
          <span class="badge badge-cyan">Trabajo Práctico Integrador</span>
          <span class="badge badge-indigo">Cátedra Análisis de Sistemas</span>
          <span class="badge badge-emerald">Curso 2K10 — 2026</span>
        </div>
        <h1 class="hero-title" style="font-size: 44px; margin-bottom: 12px;">
          Museo de Historia Natural
        </h1>
        <p style="font-size: 18px; color: var(--primary); font-weight: 600; margin-bottom: 32px;">
          Sistema de Gestión, Vigilancia y Respuesta ante Incidentes de Obras de Arte
        </p>

        <div style="text-align: left; background: rgba(0,0,0,0.3); border: 1px solid var(--card-border); border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">
          <h4 style="font-size: 12px; color: var(--accent); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 14px; font-weight: 700;">
            Distribución de los 9 Integrantes para la Defensa:
          </h4>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; font-size: 12.5px;">
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">1. Francisco Abad</strong> (423269)<br><span style="color: var(--text-muted);">Dominio y Objetivos</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">2. Agustín Cufre</strong> (419166)<br><span style="color: var(--text-muted);">Mapa de Procesos</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">3. Tomas Marcuzzi</strong> (403382)<br><span style="color: var(--text-muted);">Planilla del Proceso</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">4. Emiliano Jastrzebski</strong> (402760)<br><span style="color: var(--text-muted);">BPMN Descriptivo y Operativo</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">5. Tobias Molina</strong> (419749)<br><span style="color: var(--text-muted);">Requerimientos y Trazabilidad</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.3); border-radius: 8px;">
              <strong style="color: #38bdf8;">6. Francisco Thomas Rapp</strong> (408990)<br><span style="color: #e2e8f0; font-weight: 700;">★ Diagrama de Casos de Uso</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">7. Lucas Moyano</strong> (410975)<br><span style="color: var(--text-muted);">Plantilla CU-15 Incidente</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(129,140,248,0.1); border: 1px solid rgba(129,140,248,0.3); border-radius: 8px;">
              <strong style="color: #818cf8;">8. Juan Tarditti</strong> (400212)<br><span style="color: #e2e8f0; font-weight: 700;">★ Diagrama de Clases (DCD)</span>
            </div>
            <div style="padding: 8px 12px; background: rgba(255,255,255,0.02); border-radius: 8px;">
              <strong style="color: #ffffff;">9. Kevin Pereyra</strong> (418201)<br><span style="color: var(--text-muted);">Prototipo y Cierre</span>
            </div>
          </div>
        </div>

        <button class="nav-btn primary" onclick="nextSlide()" style="font-size: 15px; padding: 12px 28px;">
          Comenzar Presentación →
        </button>
      </div>
    </div>

    <!-- ================= SLIDE 2: ORADOR 1 ================= -->
    <div class="slide" id="slide-2">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">FA</div>
          <div class="speaker-info">
            <h4>Orador 1: Francisco Abad (Legajo 423269)</h4>
            <p>Sección 1.1 — Dominio bajo estudio y Objetivos del Negocio</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">1.1 Dominio y Misión del Museo</h2>
            <p class="subtitle">Equilibrio entre la exhibición pública de alto tránsito y la preservación patrimonial de las obras.</p>

            <div class="kv-card">
              <h5>🏛️ Organización bajo estudio</h5>
              <p>Museo de Historia Natural: institución cultural dedicada a exponer obras artísticas de autores locales, nacionales e internacionales al público general mediante el cobro de entradas y servicios de visitas guiadas.</p>
            </div>
            <div class="kv-card">
              <h5>🎯 Objetivo Estratégico General</h5>
              <p>Maximizar el acceso cultural y la recaudación de visitas, asegurando al mismo tiempo la <strong>preservación activa y el control de incidentes</strong> que puedan sufrir las piezas exhibidas en las salas.</p>
            </div>
            <div class="kv-card">
              <h5>⚠️ Problemática Operativa Identificada</h5>
              <p>Las revisiones de seguridad solían ser manuales y reactivas. El sistema de software resuelve la trazabilidad de rondas, el reporte inmediato de anomalías y la gestión técnica del catálogo.</p>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Francisco Abad):</div>
              <p class="speech-box-text">
                "Buenas tardes profesores. Para comenzar, nuestro dominio bajo estudio es el Museo de Historia Natural. La organización tiene como misión exponer colecciones de gran valor artístico e histórico, financiándose a través de la venta de entradas y servicios guiados. Sin embargo, el desafío crítico del negocio es la preservación: diariamente cientos de personas recorren las salas, lo que expone a las piezas a deterioros naturales, caídas accidentales o vandalismo. Nuestro sistema surge para digitalizar la vigilancia, permitiendo planificar rondas preventivas y actuar de inmediato ante cualquier siniestro."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 3: ORADOR 2 ================= -->
    <div class="slide" id="slide-3">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">AC</div>
          <div class="speaker-info">
            <h4>Orador 2: Agustín Cufre (Legajo 419166)</h4>
            <p>Sección 2.1 y 2.2 — Vista Externa: Mapa de Procesos de Negocio</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.1 y 2.2 Mapa de Procesos</h2>
            <p class="subtitle">Estructuración del funcionamiento del museo en tres niveles de procesos.</p>

            <div class="kv-card">
              <h5>1. Procesos Estratégicos (Dirección y Planificación)</h5>
              <p>• Planificar programación de exposiciones temporales.<br>
                 • Planificar visitas guiadas educativas.<br>
                 • Definir tarifas de entrada y aranceles de guías.</p>
            </div>
            <div class="kv-card" style="border-left: 3px solid var(--emerald);">
              <h5>2. Proceso Esencial (Core Business / Cadena de Valor)</h5>
              <p>• <strong>Exponer obras de arte:</strong> es el proceso que interactúa directamente con el visitante, entregando valor cultural y generando la recaudación del museo.</p>
            </div>
            <div class="kv-card" style="border-left: 3px solid var(--amber);">
              <h5>3. Procesos de Soporte (Apoyo Operativo)</h5>
              <p>• Gestionar ingreso y catálogo de obras artísticas.<br>
                 • <strong>Gestionar vigilancia, incidentes y restauración de obras (Proceso foco del TPI).</strong><br>
                 • Administrar Recursos Humanos.</p>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Agustín Cufre):</div>
              <p class="speech-box-text">
                "En el mapa de procesos estructuramos la organización en tres niveles. En el nivel estratégico planificamos las exposiciones y definimos tarifas. En el nivel esencial encontramos el corazón del museo: 'Exponer obras de arte', que es el proceso que recibe al visitante y cobra la entrada. Pero para que este proceso esencial funcione sin riesgos, se apoya en procesos de soporte clave: el ingreso de las obras y, fundamentalmente, 'Gestionar vigilancia, incidentes y restauración'. Este último es el proceso analizado en detalle en este trabajo, ya que garantiza que las salas estén vigiladas y las piezas aseguradas."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 4: ORADOR 3 ================= -->
    <div class="slide" id="slide-4">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">TM</div>
          <div class="speaker-info">
            <h4>Orador 3: Tomas Marcuzzi (Legajo 403382)</h4>
            <p>Sección 2.3 — Planilla del Proceso de Negocio Crítico</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.3 Planilla de Descripción de Proceso</h2>
            <p class="subtitle">Proceso de Soporte: Gestionar incidentes y restauración de obras.</p>

            <div class="grid-2-even" style="margin-bottom: 12px;">
              <div class="kv-card">
                <h5>Cliente del Proceso</h5>
                <p>Proceso Esencial: "Exponer obras de arte" (le asegura piezas en perfecto estado).</p>
              </div>
              <div class="kv-card">
                <h5>Producto del Proceso</h5>
                <p>Informe consolidado de vigilancia con novedades y obras derivadas a restauración.</p>
              </div>
            </div>

            <div class="kv-card">
              <h5>Recursos Humanos y Tecnológicos</h5>
              <p>• <strong>Humanos:</strong> Guardia del Museo / Encargado de vigilancia y Supervisores.<br>
                 • <strong>Tecnológicos:</strong> Módulo Web de Soporte en tablets táctiles y PCs de escritorio.</p>
            </div>

            <div class="kv-card" style="border-left: 3px solid var(--amber);">
              <h5>Reglas de Negocio Clave (RN)</h5>
              <p>• <strong>RN 1 (Reingreso obligatorio a depósito):</strong> Toda obra enviada a restauración debe ingresar obligatoriamente al depósito del museo antes de definir si vuelve a sala o su baja.<br>
                 • <strong>RN 2 (Registro inmediato):</strong> Ante una anomalía, el guardia debe registrar el incidente en el Módulo Web de inmediato durante su ronda.</p>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Tomas Marcuzzi):</div>
              <p class="speech-box-text">
                "Para describir formalmente este proceso de soporte utilizamos la plantilla estándar. Su objetivo es detectar anomalías a través de las rondas para que la supervisión tome medidas preventivas o correctivas. El cliente es el proceso esencial de exposición y el producto es el informe de incidentes con las derivaciones a taller. Destacamos dos reglas de negocio determinantes: la primera exige el registro inmediato del incidente en la tablet para no perder trazabilidad temporal, y la segunda impone que toda obra restaurada pase primero por depósito para certificar su estado antes de volver a exhibirse."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 5: ORADOR 4 ================= -->
    <div class="slide" id="slide-5">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">EJ</div>
          <div class="speaker-info">
            <h4>Orador 4: Emiliano Jastrzebski (Legajo 402760)</h4>
            <p>Sección 2.5 y 2.6 — Vista Interna: Modelado BPMN</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.5 y 2.6 BPMN Descriptivo y Operativo</h2>
            <p class="subtitle">Flujo secuencial de la ronda de vigilancia y compuerta de decisión.</p>

            <div class="kv-card">
              <h5>Secuencia del Flujo Operativo</h5>
              <p><strong>1. Inicio de turno:</strong> El guardia consulta en su tablet la planificación de rondas asignadas para el día.<br>
                 <strong>2. Recorrido físico:</strong> Ingresa a la sala y realiza la inspección visual.<br>
                 <strong>3. Compuerta Exclusiva de Decisión (XOR):</strong><br>
                 • <em>Camino del "NO" (Sin novedades):</em> Registra la sala con estado 'Sin novedades' y avanza a la siguiente sala.<br>
                 • <em>Camino del "SÍ" (Incidente detectado):</em> Registra la sala con 'Observación pendiente' y dispara el subproceso de reporte de incidente.<br>
                 <strong>4. Cierre de jornada:</strong> Se genera el informe consolidado con el mapa de salas recorridas.</p>
            </div>

            <div class="img-card" style="max-height: 200px;">
              <img src="{bpmn_b64}" alt="Diagrama BPMN" onclick="openModal(this.src)">
              <div class="img-caption">Diagrama BPMN (Click para ampliar)</div>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Emiliano Jastrzebski):</div>
              <p class="speech-box-text">
                "En el diagrama BPMN modelamos la vista interna de las rondas. El guardia inicia el flujo consultando el mapa de salas en el Módulo Web. Al ingresar a cada sala realiza la revisión: si todo está en orden, registra la sala 'Sin novedades'. Pero si detecta una anomalía física, el flujo se bifurca en la compuerta exclusiva: marca la sala con 'Observación pendiente' y procede al reporte detallado del incidente, lo que bloquea preventivamente la obra dañada. Al finalizar el recorrido por todas las salas asignadas, el sistema consolida automáticamente el informe diario de vigilancia."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 6: ORADOR 5 ================= -->
    <div class="slide" id="slide-6">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">TM</div>
          <div class="speaker-info">
            <h4>Orador 5: Tobias Molina (Legajo 419749)</h4>
            <p>Sección 2.4 — Especificación de Requerimientos y Trazabilidad</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.4 Requerimientos Funcionales y No Funcionales</h2>
            <p class="subtitle">Estructuración de capacidades del software y concepto de trazabilidad N a M.</p>

            <div class="grid-2-even" style="margin-bottom: 10px;">
              <div class="kv-card">
                <h5>Módulos de Requerimientos (45 RFs)</h5>
                <p>• Obras y Catálogo (RF 1-3)<br>
                   • Tablas Maestras: Material, Salas, Guías, Estilos, Incidentes (RF 4-23)<br>
                   • Exposiciones y Visitas (RF 24-28)<br>
                   • Venta de Entradas (RF 29-31)<br>
                   • Rondas y Vigilancia (RF 32-34)<br>
                   • Gestión de Incidentes (RF 35-37)<br>
                   • Restauración (RF 38-39)<br>
                   • Reportes y Sesión (RF 40-45)</p>
              </div>
              <div class="kv-card">
                <h5>Requerimientos No Funcionales (RNF)</h5>
                <p>• <strong>RNF 1 (Módulo Web):</strong> Arquitectura cliente-servidor accesible desde navegadores modernos sin software en puestos.<br>
                   • <strong>RNF 2 (Interfaz móvil táctil):</strong> Aplicación responsiva y adaptada para tablets, optimizada para rondas de inspección física.</p>
              </div>
            </div>

            <div class="kv-card" style="border-left: 3px solid var(--primary);">
              <h5>💡 Trazabilidad Metodológica: ¿Por qué no es 1 a 1 con Casos de Uso?</h5>
              <p>Un requerimiento de negocio describe el <em>qué</em>; los casos de uso modelan las interacciones observables. Un RF como <em>Generar reporte de patrones</em> se desdobla en 2 CUs (procesamiento y consulta interactiva). A su vez, ciertas tablas maestras o reglas internas no requieren un caso de uso independiente.</p>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Tobias Molina):</div>
              <p class="speech-box-text">
                "A partir de los procesos especificamos 45 requerimientos funcionales agrupados en módulos coherentes y 2 requerimientos no funcionales arquitectónicos. Un aspecto metodológico fundamental es que la relación entre requerimientos y casos de uso no es uno a uno, sino N a M. Por ejemplo, requerimientos de reportes como el informe diario se implementan a través de casos de uso de generación y de consulta; mientras que requerimientos como el registro de incidentes integran en una sola interacción la actualización del estado patrimonial de la pieza."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 7: ORADOR 6 (FRAN) ================= -->
    <div class="slide" id="slide-7">
      <div class="glass-card">
        <div class="speaker-pill" style="border-color: var(--primary); background: rgba(56, 189, 248, 0.12);">
          <div class="speaker-avatar" style="background: linear-gradient(135deg, #0284c7, #38bdf8); color: #020617;">FR</div>
          <div class="speaker-info">
            <h4 style="color: #38bdf8;">Orador 6: Francisco Thomas Rapp (Legajo 408990) — TU TEMA</h4>
            <p style="font-weight: 700; color: #ffffff;">Sección 2.7 — VISTA EXTERNA: DIAGRAMA DE CASOS DE USO (DCU)</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.7 Diagrama de Casos de Uso</h2>
            <p class="subtitle">La vista externa completa del sistema: 8 actores y 42 casos de uso continuos.</p>

            <div class="kv-card">
              <h5>Actores del Sistema</h5>
              <p>• <strong>Responsable de ingreso:</strong> CUs 1 al 4 (Ingreso, reingreso, consulta y derivación a restaurar).<br>
                 • <strong>Administrador del museo:</strong> CUs 5 al 8 (Exposiciones y visitas planificadas).<br>
                 • <strong>Atención al cliente:</strong> CU 9 (Venta entrada), CU 10 (Servicio guía), CU 11 (Agenda guías).<br>
                 • <strong>Administrador web:</strong> CU 12 (Disparo automático de rondas).<br>
                 • <strong>Encargado de vigilancia:</strong> CUs 13 al 17 (Rondas e incidente CU-15).<br>
                 • <strong>Encargado de supervisión:</strong> CUs 18 al 23 (Patrones, informes e historial).<br>
                 • <strong>Admin de sistema:</strong> CUs 24 al 42 (ABMs maestros y CU-42 Baja de obra).<br>
                 • <strong>Usuario:</strong> CUs 43 al 45 (Gestión de sesión).</p>
            </div>

            <div class="kv-card" style="border-left: 3px solid var(--primary);">
              <h5>Relaciones Clave entre Casos de Uso</h5>
              <p>• <strong>&laquo;extend&raquo;:</strong> El CU 15 (<em>Registrar incidente</em>) extiende condicionalmente al CU 14 (<em>Registrar revisión de sala</em>) solo si el guardia detecta una anomalía.<br>
                 • <strong>&laquo;include&raquo;:</strong> La contratación de guía (CU 10) incluye obligatoriamente la verificación de disponibilidad en la agenda de guías (CU 11).</p>
            </div>
          </div>

          <div>
            <div class="img-card" style="margin-bottom: 12px;">
              <img src="{dcu_b64}" alt="Diagrama de Casos de Uso" onclick="openModal(this.src)">
              <div class="img-caption">Diagrama de Casos de Uso (Click para ampliar a pantalla completa)</div>
            </div>

            <div class="speech-box">
              <div class="speech-box-title">🎙️ Tu Guion Verbal para el Zoom (Francisco Thomas Rapp):</div>
              <p class="speech-box-text">
                "Buenas tardes. Como vemos en el Diagrama de Casos de Uso, modelamos la vista externa completa del sistema con 8 actores. El núcleo operativo recae en el Encargado de Vigilancia: mientras realiza la revisión de la sala (Caso de Uso 14), si detecta un desperfecto se dispara la extensión condicional hacia el Caso de Uso 15, 'Registrar incidente'. En el módulo de atención al cliente tenemos la venta de entradas (CU 9), que ante la contratación de guía (CU 10) incluye necesariamente la consulta de agenda (CU 11). Eliminamos el actor Escuela y el envío de invitaciones para enfocar el sistema en la operativa interna, logrando una numeración correlativa del 1 al 42 que se corresponde exactamente con la especificación de objetivos."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 8: ORADOR 7 ================= -->
    <div class="slide" id="slide-8">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">LM</div>
          <div class="speaker-info">
            <h4>Orador 7: Lucas Uriel Moyano (Legajo 410975)</h4>
            <p>Sección 2.8 — Caso de Uso Esencial: Plantilla "Registrar incidente" (CU-15)</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.8 Plantilla del Caso de Uso CU-15</h2>
            <p class="subtitle">Detalle riguroso del flujo: sin frases genéricas y con total integridad de datos.</p>

            <div class="kv-card">
              <h5>Metadatos del Caso de Uso</h5>
              <p>• <strong>ID:</strong> CU-15 | <strong>Actor:</strong> Encargado de vigilancia (EV).<br>
                 • <strong>Precondición:</strong> Guardia autenticado y sala previamente seleccionada en la ronda.</p>
            </div>

            <div class="kv-card" style="border-left: 3px solid var(--primary);">
              <h5>Paso 4 (Ajuste crítico de integridad solicitado por la cátedra):</h5>
              <p><em>"4. El sistema busca la obra por el código ingresado (ej. OBJ-408) y muestra sus datos: <strong>título/nombre de la obra, sala asignada y ubicación física dentro de la sala</strong>."</em><br>
                 Eliminamos la frase genérica 'mostrar datos' especificando exactamente las propiedades de la entidad.</p>
            </div>

            <div class="kv-card">
              <h5>Paso a Paso del Flujo Normal</h5>
              <p>• <strong>Paso 5-6:</strong> Confirmación física de la obra encontrada.<br>
                 • <strong>Paso 7-8:</strong> Selección del tipo de incidente (Deterioro natural, provocado o caída accidental).<br>
                 • <strong>Paso 9:</strong> Consolidación visual del incidente y confirmación final.<br>
                 • <strong>Paso 12-13:</strong> Registro con fecha/hora de servidor y pase de la obra a <strong>estado 'Inactivo'</strong>.</p>
            </div>
          </div>

          <div>
            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Lucas Moyano):</div>
              <p class="speech-box-text">
                "En la plantilla del Caso de Uso 15 documentamos el paso a paso detallado. Siguiendo las directivas de la cátedra sobre integridad, en el Paso 4 prohibimos la frase ambigua 'mostrar datos' y explicitamos que el sistema busca el código OBJ-408 y muestra el título de la obra, la sala asignada y la ubicación física en el muro. Luego el guardia confirma el hallazgo, selecciona la tipología del daño entre las opciones reglamentarias y confirma. El sistema toma la hora automáticamente de los servicios del servidor para que no pueda ser adulterada y transiciona inmediatamente la obra al estado 'Inactivo', evitando que siga constando como disponible en exposición."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 9: ORADOR 8 (JUAN) ================= -->
    <div class="slide" id="slide-9">
      <div class="glass-card">
        <div class="speaker-pill" style="border-color: var(--accent); background: rgba(129, 140, 248, 0.12);">
          <div class="speaker-avatar" style="background: linear-gradient(135deg, #4f46e5, #818cf8);">JT</div>
          <div class="speaker-info">
            <h4 style="color: #818cf8;">Orador 8: Juan Tarditti (Legajo 400212) — TEMA DE JUAN</h4>
            <p style="font-weight: 700; color: #ffffff;">Sección 2.9 — VISTA INTERNA: DIAGRAMA DE CLASES DEL DOMINIO (DCD)</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">2.9 Diagrama de Clases del Dominio</h2>
            <p class="subtitle">Estructura estática de objetos, relaciones, métodos y multiplicidades verificadas.</p>

            <div class="kv-card" style="border-left: 3px solid var(--accent);">
              <h5>Multiplicidades Clave (Observación verificada de cátedra):</h5>
              <p>• <strong>Incidente $\longrightarrow$ (1) TipoIncidente:</strong> Todo incidente clasifica obligatoriamente en un único tipo de incidente.<br>
                 • <strong>Sala $\longrightarrow$ (1..*) SalaXGuardia:</strong> Una sala registra a lo largo del tiempo múltiples revisiones asociadas a los guardias de turno.<br>
                 • <strong>Incidente $\longrightarrow$ (1) Obra / (1) Sala:</strong> Un incidente referencia puntualmente una pieza y una sala física.<br>
                 • <strong>Obra $\longrightarrow$ (1) Estado:</strong> La obra conoce su estado de conservación actual.</p>
            </div>

            <div class="kv-card">
              <h5>Responsabilidades y Métodos de Negocio</h5>
              <p>• <strong>Sala:</strong> <code>buscarObra()</code> y <code>mostrarSala()</code>.<br>
                 • <strong>Incidente:</strong> <code>crear()</code> y <code>registrarIncidente()</code>.<br>
                 • <strong>Obra:</strong> <code>registrarObraInactiva()</code> (delega el cambio a la clase Estado).<br>
                 • <strong>Estado:</strong> <code>esInactivo()</code> y <code>registrarObraInactiva()</code>.</p>
            </div>
          </div>

          <div>
            <div class="img-card" style="margin-bottom: 12px;">
              <img src="{dcd_b64}" alt="Diagrama de Clases" onclick="openModal(this.src)">
              <div class="img-caption">Diagrama de Clases del Dominio (Click para ampliar a pantalla completa)</div>
            </div>

            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Juan Tarditti):</div>
              <p class="speech-box-text">
                "Buenas tardes profesores. En el Diagrama de Clases del Dominio modelamos la arquitectura estática que da soporte al caso de uso de incidentes. Para garantizar la consistencia técnica que nos remarcó la cátedra, aseguramos que la relación entre Incidente y TipoIncidente tenga multiplicidad 1 navegable hacia el tipo, ya que cada novedad pertenece a una única categoría. Asimismo, la relación entre Sala y la clase de asociación SalaXGuardia posee multiplicidad uno a muchos, reflejando el histórico de revisiones de cada guardia. Cuando el guardia confirma el incidente en la UI, el sistema instancia el objeto Incidente invocando sus métodos de creación y llama a registrarObraInactiva() en Obra, la cual actualiza su puntero hacia la instancia de Estado 'Inactivo'."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 10: ORADOR 9 ================= -->
    <div class="slide" id="slide-10">
      <div class="glass-card">
        <div class="speaker-pill">
          <div class="speaker-avatar">KP</div>
          <div class="speaker-info">
            <h4>Orador 9: Kevin Pereyra (Legajo 418201)</h4>
            <p>Sección 2.8 y Cierre — Prototipo de Pantalla y Trazabilidad de Punta a Punta</p>
          </div>
        </div>

        <div class="grid-2">
          <div>
            <h2 class="slide-title">Prototipo de Interfaz y Trazabilidad Integral</h2>
            <p class="subtitle">La interfaz de usuario en la tablet y cómo se valida la integridad de punta a punta.</p>

            <div class="kv-card">
              <h5>Diseño de la Pantalla del Guardia (Tablet)</h5>
              <p>• <strong>Cabecera:</strong> Usuario logueado (Sofia EV), hora de ronda y sala actual preseleccionada.<br>
                 • <strong>Búsqueda:</strong> Input para código <code>OBJ-408</code> con visualización inmediata de nombre <em>La Gioconda</em>, sala y ubicación en muro.<br>
                 • <strong>Detalle:</strong> Radio buttons de tipología y hora bloqueada tomada del reloj del sistema.<br>
                 • <strong>Confirmación:</strong> Tabla final con la pieza, el tipo y el nuevo estado <strong>Inactivo</strong>.</p>
            </div>

            <div class="kv-card" style="border-left: 3px solid var(--emerald);">
              <h5>Conclusión de la Trazabilidad</h5>
              <p>Demostramos cómo una acción del mundo real en el BPMN se convierte en requerimiento funcional, se describe en un caso de uso estandarizado, se plasma en una interfaz táctil y se almacena coherentemente en los objetos del Diagrama de Clases.</p>
            </div>
          </div>

          <div>
            <div class="img-card" style="margin-bottom: 12px;">
              <img src="{proto_b64}" alt="Prototipo de Pantalla" onclick="openModal(this.src)">
              <div class="img-caption">Prototipo de Interfaz Módulo Web (Click para ampliar)</div>
            </div>

            <div class="speech-box">
              <div class="speech-box-title">🎙️ Guion Verbal para el Zoom (Kevin Pereyra):</div>
              <p class="speech-box-text">
                "Para finalizar, diseñamos el prototipo responsivo para la tablet del guardia. Como pueden ver, responde exactamente a la plantilla del caso de uso: al ingresar el código OBJ-408, la tarjeta despliega de inmediato el nombre de la obra, su sala y la ubicación en el muro para que el guardia certifique visualmente la pieza. Al elegir la causa y confirmar el registro, la tabla inferior confirma el nuevo estado 'Inactivo'. De esta manera demostramos la integridad de punta a punta de nuestro TPI: desde la necesidad del negocio, pasando por el proceso BPMN y el caso de uso, hasta la interfaz de usuario y las clases de dominio. Quedamos a disposición de la mesa examinadora para las preguntas."
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ================= SLIDE 11: PREGUNTAS CLAVE ================= -->
    <div class="slide" id="slide-11">
      <div class="glass-card">
        <h2 class="slide-title" style="margin-bottom: 8px;">Defensa Oral: Preguntas Típicas del Ayudante / Docente</h2>
        <p class="subtitle">Respuestas rápidas y seguras para resolver en vivo cualquier pregunta en el Zoom.</p>

        <div class="grid-2-even">
          <div class="kv-card" style="border-left: 3px solid var(--primary);">
            <h5>1. "¿Por qué el caso de uso Registrar Incidente es un &laquo;extend&raquo; y no un &laquo;include&raquo;?"</h5>
            <p><strong>Respuesta de Fran:</strong> Porque la revisión de la sala es la interacción base que se ejecuta siempre en cada ronda. El reporte del incidente es un comportamiento opcional y condicional que solo ocurre si se detecta un daño; si la sala está sin novedades, la revisión finaliza sin extenderse hacia el incidente.</p>
          </div>

          <div class="kv-card" style="border-left: 3px solid var(--accent);">
            <h5>2. "¿Por qué en el DCD Incidente apunta a TipoIncidente con multiplicidad 1?"</h5>
            <p><strong>Respuesta de Juan:</strong> Porque cada incidente puntual pertenece a una única categoría técnica de daño para fines estadísticos. La navegabilidad va desde Incidente hacia TipoIncidente para conocer su descripción, cumpliendo con la multiplicidad (1) que exige la integridad del modelo.</p>
          </div>

          <div class="kv-card" style="border-left: 3px solid var(--emerald);">
            <h5>3. "¿Cómo se asegura que no haya discrepancias entre la pantalla y las clases?"</h5>
            <p><strong>Respuesta de Kevin o Lucas:</strong> Porque cada campo que muestra la interfaz proviene de los métodos getters del DCD: el código, título y ubicación se obtienen mediante <code>buscarObra()</code> y <code>mostrarObra()</code>; la hora es del sistema y el cambio a Inactivo es ejecutado por el método <code>registrarObraInactiva()</code>.</p>
          </div>

          <div class="kv-card" style="border-left: 3px solid var(--amber);">
            <h5>4. "¿Por qué no hay una relación 1 a 1 entre requerimientos y casos de uso?"</h5>
            <p><strong>Respuesta de Tobias:</strong> Porque el requerimiento funcional es la especificación de una necesidad del negocio, mientras que el caso de uso es una interacción observable. Hay requerimientos compuestos que demandan múltiples CUs (como consultas e informes automáticos) y otros que son resueltos por reglas de dominio sin requerir un caso de uso independiente.</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 24px;">
          <span class="badge badge-emerald" style="font-size: 14px; padding: 8px 18px;">
            ✓ Grupo 6 preparado con éxito para la defensa del coloquio
          </span>
        </div>
      </div>
    </div>

  </main>

  <!-- Bottom Navigation Bar -->
  <footer>
    <div style="display: flex; align-items: center; gap: 12px;">
      <button class="nav-btn" onclick="prevSlide()">← Anterior</button>
      <button class="nav-btn" onclick="nextSlide()">Siguiente →</button>
    </div>

    <div class="slide-counter">
      Diapositiva <span id="currentSlideNum">1</span> de <span id="totalSlideNum">11</span>
    </div>

    <div>
      <span style="font-size: 11px; color: #64748b; margin-right: 12px;">Navegación: [←] / [→] / [Barra Espaciadora]</span>
      <button class="nav-btn primary" onclick="goToSlide(1)">⟲ Reiniciar</button>
    </div>
  </footer>

  <!-- Modal for Diagram Zoom -->
  <div class="modal" id="imageModal" onclick="closeModal()">
    <span class="modal-close">&times;</span>
    <img id="modalImg" src="" alt="Ampliación">
  </div>

  <script>
    let currentSlide = 1;
    const totalSlides = 11;

    function updateSlide() {{
      document.querySelectorAll('.slide').forEach((s, idx) => {{
        s.classList.remove('active');
        if (idx + 1 === currentSlide) {{
          s.classList.add('active');
        }}
      }});
      document.getElementById('currentSlideNum').innerText = currentSlide;
      const progressPercent = ((currentSlide) / totalSlides) * 100;
      document.getElementById('progressBar').style.width = progressPercent + '%';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
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
      currentSlide = n;
      updateSlide();
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
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
      }} else if (e.key === 'Escape') {{
        closeModal();
      }}
    }});

    // Modal Image Zoom
    function openModal(src) {{
      const modal = document.getElementById('imageModal');
      const modalImg = document.getElementById('modalImg');
      modalImg.src = src;
      modal.classList.add('active');
    }}

    function closeModal() {{
      const modal = document.getElementById('imageModal');
      modal.classList.remove('active');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => {{}});
      }} else {{
        document.exitFullscreen().catch(err => {{}});
      }}
    }}

    function toggleNotesDrawer() {{
      alert(
        "GUION DE LOS 9 INTEGRANTES:\\n\\n" +
        "1. Francisco Abad: Dominio, misión del museo y problemática de preservación.\\n" +
        "2. Agustín Cufre: Mapa de procesos estratégicos, esenciales y de soporte.\\n" +
        "3. Tomas Marcuzzi: Planilla de procesos, reglas de negocio 1 y 2.\\n" +
        "4. Emiliano Jastrzebski: BPMN, recorrido de rondas y compuerta exclusiva.\\n" +
        "5. Tobias Molina: 45 RFs, 2 RNFs y concepto de trazabilidad N a M.\\n" +
        "6. Francisco Thomas Rapp: VISTA EXTERNA - Diagrama de Casos de Uso completo.\\n" +
        "7. Lucas Moyano: CU-15 Registrar incidente, Paso 4 sin mostrar datos.\\n" +
        "8. Juan Tarditti: VISTA INTERNA - Diagrama de Clases del Dominio y multiplicidades.\\n" +
        "9. Kevin Pereyra: Prototipo tablet, trazabilidad y cierre."
      );
    }}
  </script>
</body>
</html>
"""

with open("presentacion.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Saved presentacion.html successfully! Size:", len(html_code))
