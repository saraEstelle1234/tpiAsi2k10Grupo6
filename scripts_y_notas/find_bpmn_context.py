with open("CONTEXTO_EVALUACION_GRUPAL_ASI.md", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = [l for l in text.splitlines() if 'bpmn' in l.lower() or 'carril' in l.lower() or 'ronda' in l.lower() or 'supervisor' in l.lower()]
print("Found lines:", len(matches))
for m in matches[:30]:
    print(" -", m[:100])
