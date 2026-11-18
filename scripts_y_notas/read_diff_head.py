# Compare the image on page 9 with Diagrama_de_Casos_de_Uso.drawio
# Let's inspect the text of the PDF on page 10-12
with open("scripts_y_notas/diff_report.txt", "r", encoding="utf-8") as f:
    print(f.read()[:2000])
