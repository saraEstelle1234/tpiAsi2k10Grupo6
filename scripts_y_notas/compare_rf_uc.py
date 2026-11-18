import re

with open('scripts_y_notas/full_tpi_text_new.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract RFs from 2.4
rf_text = text[text.find("2.4 Especificación de Requerimientos"):text.find("Requerimientos No Funcionales")]
rfs = []
for line in rf_text.split('\n'):
    line = line.strip()
    # match number. Name
    m = re.match(r'^(\d+)\.\s*(.*)', line)
    if m:
        rfs.append((int(m.group(1)), m.group(2).strip()))

print(f"Total RFs found: {len(rfs)}")

# Extract UCs from 2.7
uc_text = text[text.find("Objetivos de los Casos de Uso"):text.find("Objetivos de Actores")]
ucs = []
for line in uc_text.split('\n'):
    line = line.strip()
    m = re.match(r'^(\d+)\.\s*([^:]+):', line)
    if m:
        ucs.append((int(m.group(1)), m.group(2).strip()))

print(f"Total UCs found in 2.7 text: {len(ucs)}")

print("\n--- COMPARISON RF vs UC ---")
max_len = max(len(rfs), len(ucs))
for i in range(max_len):
    rf_str = f"RF {rfs[i][0]}: {rfs[i][1]}" if i < len(rfs) else "---"
    uc_str = f"CU {ucs[i][0]}: {ucs[i][1]}" if i < len(ucs) else "---"
    print(f"{rf_str:55} | {uc_str:55}")
