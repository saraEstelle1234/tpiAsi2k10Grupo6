import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

print("ALL CELLS IN DIAGRAMA DE CASOS DE USO:")
dcu_elements = []
for cell in root.iter("mxCell"):
    cid = cell.get("id", "")
    val = cell.get("value", "")
    style = cell.get("style", "")
    if val and cell.get("vertex") == "1":
        clean = val.replace("<br>", " ").replace("&#xa;", " ").replace("\n", " ").strip()
        dcu_elements.append((cid, clean, style[:40]))

with open("scripts_y_notas/dcu_cells.txt", "w", encoding="utf-8") as f:
    for cid, val, st in dcu_elements:
        f.write(f"{cid:25} | {val} | {st}\n")

print(f"Total vertex cells with value: {len(dcu_elements)}")
