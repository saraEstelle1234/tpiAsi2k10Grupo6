with open("scripts_y_notas/pdf_analysis_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Print without console encoding errors by sanitizing
import sys
clean_text = text.encode('ascii', errors='replace').decode('ascii')
print(clean_text[:3000])
