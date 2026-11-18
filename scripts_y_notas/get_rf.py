with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract from "Requerimientos Funcionales" to "Requerimientos No Funcionales"
start = text.find("Requerimientos Funcionales")
end = text.find("Requerimientos No Funcionales")

rf_text = text[start:end]

with open("scripts_y_notas/rf_analysis.txt", "w", encoding="utf-8") as out:
    out.write(rf_text)

print("RF text length:", len(rf_text))
