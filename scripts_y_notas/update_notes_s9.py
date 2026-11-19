import re
import subprocess
import shutil

def update_notes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_s9_notes = '"9": {"speaker": "Francisco Thomas Rapp", "time": "1:30 min", "title": "Diagrama de Casos de Uso General", "speech": "En la diapositiva 9 presentamos el Diagrama de Casos de Uso General que traduce los requerimientos funcionales en interacciones del usuario con el sistema. Identificamos 5 actores del sistema: Encargado de Vigilancia, Administrador Web, Encargado de Supervisión, Responsable de Atención al Cliente y Usuario General. El núcleo de nuestra solución articula el caso de uso base CU-14 \'Registrar revisión de la sala\' con una relación «extend» hacia el CU-15 \'Registrar Incidente\', el cual solo se dispara si el guardia detecta una anomalía o daño físico en su ronda.", "bullets": ["5 Actores organizacionales modelados en el sistema.", "Relación clave: CU-14 \'Registrar revisión\' extiende a CU-15 \'Registrar incidente\'.", "Separación entre vigilancia presencial y administración centralizada."]},'

    new_s9_notes = '"9": {"speaker": "Francisco Thomas Rapp", "time": "1:30 min", "title": "Diagrama de Casos de Uso General", "speech": "En la diapositiva 9 presentamos el Diagrama de Casos de Uso General con los 45 casos de uso del sistema organizados según los roles del museo: Encargado de Vigilancia, Encargado de Supervisión, Responsable de Ingreso de Obra, Responsable de Atención al Cliente, Administrador del Museo, Admin de Sistema y Usuario. El núcleo operativo vincula el CU-14 Registrar revisión de sala con la extensión condicional al CU-15 Registrar Incidente cuando se detecta una anomalía en ronda.", "bullets": ["45 Casos de Uso organizados por rol del dominio.", "Relación clave: CU-14 \'Registrar revisión\' extiende a CU-15 \'Registrar incidente\'.", "Sectorización interactiva por actor: Vigilancia, Supervisión, Ingreso, Atención, Museo, Admin y Usuario."]},'

    if old_s9_notes in content:
        content = content.replace(old_s9_notes, new_s9_notes)
        print(f"[{filepath}] Replaced Slide 9 notes!")
    else:
        print(f"[{filepath}] old_s9_notes not found directly")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_notes('index.html')
update_notes('presentacion.html')

res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
