from PIL import Image

for fname in ['media/page6_bpmn1.png', 'media/page7_bpmn2.png']:
    try:
        img = Image.open(fname)
        print(f"{fname}: size {img.size}")
    except Exception as e:
        print(f"Error {fname}: {e}")
