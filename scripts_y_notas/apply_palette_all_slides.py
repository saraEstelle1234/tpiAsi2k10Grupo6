# -*- coding: utf-8 -*-
"""
apply_palette_all_slides.py
Applies vibrant, elegant color accents across Slides 3, 5, 6, 7, 8, 10, 11, 12, 13, 14.
"""
with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

# 1. Slide 3: Colorful ribbons on the 3 process cards
old_s3_cards = """          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Procesos Estratégicos</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; Planificar la programación de exposiciones<br>
              &bull; Planificar visitas guiadas<br>
              &bull; Definir precios de guía<br>
              &bull; Definir precios de entrada
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #FFFFFF;">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Proceso Esencial</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; <strong>Exponer obras de arte</strong>
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--text-light-secondary);">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 6px;">Procesos de Soporte</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; Gestionar ingreso de obras artísticas<br>
              &bull; Gestionar incidentes y restauración de obras<br>
              &bull; Administrar RRHH
            </div>
          </div>"""

new_s3_cards = """          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #38BDF8; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 42, 0.95) 100%);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 11px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em;">Procesos Estratégicos</span>
              <span style="font-size: 10px; font-weight: 800; background: rgba(56, 189, 248, 0.15); color: #BAE6FD; padding: 2px 7px; border-radius: 4px;">Directrices</span>
            </div>
            <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
              &bull; Planificar la programación de exposiciones<br>
              &bull; Planificar visitas guiadas<br>
              &bull; Definir precios de guía<br>
              &bull; Definir precios de entrada
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #F59E0B; background: linear-gradient(145deg, rgba(32, 36, 60, 0.85) 0%, rgba(16, 20, 36, 0.95) 100%);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 11px; font-weight: 800; color: #FCD34D; text-transform: uppercase; letter-spacing: 0.05em;">Proceso Esencial</span>
              <span style="font-size: 10px; font-weight: 800; background: rgba(245, 158, 11, 0.15); color: #FDE68A; padding: 2px 7px; border-radius: 4px;">Valor Central</span>
            </div>
            <div style="font-size: 14px; line-height: 1.6; color: #FFF;">
              &bull; <strong>Exponer obras de arte</strong>
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #10B981; background: linear-gradient(145deg, rgba(16, 38, 56, 0.85) 0%, rgba(8, 22, 34, 0.95) 100%);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 11px; font-weight: 800; color: #6EE7B7; text-transform: uppercase; letter-spacing: 0.05em;">Procesos de Soporte</span>
              <span style="font-size: 10px; font-weight: 800; background: rgba(16, 185, 129, 0.15); color: #A7F3D0; padding: 2px 7px; border-radius: 4px;">Operatividad</span>
            </div>
            <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
              &bull; Gestionar ingreso de obras artísticas<br>
              &bull; <strong>Gestionar incidentes y restauración de obras</strong><br>
              &bull; Administrar RRHH
            </div>
          </div>"""

if old_s3_cards in text:
    text = text.replace(old_s3_cards, new_s3_cards)
    print('Slide 3 replaced successfully!')
else:
    print('Slide 3 target not found.')

# 2. Slide 8 (RNFs): add subtle cyan and emerald gradient glow
old_s8_grid = """      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: stretch;">
        
        <!-- RNF 1 -->
        <div class="card-dark reveal-item revealed" style="padding: 32px 30px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid var(--blue-accent);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <span style="font-size: 12px; font-weight: 800; color: var(--blue-accent); text-transform: uppercase; letter-spacing: 0.05em;">Arquitectura y Plataforma</span>
              <span style="font-size: 12px; font-weight: 700; background: rgba(45, 127, 249, 0.12); color: #93C5FD; padding: 4px 10px; border-radius: 6px;">Sección 2.4</span>
            </div>
            <h3 style="font-size: 21px; font-weight: 800; color: #FFF; margin-bottom: 12px;">RNF 1 – Módulo Web de Soporte</h3>
            <p style="font-size: 14.5px; line-height: 1.65; color: var(--text-light); margin-bottom: 20px;">
              El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.
            </p>
          </div>

          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 14px 16px;">
            <div style="font-size: 12.5px; font-weight: 700; color: #FFF; margin-bottom: 4px;">Justificación de Calidad</div>
            <div style="font-size: 12.5px; color: var(--text-light-secondary); line-height: 1.5;">
              Facilita el despliegue centralizado, elimina tareas de mantenimiento en terminales y permite a supervisores y restauradores operar desde cualquier equipo del museo.
            </div>
          </div>
        </div>

        <!-- RNF 2 -->
        <div class="card-dark reveal-item revealed" style="padding: 32px 30px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid var(--text-light-secondary);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <span style="font-size: 12px; font-weight: 800; color: var(--text-light-secondary); text-transform: uppercase; letter-spacing: 0.05em;">Usabilidad y Operatividad en Rondas</span>
              <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #CBD5E1; padding: 4px 10px; border-radius: 6px;">Sección 2.4</span>
            </div>
            <h3 style="font-size: 21px; font-weight: 800; color: #FFF; margin-bottom: 12px;">RNF 2 – Interfaz Móvil para Rondas</h3>
            <p style="font-size: 14.5px; line-height: 1.65; color: var(--text-light); margin-bottom: 20px;">
              La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia.
            </p>
          </div>

          <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 14px 16px;">
            <div style="font-size: 12.5px; font-weight: 700; color: #FFF; margin-bottom: 4px;">Justificación de Calidad</div>
            <div style="font-size: 12.5px; color: var(--text-light-secondary); line-height: 1.5;">
              Optimiza la ergonomía del guardia en movimiento, garantizando reportes en tiempo real y reduciendo al mínimo la latencia ante daños en piezas patrimoniales.
            </div>
          </div>
        </div>

      </div>"""

new_s8_grid = """      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: stretch;">
        
        <!-- RNF 1: Cyan / Web Architecture -->
        <div class="card-dark reveal-item revealed" style="padding: 30px 28px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid #38BDF8; background: linear-gradient(145deg, rgba(16, 36, 68, 0.85) 0%, rgba(8, 18, 38, 0.95) 100%); box-shadow: 0 12px 36px rgba(0,0,0,0.4);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <span style="font-size: 11px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.06em;">Arquitectura &bull; Cliente / Servidor</span>
              <span style="font-size: 11px; font-weight: 800; background: rgba(56, 189, 248, 0.15); color: #BAE6FD; padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">RNF 1</span>
            </div>
            <h3 style="font-size: 21px; font-weight: 800; color: #FFF; margin-bottom: 12px;">RNF 1 – Módulo Web de Soporte</h3>
            <p style="font-size: 14px; line-height: 1.65; color: #CBD5E1; margin-bottom: 18px;">
              El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.
            </p>
          </div>

          <div style="background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 10px; padding: 14px 16px;">
            <div style="font-size: 12px; font-weight: 800; color: #38BDF8; text-transform: uppercase; margin-bottom: 4px;">Criterio de Calidad Arquitectónica</div>
            <div style="font-size: 12.5px; color: #E2E8F0; line-height: 1.5;">
              Despliegue centralizado y zero-maintenance en terminales: permite a supervisores y restauradores consultar estados y novedades desde cualquier puesto institucional.
            </div>
          </div>
        </div>

        <!-- RNF 2: Emerald / Mobile UX -->
        <div class="card-dark reveal-item revealed" style="padding: 30px 28px; display: flex; flex-direction: column; justify-content: space-between; border-left: 4px solid #10B981; background: linear-gradient(145deg, rgba(14, 38, 54, 0.85) 0%, rgba(8, 20, 32, 0.95) 100%); box-shadow: 0 12px 36px rgba(0,0,0,0.4);">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
              <span style="font-size: 11px; font-weight: 800; color: #6EE7B7; text-transform: uppercase; letter-spacing: 0.06em;">Usabilidad &bull; Interfaz Táctil Móvil</span>
              <span style="font-size: 11px; font-weight: 800; background: rgba(16, 185, 129, 0.15); color: #A7F3D0; padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(16, 185, 129, 0.3);">RNF 2</span>
            </div>
            <h3 style="font-size: 21px; font-weight: 800; color: #FFF; margin-bottom: 12px;">RNF 2 – Interfaz Móvil para Rondas</h3>
            <p style="font-size: 14px; line-height: 1.65; color: #CBD5E1; margin-bottom: 18px;">
              La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia.
            </p>
          </div>

          <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 10px; padding: 14px 16px;">
            <div style="font-size: 12px; font-weight: 800; color: #6EE7B7; text-transform: uppercase; margin-bottom: 4px;">Criterio de Ergonomía Operativa</div>
            <div style="font-size: 12.5px; color: #E2E8F0; line-height: 1.5;">
              Ergonomía optimizada para el guardia en ronda: botones táctiles generosos, plano interactivo de salas y reporte sin fricción para congelar el daño inmediatamente.
            </div>
          </div>
        </div>

      </div>"""

if old_s8_grid in text:
    text = text.replace(old_s8_grid, new_s8_grid)
    print('Slide 8 replaced successfully!')
else:
    print('Slide 8 target not found.')

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated generate_v9_color_deck.py with multi-slide color accents.')
