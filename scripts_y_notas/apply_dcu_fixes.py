import xml.etree.ElementTree as ET

def update_dcu(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()

    # 1. Update Registrar baja de obra: num_9 value -> "43"
    num_9 = root.find(".//mxCell[@id='num_9']")
    if num_9 is not None:
        num_9.set('value', '43')
        print("Updated num_9 value to 43")

    # 2. Update Iniciar sesion: num_43 value -> "44"
    num_43 = root.find(".//mxCell[@id='num_43']")
    if num_43 is not None:
        num_43.set('value', '44')
        print("Updated num_43 value to 44")

    # 3. Update Cerrar sesion: num_44 value -> "45"
    num_44 = root.find(".//mxCell[@id='num_44']")
    if num_44 is not None:
        num_44.set('value', '45')
        print("Updated num_44 value to 45")

    # 4. Update Modificar contrasena: num_45 value -> "46"
    num_45 = root.find(".//mxCell[@id='num_45']")
    if num_45 is not None:
        num_45.set('value', '46')
        print("Updated num_45 value to 46")

    # 5. Update txt_16 to "Registrar incidente"
    txt_16 = root.find(".//mxCell[@id='txt_16']")
    if txt_16 is not None:
        txt_16.set('value', 'Registrar incidente')
        print("Updated txt_16 to 'Registrar incidente'")

    badge_style = "text;html=1;strokeColor=none;fillColor=#ffffff;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=1;fontStyle=1;fontSize=11;"

    # 6. Reposition num_11 (Registrar contratacion de servicio de guia)
    num_11 = root.find(".//mxCell[@id='num_11']")
    if num_11 is not None:
        g11 = num_11.find('mxGeometry')
        g11.set('x', '330')
        g11.set('y', '716')
        num_11.set('style', badge_style)
        print("Repositioned num_11 to x=330, y=716 with badge style")

    # 7. Move oval_12, txt_12, num_12 (Consultar agenda de guias)
    oval_12 = root.find(".//mxCell[@id='oval_12']")
    if oval_12 is not None:
        g_o12 = oval_12.find('mxGeometry')
        g_o12.set('x', '570')
        g_o12.set('y', '740')

    txt_12 = root.find(".//mxCell[@id='txt_12']")
    if txt_12 is not None:
        g_t12 = txt_12.find('mxGeometry')
        g_t12.set('x', '555')
        g_t12.set('y', '772')

    num_12 = root.find(".//mxCell[@id='num_12']")
    if num_12 is not None:
        g_n12 = num_12.find('mxGeometry')
        g_n12.set('x', '560')
        g_n12.set('y', '716')
        num_12.set('style', badge_style)
        print("Repositioned oval_12 to x=570 and num_12 to x=560, y=716 with badge style")

    # Re-route edge_inc_visitas to enter top of oval_12 at x=628
    edge_inc_visitas = root.find(".//mxCell[@id='edge_inc_visitas']")
    if edge_inc_visitas is not None:
        edge_inc_visitas.set('style', 'endArrow=open;dashed=1;html=1;rounded=1;strokeWidth=1;endFill=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;')
        geo = edge_inc_visitas.find('mxGeometry')
        if geo is not None:
            arr = geo.find('Array')
            if arr is not None:
                arr.clear()
                for px, py in [('265', '594'), ('450', '594'), ('450', '680'), ('628', '680')]:
                    pt = ET.SubElement(arr, 'mxPoint')
                    pt.set('x', px)
                    pt.set('y', py)
        print("Re-routed edge_inc_visitas to enter top center of oval_12")

    # 8. Reposition num_16 (Registrar incidente)
    num_16 = root.find(".//mxCell[@id='num_16']")
    if num_16 is not None:
        g16 = num_16.find('mxGeometry')
        g16.set('x', '330')
        g16.set('y', '960')
        num_16.set('style', badge_style)
        print("Repositioned num_16 to x=330, y=960 with badge style")

    # Also give all other nums a crisp white fill to guarantee no edge lines ever obscure any number!
    for cell in root.iter('mxCell'):
        cid = cell.get('id', '')
        if cid.startswith('num_') and cid not in ['num_11', 'num_12', 'num_16']:
            cell.set('style', badge_style)

    # Save cleanly
    tree.write(filepath, encoding='utf-8', xml_declaration=True)
    print(f"Saved {filepath}")

update_dcu('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
update_dcu('Diagrama_de_Casos_de_Uso.drawio')
