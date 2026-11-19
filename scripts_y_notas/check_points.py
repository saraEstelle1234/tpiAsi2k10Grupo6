with open('scripts_y_notas/generate_v9_color_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

points = [
    ("Top imports", "b64_museum = base64.b64encode"),
    ("CSS end", "</style>"),
    ("Slide 6 diagram", 'id="slide-6"'),
    ("Slide 12 diagram", 'id="slide-12"'),
    ("Slide 13 start", 'id="slide-13"'),
    ("Dock buttons", 'id="dock-btn-next"'),
    ("Script end", "</script>")
]

for label, query in points:
    idx = text.find(query)
    print(f"{label}: found at {idx}")
