import os
import glob

print("Looking for image files in current dir and subdirs:")
for ext in ['*.png', '*.jpg']:
    files = glob.glob(f"**/{ext}", recursive=True)
    for f in files:
        if 'page' in f or 'dcu' in f or 'dcd' in f or 'clase' in f or 'caso' in f:
            size = os.path.getsize(f)
            print(f"{f} ({size} bytes)")
