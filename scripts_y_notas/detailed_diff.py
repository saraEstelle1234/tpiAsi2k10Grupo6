import xml.etree.ElementTree as ET

# Read drawio ucs
tree = ET.parse("Diagramas/Diagrama_de_Casos_de_Uso.drawio")
root = tree.getroot()

dcu_ucs = []
for cell in root.iter("mxCell"):
    style = cell.get("style", "")
    val = cell.get("value", "")
    cid = cell.get("id", "")
    if cid.startswith("uc_") and not cid.endswith("_txt") and not cid.endswith("_callout") and not cid.endswith("_boundary") and not cid.endswith("_box"):
        # get text from uc_xxx_txt if exists
        txt_cell = root.find(f".//mxCell[@id='{cid}_txt']")
        if txt_cell is not None:
            cval = txt_cell.get("value", "").replace("<br>", " ").replace("&#xa;", " ").replace("\n", " ").strip()
            dcu_ucs.append((cid, cval))
        else:
            cval = val.replace("<br>", " ").replace("&#xa;", " ").replace("\n", " ").strip()
            dcu_ucs.append((cid, cval))

print(f"Total DCU use cases in drawio: {len(dcu_ucs)}")

# Read pdf ucs from ucs_comparison.txt
pdf_ucs = []
with open("scripts_y_notas/ucs_comparison.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    if line.startswith("=== USE CASES IN DRAWIO"):
        break
    if line.strip() and line[0].isdigit():
        parts = line.strip().split(". ", 1)
        if len(parts) == 2:
            pdf_ucs.append((int(parts[0]), parts[1]))

print(f"Total PDF use cases: {len(pdf_ucs)}")

# Compare lists
pdf_names = [name.lower() for _, name in pdf_ucs]
dcu_names = [name.lower() for _, name in dcu_ucs]

print("\n--- IN DCU BUT MISSING IN PDF ---")
for cid, name in dcu_ucs:
    # check if name in pdf_names
    found = False
    for pname in pdf_names:
        if name.lower() in pname or pname in name.lower():
            found = True
            break
    if not found:
        print(f"DCU has '{name}' (id={cid}) -> NOT found in PDF list!")

print("\n--- IN PDF BUT MISSING IN DCU ---")
for num, name in pdf_ucs:
    found = False
    for cid, dname in dcu_ucs:
        if name.lower() in dname.lower() or dname.lower() in name.lower():
            found = True
            break
    if not found:
        print(f"PDF has {num}. '{name}' -> NOT found in DCU!")
