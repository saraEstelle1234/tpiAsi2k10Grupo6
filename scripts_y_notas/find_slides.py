with open('scripts_y_notas/generate_v9_color_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos_s14 = text.find('id="slide-14"')
pos_right = text.find('<!-- Columna Derecha', pos_s14)
print(text[pos_right:pos_right+1500])
