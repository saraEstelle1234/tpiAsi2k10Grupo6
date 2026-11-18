with open("Ev Grupal/CONTEXTO_EVALUACION_GRUPAL_ASI.md", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.splitlines()
print("Lines in CONTEXTO_EVALUACION_GRUPAL_ASI.md:", len(lines))
# print first 50 lines
print("\n".join(lines[:45]))
