import glob
import os

files = glob.glob('scripts_y_notas/*dcu*.py')
for f in files:
    print("---", f, "---")
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        lines = fp.readlines()
        print("".join(lines[:30]))
