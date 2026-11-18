with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for repeat(3, 1fr) in the HTML
import re
print("Matches for repeat(3, 1fr) in style tags or elements:")
for line in text.splitlines():
    if 'repeat(3, 1fr)' in line or 'grid-template-columns: repeat(3' in line:
        print(" ", line[:100])
