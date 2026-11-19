import re
import json

with open('guion_defensa_tpi.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect sections in guion
sections = re.findall(r'###\s*(\d+)\.\s*([^\n]+)\n(.*?)(?=\n---\n|\Z)', text, re.DOTALL)
print("Found sections in guion:", len(sections))

notes_dict = {}

for s_num, s_title, s_body in sections:
    # Speaker name and slides
    # e.g. "Agustín Cufre (Slide 01 y 02 · Portada, Dominio y Objetivos)"
    speaker_match = re.search(r'([A-Za-záéíóúÁÉÍÓÚ\s]+)\s*\((Slide[^\)]+)\)', s_title)
    if speaker_match:
        speaker = speaker_match.group(1).strip()
        slides_text = speaker_match.group(2).strip()
    else:
        speaker = s_title.strip()
        slides_text = ""

    # Clean body: convert markdown quotes > to clean paragraphs
    clean_body = []
    bullets = []
    for line in s_body.strip().split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            clean_body.append(line.lstrip('> *').rstrip('*').strip())
        elif line.startswith('-'):
            bullets.append(line.lstrip('- *').rstrip('*').strip())
        else:
            clean_body.append(line)

    speech_text = " ".join([p for p in clean_body if p])
    
    # Extract slide numbers
    slide_nums = [int(n) for n in re.findall(r'\b\d+\b', slides_text)]
    if not slide_nums:
        slide_nums = [int(s_num)]

    for sn in slide_nums:
        if 1 <= sn <= 14:
            notes_dict[sn] = {
                "slide": sn,
                "speaker": speaker,
                "title": s_title,
                "speech": speech_text[:1200],  # clean preview
                "bullets": bullets[:4]
            }

print(f"Mapped {len(notes_dict)} slides to speaker notes.")
for sn in sorted(notes_dict.keys()):
    print(f"Slide {sn}: {notes_dict[sn]['speaker']} -> {notes_dict[sn]['speech'][:60]}...")
