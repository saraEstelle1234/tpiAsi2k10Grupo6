with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_idx = text.find('PERFECT RESPONSIVE ENGINE')
print(text[s_idx:s_idx+1200])
