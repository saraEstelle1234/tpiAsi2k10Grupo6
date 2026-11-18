with open("Ev Grupal/CONTEXTO_EVALUACION_GRUPAL_ASI.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
print("\n".join(lines[120:200]))
