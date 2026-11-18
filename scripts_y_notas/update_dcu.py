import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

# 1. Update txt_4: now "Registrar obra a restaurar" (connected to act_obras)
txt_4 = root.find(".//mxCell[@id='txt_4']")
if txt_4 is not None:
    txt_4.set("value", "Registrar obra a restaurar")

# Update e_4: source becomes act_obras, target oval_4
e_4 = root.find(".//mxCell[@id='e_4']")
if e_4 is not None:
    e_4.set("source", "act_obras")
    e_4.set("target", "oval_4")

# Adjust position of act_obras slightly to center between y=50 and y=280: y=130
act_obras = root.find(".//mxCell[@id='act_obras']")
if act_obras is not None:
    geo = act_obras.find("mxGeometry")
    if geo is not None:
        geo.set("y", "130")

# 2. Update txt_9: now "Registrar baja de obra"
# Move oval_9 and txt_9 to Admin de Sistema area: x=1210, y=500
oval_9 = root.find(".//mxCell[@id='oval_9']")
if oval_9 is not None:
    geo = oval_9.find("mxGeometry")
    if geo is not None:
        geo.set("x", "1210")
        geo.set("y", "500")

txt_9 = root.find(".//mxCell[@id='txt_9']")
if txt_9 is not None:
    txt_9.set("value", "Registrar baja de obra")
    geo = txt_9.find("mxGeometry")
    if geo is not None:
        geo.set("x", "1185")
        geo.set("y", "550")

# Update e_9: connects act_admin_sist -> oval_9
e_9 = root.find(".//mxCell[@id='e_9']")
if e_9 is not None:
    e_9.set("source", "act_admin_sist")
    e_9.set("target", "oval_9")
    e_9.set("style", "endArrow=none;html=1;rounded=1;strokeColor=#000000;strokeWidth=1;exitX=0;exitY=0.7;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;")

# 3. Remove act_escuela and e_escuela
parent_root = root.find(".//root")
if parent_root is not None:
    act_escuela = root.find(".//mxCell[@id='act_escuela']")
    if act_escuela is not None:
        parent_root.remove(act_escuela)
    e_escuela = root.find(".//mxCell[@id='e_escuela']")
    if e_escuela is not None:
        parent_root.remove(e_escuela)

# 4. Update txt_23: "Emitir historial de incidentes"
txt_23 = root.find(".//mxCell[@id='txt_23']")
if txt_23 is not None:
    txt_23.set("value", "Emitir historial de incidentes")

# Save updated DCU to both locations
tree.write("Diagramas/Diagrama_de_Casos_de_Uso.drawio", encoding="utf-8", xml_declaration=True)
tree.write("Diagrama_de_Casos_de_Uso.drawio", encoding="utf-8", xml_declaration=True)

print("DCU updated successfully!")
