with open('guion_defensa_tpi.md', encoding='utf-8') as f:
    guion = f.read()

print('=== GUION STATS ===')
print('Length chars:', len(guion))
lines = guion.splitlines()
speakers = [l for l in lines if l.startswith('### ') or l.startswith('## ')]
for s in speakers[:25]:
    print(s)
