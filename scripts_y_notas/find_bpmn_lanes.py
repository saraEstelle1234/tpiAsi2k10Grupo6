from PIL import Image

# BPMN desc has height 1195. Let's see how many lanes there are.
# In Bizagi BPMN, lanes are separated by dark horizontal lines.
im = Image.open('media_presentacion/page_7_img_0_26.png')
w, h = im.size
print(f"BPMN desc size: {w}x{h}")

# Let's inspect rows to find horizontal dividing lines
pixels = im.load()
dividers = []
for y in range(h):
    # check if a row is mostly a solid line
    dark_count = sum(1 for x in range(100, w-100) if sum(pixels[x, y][:3]) < 200)
    if dark_count > (w - 200) * 0.7:
        dividers.append(y)

print("Horizontal lines in BPMN desc:", dividers)

# Let's crop into 3-4 sections vertically
im.crop((0, 0, w, int(h*0.33))).save("scripts_y_notas/desc_lane_1.png")
im.crop((0, int(h*0.33), w, int(h*0.66))).save("scripts_y_notas/desc_lane_2.png")
im.crop((0, int(h*0.66), w, h)).save("scripts_y_notas/desc_lane_3.png")

# Now BPMN oper
im_op = Image.open('media_presentacion/page_8_img_0_29.png')
w_op, h_op = im_op.size
print(f"BPMN oper size: {w_op}x{h_op}")
im_op.crop((0, 0, w_op, int(h_op*0.5))).save("scripts_y_notas/oper_lane_1.png")
im_op.crop((0, int(h_op*0.5), w_op, h_op)).save("scripts_y_notas/oper_lane_2.png")
print("Saved lane strips!")
