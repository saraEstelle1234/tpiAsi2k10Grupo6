with open(r'scripts_y_notas\generate_v9_color_deck.py', encoding='utf-8') as f:
    text = f.read()

j_idx = text.find('Jastrzebski, E.')
print(text[j_idx:j_idx+300])
