import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Clases.drawio')
root = tree.getroot()

classes = {}
for cell in root.iter('mxCell'):
    if cell.get('vertex') == '1':
        classes[cell.get('id')] = cell.get('value', '').split('\n')[0]

for cell in root.iter('mxCell'):
    if cell.get('edge') == '1':
        eid = cell.get('id')
        src = cell.get('source', '')
        tgt = cell.get('target', '')
        src_name = classes.get(src, src)
        tgt_name = classes.get(tgt, tgt)
        # find labels
        lbls = []
        for l in root.iter('mxCell'):
            if l.get('parent') == eid:
                geo = l.find('mxGeometry')
                x = geo.get('x') if geo is not None else ''
                y = geo.get('y') if geo is not None else ''
                lbls.append((l.get('value'), x, y, l.get('style')))
        print(f"Edge {eid:16} | {src_name:12} -> {tgt_name:14} | Labels: {lbls}")
