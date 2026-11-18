from PIL import Image

for p in [3, 7, 8]:
    im = Image.open(f"media_presentacion/rendered_page_7.png" if p==7 else f"media_presentacion/rendered_page_8.png" if p==8 else "media_presentacion/rendered_page_3.png")
    print(f"Page {p} size: {im.size}")
