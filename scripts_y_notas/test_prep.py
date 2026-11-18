# scripts_y_notas/generate_v3_clean_deck.py
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from build_editorial_html import (
    b64_mapa, b64_bpmn_desc, b64_bpmn_oper, b64_dcu, b64_proto, b64_dcd
)

print("Assets imported successfully.")
