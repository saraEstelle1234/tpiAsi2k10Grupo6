from PIL import Image

im = Image.open('scripts_y_notas/page15_new_dcd.png')
w, h = im.size

# Let's test candidates for each sector:
# S, tx, ty
# In CSS:
# transform: scale(S) translate(tx%, ty%)
# delta_x = (tx / 100.0) * w
# delta_y = (ty / 100.0) * h
# cx = w/2.0 - delta_x
# cy = h/2.0 - delta_y
# x1 = cx - (w / S) / 2.0
# y1 = cy - (h / S) / 2.0
# x2 = cx + (w / S) / 2.0
# y2 = cy + (h / S) / 2.0

candidates = {
    # Sector 1: Incidente & Sala
    # We want y1 <= 180, y2 >= 770, x1 <= 250, x2 >= 650
    # Try S=1.65, cy=480 -> ty = (h/2 - cy)/h * 100 = (452 - 480)/904 * 100 = -3.1%
    # cx=440 -> tx = (w/2 - cx)/w * 100 = (711 - 440)/1422 * 100 = +19.0%
    's1_candidate_A': (1.65, 19.0, -3.1),
    's1_candidate_B': (1.70, 20.0, -3.5),
    's1_candidate_C': (1.60, 18.0, -3.0),
    
    # Sector 2: Obra, Material y Componentes
    # Obra is X=[640, 901], Y=[220, 632]
    # Material is X=[1000, 1181], Y=[310, 418]
    # Autor is X=[1000, 1181], Y=[150, 274]
    # Estilo is X=[1000, 1181], Y=[0, 108]
    # Estado is X=[670, 871], Y=[0, 172]
    # Box: X from ~600 to ~1230 (width ~630), Y from ~140 to ~670 (height ~530)
    # cx = (600 + 1230)/2 = 915 -> tx = (711 - 915)/1422 * 100 = -14.3%
    # cy = (140 + 670)/2 = 405 -> ty = (452 - 405)/904 * 100 = +5.2%
    # If S = 1.65:
    's2_candidate_A': (1.65, -14.3, 5.2),
    's2_candidate_B': (1.75, -15.0, 5.0),

    # Sector 3: Clase Tipo de Incidente
    # TipoIncidente is X=[0, 211], Y=[294, 402]
    # Incidente is X=[300, 531], Y=[230, 466]
    # Multiplicity 1..* between Incidente and TipoIncidente
    # Box: X from ~0 to ~550, Y from ~200 to ~480
    # cx = 275 -> tx = (711 - 275)/1422 * 100 = +30.6%
    # cy = 340 -> ty = (452 - 340)/904 * 100 = +12.4%
    # If S = 2.0:
    's3_candidate_A': (2.0, 30.6, 12.4),
    's3_candidate_B': (1.9, 29.0, 12.0),

    # Sector 4: Asignación de Sala y Guardia
    # Sala is X=[300, 531], Y=[520, 740]
    # SalaXGuardia is X=[0, 211], Y=[544, 716]
    # Guardia is X=[0, 211], Y=[760, 900]
    # In the user's uploaded image, they showed this sector where Obra was cut off on the right!
    # Box: X from ~0 to ~580 (width ~580), Y from ~500 to ~904 (height ~404)
    # cx = 290 -> tx = (711 - 290)/1422 * 100 = +29.6%
    # cy = 702 -> ty = (452 - 702)/904 * 100 = -27.6%
    # If S = 1.9:
    's4_candidate_A': (1.9, 29.6, -27.6),
    's4_candidate_B': (1.8, 28.0, -26.0)
}

for name, (s, tx, ty) in candidates.items():
    vw = w / s
    vh = h / s
    cx = w/2.0 - (tx / 100.0) * w
    cy = h/2.0 - (ty / 100.0) * h
    
    x1 = int(cx - vw/2.0)
    y1 = int(cy - vh/2.0)
    x2 = int(cx + vw/2.0)
    y2 = int(cy + vh/2.0)
    
    crop = im.crop((max(0, x1), max(0, y1), min(w, x2), min(h, y2)))
    crop.save(f'scripts_y_notas/opt_{name}.png')
    print(f"{name}: S={s}, tx={tx}%, ty={ty}% -> Viewport in image: [{x1}, {y1}, {x2}, {y2}]")
