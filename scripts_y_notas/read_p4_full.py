with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
print("=== FULL PAGE 4 IN PDF ===")
print(pages[4])
