import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

# Check num_9
num_9 = root.find(".//mxCell[@id='num_9']")
if num_9 is not None:
    geo = num_9.find("mxGeometry")
    print(f"num_9 currently: val='{num_9.get('value')}' x={geo.get('x')} y={geo.get('y')}")

# Check oval_9 and txt_9
oval_9 = root.find(".//mxCell[@id='oval_9']")
txt_9 = root.find(".//mxCell[@id='txt_9']")
print("oval_9:", oval_9.find("mxGeometry").attrib)
print("txt_9:", txt_9.find("mxGeometry").attrib, "val:", txt_9.get("value"))

# Check oval_42 and e_sis_42
oval_42 = root.find(".//mxCell[@id='oval_42']")
e_sis_42 = root.find(".//mxCell[@id='e_sis_42']")
print("oval_42:", oval_42.find("mxGeometry").attrib)
print("e_sis_42 style:", e_sis_42.get("style"))
