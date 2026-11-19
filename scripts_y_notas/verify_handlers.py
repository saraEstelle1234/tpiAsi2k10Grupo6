import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script
script = re.search(r'<script[^>]*>([\s\S]*?)</script>', html, re.IGNORECASE).group(1)

# Find all inline handlers: onclick="foo(...)", etc.
handlers = re.findall(r'on\w+\s*=\s*["\']([^"\']+)["\']', html)

called_functions = set()
for h in handlers:
    # Match function calls like foo() or foo(1, 2)
    matches = re.findall(r'([a-zA-Z_$][a-zA-Z0-9_$]*)\s*\(', h)
    for m in matches:
        called_functions.add(m)

print(f"Total unique functions called from inline HTML handlers: {len(called_functions)}")
missing = []
for fn in sorted(called_functions):
    # Check if defined in script (function fn, const fn =, let fn =, var fn =, or window.fn =)
    patterns = [
        rf'function\s+{fn}\s*\(',
        rf'(?:const|let|var)\s+{fn}\s*=',
        rf'window\.{fn}\s*=',
    ]
    found = any(re.search(p, script) for p in patterns)
    if not found:
        # Check if native (e.g. alert, confirm, etc.)
        if fn in ['stopPropagation', 'preventDefault', 'alert', 'confirm', 'console']:
            continue
        missing.append(fn)
    else:
        print(f"  [OK] {fn}")

if missing:
    print("\nWARNING - Potential missing functions:")
    for m in missing:
        print(f"  [MISSING?] {m}")
else:
    print("\nALL INLINE HANDLER FUNCTIONS ARE FULLY DEFINED IN SCRIPT!")
