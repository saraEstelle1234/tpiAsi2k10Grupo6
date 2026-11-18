with open('scripts_y_notas/full_tpi_text_new.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Section 2.3, 2.4, 2.7, 2.8, 2.9
def extract_section(start_str, end_str):
    s = text.find(start_str)
    if s == -1:
        return f"NOT FOUND: {start_str}"
    e = text.find(end_str, s)
    if e == -1:
        return text[s:s+3000]
    return text[s:e]

print("=== 2.3 PLANILLA DE PROCESO ===")
print(extract_section("2.3 Planilla de descripción", "2.4 Especificación"))

print("\n=== 2.4 REQUERIMIENTOS ===")
print(extract_section("2.4 Especificación de Requerimientos", "2.5 BPMN"))

print("\n=== 2.8 DESCRIPCIÓN DE CASO DE USO ===")
print(extract_section("2.8. Plantilla de descripción", "PROTOTIPO DE INTERFAZ"))
