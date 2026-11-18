with open('scripts_y_notas/build_editorial_html.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'b64_bpmn_oper' in line:
        print(f"Line {i+1}: {line[:80]}")
        # print next few lines
        for j in range(i, min(i+5, len(lines))):
            print(f"  {j+1}: {lines[j][:80]}")
        break
