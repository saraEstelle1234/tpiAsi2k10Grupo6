from PIL import Image

# Let's inspect page_3 (mapa de procesos)
im3 = Image.open('media_presentacion/page_3_img_0_16.png')
# Save top, middle, bottom
w3, h3 = im3.size
im3.crop((0, 0, w3, int(h3*0.35))).save("scripts_y_notas/mapa_top.png")
im3.crop((0, int(h3*0.35), w3, int(h3*0.65))).save("scripts_y_notas/mapa_mid.png")
im3.crop((0, int(h3*0.65), w3, h3)).save("scripts_y_notas/mapa_bot.png")

# Let's inspect page_7 (bpmn descriptivo)
im7 = Image.open('media_presentacion/page_7_img_0_26.png')
w7, h7 = im7.size
# Crop left lane headers, middle tasks, right tasks
im7.crop((0, 0, int(w7*0.25), h7)).save("scripts_y_notas/bpmn_desc_lanes.png")
im7.crop((int(w7*0.2), 0, int(w7*0.6), h7)).save("scripts_y_notas/bpmn_desc_tasks1.png")
im7.crop((int(w7*0.6), 0, w7, h7)).save("scripts_y_notas/bpmn_desc_tasks2.png")

# Let's inspect page_8 (bpmn operativo)
im8 = Image.open('media_presentacion/page_8_img_0_29.png')
w8, h8 = im8.size
im8.crop((0, 0, int(w8*0.25), h8)).save("scripts_y_notas/bpmn_oper_lanes.png")
im8.crop((int(w8*0.2), 0, int(w8*0.6), h8)).save("scripts_y_notas/bpmn_oper_tasks1.png")
im8.crop((int(w8*0.6), 0, w8, h8)).save("scripts_y_notas/bpmn_oper_tasks2.png")

print("Saved inspection crops for Mapa and BPMNs!")
