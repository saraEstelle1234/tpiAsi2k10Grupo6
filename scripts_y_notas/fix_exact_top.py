# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

if text.startswith('<!DO<html lang="es">'):
    text = '<!DOCTYPE html>\n<html lang="es">' + text[len('<!DO<html lang="es">'):]

with open('presentacion.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed top perfectly.")
