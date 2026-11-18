from PIL import Image

img = Image.open('media/bpmn_operativo_corregido.png')
# Crop some text areas to inspect sharpness
crop1 = img.crop((100, 10, 300, 120)) # Guardia lane top left
crop1.save('scripts_y_notas/crop_bpmn_guardia.png')
crop2 = img.crop((240, 400, 450, 480)) # Restaurador lane
crop2.save('scripts_y_notas/crop_bpmn_restaurador.png')
print("Crops saved successfully!")
