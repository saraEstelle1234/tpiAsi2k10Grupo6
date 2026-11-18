with open('scripts_y_notas/build_editorial_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'b64_proto\s*=\s*(.*)', text)
if m:
    val = m.group(1)[:100]
    print("b64_proto declaration:", val)
