from PIL import Image

for f in ['media/board_diagram.png', 'media/page8_diagram.png']:
    try:
        im = Image.open(f)
        print(f, im.size)
    except Exception as e:
        print(f, e)
