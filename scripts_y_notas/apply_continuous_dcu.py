import xml.etree.ElementTree as ET

def update_dcu_continuous_numbering(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Mapping based on continuous 1..42 plus 43..45 for session
    # 1..8 stay unchanged
    # 10..24 shift by -1 (10->9, 11->10, ..., 24->23)
    # 25..42 shift by -1 (25->24, 26->25, ..., 42->41)
    # num_9 (Registrar baja de obra) becomes 42
    # num_43 (Iniciar sesion) becomes 43
    # num_44 (Cerrar sesion) becomes 44
    # num_45 (Modificar contrasena) becomes 45

    shifts = {}
    for i in range(10, 25):
        shifts[f'num_{i}'] = str(i - 1)
    for i in range(25, 43):
        shifts[f'num_{i}'] = str(i - 1)
    
    shifts['num_9'] = '42'
    shifts['num_43'] = '43'
    shifts['num_44'] = '44'
    shifts['num_45'] = '45'

    for cid, new_val in shifts.items():
        cell = root.find(f".//mxCell[@id='{cid}']")
        if cell is not None:
            old_val = cell.get('value')
            cell.set('value', new_val)
            print(f"Updated {cid}: {old_val} -> {new_val}")

    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Successfully updated and saved {filepath}")

update_dcu_continuous_numbering('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
