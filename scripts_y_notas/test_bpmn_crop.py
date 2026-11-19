from PIL import Image

im = Image.open('scripts_y_notas/bpmn_oper_full_image.png')
w, h = im.size
print('BPMN full size:', w, h)
crop = im.crop((int(w * 0.32), int(h * 0.46), int(w * 0.76), int(h * 0.88)))
crop.save('scripts_y_notas/test_crop_bpmn_clean.png')
print('BPMN crop saved')
