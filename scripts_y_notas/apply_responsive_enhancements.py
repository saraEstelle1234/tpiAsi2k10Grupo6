import os

# Read generate_v8_deck.py
with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .tpi-table-container to have smooth horizontal scrolling
old_tpi_table_css = """.tpi-table-container {
  width: 100%;
  border-radius: 12px;
  overflow: hidden;"""

new_tpi_table_css = """.tpi-table-container {
  width: 100%;
  border-radius: 12px;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;"""

if old_tpi_table_css in content:
    content = content.replace(old_tpi_table_css, new_tpi_table_css, 1)
    print("Updated .tpi-table-container with overflow-x: auto")
else:
    print("Warning: old_tpi_table_css not found")

# 2. Add complete responsive engine before </style>
# Note: Double braces {{ and }} for f-string compliance
responsive_css = """
    /* ========================================================
       PERFECT RESPONSIVE ENGINE (DESKTOP, TABLET, MOBILE)
       ======================================================== */

    /* Fluid Typography and Global Overflow Protection */
    html, body {{
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
    }}

    img {{
      max-width: 100%;
      height: auto;
    }}

    /* Large Desktops / Projectors (>= 1600px) */
    @media (min-width: 1600px) {{
      main {{
        max-width: 1560px;
        padding: 32px 56px 120px 56px;
      }}
    }}

    /* Laptops & Standard Monitors (1025px - 1440px) */
    @media (max-width: 1440px) {{
      main {{
        padding: 20px 36px 110px 36px;
      }}
      .giant-title {{
        font-size: clamp(28px, 3.5vw, 48px);
      }}
    }}

    /* Tablets & Small Laptops (<= 1024px) */
    @media (max-width: 1024px) {{
      header {{
        padding: 12px 24px;
      }}
      main {{
        padding: 16px 20px 105px 20px;
      }}

      /* Stack Split Diagram Layouts vertically */
      [style*="grid-template-columns: 620px 1fr"],
      [style*="grid-template-columns: 1fr 280px"],
      [style*="grid-template-columns: 1.2fr 0.8fr"],
      [style*="grid-template-columns: 1.25fr 0.75fr"],
      [style*="grid-template-columns: 0.95fr 1.05fr"] {{
        grid-template-columns: 1fr !important;
        gap: 20px !important;
      }}

      /* Responsive Diagram Frame Heights (no overflow, no clipping) */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {{
        height: clamp(340px, 52vh, 580px) !important;
      }}

      /* DCU column centering on tablet */
      #slide-9 [style*="grid-template-columns: 620px 1fr"] > div:first-child {{
        max-width: 680px;
        margin: 0 auto;
        width: 100%;
      }}
    }}

    /* Tablets Portrait & Large Mobiles (<= 860px) */
    @media (max-width: 860px) {{
      /* Stack 2-column layouts */
      [style*="grid-template-columns: 1fr 1fr"],
      [style*="grid-template-columns: 1.15fr 0.85fr"] {{
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }}

      /* Slide 7: RF Accordion 2 columns stack to 1 vertical column */
      #rf-accordion-list {{
        flex-direction: column !important;
        max-height: 62vh !important;
      }}
      .rf-col {{
        width: 100% !important;
      }}

      /* Slide 13: Trace matrix console stacks vertically */
      .trace-matrix-console {{
        grid-template-columns: 1fr !important;
        gap: 16px !important;
        min-height: auto !important;
        padding: 18px !important;
      }}
      .trace-rf-list {{
        max-height: 260px !important;
      }}

      /* Header center label hide to avoid collision */
      .header-center {{
        display: none !important;
      }}

      /* Card padding optimization */
      .card-dark {{
        padding: 18px 20px !important;
        border-radius: 16px !important;
      }}

      /* Slide 1 Hero Header */
      #slide-1 .card-dark:first-child {{
        padding: 24px 22px !important;
      }}

      /* Team grids become 2 columns */
      [style*="grid-template-columns: repeat(3, 1fr)"] {{
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
      }}

      /* Slide 14 Split */
      #slide-14 [style*="grid-template-columns: 0.95fr 1.05fr"] {{
        grid-template-columns: 1fr !important;
      }}
    }}

    /* Mobile Phones (<= 640px) */
    @media (max-width: 640px) {{
      header {{
        padding: 10px 14px;
      }}
      .header-left {{
        font-size: 12px;
      }}
      .header-counter-box {{
        padding: 4px 10px;
        font-size: 12px;
      }}

      main {{
        padding: 12px 12px 95px 12px;
      }}

      .giant-title {{
        font-size: clamp(24px, 6.5vw, 36px) !important;
        margin-bottom: 6px;
      }}
      .editorial-subtitle {{
        font-size: 13.5px !important;
        line-height: 1.45;
        margin-bottom: 14px !important;
      }}

      /* All remaining grids stack to 1 column */
      [style*="grid-template-columns: repeat(3, 1fr)"],
      [style*="grid-template-columns: repeat(2, 1fr)"],
      #slide-6 [style*="grid-template-columns: repeat(3, 1fr)"],
      #slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {{
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }}

      /* Slide 10 Metadata bar */
      #slide-10 [style*="grid-template-columns: repeat(5, 1fr)"] {{
        grid-template-columns: 1fr 1fr !important;
        gap: 10px !important;
      }}

      /* Slide 14 - Professors grid */
      #slide-14 [style*="grid-template-columns: 1fr 1fr"] {{
        grid-template-columns: 1fr !important;
        gap: 6px !important;
      }}

      /* Slide 9 Preset buttons on mobile */
      .preset-focus-bar {{
        gap: 4px !important;
      }}
      .preset-btn {{
        padding: 4px 8px !important;
        font-size: 11px !important;
      }}

      /* Buttons become mobile-friendly */
      .btn-primary, .btn-secondary {{
        min-height: 42px !important;
        padding: 0 16px !important;
        font-size: 13px !important;
      }}

      /* Compact Dock for Mobile */
      .mac-dock-container {{
        height: 52px !important;
        bottom: 8px !important;
        padding: 0 8px !important;
        gap: 6px !important;
        max-width: calc(100vw - 16px) !important;
      }}
      .dock-icon-btn {{
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        border-radius: 10px !important;
      }}
      .dock-icon-btn svg {{
        width: 17px !important;
        height: 17px !important;
      }}
      .dock-counter-badge {{
        font-size: 11px !important;
        padding: 2px 6px !important;
      }}
      .dock-divider-mac {{
        height: 20px !important;
        margin: 0 1px !important;
      }}
      .dock-tooltip {{
        display: none !important; /* Hide hover tooltips on mobile to avoid sticking */
      }}

      /* Zoom Modal Toolbar Mobile */
      .zoom-modal-toolbar {{
        top: 10px !important;
        max-width: calc(100vw - 20px) !important;
        padding: 5px 8px !important;
        gap: 4px !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
      }}
      .zoom-btn {{
        min-height: 32px !important;
        padding: 0 8px !important;
        font-size: 11px !important;
      }}

      /* Overview modal cards on mobile */
      .overview-grid {{
        grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)) !important;
        gap: 10px !important;
        padding: 14px !important;
      }}

      /* Mobile Diagram Frame Heights */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {{
        height: clamp(280px, 45vh, 420px) !important;
      }}
    }}

    /* Small Mobile Phones (<= 380px) */
    @media (max-width: 380px) {{
      .header-left span {{
        display: none;
      }}
      .mac-dock-container {{
        gap: 4px !important;
        padding: 0 4px !important;
      }}
      .dock-icon-btn {{
        width: 32px !important;
        height: 32px !important;
        min-width: 32px !important;
      }}
      #slide-10 [style*="grid-template-columns: repeat(5, 1fr)"] {{
        grid-template-columns: 1fr !important;
      }}
    }}
"""

style_idx = content.find('  </style>')
if style_idx != -1:
    content = content[:style_idx] + responsive_css + content[style_idx:]
    print("Injected responsive CSS rules before </style>")
else:
    print("Error: </style> tag not found")

# 3. Add Native Touch Swipe Navigation before </script>
touch_swipe_js = """
    // ========================================================
    // NATIVE TOUCH SWIPE NAVIGATION (TABLETS & SMARTPHONES)
    // ========================================================
    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;

    document.addEventListener('touchstart', e => {{
      if (e.touches && e.touches.length > 0) {{
        touchStartX = e.touches[0].screenX;
        touchStartY = e.touches[0].screenY;
      }}
    }}, {{ passive: true }});

    document.addEventListener('touchend', e => {{
      // Don't swipe slide if zoom modal or overview modal is open
      const zoomModal = document.getElementById('zoom-modal');
      const overviewModal = document.getElementById('overview-modal');
      if (zoomModal && zoomModal.classList.contains('active')) return;
      if (overviewModal && overviewModal.classList.contains('active')) return;

      if (e.changedTouches && e.changedTouches.length > 0) {{
        touchEndX = e.changedTouches[0].screenX;
        touchEndY = e.changedTouches[0].screenY;
        
        const diffX = touchEndX - touchStartX;
        const diffY = touchEndY - touchStartY;
        
        // Horizontal swipe threshold: > 45px and predominantly horizontal
        if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.5) {{
          if (diffX < 0) {{
            nextSlideAction();
          }} else {{
            prevSlideAction();
          }}
        }}
      }}
    }}, {{ passive: true }});
"""

script_idx = content.rfind('  </script>')
if script_idx != -1:
    content = content[:script_idx] + touch_swipe_js + content[script_idx:]
    print("Injected touch swipe JS before </script>")
else:
    print("Error: </script> tag not found")

with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_v8_deck.py successfully updated with full responsiveness!")
