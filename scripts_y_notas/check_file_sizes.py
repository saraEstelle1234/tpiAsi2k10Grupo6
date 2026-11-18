import os

large_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        fp = os.path.join(root, f)
        try:
            sz = os.path.getsize(fp)
            if sz > 5 * 1024 * 1024: # > 5MB
                large_files.append((fp, sz))
        except Exception:
            pass

print("Files larger than 5MB:")
for fp, sz in large_files:
    print(f"  {fp}: {sz / (1024*1024):.2f} MB")
if not large_files:
    print("  None! All files are well within standard git size limits.")
