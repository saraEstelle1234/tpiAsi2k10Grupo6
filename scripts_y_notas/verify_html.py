with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
slides = re.findall(r'id="slide-(\d+)"', text)
print('Total slides:', len(slides), slides)
print('Contains CU-15 Step Explorer:', 'step-explorer' in text)
print('Contains Traceability Console:', 'trace-console' in text)
print('Contains Zoom Modal:', 'zoom-modal' in text)
print('Contains PDF screenshots:', 'rendered_page_' in text)
print('Ends with html tag:', text.strip().endswith('</html>'))
