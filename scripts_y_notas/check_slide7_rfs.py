with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

import re
s7 = html[html.find('id="slide-7"'):html.find('id="slide-8"')]
rf_lines = [l.strip() for l in s7.splitlines() if re.search(r'RF\s*\d+|<strong>\d+\.</strong>|\b\d+\.\b', l)]
for l in rf_lines[:30]:
    print(l)

# Count how many RF items
rf_items = re.findall(r'<div[^>]*>(\d+)\.\s*([^<]+)</div>', s7)
print('Count of RFs in Slide 7:', len(rf_items))
for num, name in rf_items[:15]:
    print(f'{num}. {name}')
