import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Clases.drawio')
root = tree.getroot()

for cid in ['cls_incidente', 'cls_tipo_incidente', 'cls_sala', 'cls_salaxguardia', 'cls_guardia', 'cls_obra']:
    c = root.find(f".//mxCell[@id='{cid}']")
    geo = c.find('mxGeometry')
    print(f"{cid:20}: x={geo.get('x')}, y={geo.get('y')}, w={geo.get('width')}, h={geo.get('height')}")
