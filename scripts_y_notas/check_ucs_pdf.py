import re

with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract Objetivos de Casos de Uso
# Starts around "Objetivos de los Casos de Uso" and ends before "Objetivos de Actores"
start_idx = text.find("Objetivos de los Casos de Uso")
end_idx = text.find("Objetivos de Actores")

obj_text = text[start_idx:end_idx]

lines = obj_text.split("\n")
ucs = []
for line in lines:
    m = re.match(r"^\s*(\d+)[\.\?\)]\s*(.*?)(?::|$)", line)
    if m:
        ucs.append((int(m.group(1)), m.group(2).strip(), line.strip()))

print(f"Total Use Cases listed in PDF: {len(ucs)}")
for num, name, raw in ucs:
    print(f"{num:2d}: {name}")
