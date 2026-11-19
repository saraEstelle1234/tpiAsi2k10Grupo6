import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

s9_start = content.find('id="slide-9"')
s9_start = content.rfind('<div class="slide"', 0, s9_start)
s9_end = content.find('id="slide-10"', s9_start)
s9_end = content.rfind('<div class="slide"', s9_start, s9_end)

s9_html = content[s9_start:s9_end]

# Mask base64 string
s9_masked = re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', 'data:image/png;base64,[BASE64_DATA]', s9_html)
print(s9_masked)
