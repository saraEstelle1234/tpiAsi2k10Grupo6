with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

bad_snippet = '''    function closeShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.remove('active');
    }}
}
      const btns = event.target.parentElement.querySelectorAll('.preset-btn');
      btns.forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
    }}'''

clean_snippet = '''    function openShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.add('active');
    }}
    function closeShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.remove('active');
    }}'''

# Also let's check for any duplicate openShortcutsModal
if bad_snippet in text:
    text = text.replace(bad_snippet, '''    function closeShortcutsModal() {{
      const modal = document.getElementById('shortcuts-modal');
      if (modal) modal.classList.remove('active');
    }}''')
    print("Cleaned residual bad snippet.")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated generate_v8_deck.py.")
