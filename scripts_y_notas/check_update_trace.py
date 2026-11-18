with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m_trace = re.search(r'function updateTraceDossier.*?(?=\n\s*function|\n</script>)', text, re.DOTALL)
if m_trace:
    print("updateTraceDossier:\n", m_trace.group(0))
