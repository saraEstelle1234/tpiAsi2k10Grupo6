with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s13 = html[html.find('id="slide-13"'):html.find('id="slide-14"')]
print('=== SLIDE 13 CONTENT ===')
for l in s13.splitlines():
    print(l)
