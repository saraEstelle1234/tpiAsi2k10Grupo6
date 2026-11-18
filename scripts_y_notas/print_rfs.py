with open("scripts_y_notas/rf_analysis.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re
rfs = []
for line in text.split("\n"):
    clean = line.replace('\u200b', '').strip()
    m = re.match(r"^(\d+)[\.\?\)]\s*(.*)", clean)
    if m:
        rfs.append((int(m.group(1)), m.group(2).strip()))

print(f"Total RFs found: {len(rfs)}")
for n, name in rfs:
    print(f"RF {n:2d}: {name.encode('ascii', errors='replace').decode('ascii')}")
