with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
for i in range(1, len(pages)):
    p_text = pages[i]
    lines = [l.strip() for l in p_text.splitlines() if l.strip()]
    header = lines[0] if lines else f"{i}"
    # reconstruct text by joining words
    content = " ".join(lines[1:])
    # collapse multiple spaces
    import re
    content = re.sub(r'\s+', ' ', content)
    print(f"\n>>> PAGE {i} ({len(content)} chars):")
    print(content[:300] + "..." if len(content) > 300 else content)
