# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Check Slide 7
assert 'id="rf-col-left"' in html, "Missing #rf-col-left"
assert 'id="rf-col-right"' in html, "Missing #rf-col-right"
assert 'initExclusiveAccordion()' in html, "Missing initExclusiveAccordion call"

# Check RF groups
rf_groups = re.findall(r'<details class="rf-group"[^>]*>', html)
print(f"Total RF groups in Slide 7: {len(rf_groups)}")
assert len(rf_groups) == 15, f"Expected 15 RF groups, got {len(rf_groups)}"

# Check Slide 8
assert 'RNF 1 &bull; Módulo Web de Soporte' in html, "Missing RNF 1"
assert 'RNF 2 &bull; Interfaz móvil para rondas' in html, "Missing RNF 2"

rnf3 = re.findall(r'RNF\s*3', html)
rnf4 = re.findall(r'RNF\s*4', html)
rnf5 = re.findall(r'RNF\s*5', html)
rnf6 = re.findall(r'RNF\s*6', html)

print(f"Occurrences of RNF 3..6: {len(rnf3)}, {len(rnf4)}, {len(rnf5)}, {len(rnf6)}")
assert len(rnf3) == 0, f"Found {len(rnf3)} occurrences of RNF 3"
assert len(rnf4) == 0, f"Found {len(rnf4)} occurrences of RNF 4"
assert len(rnf5) == 0, f"Found {len(rnf5)} occurrences of RNF 5"
assert len(rnf6) == 0, f"Found {len(rnf6)} occurrences of RNF 6"

# Check slide count is still 14
slide_ids = re.findall(r'id=["\']slide-(\d+)["\']', html)
unique_slides = sorted(list(set(map(int, slide_ids))))
print(f"Slide IDs found: {unique_slides}")
assert unique_slides == list(range(1, 15)), f"Expected slides 1..14, got {unique_slides}"

print("ALL CHECKS PASSED PERFECTLY!")
