import pypdf
import os

pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
print("PDF files in workspace:", pdf_files)

# Check scripts_y_notas as well
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.pdf'):
            print(os.path.join(root, f))
