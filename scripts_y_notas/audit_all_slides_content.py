# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# Extract text content slide by slide
slides = re.findall(r'<div class="slide" id="slide-(\d+)"[^>]*>([\s\S]*?)(?=(?:<div class="slide" id="slide-\d+")|(?:</div>\s*</div>\s*<!-- Hotspot)|(?:</body>))', html)

print(f"Total slides extracted: {len(slides)}")

for s_num, s_content in slides:
    # remove base64 images to keep output clean
    clean_content = re.sub(r'data:image/[^;]+;base64,[^"]+', '[IMAGE_DATA]', s_content)
    clean_content = re.sub(r'<svg[\s\S]*?</svg>', '[SVG]', clean_content)
    # get text snippets
    lines = [l.strip() for l in clean_content.splitlines() if l.strip() and not l.strip().startswith('<img')]
    print(f"\n=================== SLIDE {s_num} ===================")
    for line in lines[:15]:
        # print clean text
        text_only = re.sub(r'<[^>]+>', ' ', line)
        text_only = ' '.join(text_only.split())
        if text_only and text_only != '[SVG]':
            print(f"  {text_only[:120]}")
