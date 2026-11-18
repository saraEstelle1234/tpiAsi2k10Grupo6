import re

with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

s9_match = re.search(r'(<div class="slide"[^>]*id="slide-9"[^>]*>.*?)(?=<div class="slide"[^>]*id="slide-10")', html, re.DOTALL)
if s9_match:
    s9 = s9_match.group(1)
    # remove the base64 image data so we can see the html structure clearly
    s9_clean = re.sub(r'data:image/png;base64,[A-Za-z0-9+/=]+', '[BASE64_DATA]', s9)
    print("Slide 9 HTML structure:\n", s9_clean)
