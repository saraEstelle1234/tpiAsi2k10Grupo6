with open("guion_defensa_tpi.md", "r", encoding="utf-8") as f:
    text = f.read()

for l in text.splitlines():
    if l.startswith("## ") or l.startswith("### "):
        print(l)
