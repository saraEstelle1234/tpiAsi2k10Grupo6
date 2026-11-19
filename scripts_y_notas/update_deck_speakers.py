# -*- coding: utf-8 -*-
"""
update_deck_speakers.py
Updates generate_v9_color_deck.py to set the exact 8 active speakers:
- Slide 01: 8 cards of active members
- Slides 02-13: Speaker pills in slide headers
- Slide 14: 8 active members closing credits
"""
import re

with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    code = f.read()

# 1. Update Slide 01 Members Grid to 8 Active Members (4x2 or clean responsive grid)
s1_old_members = """      <!-- 9 Members Grid with Vibrant Thematic Left Ribbons & Color Badges -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #38BDF8; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #38BDF8; background: rgba(56, 189, 248, 0.12); padding: 2px 8px; border-radius: 5px;">01 &bull; Dominio</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 423269</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Dominio bajo estudio y Objetivo general de la organización</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #60A5FA; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #93C5FD; background: rgba(96, 165, 250, 0.14); padding: 2px 8px; border-radius: 5px;">02 &bull; Procesos</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 419166</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Procesos de Negocio y Mapa de Procesos</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #818CF8; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #C7D2FE; background: rgba(129, 140, 248, 0.14); padding: 2px 8px; border-radius: 5px;">03 &bull; Plantilla</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 403382</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Plantilla de Descripción de Proceso y Reglas de Negocio</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #34D399; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #6EE7B7; background: rgba(52, 211, 153, 0.14); padding: 2px 8px; border-radius: 5px;">04 &bull; BPMN</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 402760</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Jastrzebski, Emiliano</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Modelado BPMN a Nivel Descriptivo y Operativo</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #F59E0B; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #FCD34D; background: rgba(245, 158, 11, 0.14); padding: 2px 8px; border-radius: 5px;">05 &bull; Requerimientos</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 419749</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Requerimientos Funcionales y No Funcionales (RF y RNF)</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #06B6D4; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #67E8F9; background: rgba(6, 182, 212, 0.14); padding: 2px 8px; border-radius: 5px;">06 &bull; Casos de Uso</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 408990</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Diagrama de Casos de Uso</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #FB7185; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #FECDD3; background: rgba(251, 113, 133, 0.14); padding: 2px 8px; border-radius: 5px;">07 &bull; CU-15 & Prototipo</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 410975</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Plantilla CU: Registrar Incidente y Prototipo UI</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #A855F7; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #E9D5FF; background: rgba(168, 85, 247, 0.14); padding: 2px 8px; border-radius: 5px;">08 &bull; Clases</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 400212</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Diagrama de Clases del Dominio</div>
        </div>

        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #2DD4BF; background: linear-gradient(145deg, rgba(20, 38, 70, 0.8) 0%, rgba(10, 20, 42, 0.9) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #99F6E4; background: rgba(45, 212, 191, 0.14); padding: 2px 8px; border-radius: 5px;">09 &bull; Trazabilidad</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 418201</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Trazabilidad de Requerimientos y Cierre</div>
        </div>
      </div>"""

s1_new_members = """      <!-- 8 Active Presenting Members Grid (Balanced 4x2 Responsive Layout) -->
      <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
        
        <!-- 1. Cufre, Agustín (Apertura y Cierre) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #38BDF8; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #38BDF8; background: rgba(56, 189, 248, 0.14); padding: 2px 8px; border-radius: 5px;">01-02 &bull; Dominio</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 419166</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Dominio y Objetivos &bull; Trazabilidad y Cierre (13-14)</div>
        </div>

        <!-- 2. Pereyra, Kevin (Mapa de Procesos) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #60A5FA; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #93C5FD; background: rgba(96, 165, 250, 0.14); padding: 2px 8px; border-radius: 5px;">03 &bull; Procesos</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 418201</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Mapa de Procesos Organizacional (Estratégicos / Soporte)</div>
        </div>

        <!-- 3. Molina, Tobias (Plantilla de Proceso) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #818CF8; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #C7D2FE; background: rgba(129, 140, 248, 0.14); padding: 2px 8px; border-radius: 5px;">04 &bull; Plantilla</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 419749</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Plantilla Proceso de Soporte: Gestionar Incidentes</div>
        </div>

        <!-- 4. Marcuzzi, Tomas (BPMN) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #34D399; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #6EE7B7; background: rgba(52, 211, 153, 0.14); padding: 2px 8px; border-radius: 5px;">05-06 &bull; BPMN</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 403382</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Modelado BPMN Nivel Descriptivo y Operativo (4 Carriles)</div>
        </div>

        <!-- 5. Moyano, Lucas Uriel (RF y RNF) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #F59E0B; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #FCD34D; background: rgba(245, 158, 11, 0.14); padding: 2px 8px; border-radius: 5px;">07-08 &bull; Requerimientos</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 410975</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Catálogo de Requerimientos Funcionales y No Funcionales</div>
        </div>

        <!-- 6. Thomas Rapp, Francisco (Casos de Uso) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #06B6D4; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #67E8F9; background: rgba(6, 182, 212, 0.14); padding: 2px 8px; border-radius: 5px;">09 &bull; Casos de Uso</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 408990</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Diagrama de Casos de Uso (DCU General del Sistema)</div>
        </div>

        <!-- 7. Abad, Francisco (CU-15 y Prototipo) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #FB7185; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #FECDD3; background: rgba(251, 113, 133, 0.14); padding: 2px 8px; border-radius: 5px;">10-11 &bull; CU-15 & Mockup</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 423269</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Plantilla CU-15: Registrar Incidente y Prototipo UI</div>
        </div>

        <!-- 8. Tarditti, Juan Sebastián (Diagrama de Clases) -->
        <div class="card-dark" style="padding: 16px 18px; border-left: 3.5px solid #A855F7; background: linear-gradient(145deg, rgba(20, 38, 72, 0.85) 0%, rgba(10, 20, 44, 0.95) 100%);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
            <span style="font-size: 10px; font-weight: 800; color: #E9D5FF; background: rgba(168, 85, 247, 0.14); padding: 2px 8px; border-radius: 5px;">12 &bull; Clases</span>
            <span style="font-size: 11px; color: #94A3B8; font-family: monospace;">Leg: 400212</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: #CBD5E1; margin-top: 4px; line-height: 1.4;">Diagrama de Clases del Dominio (DCD & Multiplicidades)</div>
        </div>

      </div>"""

if s1_old_members in code:
    code = code.replace(s1_old_members, s1_new_members)
    print('Slide 1 updated with 8 active members!')
else:
    print('Slide 1 target not found!')

# 2. Add Speaker Pill to Slide 2 to Slide 13 Headers
speaker_map = {
    'slide-2': ('Agustín Cufre', '419166', '#38BDF8'),
    'slide-3': ('Kevin Pereyra', '418201', '#60A5FA'),
    'slide-4': ('Tobias Molina', '419749', '#818CF8'),
    'slide-5': ('Tomas Marcuzzi', '403382', '#34D399'),
    'slide-6': ('Tomas Marcuzzi', '403382', '#34D399'),
    'slide-7': ('Lucas Moyano', '410975', '#F59E0B'),
    'slide-8': ('Lucas Moyano', '410975', '#F59E0B'),
    'slide-9': ('Francisco Thomas Rapp', '408990', '#06B6D4'),
    'slide-10': ('Francisco Abad', '423269', '#FB7185'),
    'slide-11': ('Francisco Abad', '423269', '#FB7185'),
    'slide-12': ('Juan Sebastián Tarditti', '400212', '#A855F7'),
    'slide-13': ('Agustín Cufre', '419166', '#38BDF8'),
}

for sid, (speaker, legajo, color) in speaker_map.items():
    # find slide header
    pattern = rf'(<div class="slide"[^>]*id="{sid}"[^>]*>.*?<div class="breadcrumb-tag"[^>]*>)(.*?)(</div>)'
    m = re.search(pattern, code, re.DOTALL)
    if m:
        pill = f' <span class="speaker-pill" style="font-size: 11px; font-weight: 800; background: rgba(255,255,255,0.08); color: {color}; border: 1px solid {color}55; padding: 3px 10px; border-radius: 999px; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px;">🎙️ Expone: {speaker}</span>'
        replacement = m.group(1) + m.group(2) + pill + m.group(3)
        code = code[:m.start()] + replacement + code[m.end():]
        print(f'Added speaker pill to {sid}: {speaker}')

# 3. Slide 14: Update team list to 8 active members
s14_old_block = """            <!-- 3x3 Compact Member Grid -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
              
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Tarditti, Juan S.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 400212</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Thomas Rapp, F.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 408990</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Abad, Francisco</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 423269</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Molina, Tobias</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419749</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Moyano, Lucas U.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 410975</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Pereyra, Kevin</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 418201</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Marcuzzi, Tomas</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 403382</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Cufre, Agustín</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419166</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Jastrzebski, E.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 402760</div>
              </div>
            </div>"""

s14_new_block = """            <!-- 8 Active Members Grid (4x2 Clean Layout) -->
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
              
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #38BDF8; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Cufre, Agustín</div>
                <div style="font-size: 11px; color: #38BDF8; font-family: monospace; margin-top: 2px;">Leg. 419166</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #60A5FA; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Pereyra, Kevin</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 418201</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #818CF8; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Molina, Tobias</div>
                <div style="font-size: 11px; color: #818CF8; font-family: monospace; margin-top: 2px;">Leg. 419749</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #34D399; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Marcuzzi, Tomas</div>
                <div style="font-size: 11px; color: #34D399; font-family: monospace; margin-top: 2px;">Leg. 403382</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #F59E0B; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Moyano, Lucas U.</div>
                <div style="font-size: 11px; color: #F59E0B; font-family: monospace; margin-top: 2px;">Leg. 410975</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #06B6D4; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Thomas Rapp, F.</div>
                <div style="font-size: 11px; color: #06B6D4; font-family: monospace; margin-top: 2px;">Leg. 408990</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #FB7185; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Abad, Francisco</div>
                <div style="font-size: 11px; color: #FB7185; font-family: monospace; margin-top: 2px;">Leg. 423269</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-left: 3px solid #A855F7; border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Tarditti, Juan S.</div>
                <div style="font-size: 11px; color: #A855F7; font-family: monospace; margin-top: 2px;">Leg. 400212</div>
              </div>

            </div>"""

if s14_old_block in code:
    code = code.replace(s14_old_block, s14_new_block)
    # Also update "9 Integrantes" tag to "8 Integrantes"
    code = code.replace('9 Integrantes\n              </span>', '8 Integrantes Activos\n              </span>')
    print('Slide 14 updated with 8 active members!')
else:
    print('Slide 14 target not found!')

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('generate_v9_color_deck.py updated successfully with speakers!')
