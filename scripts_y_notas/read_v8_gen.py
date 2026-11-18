with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size of generate_v8_deck.py:", len(text))
# print top 60 lines
lines = text.splitlines()
for i, l in enumerate(lines[:60]):
    print(f"{i+1}: {l[:100]}")
