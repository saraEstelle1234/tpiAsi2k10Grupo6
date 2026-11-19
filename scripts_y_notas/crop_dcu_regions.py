# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('scripts_y_notas/extracted_dcu_full.png')
w, h = im.size

# Let's inspect where the actors are on the left and right sides:
# We know the actors from the text:
# 1. Responsable de ingreso de obra
# 2. Administrador del museo
# 3. Responsable de atención al cliente
# 4. Administrador web
# 5. Encargado de vigilancia
# 6. Encargado de supervisión
# 7. Admin de sistema
# 8. Usuario

# Let's crop the key regions of DCU and save them:
# Region 1: Top Left (x: 0-50%, y: 0-25%)
im.crop((0, 0, int(w*0.5), int(h*0.25))).save('scripts_y_notas/dcu_reg_top_left.png')
# Region 2: Mid-Top Left (x: 0-50%, y: 25-50%)
im.crop((0, int(h*0.25), int(w*0.5), int(h*0.50))).save('scripts_y_notas/dcu_reg_midtop_left.png')
# Region 3: Mid-Bottom Left (x: 0-50%, y: 50-75%)
im.crop((0, int(h*0.50), int(w*0.5), int(h*0.75))).save('scripts_y_notas/dcu_reg_midbot_left.png')
# Region 4: Bottom Left (x: 0-50%, y: 75-100%)
im.crop((0, int(h*0.75), int(w*0.5), h)).save('scripts_y_notas/dcu_reg_bot_left.png')

# Region 5: Top Right (x: 50-100%, y: 0-25%)
im.crop((int(w*0.5), 0, w, int(h*0.25))).save('scripts_y_notas/dcu_reg_top_right.png')
# Region 6: Mid-Top Right (x: 50-100%, y: 25-50%)
im.crop((int(w*0.5), int(h*0.25), w, int(h*0.50))).save('scripts_y_notas/dcu_reg_midtop_right.png')
# Region 7: Mid-Bottom Right (x: 50-100%, y: 50-75%)
im.crop((int(w*0.5), int(h*0.50), w, int(h*0.75))).save('scripts_y_notas/dcu_reg_midbot_right.png')
# Region 8: Bottom Right (x: 50-100%, y: 75-100%)
im.crop((int(w*0.5), int(h*0.75), w, h)).save('scripts_y_notas/dcu_reg_bot_right.png')

print("Saved 8 DCU regions.")
