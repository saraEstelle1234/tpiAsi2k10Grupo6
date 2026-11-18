with open("scripts_y_notas/pdf_dump_all.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
print("=== PAGE 13 IN PDF (PLANTILLA CU) ===")
print(pages[13])
