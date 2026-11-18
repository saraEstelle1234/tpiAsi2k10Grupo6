with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

s14_start = html.find('id="slide-14"')
print(html[s14_start+5500:s14_start+9000])
