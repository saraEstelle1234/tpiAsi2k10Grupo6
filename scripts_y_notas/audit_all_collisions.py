import xml.etree.ElementTree as ET
import math

tree = ET.parse('Diagramas/Diagrama_de_Casos_de_Uso.drawio')
root = tree.getroot()

# Collect all nums
nums = {}
for cell in root.iter('mxCell'):
    cid = cell.get('id', '')
    if cid.startswith('num_'):
        geo = cell.find('mxGeometry')
        if geo is not None:
            x = float(geo.get('x', 0))
            y = float(geo.get('y', 0))
            w = float(geo.get('width', 24))
            h = float(geo.get('height', 18))
            nums[cid] = {'val': cell.get('value'), 'rect': (x, y, x + w, y + h), 'center': (x + w/2, y + h/2)}

# Collect all ovals
ovals = {}
for cell in root.iter('mxCell'):
    cid = cell.get('id', '')
    if cid.startswith('oval_') or cid.startswith('act_'):
        geo = cell.find('mxGeometry')
        if geo is not None:
            x = float(geo.get('x', 0))
            y = float(geo.get('y', 0))
            w = float(geo.get('width', 0))
            h = float(geo.get('height', 0))
            ovals[cid] = (x, y, w, h)

# Function to check segment-rect intersection or distance
def seg_rect_dist(p1, p2, rect):
    rx1, ry1, rx2, ry2 = rect
    # Sample 20 points along segment
    min_d = 999999
    for i in range(21):
        t = i / 20.0
        px = p1[0] + t * (p2[0] - p1[0])
        py = p1[1] + t * (p2[1] - p1[1])
        # Distance from px, py to rect
        dx = max(rx1 - px, 0, px - rx2)
        dy = max(ry1 - py, 0, py - ry2)
        d = math.hypot(dx, dy)
        if d < min_d:
            min_d = d
    return min_d

# Check each edge
print("=== CHECKING ALL EDGES AGAINST ALL NUMBERS ===")
for cell in root.iter('mxCell'):
    if cell.get('edge') == '1':
        eid = cell.get('id', '')
        src = cell.get('source', '')
        tgt = cell.get('target', '')
        geo = cell.find('mxGeometry')
        pts = []
        if src in ovals:
            sx, sy, sw, sh = ovals[src]
            pts.append((sx + sw/2, sy + sh/2))
        if geo is not None:
            arr = geo.find('Array')
            if arr is not None:
                for pt in arr.findall('mxPoint'):
                    pts.append((float(pt.get('x')), float(pt.get('y'))))
        if tgt in ovals:
            tx, ty, tw, th = ovals[tgt]
            pts.append((tx + tw/2, ty + th/2))
        
        # Check against all nums
        for nid, ndata in nums.items():
            for i in range(len(pts) - 1):
                d = seg_rect_dist(pts[i], pts[i+1], ndata['rect'])
                if d < 5.0: # Close or colliding!
                    print(f"COLLISION: edge '{eid}' ({src} -> {tgt}) collides with '{nid}' (val={ndata['val']}) at dist={d:.1f} px!")
