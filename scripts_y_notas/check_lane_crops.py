from PIL import Image

# Check lane names in BpmnNivelDescriptivo.png
desc = Image.open('Diagramas/BpmnNivelDescriptivo.png')
print("Descriptivo size:", desc.size)
# The lane headers are on the left: let's save crops of left regions
for i in range(4):
    y1 = int(i * desc.height / 4)
    y2 = int((i + 1) * desc.height / 4)
    crop = desc.crop((0, y1, 150, y2))
    crop.save(f'scripts_y_notas/desc_lane_{i+1}.png')

# Also check Operativo
oper = Image.open('Diagramas/BpmnNivelOperativo.png')
print("Operativo size:", oper.size)
for i in range(4):
    y1 = int(i * oper.height / 4)
    y2 = int((i + 1) * oper.height / 4)
    crop = oper.crop((0, y1, 150, y2))
    crop.save(f'scripts_y_notas/oper_lane_{i+1}.png')

print("Crops saved!")
