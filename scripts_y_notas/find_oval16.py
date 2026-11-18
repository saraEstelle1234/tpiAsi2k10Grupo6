import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

for cid in ["oval_16", "txt_16", "num_16"]:
    c = root.find(f".//mxCell[@id='{cid}']")
    if c is not None:
        geo = c.find("mxGeometry")
        val = c.get("value", "")
        print(f"{cid}: val='{val}' x={geo.get('x')} y={geo.get('y')}")
