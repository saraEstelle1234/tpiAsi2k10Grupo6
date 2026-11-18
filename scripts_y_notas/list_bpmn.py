import os

# Let's search for bpmn ocr or text
for f in os.listdir('scripts_y_notas'):
    if 'bpmn' in f.lower() or 'ocr' in f.lower():
        print(f)
