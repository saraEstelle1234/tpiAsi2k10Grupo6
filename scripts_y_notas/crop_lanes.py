from PIL import Image

# Let's inspect lane labels on the left of BpmnNivelDescriptivo.png and BpmnNivelOperativo.png
desc = Image.open('Diagramas/BpmnNivelDescriptivo.png')
# The pool header and lane headers are typically on the left side
crop_desc_lanes = desc.crop((0, 0, 120, desc.height))
crop_desc_lanes.save('scripts_y_notas/desc_lanes.png')

oper = Image.open('Diagramas/BpmnNivelOperativo.png')
crop_oper_lanes = oper.crop((0, 0, 120, oper.height))
crop_oper_lanes.save('scripts_y_notas/oper_lanes.png')

print("Lane crops saved!")
