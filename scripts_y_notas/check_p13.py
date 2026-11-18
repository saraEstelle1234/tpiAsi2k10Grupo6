with open('scripts_y_notas/full_tpi_text_v3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

p13 = text.find("=== PAGE 13 ===")
p14 = text.find("=== PAGE 14 ===")
print(text[p13:p14])
