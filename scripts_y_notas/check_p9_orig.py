from PIL import Image

for path in ['media_presentacion/page_9_img_0_32.png', 'media_presentacion/rendered_page_9.png']:
    try:
        im = Image.open(path)
        print(f"{path}: size={im.size}, corner={im.getpixel((0,0))}")
    except Exception as e:
        print(path, e)
