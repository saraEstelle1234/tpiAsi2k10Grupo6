with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s7 = html[html.find('id="slide-7"'):html.find('id="slide-8"')]
s8 = html[html.find('id="slide-8"'):html.find('id="slide-9"')]

print('=== SLIDE 7 (first 1000 chars) ===')
print(s7[:1000])

print('=== SLIDE 8 (first 1000 chars) ===')
print(s8[:1000])
