with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("======================================== PAGE ")
print("=== PAGE 3 ===")
print(pages[3])
print("=== PAGE 4 ===")
print(pages[4])
