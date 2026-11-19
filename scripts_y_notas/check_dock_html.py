import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('mac-dock in html:', 'id="mac-dock"' in html)
print('dock-hotspot in html:', 'id="dock-hotspot"' in html)
print('dock-touch-handle in html:', 'dock-touch-handle' in html)

m = re.search(r'(<div[^>]*id="dock-hotspot"[\s\S]*?<!-- End macOS Dock -->)', html)
if not m:
    m = re.search(r'(<div[^>]*id="dock-hotspot"[\s\S]*?</div>\s*</div>\s*</div>)', html)
if m:
    print("Found dock HTML:\n", m.group(0)[:800])
else:
    # let's search for dock-hotspot context
    idx = html.find('id="dock-hotspot"')
    print("Found index:", idx)
    print(html[idx:idx+1500])
