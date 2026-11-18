# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Slide count
slide_ids = re.findall(r'id=["\']slide-(\d+)["\']', html)
unique_slides = sorted(list(set(map(int, slide_ids))))
print("Unique slides:", unique_slides)
assert unique_slides == list(range(1, 15)), f"Expected 1..14, got {unique_slides}"

# 2. Slide 14 checks
assert '¡Muchas Gracias!' in html, "¡Muchas Gracias! missing"
assert 'Cattaneo, Marcela F.' in html, "Professor Cattaneo missing"
assert 'Turanzas, Susana B.' in html, "Professor Turanzas missing"
assert 'Sanchez, Claudia E.' in html, "Professor Sanchez missing"
assert 'Padilla, Tomas Lautaro' in html, "Professor Padilla missing"
assert 'Curso 2K10' in html, "Curso 2K10 missing"
assert 'Tarditti, Juan S.' in html, "Tarditti missing in slide 14"
assert 'Leg. 400212' in html, "Legajo 400212 missing in slide 14"

# 3. Slide 4 checks
assert 'Observaciones' in html, "Observaciones missing in Slide 4"
assert 'No aplica' in html, "No aplica missing in Slide 4"

# 4. Slide 12 checks
assert 'height: 610px;' in html, "height: 610px missing in Slide 12"

# 5. Slide 2 checks
assert 'Proceso Esencial del Negocio' in html, "Proceso Esencial missing in Slide 2"

print("ALL VERIFICATIONS PASSED 100% PERFECTLY!")
