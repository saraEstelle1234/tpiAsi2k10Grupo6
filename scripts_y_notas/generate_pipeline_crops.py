from PIL import Image

# 1. BPMN Operativo: Crop the Incident detection and registration tasks
im_bpmn = Image.open('media/bpmn_operativo_corregido.png')
w, h = im_bpmn.size
print("BPMN size:", w, h)
# Let's crop center-left where the incident tasks are
# Let's save a crop of around 35% to 70% width, 20% to 75% height
crop_bpmn = im_bpmn.crop((int(w * 0.28), int(h * 0.18), int(w * 0.68), int(h * 0.65)))
crop_bpmn.save('scripts_y_notas/test_crop_bpmn.png')

# 2. DCU: Crop CU-15 Registrar Incidente
im_dcu = Image.open('media/page8_diagram.png')
w_dcu, h_dcu = im_dcu.size
print("DCU size:", w_dcu, h_dcu)
# Let's crop around center/right where incident use cases are
crop_dcu = im_dcu.crop((int(w_dcu * 0.25), int(h_dcu * 0.35), int(w_dcu * 0.75), int(h_dcu * 0.65)))
crop_dcu.save('scripts_y_notas/test_crop_dcu.png')

# 3. Prototipo: Crop top/middle
im_proto = Image.open('media/page13_prototipo.png')
w_p, h_p = im_proto.size
print("Proto size:", w_p, h_p)
crop_proto = im_proto.crop((int(w_p * 0.05), int(h_p * 0.12), int(w_p * 0.65), int(h_p * 0.75)))
crop_proto.save('scripts_y_notas/test_crop_proto.png')

# 4. DCD: Crop Incidente & Sala classes
im_dcd = Image.open('media/board_crop_1_left.png')
w_dcd, h_dcd = im_dcd.size
print("DCD size:", w_dcd, h_dcd)
crop_dcd = im_dcd.crop((int(w_dcd * 0.05), int(h_dcd * 0.05), int(w_dcd * 0.95), int(h_dcd * 0.7)))
crop_dcd.save('scripts_y_notas/test_crop_dcd.png')

print("All test crops generated.")
