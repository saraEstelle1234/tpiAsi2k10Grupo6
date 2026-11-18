with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

s8_start = html.find('id="slide-8"')
s9_start = html.find('id="slide-9"')
print("=== SLIDE 8 TEXT ===")
print(html[s8_start:s8_start+2000])

s14_start = html.find('id="slide-14"')
print("=== SLIDE 14 TEXT ===")
print(html[s14_start:s14_start+3000])
