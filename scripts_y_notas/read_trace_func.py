with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function renderTraceMatrixItems.*?(?=\n\s*function|\n</script>)', text, re.DOTALL)
if m:
    print("renderTraceMatrixItems:\n", m.group(0)[:800])
