with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

s14_start = text.find('id="slide-14"')
grid_start = text.find('<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">', s14_start)
j_end = text.find('Leg. 402760</div>\n              </div>\n\n            </div>', grid_start)
target_end = j_end + len('Leg. 402760</div>\n              </div>\n\n            </div>')

print('grid_start:', grid_start, 'target_end:', target_end)

new_grid = """<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
              
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

text = text[:grid_start] + new_grid + text[target_end:]
text = text.replace('9 Integrantes', '8 Integrantes Activos')

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated Slide 14 successfully!')
