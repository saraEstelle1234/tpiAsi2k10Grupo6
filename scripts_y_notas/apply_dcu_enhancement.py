import re
import shutil
import subprocess

def apply_dcu_enhancement(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New DCU_ACTOR_STEPS in JavaScript
    old_steps = """    const DCU_ACTOR_STEPS = {
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
    };"""

    new_steps = """    const DCU_ACTOR_STEPS = {
      'all': {
        tag: 'VISTA COMPLETA',
        title: 'Vista Panorámica de los 45 Casos de Uso',
        desc: 'Estructura integral de 45 Casos de Uso numerados del 1 al 45, cubriendo la totalidad de roles del museo y la frontera del software.',
        transform: 'scale(1) translate(0%, 0%)'
      },
      'vigilancia': {
        tag: 'ACTOR PRINCIPAL DEL TPI',
        title: 'Encargado de Vigilancia (CU 13 al 17)',
        desc: 'Rondas presenciales y reporte físico: CU 13 (Consultar planificación), CU 14 (Registrar revisión de sala), CU 15 (Registrar incidente - nexo central extend), CU 16 (Consultar sala) y CU 17 (Consultar incidente).',
        transform: 'scale(2.4) translate(31.5%, -13%)'
      },
      'supervision': {
        tag: 'CONTROL Y RESOLUCIÓN',
        title: 'Encargado de Supervisión (CU 18 al 23)',
        desc: 'Seguimiento, auditoría y análisis: CU 18 (Generar patrones de incidentes), CU 19 (Consultar patrones), CU 20 (Generar informe diario), CU 21 (Consultar informe), CU 22 (Emitir historial) y CU 23 (Registrar seguimiento de resolución).',
        transform: 'scale(2.4) translate(37.5%, -35%)'
      },
      'ingreso': {
        tag: 'CATÁLOGO Y RESTAURACIÓN',
        title: 'Responsable de Ingreso de Obra (CU 1 al 4)',
        desc: 'Ciclo patrimonial de piezas: CU 1 (Registrar ingreso de obra), CU 2 (Registrar reingreso), CU 3 (Consultar obra) y CU 4 (Registrar obra a restaurar).',
        transform: 'scale(2.4) translate(37.5%, 39.5%)'
      },
      'atencion': {
        tag: 'OPERACIÓN COMERCIAL & VISITAS',
        title: 'Responsable de Atención al Cliente (CU 9 al 11)',
        desc: 'Operación diaria con visitantes: CU 9 (Registrar venta de entrada), CU 10 (Registrar contratación de guía - include) y CU 11 (Consultar agenda de guías).',
        transform: 'scale(2.35) translate(30%, 8.5%)'
      },
      'museo': {
        tag: 'PLANIFICACIÓN MUSEOLÓGICA',
        title: 'Administrador del Museo (CU 5 al 8)',
        desc: 'Planificación de exposiciones y visitas: CU 5 (Registrar programación de exposiciones), CU 6 (Consultar programación), CU 7 (Consultar planificación de visitas guiadas) y CU 8 (Registrar planificación de visitas).',
        transform: 'scale(2.35) translate(36%, 22%)'
      },
      'admin': {
        tag: 'DATOS MAESTROS DEL SISTEMA',
        title: 'Admin de Sistema (CU 24 al 42)',
        desc: 'Mantenimiento de tablas maestras: CU 24-27 (Salas), CU 28-30 (Materiales), CU 31-34 (Tipos de incidente), CU 35-38 (Guías), CU 39-41 (Estilos de obra) y CU 42 (Baja de obra).',
        transform: 'scale(2.15) translate(-25.5%, 32.5%)'
      },
      'usuario': {
        tag: 'SEGURIDAD Y CONTROL DE SESIÓN',
        title: 'Usuario (CU 43 al 45: Iniciar, Modificar y Cerrar Sesión)',
        desc: 'Funciones transversales de acceso al sistema: CU 43 (Iniciar sesión), CU 44 (Cerrar sesión) y CU 45 (Modificar contraseña / sesión).',
        transform: 'scale(2.3) translate(-26.5%, -1%)'
      }
    };"""

    if old_steps in content:
        content = content.replace(old_steps, new_steps)
        print(f"[{filepath}] Replaced DCU_ACTOR_STEPS")
    else:
        print(f"[{filepath}] old_steps not found directly, checking regex...")
        content = re.sub(
            r'const DCU_ACTOR_STEPS = \{[\s\S]*?\n    \};',
            new_steps.strip(),
            content
        )

    # 2. Extract base64 image from Slide 9
    img_match = re.search(r'(<img id="dcu-img"[^>]*src="data:image/png;base64,[^"]+"[^>]*>)', content)
    if not img_match:
        print(f"[{filepath}] Error: could not find dcu-img tag!")
        return
    dcu_img_tag = img_match.group(1)

    # 3. New Slide 9 HTML structure
    s9_pattern = r'(<div class="slide" id="slide-9"[\s\S]*?)(<!-- SLIDE 10:)'
    m_s9 = re.search(s9_pattern, content)
    if not m_s9:
        print(f"[{filepath}] Error: could not match slide-9 block")
        return

    new_slide_9 = f"""<div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
        <div>
          <div class="breadcrumb-tag">09 &bull; Frontera del Software </div>
          <h1 class="giant-title">Diagrama de Casos de Uso</h1>
          <p class="editorial-subtitle">
            Delimitación formal de las 45 funciones del software organizadas por rol del dominio (Sección 2.7 del TPI)
          </p>
        </div>
      </div>

      <!-- Barra de Sectorización por Actor de ancho completo (con todos los roles exactos) -->
      <div class="guided-tour-bar" id="dcu-tour-bar" style="margin-bottom: 14px; display: flex; flex-wrap: wrap; gap: 8px; align-items: center;">
        <span class="tour-label" style="font-weight: 700; color: #93C5FD; display: flex; align-items: center; gap: 6px; font-size: 12.5px; margin-right: 4px;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/></svg>
          Sectorizar por Actor:
        </span>
        <button class="tour-btn active" onclick="setDcuSector('all', this)">① Ver Todo (45 CUs)</button>
        <button class="tour-btn" onclick="setDcuSector('vigilancia', this)">② Encargado de Vigilancia (CU 13-17)</button>
        <button class="tour-btn" onclick="setDcuSector('supervision', this)">③ Encargado de Supervisión (CU 18-23)</button>
        <button class="tour-btn" onclick="setDcuSector('ingreso', this)">④ Responsable de Ingreso de Obra (CU 1-4)</button>
        <button class="tour-btn" onclick="setDcuSector('atencion', this)">⑤ Responsable de Atención (CU 9-11)</button>
        <button class="tour-btn" onclick="setDcuSector('museo', this)">⑥ Admin del Museo (CU 5-8)</button>
        <button class="tour-btn" onclick="setDcuSector('admin', this)">⑦ Admin de Sistema (CU 24-42)</button>
        <button class="tour-btn" onclick="setDcuSector('usuario', this)">⑧ Usuario (CU 43-45: Sesión)</button>
      </div>

      <!-- Grid: Columna Izquierda ajustada al ratio vertical (alto y flaco, SIN bandas negras), Columna Derecha con detalle de actores -->
      <div style="display: grid; grid-template-columns: auto 1fr; gap: 20px; align-items: stretch;">
        
        <!-- Columna Izquierda: Formato vertical exacto del diagrama (relación 1455 / 1675) -->
        <div style="display: flex; flex-direction: column; width: clamp(390px, calc(68vh * 0.869), 560px); flex-shrink: 0;">
          <div class="card-dark reveal-item revealed" style="height: clamp(520px, 70vh, 740px); padding: 8px; display: flex; flex-direction: column; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); background: #0A1128;">
            <div class="cinematic-viewport dark-bg" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: #060B14;">
              {dcu_img_tag}
            </div>
            <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px; display: flex; justify-content: space-between; align-items: center;">
              <span style="font-size: 12px; font-weight: 600; color: #CBD5E1;">45 CUs &bull; Clic para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 34px; padding: 0 14px; font-size: 12px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (45 CUs)')">
                Ampliar <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
              </button>
            </div>
          </div>

          <!-- Card dinámico explicativo del Actor y CUs activos -->
          <div class="tour-step-card" id="dcu-tour-card" style="margin-top: 10px; margin-bottom: 0;">
            <div class="tour-step-tag" id="dcu-tour-tag">VISTA COMPLETA</div>
            <div class="tour-step-title" id="dcu-tour-title" style="font-size: 13.5px; font-weight: 700;">Vista Panorámica de los 45 Casos de Uso</div>
            <div class="tour-step-desc" id="dcu-tour-desc" style="font-size: 12px; line-height: 1.5;">Estructura integral de 45 Casos de Uso numerados del 1 al 45, cubriendo la totalidad de roles del museo y la frontera del software.</div>
          </div>
        </div>

        <!-- Columna Derecha: Panel de roles ampliado con desglose numérico completo de todos los actores -->
        <div class="card-dark reveal-item revealed" style="padding: 22px 24px; display: flex; flex-direction: column; justify-content: space-between; max-height: clamp(520px, 70vh, 740px); overflow-y: auto;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
              <div class="breadcrumb-tag" style="margin-bottom: 0;">Frontera del Software &bull; Sección 2.7</div>
              <span style="font-size: 12px; font-weight: 700; color: #93C5FD; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 999px; padding: 2px 10px;">7 Roles &bull; 45 Casos de Uso</span>
            </div>
            
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 8px; letter-spacing: -0.01em;">Organización de los Casos de Uso por Actor</h3>
            <p style="font-size: 12.5px; line-height: 1.5; color: var(--text-light); margin-bottom: 14px;">
              El modelo delimita taxativamente las funciones del software mediante 45 casos de uso numerados de forma unívoca, asociando cada caso al rol responsable:
            </p>

            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
              
              <!-- Rol 1: Encargado de Vigilancia -->
              <div style="background: rgba(45, 127, 249, 0.06); border: 1px solid rgba(45, 127, 249, 0.2); border-left: 3px solid var(--blue-accent); border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('vigilancia', document.querySelectorAll('#dcu-tour-bar .tour-btn')[1])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>👮 Encargado de Vigilancia</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 13 al 17</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Rondas presenciales y reporte in situ: <strong>CU 13</strong> (Consultar ronda), <strong>CU 14</strong> (Revisión de sala), <strong>CU 15</strong> (Registrar incidente - nexo central extend), <strong>CU 16</strong> (Consultar sala) y <strong>CU 17</strong> (Consultar incidente).
                </div>
              </div>

              <!-- Rol 2: Encargado de Supervisión -->
              <div style="background: rgba(96, 165, 250, 0.06); border: 1px solid rgba(96, 165, 250, 0.2); border-left: 3px solid #60A5FA; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('supervision', document.querySelectorAll('#dcu-tour-bar .tour-btn')[2])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>📋 Encargado de Supervisión</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 18 al 23</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Auditoría y control: <strong>CU 18 y 19</strong> (Patrones de incidentes), <strong>CU 20 y 21</strong> (Informe diario de vigilancia), <strong>CU 22</strong> (Historial de incidentes) y <strong>CU 23</strong> (Seguimiento de resolución).
                </div>
              </div>

              <!-- Rol 3: Responsable de Ingreso de Obra -->
              <div style="background: rgba(56, 189, 248, 0.06); border: 1px solid rgba(56, 189, 248, 0.2); border-left: 3px solid #38BDF8; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('ingreso', document.querySelectorAll('#dcu-tour-bar .tour-btn')[3])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>🎨 Resp. Ingreso de Obra</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 01 al 04</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Gestión patrimonial: <strong>CU 1</strong> (Ingreso de obra), <strong>CU 2</strong> (Reingreso de obra), <strong>CU 3</strong> (Consultar obra) y <strong>CU 4</strong> (Registrar obra a restaurar - RN 1).
                </div>
              </div>

              <!-- Rol 4: Responsable de Atención al Cliente -->
              <div style="background: rgba(16, 185, 129, 0.06); border: 1px solid rgba(16, 185, 129, 0.2); border-left: 3px solid #10B981; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('atencion', document.querySelectorAll('#dcu-tour-bar .tour-btn')[4])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #A7F3D0; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>🎟️ Resp. Atención al Cliente</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 09 al 11</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Operación comercial con público: <strong>CU 9</strong> (Venta de entrada general), <strong>CU 10</strong> (Contratación de servicio de guía - include) y <strong>CU 11</strong> (Consultar agenda de guías).
                </div>
              </div>

              <!-- Rol 5: Administrador del Museo -->
              <div style="background: rgba(245, 158, 11, 0.06); border: 1px solid rgba(245, 158, 11, 0.2); border-left: 3px solid #F59E0B; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('museo', document.querySelectorAll('#dcu-tour-bar .tour-btn')[5])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #FDE68A; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>🏛️ Administrador del Museo</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 05 al 08</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Planificación de actividades: <strong>CU 5 y 6</strong> (Programación de exposiciones) y <strong>CU 7 y 8</strong> (Planificación de visitas guiadas del museo).
                </div>
              </div>

              <!-- Rol 6: Admin de Sistema -->
              <div style="background: rgba(129, 140, 248, 0.06); border: 1px solid rgba(129, 140, 248, 0.2); border-left: 3px solid #818CF8; border-radius: 10px; padding: 10px 12px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('admin', document.querySelectorAll('#dcu-tour-bar .tour-btn')[6])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #E0E7FF; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>⚙️ Admin de Sistema</span>
                  <span style="font-size: 11px; opacity: 0.85;">CU 24 al 42</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Tablas maestras: <strong>CU 24-27</strong> (Salas), <strong>CU 28-30</strong> (Materiales), <strong>CU 31-34</strong> (Tipos de daño), <strong>CU 35-38</strong> (Guías), <strong>CU 39-41</strong> (Estilos) y <strong>CU 42</strong> (Baja de obra).
                </div>
              </div>

              <!-- Rol 7: Usuario (Control de Sesión) - FULL WIDTH EN EL GRID -->
              <div style="grid-column: span 2; background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-left: 3px solid #38BDF8; border-radius: 10px; padding: 10px 14px; cursor: pointer; transition: background 0.2s ease;" onclick="setDcuSector('usuario', document.querySelectorAll('#dcu-tour-bar .tour-btn')[7])" title="Clic para enfocar en el diagrama">
                <div style="font-size: 12.5px; font-weight: 800; color: #BAE6FD; margin-bottom: 3px; display: flex; justify-content: space-between;">
                  <span>🔐 Usuario (Control y Gestión de Sesión)</span>
                  <span style="font-size: 11.5px; opacity: 0.95; font-weight: 700;">CU 43, 44 y 45</span>
                </div>
                <div style="font-size: 11.5px; color: var(--text-light); line-height: 1.45;">
                  Funciones transversales de autenticación y seguridad: <strong>CU 43 (Iniciar sesión)</strong>, <strong>CU 44 (Cerrar sesión)</strong> y <strong>CU 45 (Modificar sesión / contraseña)</strong>.
                </div>
              </div>

            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 10px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD; line-height: 1.45;">
              💡 <em>Hacé clic en cualquiera de los botones de la barra superior o en las tarjetas de actores para enfocar ese sector en alta resolución, o hacé clic sobre el diagrama para navegarlo con zoom libre.</em>
            </div>
          </div>
        </div>

      </div>
    </div>
    \\2"""

    content = re.sub(s9_pattern, new_slide_9, content)
    print(f"[{filepath}] Replaced Slide 9 HTML structure successfully!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

apply_dcu_enhancement('index.html')
apply_dcu_enhancement('presentacion.html')

# Test DOM run
res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
