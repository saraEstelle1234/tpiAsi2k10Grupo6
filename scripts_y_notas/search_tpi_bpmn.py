with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("======================================== PAGE ")

for i, page in enumerate(pages):
    if any(k in page.lower() for k in ["restaur", "supervisor", "bpmn", "incidente", "2.5", "2.6"]):
        print(f"\n--- PAGE {i} ---")
        lines = page.splitlines()
        for line in lines:
            if any(k in line.lower() for k in ["restaur", "supervisor", "nivel", "bpmn", "proceso", "ronda", "regla", "actividad"]):
                print("  " + line[:120])
