import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

# 1. Fix num_9 position and value:
# Place num_9 right in front of oval_9 (x=1210, y=500)
# Exactly matching num_40, num_41, num_42 pattern: x = oval.x - 28 = 1182, y = 504
num_9 = root.find(".//mxCell[@id='num_9']")
if num_9 is not None:
    geo = num_9.find("mxGeometry")
    if geo is not None:
        geo.set("x", "1182")
        geo.set("y", "504")
        geo.set("width", "24")
        geo.set("height", "18")
    num_9.set("value", "9")

# 2. Fix txt_9 position and alignment:
# Exactly matching txt_40, txt_41, txt_42 pattern: x = oval.x - 15 = 1195, y = 532
txt_9 = root.find(".//mxCell[@id='txt_9']")
if txt_9 is not None:
    geo = txt_9.find("mxGeometry")
    if geo is not None:
        geo.set("x", "1195")
        geo.set("y", "532")
        geo.set("width", "145")
        geo.set("height", "24")
    txt_9.set("value", "Registrar baja de obra")

# 3. Fix oval_9 position
oval_9 = root.find(".//mxCell[@id='oval_9']")
if oval_9 is not None:
    geo = oval_9.find("mxGeometry")
    if geo is not None:
        geo.set("x", "1210")
        geo.set("y", "500")
        geo.set("width", "115")
        geo.set("height", "28")

# 4. Fix e_9 (edge from act_admin_sist to oval_9):
e_9 = root.find(".//mxCell[@id='e_9']")
if e_9 is not None:
    e_9.set("source", "act_admin_sist")
    e_9.set("target", "oval_9")
    e_9.set("style", "endArrow=classic;html=1;rounded=1;strokeWidth=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;")
    # Waypoint at (1360, 514)
    geo = e_9.find("mxGeometry")
    if geo is not None:
        # clear existing array if any
        arr = geo.find("Array")
        if arr is not None:
            geo.remove(arr)
        new_arr = ET.SubElement(geo, "Array", {"as": "points"})
        ET.SubElement(new_arr, "mxPoint", {"x": "1360", "y": "514"})

# 5. Fix e_sis_42 (edge to oval_42 so it enters from top and does not cross oval_9):
e_sis_42 = root.find(".//mxCell[@id='e_sis_42']")
if e_sis_42 is not None:
    e_sis_42.set("style", "endArrow=classic;html=1;rounded=1;strokeWidth=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;")
    geo = e_sis_42.find("mxGeometry")
    if geo is not None:
        arr = geo.find("Array")
        if arr is not None:
            geo.remove(arr)
        new_arr = ET.SubElement(geo, "Array", {"as": "points"})
        ET.SubElement(new_arr, "mxPoint", {"x": "1355", "y": "488"})
        ET.SubElement(new_arr, "mxPoint", {"x": "1117", "y": "488"})

# 6. Verify e_4 (edge from act_obras to oval_4 "Registrar obra a restaurar"):
e_4 = root.find(".//mxCell[@id='e_4']")
if e_4 is not None:
    e_4.set("source", "act_obras")
    e_4.set("target", "oval_4")
    e_4.set("style", "endArrow=classic;html=1;rounded=1;strokeWidth=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;")
    # Clean geometry
    geo = e_4.find("mxGeometry")
    if geo is not None:
        arr = geo.find("Array")
        if arr is not None:
            geo.remove(arr)

# Save to both locations
tree.write("Diagramas/Diagrama_de_Casos_de_Uso.drawio", encoding="utf-8", xml_declaration=True)
tree.write("Diagrama_de_Casos_de_Uso.drawio", encoding="utf-8", xml_declaration=True)

print("Diagrama de Casos de Uso completely fixed!")
