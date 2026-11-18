import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

diagram = root.find(".//diagram")
if diagram is not None:
    print("Diagram attributes:", diagram.attrib)
# check mxGraphModel
model = root.find(".//mxGraphModel")
if model is not None:
    print("mxGraphModel attributes:", model.attrib)
