with open('scripts_y_notas/full_tpi_text.txt', 'r', encoding='utf-8') as f:
    pages = f.read().split('========================================')

print(f"Total pages: {len(pages)}")
for i, page in enumerate(pages):
    first_lines = [l.strip() for l in page.split('\n') if l.strip()][:3]
    print(f"Page chunk {i}: {first_lines}")
