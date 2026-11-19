import re

with open(r'scripts_y_notas\audit_tpi_pdf\tpi_full_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')

# Extract RFs from page 5 and 6
rf_text = pages[5] + '\n' + pages[6]
rfs = re.findall(r'(\d+)\.\s*([^\n\r]+)', rf_text)
print(f'Total RFs found in text: {len(rfs)}')
rf_dict = {int(num): name.strip() for num, name in rfs}

# Extract CUs from page 10, 11, 12
cu_text = pages[10] + '\n' + pages[11] + '\n' + pages[12]
cus = re.findall(r'(\d+)\.\s*([^\n\r:]+)', cu_text)
print(f'Total CUs found in text: {len(cus)}')
cu_dict = {int(num): name.strip() for num, name in cus}

print('\nRF Numbers:', sorted(rf_dict.keys()))
print('CU Numbers:', sorted(cu_dict.keys()))

# Check missing RFs in numbering
all_rf_nums = set(range(1, max(rf_dict.keys()) + 1))
missing_rf_nums = all_rf_nums - set(rf_dict.keys())
print('Missing RF numbers in sequence:', missing_rf_nums)

# Check missing CU numbers
all_cu_nums = set(range(1, max(cu_dict.keys()) + 1))
missing_cu_nums = all_cu_nums - set(cu_dict.keys())
print('Missing CU numbers in sequence:', missing_cu_nums)

# Check CU 15 vs RF 35
print('\nCU 15:', cu_dict.get(15))
print('RF 35:', rf_dict.get(35))
