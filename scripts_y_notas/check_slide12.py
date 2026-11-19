with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s12 = html[html.find('id="slide-12"'):html.find('id="slide-13"')]
print('=== SLIDE 12 FULL CONTENT ===')
print(s12)
