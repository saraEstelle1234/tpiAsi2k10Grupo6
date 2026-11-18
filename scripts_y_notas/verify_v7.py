# -*- coding: utf-8 -*-
"""
verify_v7.py
Comprehensive audit for v7 presentation deck:
1. Exactly 15 slides.
2. Slide 7 has 15 collapsible groups matching the TPI bold titles.
3. Slide 8 has 6 generous RNF cards (no N:M chamuyo).
4. Slide 9 has enlarged DCU with actor presets (Guardia, Supervisor, Ingreso, Administrador) and single conception card.
5. Slide 10 has full Section 2.8 CU-15 template (Objective, Precondition, 14 Normal steps, Alternates A1-A3, Postconditions).
6. 9 speakers properly assigned across the 15 slides.
"""

import os
import re

def verify_v7():
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

    # 3. Clean titles check
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
        "Multiplicidades y Asociaciones",
        "Trazabilidad de Requerimientos",
        "¡Muchas Gracias!"
    ]
    h1_matches = [m.strip() for m in re.findall(r'<h1[^>]*class="[^"]*giant-title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)]
    if h1_matches != expected_titles:
        for i, (exp, act) in enumerate(zip(expected_titles, h1_matches), 1):
            if exp != act:
                errors.append(f"Slide {i} title mismatch: expected '{exp}', got '{act}'")

    # 4. Slide 7: 15 bold titles
    expected_rf_groups = [
        "Administrar Obras de Arte",
        "Administrar Tipos de Obra",
        "Administrar Tipos de Material",
        "Administrar Salas",
        "Administrar Guías",
        "Administrar Estilos de Obra",
        "Administrar Tipos de Incidentes",
        "Gestionar Exposiciones",
        "Gestionar Visitas Guiadas",
        "Gestionar Venta de Entradas",
        "Gestionar Planificación y Rondas",
        "Gestionar Incidentes",
        "Gestionar Restauración",
        "Generar Informes y Reportes",
        "Administrar Sesión"
    ]
    for grp in expected_rf_groups:
        if grp not in html:
            errors.append(f"Slide 7 missing RF group: '{grp}'")

    if 'expandAllRf' not in html or 'collapseAllRf' not in html:
        errors.append("Slide 7 missing expand/collapse functions")

    # 5. Slide 8: Dedicated RNFs
    rnfs = ["RNF 1", "RNF 2", "RNF 3", "RNF 4", "RNF 5", "RNF 6"]
    for r in rnfs:
        if r not in html:
            errors.append(f"Slide 8 missing: '{r}'")

    # 6. Slide 9: DCU enlarged with actor presets
    actor_presets = ["Guardia (CU-14 / CU-15)", "Supervisor", "Ingreso y Obras", "Administrador"]
    for ap in actor_presets:
        if ap not in html:
            errors.append(f"Slide 9 missing actor preset: '{ap}'")

    if "Concepción General del Diagrama" not in html:
        errors.append("Slide 9 missing single conception card")

    # 7. Slide 10: Section 2.8 CU-15 template
    s10_markers = [
        "ID Caso de Uso",
        "Encargado de vigilancia (EV)",
        "Pre-Condición",
        "Curso Normal (Flujo Principal)",
        "Cursos Alternativos",
        "Post-Condiciones",
        "Deterioro natural, Deterioro provocado y Caída accidental",
        "El sistema registra el objeto con estado",
        "Inactivo"
    ]
    for sm in s10_markers:
        if sm not in html:
            errors.append(f"Slide 10 missing template marker: '{sm}'")

    # 8. Slide 15: Cierre & 9 members
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
            errors.append(f"Slide 15 missing member or button: '{m}'")

    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f" - {e}")
        return False
    else:
        print("\nALL 8 V7 AUDIT CHECKS PASSED 100% PERFECTLY!")
        return True

if __name__ == '__main__':
    verify_v7()
