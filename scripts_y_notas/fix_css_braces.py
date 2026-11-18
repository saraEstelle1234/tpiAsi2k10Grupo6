with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's locate the PERFECT RESPONSIVE ENGINE section
start_marker = "/* ========================================================\n       PERFECT RESPONSIVE ENGINE (DESKTOP, TABLET, MOBILE)\n       ======================================================== */"
end_marker = "</style>"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

print(f"start_idx: {start_idx}, end_idx: {end_idx}")

# Notice that line 104 is out.write('''<!DOCTYPE html> ... ''')
# So in this block, curly braces MUST be SINGLE { and } !

clean_responsive_css = """/* ========================================================
       PERFECT RESPONSIVE ENGINE (DESKTOP, TABLET, MOBILE)
       ======================================================== */

    /* Global Overflow Protection & Fluid Setup */
    html, body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100% !important;
    }

    img {
      max-width: 100%;
      height: auto;
    }

    /* Table Horizontal Touch Scrolling */
    .tpi-table-container,
    .table-responsive-wrapper {
      width: 100% !important;
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
      border-radius: 12px !important;
    }

    /* ----------------------------------------------------
       LAPTOPS & MONITORS (1025px - 1440px)
       ---------------------------------------------------- */
    @media (max-width: 1440px) {
      main {
        padding: 20px 36px 110px 36px;
      }
      .giant-title {
        font-size: clamp(28px, 3.5vw, 48px);
      }
    }

    /* ----------------------------------------------------
       TABLETS & SMALL LAPTOPS (<= 1024px)
       ---------------------------------------------------- */
    @media (max-width: 1024px) {
      header {
        padding: 12px 24px;
      }
      main {
        padding: 16px 20px 120px 20px !important;
      }

      /* Stack Split Diagram Layouts vertically */
      [style*="grid-template-columns: 620px 1fr"],
      [style*="grid-template-columns: 1fr 280px"],
      [style*="grid-template-columns: 1.2fr 0.8fr"],
      [style*="grid-template-columns: 1.25fr 0.75fr"],
      [style*="grid-template-columns: 0.95fr 1.05fr"] {
        grid-template-columns: 1fr !important;
        gap: 20px !important;
      }

      /* Responsive Diagram Frame Heights */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {
        height: clamp(340px, 52vh, 560px) !important;
      }

      /* Slide 9 DCU center frame */
      #slide-9 [style*="grid-template-columns: 620px 1fr"] > div:first-child {
        max-width: 680px;
        margin: 0 auto;
        width: 100%;
      }
    }

    /* ----------------------------------------------------
       TABLETS PORTRAIT & LARGE MOBILES (<= 860px)
       ---------------------------------------------------- */
    @media (max-width: 860px) {
      /* Stack 2-column layouts */
      [style*="grid-template-columns: 1fr 1fr"],
      [style*="grid-template-columns: 1.15fr 0.85fr"] {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }

      /* Slide 7: RF Accordion 2 columns stack to 1 vertical column */
      #rf-accordion-list {
        flex-direction: column !important;
        max-height: 60vh !important;
      }
      .rf-col {
        width: 100% !important;
      }

      /* Slide 13: Trace matrix console stacks vertically */
      .trace-matrix-console {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
        min-height: auto !important;
        padding: 18px !important;
      }
      .trace-rf-list {
        max-height: 260px !important;
      }

      /* Header center label hide to prevent collision */
      .header-center {
        display: none !important;
      }

      /* Card padding optimization */
      .card-dark {
        padding: 18px 20px !important;
        border-radius: 16px !important;
      }

      /* Slide 1 Hero Header */
      #slide-1 .card-dark:first-child {
        padding: 24px 20px !important;
      }

      /* Team grids become 1 column on mobile / 2 on tablet */
      #slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }

      /* Slide 14 Split */
      #slide-14 [style*="grid-template-columns: 0.95fr 1.05fr"] {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }
      #slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 8px !important;
      }
    }

    /* ----------------------------------------------------
       SMARTPHONES (<= 640px)
       ---------------------------------------------------- */
    @media (max-width: 640px) {
      header {
        padding: 10px 14px !important;
      }
      .header-left {
        font-size: 11px !important;
        letter-spacing: 0.03em !important;
      }
      .header-left::before {
        width: 6px !important;
        height: 6px !important;
      }
      .header-counter-box {
        padding: 3px 8px !important;
        font-size: 11px !important;
      }

      /* Generous bottom padding so dock and touch handle never cover content */
      main {
        padding: 12px 12px 140px 12px !important;
      }

      .giant-title {
        font-size: clamp(22px, 6.2vw, 32px) !important;
        margin-bottom: 6px !important;
        line-height: 1.12 !important;
      }
      .editorial-subtitle {
        font-size: 13px !important;
        line-height: 1.45 !important;
        margin-bottom: 14px !important;
      }

      /* Slide 1 Hero Header Buttons Stack Vertically */
      #slide-1 .card-dark:first-child div[style*="display: flex; align-items: center; gap: 14px;"] {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 10px !important;
        width: 100% !important;
      }
      #slide-1 .btn-primary,
      #slide-1 .btn-secondary {
        width: 100% !important;
        justify-content: center !important;
        min-height: 46px !important;
        font-size: 13.5px !important;
      }

      /* Slide 1 9 Members: 1 clean column */
      #slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }
      #slide-1 [style*="grid-template-columns: repeat(3, 1fr)"] > .card-dark {
        padding: 14px 16px !important;
      }

      /* Slide 6: 3 correction cards stack */
      #slide-6 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      /* Slide 10: Metadata bar stacks into 2 columns or 1 column */
      #slide-10 [style*="grid-template-columns: repeat(5, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 8px !important;
      }

      /* Slide 13: Filters stack cleanly */
      #slide-13 div[style*="display: flex; gap: 14px; align-items: center; margin-bottom: 14px;"] {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 10px !important;
      }
      .trace-module-pills {
        flex-wrap: wrap !important;
        gap: 6px !important;
      }
      .trace-module-btn {
        padding: 6px 10px !important;
        font-size: 11.5px !important;
      }

      /* Slide 14: Institutional & Members stack */
      #slide-14 [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
        gap: 6px !important;
      }
      #slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 8px !important;
      }

      /* Slide 9 Preset buttons on mobile */
      .preset-focus-bar {
        gap: 4px !important;
        justify-content: center !important;
      }
      .preset-btn {
        padding: 4px 8px !important;
        font-size: 11px !important;
      }

      /* Compact Dock for Mobile */
      .mac-dock-container {
        height: 52px !important;
        bottom: 8px !important;
        padding: 0 8px !important;
        gap: 5px !important;
        max-width: calc(100vw - 16px) !important;
      }
      .dock-icon-btn {
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        border-radius: 9px !important;
      }
      .dock-icon-btn svg {
        width: 17px !important;
        height: 17px !important;
      }
      .dock-counter-badge {
        font-size: 11px !important;
        padding: 2px 6px !important;
      }
      .dock-divider-mac {
        height: 20px !important;
        margin: 0 1px !important;
      }
      .dock-tooltip {
        display: none !important;
      }

      /* Touch Handle Bar on Mobile */
      .dock-touch-handle {
        bottom: 6px !important;
        padding: 3px 14px !important;
      }

      /* Zoom Modal Toolbar Mobile */
      .zoom-modal-toolbar {
        top: 8px !important;
        max-width: calc(100vw - 16px) !important;
        padding: 4px 8px !important;
        gap: 4px !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
      }
      .zoom-btn {
        min-height: 30px !important;
        padding: 0 8px !important;
        font-size: 11px !important;
      }

      /* Overview modal cards on mobile */
      .overview-grid {
        grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)) !important;
        gap: 10px !important;
        padding: 12px !important;
      }

      /* Mobile Diagram Frame Heights */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {
        height: clamp(260px, 44vh, 400px) !important;
      }
    }

    /* ----------------------------------------------------
       SMALL MOBILE PHONES (<= 380px)
       ---------------------------------------------------- */
    @media (max-width: 380px) {
      .header-left span {
        display: none;
      }
      .mac-dock-container {
        gap: 3px !important;
        padding: 0 4px !important;
      }
      .dock-icon-btn {
        width: 30px !important;
        height: 30px !important;
        min-width: 30px !important;
      }
      .dock-icon-btn svg {
        width: 15px !important;
        height: 15px !important;
      }
    }
  """

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + clean_responsive_css + "\n" + text[end_idx:]
    with open('scripts_y_notas/generate_v8_deck.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced responsive CSS with valid single-brace syntax!")
else:
    print("Could not find start_idx or end_idx!")
