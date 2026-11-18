# scripts_y_notas/verify_v3.py
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
for m in team:
    if m not in html:
        print('Missing member:', m)
print('All 9 members present:', all(m in html for m in team))

# Check Slide 2 content
s2_checks = [
    'Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas',
    'preservando las obras con un sistema de gestión de incidentes',
    'Regla de Reingreso Obligatorio a Depósito'
]
for sc in s2_checks:
    print(f'Slide 2 check "{sc[:35]}...":', sc in html)

# Check Slide 3 content
s3_checks = [
    'Planificar la programación de exposiciones',
    'Planificar visitas guiadas',
    'Definir precios de guía',
    'Definir precios de entrada',
    'Exponer obras de arte',
    'Gestionar ingreso de obras artísticas',
    'Gestionar incidentes y restauración de obras',
    'Administrar RRHH'
]
for sc in s3_checks:
    print(f'Slide 3 check "{sc}":', sc in html)

# Check SVG decor
svg_decor_count = html.count('class="svg-decor-bg"')
print(f'SVG decor elements count: {svg_decor_count}')
