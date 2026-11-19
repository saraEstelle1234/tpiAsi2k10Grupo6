with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

tour_card_bpmn = """        <!-- Card dinámico explicativo de la fase activa -->
        <div class="tour-step-card" id="bpmn-tour-card">
          <div class="tour-step-tag" id="bpmn-tour-tag">VISTA GENERAL</div>
          <div class="tour-step-title" id="bpmn-tour-title">Visión General del Proceso Operativo</div>
          <div class="tour-step-desc" id="bpmn-tour-desc">Flujo completo de 4 carriles (Guardia, Encargado Web, Supervisor, Restaurador) con compuertas, almacenes de datos y cambios de estado destino explícitos.</div>
        </div>
"""

target = '<!-- 3 Puntos concretos que explican cómo se plantearon las correcciones del profesor -->'
if target in text:
    text = text.replace(target, tour_card_bpmn + '\n        ' + target)
    print("Inserted tour_card_bpmn successfully!")
    with open('presentacion.html', 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("Target not found!")
