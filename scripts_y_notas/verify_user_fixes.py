# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("--- 1. Top of file check ---")
print(repr(text[:60]))
assert text.startswith('<!DOCTYPE html>\n<html lang="es">'), "Top of file invalid!"
# Check no stray CTYPE html>
assert ' CTYPE html>' not in text and '\nCTYPE html>' not in text, "Stray CTYPE html> found!"

print("\n--- 2. Speaker-pill check ---")
speaker_pills = re.findall(r'<span class="speaker-pill"[^>]*>.*?</span>', text)
print(f"Remaining speaker pills in slides: {len(speaker_pills)}")
assert len(speaker_pills) == 0, "Speaker pills should be 0!"

print("\n--- 3. Slide 09 check ---")
assert 'id="dcu-tour-bar"' in text, "dcu-tour-bar missing!"
assert 'id="dcu-tour-card"' in text, "dcu-tour-card missing!"
assert 'id="dcu-tour-tag"' in text, "dcu-tour-tag missing!"
assert 'setDcuSector' in text, "setDcuSector missing!"
assert 'DCU_ACTOR_STEPS' in text, "DCU_ACTOR_STEPS missing!"
print("Slide 09 DCU Sectorization: OK")

print("\n--- 4. Slide 12 check ---")
assert 'id="dcd-tour-bar"' in text, "dcd-tour-bar missing!"
assert 'id="dcd-tour-card"' in text, "dcd-tour-card missing!"
assert 'id="dcd-tour-tag"' in text, "dcd-tour-tag missing!"
assert 'setDcdTour' in text, "setDcdTour missing!"
assert 'DCD_TOUR_STEPS' in text, "DCD_TOUR_STEPS missing!"
print("Slide 12 DCD Tour & Card: OK")

print("\n--- 5. Script tags check ---")
open_scripts = len(re.findall(r'<script\b', text))
close_scripts = len(re.findall(r'</script>', text))
print(f"Script tags: <script>={open_scripts}, </script>={close_scripts}")
assert open_scripts == close_scripts, "Unbalanced script tags!"

print("\n--- 6. Length and index.html match ---")
with open('index.html', 'r', encoding='utf-8') as f:
    idx_text = f.read()
assert len(text) == len(idx_text), "presentacion.html and index.html sizes do not match!"
print(f"Sizes match: {len(text)} bytes.")

print("\nALL VERIFICATIONS PASSED 100% PERFECTLY!")
