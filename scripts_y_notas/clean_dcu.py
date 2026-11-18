with open("scripts_y_notas/dcu_cells.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

actors = []
use_cases = []
for line in lines:
    parts = line.strip().split(" | ")
    if len(parts) >= 2:
        cid, val = parts[0], parts[1]
        if "actor" in line.lower():
            actors.append((cid, val))
        elif not cid.startswith("note") and not cid.startswith("sys_") and not "title" in cid:
            use_cases.append((cid, val))

with open("scripts_y_notas/dcu_clean_list.txt", "w", encoding="utf-8") as out:
    out.write("ACTORS IN DCU:\n")
    for cid, val in actors:
        out.write(f"  {cid}: {val}\n")
    out.write(f"\nUSE CASES IN DCU ({len(use_cases)}):\n")
    for cid, val in use_cases:
        out.write(f"  {cid}: {val}\n")

print(f"Actors found: {len(actors)}, Use cases: {len(use_cases)}")
