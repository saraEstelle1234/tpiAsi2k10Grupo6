with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s4 = html[html.find('id="slide-4"'):html.find('id="slide-5"')]
print('=== SLIDE 4 CONTENT ===')
for l in s4.splitlines():
    if not 'data:image' in l:
        print(l)
