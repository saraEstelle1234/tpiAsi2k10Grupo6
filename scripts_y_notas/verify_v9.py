# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Check garantia de integridad
assert 'garantía de integridad' not in html.lower(), "Found 'garantía de integridad' in HTML!"
assert 'trazabilidad 100%' not in html.lower(), "Found 'TRAZABILIDAD 100%' in HTML!"

# 2. Check Slide 9
assert 'id="slide-9"' in html, "Slide 9 missing"
assert 'height: 580px;' in html, "height 580px missing"

# 3. Check Slide 12
assert 'id="slide-12"' in html, "Slide 12 missing"
# Check no wall of text on reingreso
assert 'Sustento de la RN-1: toda obra reparada' not in html, "Old reingreso text still in Slide 12"

# 4. Check Slide 13
assert 'id="slide-13"' in html, "Slide 13 missing"
assert 'font-size: 15px; color: #FFFFFF; font-weight: 600;' in html, "New larger trace item font missing"

# 5. Check Slide 7
assert '.rf-item {' in html, "rf-item CSS missing"
assert 'font-size: 15.5px;' in html, "rf-item 15.5px missing"

# 6. Check total slides
slide_ids = re.findall(r'id=["\']slide-(\d+)["\']', html)
unique_slides = sorted(list(set(map(int, slide_ids))))
print(f"Unique slides: {unique_slides}")
assert unique_slides == list(range(1, 15)), f"Expected 1..14, got {unique_slides}"

print("ALL V9 AUDIT CHECKS PASSED 100% PERFECTLY!")
