import re
import shutil
import subprocess

def update_name(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update button text in the tour bar
    btn_target = '<button class="tour-btn" onclick="setBpmnTour(3, this)">④ Acciones Sugeridas</button>'
    btn_replacement = '<button class="tour-btn" onclick="setBpmnTour(3, this)">④ Tipificación de Incidente</button>'
    if btn_target in content:
        content = content.replace(btn_target, btn_replacement)
        print(f"[{filepath}] Replaced button label with '④ Tipificación de Incidente'")
    else:
        print(f"[{filepath}] Button target not found directly!")

    # 2. Update step in BPMN_TOUR_STEPS
    step_target = """      {
        title: "Fase 3: Consulta de Acciones Sugeridas",
        desc: "El sistema propone inmediatamente la acción preventiva según el material del objeto (deterioro provocado, caída accidental o deterioro natural).",
        tag: "PASO 3 DE 4 · ACCIONES SUGERIDAS",
        transform: "scale(2.05) translate(-6%, 0%)"
      },"""

    step_replacement = """      {
        title: "Fase 3: Tipificación del Incidente",
        desc: "El sistema clasifica el tipo de daño (deterioro provocado, accidental o natural) y propone la acción preventiva según el material del objeto.",
        tag: "PASO 3 DE 4 · TIPIFICACIÓN DE INCIDENTE",
        transform: "scale(2.05) translate(-6%, 0%)"
      },"""

    if step_target in content:
        content = content.replace(step_target, step_replacement)
        print(f"[{filepath}] Replaced BPMN_TOUR_STEPS[3] title and tag")
    else:
        print(f"[{filepath}] step_target not found directly, checking regex...")
        content = re.sub(
            r'title:\s*"Fase 3:[^"]*",\s*desc:\s*"[^"]*",\s*tag:\s*"PASO 3 DE 4 · [^"]*",\s*transform:\s*"scale\(2\.05\) translate\(-6%,\s*0%\)"',
            'title: "Fase 3: Tipificación del Incidente",\n        desc: "El sistema clasifica el tipo de daño (deterioro provocado, accidental o natural) y propone la acción preventiva según el material del objeto.",\n        tag: "PASO 3 DE 4 · TIPIFICACIÓN DE INCIDENTE",\n        transform: "scale(2.05) translate(-6%, 0%)"',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_name('index.html')
update_name('presentacion.html')

# Run node validation
res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
