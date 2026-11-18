with open('scripts_y_notas/full_tpi_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's write out pages 3-6 (Procesos y Requerimientos) and 13 (CU)
p3_idx = text.find('PAGE 3')
p7_idx = text.find('PAGE 7')
print("=== SECTION 2.1 - 2.4 ===")
print(text[p3_idx:p7_idx])
