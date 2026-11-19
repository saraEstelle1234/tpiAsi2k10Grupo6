import re

file_path = 'scripts_y_notas/generate_v9_color_deck.py'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update image path to HD
old_img = "with open('media/museo_historia_natural.png', 'rb') as _f_mus:"
new_img = "with open('media/museo_historia_natural_hd.png', 'rb') as _f_mus:"
if old_img in content:
    content = content.replace(old_img, new_img)
    print("Replaced museum image with HD version")
else:
    print("WARNING: old_img string not found")

# 2. Remove floating pill from Slide 1
pill_pattern = r'\s*<!-- Museum Official Case Floating Pill -->\s*<div style="display: inline-flex; align-items: center; gap: 10px; background: rgba\(56, 189, 248, 0\.12\);.*?</div>\s*(?=<div class="breadcrumb-tag")'
content_new, count = re.subn(pill_pattern, '\n\n        ', content, flags=re.DOTALL)
if count > 0:
    print(f"Removed {count} floating pill block(s)")
    content = content_new
else:
    print("WARNING: pill_pattern did not match, trying direct string replacement")
    pill_exact = '''        <!-- Museum Official Case Floating Pill -->
        <div style="display: inline-flex; align-items: center; gap: 10px; background: rgba(56, 189, 248, 0.12); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 999px; padding: 4px 16px 4px 6px; margin-bottom: 14px; box-shadow: 0 4px 16px rgba(0,0,0,0.3);">
          <img src="data:image/png;base64,{b64_museum}" alt="Museo" style="width: 26px; height: 26px; border-radius: 50%; object-fit: cover; border: 1.5px solid #38BDF8;">
          <span style="font-size: 11.5px; font-weight: 800; color: #BAE6FD; text-transform: uppercase; letter-spacing: 0.06em;">Museo de Historia Natural &bull; Caso Oficial 2026</span>
        </div>\n\n'''
    if pill_exact in content:
        content = content.replace(pill_exact, '')
        print("Replaced exact pill string successfully")
    else:
        print("ERROR: Could not find exact pill block!")

# 3. Enhance responsive queries for repeat(4, 1fr)
old_tablet_s1 = '#slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 12px !important;\n      }'
new_tablet_s1 = '#slide-1 [style*="grid-template-columns: repeat(3, 1fr)"],\n      #slide-1 [style*="grid-template-columns: repeat(4, 1fr)"] {\n        grid-template-columns: repeat(2, 1fr) !important;\n        gap: 12px !important;\n      }'
if old_tablet_s1 in content:
    content = content.replace(old_tablet_s1, new_tablet_s1)
    print("Updated tablet media query for Slide 1")

old_tablet_s14 = '#slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 8px !important;\n      }'
new_tablet_s14 = '#slide-14 [style*="grid-template-columns: repeat(3, 1fr)"],\n      #slide-14 [style*="grid-template-columns: repeat(4, 1fr)"] {\n        grid-template-columns: repeat(2, 1fr) !important;\n        gap: 8px !important;\n      }'
if old_tablet_s14 in content:
    content = content.replace(old_tablet_s14, new_tablet_s14)
    print("Updated tablet media query for Slide 14")

old_phone_s1 = '#slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 10px !important;\n      }\n      #slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] > .card-dark {\n        padding: 14px 16px !important;\n      }'
new_phone_s1 = '#slide-1 [style*="grid-template-columns: repeat(3, 1fr)"],\n      #slide-1 [style*="grid-template-columns: repeat(4, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 10px !important;\n      }\n      #slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] > .card-dark,\n      #slide-1 [style*="grid-template-columns: repeat(4, 1fr)"] > .card-dark {\n        padding: 14px 16px !important;\n      }'
if old_phone_s1 in content:
    content = content.replace(old_phone_s1, new_phone_s1)
    print("Updated phone media query for Slide 1")

old_phone_s14 = '#slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 8px !important;\n      }'
new_phone_s14 = '#slide-14 [style*="grid-template-columns: repeat(3, 1fr)"],\n      #slide-14 [style*="grid-template-columns: repeat(4, 1fr)"] {\n        grid-template-columns: 1fr !important;\n        gap: 8px !important;\n      }'
if old_phone_s14 in content:
    content = content.replace(old_phone_s14, new_phone_s14)
    print("Updated phone media query for Slide 14")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_v9_color_deck.py updated successfully.")
