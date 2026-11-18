import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

ovals = []
for cell in root.iter("mxCell"):
    cid = cell.get("id", "")
    if cid.startswith("oval_"):
        idx = int(cid.split("_")[1])
        # find num cell and txt cell
        num_cell = root.find(f".//mxCell[@id='num_{idx}']")
        txt_cell = root.find(f".//mxCell[@id='txt_{idx}']")
        nval = num_cell.get("value") if num_cell is not None else None
        tval = txt_cell.get("value") if txt_cell is not None else None
        geo = cell.find("mxGeometry")
        x = geo.get("x") if geo is not None else None
        y = geo.get("y") if geo is not None else None
        ovals.append((idx, nval, tval, x, y))

for idx, nval, tval, x, y in sorted(ovals, key=lambda o: (float(o[3] or 0), float(o[4] or 0))):
    print(f"oval_{idx:2d} | num='{nval}' | txt='{tval}' | x={x} y={y}")
