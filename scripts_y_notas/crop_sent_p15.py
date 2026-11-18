from PIL import Image

img = Image.open('scripts_y_notas/sent_pdf_page15.png')
w, h = img.size
print(f"Size: {w}x{h}")

# Let's crop into 4 quadrants to see what was sent in the PDF
q1 = img.crop((0, 0, w//2, h//2))
q1.save('scripts_y_notas/sent_p15_topleft.png')

q2 = img.crop((w//2, 0, w, h//2))
q2.save('scripts_y_notas/sent_p15_topright.png')

q3 = img.crop((0, h//2, w//2, h))
q3.save('scripts_y_notas/sent_p15_botleft.png')

q4 = img.crop((w//2, h//2, w, h))
q4.save('scripts_y_notas/sent_p15_botright.png')

print("Saved quadrants.")
