with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Total length:', len(html))
print('Ends with </html>:', html.strip().endswith('</html>'))
print('Has Manrope font:', 'Manrope' in html)

slides = [f'id="slide-{i}"' for i in range(1, 15)]
found_slides = [s for s in slides if s in html]
print(f'Slides found: {len(found_slides)} / 14')

dock_elements = ['Anterior', 'Siguiente', 'Vista general', 'Pantalla completa', 'Mostrar todo', 'mini-tutorial', 'zoom-modal', 'overview-modal']
for d in dock_elements:
    print(f'Contains {d}:', d in html)

data_imgs = html.count('data:image/')
print(f'Data images count: {data_imgs}')

cu15_check = ['CU-15', 'Registrar Incidente', 'Paso 4', 'A1', 'A2', 'A3']
for c in cu15_check:
    print(f'CU15 check {c}:', c in html)

team_members = ['Tomás Marcuzzi', 'Juan Ignacio', 'Agustín Cufré', 'Tobías', 'Lucas Moyano', 'Emiliano Jastrzebski']
for m in team_members:
    print(f'Member {m}:', m in html)
