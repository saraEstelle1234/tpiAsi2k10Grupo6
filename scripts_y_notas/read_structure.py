with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

current_page = 0
page_text = {}
for line in lines:
    if line.startswith("="*40 + " PAGE"):
        pnum = int(line.split()[2])
        current_page = pnum
        page_text[current_page] = []
    elif current_page > 0:
        page_text[current_page].append(line)

print("PAGES OVERVIEW:")
for p in sorted(page_text.keys()):
    txt = "".join(page_text[p])
    first_few = [l.strip() for l in txt.split("\n") if l.strip()][:3]
    print(f"Page {p:2d}: {len(txt):5d} chars | {' // '.join(first_few)}")
