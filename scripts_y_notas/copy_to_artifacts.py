# -*- coding: utf-8 -*-
import shutil
import os

artifact_dir = r"C:\Users\thoma\.gemini\antigravity\brain\5086ba7a-0eba-448a-b21d-e90862728035"

files_to_copy = ["presentacion.html", "guion_defensa_tpi.md"]

for fname in files_to_copy:
    src = fname
    dst = os.path.join(artifact_dir, fname)
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    print(f"Copied {fname} -> {dst} ({size:,} bytes)")

print("Copy completed successfully!")
