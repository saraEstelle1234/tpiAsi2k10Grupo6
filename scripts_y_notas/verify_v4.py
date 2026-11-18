# scripts_y_notas/verify_v4.py
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Length:', len(html))
print('Ends with </html>:', html.strip().endswith('</html>'))
print('Has Manrope font:', 'Manrope' in html)

slides = [f'id="slide-{i}"' for i in range(1, 15)]
found_slides = [s for s in slides if s in html]
print(f'Slides found: {len(found_slides)} / 14')

# Check absence of invented texts
invented_texts = ['Problemática Detectada', 'Misión Institucional', 'RN1 / RN2', 'DOMINIO OO']
for inv in invented_texts:
    print(f'Invented "{inv}" present:', inv in html)

# Check presence of macOS dock
dock_checks = ['mac-dock', 'dock-hotspot', 'dock-icon-btn', 'dock-tooltip', 'mac-jumping', 'dock-touch-handle']
for dc in dock_checks:
    print(f'Dock check "{dc}":', dc in html)

# Check header counter
counter_checks = ['header-counter-box', 'tabular-nums', 'counter-current', 'counter-total']
for cc in counter_checks:
    print(f'Counter check "{cc}":', cc in html)

# Check Slide 1 members
team = [
    'Abad, Francisco', 'Cufre, Agustín', 'Marcuzzi, Tomas', 'Jastrzebski, Emiliano',
    'Molina, Tobias', 'Thomas Rapp, Francisco', 'Moyano, Lucas Uriel',
    'Tarditti, Juan Sebastián', 'Pereyra, Kevin'
]
print('All 9 members present:', all(m in html for m in team))

# Check Theme Alternation
light_slides = ['id="slide-3" data-topic="03 · Mapa de Procesos" data-theme="light"', 'id="slide-4"', 'id="slide-7"']
for ls in light_slides:
    print(f'Light slide marker "{ls}":', ls in html)

dark_slides = ['id="slide-1" data-topic="01 · Portada y Equipo" data-theme="dark"', 'id="slide-2"', 'id="slide-14"']
for ds in dark_slides:
    print(f'Dark slide marker "{ds}":', ds in html)

# Check Slide 2 content
print('Slide 2 exact objective present:', 'Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas' in html)

# Check Slide 3 content
print('Slide 3 exact processes present:', 'Planificar la programación de exposiciones' in html and 'Exponer obras de arte' in html)

# Check cards styling
print('Has card-light:', 'card-light' in html)
print('Has card-dark:', 'card-dark' in html)
