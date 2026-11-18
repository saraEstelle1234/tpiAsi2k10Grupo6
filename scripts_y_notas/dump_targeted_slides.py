# -*- coding: utf-8 -*-
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

def get_slice(start_str, end_str):
    p1 = text.find(start_str)
    p2 = text.find(end_str, p1)
    return text[p1:p2]

with open('scripts_y_notas/s2_code.txt', 'w', encoding='utf-8') as f:
    f.write(get_slice('id="slide-2"', 'id="slide-3"'))

with open('scripts_y_notas/s4_code.txt', 'w', encoding='utf-8') as f:
    f.write(get_slice('id="slide-4"', 'id="slide-5"'))

with open('scripts_y_notas/s5_code.txt', 'w', encoding='utf-8') as f:
    f.write(get_slice('id="slide-5"', 'id="slide-6"'))

with open('scripts_y_notas/s12_code.txt', 'w', encoding='utf-8') as f:
    f.write(get_slice('id="slide-12"', 'id="slide-13"'))

with open('scripts_y_notas/s14_code.txt', 'w', encoding='utf-8') as f:
    # up to closing slides div
    p1 = text.find('id="slide-14"')
    p2 = text.find('</div>\n  </div>\n\n  <!-- DOCK', p1)
    if p2 == -1:
        p2 = text.find('<!-- DOCK', p1)
    f.write(text[p1:p2])

print("Dumped s2, s4, s5, s12, s14 code!")
