# -*- coding: utf-8 -*-
"""
build_v6_deck.py
Builds the complete, refined 15-slide presentation deck:
1. Pure dark navy aesthetic (#0A1628) with subtle geometric SVGs on all slides.
2. Short, punchy slide titles without filler words.
3. Slide 2: Concise domain & organization description, 3 clean objective cards (01, 02, 03), museum SVG icon.
4. Slide 4: Native HTML table matching media_1794954554615_9e05f515.png (Section 2.3: Gestionar incidentes y restauración).
5. Slide 5: Single unified high-level conception card on the right for BPMN Nivel Descriptivo.
6. Slide 14: Deep explanation of traceability in ASI (definition, N:M relationship, non-CU requirements) and interactive 8-module matrix.
7. Slide 15: NEW closing slide ("¡Muchas Gracias!", Grupo 6, 9 members, restart button).
8. Counters updated to 15 (header, dock, progress bar, overview grid).
"""

import os
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)

    v5_path = os.path.join(base_dir, "generate_v5_pure_navy_deck.py")
    with open(v5_path, "r", encoding="utf-8") as f:
        src = f.read()

    print(f"Loaded v5 source ({len(src)} bytes)")

    # 1. Update total slides in text from 14 to 15
    src = src.replace('<span class="counter-total">14</span>', '<span class="counter-total">15</span>')
    src = src.replace('style="width: 7.14%;"', 'style="width: 6.67%;"')
    src = src.replace('<div class="dock-counter-badge" id="dock-counter-text">01 / 14</div>', '<div class="dock-counter-badge" id="dock-counter-text">01 / 15</div>')
    src = src.replace('const totalSlides = 14;', 'const totalSlides = 15;')
    src = src.replace('Ver los 14 slides', 'Ver los 15 slides')

    # Add custom styles for TPI Table and Traceability Modules
    table_styles = '''
/* ========================================================
   TPI SECTION 2.3 NATIVE TABLE (SLIDE 4)
   ======================================================== */
.tpi-table-container {
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(14, 31, 58, 0.7);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.tpi-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.tpi-table-main-header {
  background: linear-gradient(90deg, #183359 0%, #112440 100%);
  color: #FFFFFF;
  font-size: 15px;
  font-weight: 800;
  padding: 13px 20px;
  border-bottom: 2px solid var(--blue-accent);
  letter-spacing: -0.01em;
}

.tpi-col-label {
  width: 22%;
  padding: 11px 16px;
  font-size: 13px;
  font-weight: 700;
  color: #93C5FD;
  background: rgba(15, 30, 54, 0.9);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-col-content {
  width: 78%;
  padding: 11px 18px;
  font-size: 13px;
  line-height: 1.55;
  color: var(--text-light);
  background: rgba(10, 22, 40, 0.55);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-col-subtable-cell {
  width: 78%;
  padding: 0;
  background: rgba(10, 22, 40, 0.55);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-subtable {
  width: 100%;
  border-collapse: collapse;
}

.tpi-subtable th {
  background: rgba(255, 255, 255, 0.04);
  color: #CBD5E1;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 8px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.tpi-subtable th:last-child {
  border-right: none;
}

.tpi-subtable td {
  padding: 8px 14px;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--text-light);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.tpi-subtable td:last-child {
  border-right: none;
}

.tpi-subtable tr:last-child td {
  border-bottom: none;
}

/* ========================================================
   TRACEABILITY EXPANDED MATRIX (SLIDE 14)
   ======================================================== */
.trace-module-pills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.trace-module-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-light-secondary);
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.trace-module-btn:hover {
  background: rgba(47, 107, 255, 0.15);
  border-color: var(--blue-accent);
  color: #FFF;
}

.trace-module-btn.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFF;
  box-shadow: 0 4px 14px rgba(47, 107, 255, 0.35);
}
'''
    src = src.replace('/* Presets focus bar for DCU & DCD */', table_styles + '\n/* Presets focus bar for DCU & DCD */')

    # Update slideTitles in JavaScript
    old_titles = '''    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Contexto y Objetivos",
      "03 · Mapa de Procesos",
      "04 · Proceso Crítico y Reglas",
      "05 · BPMN Descriptivo",
      "06 · BPMN Operativo",
      "07 · Requerimientos",
      "08 · Casos de Uso",
      "09 · Actores y Relaciones",
      "10 · Plantilla CU-15",
      "11 · Prototipo UI",
      "12 · Clases del Dominio",
      "13 · Multiplicidades",
      "14 · Trazabilidad y Cierre"
    ];'''

    new_titles = '''    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Dominio bajo Estudio",
      "03 · Mapa de Procesos",
      "04 · Plantilla de Proceso",
      "05 · BPMN Nivel Descriptivo",
      "06 · BPMN Nivel Operativo",
      "07 · Requerimientos del Sistema",
      "08 · Diagrama de Casos de Uso",
      "09 · Actores y Casos de Uso",
      "10 · Plantilla de Caso de Uso",
      "11 · Prototipo de Interfaz",
      "12 · Diagrama de Clases",
      "13 · Multiplicidades y Asociaciones",
      "14 · Trazabilidad de Requerimientos",
      "15 · Cierre y Agradecimiento"
    ];'''
    src = src.replace(old_titles, new_titles)

    # 2. Update titles across all slides to make them direct and clean:
    # Slide 2: Dominio bajo Estudio
    s2_old_header = '''      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">02 &bull; Dominio bajo Estudio y Objetivos</div>
          <h1 class="giant-title">Dominio bajo Estudio y Objetivos de la Organización</h1>
          <p class="editorial-subtitle">
            Caso de Estudio: Museo de Historia Natural &bull; Sección 1.1 del Trabajo Práctico Integrador
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_museum_arch}
        </div>
      </div>'''

    s2_new_header = '''      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">02 &bull; Dominio y Objetivos</div>
          <h1 class="giant-title">Dominio bajo Estudio</h1>
          <p class="editorial-subtitle">
            Museo de Historia Natural &bull; Contexto institucional y objetivos de la organización
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_museum_arch}
        </div>
      </div>'''
    src = src.replace(s2_old_header, s2_new_header)
    src = src.replace('data-topic="02 · Contexto y Objetivos"', 'data-topic="02 · Dominio y Objetivos"')

    # Slide 3: Mapa de Procesos
    src = src.replace('<div class="breadcrumb-tag">03 &bull; Cadena de Valor del Museo</div>', '<div class="breadcrumb-tag">03 &bull; Procesos de Negocio</div>')
    src = src.replace('<h1 class="giant-title">Mapa de Procesos: Cadena de Valor del Museo</h1>', '<h1 class="giant-title">Mapa de Procesos</h1>')
    src = src.replace('Clasificación estratégica formal de los procesos de negocio de la organización (Sección 2.1 del TPI)', 'Estructura de la cadena de valor de la organización (Sección 2.1 del TPI)')
    src = src.replace('data-topic="03 · Mapa de Procesos"', 'data-topic="03 · Mapa de Procesos"')

    # Slide 4: Plantilla de Proceso - Complete replacement of Slide 4 HTML
    s4_start = src.find('<!-- SLIDE 4: PROCESO CRÍTICO & REGLAS -->')
    s5_start = src.find('<!-- SLIDE 5: BPMN DESCRIPTIVO -->')
    
    if s4_start != -1 and s5_start != -1:
        s4_new_html = '''<!-- SLIDE 4: PLANTILLA DE PROCESO -->
    <div class="slide" id="slide-4" data-topic="04 · Plantilla de Proceso">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">04 &bull; Proceso de Soporte</div>
          <h1 class="giant-title">Plantilla de Proceso</h1>
          <p class="editorial-subtitle">
            Proceso de Negocio: Gestionar incidentes y restauración de obras (Sección 2.3 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_rules_gear}
        </div>
      </div>

      <div class="tpi-table-container reveal-item revealed">
        <table class="tpi-table">
          <thead>
            <tr>
              <th colspan="2" class="tpi-table-main-header">
                Proceso de Negocio: Gestionar incidentes y restauración de obras
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="tpi-col-label">Objetivo</td>
              <td class="tpi-col-content">
                Gestionar incidentes y restauración de obras mediante las rondas de vigilancia realizadas por el guardia, registrando los incidentes en el Módulo Web para que los supervisores tomen medidas en relación a la obra, envío a restauración, registro de baja de obra, etc.
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Cliente del Proceso</td>
              <td class="tpi-col-content">
                Proceso: “Exponer obras de artes” (esencial).
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Producto del Proceso</td>
              <td class="tpi-col-content">
                Informe generado con todos los incidentes ocurridos, y obra enviada a reparación.
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Proveedores del proceso e insumos que brinda cada uno</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Proveedor</th>
                      <th style="width: 50%;">Insumo</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Proceso: Gestionar ingreso de obras artísticas.</td>
                      <td>Obra dañada</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Obra registrada en Módulo Web</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Recursos del proceso</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Recursos Humanos</th>
                      <th style="width: 50%;">Recursos Tecnológicos - Hardware</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Guardia del Museo</td>
                      <td>Modulo Web de Soporte</td>
                    </tr>
                    <tr>
                      <td>Supervisor</td>
                      <td>PC</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Formularios, registros e información del proceso</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Formularios</th>
                      <th style="width: 50%;">Registros e información</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Informe</td>
                      <td>Incidente</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Informe</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Planificación de ronda de vigilancia</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Reglas de Negocio</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 8%;">ID</th>
                      <th style="width: 32%;">Regla de negocio</th>
                      <th style="width: 60%;">Descripción</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">1.</td>
                      <td style="font-weight: 600; color: #FFF;">Reingreso obligatorio a deposito</td>
                      <td>Toda obra enviada a restauración, se haya podido reparar con exito o no, debe ingresar obligatoriamente al depósito del museo antes de definir su destino final o su baja</td>
                    </tr>
                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">2.</td>
                      <td style="font-weight: 600; color: #FFF;">Registro inmediato de incidente</td>
                      <td>El guardia debe registrar el incidente de la obra de forma inmediata, indicando detalles del incidente.</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
'''
        src = src[:s4_start] + s4_new_html + src[s5_start:]
        print("Slide 4 replaced successfully.")

    # Slide 5: BPMN Nivel Descriptivo - Replace right column with a single clear text card
    s5_start = src.find('<!-- SLIDE 5: BPMN DESCRIPTIVO -->')
    s6_start = src.find('<!-- SLIDE 6: BPMN OPERATIVO -->')
    if s5_start != -1 and s6_start != -1:
        s5_new_html = '''<!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="display: flex; flex-direction: column;">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1" style="flex: 1; object-fit: contain;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; Vista General</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Nivel 1 &bull; Alcance de Negocio</div>
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción del Modelo Descriptivo</h3>
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              Modela el flujo global de negocio de punta a punta entre los actores clave: <strong>Guardia del Museo</strong>, <strong>Módulo Web</strong> y <strong>Supervisor</strong>, prescindiendo del detalle de software para brindar una perspectiva ejecutiva del proceso de vigilancia y respuesta.
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ronda y Verificación Física</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia recorre las salas asignadas según la planificación y constata visualmente el estado de las obras expuestas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Detección y Registro Inmediato</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Al detectar cualquier anomalía, el guardia accede al Módulo Web y registra el incidente en el momento exacto (Regla de Negocio 2).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Evaluación y Decisión del Supervisor</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El supervisor analiza el incidente consolidado en el sistema y define el curso de acción: traslado a restauración externa o baja de la obra.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Regla Fundamental de Integridad</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Toda obra restaurada reingresa obligatoriamente al depósito del museo antes de definir cualquier nuevo destino o exhibición (RN-1).
            </div>
          </div>
        </div>
      </div>
    </div>
'''
        src = src[:s5_start] + s5_new_html + src[s6_start:]
        print("Slide 5 replaced successfully.")

    # Slide 6: BPMN Nivel Operativo titles
    src = src.replace('<div class="breadcrumb-tag">06 &bull; Modelado BPMN Nivel 2 Operativo</div>', '<div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>')
    src = src.replace('<h1 class="giant-title">Modelado BPMN Nivel 2: Detalle Operativo</h1>', '<h1 class="giant-title">BPMN Nivel Operativo</h1>')
    src = src.replace('Orquestación técnica detallada con compuertas exclusivas, eventos de temporización y tareas automatizadas (Sección 2.6)', 'Detalle de ejecución técnica, eventos de temporización y compuertas del sistema (Sección 2.6 del TPI)')
    src = src.replace('data-topic="06 · BPMN Operativo"', 'data-topic="06 · BPMN Operativo"')

    # Slide 7: Requerimientos titles
    src = src.replace('<div class="breadcrumb-tag">07 &bull; Requerimientos Funcionales y No Funcionales</div>', '<div class="breadcrumb-tag">07 &bull; Requerimientos</div>')
    src = src.replace('<h1 class="giant-title">Especificación de Requerimientos y Trazabilidad</h1>', '<h1 class="giant-title">Requerimientos del Sistema</h1>')
    src = src.replace('Catálogo completo de requerimientos funcionales estructurados por módulo y restricciones de calidad (Sección 2.4)', 'Requerimientos Funcionales y No Funcionales del sistema (Sección 2.4 del TPI)')
    src = src.replace('data-topic="07 · Requerimientos"', 'data-topic="07 · Requerimientos"')

    # Slide 8: Casos de Uso titles
    src = src.replace('<div class="breadcrumb-tag">08 &bull; Diagrama de Casos de Uso del Sistema</div>', '<div class="breadcrumb-tag">08 &bull; Casos de Uso</div>')
    src = src.replace('<h1 class="giant-title">Diagrama de Casos de Uso (DCU General)</h1>', '<h1 class="giant-title">Diagrama de Casos de Uso</h1>')
    src = src.replace('Vista panorámica de los 42 Casos de Uso y límites del sistema de gestión y vigilancia (Sección 2.7)', 'Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)')
    src = src.replace('data-topic="08 · Casos de Uso"', 'data-topic="08 · Casos de Uso"')

    # Slide 9: Actores titles
    src = src.replace('<div class="breadcrumb-tag">09 &bull; Actores Principales y Paquetes de Casos de Uso</div>', '<div class="breadcrumb-tag">09 &bull; Casos de Uso</div>')
    src = src.replace('<h1 class="giant-title">Arquitectura de Actores y Dependencias UML</h1>', '<h1 class="giant-title">Actores y Casos de Uso</h1>')
    src = src.replace('Distribución de responsabilidades y relaciones en el modelo de Casos de Uso (Sección 2.7)', 'Distribución de responsabilidades y límites del sistema (Sección 2.7 del TPI)')
    src = src.replace('data-topic="09 · Actores y Relaciones"', 'data-topic="09 · Actores y Casos de Uso"')

    # Slide 10: Plantilla CU-15 titles
    src = src.replace('<div class="breadcrumb-tag">10 &bull; Especificación Formal de Caso de Uso</div>', '<div class="breadcrumb-tag">10 &bull; Especificación</div>')
    src = src.replace('<h1 class="giant-title">Caso de Uso: Registrar Incidente (CU-15)</h1>', '<h1 class="giant-title">Plantilla de Caso de Uso</h1>')
    src = src.replace('Especificación detallada paso a paso del flujo principal y alternativos del CU-15 (Sección 2.8)', 'CU-15: Registrar Incidente de Obra (Sección 2.8 del TPI)')
    src = src.replace('data-topic="10 · Plantilla Registrar Incidente"', 'data-topic="10 · Plantilla de Caso de Uso"')

    # Slide 11: Prototipo titles
    src = src.replace('<div class="breadcrumb-tag">11 &bull; Prototipo de Interfaz de Usuario</div>', '<div class="breadcrumb-tag">11 &bull; Prototipo UI</div>')
    src = src.replace('<h1 class="giant-title">Prototipo de Pantalla: Registrar Incidente</h1>', '<h1 class="giant-title">Prototipo de Interfaz</h1>')
    src = src.replace('Diseño de interfaz para terminal tablet del guardia durante la ronda de vigilancia (Sección 2.9)', 'Pantalla de registro de incidente en tablet para guardia (Sección 2.9 del TPI)')
    src = src.replace('data-topic="11 · Prototipo UI"', 'data-topic="11 · Prototipo de Interfaz"')

    # Slide 12: Diagrama de Clases titles
    src = src.replace('<h1 class="giant-title">Diagrama de Clases del Dominio (DCD General)</h1>', '<h1 class="giant-title">Diagrama de Clases</h1>')
    src = src.replace('<div class="breadcrumb-tag">12 &bull; Vista Interna Orientada a Objetos</div>', '<div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>')
    src = src.replace('Modelo de Dominio para el caso de uso Registrar Incidente (Sección 2.9 del TPI)', 'Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)')
    src = src.replace('data-topic="12 · Diagrama de Clases del Dominio"', 'data-topic="12 · Diagrama de Clases"')

    # Slide 13: Multiplicidades titles
    src = src.replace('<h1 class="giant-title">Multiplicidades y Reglas Estructurales del DCD</h1>', '<h1 class="giant-title">Multiplicidades y Asociaciones</h1>')
    src = src.replace('<div class="breadcrumb-tag">13 &bull; Multiplicidades y Reglas de Integridad del Dominio</div>', '<div class="breadcrumb-tag">13 &bull; Modelo de Dominio</div>')
    src = src.replace('Garantía de consistencia de datos y acoplamiento según directivas de cátedra (Sección 2.9 del TPI)', 'Relaciones estructurales, multiplicidades y reglas del dominio (Sección 2.10 del TPI)')
    src = src.replace('data-topic="13 · Multiplicidades e Integridad"', 'data-topic="13 · Multiplicidades y Asociaciones"')

    # Slide 14: Traceability & Slide 15: Cierre & Agradecimiento
    s14_start = src.find('<!-- SLIDE 14: TRAZABILIDAD & CIERRE -->')
    dock_start = src.find('<!-- Hotspot trigger zone at bottom', s14_start)

    if s14_start != -1 and dock_start != -1:
        s14_and_15_html = '''<!-- SLIDE 14: TRAZABILIDAD -->
    <div class="slide" id="slide-14" data-topic="14 · Trazabilidad">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">14 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Mapeo integral: Reglas de Negocio &rarr; BPMN &rarr; Requerimientos &rarr; Casos de Uso &rarr; Clases del Dominio
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

      <!-- Conceptual Explanation of Traceability in ASI -->
      <div class="card-dark reveal-item revealed" style="margin-bottom: 20px; padding: 22px 26px; border-left: 4px solid var(--blue-accent);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-size: 15px; font-weight: 800; color: #FFF;">El Concepto de Trazabilidad en Análisis de Sistemas</span>
          <span style="font-size: 11px; font-weight: 700; background: rgba(47,107,255,0.18); color: #93C5FD; padding: 4px 10px; border-radius: 999px;">FUNDAMENTO METODOLÓGICO</span>
        </div>
        <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
          La <strong>trazabilidad</strong> es la propiedad que permite relacionar bidireccionalmente cada elemento del sistema de información con los objetivos de negocio que le dieron origen (<em>forward & backward traceability</em>).
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 12px; font-size: 13px; line-height: 1.5; color: var(--text-light-secondary);">
          <div style="background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px;">
            <strong style="color: #FFF;">Relación N a M (Muchos a Muchos):</strong> Un requerimiento puede materializarse en múltiples casos de uso (ej. gestión de obras dividida en alta, consulta, reparación y baja), mientras que un caso de uso complejo puede dar cumplimiento simultáneo a varios requerimientos funcionales (ej. CU-15 registra el hecho, captura fecha/hora y asocia la obra).
          </div>
          <div style="background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px;">
            <strong style="color: #FFF;">Requerimientos sin Caso de Uso interactivo:</strong> Ciertos requerimientos no originan un CU con actor porque corresponden a <em>reglas de dominio/integridad referencial</em> garantizadas directamente en el Diagrama de Clases (ej. RN-1 reingreso a depósito), o a <em>requerimientos no funcionales transversales</em> (seguridad, rendimiento).
          </div>
        </div>
      </div>

      <!-- Interactive 8-Module Trace Matrix -->
      <div class="trace-matrix-console reveal-item revealed">
        <div style="width: 32%;">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 10px;">Seleccionar Módulo del Sistema:</div>
          <div class="trace-rf-list" style="max-height: 380px; overflow-y: auto;">
            <div class="trace-rf-item active" onclick="selectTraceModule(this, 'mod-incidentes')">
              <strong>Módulo 6</strong> &bull; Gestión de Incidentes
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-rondas')">
              <strong>Módulo 5</strong> &bull; Planificación y Rondas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-obras')">
              <strong>Módulo 1</strong> &bull; Obras y Catálogo
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-maestros')">
              <strong>Módulo 2</strong> &bull; Parámetros Maestros
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-exposiciones')">
              <strong>Módulo 3</strong> &bull; Exposiciones y Visitas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-entradas')">
              <strong>Módulo 4</strong> &bull; Venta de Entradas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-informes')">
              <strong>Módulo 7</strong> &bull; Informes y Reportes
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-seguridad')">
              <strong>Módulo 8</strong> &bull; Seguridad y Reglas de Negocio
            </div>
          </div>
        </div>

        <div class="trace-impact-dossier" id="trace-dossier-content" style="width: 68%;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 14px;">
            <span style="font-size: 16px; font-weight: 800; color: #FFF;" id="trace-mod-title">Módulo 6: Gestión de Incidentes</span>
            <span style="font-size: 11px; font-weight: 700; background: var(--blue-accent); color: #FFF; padding: 4px 10px; border-radius: 4px;" id="trace-mod-badge">PROCESO DE SOPORTE CRÍTICO</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13.5px;">
            <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Requerimientos Funcionales Incluidos</span>
              <span id="trace-rfs" style="color: var(--text-light); line-height: 1.5; margin-top: 4px; display: block;">
                <strong>RF-37:</strong> Registrar incidente &bull; <strong>RF-38:</strong> Consultar incidentes &bull; <strong>RF-39:</strong> Registrar seguimiento de resolución de incidente.
              </span>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #60A5FA; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Casos de Uso Asociados</span>
                <span id="trace-cus" style="color: #FFF; font-weight: 600; line-height: 1.5; margin-top: 4px; display: block;">
                  CU-15 Registrar incidente<br>CU-17 Consultar incidente<br>CU-23 Registrar seguimiento
                </span>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #38BDF8; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Actores y Clases DCD</span>
                <span id="trace-actors" style="color: var(--text-light); line-height: 1.5; margin-top: 4px; display: block;">
                  <strong>Actores:</strong> Guardia del Museo, Supervisor.<br><strong>Clases:</strong> Incidente, TipoIncidente, Obra, Guardia, Supervisor.
                </span>
              </div>
            </div>

            <div style="background: rgba(47,107,255,0.08); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
              <span style="color: #93C5FD; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Justificación Analítica de Trazabilidad</span>
              <span id="trace-rationale" style="color: var(--text-light); font-size: 12.5px; line-height: 1.5; margin-top: 4px; display: block;">
                Conexión directa con la Regla de Negocio 2 (inmediatez de registro) y la compuerta de anomalía del BPMN Operativo. El CU-15 materializa en pantalla táctil la captura del daño, garantizando que el incidente quede disponible al supervisor para la toma de medidas.
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 15: CIERRE & AGRADECIMIENTO -->
    <div class="slide" id="slide-15" data-topic="15 · Cierre y Agradecimiento">
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
            {svg_grid} Ver las 15 slides
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
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Caso de Uso: Registrar Incidente</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 400212</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Clases del Dominio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 418201</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Prototipo de Interfaz y Trazabilidad de Requerimientos</div>
        </div>
      </div>
    </div>
'''
        # In src, find from s14_start to dock_start
        # dock_start points to '<!-- Hotspot trigger zone at bottom'
        # preceding dock_start is "out.write(f'''\n  "
        # Let's find out where out.write(f''' is right before dock_start
        last_out_write = src.rfind("out.write(f'''", s14_start, dock_start)
        replacement = s14_and_15_html + "\n''')\n\n        # ========================================================\n        # macOS STYLE DOCK CONTAINER (SPRING + FISHEYE)\n        # ========================================================\n        out.write(f'''\n  "
        src = src[:s14_start] + replacement + src[dock_start:]
        print("Slide 14 and Slide 15 stitched successfully.")

    # JavaScript Traceability Modules Data with escaped double braces for Python f-string
    js_trace_code = '''
    // ========================================================
    // EXPANDED TRACEABILITY MODULES CONTROLLER
    // ========================================================
    const traceModulesData = {{
      'mod-incidentes': {{
        title: 'Módulo 6: Gestión de Incidentes',
        badge: 'PROCESO DE SOPORTE CRÍTICO',
        rfs: '<strong>RF-37:</strong> Registrar incidente &bull; <strong>RF-38:</strong> Consultar incidentes &bull; <strong>RF-39:</strong> Registrar seguimiento de resolución de incidente.',
        cus: 'CU-15 Registrar incidente<br>CU-17 Consultar incidente<br>CU-23 Registrar seguimiento de resolución',
        actors: '<strong>Actores:</strong> Guardia del Museo, Supervisor.<br><strong>Clases:</strong> Incidente, TipoIncidente, Obra, Guardia, Supervisor.',
        rationale: 'Conexión directa con la Regla de Negocio 2 (inmediatez de registro) y la compuerta de anomalía del BPMN Operativo. El CU-15 materializa en pantalla táctil la captura del daño, garantizando que el incidente quede disponible al supervisor para la toma de medidas.'
      }},
      'mod-rondas': {{
        title: 'Módulo 5: Planificación y Rondas de Vigilancia',
        badge: 'PREVENCIÓN Y PATRULLAJE',
        rfs: '<strong>RF-34:</strong> Generar planificación de rondas &bull; <strong>RF-35:</strong> Consultar planificación &bull; <strong>RF-36:</strong> Registrar revisión de sala.',
        cus: 'CU-12 Generar planificación de rondas<br>CU-13 Consultar planificación ronda<br>CU-14 Registrar revisión de la sala',
        actors: '<strong>Actores:</strong> Supervisor, Guardia del Museo.<br><strong>Clases:</strong> PlanificacionRonda, Guardia, Sala, AsignacionRonda.',
        rationale: 'Establece la base física preventiva donde el guardia patrulla periódicamente las salas del museo. Cumplimentar la revisión de sala es la precondición operativa para la eventual detección de obras dañadas.'
      }},
      'mod-obras': {{
        title: 'Módulo 1: Obras de Arte y Catálogo',
        badge: 'NÚCLEO PATRIMONIAL',
        rfs: '<strong>RF-01:</strong> Registrar ingreso de obra &bull; <strong>RF-02:</strong> Registrar reingreso a depósito &bull; <strong>RF-03:</strong> Consultar obra &bull; <strong>RF-04:</strong> Registrar baja de obra &bull; <strong>RF-39:</strong> Registrar obra a restaurar.',
        cus: 'CU-01 Registrar ingreso de obra<br>CU-02 Registrar reingreso de obra<br>CU-03 Consultar obra<br>CU-04 Registrar obra a restaurar<br>CU-42 Registrar baja de obra',
        actors: '<strong>Actores:</strong> Supervisor, Encargado de Museo.<br><strong>Clases:</strong> Obra, EstadoObra, Deposito, Artista, Estilo, TipoMaterial.',
        rationale: 'Gestiona el ciclo de vida del inventario patrimonial. Garantiza el cumplimiento de la RN-1 (reingreso obligatorio a depósito luego de cualquier envío a restauración, previo a su reasignación o baja).'
      }},
      'mod-maestros': {{
        title: 'Módulo 2: Parámetros Maestros y Tablas de Soporte',
        badge: 'CONFIGURACIÓN Y CONSISTENCIA',
        rfs: '<strong>RF-05..RF-24:</strong> Registrar, consultar, modificar y dar de baja Tipos de Obra, Tipos de Material, Salas, Guías, Estilos y Tipos de Incidentes.',
        cus: 'CU-08..CU-10 Materiales &bull; CU-11..14 / CU-24..27 Salas<br>CU-15..18 / CU-35..38 Guías &bull; CU-19..21 / CU-39..41 Estilos<br>CU-22..24 / CU-31..34 Tipos de Incidente',
        actors: '<strong>Actores:</strong> Administrador del Sistema, Supervisor.<br><strong>Clases:</strong> TipoObra, TipoMaterial, Sala, Guia, Estilo, TipoIncidente.',
        rationale: 'Provee los datos normalizados indispensables para la consistencia transaccional del sistema. Evita ambigüedades en la tipificación de incidentes, clasificación artística y ubicación en salas.'
      }},
      'mod-exposiciones': {{
        title: 'Módulo 3: Gestión de Exposiciones y Visitas',
        badge: 'PROCESO CLAVE ESENCIAL',
        rfs: '<strong>RF-25..RF-30:</strong> Registrar y consultar programación de exposiciones, planificar visitas guiadas, generar invitaciones y consultar agenda de guías.',
        cus: 'CU-05 Registrar programación exposiciones<br>CU-06 Consultar exposiciones<br>CU-07 Consultar visitas guiadas<br>CU-08 Registrar planificación visitas<br>CU-11 Consultar agenda de guías',
        actors: '<strong>Actores:</strong> Encargado de Museo, Guía, Visitante.<br><strong>Clases:</strong> Exposicion, ObraEnExposicion, VisitaGuiada, Guia, Sala.',
        rationale: 'Satisface el proceso de negocio sustantivo del museo ("Exponer obras de arte"). Cada exposición vincula temporalmente obras con salas específicas, delimitando el alcance de patrullaje de los guardias.'
      }},
      'mod-entradas': {{
        title: 'Módulo 4: Gestión de Venta de Entradas',
        badge: 'CONTROL DE AFORO Y RECAUDACIÓN',
        rfs: '<strong>RF-31:</strong> Registrar venta de entrada &bull; <strong>RF-32:</strong> Contratación de servicio de guía &bull; <strong>RF-33:</strong> Consultar venta de entrada.',
        cus: 'CU-09 Registrar venta de entrada<br>CU-10 Registrar servicio adicional de guía<br>CU-32 Consultar venta de entrada',
        actors: '<strong>Actores:</strong> Empleado de Boletería, Visitante.<br><strong>Clases:</strong> Entrada, Tarifa, DetalleVenta, Visitante.',
        rationale: 'Regula el ingreso de público y financiamiento operativo del museo, permitiendo calcular el volumen de aforo por sala para ajustar las frecuencias de rondas de vigilancia.'
      }},
      'mod-informes': {{
        title: 'Módulo 7: Informes y Reportes Gerenciales',
        badge: 'INTELIGENCIA Y CONTROL',
        rfs: '<strong>RF-40:</strong> Generar informe diario &bull; <strong>RF-41:</strong> Reporte de patrones &bull; <strong>RF-42:</strong> Consultar informe &bull; <strong>RF-43:</strong> Emitir historial.',
        cus: 'CU-18/19 Patrones de incidentes<br>CU-20/21 Informe diario de vigilancia<br>CU-22 Emitir historial de incidentes',
        actors: '<strong>Actores:</strong> Director del Museo, Supervisor.<br><strong>Clases:</strong> InformeDiario, Incidente, Sala, Obra.',
        rationale: 'Consolida los eventos registrados por los guardias en auditorías periódicas que permiten al Director y Supervisores evaluar medidas de prevención y zonas de mayor riesgo en el edificio.'
      }},
      'mod-seguridad': {{
        title: 'Módulo 8: Seguridad y Reglas de Dominio',
        badge: 'INTEGRIDAD TRANSVERSAL',
        rfs: '<strong>RF-44:</strong> Iniciar sesión &bull; <strong>RF-45:</strong> Cerrar sesión &bull; <strong>RF-46:</strong> Modificar contraseña &bull; <strong>RN-1:</strong> Reingreso a depósito &bull; <strong>RN-2:</strong> Registro inmediato.',
        cus: 'Transversal por Módulo Web (Autenticación y Sesión)<br>Restricciones de Integridad en Clases (RN-1 y RN-2)',
        actors: '<strong>Actores:</strong> Todos los roles autenticados.<br><strong>Clases:</strong> Usuario, Rol, Sesion, Obra, Incidente.',
        rationale: 'Requerimientos que NO poseen un caso de uso independiente con actor final porque se gestionan mediante el middleware de seguridad del Módulo Web o mediante restricciones del dominio de persistencia.'
      }}
    }};

    function selectTraceModule(el, modKey) {{
      document.querySelectorAll('.trace-rf-list .trace-rf-item').forEach(item => item.classList.remove('active'));
      el.classList.add('active');

      const data = traceModulesData[modKey];
      if (!data) return;

      document.getElementById('trace-mod-title').innerText = data.title;
      document.getElementById('trace-mod-badge').innerText = data.badge;
      document.getElementById('trace-rfs').innerHTML = data.rfs;
      document.getElementById('trace-cus').innerHTML = data.cus;
      document.getElementById('trace-actors').innerHTML = data.actors;
      document.getElementById('trace-rationale').innerText = data.rationale;
    }}
'''

    # Replace old traceData in JS with traceModulesData
    td_idx = src.find('const traceData = {')
    td_end = src.find('// Filter requirements in Slide 7', td_idx)
    if td_idx != -1 and td_end != -1:
        src = src[:td_idx] + js_trace_code + '\n    ' + src[td_end:]
        print("Traceability JS controller replaced successfully.")

    # Save final generator
    v6_gen_path = os.path.join(base_dir, "generate_v6_final_deck.py")
    with open(v6_gen_path, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"generate_v6_final_deck.py created successfully ({len(src)} bytes).")

if __name__ == "__main__":
    main()
