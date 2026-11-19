import re
import subprocess
import shutil

def apply_dcd_fixes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update DCD_TOUR_STEPS
    old_steps = """    const DCD_TOUR_STEPS = [
      {
        title: "Vista Completa del Diagrama de Clases",
        desc: "Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.",
        tag: "VISTA COMPLETA DCD",
        transform: "scale(1) translate(0%, 0%)"
      },
      {
        title: "Sector 1: Núcleo Incidente & Sala",
        desc: "La clase Incidente registra fecha, hora y descripción, asociándose a Sala (1). Conoce al guardia de turno a través de la relación histórica SalaXGuardia.",
        tag: "SECTOR 1 · INCIDENTE & SALA",
        transform: "scale(2.1) translate(21%, -2%)"
      },
      {
        title: "Sector 2: Obra, Material y Componentes",
        desc: "Obra encapsula registrarObraInactiva() y registrarObraActiva(), vinculándose con Material (para evaluar sensibilidad física), TipoObra y Autor.",
        tag: "SECTOR 2 · OBRA & MATERIAL",
        transform: "scale(2.0) translate(-13%, 8%)"
      },
      {
        title: "Sector 3: Clase Tipo de Incidente",
        desc: "TipoIncidente tipifica el evento (accidental, provocado o natural), orientando las acciones de mitigación inmediata y contingencia.",
        tag: "SECTOR 3 · TIPO DE INCIDENTE",
        transform: "scale(2.4) translate(32%, 13%)"
      },
      {
        title: "Sector 4: Asignación de Sala y Guardia",
        desc: "La clase Sala se vincula con SalaXGuardia (1..*) registrando el historial de rondas presenciales y el Guardia asignado a cada revisión de sala.",
        tag: "ASIGNACIÓN SALA Y GUARDIA",
        transform: "scale(2.05) translate(31%, -27.5%)"
      }
    ];"""

    new_steps = """    const DCD_TOUR_STEPS = [
      {
        title: "Vista Completa del Diagrama de Clases",
        desc: "Estructura global de clases del dominio, asociaciones, atributos, métodos y multiplicidades corregidas.",
        tag: "VISTA COMPLETA DCD",
        transform: "scale(1) translate(0%, 0%)"
      },
      {
        title: "Sector 1: Núcleo Incidente & Sala",
        desc: "La clase Incidente registra fecha, hora y descripción, asociándose a Sala (1). Conoce al guardia de turno a través de la relación histórica SalaXGuardia.",
        tag: "SECTOR 1 · INCIDENTE & SALA",
        transform: "scale(1.58) translate(18.7%, -2.5%)"
      },
      {
        title: "Sector 2: Obra, Material y Componentes",
        desc: "Obra encapsula registrarObraInactiva() y registrarObraActiva(), vinculándose con Material (para evaluar sensibilidad física), TipoObra y Autor.",
        tag: "SECTOR 2 · OBRA & MATERIAL",
        transform: "scale(1.6) translate(-14.7%, 8%)"
      },
      {
        title: "Sector 3: Clase Tipo de Incidente",
        desc: "TipoIncidente tipifica el evento (accidental, provocado o natural), orientando las acciones de mitigación inmediata y contingencia.",
        tag: "SECTOR 3 · TIPO DE INCIDENTE",
        transform: "scale(1.95) translate(30.3%, 12.4%)"
      },
      {
        title: "Sector 4: Asignación de Sala y Guardia",
        desc: "La clase Sala se vincula con SalaXGuardia (1..*) registrando el historial de rondas presenciales y el Guardia asignado a cada revisión de sala.",
        tag: "ASIGNACIÓN SALA Y GUARDIA",
        transform: "scale(1.75) translate(30.3%, -26.3%)"
      }
    ];"""

    if old_steps in content:
        content = content.replace(old_steps, new_steps)
        print(f"[{filepath}] Replaced DCD_TOUR_STEPS successfully!")
    else:
        print(f"[{filepath}] DCD_TOUR_STEPS not matched directly, checking regex...")
        content = re.sub(
            r'const DCD_TOUR_STEPS = \[[\s\S]*?\n    \];',
            new_steps.strip(),
            content
        )

    # 2. Upgrade DCD container height in Slide 12 to 740px clamp
    content = content.replace(
        '<div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: clamp(480px, 68vh, 720px);',
        '<div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: clamp(520px, 72vh, 760px);'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

apply_dcd_fixes('index.html')
apply_dcd_fixes('presentacion.html')

res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
