# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_s6 = text.find('id="slide-6"')
idx_s6_end = text.find('id="slide-7"')
s6_chunk = text[idx_s6:idx_s6_end]

idx_inner = s6_chunk.find('id="bpmn-oper-inner"')
print(s6_chunk[idx_inner:idx_inner+600])
