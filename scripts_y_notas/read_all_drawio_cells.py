import xml.etree.ElementTree as ET

tree = ET.parse('Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for cell in root.iter('mxCell'):
    val = cell.get('value', '')
    style = cell.get('style', '')
    geo = cell.find('mxGeometry')
    coords = ""
    if geo is not None:
        coords = f"x={geo.get('x')}, y={geo.get('y')}, w={geo.get('width')}, h={geo.get('height')}"
    if val:
        print(f"[{coords}] {repr(val)}")
