import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.findall(r'(\.deck-container[^{]*\{[^}]+\}|\.slide-viewport[^{]*\{[^}]+\}|main[^{]*\{[^}]+\})', html)
for rule in m:
    print(rule)
