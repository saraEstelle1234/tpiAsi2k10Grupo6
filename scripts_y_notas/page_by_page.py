with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
for p in pages[1:]:
    lines = [l.strip() for l in p.splitlines() if l.strip()]
    page_num = lines[0].split(" ---")[0] if lines else "?"
    print(f"\n================ PAGE {page_num} ================")
    # print first 10 non-empty lines
    for l in lines[1:12]:
        print("  ", l[:100])
