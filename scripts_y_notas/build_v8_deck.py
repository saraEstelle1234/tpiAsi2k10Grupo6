# -*- coding: utf-8 -*-
"""
build_v8_deck.py
Builds the final 14-slide presentation deck:
1. Slide 12: Diagrama de Clases (DCD General) enlarged, clean canvas #121212, and UN SOLO CUADRO DE TEXTO explaining the conception & logic (no useless extra cards).
2. Slide 13: Matriz de Trazabilidad COMPLETA (34 requirements mapped to CU & DCD classes, filter pills, search bar, full Dossier).
   (Old Slide 13 "Multiplicidades" is DELETED as requested).
3. Slide 14: Cierre y Agradecimiento ("¡Muchas Gracias!", Grupo 6 TPI ASI, 9 members with legajos, restart button).
4. Total slides = 14 (header counter 01/14, dock counter 01/14, progress bar, overview grid).
5. 9 presenters assigned across the 14 slides (Fran on DCU, Juan on DCD).
"""

import os
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)

    v7_path = os.path.join(base_dir, "generate_v7_deck.py")
    with open(v7_path, "r", encoding="utf-8") as f:
        src = f.read()

    print(f"Loaded v7 generator ({len(src)} bytes)")

    # 1. Update total slides in text from 15 to 14
    src = src.replace('<span class="counter-total">15</span>', '<span class="counter-total">14</span>')
    src = src.replace('style="width: 6.67%;"', 'style="width: 7.14%;"')
    src = src.replace('<div class="dock-counter-badge" id="dock-counter-text">01 / 15</div>', '<div class="dock-counter-badge" id="dock-counter-text">01 / 14</div>')
    src = src.replace('const totalSlides = 15;', 'const totalSlides = 14;')
    src = src.replace('Ver las 15 slides', 'Ver los 14 slides')
    src = src.replace('Ver los 15 slides', 'Ver los 14 slides')

    # Update slideTitles in JavaScript (14 slides)
    old_titles = '''    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Dominio bajo Estudio",
      "03 · Mapa de Procesos",
      "04 · Plantilla de Proceso",
      "05 · BPMN Nivel Descriptivo",
      "06 · BPMN Nivel Operativo",
      "07 · Requerimientos Funcionales",
      "08 · Requerimientos No Funcionales",
      "09 · Diagrama de Casos de Uso",
      "10 · Plantilla de Caso de Uso",
      "11 · Prototipo de Interfaz",
      "12 · Diagrama de Clases",
      "13 · Multiplicidades y Asociaciones",
      "14 · Trazabilidad de Requerimientos",
      "15 · Cierre y Agradecimiento"
    ];'''

    new_titles = '''    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Dominio bajo Estudio",
      "03 · Mapa de Procesos",
      "04 · Plantilla de Proceso",
      "05 · BPMN Nivel Descriptivo",
      "06 · BPMN Nivel Operativo",
      "07 · Requerimientos Funcionales",
      "08 · Requerimientos No Funcionales",
      "09 · Diagrama de Casos de Uso",
      "10 · Plantilla de Caso de Uso",
      "11 · Prototipo de Interfaz",
      "12 · Diagrama de Clases",
      "13 · Trazabilidad de Requerimientos",
      "14 · Cierre y Agradecimiento"
    ];'''

    src = src.replace(old_titles, new_titles)

    # 2. Replace Slides 12, 13, 14, 15 with the new Slides 12, 13, 14
    s12_start = src.find('<!-- SLIDE 12: DIAGRAMA DE CLASES -->')
    dock_start = src.find('<!-- Hotspot trigger zone at bottom')

    if s12_start != -1 and dock_start != -1:
        new_slides_12_to_14 = '''<!-- SLIDE 12: DIAGRAMA DE CLASES -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.55fr 0.45fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">Clases, Atributos, Métodos y Multiplicidades del Dominio</span>
              <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
                Ampliar a pantalla completa {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- UN SOLO CUADRO EXPLICATIVO GENERAL DE LA LÓGICA -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Lógica y Diseño OO</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción y Lógica del Modelo de Dominio</h3>
            
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              El modelo estático plasma la persistencia y la lógica de negocio requerida para la gestión patrimonial y el proceso de vigilancia, estructurando las entidades según directivas de cátedra.
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ciclo del Incidente y Tipificación</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  La clase <code>Incidente</code> captura fecha, hora del servidor y descripción. Se vincula con multiplicidad obligatoria <strong>1</strong> a <code>TipoIncidente</code> y a la <code>Obra</code> afectada.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Transición de Estado de Obra</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Al registrarse el incidente, el método <code>registrarIncidente()</code> en la clase <code>Obra</code> actualiza su puntero hacia <code>Estado</code> a <em>'Inactivo'</em> (Regla de Negocio 2).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Histórico de Rondas (SalaXGuardia)</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  La clase asociativa <code>SalaXGuardia</code> modela la relación 1 a muchos (1..*), preservando la fecha y hora de inspección de cada guardia por cada sala recorrida.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #818CF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">4. Regla de Reingreso Obligatorio</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Sustento de la RN-1: toda obra reparada o no solo egresa de restauración mediante el método <code>registrarReingreso()</code> al depósito del museo.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Visor de Alta Resolución</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Hacé clic en el diagrama para examinar cada clase con zoom de rueda del mouse y desplazamiento panorámico libre.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 13: TRAZABILIDAD COMPLETA (RF <-> CU <-> DCD) -->
    <div class="slide" id="slide-13" data-topic="13 · Trazabilidad de Requerimientos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Matriz completa de correspondencia: Requerimiento Funcional (RF) &rarr; Caso de Uso (CU) &rarr; Diagrama de Clases (DCD)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"/>
            <circle cx="6" cy="12" r="3"/>
            <circle cx="18" cy="19" r="3"/>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
          </svg>
        </div>
      </div>

      <!-- Filter Controls Bar -->
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 12px;">
        <input type="text" id="trace-search-input" class="search-input" placeholder="🔍 Filtrar trazabilidad (ej: RF-35, incidente, obra, sala, ronda, informe)..." oninput="filterTraceMatrix()" style="flex: 1; height: 42px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 8px; padding: 0 16px; color: #FFF; font-size: 13.5px;">
        
        <div class="trace-module-pills" style="margin-bottom: 0; display: flex; gap: 6px;">
          <button class="trace-module-btn active" onclick="filterTraceModule(this, 'ALL')">Todos (34)</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'INCIDENTES')">Incidentes y Rondas</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'OBRAS')">Obras y Depósito</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'MAESTROS')">Salas y Maestros</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'REPORTES')">Informes</button>
        </div>
      </div>

      <!-- Interactive Trace Matrix Console -->
      <div class="trace-matrix-console reveal-item revealed" style="margin-bottom: 0;">
        <!-- Left Column: Scrollable List of All Mapped Requirements -->
        <div style="width: 38%; display: flex; flex-direction: column;">
          <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 8px;">
            Seleccionar Requerimiento Funcional:
          </div>
          <div class="trace-rf-list" id="trace-items-container" style="max-height: 440px; overflow-y: auto; padding-right: 6px;">
            <!-- Dynamically populated / hardcoded items -->
          </div>
        </div>

        <!-- Right Column: Detail Dossier of Selected Trace Link -->
        <div class="trace-impact-dossier" id="trace-dossier-panel" style="width: 62%; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 14px;">
              <div>
                <span style="font-size: 12px; font-weight: 700; color: #93C5FD; text-transform: uppercase;" id="td-rf-code">REQUERIMIENTO FUNCIONAL RF-35</span>
                <div style="font-size: 17px; font-weight: 800; color: #FFF; margin-top: 2px;" id="td-rf-name">Registrar incidente</div>
              </div>
              <span style="font-size: 12px; font-weight: 800; background: var(--blue-accent); color: #FFF; padding: 4px 12px; border-radius: 6px;" id="td-cu-badge">CU-15</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px;">
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #60A5FA; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Caso de Uso Asociado (DCU)</span>
                <span id="td-cu-info" style="color: #FFF; font-weight: 600; font-size: 13.5px;">CU-15: Registrar incidente &bull; Actor: Encargado de vigilancia (EV)</span>
              </div>

              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #38BDF8; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Clases, Atributos y Métodos Afectados (DCD)</span>
                <span id="td-dcd-info" style="color: var(--text-light); line-height: 1.5;">
                  <strong>Clases:</strong> <code>Incidente</code>, <code>TipoIncidente</code>, <code>Obra</code>, <code>Estado</code>.<br>
                  <strong>Método invocado:</strong> <code>obra.registrarIncidente()</code> actualiza puntero a Estado 'Inactivo'.
                </span>
              </div>

              <div style="background: rgba(47,107,255,0.08); border-left: 3px solid var(--blue-accent); padding: 12px 14px; border-radius: 0 8px 8px 0;">
                <span style="color: #93C5FD; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase; margin-bottom: 4px;">Justificación de Trazabilidad y Lógica</span>
                <span id="td-rationale" style="color: var(--text-light); font-size: 12.5px; line-height: 1.55;">
                  El requerimiento exige documentar el daño in situ. El CU-15 materializa la interacción en tablet, y el DCD persiste el hecho en la entidad Incidente vinculada obligatoriamente a TipoIncidente, actualizando en la misma transacción el estado de la obra para su derivación por supervisión.
                </span>
              </div>
            </div>
          </div>

          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 14px; margin-top: 14px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 12px; color: var(--text-light-secondary);">
              Garantía de Integridad: Todo caso de uso implementa al menos un RF y se persiste en entidades del DCD.
            </span>
            <span style="font-size: 11px; font-weight: 700; background: rgba(16,185,129,0.2); color: #6EE7B7; padding: 3px 8px; border-radius: 4px;">TRAZABILIDAD 100%</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 14: CIERRE & AGRADECIMIENTO -->
    <div class="slide" id="slide-14" data-topic="14 · Cierre y Agradecimiento">
      <div class="card-dark" style="margin-bottom: 24px; position: relative; overflow: hidden; padding: 38px 44px; text-align: center;">
        <div style="position: absolute; right: -40px; top: -40px; opacity: 0.08; pointer-events: none;">
          <svg width="340" height="340" viewBox="0 0 200 200" fill="none">
            <circle cx="100" cy="100" r="90" stroke="#2F6BFF" stroke-width="12"/>
            <path d="M40 100 L85 145 L160 65" stroke="#2F6BFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <div class="breadcrumb-tag" style="display: inline-flex; margin-bottom: 12px;">
          {svg_check} Defensa Oral Finalizada &bull; Trabajo Práctico Integrador
        </div>
        <h1 class="giant-title" style="margin-bottom: 8px; font-size: 48px;">¡Muchas Gracias!</h1>
        <p class="editorial-subtitle" style="max-width: 680px; margin: 0 auto 24px auto; font-size: 15px;">
          Sistema de Gestión y Vigilancia Museológica &bull; Grupo 6 &bull; Curso 2K10 &bull; Cátedra de Análisis de Sistemas de Información &bull; UTN - FRC 2026
        </p>

        <div style="display: flex; justify-content: center; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="goToSlide(1)" style="min-height: 48px; padding: 0 24px; font-size: 14px;">
            Volver al inicio ↺
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()" style="min-height: 48px; padding: 0 22px; font-size: 14px;">
            {svg_grid} Ver los 14 slides
          </button>
        </div>
      </div>

      <!-- 9 Members Grid (Balanced 3x3) -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 423269</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Dominio bajo estudio y Objetivos organizacionales</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419166</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Procesos de Negocio y Mapa de Procesos</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 403382</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Proceso y Reglas de Negocio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Jastrzebski, Emiliano</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 402760</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Modelado BPMN a Nivel Descriptivo y Operativo</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419749</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Requerimientos Funcionales y No Funcionales</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 408990</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Casos de Uso</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 410975</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Caso de Uso CU-15 y Prototipo UI</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 400212</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Clases del Dominio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 418201</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Matriz de Trazabilidad Integral y Cierre</div>
        </div>
      </div>
    </div>
'''
        replacement = new_slides_12_to_14 + "\n''')\n\n        # ========================================================\n        # macOS STYLE DOCK CONTAINER (SPRING + FISHEYE)\n        # ========================================================\n        out.write(f'''\n  "
        src = src[:s12_start] + replacement + src[dock_start:]
        print("Slides 12, 13, 14 replaced successfully.")

    # 3. Comprehensive Traceability JavaScript Data & Functions
    trace_matrix_js = '''
    // ========================================================
    // COMPREHENSIVE TRACEABILITY MATRIX (RF <-> CU <-> DCD)
    // ========================================================
    const fullTraceData = [
      {{
        rf: 'RF-01',
        name: 'Registrar ingreso de obra',
        cat: 'OBRAS',
        cu: 'CU-01 Registrar ingreso de obra',
        actor: 'Responsable de ingreso de obra',
        dcd: 'Obra, Autor, Estilo, Material, TipoObra, TipoIngreso',
        methods: 'obra.crear(), autor.asociar(), estilo.vincular()',
        rationale: 'Da de alta la obra en el inventario patrimonial. El CU-01 captura los datos y el DCD persiste la entidad Obra asociada a sus catálogos maestros de clasificación.'
      }},
      {{
        rf: 'RF-02',
        name: 'Consultar obra',
        cat: 'OBRAS',
        cu: 'CU-03 Consultar obra',
        actor: 'Responsable de ingreso, Supervisor',
        dcd: 'Obra, Estado, Sala, Exposicion',
        methods: 'obra.getDatos(), obra.getEstadoActual()',
        rationale: 'Permite consultar la ficha técnica y localización de cualquier obra. En el DCD se materializa mediante las asociaciones de Obra con Estado y Sala.'
      }},
      {{
        rf: 'RF-03',
        name: 'Registrar baja de obra',
        cat: 'OBRAS',
        cu: 'CU-42 Registrar baja de obra',
        actor: 'Admin de sistema, Supervisor',
        dcd: 'Obra, Estado',
        methods: 'obra.darDeBaja(), estado.transicionar("Baja")',
        rationale: 'Formaliza la salida del catálogo de una obra irrecuperable o dada de baja. Actualiza el puntero de Estado en el DCD para auditoría histórica.'
      }},
      {{
        rf: 'RF-04',
        name: 'Registrar tipo de obra',
        cat: 'MAESTROS',
        cu: 'CU-05 / Parámetros Maestros',
        actor: 'Admin de sistema',
        dcd: 'TipoObra',
        methods: 'tipoObra.crear()',
        rationale: 'Parametriza los tipos (escultura, pintura, objeto animado). En el DCD alimenta la clasificación consumida por la entidad Obra.'
      }},
      {{
        rf: 'RF-07',
        name: 'Registrar tipo de material',
        cat: 'MAESTROS',
        cu: 'CU-28 Registrar tipo de material',
        actor: 'Admin de sistema',
        dcd: 'Material',
        methods: 'material.crear()',
        rationale: 'Normaliza los materiales artísticos (óleo, lienzo, bronce). El DCD vincula Material con Obra para calibrar protocolos de conservación.'
      }},
      {{
        rf: 'RF-10',
        name: 'Registrar sala',
        cat: 'MAESTROS',
        cu: 'CU-24 Registrar sala nueva',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.crear()',
        rationale: 'Da de alta espacios de exhibición física. En el DCD la Sala es el contenedor espacial de las Obras y el destino de las Rondas.'
      }},
      {{
        rf: 'RF-11',
        name: 'Consultar sala',
        cat: 'MAESTROS',
        cu: 'CU-27 Consultar salas',
        actor: 'Admin de sistema, Supervisor',
        dcd: 'Sala, Obra',
        methods: 'sala.getObrasExpuestas()',
        rationale: 'Permite inspeccionar la ocupación y obras activas en sala. En el DCD navega la relación Sala-Obra (1 a 1..*).'
      }},
      {{
        rf: 'RF-12',
        name: 'Modificar sala',
        cat: 'MAESTROS',
        cu: 'CU-25 Modificar sala',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.modificarDatos()',
        rationale: 'Actualiza nombre, capacidad o aforo. Modifica los atributos de la entidad Sala en el DCD.'
      }},
      {{
        rf: 'RF-13',
        name: 'Registrar baja de sala',
        cat: 'MAESTROS',
        cu: 'CU-26 Registrar baja de sala',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.darDeBaja()',
        rationale: 'Inhabilita una sala por reformas. Valida que no contenga obras activas antes de persistir la baja en el DCD.'
      }},
      {{
        rf: 'RF-14',
        name: 'Registrar guía',
        cat: 'MAESTROS',
        cu: 'CU-35 Registrar alta de guía',
        actor: 'Admin de sistema',
        dcd: 'Guia',
        methods: 'guia.crear()',
        rationale: 'Incorpora personal al cuerpo de guías. Persiste datos de contacto e idiomas en la entidad Guia del DCD.'
      }},
      {{
        rf: 'RF-15',
        name: 'Consultar guía',
        cat: 'MAESTROS',
        cu: 'CU-38 Consultar guía',
        actor: 'Admin de sistema, Encargado',
        dcd: 'Guia, VisitaGuiada',
        methods: 'guia.getAgenda()',
        rationale: 'Permite revisar la carga horaria y recorridos asignados a un guía en el DCD.'
      }},
      {{
        rf: 'RF-18',
        name: 'Registrar estilo de obra',
        cat: 'MAESTROS',
        cu: 'CU-39 Registrar estilo de obra',
        actor: 'Admin de sistema',
        dcd: 'Estilo',
        methods: 'estilo.crear()',
        rationale: 'Estandariza corrientes históricas (barroco, cubismo, renacentista) asociadas a las Obras en el DCD.'
      }},
      {{
        rf: 'RF-19',
        name: 'Consultar estilo de obra',
        cat: 'MAESTROS',
        cu: 'CU-41 Consultar estilo de obra',
        actor: 'Admin de sistema',
        dcd: 'Estilo',
        methods: 'estilo.listar()',
        rationale: 'Provee el catálogo consumido durante el alta de obras y curaduría de muestras.'
      }},
      {{
        rf: 'RF-21',
        name: 'Registrar tipo de incidente',
        cat: 'MAESTROS',
        cu: 'CU-31 Registrar tipo de incidente',
        actor: 'Admin de sistema',
        dcd: 'TipoIncidente',
        methods: 'tipoIncidente.crear()',
        rationale: 'Define las tipologías de daño (deterioro natural, provocado, caída accidental). En el DCD es mandatorio para Incidente (1 a 1).'
      }},
      {{
        rf: 'RF-22',
        name: 'Consultar tipo de incidente',
        cat: 'MAESTROS',
        cu: 'CU-34 Consultar tipo de incidente',
        actor: 'Admin de sistema, Guardia',
        dcd: 'TipoIncidente',
        methods: 'tipoIncidente.listarActivos()',
        rationale: 'Suministra las opciones mostradas en el selector del formulario táctil del CU-15 en tablet.'
      }},
      {{
        rf: 'RF-24',
        name: 'Registrar programación de exposiciones',
        cat: 'MAESTROS',
        cu: 'CU-05 Registrar programación de exposiciones',
        actor: 'Administrador del museo',
        dcd: 'Exposicion, Obra, Sala',
        methods: 'exposicion.planificar(), obra.asignarSala()',
        rationale: 'Cronograma de muestras artísticas. Asocia obras a salas específicas durante un período determinado en el DCD.'
      }},
      {{
        rf: 'RF-25',
        name: 'Consultar programación de exposiciones',
        cat: 'MAESTROS',
        cu: 'CU-06 Consultar exposiciones',
        actor: 'Administrador del museo, Público',
        dcd: 'Exposicion, Sala',
        methods: 'exposicion.listarVigentes()',
        rationale: 'Permite consultar cartelera y salas asignadas. En el DCD consulta la entidad Exposicion.'
      }},
      {{
        rf: 'RF-26',
        name: 'Registrar planificación de visitas guiadas',
        cat: 'MAESTROS',
        cu: 'CU-08 Registrar planificación de visitas',
        actor: 'Administrador del museo',
        dcd: 'VisitaGuiada, Guia, Sala',
        methods: 'visita.crear(), guia.asignar()',
        rationale: 'Agenda recorridos pedagógicos coordinando guía y salas en el DCD.'
      }},
      {{
        rf: 'RF-27',
        name: 'Consultar planificación de visitas guiadas',
        cat: 'MAESTROS',
        cu: 'CU-07 Consultar visitas guiadas',
        actor: 'Administrador del museo',
        dcd: 'VisitaGuiada',
        methods: 'visita.listarPorFecha()',
        rationale: 'Control de aforo y visitas confirmadas para evitar superposiciones con las rondas de guardia.'
      }},
      {{
        rf: 'RF-28',
        name: 'Consultar agenda de guías',
        cat: 'MAESTROS',
        cu: 'CU-11 Consultar agenda de guías',
        actor: 'Administrador del museo, Guía',
        dcd: 'Guia, VisitaGuiada',
        methods: 'guia.getDisponibilidad()',
        rationale: 'Verifica disponibilidad del personal para asignación de nuevos recorridos en el DCD.'
      }},
      {{
        rf: 'RF-29',
        name: 'Registrar venta de entrada',
        cat: 'MAESTROS',
        cu: 'CU-09 Registrar venta de entrada',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada, Tarifa, Visitante',
        methods: 'entrada.emitir(), tarifa.calcular()',
        rationale: 'Regula el ingreso de público y cobro de tarifas. Persiste la venta en la entidad Entrada del DCD.'
      }},
      {{
        rf: 'RF-30',
        name: 'Contratar servicio adicional de guía',
        cat: 'MAESTROS',
        cu: 'CU-10 Registrar servicio adicional de guía',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada, Guia',
        methods: 'entrada.agregarServicioGuia()',
        rationale: 'Adiciona el guiado profesional a la entrada del visitante en el DCD.'
      }},
      {{
        rf: 'RF-31',
        name: 'Consultar venta de entrada',
        cat: 'MAESTROS',
        cu: 'CU-32 Consultar venta de entrada',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada',
        methods: 'entrada.getDetalle()',
        rationale: 'Auditoría de recaudación y cantidad de personas que ingresaron a las salas del museo.'
      }},
      {{
        rf: 'RF-32',
        name: 'Generar planificación de rondas de vigilancia',
        cat: 'INCIDENTES',
        cu: 'CU-12 Generar planificación de rondas',
        actor: 'Administrador web (Automático)',
        dcd: 'Guardia, Sala, SalaXGuardia',
        methods: 'guardia.asignarRonda(), salaXGuardia.crear()',
        rationale: 'Disparador automático del sistema que programa el cronograma de inspección y genera las instancias de SalaXGuardia en el DCD.'
      }},
      {{
        rf: 'RF-33',
        name: 'Consultar planificación de rondas de vigilancia',
        cat: 'INCIDENTES',
        cu: 'CU-13 Consultar planificación ronda',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'Guardia, SalaXGuardia, Sala',
        methods: 'guardia.getRondasTurno()',
        rationale: 'Permite al guardia consultar en su tablet las salas asignadas para su turno de patrullaje.'
      }},
      {{
        rf: 'RF-34',
        name: 'Registrar revisión de sala',
        cat: 'INCIDENTES',
        cu: 'CU-14 Registrar revisión de la sala',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'SalaXGuardia, Guardia, Sala',
        methods: 'salaXGuardia.marcarVerificada(), salaXGuardia.setFin()',
        rationale: 'Certifica la inspección presencial del guardia en la sala, estampando marca de tiempo en la clase asociativa SalaXGuardia.'
      }},
      {{
        rf: 'RF-35',
        name: 'Registrar incidente',
        cat: 'INCIDENTES',
        cu: 'CU-15 Registrar incidente',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'Incidente, TipoIncidente, Obra, Estado',
        methods: 'incidente.crear(), obra.registrarIncidente(), estado.setInactivo()',
        rationale: 'Núcleo del proceso de soporte (RN-2). El CU-15 persiste la entidad Incidente vinculada obligatoriamente a TipoIncidente y actualiza la Obra a estado Inactivo.'
      }},
      {{
        rf: 'RF-36',
        name: 'Consultar incidentes',
        cat: 'INCIDENTES',
        cu: 'CU-17 Consultar incidente',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra, TipoIncidente',
        methods: 'incidente.listarPendientes(), obra.getHistorial()',
        rationale: 'Permite al supervisor examinar las denuncias cargadas por los guardias para decidir derivación a talleres o bajas.'
      }},
      {{
        rf: 'RF-37',
        name: 'Registrar seguimiento de resolución de incidente',
        cat: 'INCIDENTES',
        cu: 'CU-23 Registrar seguimiento',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra',
        methods: 'incidente.actualizarResolucion()',
        rationale: 'Rastrea el informe de peritaje y los avances de la restauración de piezas afectadas.'
      }},
      {{
        rf: 'RF-40',
        name: 'Registrar obra a restaurar',
        cat: 'OBRAS',
        cu: 'CU-04 Registrar obra a restaurar',
        actor: 'Responsable de ingreso, Supervisor',
        dcd: 'Obra, Estado',
        methods: 'obra.enviarARestauracion(), estado.transicionar("En Restauración")',
        rationale: 'Documenta la salida de la pieza dañada hacia el taller especializado, transicionando su Estado en el DCD.'
      }},
      {{
        rf: 'RF-41',
        name: 'Registrar reingreso de obra al depósito',
        cat: 'OBRAS',
        cu: 'CU-02 Registrar reingreso de obra',
        actor: 'Responsable de ingreso de obra',
        dcd: 'Obra, Estado',
        methods: 'obra.registrarReingreso(), estado.transicionar("En Depósito")',
        rationale: 'Cumplimiento estricto de la Regla de Negocio 1: toda obra reparada debe reingresar indefectiblemente al depósito institucional.'
      }},
      {{
        rf: 'RF-42',
        name: 'Generar informe diario de vigilancia',
        cat: 'REPORTES',
        cu: 'CU-20 Generar informe diario de vigilancia',
        actor: 'Encargado de supervisión, Director',
        dcd: 'Incidente, SalaXGuardia, Guardia',
        methods: 'informe.consolidarTurno()',
        rationale: 'Consolida las rondas concluidas y los incidentes registrados en el día para auditoría directiva.'
      }},
      {{
        rf: 'RF-43',
        name: 'Generar reporte de patrones de incidentes',
        cat: 'REPORTES',
        cu: 'CU-18 Generar patrones de incidentes',
        actor: 'Encargado de supervisión, Director',
        dcd: 'Incidente, TipoIncidente, Sala',
        methods: 'reporte.calcularEstadisticas()',
        rationale: 'Análisis de correlación entre tipologías de incidentes y salas de mayor recurrencia para prevención de daños.'
      }},
      {{
        rf: 'RF-44',
        name: 'Emitir historial de incidentes',
        cat: 'REPORTES',
        cu: 'CU-22 Emitir historial de incidentes',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra',
        methods: 'obra.getHistorialIncidentes()',
        rationale: 'Emite la hoja de vida pericial de una obra, vinculando todos los incidentes sufridos a lo largo de su custodia.'
      }}
    ];

    let currentTraceFilter = 'ALL';

    function renderTraceMatrixItems() {{
      const container = document.getElementById('trace-items-container');
      if (!container) return;
      container.innerHTML = '';

      const query = document.getElementById('trace-search-input')?.value.toLowerCase() || '';

      const filtered = fullTraceData.filter(item => {{
        const matchesCat = (currentTraceFilter === 'ALL' || item.cat === currentTraceFilter);
        const text = (item.rf + ' ' + item.name + ' ' + item.cu + ' ' + item.dcd + ' ' + item.rationale).toLowerCase();
        const matchesQuery = query === '' || text.includes(query);
        return matchesCat && matchesQuery;
      }});

      if (filtered.length === 0) {{
        container.innerHTML = '<div style="color: var(--text-light-secondary); padding: 16px; font-size: 13px;">No se encontraron requerimientos para este filtro.</div>';
        return;
      }}

      filtered.forEach((item, index) => {{
        const div = document.createElement('div');
        div.className = 'trace-rf-item' + (index === 0 ? ' active' : '');
        div.onclick = () => selectTraceDetail(div, item);
        div.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <strong style="color: var(--blue-accent);">${{item.rf}}</strong>
            <span style="font-size: 10.5px; font-weight: 700; background: rgba(47,107,255,0.18); color: #93C5FD; padding: 2px 6px; border-radius: 4px;">${{item.cu.split(' ')[0]}}</span>
          </div>
          <div style="font-size: 12.5px; color: #FFF; margin-top: 3px; font-weight: 600;">${{item.name}}</div>
        `;
        container.appendChild(div);

        if (index === 0) {{
          updateTraceDossier(item);
        }}
      }});
    }}

    function selectTraceDetail(element, item) {{
      document.querySelectorAll('#trace-items-container .trace-rf-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      updateTraceDossier(item);
    }}

    function updateTraceDossier(item) {{
      document.getElementById('td-rf-code').innerText = 'REQUERIMIENTO FUNCIONAL ' + item.rf;
      document.getElementById('td-rf-name').innerText = item.name;
      document.getElementById('td-cu-badge').innerText = item.cu.split(' ')[0];
      document.getElementById('td-cu-info').innerHTML = `<strong>${{item.cu}}</strong> &bull; Actor: ${{item.actor}}`;
      document.getElementById('td-dcd-info').innerHTML = `<strong>Clases DCD:</strong> ${{item.dcd}}<br><strong>Métodos / Lógica:</strong> <code>${{item.methods}}</code>`;
      document.getElementById('td-rationale').innerText = item.rationale;
    }}

    function filterTraceModule(btn, cat) {{
      document.querySelectorAll('.trace-module-pills .trace-module-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTraceFilter = cat;
      renderTraceMatrixItems();
    }}

    function filterTraceMatrix() {{
      renderTraceMatrixItems();
    }}
'''

    # Replace old selectTraceModule in JS with trace_matrix_js
    tm_idx = src.find('// EXPANDED TRACEABILITY MODULES CONTROLLER')
    tm_end = src.find('// ========================================================', tm_idx + 50)
    if tm_idx != -1 and tm_end != -1:
        src = src[:tm_idx] + trace_matrix_js + '\n    ' + src[tm_end:]
        print("Traceability matrix JS replaced successfully.")

    # Call renderTraceMatrixItems() on slide update or view init
    src = src.replace('updateSlide();', 'renderTraceMatrixItems();\n    updateSlide();')

    # Save to generate_v8_deck.py
    v8_gen_path = os.path.join(base_dir, "generate_v8_deck.py")
    with open(v8_gen_path, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"generate_v8_deck.py created successfully ({len(src)} bytes).")

if __name__ == "__main__":
    main()
