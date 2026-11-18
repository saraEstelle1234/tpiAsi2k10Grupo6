with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    deck = f.read()

script_idx = deck.rfind('</script>')
print(f"</script> found at {script_idx}")
print(deck[script_idx-250:script_idx])
