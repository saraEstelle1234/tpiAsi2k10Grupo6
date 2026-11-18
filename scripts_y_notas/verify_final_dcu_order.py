import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

ovals = []
for cell in root.iter('mxCell'):
    cid = cell.get('id', '')
    if cid.startswith('oval_'):
        idx = cid.replace('oval_', '')
        num_cell = root.find(f".//mxCell[@id='num_{idx}']")
        txt_cell = root.find(f".//mxCell[@id='txt_{idx}']")
        nval = int(num_cell.get('value', 0)) if num_cell is not None else 0
        tval = txt_cell.get('value', '') if txt_cell is not None else ''
        geo = cell.find('mxGeometry')
        x = float(geo.get('x', 0)) if geo is not None else 0
        y = float(geo.get('y', 0)) if geo is not None else 0
        ovals.append((nval, idx, tval, x, y))

for nval, idx, tval, x, y in sorted(ovals, key=lambda o: o[0]):
    print(f"[{nval:2d}] (oval_{idx:2s}) : {tval:45} | x={x:5.0f}, y={y:5.0f}")
