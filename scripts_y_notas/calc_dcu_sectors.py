import xml.etree.ElementTree as ET

tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

# Let's map which ovals / use cases are connected to which actors:
# Edges: source -> target
connections = {}
actors = {}
ovals = {}

for cell in root.iter("mxCell"):
    cid = cell.get("id", "")
    val = cell.get("value", "").replace("\n", " ").replace("&#xa;", " ")
    style = cell.get("style", "")
    if "actor" in style.lower():
        geo = cell.find("mxGeometry")
        x = float(geo.get("x", 0)) if geo is not None else 0
        y = float(geo.get("y", 0)) if geo is not None else 0
        actors[cid] = (val, x, y)
    elif cid.startswith("oval_"):
        idx = cid.replace("oval_", "")
        num_cell = root.find(f".//mxCell[@id='num_{idx}']")
        txt_cell = root.find(f".//mxCell[@id='txt_{idx}']")
        nval = num_cell.get("value", "") if num_cell is not None else ""
        tval = txt_cell.get("value", "") if txt_cell is not None else ""
        geo = cell.find("mxGeometry")
        x = float(geo.get("x", 0)) if geo is not None else 0
        y = float(geo.get("y", 0)) if geo is not None else 0
        w = float(geo.get("width", 0)) if geo is not None else 0
        h = float(geo.get("height", 0)) if geo is not None else 0
        ovals[cid] = (nval, tval, x, y, w, h)

for cell in root.iter("mxCell"):
    if cell.get("edge") == "1":
        src = cell.get("source")
        tgt = cell.get("target")
        if src in actors:
            connections.setdefault(src, []).append(tgt)
        if tgt in actors:
            connections.setdefault(tgt, []).append(src)

print("=== ACTOR AND CONNECTED USE CASES ===")
for aid, (aname, ax, ay) in actors.items():
    conns = connections.get(aid, [])
    print(f"\nActor: {aname} (id={aid}, pos=({ax:.0f}, {ay:.0f})) -> {len(conns)} use cases:")
    # calculate bounding box of actor + connected ovals
    xs = [ax]
    ys = [ay]
    for cid in conns:
        if cid in ovals:
            nval, tval, ox, oy, ow, oh = ovals[cid]
            xs.extend([ox, ox + ow])
            ys.extend([oy, oy + oh])
            print(f"   CU {nval:2s}: {tval:35s} at ({ox:5.0f}, {oy:5.0f})")
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    print(f"   --> BBox: X=[{min_x:.0f}, {max_x:.0f}], Y=[{min_y:.0f}, {max_y:.0f}] | Center: ({center_x:.0f}, {center_y:.0f})")
    # Percentage relative to 1455 x 1675
    pct_x = (center_x / 1455.0) * 100
    pct_y = (center_y / 1675.0) * 100
    span_x = max_x - min_x
    span_y = max_y - min_y
    print(f"   --> Pct Center: {pct_x:.1f}%, {pct_y:.1f}% | Span: {span_x:.0f} x {span_y:.0f}")

