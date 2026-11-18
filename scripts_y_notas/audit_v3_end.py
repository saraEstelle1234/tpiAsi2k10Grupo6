with open('scripts_y_notas/full_tpi_text_v3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

s = text.find("Gestionar Incidentes")
e = text.find("Requerimientos No Funcionales")
print(text[s:e])
