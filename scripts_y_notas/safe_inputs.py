import re
import shutil

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    "const query = document.getElementById('trace-search-input')?.value.toLowerCase() || '';",
    "const query = (document.getElementById('trace-search-input')?.value || '').toLowerCase();"
)

c = c.replace(
    "const query = document.getElementById('rf-search-input').value.toLowerCase().trim();",
    "const rfInput = document.getElementById('rf-search-input');\n      const query = (rfInput ? rfInput.value : '').toLowerCase().trim();"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

shutil.copyfile('index.html', 'presentacion.html')
print("Updated search input handlers and synced to presentacion.html")
