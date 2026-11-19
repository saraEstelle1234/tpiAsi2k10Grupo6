# -*- coding: utf-8 -*-
"""
perfect_s9_and_zooms.py
1. Fixes Slide 09 grid to 1fr 320px
2. Wraps dcu-img with #dcu-inner (aspect-ratio: 1455/1675) and overrides max-height: 100% !important
3. Sets laser coordinates for BPMN (s6), DCU (s9), DCD (s12)
"""

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Slide 09 Grid
idx_s9 = html.find('id="slide-9"')
idx_s9_end = html.find('id="slide-10"')
s9_chunk = html[idx_s9:idx_s9_end]

# Replace grid-template-columns in slide 9
s9_chunk = s9_chunk.replace(
    'style="display: grid; grid-template-columns: 620px 1fr; gap: 24px; align-items: stretch;"',
    'style="display: grid; grid-template-columns: 1fr 320px; gap: 20px; align-items: stretch;"'
)

# Replace the diagram container in slide 9
target_s9_container = """<div class="card-dark reveal-item revealed" style="height: 750px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; background: #121212; border-radius: 10px; width: 100%; height: 100%;">
              <img id="dcu-img" """

replacement_s9_container = """<div class="card-dark reveal-item revealed" style="height: 750px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1); background: #0A1128;">
            <div class="cinematic-viewport dark-bg" style="flex: 1; width: 100%; height: 100%; overflow: hidden; position: relative; border-radius: 10px; display: flex; align-items: center; justify-content: center; background: #060B14;">
              <div id="dcu-inner" style="height: 100%; aspect-ratio: 1455 / 1675; display: flex; align-items: center; justify-content: center; transform-origin: 50% 50%; transition: transform 0.85s cubic-bezier(0.2, 0.8, 0.2, 1); will-change: transform;">
                <img id="dcu-img" style="width: 100%; height: 100%; max-height: 100% !important; max-width: 100% !important; object-fit: fill; display: block;" """

if target_s9_container in s9_chunk:
    s9_chunk = s9_chunk.replace(target_s9_container, replacement_s9_container)
    # Close the extra div for #dcu-inner
    idx_act = s9_chunk.find('<div class="diagram-action-bar"')
    s9_chunk = s9_chunk[:idx_act] + '</div>\n          ' + s9_chunk[idx_act:]
    print("Slide 09 container perfectly upgraded!")
else:
    print("Warning: target_s9_container not found!")

html = html[:idx_s9] + s9_chunk + html[idx_s9_end:]

# Slide 06 (BPMN) height upgrade to 640px
html = html.replace('style="height: 500px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);"',
                    'style="height: 640px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);"')

# Slide 12 button text
html = html.replace('⑤ Multiplicidades Corregidas', '⑤ Asignación Sala y Guardia')

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Synchronized presentacion.html and index.html!")
