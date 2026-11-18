# -*- coding: utf-8 -*-
"""
build_v7_deck.py
Builds the refined 15-slide presentation deck:
1. Slide 7: Requerimientos Funcionales (interactive accordion with all 15 bold categories from the TPI, search & expand all).
2. Slide 8: Requerimientos No Funcionales (dedicated slide with generous cards for RNF-1 to RNF-6, no N:M chamuyo).
3. Slide 9: Diagrama de Casos de Uso (much larger view, actor presets: Guardia, Supervisor, Ingreso, Administrador, single explanatory card).
4. Slide 10: Plantilla CU-15 (faithful to Section 2.8 with ID, Name, Actors, Type, Objective, Precondition, 14 Normal steps, Alternates A1-A3, Postconditions).
5. Slide 11: Prototipo de Interfaz (matching CU-15).
6. Slide 14: Trazabilidad (concept N:M + 8-module matrix).
7. Slide 15: Cierre & 9 members.
8. Speaker topics updated for the 9 presenters (Fran on DCU, Juan on DCD).
"""

import os
import sys

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)

    v6_path = os.path.join(base_dir, "generate_v6_final_deck.py")
    with open(v6_path, "r", encoding="utf-8") as f:
        src = f.read()

    print(f"Loaded v6 generator ({len(src)} bytes)")

    # Update slideTitles in JavaScript
    old_titles = '''    const slideTitles = [
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
      "13 · Multiplicidades y Asociaciones",
      "14 · Trazabilidad de Requerimientos",
      "15 · Cierre y Agradecimiento"
    ];'''

    src = src.replace(old_titles, new_titles)

    # CSS for RF Accordion and Template CU-15
    extra_css = '''
/* ========================================================
   REQUERIMIENTOS FUNCIONALES ACCORDION (SLIDE 7)
   ======================================================== */
.rf-group {
  background: rgba(14, 31, 58, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}

.rf-group[open] {
  border-color: var(--blue-accent);
  background: rgba(20, 42, 78, 0.75);
}

.rf-summary {
  padding: 12px 18px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  font-weight: 700;
  color: #FFFFFF;
  user-select: none;
}

.rf-summary::-webkit-details-marker {
  display: none;
}

.rf-summary::after {
  content: '▼';
  font-size: 10px;
  color: var(--blue-accent);
  transition: transform 0.2s ease;
}

.rf-group[open] .rf-summary::after {
  transform: rotate(180deg);
}

.rf-badge {
  font-size: 11px;
  font-weight: 700;
  background: rgba(47, 107, 255, 0.2);
  color: #93C5FD;
  padding: 3px 8px;
  border-radius: 999px;
  margin-left: 8px;
}

.rf-body {
  padding: 8px 18px 14px 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  font-size: 13px;
  line-height: 1.6;
  color: var(--text-light);
}

.rf-item {
  padding: 6px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.rf-item:last-child {
  border-bottom: none;
}

.rf-num {
  font-weight: 700;
  color: var(--blue-accent);
  font-family: monospace;
  font-size: 12px;
  flex-shrink: 0;
}

/* ========================================================
   CU-15 FORMAL TEMPLATE (SLIDE 10)
   ======================================================== */
.cu-template-container {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(14, 31, 58, 0.75);
}

.cu-step-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 6px;
  font-size: 13px;
  line-height: 1.45;
  color: var(--text-light);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.cu-step-row:hover {
  background: rgba(47, 107, 255, 0.1);
}

.cu-step-num {
  font-weight: 800;
  color: #93C5FD;
  font-size: 12px;
  min-width: 22px;
  text-align: right;
  flex-shrink: 0;
}
'''
    src = src.replace('/* Presets focus bar for DCU & DCD */', extra_css + '\n/* Presets focus bar for DCU & DCD */')

    # Update Member topics in Slide 1 and Slide 15
    src = src.replace('Dominio bajo estudio y Objetivos organizacionales', 'Dominio bajo estudio y Objetivos de la organización')
    src = src.replace('Requerimientos Funcionales y No Funcionales', 'Requerimientos Funcionales y No Funcionales (RF y RNF)')
    src = src.replace('Prototipo de Interfaz y Trazabilidad de Requerimientos', 'Trazabilidad de Requerimientos y Cierre')

    # Locate section between s7_start and s11_start
    s7_start = src.find('<!-- SLIDE 7: REQUERIMIENTOS -->')
    s11_start = src.find('<!-- SLIDE 11: PROTOTIPO DE PANTALLA -->')

    if s7_start != -1 and s11_start != -1:
        # Define New Slides 7, 8, 9, 10
        new_slides_7_to_10 = '''<!-- SLIDE 7: REQUERIMIENTOS FUNCIONALES -->
    <div class="slide" id="slide-7" data-topic="07 · Requerimientos Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">07 &bull; Especificación de Requerimientos</div>
          <h1 class="giant-title">Requerimientos Funcionales</h1>
          <p class="editorial-subtitle">
            Catálogo estructurado por paquetes funcionales del sistema (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="display: flex; gap: 10px; align-items: center; padding-top: 10px;">
          <button class="btn-secondary" onclick="expandAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Expandir todos
          </button>
          <button class="btn-secondary" onclick="collapseAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Colapsar todos
          </button>
        </div>
      </div>

      <div style="margin-bottom: 14px;">
        <input type="text" id="rf-search-input" class="search-input" placeholder="🔍 Filtrar requerimientos por palabra clave (ej: obra, sala, incidente, ronda, informe)..." oninput="filterRequirements()" style="width: 100%; height: 46px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0 18px; color: #FFF; font-size: 14px;">
      </div>

      <!-- 15 Global Bold Categories from TPI in 2 Scrollable Columns -->
      <div id="rf-accordion-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-height: 520px; overflow-y: auto; padding-right: 6px;">
        
        <!-- 1. Administrar Obras de Arte -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Administrar Obras de Arte <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 1.</span> Registrar ingreso de obra</div>
            <div class="rf-item"><span class="rf-num">RF 2.</span> Consultar obra</div>
            <div class="rf-item"><span class="rf-num">RF 3.</span> Registrar baja de obra</div>
          </div>
        </details>

        <!-- 2. Administrar Tipos de Obra -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Obra <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 4.</span> Registrar tipo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 5.</span> Consultar tipo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 6.</span> Registrar baja de tipo de obra</div>
          </div>
        </details>

        <!-- 3. Administrar Tipos de Material -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Material <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 7.</span> Registrar tipo de material</div>
            <div class="rf-item"><span class="rf-num">RF 8.</span> Consultar tipo de material</div>
            <div class="rf-item"><span class="rf-num">RF 9.</span> Registrar baja de tipo de material</div>
          </div>
        </details>

        <!-- 4. Administrar Salas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Salas <span class="rf-badge">4 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 10.</span> Registrar sala</div>
            <div class="rf-item"><span class="rf-num">RF 11.</span> Consultar sala</div>
            <div class="rf-item"><span class="rf-num">RF 12.</span> Modificar sala</div>
            <div class="rf-item"><span class="rf-num">RF 13.</span> Registrar baja de sala</div>
          </div>
        </details>

        <!-- 5. Administrar Guías -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Guías <span class="rf-badge">4 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 14.</span> Registrar guía</div>
            <div class="rf-item"><span class="rf-num">RF 15.</span> Consultar guía</div>
            <div class="rf-item"><span class="rf-num">RF 16.</span> Registrar modificación de guía</div>
            <div class="rf-item"><span class="rf-num">RF 17.</span> Registrar baja de guía</div>
          </div>
        </details>

        <!-- 6. Administrar Estilos de Obra -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Estilos de Obra <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 18.</span> Registrar estilo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 19.</span> Consultar estilo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 20.</span> Registrar baja de estilo de obra</div>
          </div>
        </details>

        <!-- 7. Administrar Tipos de Incidentes -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Incidentes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 21.</span> Registrar tipo de incidente</div>
            <div class="rf-item"><span class="rf-num">RF 22.</span> Consultar tipo de incidente</div>
            <div class="rf-item"><span class="rf-num">RF 23.</span> Registrar baja de tipo de incidente</div>
          </div>
        </details>

        <!-- 8. Gestionar Exposiciones -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Exposiciones <span class="rf-badge">2 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 24.</span> Registrar programación de exposiciones</div>
            <div class="rf-item"><span class="rf-num">RF 25.</span> Consultar programación de exposiciones</div>
          </div>
        </details>

        <!-- 9. Gestionar Visitas Guiadas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Visitas Guiadas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 26.</span> Registrar planificación de visitas guiadas</div>
            <div class="rf-item"><span class="rf-num">RF 27.</span> Consultar planificación de visitas guiadas</div>
            <div class="rf-item"><span class="rf-num">RF 28.</span> Consultar agenda de guías</div>
          </div>
        </details>

        <!-- 10. Gestionar Venta de Entradas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Venta de Entradas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 29.</span> Registrar venta de entrada</div>
            <div class="rf-item"><span class="rf-num">RF 30.</span> Registrar contratación de servicio adicional de guía</div>
            <div class="rf-item"><span class="rf-num">RF 31.</span> Consultar venta de entrada</div>
          </div>
        </details>

        <!-- 11. Gestionar Planificación y Rondas de Vigilancia -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Planificación y Rondas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 32.</span> Generar planificación de rondas de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 33.</span> Consultar planificación de rondas de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 34.</span> Registrar revisión de sala</div>
          </div>
        </details>

        <!-- 12. Gestionar Incidentes -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Incidentes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 35.</span> Registrar incidente</div>
            <div class="rf-item"><span class="rf-num">RF 36.</span> Consultar incidentes</div>
            <div class="rf-item"><span class="rf-num">RF 37.</span> Registrar seguimiento de resolución de incidente</div>
          </div>
        </details>

        <!-- 13. Gestionar Restauración -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Restauración <span class="rf-badge">2 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 40.</span> Registrar obra a restaurar</div>
            <div class="rf-item"><span class="rf-num">RF 41.</span> Registrar reingreso de obra</div>
          </div>
        </details>

        <!-- 14. Generar Informes y Reportes -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Generar Informes y Reportes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 42.</span> Generar informe diario de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 43.</span> Generar reporte de patrones de incidentes</div>
            <div class="rf-item"><span class="rf-num">RF 44.</span> Emitir historial de incidentes</div>
          </div>
        </details>

        <!-- 15. Administrar Sesión -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Sesión <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 45.</span> Iniciar sesión</div>
            <div class="rf-item"><span class="rf-num">RF 46.</span> Cerrar sesión</div>
            <div class="rf-item"><span class="rf-num">RF 47.</span> Modificar contraseña</div>
          </div>
        </details>

      </div>
    </div>

    <!-- SLIDE 8: REQUERIMIENTOS NO FUNCIONALES -->
    <div class="slide" id="slide-8" data-topic="08 · Requerimientos No Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
        <div>
          <div class="breadcrumb-tag">08 &bull; Restricciones de Calidad y Arquitectura</div>
          <h1 class="giant-title">Requerimientos No Funcionales</h1>
          <p class="editorial-subtitle">
            Criterios de calidad, arquitectura y restricciones técnicas del sistema (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;">
        
        <div class="card-dark reveal-item revealed" style="border-top: 3px solid var(--blue-accent); padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Arquitectura &bull; Acceso Web Ubicuo</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 1 &bull; Módulo Web de Soporte</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #60A5FA; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Usabilidad &bull; Terminal Táctil para Guardias</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 2 &bull; Interfaz Móvil para Rondas</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #38BDF8; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Rendimiento &bull; Transacciones Críticas</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 3 &bull; Tiempos de Respuesta &lt; 2s</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            El sistema procesará las consultas de salas y registros de incidentes en menos de 2 segundos en condiciones normales de carga, asegurando fluidez operativa durante la ronda.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #818CF8; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Seguridad &bull; Control de Acceso por Rol</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 4 &bull; Autenticación y RBAC</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Autenticación obligatoria con perfiles diferenciados (Guardia, Supervisor, Encargado, Administrador), contraseñas robustas y sesiones cifradas HTTPS para salvaguardar la integridad de los datos.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #A78BFA; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Disponibilidad &bull; Operatividad 24/7</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 5 &bull; Confiabilidad y Persistencia ACID</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Disponibilidad continua con base de datos relacional que garantiza atomicidad, consistencia, aislamiento y durabilidad (ACID) en cada actualización del inventario patrimonial.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #F472B6; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Auditoría &bull; Registro Inmutable de Eventos</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 6 &bull; Trazabilidad y Marcas de Tiempo</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Captura automática e inalterable de fecha, hora de servidor y usuario responsable en cada transacción de vigilancia, sustentando los informes diarios y reportes de patrones.
          </div>
        </div>

      </div>
    </div>

    <!-- SLIDE 9: DCU GENERAL (AMPLIADO Y SECTORIZADO POR ACTOR) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.55fr 0.45fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Sectorizar por Actor:</span>
            <button class="preset-btn active" onclick="setDiagramPreset('dcu-img', 1, 0, 0)">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.3, -20, -22)">Guardia (CU-14 / CU-15)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.0, 18, -16)">Supervisor</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.1, -20, 22)">Ingreso y Obras</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 1.9, 20, 20)">Administrador</button>
          </div>

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcu-img" src="{b64_dcu}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: zoom-in;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">42 Casos de Uso &bull; Fondo nativo sin bordes negros</span>
              <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar a pantalla completa {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- UN SOLO CUADRO EXPLICATIVO GENERAL -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Límites y Concepción</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción General del Diagrama</h3>
            
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              El modelo define el límite completo del software mediante <strong>42 Casos de Uso</strong> numerados de forma unívoca y continua, satisfaciendo el proceso sustantivo (<em>Exponer obras de arte</em>) y el proceso de soporte crítico bajo estudio (<em>Gestionar incidentes y restauración</em>).
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">8 Actores del Sistema</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  7 roles humanos con accesos diferenciados y 1 temporizador de software (<em>Administrador Web</em>) que dispara la planificación de rondas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Separación Operativa / Gerencial</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia opera en terminal móvil (revisión y reporte), mientras que supervisores y administradores gestionan el catálogo patrimonial e informes.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Centralidad de la Vigilancia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El <strong>CU-15 (Registrar incidente)</strong> constituye el núcleo de integración entre la detección en sala y la custodia patrimonial.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Navegación Interactiva</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Utilizá los botones superiores para enfocar la sección de cada actor o hacé clic en el diagrama para explorar con zoom libre.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: PLANTILLA CU-15 (ESTILO PLANTILLA ORIGINAL SECCIÓN 2.8) -->
    <div class="slide" id="slide-10" data-topic="10 · Plantilla de Caso de Uso">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">10 &bull; Especificación Formal de Caso de Uso</div>
          <h1 class="giant-title">Plantilla de Caso de Uso</h1>
          <p class="editorial-subtitle">
            Descripción formal: Registrar Incidente (CU-15 &bull; Sección 2.8 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
        </div>
      </div>

      <!-- Header Metadata Bar matching TPI Section 2.8 -->
      <div class="card-dark reveal-item revealed" style="margin-bottom: 14px; padding: 14px 20px;">
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; font-size: 13px;">
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">ID Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;">CU-15</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Nombre Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;">Registrar incidente</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Actor Principal</span>
            <strong style="color: #FFF; font-size: 14px;">Encargado de vigilancia (EV)</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Actor Secundario</span>
            <strong style="color: #CBD5E1; font-size: 14px;">&mdash;</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Tipo de Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;"><span style="color: var(--blue-accent);">[X]</span> Concreto &nbsp; [ ] Abstracto</strong>
          </div>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 16px;">
        <!-- Left Column: Objetivo, Pre-Condición, Cursos Alternativos, Post-Condiciones -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
          
          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Objetivo</div>
            <div style="font-size: 13px; line-height: 1.5; color: var(--text-light);">
              Registrar incidente en una sala del museo, indicando la pieza involucrada y el tipo de incidente con la hora.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Pre-Condición</div>
            <div style="font-size: 13px; line-height: 1.5; color: var(--text-light);">
              Usuario logueado en el Módulo Web de Soporte y sala seleccionada.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #F59E0B; text-transform: uppercase; margin-bottom: 6px;">Cursos Alternativos</div>
            <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              <div><strong style="color: #FCD34D;">A1 (Paso 11):</strong> El EV no confirma el registro del incidente. Se cancela el caso de uso.</div>
              <div><strong style="color: #FCD34D;">A2 (Paso 4):</strong> El sistema busca el código del objeto pero no lo encuentra, y solicita que se ingrese otro código.</div>
              <div><strong style="color: #FCD34D;">A3 (Paso 6):</strong> El EV no confirma el objeto encontrado. Se cancela el caso de uso.</div>
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #10B981; text-transform: uppercase; margin-bottom: 6px;">Post-Condiciones</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              <div style="margin-bottom: 4px;"><strong style="color: #6EE7B7;">Éxito:</strong> El sistema registró con éxito el incidente en una sala, con la pieza, el tipo de incidente, hora y registra el objeto con estado “Inactivo”. Incidente registrado exitosamente.</div>
              <div><strong style="color: #F87171;">Fracaso:</strong> El CU se cancela cuando: (A1) El EV no confirmó el registro; (A2) El EV cancela en cualquier momento; (A3) El EV no confirmó el objeto encontrado.</div>
            </div>
          </div>

        </div>

        <!-- Right Column: Curso Normal (14 Pasos) -->
        <div class="card-dark reveal-item revealed" style="padding: 16px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 8px; margin-bottom: 10px;">
            <span style="font-size: 13px; font-weight: 700; color: #FFF; text-transform: uppercase;">Curso Normal (Flujo Principal)</span>
            <span style="font-size: 11px; font-weight: 700; background: rgba(47,107,255,0.2); color: #93C5FD; padding: 3px 8px; border-radius: 999px;">14 Pasos Secuenciales</span>
          </div>

          <div style="max-height: 440px; overflow-y: auto; padding-right: 6px; display: flex; flex-direction: column;">
            <div class="cu-step-row"><span class="cu-step-num">1.</span> <span>El EV ingresa a la opción <em>Reportar incidente</em>.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">2.</span> <span>El sistema solicita que ingrese el código del objeto.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">3.</span> <span>El EV ingresa el código del objeto.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">4.</span> <span>El sistema busca la obra por el código ingresado y muestra sus datos: título/nombre de la obra, sala asignada y ubicación física dentro de la sala. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A2 si no existe]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">5.</span> <span>El sistema solicita que se confirme que el objeto encontrado es el correcto.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">6.</span> <span>El EV confirma el objeto encontrado. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A3 si no confirma]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">7.</span> <span>El sistema solicita que se seleccione el tipo de incidente entre Deterioro natural, Deterioro provocado y Caída accidental.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">8.</span> <span>El EV selecciona el tipo de incidente.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">9.</span> <span>El sistema muestra los datos del incidente para su revisión final: sala/ubicación, obra involucrada, tipo de incidente seleccionado, hora actual del registro y el nuevo estado de la obra.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">10.</span> <span>El sistema solicita que se confirme el registro del incidente.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">11.</span> <span>El EV confirma el registro del incidente. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A1 si cancela]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">12.</span> <span>El sistema registra el incidente en una sala del museo, con la pieza involucrada, el tipo de incidente, la hora (que se obtiene de la hora actual).</span></div>
            <div class="cu-step-row" style="background: rgba(16, 185, 129, 0.08);"><span class="cu-step-num" style="color: #6EE7B7;">13.</span> <span>El sistema registra el objeto con estado <strong>“Inactivo”</strong>.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">14.</span> <span>Fin del caso de uso.</span></div>
          </div>
        </div>
      </div>
    </div>
'''
        src = src[:s7_start] + new_slides_7_to_10 + src[s11_start:]
        print("Slides 7, 8, 9, 10 replaced successfully.")

    # JavaScript helper functions for Accordion expand/collapse
    rf_js_helpers = '''
    // ========================================================
    // REQUERIMIENTOS FUNCIONALES EXPAND / COLLAPSE
    // ========================================================
    function expandAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = true);
    }}

    function collapseAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = false);
    }}
'''
    src = src.replace('function filterRequirements() {', rf_js_helpers + '\n    function filterRequirements() {')

    # Save to generate_v7_deck.py
    v7_gen_path = os.path.join(base_dir, "generate_v7_deck.py")
    with open(v7_gen_path, "w", encoding="utf-8") as f:
        f.write(src)

    print(f"generate_v7_deck.py created successfully ({len(src)} bytes).")

if __name__ == "__main__":
    main()
