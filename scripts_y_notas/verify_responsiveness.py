with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ("Global overflow-x protection", "overflow-x: hidden !important" in html),
    ("Tablet media query @media (max-width: 1024px)", "@media (max-width: 1024px)" in html),
    ("Tablet portrait media query @media (max-width: 860px)", "@media (max-width: 860px)" in html),
    ("Mobile media query @media (max-width: 640px)", "@media (max-width: 640px)" in html),
    ("Micro-phone media query @media (max-width: 380px)", "@media (max-width: 380px)" in html),
    ("Touch swipe navigation listener", "touchstart" in html and "touchend" in html and "nextSlideAction()" in html),
    ("Table horizontal touch scrolling", "overflow-x: auto" in html and "-webkit-overflow-scrolling: touch" in html),
    ("Compact dock for mobile", ".mac-dock-container" in html and "height: 52px !important" in html),
    ("Trace matrix responsive stacking", ".trace-matrix-console" in html and "max-height: 260px !important" in html),
    ("RF accordion responsive stacking", "#rf-accordion-list" in html and "flex-direction: column !important" in html),
]

all_ok = True
for name, ok in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        all_ok = False

if all_ok:
    print("\nALL RESPONSIVE AUDIT CHECKS PASSED 100%!")
else:
    print("\nSOME RESPONSIVE CHECKS FAILED!")
