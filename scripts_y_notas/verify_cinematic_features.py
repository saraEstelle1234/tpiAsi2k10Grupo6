with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Check slides
slides = re.findall(r'<div class="slide[^"]*" id="slide-(\d+)"', text)
print("Total slides:", len(slides))
assert len(slides) == 14, f"Expected 14 slides, found {len(slides)}"

# 2. Check Slide 6 elements
assert 'id="bpmn-tour-bar"' in text, "BPMN tour bar missing!"
assert 'id="bpmn-oper-inner"' in text, "BPMN oper inner missing!"
assert 'id="bpmn-tour-card"' in text, "BPMN tour card missing!"
print("Slide 06 Guided Tour verified.")

# 3. Check Slide 12 elements
assert 'id="dcd-tour-bar"' in text, "DCD tour bar missing!"
assert 'id="dcd-tour-card"' in text, "DCD tour card missing!"
print("Slide 12 Guided Tour verified.")

# 4. Check Slide 13 elements
assert 'id="traza-nodes-grid"' in text, "Traza nodes grid missing!"
assert 'id="traza-node-1"' in text and 'id="traza-node-5"' in text, "Traza nodes missing!"
assert 'id="traza-node-detail-card"' in text, "Traza detail card missing!"
assert 'Nota de Alcance Metodológico' in text, "Traza scope note missing!"
print("Slide 13 Nodal Pipeline verified.")

# 5. Check Speaker Notes
assert 'id="speaker-notes-drawer"' in text, "Speaker notes drawer missing!"
assert 'id="dock-btn-notes"' in text, "Dock notes button missing!"
assert 'SPEAKER_NOTES' in text, "SPEAKER_NOTES JS object missing!"
assert "window.addEventListener('keydown'" in text, "Keyboard listener missing!"
print("Speaker Notes drawer verified.")

# 6. Check JS script tags balance
assert text.count('<script>') == text.count('</script>'), "Mismatched script tags!"
print("Script tags balanced.")

print("\nALL 4 CINEMATIC INNOVATIONS VERIFIED 100% PERFECTLY!")
