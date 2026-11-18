with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Slide 9
s9_start = content.find('<!-- SLIDE 9: DCU')
s10_start = content.find('<!-- SLIDE 10:')

if s9_start == -1 or s10_start == -1:
    raise Exception("Could not find Slide 9 boundaries")

new_s9 = """<!-- SLIDE 9: DCU GENERAL (MAXIMIZADO ALTO, SIN BANDAS NEGRAS, SIN CUADRITOS NEGROS) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 620px 1fr; gap: 24px; align-items: stretch;">
        <!-- Columna Izquierda: Diagrama en proporción vertical exacta (sin bandas negras) -->
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px; display: flex; flex-wrap: wrap; gap: 6px;">
            <span style="font-size: 11.5px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 2px;">Sectorizar:</span>
            <button class="preset-btn active" onclick="setDcuSector('all', this)" style="padding: 4px 10px; font-size: 11.5px;">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDcuSector('guardia', this)" style="padding: 4px 10px; font-size: 11.5px;">Guardia</button>
            <button class="preset-btn" onclick="setDcuSector('supervisor', this)" style="padding: 4px 10px; font-size: 11.5px;">Supervisor</button>
            <button class="preset-btn" onclick="setDcuSector('ingreso', this)" style="padding: 4px 10px; font-size: 11.5px;">Ingreso</button>
            <button class="preset-btn" onclick="setDcuSector('admin', this)" style="padding: 4px 10px; font-size: 11.5px;">Admin</button>
          </div>

          <!-- Marco del diagrama: Proporción vertical ajustada a 0.868 para eliminar bandas laterales -->
          <div class="card-dark reveal-item revealed" style="height: 750px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; background: #121212; border-radius: 10px; width: 100%; height: 100%;">
              <img id="dcu-img" src="{b64_dcu}" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in; transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
              <span style="font-size: 12px; font-weight: 600; color: #CBD5E1;">42 CUs &bull; Clic para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 34px; padding: 0 14px; font-size: 12px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- Columna Derecha: Explicación limpia, continua y elegante (SIN CUADRITOS NEGROS) -->
        <div class="card-dark reveal-item revealed" style="padding: 28px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Frontera del Software &bull; Sección 2.7</div>
            <h3 style="font-size: 20px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Organización de los 42 Casos de Uso</h3>
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 20px;">
              El modelo delimita taxativamente las funciones del software mediante 42 casos de uso numerados de forma unívoca, estructurados según los cuatro actores clave del dominio:
            </p>

            <div style="display: flex; flex-direction: column; gap: 16px; padding-left: 4px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Guardia de Vigilancia (CU 13 al CU 17)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Rondas presenciales y reporte in situ con tablet táctil: <strong>CU-14 (Revisar sala)</strong> y <strong>CU-15 (Registrar incidente)</strong> como nexo operativo principal.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Supervisor de Seguridad (CU 18 al CU 23)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Análisis y control: seguimiento de novedades no resueltas, análisis de patrones de recurrencia y definición del plan de acción (taller de restauración o baja).
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Ingreso y Ciclo de Obras (CU 01 al CU 04)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Gestión patrimonial: ingreso de obras, derivación a restauración externa y cumplimiento riguroso de la <strong>Regla de Negocio 1</strong> (reingreso obligatorio a depósito).
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Administración y Catálogos (CU 24 al CU 42)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Mantenimiento de tablas maestras: salas, materiales, tipos de daño, guías, tarifas y administración de accesos del sistema.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 10px; padding: 12px 14px; margin-top: 20px;">
            <div style="font-size: 12.5px; color: #93C5FD; line-height: 1.45;">
              💡 <em>Usá los botones de la barra superior para enfocar automáticamente cada sector por actor, o hacé clic sobre el diagrama para navegarlo con zoom libre.</em>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

content = content[:s9_start] + new_s9 + content[s10_start:]

# 2. Update Slide 12
s12_start = content.find('<!-- SLIDE 12: DIAGRAMA DE CLASES')
s13_start = content.find('<!-- SLIDE 13:')

if s12_start == -1 or s13_start == -1:
    raise Exception("Could not find Slide 12 boundaries")

new_s12 = """<!-- SLIDE 12: DIAGRAMA DE CLASES (MAXIMIZADO AL MÁXIMO, SIN TIRA INFERIOR, SIN CUADRITOS NEGROS) -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
        <!-- Columna Izquierda: Diagrama de clases maximizado en alto y ancho (~1060px x 740px) -->
        <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 740px; display: flex; flex-direction: column; padding: 10px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);">
          <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; background: #121212; border-radius: 10px;">
            <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
          </div>
          <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
            <span style="font-size: 12.5px; font-weight: 600; color: #CBD5E1;">Clases, Atributos y Métodos &bull; Visualización de Dominio</span>
            <button class="btn-primary" style="min-height: 36px; padding: 0 16px; font-size: 12.5px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
              Ampliar {svg_expand}
            </button>
          </div>
        </div>

        <!-- Columna Derecha: Síntesis conceptual continua y limpia (SIN CUADRITOS NEGROS) -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Modelo de Dominio</div>
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Lógica Estructural</h3>
            <p style="font-size: 13px; line-height: 1.55; color: var(--text-light); margin-bottom: 18px;">
              Entidades y relaciones estructurales especificadas en la Sección 2.10 del TPI:
            </p>

            <div style="display: flex; flex-direction: column; gap: 15px; padding-left: 2px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Gestión de Incidentes</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La entidad <code>Incidente</code> documenta fecha, hora y descripción, vinculada a su <code>TipoIncidente</code> y a la <code>Obra</code> afectada.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Obra y Estados</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  <code>Obra</code> encapsula autor, estilo, dimensiones y material (para sugerir acciones inmediatas), transicionando a <em>'Inactivo'</em> ante daño.
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Vigilancia y Rondas</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La relación entre <code>Guardia</code> y <code>Sala</code> se asienta mediante la clase asociativa <code>SalaXGuardia</code>, auditando fecha y hora de ronda.
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Depósito (Regla 1)</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  Toda obra derivada a <code>Restaurador</code> debe ingresar obligatoriamente a la clase <code>Deposito</code> antes de reasignarse.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Hacé clic en el diagrama o en 'Ampliar' para explorar todas las clases, atributos y métodos en alta resolución.</em>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

content = content[:s12_start] + new_s12 + content[s13_start:]

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_v8_deck.py successfully updated with new Slide 09 and Slide 12!")
