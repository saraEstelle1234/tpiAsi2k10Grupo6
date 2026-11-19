with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s3 = html[html.find('id="slide-3"'):html.find('id="slide-4"')]
print('=== SLIDE 3 RIGHT COLUMN ===')
for l in s3.splitlines():
    if not 'data:image' in l:
        print(l)
