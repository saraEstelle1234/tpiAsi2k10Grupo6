with open("scripts_y_notas/enunciado_dump.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
if len(pages) > 4:
    print("=== FULL PAGE 4 ENUNCIADO ===")
    print(pages[4])
