import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for cell in root.iter('mxCell'):
    geo = cell.find('mxGeometry')
    if geo is not None:
        try:
            x = float(geo.get('x', 0))
            y = float(geo.get('y', 0))
            if 250 <= x <= 650 and 600 <= y <= 745:
                print(f"Cell {cell.get('id')}: val={cell.get('value')!r}, x={x}, y={y}")
        except:
            pass
