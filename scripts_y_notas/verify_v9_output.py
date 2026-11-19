with open('presentacion.html', encoding='utf-8') as f:
    html = f.read()

import re

# 1. Check museum image occurrences
mus_occurrences = html.count('alt="Museo"') + html.count('alt="Museo de Historia Natural"')
print(f'Museum image occurrences in presentacion.html: {mus_occurrences}')

# 2. Check slide count
slides = re.findall(r'<div class="slide[^"]*" id="([^"]+)"', html)
print(f'Total slides found: {len(slides)}')
print('Slide IDs:', slides)

# 3. Check CSS variables
for var in ['--cyan-bright', '--amber-warm', '--emerald-vibrant', '--purple-indigo', '--rose-coral']:
    print(f'CSS variable {var} in html:', var in html)

# 4. Check Slide 1 member cards
s1 = html[:html.find('id="slide-2"')]
legajos = re.findall(r'Leg:\s*(\d+)', s1)
print(f'Member cards with legajos in Slide 1: {len(legajos)}')

# 5. Check Slide 2 museum showcase
s2 = html[html.find('id="slide-2"'):html.find('id="slide-3"')]
print('Slide 2 has museum photograph:', 'Fotografía Oficial del Dominio' in s2)

# 6. Check Slide 12 multiplicities
s12 = html[html.find('id="slide-12"'):html.find('id="slide-13"')]
print('Slide 12 has multiplicities note:', 'Multiplicidades' in s12)

# 7. Check Slide 13 pipeline
s13 = html[html.find('id="slide-13"'):html.find('id="slide-14"')]
print('Slide 13 has pipeline:', 'trace-pipeline-container' in s13)
