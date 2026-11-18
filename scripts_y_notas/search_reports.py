import glob

for f in glob.glob("scripts_y_notas/*.txt"):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        txt = fp.read()
        if "bpmn" in txt.lower() or "restaur" in txt.lower():
            print(f"File {f} mentions bpmn/restaur. Size: {len(txt)}")
            # print snippets
            lines = [l for l in txt.splitlines() if any(k in l.lower() for k in ['bpmn', 'carril', 'restaurar', 'tarifa', 'cambio de estado'])]
            for l in lines[:5]:
                print("   ", l[:100])
