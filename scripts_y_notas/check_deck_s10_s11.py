with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s10 = html[html.find('id="slide-10"'):html.find('id="slide-11"')]
s11 = html[html.find('id="slide-11"'):html.find('id="slide-12"')]

print('=== S10 snippets ===')
for l in s10.splitlines():
    if any(k in l.lower() for k in ['paso 4', 'busca', 'muestra', 'código']):
        print(l.strip()[:140])

print('\n=== S11 snippets ===')
for l in s11.splitlines():
    if any(k in l.lower() for k in ['búsqueda', 'muestra', 'objeto', 'código']):
        print(l.strip()[:140])

import re
for m in re.finditer(r'<span class="cu-step-num"[^>]*>4\.</span> <span>(.*?)</span>', html):
    print('Slide 10 Step 4 text:', m.group(1))
