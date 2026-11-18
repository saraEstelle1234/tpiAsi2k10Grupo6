with open("scripts_y_notas/diff_report.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

import sys
clean_lines = [l.encode('ascii', errors='replace').decode('ascii') for l in lines]

for line in clean_lines:
    if "[EN DCU PERO NO EN PDF]" in line or "[EN PDF PERO NO EN DCU]" in line:
        print(line.strip())
