with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

old_incident = '''              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Gestión de Incidentes</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La entidad <code>Incidente</code> documenta fecha, hora y descripción, vinculada a su <code>TipoIncidente</code> y a la <code>Obra</code> afectada.
                </div>
              </div>'''

new_incident = '''              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Gestión de Incidentes (1..1)</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La entidad <code>Incidente</code> documenta fecha, hora y descripción. Multiplicidad <strong>1</strong> hacia <code>TipoIncidente</code> y <strong>1</strong> hacia <code>Obra</code>.
                </div>
              </div>'''

old_guardia = '''              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Vigilancia y Rondas</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La relación entre <code>Guardia</code> y <code>Sala</code> se asienta mediante la clase asociativa <code>SalaXGuardia</code>, auditando fecha y hora de ronda.
                </div>
              </div>'''

new_guardia = '''              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Vigilancia y Rondas (1..*)</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  Auditoría de rondas mediante clase asociativa <code>SalaXGuardia</code>. Multiplicidad <strong>1..*</strong> desde <code>Sala</code> y <strong>1</strong> hacia <code>Guardia</code>.
                </div>
              </div>'''

old_tip = '''            <div style="font-size: 12px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Hacé clic en el diagrama o en 'Ampliar' para explorar todas las clases, atributos y métodos en alta resolución.</em>
            </div>'''

new_tip = '''            <div style="font-size: 12px; color: #93C5FD; line-height: 1.45;">
              ✨ <strong>Multiplicidades Verificadas:</strong> <code>Incidente &rarr; (1) TipoIncidente</code> | <code>Sala &rarr; (1..*) SalaXGuardia</code>. Clic en 'Ampliar' para explorar atributos y métodos.
            </div>'''

print('old_incident found:', old_incident in html)
print('old_guardia found:', old_guardia in html)
print('old_tip found:', old_tip in html)

if old_incident in html and old_guardia in html and old_tip in html:
    html = html.replace(old_incident, new_incident)
    html = html.replace(old_guardia, new_guardia)
    html = html.replace(old_tip, new_tip)
    with open('presentacion.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated presentacion.html and index.html successfully!')
else:
    print('Could not find all blocks to replace.')
