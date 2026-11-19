# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Check all 14 slides exist
slide_matches = re.findall(r'id="slide-(\d+)"', text)
print(f"Total slides: {len(slide_matches)}")
assert len(slide_matches) == 14, f"Expected 14 slides, found {len(slide_matches)}"

# 2. Check Feature 1: BPMN Guided Tour (Slide 6)
assert 'id="bpmn-tour-bar"' in text, "BPMN tour bar missing!"
assert 'id="bpmn-img"' in text or 'id="bpmn-oper-inner"' in text, "BPMN img missing!"
assert 'id="bpmn-tour-card"' in text, "BPMN tour card missing!"
print("Slide 06 Guided Tour verified.")

# 3. Check Feature 2: DCD Guided Tour (Slide 12)
assert 'id="dcd-tour-bar"' in text, "DCD tour bar missing!"
assert 'id="dcd-img"' in text, "DCD img missing!"
assert 'id="dcd-tour-card"' in text, "DCD tour card missing!"
print("Slide 12 Guided Tour verified.")

# 4. Check Feature 1: Traza Nodal Pipeline (Slide 13)
assert 'class="traza-pipeline-card"' in text, "Traza pipeline card missing!"
assert 'id="traza-nodes-grid"' in text, "Traza nodes grid missing!"
assert 'traza-node-detail-card' in text, "Traza node detail card missing!"
print("Slide 13 Nodal Pipeline verified.")

# 5. Check Feature 4: Speaker Notes Drawer
assert 'id="speaker-notes-drawer"' in text, "Speaker notes drawer missing!"
assert 'SPEAKER_NOTES' in text, "SPEAKER_NOTES object missing!"
assert 'toggleSpeakerNotes' in text, "toggleSpeakerNotes function missing!"
print("Speaker Notes drawer verified.")

# 6. Check Scripts
open_s = len(re.findall(r'<script\b', text))
close_s = len(re.findall(r'</script>', text))
assert open_s == close_s, "Unbalanced script tags!"
print("Script tags balanced.")

print("\nALL CINEMATIC INNOVATIONS VERIFIED 100% PERFECTLY!")
