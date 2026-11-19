with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

s1 = html[:html.find('id="slide-2"')]
import re
idx_start = s1.find('<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">')
idx_end = s1.find('<!-- SLIDE 2')
members_block = s1[idx_start:idx_end]
cards = re.findall(r'<div class="card-dark" style="padding: 18px 20px;">(.*?)</div>\s*</div>', members_block, re.DOTALL)
print(f'Total cards: {len(cards)}')
for idx, c in enumerate(cards):
    lines = [l.strip() for l in c.splitlines() if l.strip()]
    print(f'=== Member {idx+1} ===')
    for l in lines:
        clean = re.sub(r'<[^>]+>', '', l).strip()
        if clean:
            print(' ', clean)
