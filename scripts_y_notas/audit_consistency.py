with open('scripts_y_notas/full_tpi_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect sections:
# 1. Procesos de negocio
# 2. Requerimientos funcionales
# 3. DCU
# 4. CU Registrar incidente
# 5. DCD
print("Length of full_tpi_text:", len(text))

# Let's search for key terms and check consistency:
# - States of Obra: "Inactivo" vs "Inactiva" vs "Baja" vs "Restauracion"
# - States of Revision: "con observación pendiente", "sin novedades"
# - Attributes of Obra in CU vs DCD vs Prototipo
# - Attributes of Incidente in CU vs DCD vs Prototipo
# - Attributes of Sala in CU vs DCD vs Prototipo
# - Actor names: "Encargado de vigilancia" (EV) vs "Guardia"
# - Process names vs CU names vs RF names
