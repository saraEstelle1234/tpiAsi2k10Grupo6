import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

print("=== ACTORS NOW IN DCU ===")
for cell in root.iter("mxCell"):
    style = cell.get("style", "")
    if "actor" in style.lower():
        print(f"Actor: {cell.get('id')} -> {cell.get('value').replace(chr(10), ' ')}")

print("\n=== TARGET OVALS MODIFIED ===")
for cid in ["txt_4", "txt_9", "txt_23"]:
    c = root.find(f".//mxCell[@id='{cid}']")
    if c is not None:
        print(f"{cid}: {c.get('value')}")

print("\n=== EDGES MODIFIED ===")
for eid in ["e_4", "e_9"]:
    e = root.find(f".//mxCell[@id='{eid}']")
    if e is not None:
        print(f"{eid}: {e.get('source')} -> {e.get('target')}")

# Check act_escuela
esc = root.find(".//mxCell[@id='act_escuela']")
print("act_escuela exists?", esc is not None)
