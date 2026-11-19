# -*- coding: utf-8 -*-
with open('presentacion.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check setDcuSector
idx_dcu_fn = text.find('function setDcuSector')
print("setDcuSector found:", idx_dcu_fn != -1)
print(text[idx_dcu_fn:idx_dcu_fn+500])

# Check setDcdTour
idx_dcd_fn = text.find('function setDcdTour')
print("\nsetDcdTour found:", idx_dcd_fn != -1)
print(text[idx_dcd_fn:idx_dcd_fn+500])

# Check setBpmnTour
idx_bpmn_fn = text.find('function setBpmnTour')
print("\nsetBpmnTour found:", idx_bpmn_fn != -1)
print(text[idx_bpmn_fn:idx_bpmn_fn+500])
