with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = re.findall(r'<button[^>]*dock[^>]*>', html)
print('Dock buttons found:', len(matches))
if matches:
    print(matches[:3])
else:
    # let's find class="dock"
    pos = html.find('class="dock"')
    if pos != -1:
        print(html[pos:pos+400])
    else:
        print('class="dock" not found, searching dock in html')
        pos = html.find('dock')
        print(html[pos-50:pos+200])
