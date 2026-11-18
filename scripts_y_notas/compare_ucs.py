import re
import xml.etree.ElementTree as ET

with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find("Objetivos de los Casos de Uso")
end_idx = text.find("Objetivos de Actores")
obj_text = text[start_idx:end_idx]

pdf_ucs = []
for line in obj_text.split("\n"):
    # strip zero-width space \u200b
    clean_line = line.replace('\u200b', '').strip()
    m = re.match(r"^(\d+)[\.\?\)]\s*(.*?)(?::|$)", clean_line)
    if m:
        pdf_ucs.append((int(m.group(1)), m.group(2).strip()))

print(f"PDF Use cases count: {len(pdf_ucs)}")

# Now read DCU .drawio
tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

drawio_ucs = []
for cell in root.iter("mxCell"):
    style = cell.get("style", "")
    val = cell.get("value", "")
    # In DCU, use cases are ellipses or text below ellipse
    if "ellipse" in style or ("text" in style and cell.get("parent") == "1"):
        clean_val = val.replace("<br>", " ").replace("&#xa;", " ").replace("\n", " ").strip()
        if clean_val and not clean_val.startswith("Encargado") and not clean_val.startswith("Responsable") and not clean_val.startswith("Admin") and not clean_val.startswith("Usuario"):
            drawio_ucs.append((cell.get("id"), clean_val))

with open("scripts_y_notas/ucs_comparison.txt", "w", encoding="utf-8") as out:
    out.write("=== USE CASES IN PDF (1..42) ===\n")
    for num, name in pdf_ucs:
        out.write(f"{num:2d}. {name}\n")
    
    out.write("\n=== USE CASES IN DRAWIO ===\n")
    for cid, val in drawio_ucs:
        out.write(f"{cid}: {val}\n")

print("Comparison written to scripts_y_notas/ucs_comparison.txt")
