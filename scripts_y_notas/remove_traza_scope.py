import re
import subprocess
import shutil

def remove_traza_scope(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target HTML block to remove
    target = """        <!-- Nota de Alcance Metodológico -->
        <div class="traza-scope-card">
          <span class="traza-scope-badge">Nota de Alcance Metodológico</span>
          <span>
            El prototipo y el diagrama de clases modelan en profundidad el caso crítico <strong>Registrar Incidente</strong> por indicación directa de la cátedra de ASI. Las operaciones de Entrada, Guías y Exposiciones se mantienen en el nivel analítico de Procesos y RFs para no dispersar el alcance de la defensa.
          </span>
        </div>"""

    if target in content:
        content = content.replace(target, "")
        print(f"[{filepath}] Removed 'Nota de Alcance Metodológico' card successfully!")
    else:
        # Regex fallback
        content = re.sub(
            r'\s*<!-- Nota de Alcance Metodológico -->\s*<div class="traza-scope-card">[\s\S]*?</div>',
            '',
            content
        )
        print(f"[{filepath}] Regex replaced 'Nota de Alcance Metodológico'")

    # Also clean up speaker note for Slide 13
    content = content.replace(
        'Como nota de alcance, el DCD modela con máxima granularidad este caso crítico por indicación de la cátedra, garantizando una arquitectura robusta y consistente.',
        'Garantizamos así una arquitectura robusta y consistente para todo el ciclo de incidentes.'
    )
    content = content.replace(
        '"Nota de alcance: Foco exhaustivo en el caso crítico de incidentes."',
        '"Validación cruzada E2E en todos los artefactos de diseño."'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

remove_traza_scope('index.html')
remove_traza_scope('presentacion.html')

res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
