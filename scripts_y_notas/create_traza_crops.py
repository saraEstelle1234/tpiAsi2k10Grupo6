from PIL import Image

im_dcu = Image.open('scripts_y_notas/dcu_full_image.png')
w_d, h_d = im_dcu.size
# Crop Encargado de vigilancia and the two use cases: Registrar revisión and Registrar incidente
crop_dcu = im_dcu.crop((int(w_d * 0.01), int(h_d * 0.58), int(w_d * 0.40), int(h_d * 0.70)))
target_w = 480
target_h_d = int(crop_dcu.height * (target_w / crop_dcu.width))
crop_dcu = crop_dcu.resize((target_w, target_h_d), Image.Resampling.LANCZOS)
crop_dcu.save('media/traza_node_dcu.png', optimize=True)
print("Updated media/traza_node_dcu.png", crop_dcu.size)
