# -*- coding: utf-8 -*-
"""
apply_palette_v9.py
Modifies generate_v9_color_deck.py to introduce the enhanced multi-color palette,
embeds the museum photograph on Slide 1 & Slide 2, and runs it to compile presentacion.html and index.html.
"""
import re, base64

with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    code = f.read()

# 1. SLIDE 1 REPLACEMENT
s1_old_pattern = r'<!-- SLIDE 1: PORTADA & EQUIPO -->.*?<!-- SLIDE 2: DOMINIO & OBJETIVOS -->'
s1_new = """<!-- SLIDE 1: PORTADA & EQUIPO -->
    <div class="slide active" id="slide-1" data-topic="01 · Portada y Equipo">
      <div class="card-dark" style="margin-bottom: 24px; position: relative; overflow: hidden; padding: 36px 40px; border: 1px solid rgba(56, 189, 248, 0.25); background: linear-gradient(145deg, rgba(16, 32, 62, 0.9) 0%, rgba(8, 16, 32, 0.95) 100%); box-shadow: 0 16px 44px rgba(0,0,0,0.45);">
        <div style="position: absolute; right: -30px; bottom: -30px; opacity: 0.15; pointer-events: none;">
          <svg width="340" height="340" viewBox="0 0 200 200" fill="none">
            <path d="M0 100 C 40 40, 160 160, 200 100" stroke="#38BDF8" stroke-width="24" fill="none"/>
            <path d="M0 130 C 40 70, 160 190, 200 130" stroke="#2F6BFF" stroke-width="12" fill="none"/>
            <circle cx="160" cy="50" r="30" stroke="#38BDF8" stroke-width="8"/>
          </svg>
        </div>

        <!-- Museum Official Case Floating Pill -->
        <div style="display: inline-flex; align-items: center; gap: 10px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 999px; padding: 4px 16px 4px 6px; margin-bottom: 14px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
          <img src="data:image/png;base64,{b64_museum}" alt="Museo" style="width: 26px; height: 26px; border-radius: 50%; object-fit: cover; border: 1.5px solid #38BDF8;">
          <span style="font-size: 11.5px; font-weight: 800; color: #BAE6FD; text-transform: uppercase; letter-spacing: 0.06em;">Museo de Historia Natural &bull; Caso Oficial 2026</span>
        </div>

        <div class="breadcrumb-tag" style="background: rgba(45, 127, 249, 0.15); color: #93C5FD; border-color: rgba(45, 127, 249, 0.3);">
          {svg_asterisk} Trabajo Práctico Integrador &bull; Análisis de Sistemas de Información
        </div>
        <h1 class="giant-title" style="background: linear-gradient(135deg, #FFFFFF 0%, #BAE6FD 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
          Sistema de Gestión y Vigilancia Museológica
        </h1>
        <p class="editorial-subtitle" style="color: #CBD5E1;">
          Cátedra de Análisis de Sistemas &bull; Curso 2K10 &bull; Año 2026 &bull; Equipo Grupo 6
        </p>

        <div style="display: flex; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="nextSlideAction()" style="background: linear-gradient(135deg, #2D7FF9 0%, #0284C7 100%); box-shadow: 0 8px 24px rgba(45, 127, 249, 0.35);">
            Comenzar presentación {svg_arrow_right}
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()">
            {svg_grid} Ver los 14 slides
          </button>
        </div>
      </div>

      <!-- 9 Members Grid with Vibrant Thematic Left Ribbons & Color Badges -->
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
      </div>
    </div>
    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->"""

code = re.sub(s1_old_pattern, s1_new, code, flags=re.DOTALL)

# 2. SLIDE 2 REPLACEMENT (WITH MUSEUM PHOTOGRAPH SHOWCASE)
s2_old_pattern = r'<!-- SLIDE 2: DOMINIO & OBJETIVOS -->.*?<!-- SLIDE 3: MAPA DE PROCESOS -->'
s2_new = """<!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide" id="slide-2" data-topic="02 · Dominio y Objetivos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 16px;">
        <div>
          <div class="breadcrumb-tag" style="background: rgba(245, 158, 11, 0.12); color: #FCD34D; border-color: rgba(245, 158, 11, 0.3);">
            02 &bull; Dominio y Objetivos
          </div>
          <h1 class="giant-title">Dominio bajo Estudio</h1>
          <p class="editorial-subtitle">
            Museo de Historia Natural &bull; Contexto institucional, patrimonio artístico y objetivos de la organización
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 6px;">
          {svg_museum_arch}
        </div>
      </div>

      <!-- Top Section: Real Museum Photograph Showcase + Operational Overview -->
      <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 20px; margin-bottom: 20px;">
        
        <!-- Museum Official Photograph Card -->
        <div class="card-dark reveal-item revealed" style="padding: 12px; display: flex; flex-direction: column; justify-content: space-between; border: 1.5px solid rgba(56, 189, 248, 0.35); background: linear-gradient(145deg, rgba(20, 38, 72, 0.9) 0%, rgba(10, 20, 42, 0.95) 100%); box-shadow: 0 12px 36px rgba(0,0,0,0.45);">
          <div style="position: relative; overflow: hidden; border-radius: 10px; height: 185px; width: 100%; box-shadow: 0 8px 24px rgba(0,0,0,0.5);">
            <img src="data:image/png;base64,{b64_museum}" alt="Museo de Historia Natural" style="width: 100%; height: 100%; object-fit: cover;">
            <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(7, 16, 30, 0.95) 0%, rgba(7, 16, 30, 0.6) 60%, transparent 100%); padding: 10px 14px;">
              <span style="font-size: 11px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.06em;">Fotografía Oficial del Dominio</span>
              <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-top: 2px;">Museo de Historia Natural &bull; Sala de Exhibiciones</div>
            </div>
          </div>
          <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 10px; padding: 0 4px;">
            <span style="font-size: 12px; color: #93C5FD; line-height: 1.4;">Colección de paleontología, obras animadas y patrimonio histórico</span>
            <span style="font-size: 11px; font-weight: 800; background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">Caso TPI 2026</span>
          </div>
        </div>

        <!-- 2 Clean Domain Operations Cards -->
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed" style="border-left: 3.5px solid #38BDF8; padding: 16px 20px;">
            <div style="font-size: 11.5px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Organización y Operatoria del Dominio</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El museo expone colecciones de artistas locales, nacionales e internacionales. El público ingresa mediante cobro de entradas generales, con opción arancelada de visitas guiadas. Las piezas ingresan por compra, donación o préstamo, registrándose autor, estilo, dimensiones, material y valuación.
            </div>
          </div>
          <div class="card-dark reveal-item revealed" style="border-left: 3.5px solid #F59E0B; padding: 16px 20px;">
            <div style="font-size: 11.5px; font-weight: 800; color: #FCD34D; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Salas Temáticas y Monitoreo de Objetos Animados</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Distribuido en salas temáticas con objetos animados sensibles a estímulos físicos según su material. El guardia efectúa rondas de vigilancia diaria priorizando salas críticas, reportando de inmediato observaciones o novedades.
            </div>
          </div>
        </div>

      </div>

      <!-- 3 Structured Objective Cards Strictly from TPI Section 1.1, 2.1 & 2.3 -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark reveal-item revealed" style="padding: 18px 20px; border-left: 3.5px solid #38BDF8;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 11px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em;">Sección 1.1 del TPI</span>
            <span style="font-size: 11px; background: rgba(56, 189, 248, 0.12); color: #BAE6FD; padding: 2px 7px; border-radius: 4px;">Misión</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 6px;">Objetivo de la Organización</div>
          <div style="font-size: 13px; color: #CBD5E1; line-height: 1.5;">
            Exponer obras al público mediante el cobro de entradas, preservando el patrimonio con un sistema integrado de gestión de incidentes.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 18px 20px; border-left: 3.5px solid #F59E0B;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 11px; font-weight: 800; color: #FCD34D; text-transform: uppercase; letter-spacing: 0.05em;">Sección 2.1 del TPI</span>
            <span style="font-size: 11px; background: rgba(245, 158, 11, 0.14); color: #FDE68A; padding: 2px 7px; border-radius: 4px;">Esencial</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 6px;">Proceso Esencial</div>
          <div style="font-size: 13px; color: #CBD5E1; line-height: 1.5;">
            <strong>Exponer obras de arte:</strong> Corazón operativo del museo y cliente receptor directo de las obras preservadas por el sistema.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 18px 20px; border-left: 3.5px solid #818CF8;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 11px; font-weight: 800; color: #C7D2FE; text-transform: uppercase; letter-spacing: 0.05em;">Sección 2.3 del TPI</span>
            <span style="font-size: 11px; background: rgba(129, 140, 248, 0.14); color: #E0E7FF; padding: 2px 7px; border-radius: 4px;">Soporte</span>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 6px;">Objetivo del Proceso Bajo Estudio</div>
          <div style="font-size: 13px; color: #CBD5E1; line-height: 1.5;">
            Gestionar incidentes y restauración de obras mediante rondas de vigilancia del guardia, notificando para que los supervisores resuelvan el destino de la obra.
          </div>
        </div>
      </div>
    </div>
    <!-- SLIDE 3: MAPA DE PROCESOS -->"""

code = re.sub(s2_old_pattern, s2_new, code, flags=re.DOTALL)

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated generate_v9_color_deck.py with Slide 1 and Slide 2 color upgrades and museum photo!')
