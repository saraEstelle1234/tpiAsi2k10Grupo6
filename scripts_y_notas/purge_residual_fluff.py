# -*- coding: utf-8 -*-
"""
purge_residual_fluff.py
Cleans up any remaining non-literal filler phrases:
1. Slide 2: Remove unnecessary expandable filler prose; keep literal TPI definitions.
2. Slide 5: Make BPMN Descriptivo card 100% direct and concise.
3. Slide 11: Make prototype cards strictly match CU-15 steps 1-14 from Section 2.8 without marketing jargon.
"""

with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Slide 2: Clean cards without extra fluff
old_s2_cards = """      <!-- 3 Expandable Objective Cards Strictly from TPI -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">01</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Objetivo General de la Organización</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas, preservando las obras con un sistema de gestión de incidentes.
          </div>
          <div class="card-extra-content">
            Definido textualmente en la Sección 1.1 del TPI: sostener la exposición de arte como proceso esencial y financiar las actividades mediante el cobro de entradas y servicios de guía, asegurando la conservación integral del patrimonio.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">02</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Objetivo del Proceso de Vigilancia</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Gestionar incidentes y restauración de obras mediante las rondas de vigilancia del guardia, registrando en el Módulo Web.
          </div>
          <div class="card-extra-content">
            Definido en la plantilla de proceso (Sección 2.3): permitir que los supervisores tomen medidas en relación a la obra, tales como envío a restauración, registro de baja de obra o refuerzo de vigilancia en sectores conflictivos.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">03</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Proceso Esencial del Negocio</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Exponer obras de arte: proceso clave que entrega valor a la comunidad y cliente del proceso de vigilancia.
          </div>
          <div class="card-extra-content">
            Definido en la Sección 2.1 del TPI: la exposición artística es el proceso sustantivo sobre el cual se articulan las rondas de inspección física y la custodia del patrimonio cultural.
          </div>
        </div>
      </div>"""

new_s2_cards = """      <!-- 3 Clean Objective Cards Strictly from TPI Section 1.1 & 2.1 -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #60A5FA; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 1.1 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Objetivo de la Organización</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas, preservando las obras con un sistema de gestión de incidentes.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 2.1 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Proceso Esencial</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            <strong>Exponer obras de arte:</strong> Proceso central de la organización y cliente receptor de las obras protegidas por el sistema de vigilancia.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #818CF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 2.3 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Objetivo del Proceso Bajo Estudio</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            Gestionar incidentes y restauración de obras mediante las rondas de vigilancia del guardia, registrando en el Módulo Web para que los supervisores tomen medidas.
          </div>
        </div>
      </div>"""

if old_s2_cards in code:
    code = code.replace(old_s2_cards, new_s2_cards)
    print("Purged Slide 2 cards successfully!")
else:
    print("WARNING: old_s2_cards not found")

# 2. Slide 5: Clean BPMN description
old_s5_p = """            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              Modela el flujo global de negocio de punta a punta entre los actores clave: <strong>Guardia del Museo</strong>, <strong>Módulo Web</strong> y <strong>Supervisor</strong>, prescindiendo del detalle de software para brindar una perspectiva ejecutiva del proceso de vigilancia y respuesta.
            </p>"""

new_s5_p = """            <p style="font-size: 13.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              Flujo global de negocio entre los tres actores clave: <strong>Guardia del Museo</strong>, <strong>Módulo Web</strong> y <strong>Supervisor</strong> (Sección 2.5 del TPI).
            </p>"""

if old_s5_p in code:
    code = code.replace(old_s5_p, new_s5_p)
    print("Purged Slide 5 paragraph successfully!")

# 3. Slide 11: Clean prototype card 3
old_s11_c3 = """<div class="card-dark reveal-item revealed" style="border-top: 3px solid #38BDF8; padding: 18px 20px;">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">3. Confirmación Segura (Pasos 9 a 14)</div>
          <div style="font-size: 13px; line-height: 1.55; color: var(--text-light);">
            Botón de confirmación con diálogo modal que previene registros involuntarios antes de impactar en la base de datos.
          </div>
        </div>"""

new_s11_c3 = """<div class="card-dark reveal-item revealed" style="border-top: 3px solid #38BDF8; padding: 18px 20px;">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">3. Confirmación y Registro (Pasos 9 a 12)</div>
          <div style="font-size: 13px; line-height: 1.55; color: var(--text-light);">
            El sistema solicita confirmación del incidente, el guardia confirma y la obra pasa a estado 'Inactivo' con registro de hora.
          </div>
        </div>"""

if old_s11_c3 in code:
    code = code.replace(old_s11_c3, new_s11_c3)
    print("Purged Slide 11 card 3 successfully!")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_v8_deck.py purged of residual fluff!")
