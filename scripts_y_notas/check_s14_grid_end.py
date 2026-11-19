with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

s14_start = text.find('id="slide-14"')
grid_start = text.find('<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">', s14_start)
print(text[grid_start:grid_start+1500])
