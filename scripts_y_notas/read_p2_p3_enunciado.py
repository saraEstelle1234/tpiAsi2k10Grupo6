with open("scripts_y_notas/enunciado_dump.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("--- PAGE ")
print("=== PAGE 2 ===")
print(pages[2])
print("\n=== PAGE 3 ===")
print(pages[3])
