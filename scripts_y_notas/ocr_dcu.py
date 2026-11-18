# -*- coding: utf-8 -*-
try:
    import pytesseract
    from PIL import Image
    for q in ['topleft', 'topright', 'botleft', 'botright']:
        txt = pytesseract.image_to_string(Image.open(f'scripts_y_notas/dcu_q_{q}.png'))
        print(f"=== {q.upper()} ===")
        actors = [l for l in txt.splitlines() if any(k in l.lower() for k in ['guardia', 'supervisor', 'obra', 'admin', 'ingreso', 'visita', 'guia', 'cliente'])]
        print("Actors/Keywords found:", actors[:6])
except Exception as e:
    print("Error / No tesseract:", e)
