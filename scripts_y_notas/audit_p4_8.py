with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("======================================== PAGE ")

for p in range(4, 9):
    print(f"\n{'='*20} PAGE {p} {'='*20}")
    print(pages[p][:1500].encode('ascii', errors='replace').decode('ascii'))
