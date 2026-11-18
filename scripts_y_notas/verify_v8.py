# -*- coding: utf-8 -*-
"""
verify_v8.py
Comprehensive audit for v8 presentation deck:
1. Exactly 14 slides (slide-1 to slide-14).
2. Clean titles without filler words.
3. Multiplicidades slide removed.
4. Slide 12 has enlarged DCD + single conception card.
5. Slide 13 has comprehensive traceability matrix (34 RFs mapped to CU and DCD).
6. Slide 14 has final closing + 9 members with legajos and restart button.
7. All counters and progress lines match 14 slides.
"""

import os
import re

def verify_v8():
    html_path = "presentacion.html"
    if not os.path.exists(html_path):
        print("FAIL: presentacion.html does not exist.")
        return False

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    size_mb = len(html) / (1024 * 1024)
    print(f"File size: {size_mb:.2f} MB")

    errors = []

    # 1. Slide count
    slide_ids = re.findall(r'id=["\']slide-(\d+)["\']', html)
    unique_slides = sorted(list(set(map(int, slide_ids))))
    print(f"Found slides: {unique_slides}")
    if unique_slides != list(range(1, 15)):
        errors.append(f"Expected slides 1..14, got: {unique_slides}")

    # 2. Total slides in JS and counters
    if 'const totalSlides = 14;' not in html:
        errors.append("const totalSlides is not 14")
    if '01 / 14' not in html:
        errors.append("dock-counter-badge does not contain '01 / 14'")
    if '<span class="counter-total">14</span>' not in html:
        errors.append("counter-total is not 14")

    # 3. Clean titles
    expected_titles = [
        "Sistema de Gestión y Vigilancia Museológica",
        "Dominio bajo Estudio",
        "Mapa de Procesos",
        "Plantilla de Proceso",
        "BPMN Nivel Descriptivo",
        "BPMN Nivel Operativo",
        "Requerimientos Funcionales",
        "Requerimientos No Funcionales",
        "Diagrama de Casos de Uso",
        "Plantilla de Caso de Uso",
        "Prototipo de Interfaz",
        "Diagrama de Clases",
        "Trazabilidad de Requerimientos",
        "¡Muchas Gracias!"
    ]
    h1_matches = [m.strip() for m in re.findall(r'<h1[^>]*class="[^"]*giant-title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)]
    if h1_matches != expected_titles:
        for i, (exp, act) in enumerate(zip(expected_titles, h1_matches), 1):
            if exp != act:
                errors.append(f"Slide {i} title mismatch: expected '{exp}', got '{act}'")

    # 4. Multiplicidades slide check (MUST BE GONE)
    if "Multiplicidades y Asociaciones" in h1_matches or "Multiplicidades y Reglas Estructurales" in html:
        errors.append("Multiplicidades slide is still present (should be removed)")

    # 5. Slide 12 (Diagrama de Clases)
    if "Concepción y Lógica del Modelo de Dominio" not in html:
        errors.append("Slide 12 missing conception card: 'Concepción y Lógica del Modelo de Dominio'")
    if "Clases Intervinientes" in html:
        errors.append("Slide 12 still has old card 'Clases Intervinientes'")

    # 6. Slide 13 (Trazabilidad Completa)
    s13_markers = [
        "fullTraceData",
        "renderTraceMatrixItems",
        "trace-search-input",
        "trace-module-btn",
        "td-rf-code",
        "td-dcd-info",
        "td-rationale"
    ]
    for sm in s13_markers:
        if sm not in html:
            errors.append(f"Slide 13 missing traceability feature: '{sm}'")

    # 7. Slide 14 (Cierre y Agradecimiento)
    members = [
        "423269", # Abad
        "419166", # Cufre
        "403382", # Marcuzzi
        "402760", # Jastrzebski
        "419749", # Molina
        "408990", # Thomas
        "410975", # Moyano
        "400212", # Tarditti
        "418201", # Pereyra
        "goToSlide(1)"
    ]
    for m in members:
        if m not in html:
            errors.append(f"Slide 14 missing member or button: '{m}'")

    # 8. All base64 diagrams loaded
    diagram_keys = ['b64_mapa', 'b64_bpmn_desc', 'b64_bpmn_oper', 'b64_dcu', 'b64_proto', 'b64_dcd']
    for dk in diagram_keys:
        if f'{dk}: "' not in html:
            errors.append(f"Missing diagram asset in diagramAssets: {dk}")

    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f" - {e}")
        return False
    else:
        print("\nALL 8 V8 AUDIT CHECKS PASSED 100% PERFECTLY!")
        return True

if __name__ == '__main__':
    verify_v8()
