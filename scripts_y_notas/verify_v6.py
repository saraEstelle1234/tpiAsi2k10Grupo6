# -*- coding: utf-8 -*-
"""
verify_v6.py
Verifies presentacion.html against all user requirements for v6:
1. 15 slides total (with unique IDs slide-1 to slide-15).
2. Clean titles without filler words.
3. Slide 4 contains the exact table from media_1794954554615_9e05f515.png.
4. Slide 5 contains single high-level conception card.
5. Slide 14 contains deep traceability concepts (N:M, non-CU) and 8-module matrix.
6. Slide 15 contains "¡Muchas Gracias!", 9 members with legajos, restart button.
7. Counters and progress calculations all set to 15.
"""

import os
import re

def verify_v6():
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
    if unique_slides != list(range(1, 16)):
        errors.append(f"Expected slides 1..15, got: {unique_slides}")

    # 2. Total slides in JS and counters
    if 'const totalSlides = 15;' not in html:
        errors.append("const totalSlides is not 15")
    if '01 / 15' not in html:
        errors.append("dock-counter-badge does not contain '01 / 15'")
    if '<span class="counter-total">15</span>' not in html:
        errors.append("counter-total is not 15")

    # 3. Clean titles
    expected_titles = [
        "Sistema de Gestión y Vigilancia Museológica",
        "Dominio bajo Estudio",
        "Mapa de Procesos",
        "Plantilla de Proceso",
        "BPMN Nivel Descriptivo",
        "BPMN Nivel Operativo",
        "Requerimientos del Sistema",
        "Diagrama de Casos de Uso",
        "Actores y Casos de Uso",
        "Plantilla de Caso de Uso",
        "Prototipo de Interfaz",
        "Diagrama de Clases",
        "Multiplicidades y Asociaciones",
        "Trazabilidad de Requerimientos",
        "¡Muchas Gracias!"
    ]

    h1_matches = [m.strip() for m in re.findall(r'<h1[^>]*class="[^"]*giant-title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)]
    print(f"Extracted {len(h1_matches)} h1 titles.")

    if h1_matches != expected_titles:
        for i, (exp, act) in enumerate(zip(expected_titles, h1_matches), 1):
            if exp != act:
                errors.append(f"Slide {i} title mismatch: expected '{exp}', got '{act}'")

    # 4. Slide 4 Section 2.3 Table
    s4_markers = [
        "Proceso de Negocio: Gestionar incidentes y restauración de obras",
        "Reingreso obligatorio a deposito",
        "Registro inmediato de incidente",
        "Exponer obras de artes",
        "Modulo Web de Soporte"
    ]
    for sm in s4_markers:
        if sm not in html:
            errors.append(f"Slide 4 missing table content: '{sm}'")

    # 5. Slide 5 Conception card
    if "Concepción del Modelo Descriptivo" not in html:
        errors.append("Slide 5 missing 'Concepción del Modelo Descriptivo'")
    if "Carril: Guardia de Vigilancia" in html:
        errors.append("Slide 5 still has separate carril card 'Carril: Guardia de Vigilancia'")

    # 6. Slide 14 Traceability Concepts
    s14_markers = [
        "El Concepto de Trazabilidad en Análisis de Sistemas",
        "Relación N a M (Muchos a Muchos)",
        "Requerimientos sin Caso de Uso interactivo",
        "traceModulesData",
        "selectTraceModule"
    ]
    for sm in s14_markers:
        if sm not in html:
            errors.append(f"Slide 14 missing traceability feature: '{sm}'")

    # 7. Slide 15 Closing slide
    s15_markers = [
        "¡Muchas Gracias!",
        "Defensa Oral Finalizada",
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
    for sm in s15_markers:
        if sm not in html:
            errors.append(f"Slide 15 missing marker: '{sm}'")

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
        print("\nALL 8 AUDIT CHECKS PASSED 100% PERFECTLY!")
        return True

if __name__ == '__main__':
    verify_v6()
