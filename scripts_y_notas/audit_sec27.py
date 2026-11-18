with open('scripts_y_notas/full_tpi_text_new.txt', 'r', encoding='utf-8') as f:
    text = f.read()

s27 = text.find("2.7 Diagrama de casos de uso")
s28 = text.find("2.8. Plantilla de descripción")
print(text[s27:s28])
