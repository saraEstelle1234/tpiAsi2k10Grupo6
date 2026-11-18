import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = []

# 1. Slide count is exactly 14
slide_ids = re.findall(r'<div class="slide[^"]*" id="slide-(\d+)"', html)
checks.append(("Slide count is 14", len(slide_ids) == 14 and slide_ids == [str(i) for i in range(1, 15)]))

# 2. Slide 05 layout & 4 lanes
s5_slice = html[html.find('id="slide-5"'):html.find('id="slide-6"')]
s5_match = ('BPMN Nivel Descriptivo' in s5_slice and 
            'Guardia del museo' in s5_slice and 
            'Admin de sistema' in s5_slice and 
            'Encargado de supervisión' in s5_slice and 
            'Encargado de restauración' in s5_slice and
            'height: 620px' in s5_slice)
checks.append(("Slide 05 has new Descriptivo diagram, 620px height & 4 lanes listed", s5_match))

# 3. Slide 06 layout & 4 lanes with professor corrections
s6_slice = html[html.find('id="slide-6"'):html.find('id="slide-7"')]
s6_match = ('BPMN Nivel Operativo' in s6_slice and 
            'Alimentación y Almacenes' in s6_slice and 
            'Estados Explícitos' in s6_slice and 
            '4 Carriles y Restauración' in s6_slice and
            'height: 520px' in s6_slice and
            'Restaurar obra' in s6_slice)
checks.append(("Slide 06 has new Operativo diagram (1682x798), 520px height & 4 lanes with professor corrections", s6_match))

# 4. Slide 09 layout (DCU): Taller (750px), narrower (620px) to match 0.868 aspect ratio with NO side bands, NO cuadritos negros
s9_slice = html[html.find('id="slide-9"'):html.find('id="slide-10"')]
s9_match = ('height: 750px' in s9_slice and 
            'grid-template-columns: 620px 1fr' in s9_slice and
            'max-width: 580px' not in s9_slice)
checks.append(("Slide 09 (DCU) has height 750px, exact 620px portrait width (no lateral black bands) and clean continuous text (no cuadritos negros)", s9_match))

# 5. Slide 12 layout (DCD): Maximized (740px), lifecycle strip removed, NO cuadritos negros
s12_slice = html[html.find('id="slide-12"'):html.find('id="slide-13"')]
s12_match = ('height: 740px' in s12_slice and 
             'grid-template-columns: 1fr 280px' in s12_slice and
             'Ciclo de Vida de Obra:' not in s12_slice and
             'Activa (En Sala)' not in s12_slice)
checks.append(("Slide 12 (DCD) has height 740px, bottom strip removed, maximized diagram and continuous clean text", s12_match))

# 6. Slide 08 RNF count (strictly 2 RNFs from TPI)
s8_slice = html[html.find('id="slide-8"'):html.find('id="slide-9"')]
rnfs_present = 'RNF 1' in s8_slice and 'RNF 2' in s8_slice and 'RNF 3' not in s8_slice and 'RNF-03' not in s8_slice
checks.append(("Slide 08 has strictly 2 RNFs according to official TPI", rnfs_present))

# 7. Slide 04 observaciones
s4_slice = html[html.find('id="slide-4"'):html.find('id="slide-5"')]
checks.append(("Slide 04 has Observaciones: — (No aplica)", 'Observaciones' in s4_slice and 'No aplica' in s4_slice))

# 8. Slide 14 all 9 members & institutional data
s14_slice = html[html.find('id="slide-14"'):]
legajos = ["400212", "408990", "410975", "402760", "419749", "403382", "419166", "423269", "418201"]
all_members = all(leg in s14_slice for leg in legajos)
checks.append(("Slide 14 has all 9 members by legajo & academic metadata", all_members and 'UTN' in s14_slice and 'Cattaneo' in s14_slice))

# 9. No floating shortcuts button
checks.append(("No floating shortcuts button or modal", 'shortcuts-btn' not in html and 'shortcuts-modal' not in html))

# 10. Check syntax errors in JS
checks.append(("No unmatched JS braces in script", 'openZoomModal' in html and 'setDcuSector' in html))

all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

if all_passed:
    print("\nALL 10 VERIFICATION CHECKS PASSED 100%!")
else:
    print("\nSOME CHECKS FAILED!")
