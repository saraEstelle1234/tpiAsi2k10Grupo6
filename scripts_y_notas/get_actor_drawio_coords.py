import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

print("=== ACTORS IN DRAWIO WITH EXACT COORDINATES ===")
actors = []
for cell in root.iter("mxCell"):
    style = cell.get("style", "")
    if "actor" in style.lower():
        cid = cell.get("id")
        val = cell.get("value", "").replace("\n", " ").replace("&#xa;", " ")
        geo = cell.find("mxGeometry")
        x = float(geo.get("x", 0)) if geo is not None else 0
        y = float(geo.get("y", 0)) if geo is not None else 0
        w = float(geo.get("width", 0)) if geo is not None else 0
        h = float(geo.get("height", 0)) if geo is not None else 0
        actors.append((cid, val, x, y, w, h))

for a in actors:
    print(f"ID: {a[0]:15} | Name: {a[1]:30} | x={a[2]:6.1f}, y={a[3]:6.1f}, w={a[4]:4.1f}, h={a[5]:4.1f}")

# Also let's find the bounds of all elements in the diagram
all_x = []
all_y = []
for geo in root.iter("mxGeometry"):
    if geo.get("x") is not None:
        all_x.append(float(geo.get("x")))
    if geo.get("y") is not None:
        all_y.append(float(geo.get("y")))

print(f"Overall DrawIO bounds: X=[{min(all_x):.1f}, {max(all_x):.1f}], Y=[{min(all_y):.1f}, {max(all_y):.1f}]")
