with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

s_idx = text.find('NATIVE TOUCH SWIPE NAVIGATION')
print("presentacion.html around NATIVE TOUCH SWIPE NAVIGATION:")
print(text[s_idx:s_idx+600])
