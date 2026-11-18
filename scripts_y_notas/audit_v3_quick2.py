with open('scripts_y_notas/full_tpi_text_v3.txt', 'r', encoding='utf-8') as f:
    text = f.read()

def get_sec(s_str, e_str):
    s = text.find(s_str)
    e = text.find(e_str, s) if s != -1 else -1
    return text[s:e] if (s != -1 and e != -1) else "NOT FOUND"

print("--- 2.4 REQUERIMIENTOS ---")
sec_24 = get_sec("2.4 Especificación de Requerimientos", "2.5 BPMN")
for line in sec_24.split('\n'):
    l = line.strip()
    words = ['Gestionar Visitas', 'escuela', '26.', '27.', '28.', '29.', '30.', '31.', '32.', '35.', '38.', '42.', '45.']
    if any(w in l for w in words):
        print(line)

print("\n--- 2.8 PLANTILLA CU ---")
sec_28 = get_sec("DESCRIPCIÓN DE CASO DE USO", "PROTOTIPO DE INTERFAZ")
for line in sec_28.split('\n')[:25]:
    print(line)
