# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
idx = html.find('id="rf-accordion-list"')
print(html[idx:idx+900])
