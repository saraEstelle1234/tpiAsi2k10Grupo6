import xml.etree.ElementTree as ET

def fix_multiplicities(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    label_style = "resizable=0;html=1;align=center;verticalAlign=bottom;labelBackgroundColor=none;fontSize=12;fontStyle=1;"

    for cell in root.iter('mxCell'):
        cid = cell.get('id', '')
        if cid.endswith('_lbl'):
            geo = cell.find('mxGeometry')
            if geo is not None:
                # Set x to 0.75 and y to -12 so it floats clearly above the arrow line near target
                geo.set('x', '0.75')
                geo.set('y', '-12')
                cell.set('style', label_style)
                print(f"Fixed label {cid} on {filepath}")

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Successfully saved {filepath}")

fix_multiplicities('Diagramas/Diagrama_de_Clases.drawio')
fix_multiplicities('Diagrama_de_Clases.drawio')
