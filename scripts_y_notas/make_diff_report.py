import re

# Read DCU use cases (take distinct text values)
with open("scripts_y_notas/dcu_clean_list.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

dcu_ucs = []
in_uc = False
for line in lines:
    if "USE CASES IN DCU" in line:
        in_uc = True
        continue
    if in_uc and " | " in line or in_uc and ":" in line:
        parts = line.strip().split(": ", 1)
        if len(parts) == 2:
            val = parts[1].strip()
            # If not in list, add
            if val and val not in dcu_ucs:
                dcu_ucs.append(val)

print(f"Distinct DCU Use Cases: {len(dcu_ucs)}")

# Read PDF use cases from scripts_y_notas/full_tpi_text.txt
with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find("Objetivos de los Casos de Uso")
end_idx = text.find("Objetivos de Actores")
obj_text = text[start_idx:end_idx]

pdf_ucs = []
for line in obj_text.split("\n"):
    clean_line = line.replace('\u200b', '').strip()
    m = re.match(r"^(\d+)[\.\?\)]\s*(.*?)(?::|$)", clean_line)
    if m:
        pdf_ucs.append((int(m.group(1)), m.group(2).strip()))

print(f"PDF Use Cases: {len(pdf_ucs)}")

with open("scripts_y_notas/diff_report.txt", "w", encoding="utf-8") as out:
    out.write("=== REPORTE DE COMPARACION DCU (45) vs PDF OBJETIVOS (42) ===\n\n")
    
    out.write("LISTA COMPLETA PDF (42):\n")
    for n, name in pdf_ucs:
        out.write(f"  {n:2d}. {name}\n")
        
    out.write(f"\nLISTA COMPLETA DCU ({len(dcu_ucs)}):\n")
    for i, name in enumerate(dcu_ucs, 1):
        out.write(f"  {i:2d}. {name}\n")

    out.write("\n=== CASOS EN DCU QUE NO ESTAN EN LA LISTA DEL PDF ===\n")
    for name in dcu_ucs:
        # Check fuzzy match
        found = any(name.lower() in p[1].lower() or p[1].lower() in name.lower() for p in pdf_ucs)
        if not found:
            out.write(f"  [EN DCU PERO NO EN PDF]: {name}\n")

    out.write("\n=== CASOS EN PDF QUE NO ESTAN EN DCU ===\n")
    for n, name in pdf_ucs:
        found = any(name.lower() in d.lower() or d.lower() in name.lower() for d in dcu_ucs)
        if not found:
            out.write(f"  [EN PDF PERO NO EN DCU]: {n}. {name}\n")

print("Report generated in scripts_y_notas/diff_report.txt")
