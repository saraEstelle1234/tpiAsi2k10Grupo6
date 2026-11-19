with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

import re
s7 = html[html.find('id="slide-7"'):html.find('id="slide-8"')]
rf_items = re.findall(r'<div class="rf-item"><span class="rf-num">(?:RF\s*)?(\d+)\.</span>\s*([^<]+)</div>', s7)
print(f'Total rf-items in Slide 7: {len(rf_items)}')
for num, name in rf_items:
    print(f'RF {num}: {name}')
