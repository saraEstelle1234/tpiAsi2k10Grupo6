import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for cell in root.iter('mxCell'):
    cid = cell.get('id', '')
    val = cell.get('value', '')
    if val == '9' or ' 9' in val or '9 ' in val or val == '9.':
        geo = cell.find('mxGeometry')
        gx = geo.get('x') if geo is not None else ''
        gy = geo.get('y') if geo is not None else ''
        print(f"Found '9' in cell {cid}: val={val!r}, x={gx}, y={gy}")
