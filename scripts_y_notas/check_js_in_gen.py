with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function setDiagramPreset.*?(?=\n\s*function|\n</script>)', text, re.DOTALL)
if m:
    print("setDiagramPreset in generate_v8_deck.py:\n", m.group(0))

m_trace = re.search(r'function selectTraceDetail.*?(?=\n\s*function|\n</script>)', text, re.DOTALL)
if m_trace:
    print("\nselectTraceDetail in generate_v8_deck.py:\n", m_trace.group(0)[:600])
