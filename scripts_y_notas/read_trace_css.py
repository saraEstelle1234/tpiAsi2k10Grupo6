# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1040, min(1115, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
