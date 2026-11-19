with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

import re

for i in range(1, 15):
    s_id = f'slide-{i}'
    next_id = f'slide-{i+1}' if i < 14 else '</body>'
    s_content = html[html.find(f'id="{s_id}"'):html.find(f'id="{next_id}"') if i < 14 else len(html)]
    
    # search for member names
    names = []
    for name in ['Abad', 'Cufre', 'Marcuzzi', 'Jastrzebski', 'Molina', 'Thomas', 'Moyano', 'Tarditti', 'Pereyra']:
        if name in s_content:
            names.append(name)
    print(f'Slide {i:02d}: {names}')
