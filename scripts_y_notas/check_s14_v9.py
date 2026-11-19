with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

s14 = text[text.find('id="slide-14"'):]
grid_idx = s14.find('grid-template-columns: repeat(3, 1fr);')
if grid_idx != -1:
    print('Found grid in Slide 14:')
    print(s14[grid_idx-50:grid_idx+400])
