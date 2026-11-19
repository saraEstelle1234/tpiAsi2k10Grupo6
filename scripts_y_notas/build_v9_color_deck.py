# -*- coding: utf-8 -*-
"""
build_v9_color_deck.py
Takes generate_v8_deck.py and applies the enhanced color palette and museum photo.
"""
import os, sys, re, base64

with open('media/museo_historia_natural.png', 'rb') as f:
    b64_museum = base64.b64encode(f.read()).decode('utf-8')

with open(r'scripts_y_notas\generate_v8_deck.py', encoding='utf-8') as f:
    code = f.read()

print('Original length:', len(code))

# 1. Add b64_museum to the imports/top variables
import_target = 'from build_editorial_html import ('
new_import = f'''# Museum image base64
with open('media/museo_historia_natural.png', 'rb') as _f_mus:
    b64_museum = base64.b64encode(_f_mus.read()).decode('utf-8')

from build_editorial_html import ('''
code = code.replace(import_target, new_import, 1)

# 2. Update CSS Root variables for enhanced multi-tone color palette
root_target = """:root {
  --navy-deep: #0A1628;
  --navy-card: #11233F;
  --navy-card-border: rgba(255, 255, 255, 0.10);
  --navy-card-hover: #162B4E;
  
  --blue-accent: #2F6BFF;
  --blue-accent-hover: #1A54E1;
  --blue-ice: #E8EEF7;
  
  --text-light: #F4F7FB;
  --text-light-secondary: #8E9EB5;
  --text-light-muted: #5A6E87;
  
  --border-dark: rgba(255, 255, 255, 0.12);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
}"""

root_replacement = """:root {
  --navy-deep: #07101E;
  --navy-surface: #0C1A30;
  --navy-card: #11233F;
  --navy-card-elevated: #162E52;
  --navy-card-border: rgba(255, 255, 255, 0.12);
  --navy-card-hover: #1A3560;
  
  /* Rich Multi-Tone Color Palette */
  --blue-accent: #2D7FF9;
  --blue-accent-hover: #1A54E1;
  --blue-light: #93C5FD;
  --blue-ice: #E0E7FF;
  
  --cyan-bright: #38BDF8;
  --cyan-light: #BAE6FD;
  --cyan-glow: rgba(56, 189, 248, 0.20);
  --cyan-bg: rgba(56, 189, 248, 0.12);
  
  --amber-warm: #F59E0B;
  --amber-light: #FDE68A;
  --amber-glow: rgba(245, 158, 11, 0.20);
  --amber-bg: rgba(245, 158, 11, 0.12);
  
  --emerald-vibrant: #10B981;
  --emerald-light: #A7F3D0;
  --emerald-glow: rgba(16, 185, 129, 0.20);
  --emerald-bg: rgba(16, 185, 129, 0.12);
  
  --purple-indigo: #818CF8;
  --purple-light: #E0E7FF;
  --purple-glow: rgba(129, 140, 248, 0.20);
  --purple-bg: rgba(129, 140, 248, 0.12);
  
  --rose-coral: #F43F5E;
  --rose-light: #FECDD3;
  --rose-glow: rgba(244, 63, 94, 0.20);
  --rose-bg: rgba(244, 63, 94, 0.12);
  
  --text-pure: #FFFFFF;
  --text-light: #F1F5F9;
  --text-light-secondary: #94A3B8;
  --text-light-muted: #64748B;
  
  --border-dark: rgba(255, 255, 255, 0.14);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-smooth: cubic-bezier(0.16, 1, 0.3, 1);
}

.card-dark {
  background: linear-gradient(145deg, rgba(18, 35, 66, 0.85) 0%, rgba(10, 20, 40, 0.95) 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
}

.card-clarita {
  background: linear-gradient(145deg, rgba(30, 56, 100, 0.70) 0%, rgba(16, 32, 62, 0.80) 100%) !important;
  border: 1px solid rgba(56, 189, 248, 0.30) !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}"""

code = code.replace(root_target, root_replacement, 1)

print('Root replaced:', root_target not in code)

with open(r'scripts_y_notas\generate_v9_color_deck.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Wrote initial generate_v9_color_deck.py')
