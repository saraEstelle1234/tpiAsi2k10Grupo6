from PIL import Image

im = Image.open('media_presentacion/page_15_img_0_50.png')
print("page_15_img_0_50 (DCD) size:", im.size)
print("Aspect ratio:", im.size[0] / im.size[1])
