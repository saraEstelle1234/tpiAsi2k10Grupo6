import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for cell in root.iter('mxCell'):
    cid = cell.get('id', '')
    if cid.startswith('num_'):
        idx = cid.replace('num_', '')
        txt_cell = root.find(f".//mxCell[@id='txt_{idx}']")
        txt_val = txt_cell.get('value', '') if txt_cell is not None else ''
        print(f"{cid:10}: current_val={cell.get('value')!r:5} | txt={txt_val}")
