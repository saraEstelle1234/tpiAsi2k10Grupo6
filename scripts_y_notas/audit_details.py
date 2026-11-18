with open("scripts_y_notas/full_tpi_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("======================================== PAGE ")

# Let's inspect Page 1 to 4:
print("=== PAGE 2: Consignas y Objetivos ===")
p2 = pages[2]
print(p2[:1200].encode('ascii', errors='replace').decode('ascii'))

print("\n=== PAGE 3 & 4: Procesos ===")
p3 = pages[3]
print(p3[:1200].encode('ascii', errors='replace').decode('ascii'))
