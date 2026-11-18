import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for cid in ['oval_40', 'num_40', 'txt_40',
            'oval_41', 'num_41', 'txt_41',
            'oval_42', 'num_42', 'txt_42',
            'oval_9', 'num_9', 'txt_9']:
    c = root.find(f".//mxCell[@id='{cid}']")
    geo = c.find('mxGeometry')
    x = geo.get('x')
    y = geo.get('y')
    w = geo.get('width')
    h = geo.get('height')
    print(f"{cid:8}: val={c.get('value')!r:30} x={x:5} y={y:5} w={w:5} h={h:5} style={c.get('style')}")
