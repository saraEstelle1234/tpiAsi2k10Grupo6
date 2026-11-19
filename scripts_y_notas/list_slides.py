with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

import re
slide_divs = re.findall(r'<div class="slide"[^>]*id="([^"]+)"[^>]*>', html)
print('Slide IDs:', slide_divs)
