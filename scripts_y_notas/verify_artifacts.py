# -*- coding: utf-8 -*-
import os

artifact_dir = r"C:\Users\thoma\.gemini\antigravity\brain\5086ba7a-0eba-448a-b21d-e90862728035"
html_path = os.path.join(artifact_dir, "presentacion.html")
md_path = os.path.join(artifact_dir, "guion_defensa_tpi.md")

with open(html_path, 'r', encoding='utf-8') as f:
    html_text = f.read()

with open(md_path, 'r', encoding='utf-8') as f:
    md_text = f.read()

assert 'id="slide-14"' in html_text, "Slide 14 missing in artifact HTML"
assert 'id="slide-15"' not in html_text, "Slide 15 should not exist in artifact HTML"
assert 'const totalSlides = 14;' in html_text, "totalSlides=14 missing in artifact HTML"
assert 'RF-35' in html_text, "RF-35 missing in artifact HTML"
assert '14 slides' in md_text, "14 slides missing in MD"
assert 'Juan Sebastián Tarditti' in md_text, "Juan Tarditti missing in MD"
assert 'Kevin Pereyra' in md_text, "Kevin Pereyra missing in MD"

print("Artifact checks verified successfully!")
