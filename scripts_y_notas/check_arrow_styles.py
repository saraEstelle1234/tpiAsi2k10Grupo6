import xml.etree.ElementTree as ET

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

for eid in ['e_1', 'e_10', 'e_15', 'edge_ext_guia', 'edge_inc_guia', 'edge_ext_incidente']:
    cell = root.find(f".//mxCell[@id='{eid}']")
    if cell is not None:
        print(f"{eid:20}: style={cell.get('style')}")
