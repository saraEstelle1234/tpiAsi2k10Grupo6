with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

print("=== SLIDE 9 ===")
print("\n".join(lines[2040:2110]))

print("=== SLIDE 11 ===")
print("\n".join(lines[2235:2280]))

print("=== SLIDE 12 ===")
print("\n".join(lines[2284:2355]))

print("=== SLIDE 13 ===")
print("\n".join(lines[2356:2450]))
