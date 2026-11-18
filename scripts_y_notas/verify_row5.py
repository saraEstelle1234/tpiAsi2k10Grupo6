import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

for cid in ["num_9", "oval_9", "txt_9", "e_9", "oval_42", "txt_42", "e_sis_42", "num_4", "oval_4", "txt_4", "e_4"]:
    c = root.find(f".//mxCell[@id='{cid}']")
    if c is not None:
        geo = c.find("mxGeometry")
        gx = geo.get("x") if geo is not None else None
        gy = geo.get("y") if geo is not None else None
        print(f"{cid:10} | val='{c.get('value')}' | x={gx} y={gy}")
