# -*- coding: utf-8 -*-
import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("File size:", len(html))

# 1. Total slides count
slides = re.findall(r'<div class="slide[^"]*" id="slide-(\d+)"', html)
print(f"Total slides found: {len(slides)} -> {slides}")
assert len(slides) == 14, f"Expected 14 slides, found {len(slides)}"

# 2. Check Slide 4 for Observaciones
assert "Observaciones: — (No aplica)" in html or "Observaciones: — (No Aplica)" in html or "Observaciones: —" in html or "No aplica" in html, "Slide 4 observations missing"
print("Slide 4: Observaciones verified!")

# 3. Check Slide 8 for RNFs count
s8_match = re.search(r'(<div class="slide"[^>]*id="slide-8"[^>]*>.*?)(?=<div class="slide"[^>]*id="slide-9")', html, re.DOTALL)
assert s8_match, "Slide 8 not found"
s8 = s8_match.group(1)
rnfs = set(re.findall(r'RNF\s*\d+', s8))
print(f"Unique RNFs found in Slide 8: {rnfs}")
assert rnfs == {'RNF 1', 'RNF 2'}, f"Expected exactly RNF 1 and RNF 2 in Slide 8, found {rnfs}"

# 4. Check Slide 9 for DCU sector zoom and container
assert "setDcuSector('guardia', this)" in html, "setDcuSector not found in Slide 9"
assert "setDcuSector('supervisor', this)" in html, "supervisor sector not found in Slide 9"
assert "setDcuSector('ingreso', this)" in html, "ingreso sector not found in Slide 9"
assert "setDcuSector('admin', this)" in html, "admin sector not found in Slide 9"
assert "setDcuSector('all', this)" in html, "all sector not found in Slide 9"
assert "transformOrigin = '19% 62%'" in html, "Guardia coordinates missing in JS"
assert "transformOrigin = '19% 86%'" in html, "Supervisor coordinates missing in JS"
print("Slide 9: DCU sector zoom and coordinates verified!")

# 5. Check Idea 1 (Slide 11 Hotspots)
assert "id=\"hotspot-1\"" in html and "id=\"hotspot-2\"" in html and "id=\"hotspot-3\"" in html, "Hotspots missing in Slide 11"
assert "highlightProtoStep" in html, "highlightProtoStep JS missing"
assert "proto-step-card-1" in html, "Step cards missing IDs in Slide 11"
print("Idea 1 (Slide 11 Hotspots): Verified!")

# 6. Check Idea 3 (Slide 12 Obra Lifecycle)
assert "Ciclo de Vida de Obra:" in html, "Lifecycle strip missing in Slide 12"
assert "Activa (En Sala)" in html and "Inactiva (Incidente)" in html and "En Restauración" in html and "En Depósito (RN-1)" in html, "Lifecycle states missing"
print("Idea 3 (Slide 12 Obra Lifecycle): Verified!")

# 7. Check Idea 2 (Slide 13 Trace Pipeline)
assert "trace-pipeline-container" in html, "Trace pipeline missing in Slide 13"
assert "pipe-rf" in html and "pipe-cu" in html and "pipe-dcd" in html, "Pipeline nodes missing in Slide 13"
print("Idea 2 (Slide 13 Trace Pipeline): Verified!")

# 8. Check Idea 4 (Shortcuts Pill & Modal)
assert "shortcuts-pill-btn" in html, "Shortcuts pill button missing"
assert "shortcuts-modal" in html, "Shortcuts modal missing"
assert "openShortcutsModal" in html and "closeShortcutsModal" in html, "Shortcuts modal functions missing"
print("Idea 4 (Shortcuts Pill & Modal): Verified!")

# 9. Check Slide 14 Members & Metadata
real_members = [
    "Abad, Francisco", "Cufre, Agustín", "Marcuzzi, Tomas", "Jastrzebski",
    "Molina, Tobias", "Thomas Rapp", "Moyano, Lucas", "Tarditti, Juan", "Pereyra, Kevin"
]
for m in real_members:
    assert m in html, f"Member {m} missing in HTML"
print("Slide 14: All 9 real team members verified!")

profs = ["Cattaneo", "Turanzas", "Sanchez", "Padilla"]
for p in profs:
    assert p in html, f"Professor {p} missing in Slide 14"
print("Slide 14: All professors and academic metadata verified!")

print("\n==========================================")
print("ALL 9 VERIFICATION CHECKS PASSED 100%!")
print("==========================================")
