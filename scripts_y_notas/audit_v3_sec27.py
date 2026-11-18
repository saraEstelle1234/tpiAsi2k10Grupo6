with open('scripts_y_notas/full_tpi_text_v3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find("Objetivos de los Casos de Uso")
e = text.find("Objetivos de Actores")
print(text[s:e])
