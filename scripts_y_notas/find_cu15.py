import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

for cid in ["oval_15", "txt_15", "num_15", "oval_14", "txt_14", "num_14"]:
    c = root.find(f".//mxCell[@id='{cid}']")
    if c is not None:
        geo = c.find("mxGeometry")
        val = c.get("value", "")
        if geo is not None:
            print(f"{cid}: val='{val}' x={geo.get('x')} y={geo.get('y')} w={geo.get('width')} h={geo.get('height')}")
        else:
            print(f"{cid}: val='{val}'")

# check edges connected to oval_15
for e in root.iter("mxCell"):
    if e.get("edge") == "1" and (e.get("source") in ["oval_15", "oval_14"] or e.get("target") in ["oval_15", "oval_14"]):
        print(f"Edge {e.get('id')}: {e.get('source')} -> {e.get('target')} style={e.get('style')}")

