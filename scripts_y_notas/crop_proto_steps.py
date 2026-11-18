from PIL import Image

im = Image.open('scripts_y_notas/tablet_proto.png')
w, h = im.size

# Screen bounds in the tablet mockup:
# Bezel is from ~122 to ~1926 (width = 1804px) -> ~6% to ~94%
# Y is from ~60 to ~992 (height = 932px) -> ~5% to ~87%

# Let's save 3 crops corresponding to the 3 steps of CU-15:
# Step 1: Busqueda de Obra (input field and obra info)
# Usually top-left or upper area of the form
im.crop((int(w*0.12), int(h*0.22), int(w*0.52), int(h*0.52))).save("scripts_y_notas/proto_step1_busqueda.png")

# Step 2: Tipificacion del incidente (select / textarea)
im.crop((int(w*0.12), int(h*0.50), int(w*0.88), int(h*0.75))).save("scripts_y_notas/proto_step2_tipo.png")

# Step 3: Botones de confirmacion (Registrar Incidente / Cancelar)
im.crop((int(w*0.55), int(h*0.75), int(w*0.88), int(h*0.87))).save("scripts_y_notas/proto_step3_botones.png")

print("Saved test crops for the 3 steps.")
