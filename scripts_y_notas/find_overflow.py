# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

for line_no, line in enumerate(html.splitlines(), 1):
    if 'overflow' in line and ('trace' in line or line_no > 1000):
        print(f"Line {line_no}: {line.strip()[:140]}")
