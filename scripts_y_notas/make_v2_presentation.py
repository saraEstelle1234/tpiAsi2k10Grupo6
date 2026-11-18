# -*- coding: utf-8 -*-
"""
Enhanced V2 Deluxe Presentation Generator for TPI ASI 2K10 - Grupo 6.
Updates:
- Slide 7: Interactive Accordion Requerimientos Explorer (Clean text, expandable modules, search/filter, expand all)
- Slide 8: Expansive DCU layout (huge readable viewport + quadrant preset focus buttons + inline pan/wheel)
- Slide 12: Expansive DCD layout (huge readable viewport + quadrant preset focus buttons + inline pan/wheel)
"""
import os
import base64

def get_b64(path):
    if not os.path.exists(path):
        print(f"Warning: {path} not found!")
        return ""
    with open(path, "rb") as f:
        ext = path.split('.')[-1].lower()
        if ext == 'jpg': ext = 'jpeg'
        return f"data:image/{ext};base64," + base64.b64encode(f.read()).decode('ascii')

print("Encoding diagram assets...")
b64_mapa = get_b64("media_presentacion/page_3_img_0_16.png")
b64_bpmn_desc = get_b64("media_presentacion/page_7_img_0_26.png")
b64_bpmn_oper = get_b64("media_presentacion/page_8_img_0_29.png")
b64_dcu = get_b64("media_presentacion/page_9_img_0_32.png")
b64_proto = get_b64("media_presentacion/page_14_img_0_47.jpeg")
b64_dcd = get_b64("media_presentacion/page_15_img_0_50.png")
print("Assets encoded.")

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Museo Provincial de Historia Natural &bull; TPI ASI 2K10 (Grupo 6)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --navy-deep: #050b14;
      --navy-main: #0a1526;
      --navy-surface: #0f1f38;
      --navy-card: #132746;
      --navy-card-hover: #173056;
      --navy-border: rgba(203, 178, 106, 0.22);
      --navy-border-hover: rgba(203, 178, 106, 0.55);
      
      --gold-primary: #d4af37;
      --gold-light: #f3e5ab;
      --gold-muted: #c5a059;
      --gold-glow: rgba(212, 175, 55, 0.25);
      
      --cyan-marine: #38bdf8;
      --cyan-marine-dim: rgba(56, 189, 248, 0.15);
      --emerald-marine: #34d399;
      --rose-marine: #fb7185;
      
      --text-ivory: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --font-display: 'Cinzel', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background: radial-gradient(circle at 50% -20%, #152b4d 0%, #0a1526 50%, #050b14 100%);
      color: var(--text-ivory);
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      flex-direction: column;
      user-select: none;
    }}

    /* Top Archival Header */
    header {{
      height: 68px;
      padding: 0 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--navy-border);
      background: rgba(10, 21, 38, 0.94);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 60;
    }}

    .header-brand {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .museum-logo-svg {{
      width: 32px;
      height: 32px;
      fill: var(--gold-primary);
      filter: drop-shadow(0 0 8px rgba(212, 175, 55, 0.4));
    }}

    .header-titles {{
      display: flex;
      flex-direction: column;
    }}

    .header-title-main {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: var(--gold-light);
      text-transform: uppercase;
    }}

    .header-title-sub {{
      font-size: 11px;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      text-transform: uppercase;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .badge-gold {{
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.35);
      color: var(--gold-light);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      padding: 5px 12px;
      border-radius: 4px;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .btn-header {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-ivory);
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .btn-header:hover {{
      background: rgba(212, 175, 55, 0.15);
      border-color: var(--gold-primary);
      color: var(--gold-light);
    }}

    /* Progress Line */
    .progress-bar-container {{
      width: 100%;
      height: 3px;
      background: rgba(255, 255, 255, 0.03);
      position: sticky;
      top: 68px;
      z-index: 59;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--gold-muted), var(--gold-primary), var(--cyan-marine));
      width: 6.66%;
      transition: width 0.35s ease;
      box-shadow: 0 0 10px rgba(212, 175, 55, 0.5);
    }}

    /* Main Stage */
    main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px 32px;
      max-width: 1540px;
      margin: 0 auto;
      width: 100%;
    }}

    .slide {{
      display: none;
      width: 100%;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.35s ease, transform 0.35s ease;
    }}
    .slide.active {{
      display: block;
      opacity: 1;
      transform: translateY(0);
    }}

    /* Museum Frame Cards */
    .museum-card {{
      background: var(--navy-card);
      border: 1px solid var(--navy-border);
      border-radius: 14px;
      padding: 24px 28px;
      box-shadow: 0 18px 40px -15px rgba(0, 0, 0, 0.65);
      position: relative;
    }}

    .museum-card.gold-edge {{
      border-top: 3px solid var(--gold-primary);
    }}

    .museum-card .corner-tl,
    .museum-card .corner-tr,
    .museum-card .corner-bl,
    .museum-card .corner-br {{
      position: absolute;
      width: 8px;
      height: 8px;
      pointer-events: none;
      border-color: var(--gold-muted);
    }}
    .museum-card .corner-tl {{ top: 6px; left: 6px; border-top: 1.5px solid; border-left: 1.5px solid; }}
    .museum-card .corner-tr {{ top: 6px; right: 6px; border-top: 1.5px solid; border-right: 1.5px solid; }}
    .museum-card .corner-bl {{ bottom: 6px; left: 6px; border-bottom: 1.5px solid; border-left: 1.5px solid; }}
    .museum-card .corner-br {{ bottom: 6px; right: 6px; border-bottom: 1.5px solid; border-right: 1.5px solid; }}

    /* Typography */
    .chapter-tag {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--gold-primary);
      margin-bottom: 6px;
    }}

    .slide-title {{
      font-family: var(--font-display);
      font-size: 30px;
      font-weight: 800;
      letter-spacing: 0.02em;
      line-height: 1.2;
      color: var(--text-ivory);
      margin-bottom: 4px;
    }}

    .slide-subtitle {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 18px;
    }}

    /* Grid Layouts */
    .grid-2 {{
      display: grid;
      grid-template-columns: 1.12fr 0.88fr;
      gap: 22px;
      align-items: stretch;
    }}
    .grid-2-even {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      align-items: stretch;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}

    /* Gallery Artwork Viewer Containers */
    .gallery-frame {{
      background: #081322;
      border: 1px solid rgba(203, 178, 106, 0.25);
      border-radius: 12px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      padding: 10px;
    }}
    .gallery-frame:hover {{
      border-color: var(--gold-primary);
      box-shadow: 0 10px 30px rgba(212, 175, 55, 0.2);
    }}
    .gallery-frame img {{
      width: 100%;
      height: 100%;
      max-height: 460px;
      object-fit: contain;
      display: block;
      border-radius: 6px;
      transition: transform 0.3s ease;
    }}

    .gallery-frame-badge {{
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(10, 21, 38, 0.9);
      border: 1px solid var(--gold-muted);
      color: var(--gold-light);
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
      pointer-events: none;
      backdrop-filter: blur(8px);
    }}

    /* ====================================================== */
    /* EXPANSIVE DIAGRAM VIEWPORT (FOR DCU & DCD)             */
    /* ====================================================== */
    .expansive-diagram-layout {{
      display: grid;
      grid-template-columns: 1.35fr 0.65fr;
      gap: 20px;
      align-items: stretch;
    }}

    .expansive-viewport-card {{
      background: #081322;
      border: 1px solid rgba(203, 178, 106, 0.3);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    .expansive-toolbar {{
      height: 48px;
      padding: 0 16px;
      background: rgba(10, 21, 38, 0.95);
      border-bottom: 1px solid var(--navy-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .preset-pill-group {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .preset-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .preset-btn:hover, .preset-btn.active {{
      background: rgba(212, 175, 55, 0.2);
      border-color: var(--gold-primary);
      color: var(--gold-light);
    }}

    .expansive-canvas {{
      flex: 1;
      height: 560px;
      overflow: hidden;
      position: relative;
      cursor: grab;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #0e1e36 0%, #060d18 100%);
    }}
    .expansive-canvas.dragging {{
      cursor: grabbing;
    }}
    .expansive-canvas img {{
      max-width: 95%;
      max-height: 95%;
      object-fit: contain;
      border-radius: 6px;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.7);
      user-select: none;
      pointer-events: none;
    }}

    /* Museum Spec Blocks */
    .arch-block {{
      background: rgba(15, 31, 56, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-left: 3px solid var(--gold-muted);
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 12px;
      transition: all 0.2s ease;
    }}
    .arch-block:hover {{
      background: rgba(23, 48, 86, 0.7);
      border-left-color: var(--gold-primary);
    }}
    .arch-block-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .arch-block-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Golden Rule Plaques */
    .plaque-gold {{
      background: linear-gradient(135deg, rgba(212, 175, 55, 0.12), rgba(10, 21, 38, 0.85));
      border: 1px solid var(--gold-muted);
      border-radius: 10px;
      padding: 16px 20px;
      margin-bottom: 14px;
      position: relative;
    }}
    .plaque-gold-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}
    .plaque-gold-title {{
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 700;
      color: var(--gold-light);
      letter-spacing: 0.06em;
      text-transform: uppercase;
    }}

    /* Roster Cards (Slide 1) */
    .roster-card-v2 {{
      background: rgba(15, 31, 56, 0.75);
      border: 1px solid rgba(203, 178, 106, 0.18);
      border-radius: 10px;
      padding: 16px 18px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.25s ease;
      position: relative;
    }}
    .roster-card-v2:hover {{
      border-color: var(--gold-primary);
      background: rgba(23, 48, 86, 0.85);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }}
    .roster-card-v2 .badge-num {{
      font-family: var(--font-display);
      font-size: 11px;
      color: var(--gold-muted);
      font-weight: 700;
    }}
    .roster-card-v2 .name {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-ivory);
    }}
    .roster-card-v2 .legajo {{
      font-size: 12px;
      color: var(--cyan-marine);
      font-family: monospace;
      font-weight: 600;
    }}
    .roster-card-v2 .role {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.35;
      margin-top: 4px;
    }}

    /* ====================================================== */
    /* ACCORDION REQUERIMIENTOS EXPLORER (SLIDE 7)            */
    /* ====================================================== */
    .req-explorer-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .req-search-box {{
      background: rgba(10, 21, 38, 0.85);
      border: 1px solid var(--navy-border);
      border-radius: 6px;
      padding: 6px 12px;
      color: var(--text-ivory);
      font-size: 12px;
      width: 240px;
      outline: none;
    }}
    .req-search-box:focus {{
      border-color: var(--gold-primary);
    }}

    .req-accordion-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      max-height: 520px;
      overflow-y: auto;
      padding-right: 6px;
    }}
    .req-accordion-grid::-webkit-scrollbar {{
      width: 5px;
    }}
    .req-accordion-grid::-webkit-scrollbar-thumb {{
      background: var(--navy-border);
      border-radius: 4px;
    }}

    .req-card {{
      background: rgba(15, 31, 56, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.2s ease;
    }}
    .req-card:hover {{
      border-color: rgba(203, 178, 106, 0.35);
    }}
    .req-card.gold-focus {{
      border-left: 3px solid var(--gold-primary);
    }}

    .req-card-header {{
      padding: 12px 16px;
      background: rgba(10, 21, 38, 0.8);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: background 0.2s ease;
    }}
    .req-card-header:hover {{
      background: rgba(23, 48, 86, 0.85);
    }}
    .req-card-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--gold-light);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .req-card-arrow {{
      font-size: 11px;
      color: var(--gold-muted);
      transition: transform 0.25s ease;
    }}
    .req-card.open .req-card-arrow {{
      transform: rotate(180deg);
    }}

    .req-card-body {{
      display: none;
      padding: 12px 16px;
      background: rgba(8, 19, 34, 0.95);
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      flex-direction: column;
      gap: 6px;
    }}
    .req-card.open .req-card-body {{
      display: flex;
    }}

    .req-item-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12.5px;
      color: var(--text-ivory);
      padding: 4px 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.03);
    }}
    .req-code-badge {{
      font-family: monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--cyan-marine);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 2px 6px;
      border-radius: 4px;
      min-width: 48px;
      text-align: center;
    }}

    /* Bottom Control Bar */
    footer {{
      height: 74px;
      padding: 0 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--navy-border);
      background: rgba(10, 21, 38, 0.95);
      backdrop-filter: blur(16px);
      position: sticky;
      bottom: 0;
      z-index: 60;
    }}

    .nav-btn-v2 {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--navy-border);
      color: var(--text-ivory);
      padding: 9px 20px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .nav-btn-v2:hover:not(:disabled) {{
      background: rgba(212, 175, 55, 0.18);
      border-color: var(--gold-primary);
      color: var(--gold-light);
      transform: translateY(-1px);
    }}
    .nav-btn-v2:disabled {{
      opacity: 0.3;
      cursor: not-allowed;
    }}

    .dots-strip {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .dot-v2 {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.18);
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .dot-v2.active {{
      background: var(--gold-primary);
      box-shadow: 0 0 10px var(--gold-primary);
      width: 20px;
      border-radius: 4px;
    }}
    .dot-v2:hover:not(.active) {{
      background: rgba(212, 175, 55, 0.6);
    }}

    .counter-label {{
      font-family: var(--font-display);
      font-size: 12px;
      letter-spacing: 0.06em;
      color: var(--gold-light);
    }}

    /* Pan & Zoom Modal */
    .zoom-modal {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(5, 11, 20, 0.96);
      backdrop-filter: blur(20px);
      z-index: 9999;
      display: none;
      flex-direction: column;
      opacity: 0;
      transition: opacity 0.25s ease;
    }}
    .zoom-modal.active {{
      display: flex;
      opacity: 1;
    }}

    .modal-bar {{
      height: 64px;
      padding: 0 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(10, 21, 38, 0.95);
      border-bottom: 1px solid var(--navy-border);
    }}
    .modal-title-text {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: var(--gold-light);
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .modal-tools {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .tool-btn-v2 {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: var(--text-ivory);
      width: 36px;
      height: 36px;
      border-radius: 6px;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tool-btn-v2:hover {{
      background: var(--gold-primary);
      color: #000;
      border-color: var(--gold-primary);
    }}
    .zoom-scale-text {{
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-light);
      min-width: 55px;
      text-align: center;
      font-family: monospace;
    }}

    .modal-viewport {{
      flex: 1;
      width: 100%;
      height: calc(100vh - 64px);
      overflow: hidden;
      position: relative;
      cursor: grab;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #0e1e36 0%, #050b14 100%);
    }}
    .modal-viewport.dragging {{
      cursor: grabbing;
    }}
    .zoomable-content {{
      position: absolute;
      transform-origin: center center;
      transition: transform 0.05s linear;
      will-change: transform;
      user-select: none;
    }}
    .zoomable-content img {{
      max-width: 90vw;
      max-height: 85vh;
      object-fit: contain;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85);
      border-radius: 6px;
      display: block;
      pointer-events: none;
      border: 1px solid rgba(203, 178, 106, 0.3);
    }}

    .modal-hint-pill {{
      position: absolute;
      bottom: 22px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(10, 21, 38, 0.88);
      border: 1px solid var(--navy-border);
      padding: 6px 18px;
      border-radius: 20px;
      font-size: 12px;
      color: var(--text-muted);
      pointer-events: none;
      backdrop-filter: blur(10px);
    }}

    /* Step Explorer & Traceability Styles */
    .step-explorer {{
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 20px;
      align-items: stretch;
    }}
    .steps-list-container {{
      max-height: 480px;
      overflow-y: auto;
      padding-right: 8px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .steps-list-container::-webkit-scrollbar {{
      width: 5px;
    }}
    .steps-list-container::-webkit-scrollbar-thumb {{
      background: var(--navy-border);
      border-radius: 4px;
    }}
    .step-item-card {{
      background: rgba(15, 31, 56, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 8px;
      padding: 10px 14px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.2s ease;
    }}
    .step-item-card:hover {{
      background: rgba(23, 48, 86, 0.7);
      border-color: rgba(203, 178, 106, 0.3);
    }}
    .step-item-card.active {{
      background: rgba(212, 175, 55, 0.15);
      border-color: var(--gold-primary);
      box-shadow: 0 0 12px rgba(212, 175, 55, 0.2);
    }}
    .step-badge-num {{
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      color: var(--gold-primary);
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid rgba(212, 175, 55, 0.3);
      padding: 3px 8px;
      border-radius: 4px;
      min-width: 30px;
      text-align: center;
    }}
    .step-summary-text {{
      font-size: 12.5px;
      color: var(--text-ivory);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
    }}

    .step-detail-viewer {{
      background: #081322;
      border: 1px solid var(--navy-border);
      border-radius: 12px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .step-detail-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
    }}
    .step-detail-title {{
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      color: var(--gold-light);
    }}
    .step-actor-tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 4px;
    }}
    .actor-guardia {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.35); }}
    .actor-sistema {{ background: rgba(212, 175, 55, 0.15); color: var(--gold-light); border: 1px solid rgba(212, 175, 55, 0.35); }}
    .step-action-box {{
      font-size: 14px;
      color: var(--text-ivory);
      line-height: 1.55;
      margin-bottom: 16px;
    }}
    .step-data-payload {{
      background: rgba(10, 21, 38, 0.95);
      border: 1px solid rgba(203, 178, 106, 0.3);
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 16px;
    }}
    .step-data-payload-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--gold-muted);
      margin-bottom: 6px;
    }}

    /* Traceability Console */
    .trace-console {{
      display: grid;
      grid-template-columns: 0.95fr 1.05fr;
      gap: 22px;
      align-items: stretch;
    }}
    .trace-filters {{
      display: flex;
      gap: 8px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}
    .trace-filter-pill {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .trace-filter-pill:hover,
    .trace-filter-pill.active {{
      background: rgba(212, 175, 55, 0.18);
      border-color: var(--gold-primary);
      color: var(--gold-light);
    }}
    .trace-rf-list {{
      max-height: 420px;
      overflow-y: auto;
      padding-right: 6px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .trace-rf-list::-webkit-scrollbar {{
      width: 5px;
    }}
    .trace-rf-list::-webkit-scrollbar-thumb {{
      background: var(--navy-border);
      border-radius: 4px;
    }}
    .trace-rf-item {{
      background: rgba(15, 31, 56, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 8px;
      padding: 10px 14px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .trace-rf-item:hover {{
      background: rgba(23, 48, 86, 0.7);
      border-color: rgba(203, 178, 106, 0.3);
    }}
    .trace-rf-item.active {{
      background: rgba(212, 175, 55, 0.15);
      border-color: var(--gold-primary);
    }}
    .trace-rf-code {{
      font-family: monospace;
      font-size: 11.5px;
      font-weight: 700;
      color: var(--gold-light);
    }}
    .trace-rf-name {{
      font-size: 12.5px;
      color: var(--text-ivory);
      flex: 1;
      margin-left: 10px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .trace-impact-dossier {{
      background: #081322;
      border: 1px solid var(--navy-border);
      border-radius: 12px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .trace-impact-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 10px;
    }}
    .trace-pill-group {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 4px;
    }}
    .pill-cu {{
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #38bdf8;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}
    .pill-class {{
      background: rgba(192, 132, 252, 0.15);
      border: 1px solid rgba(192, 132, 252, 0.35);
      color: #c084fc;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      font-family: monospace;
    }}
    .pill-rule {{
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid rgba(212, 175, 55, 0.35);
      color: var(--gold-light);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
    }}
  </style>
</head>
<body>

  <!-- Top Archival Header -->
  <header>
    <div class="header-brand">
      <svg class="museum-logo-svg" viewBox="0 0 24 24">
        <path d="M12 2L2 7V9H22V7L12 2ZM4 11V18H6V11H4ZM8 11V18H10V11H8ZM12 11V18H14V11H12ZM16 11V18H18V11H16ZM20 11V18H22V11H20ZM2 20V22H22V20H2Z"/>
      </svg>
      <div class="header-titles">
        <span class="header-title-main">Museo Provincial de Historia Natural</span>
        <span class="header-title-sub">Cátedra ASI &bull; Curso 2K10 &bull; Grupo 6 &bull; Ciclo 2026</span>
      </div>
    </div>
    <div class="header-actions">
      <span class="badge-gold" id="slide-topic-badge">1.1 Introducción</span>
      <button class="btn-header" onclick="toggleFullscreen()" title="Pantalla Completa (F11)">
        <span>⛶</span> Pantalla Completa
      </button>
    </div>
  </header>

  <!-- Progress Line -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="progress-bar"></div>
  </div>

  <!-- Main Stage -->
  <main>

    <!-- SLIDE 1: PORTADA & EQUIPO -->
    <div class="slide active" id="slide-1" data-topic="Catálogo & Roster">
      <div class="museum-card gold-edge" style="margin-bottom: 20px;">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
          <div>
            <span class="chapter-tag">
              <svg style="width: 13px; height: 13px; fill: currentColor;" viewBox="0 0 24 24"><path d="M12 2L2 7V9H22V7L12 2Z"/></svg>
              Trabajo Práctico Integrador &bull; Análisis de Sistemas de Información
            </span>
            <h1 class="slide-title">Sistema de Gestión, Vigilancia y Preservación Museológica</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">
              Modelo de Dominio, Procesos BPMN, Casos de Uso y Clases para la conservación patrimonial.
            </p>
          </div>
          <div style="text-align: right;">
            <span class="badge-gold">UTN - FRC</span>
            <div style="font-size: 12px; color: var(--text-muted); margin-top: 6px;">Evaluación Grupal Oral</div>
          </div>
        </div>

        <div style="display: flex; gap: 8px; margin-top: 14px; flex-wrap: wrap;">
          <span class="badge-gold">45 Requerimientos Funcionales</span>
          <span class="badge-gold">42 CUs Dominio + 3 Sesión</span>
          <span class="badge-gold">BPMN Nivel 1 & 2</span>
          <span class="badge-gold">CU-15 Registrar Incidente</span>
          <span class="badge-gold">Diagrama de Clases del Dominio</span>
        </div>
      </div>

      <div class="grid-3">
        <div class="roster-card-v2">
          <div class="badge-num">I &bull; Contexto</div>
          <div class="name">Abad, Francisco</div>
          <div class="legajo">Legajo: 423269</div>
          <div class="role">Dominio bajo estudio y Objetivos estratégicos del Negocio</div>
        </div>
        <div class="roster-card-v2">
          <div class="badge-num">II &bull; Vista Externa</div>
          <div class="name">Cufre, Agustín</div>
          <div class="legajo">Legajo: 419166</div>
          <div class="role">Mapa de Procesos de Negocio y Clasificación de Procesos</div>
        </div>
        <div class="roster-card-v2">
          <div class="badge-num">III &bull; Reglas</div>
          <div class="name">Marcuzzi, Tomas</div>
          <div class="legajo">Legajo: 403382</div>
          <div class="role">Ficha Técnica del Proceso Crítico y Reglas de Negocio (RN1 / RN2)</div>
        </div>
        <div class="roster-card-v2">
          <div class="badge-num">IV &bull; Procesos</div>
          <div class="name">Jastrzebski, Emiliano</div>
          <div class="legajo">Legajo: 402760</div>
          <div class="role">Modelado de Procesos BPMN: Nivel Descriptivo y Operativo</div>
        </div>
        <div class="roster-card-v2">
          <div class="badge-num">V &bull; Requerimientos</div>
          <div class="name">Molina, Tobias</div>
          <div class="legajo">Legajo: 419749</div>
          <div class="role">Especificación de Requerimientos y Trazabilidad N a M</div>
        </div>
        <div class="roster-card-v2" style="border-color: var(--gold-primary);">
          <div class="badge-num">VI &bull; Casos de Uso</div>
          <div class="name">Thomas Rapp, Francisco</div>
          <div class="legajo">Legajo: 408990</div>
          <div class="role">Vista Externa: Diagrama de Casos de Uso del Sistema (DCU)</div>
        </div>
        <div class="roster-card-v2" style="border-color: var(--cyan-marine);">
          <div class="badge-num">VII &bull; Plantilla CU</div>
          <div class="name">Moyano, Lucas Uriel</div>
          <div class="legajo">Legajo: 410975</div>
          <div class="role">Caso de Uso Esencial: Plantilla Interactiva CU-15 Registrar Incidente</div>
        </div>
        <div class="roster-card-v2" style="border-color: var(--gold-primary);">
          <div class="badge-num">VIII &bull; Dominio OO</div>
          <div class="name">Tarditti, Juan Sebastián</div>
          <div class="legajo">Legajo: 400212</div>
          <div class="role">Vista Interna: Diagrama de Clases del Dominio y Multiplicidades</div>
        </div>
        <div class="roster-card-v2" style="border-color: var(--cyan-marine);">
          <div class="badge-num">IX &bull; Consistencia</div>
          <div class="name">Pereyra, Kevin</div>
          <div class="legajo">Legajo: 418201</div>
          <div class="role">Prototipo de Interfaz Web Tablet y Matriz de Trazabilidad N a M</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide" id="slide-2" data-topic="Dominio & Negocio">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <span class="chapter-tag">Capítulo 1 &bull; Contexto Institucional</span>
        <h1 class="slide-title">Dominio bajo Estudio y Objetivos del Negocio</h1>
        <p class="slide-subtitle">Museo Provincial de Historia Natural: Custodia patrimonial, exhibición cultural y gestión de rondas.</p>

        <div class="grid-2">
          <div>
            <div class="arch-block">
              <div class="arch-block-title">Problemática Detectada en el Negocio</div>
              <div class="arch-block-desc">
                El museo alberga colecciones históricas y biológicas insustituibles. La operatoria manual previa provocaba demoras críticas en la comunicación de incidentes de deterioro o caídas, falta de trazabilidad en las restauraciones y desajustes en las rondas de guardia.
              </div>
            </div>

            <div class="arch-block">
              <div class="arch-block-title">Misión y Propósito Organizacional</div>
              <div class="arch-block-desc">
                Resguardar el patrimonio museológico mediante un estricto control de exhibición y rondas de seguridad activa, garantizando al mismo tiempo una experiencia de divulgación ágil para los visitantes.
              </div>
            </div>
          </div>

          <div>
            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Objetivo Estratégico 1</span>
                <span class="badge-gold">Tiempo Real</span>
              </div>
              <div class="arch-block-desc">
                Estandarizar y digitalizar el reporte de incidentes en sala en el momento exacto del hallazgo mediante tablets portátiles de ronda.
              </div>
            </div>

            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Objetivo Estratégico 2</span>
                <span class="badge-gold">Trazabilidad</span>
              </div>
              <div class="arch-block-desc">
                Asegurar la cadena de custodia de piezas dañadas, obligando al reingreso a depósito previo a cualquier nueva disposición o baja.
              </div>
            </div>

            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Objetivo Estratégico 3</span>
                <span class="badge-gold">Operatividad</span>
              </div>
              <div class="arch-block-desc">
                Coordinar eficazmente las agendas de guías de visitas y emitir informes diarios consolidados de vigilancia para supervisión.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: MAPA DE PROCESOS -->
    <div class="slide" id="slide-3" data-topic="2.2 Mapa de Procesos">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="chapter-tag">Capítulo 2.1 y 2.2 &bull; Vista Externa Organizacional</span>
            <h1 class="slide-title">Mapa de Procesos de Negocio</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Clasificación de procesos: Estratégicos, Esenciales/Clave y de Soporte.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')">
            <span>🔍</span> Inspeccionar con Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="gallery-frame" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')">
            <img src="{b64_mapa}" alt="Mapa de Procesos">
            <div class="gallery-frame-badge"><span>🔍</span> Pan & Zoom</div>
          </div>

          <div style="display: flex; flex-direction: column; justify-content: space-between;">
            <div class="arch-block">
              <div class="arch-block-title">Procesos Estratégicos</div>
              <div class="arch-block-desc">
                Planificación institucional, adquisición de nuevas colecciones, relaciones científicas y gestión de exposiciones temporales.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--cyan-marine);">
              <div class="arch-block-title" style="color: var(--cyan-marine);">Procesos Clave / Esenciales</div>
              <div class="arch-block-desc">
                &bull; <strong>Exposición de Obras de Arte:</strong> Interacción con visitantes y divulgación cultural.<br>
                &bull; <strong>Gestión y Realización de Visitas Guiadas:</strong> Atención a grupos educativos y público general.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--gold-primary);">
              <div class="arch-block-title" style="color: var(--gold-light);">Proceso de Soporte Crítico Seleccionado</div>
              <div class="arch-block-desc">
                <strong>Realizar Ronda de Vigilancia y Gestión de Incidentes:</strong> Custodia activa en salas, verificación de condiciones de las obras y reporte inmediato de siniestros.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: FICHA TÉCNICA DEL PROCESO & REGLAS -->
    <div class="slide" id="slide-4" data-topic="2.3 Proceso Crítico">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <span class="chapter-tag">Capítulo 2.3 &bull; Ficha Técnica & Reglas de Negocio</span>
        <h1 class="slide-title">Descripción del Proceso Crítico: Vigilancia e Incidentes</h1>
        <p class="slide-subtitle">Ficha técnica estructurada, formularios intervinientes y reglas de negocio determinantes.</p>

        <div class="grid-2-even">
          <div>
            <div class="arch-block">
              <div class="arch-block-title">Formularios y Documentos del Proceso</div>
              <div class="arch-block-desc">
                &bull; <strong>Planificación de Ronda:</strong> Hoja de ruta asignada al guardia por sala y turno.<br>
                &bull; <strong>Registro de Incidente:</strong> Acta electrónica de tipificación de anomalía, pieza y hora.<br>
                &bull; <strong>Informe Diario de Vigilancia:</strong> Resumen consolidado emitido al cierre de guardia.
              </div>
            </div>

            <div class="arch-block">
              <div class="arch-block-title">Listado de Actividades Formales</div>
              <div class="arch-block-desc">
                1. Consultar planificación de rondas de vigilancia.<br>
                2. Inspección física de sala: bifurcación en compuerta.<br>
                3. Registro de sala con 'Observación pendiente' (camino del incidente).<br>
                4. Registro de sala con 'Sin novedades' (camino normal).<br>
                5. Generación de informe con salas recorridas y cierre.
              </div>
            </div>
          </div>

          <div>
            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Regla de Negocio 1 &bull; RN1</span>
                <span class="badge-gold">Mandatoria</span>
              </div>
              <div style="font-size: 13.5px; color: var(--gold-light); font-weight: 700; margin-bottom: 6px;">
                Reingreso Obligatorio a Depósito
              </div>
              <div class="arch-block-desc">
                Toda obra enviada a restauración, se haya podido reparar con éxito o no, debe ingresar obligatoriamente al depósito del museo antes de definir su destino final o su baja formal. Ninguna pieza retorna directamente a sala de exhibición.
              </div>
            </div>

            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Regla de Negocio 2 &bull; RN2</span>
                <span class="badge-gold">Inmediatez</span>
              </div>
              <div style="font-size: 13.5px; color: var(--gold-light); font-weight: 700; margin-bottom: 6px;">
                Registro Inmediato de Incidente
              </div>
              <div class="arch-block-desc">
                El guardia debe registrar el incidente de la obra de forma inmediata ante el hallazgo en la sala, indicando obligatoriamente los datos exactos del siniestro, la pieza involucrada y la hora actual del servidor.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="2.5 BPMN Descriptivo">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div>
            <span class="chapter-tag">Capítulo 2.5 &bull; Vista Interna Macro &bull; Nivel 1</span>
            <h1 class="slide-title">BPMN a Nivel Descriptivo</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Flujo macro del proceso de vigilancia, carriles de responsabilidad y visión gerencial.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')">
            <span>🔍</span> Inspeccionar con Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="gallery-frame" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')">
            <img src="{b64_bpmn_desc}" alt="BPMN Descriptivo">
            <div class="gallery-frame-badge"><span>🔍</span> Pan & Zoom</div>
          </div>

          <div style="display: flex; flex-direction: column; justify-content: space-between;">
            <div class="arch-block">
              <div class="arch-block-title">Objetivo del Nivel Descriptivo</div>
              <div class="arch-block-desc">
                Brindar una perspectiva de negocio de alto nivel comprensible para la dirección del museo, estableciendo el inicio de la jornada, la verificación de salas y la emisión final del informe diario.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--cyan-marine);">
              <div class="arch-block-title" style="color: var(--cyan-marine);">Carriles de Responsabilidad (Lanes)</div>
              <div class="arch-block-desc">
                &bull; <strong>Encargado de Vigilancia:</strong> Ejecuta la inspección de salas asignadas.<br>
                &bull; <strong>Sistema Central:</strong> Valida estados, persigue registros y emite informes.<br>
                &bull; <strong>Supervisor:</strong> Recibe el reporte diario y audita novedades.
              </div>
            </div>

            <div class="arch-block">
              <div class="arch-block-title">Punto de Integración con el Nivel 2</div>
              <div class="arch-block-desc">
                La tarea central de revisión de sala se expande detalladamente en el nivel operativo mediante compuertas condicionales.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide" id="slide-6" data-topic="2.6 BPMN Operativo">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div>
            <span class="chapter-tag">Capítulo 2.6 &bull; Vista Interna Detallada &bull; Nivel 2</span>
            <h1 class="slide-title">BPMN a Nivel Operativo: Bifurcación en Sala</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Lógica de control, compuerta exclusiva (XOR) y disparo del subproceso de incidentes.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')">
            <span>🔍</span> Inspeccionar con Pan & Zoom
          </button>
        </div>

        <div class="gallery-frame" style="margin-bottom: 14px; max-height: 280px; padding: 6px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')">
          <img src="{b64_bpmn_oper}" style="max-height: 260px; width: 100%; object-fit: contain;" alt="BPMN Operativo">
          <div class="gallery-frame-badge"><span>🔍</span> Pan & Zoom Panorámico</div>
        </div>

        <div class="grid-2-even">
          <div class="arch-block" style="border-left-color: var(--emerald-marine);">
            <div class="arch-block-title" style="color: var(--emerald-marine);">Camino Normal (Sin Novedades)</div>
            <div class="arch-block-desc">
              Si el guardia no constata anomalías en las piezas ni en las condiciones de la sala, registra el estado 'Sin novedades'. El sistema actualiza el registro de recorrido y habilita la inspección de la siguiente sala asignada en la planificación.
            </div>
          </div>

          <div class="arch-block" style="border-left-color: var(--rose-marine);">
            <div class="arch-block-title" style="color: var(--rose-marine);">Camino Alternativo (Anomalía Detectada)</div>
            <div class="arch-block-desc">
              Ante deterioro o caída, la sala pasa a 'Observación pendiente', disparando en forma inmediata la invocación del subproceso / caso de uso <strong>CU-15 Registrar incidente</strong> con identificación de la pieza, tipificación del daño y sellado de tiempo.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ====================================================== -->
    <!-- SLIDE 7: REQUERIMIENTOS INTERACTIVOS (DESPLEGABLES)    -->
    <!-- ====================================================== -->
    <div class="slide" id="slide-7" data-topic="2.4 Requerimientos">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div class="req-explorer-header">
          <div>
            <span class="chapter-tag">Capítulo 2.4 &bull; Catálogo Interactivo &bull; Tobias Molina</span>
            <h1 class="slide-title">Especificación de Requerimientos del Sistema</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">45 Requerimientos Funcionales clasificados por módulo y 2 No Funcionales. Haz click en cada módulo para desplegar.</p>
          </div>
          <div style="display: flex; gap: 8px; align-items: center;">
            <input type="text" class="req-search-box" id="req-search" placeholder="🔍 Filtrar requerimiento..." oninput="searchReqs()">
            <button class="btn-header" onclick="toggleAllReqs(true)">Expandir Todos</button>
            <button class="btn-header" onclick="toggleAllReqs(false)">Colapsar</button>
          </div>
        </div>

        <div class="req-accordion-grid" id="req-accordion-container">
          <!-- Module 1: Obras -->
          <div class="req-card" id="req-card-1">
            <div class="req-card-header" onclick="toggleReqCard('req-card-1')">
              <span class="req-card-title">🖼️ Administrar Obras de Arte & Tipología</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">9 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-01</span><span>Registrar ingreso de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-02</span><span>Consultar obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-03</span><span>Registrar baja de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-04</span><span>Registrar tipo de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-05</span><span>Consultar tipo de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-06</span><span>Registrar baja de tipo de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-07</span><span>Registrar tipo de material</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-08</span><span>Consultar tipo de material</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-09</span><span>Registrar baja de tipo de material</span></div>
            </div>
          </div>

          <!-- Module 2: Salas -->
          <div class="req-card" id="req-card-2">
            <div class="req-card-header" onclick="toggleReqCard('req-card-2')">
              <span class="req-card-title">🏛️ Administrar Salas de Exhibición</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">4 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-10</span><span>Registrar sala</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-11</span><span>Consultar sala</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-12</span><span>Modificar sala</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-13</span><span>Registrar baja de sala</span></div>
            </div>
          </div>

          <!-- Module 3: Guías y Estilos -->
          <div class="req-card" id="req-card-3">
            <div class="req-card-header" onclick="toggleReqCard('req-card-3')">
              <span class="req-card-title">🎙️ Administrar Guías & Estilos de Obra</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">7 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-14</span><span>Registrar guía</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-15</span><span>Consultar guía</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-16</span><span>Registrar modificación de guía</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-17</span><span>Registrar baja de guía</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-18</span><span>Registrar estilo de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-19</span><span>Consultar estilo de obra</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-20</span><span>Registrar baja de estilo de obra</span></div>
            </div>
          </div>

          <!-- Module 4: Incidentes y Exposiciones -->
          <div class="req-card" id="req-card-4">
            <div class="req-card-header" onclick="toggleReqCard('req-card-4')">
              <span class="req-card-title">⚠️ Tipos de Incidentes & Exposiciones</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">5 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-21</span><span>Registrar tipo de incidente</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-22</span><span>Consultar tipo de incidente</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-23</span><span>Registrar baja de tipo de incidente</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-24</span><span>Registrar programación de exposiciones</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-25</span><span>Consultar programación de exposiciones</span></div>
            </div>
          </div>

          <!-- Module 5: Visitas y Entradas -->
          <div class="req-card" id="req-card-5">
            <div class="req-card-header" onclick="toggleReqCard('req-card-5')">
              <span class="req-card-title">🎟️ Visitas Guiadas & Venta de Entradas</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">6 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-26</span><span>Registrar planificación de visitas guiadas</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-27</span><span>Consultar planificación de visitas guiadas</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-28</span><span>Consultar agenda de guías</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-29</span><span>Registrar venta de entrada</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-30</span><span>Registrar contratación de servicio adicional de guía</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-31</span><span>Consultar venta de entrada</span></div>
            </div>
          </div>

          <!-- Module 6: Rondas e Incidentes (CRÍTICO) -->
          <div class="req-card gold-focus open" id="req-card-6">
            <div class="req-card-header" onclick="toggleReqCard('req-card-6')">
              <span class="req-card-title" style="color: var(--gold-light);">🛡️ Rondas e Incidentes (Proceso Crítico)</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">6 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-32</span><span>Generar planificación de rondas de vigilancia</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-33</span><span>Consultar planificación de rondas de vigilancia</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-34</span><span>Registrar revisión de sala</span></div>
              <div class="req-item-row"><span class="req-code-badge" style="background: rgba(212, 175, 55, 0.2); border-color: var(--gold-primary); color: var(--gold-light);">RF-35</span><strong style="color: var(--gold-light);">Registrar incidente (Disparador de CU-15)</strong></div>
              <div class="req-item-row"><span class="req-code-badge">RF-36</span><span>Consultar incidentes</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-37</span><span>Registrar seguimiento de resolución de incidente</span></div>
            </div>
          </div>

          <!-- Module 7: Restauración, Reportes & Sesión -->
          <div class="req-card" id="req-card-7">
            <div class="req-card-header" onclick="toggleReqCard('req-card-7')">
              <span class="req-card-title">🔄 Restauración, Informes & Sesión</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">7 RFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row"><span class="req-code-badge">RF-40</span><span>Registrar obra a restaurar</span></div>
              <div class="req-item-row"><span class="req-code-badge" style="color: var(--emerald-marine);">RF-41</span><span>Registrar reingreso de obra (Aplica Regla de Negocio RN1)</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-42</span><span>Generar informe diario de vigilancia</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-43</span><span>Generar reporte de patrones de incidentes</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-44</span><span>Emitir historial de incidentes</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-45</span><span>Iniciar sesión</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-46</span><span>Cerrar sesión</span></div>
              <div class="req-item-row"><span class="req-code-badge">RF-47</span><span>Modificar contraseña</span></div>
            </div>
          </div>

          <!-- Module 8: Requerimientos No Funcionales -->
          <div class="req-card" id="req-card-8">
            <div class="req-card-header" onclick="toggleReqCard('req-card-8')">
              <span class="req-card-title">📱 Requerimientos No Funcionales</span>
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">2 RNFs</span>
                <span class="req-card-arrow">▼</span>
              </div>
            </div>
            <div class="req-card-body">
              <div class="req-item-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="req-code-badge" style="color: var(--gold-light);">RNF-1</span>
                  <strong>Módulo Web de Soporte</strong>
                </div>
                <div style="font-size: 12px; color: var(--text-muted); line-height: 1.4;">
                  Arquitectura web cliente-servidor accesible desde navegadores modernos sin requerir instalación de software en los puestos de trabajo.
                </div>
              </div>
              <div class="req-item-row" style="flex-direction: column; align-items: flex-start; gap: 4px; border-bottom: none;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <span class="req-code-badge" style="color: var(--cyan-marine);">RNF-2</span>
                  <strong>Interfaz Móvil para Rondas en Tablet</strong>
                </div>
                <div style="font-size: 12px; color: var(--text-muted); line-height: 1.4;">
                  Interfaz responsiva y táctil adaptada para tablets portátiles, permitiendo visualización de planos de salas y reporte inmediato de siniestros.
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ====================================================== -->
    <!-- SLIDE 8: DCU EXPANSIVO (FRAN THOMAS RAPP)              -->
    <!-- ====================================================== -->
    <div class="slide" id="slide-8" data-topic="2.7 Casos de Uso">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <div>
            <span class="chapter-tag">Capítulo 2.7 &bull; Vista Externa del Software &bull; Francisco Thomas Rapp</span>
            <h1 class="slide-title">Diagrama de Casos de Uso del Sistema (DCU)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Frontera del sistema, numeración continua correlativa del 1 al 42 y módulo de sesión 43 al 45.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso Completo')">
            <span>🔍</span> Super Zoom Modal HD
          </button>
        </div>

        <div class="expansive-diagram-layout">
          <!-- Big Diagram Viewport with Toolbar Presets -->
          <div class="expansive-viewport-card">
            <div class="expansive-toolbar">
              <span style="font-size: 11px; font-weight: 700; color: var(--gold-light); text-transform: uppercase;">
                🎯 Enfoque Rápido por Cuadrante:
              </span>
              <div class="preset-pill-group">
                <button class="preset-btn active" id="btn-dcu-all" onclick="focusDcu('all', this)">🔍 Ver Todo</button>
                <button class="preset-btn" id="btn-dcu-obras" onclick="focusDcu('obras', this)">🖼️ Obras (1..9)</button>
                <button class="preset-btn" id="btn-dcu-incidentes" onclick="focusDcu('incidentes', this)">🛡️ Rondas (13..24)</button>
                <button class="preset-btn" id="btn-dcu-entradas" onclick="focusDcu('entradas', this)">🎟️ Entradas (10..12)</button>
                <button class="preset-btn" id="btn-dcu-admin" onclick="focusDcu('admin', this)">💻 Admin (25..45)</button>
              </div>
            </div>

            <div class="expansive-canvas" id="dcu-canvas">
              <img id="slide-dcu-img" src="{b64_dcu}" alt="Diagrama de Casos de Uso">
              <div class="gallery-frame-badge">💡 Haz click en los cuadrantes arriba para ampliar sectores</div>
            </div>
          </div>

          <!-- Right Column: System Boundary & Architecture -->
          <div style="display: flex; flex-direction: column; justify-content: space-between;">
            <div class="arch-block">
              <div class="arch-block-title">Consistencia de Numeración 1..42</div>
              <div class="arch-block-desc">
                Se unificó la secuencia correlativa del 1 al 42 en perfecta correspondencia con la tabla de objetivos, evitando desfases numéricos de versiones previas.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--gold-primary);">
              <div class="arch-block-title" style="color: var(--gold-light);">Núcleo Operativo del Guardia</div>
              <div class="arch-block-desc">
                &bull; <strong>CU-13:</strong> Generar planificación de rondas<br>
                &bull; <strong>CU-14:</strong> Consultar planificación de rondas<br>
                &bull; <strong>CU-15:</strong> Registrar incidente (Caso de Estudio)<br>
                &bull; <strong>CU-16:</strong> Registrar revisión de la sala
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--cyan-marine);">
              <div class="arch-block-title" style="color: var(--cyan-marine);">Frontera del Sistema (Boundary)</div>
              <div class="arch-block-desc">
                Delimita estrictamente las capacidades provistas por el software del museo respecto del entorno operativo y los actores externos.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 9: ACTORES Y RELACIONES DCU -->
    <div class="slide" id="slide-9" data-topic="2.7 Relaciones DCU">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <span class="chapter-tag">Capítulo 2.7 &bull; Arquitectura de Casos de Uso &bull; Francisco Thomas Rapp</span>
        <h1 class="slide-title">Actores y Dependencias &laquo;extend&raquo; e &laquo;include&raquo;</h1>
        <p class="slide-subtitle">Fundamentación rigurosa de las relaciones formales en el Diagrama de Casos de Uso.</p>

        <div class="grid-2-even">
          <div>
            <div class="arch-block">
              <div class="arch-block-title">Actores Principales del Dominio</div>
              <div class="arch-block-desc">
                &bull; <strong>Responsable de Ingreso de Obras:</strong> Registra altas, reingresos y derivaciones a restauración.<br>
                &bull; <strong>Administrador del Museo:</strong> Planifica exhibiciones y autoriza bajas de piezas.<br>
                &bull; <strong>Responsable de Atención al Cliente:</strong> Venta de entradas y contratación de guías.<br>
                &bull; <strong>Encargado de Vigilancia (EV):</strong> Rondas, revisión de salas y reporte de siniestros.<br>
                &bull; <strong>Encargado de Supervisión:</strong> Informes consolidados y patrones de incidentes.<br>
                &bull; <strong>Admin del Sistema / Usuario:</strong> Parámetros de catálogos y seguridad.
              </div>
            </div>
          </div>

          <div>
            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Relación &laquo;extend&raquo; (Condicional)</span>
                <span class="badge-gold">CU-15 &rarr; CU-16</span>
              </div>
              <div class="arch-block-desc">
                <strong>Registrar incidente &rarr; Registrar revisión de la sala:</strong><br>
                El guardia siempre revisa la sala (caso base). La registración de un incidente es una <em>extensión condicional</em> que solo se ejecuta cuando se constata un desperfecto físico.
              </div>
            </div>

            <div class="plaque-gold">
              <div class="plaque-gold-header">
                <span class="plaque-gold-title">Relación &laquo;include&raquo; (Mandatoria)</span>
                <span class="badge-gold">CU-11 &rarr; CU-12</span>
              </div>
              <div class="arch-block-desc">
                <strong>Contratar servicio de guía &rarr; Consultar agenda de guías:</strong><br>
                Es técnicamente imposible contratar un servicio de guía sin incluir de manera obligatoria la verificación de disponibilidad horaria del personal.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: EXPLORADOR INTERACTIVO CU-15 -->
    <div class="slide" id="slide-10" data-topic="2.8 Plantilla CU-15">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div>
            <span class="chapter-tag">Capítulo 2.8 &bull; Especificación de Caso de Uso &bull; Lucas Moyano</span>
            <h1 class="slide-title">Explorador Interactivo: Registrar Incidente (CU-15)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Haz click en cada paso para inspeccionar la interacción entre el operador y el sistema.</p>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn-header" onclick="showNormalCourse()">Curso Normal (14 Pasos)</button>
            <button class="btn-header" onclick="showAltCourses()">Cursos Alternativos</button>
          </div>
        </div>

        <div class="step-explorer">
          <div class="steps-list-container" id="steps-container"></div>

          <div class="step-detail-viewer">
            <div>
              <div class="step-detail-header">
                <div class="step-detail-title" id="detail-step-title">Paso 1: Inicio</div>
                <div class="step-actor-tag actor-guardia" id="detail-step-actor">Encargado de Vigilancia</div>
              </div>
              <div class="step-action-box" id="detail-step-desc">
                El Encargado de Vigilancia ingresa a la opción "Reportar incidente" desde la pantalla de la tablet.
              </div>
              <div class="step-data-payload" id="detail-step-payload">
                <div class="step-data-payload-title">Datos / Estado en este paso:</div>
                <div style="font-size: 13px; color: var(--gold-light);" id="detail-step-data">
                  Entrada al caso de uso transaccional. Precondición activa: guardia logueado.
                </div>
              </div>
            </div>

            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 10px;">
              <button class="btn-header" onclick="prevStep()"><span>&larr;</span> Paso Anterior</button>
              <span style="font-size: 12px; color: var(--gold-light); font-family: var(--font-display);" id="step-progress-label">Paso 1 de 14</span>
              <button class="btn-header" onclick="nextStep()">Siguiente Paso <span>&rarr;</span></button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 11: PROTOTIPO DE INTERFAZ -->
    <div class="slide" id="slide-11" data-topic="2.8 Prototipo UI">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div>
            <span class="chapter-tag">Capítulo 2.8 &bull; Interfaz de Usuario &bull; Kevin Pereyra</span>
            <h1 class="slide-title">Prototipo de Pantalla: Módulo Web en Tablet</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Diseño ergonómico para el guardia y correspondencia con los pasos del CU-15.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
            <span>🔍</span> Inspeccionar con Pan & Zoom
          </button>
        </div>

        <div class="grid-2">
          <div class="gallery-frame" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
            <img src="{b64_proto}" alt="Prototipo Tablet">
            <div class="gallery-frame-badge"><span>🔍</span> Pan & Zoom</div>
          </div>

          <div style="display: flex; flex-direction: column; justify-content: space-between;">
            <div class="arch-block">
              <div class="arch-block-title">Entrada Rápida de Inventario (Pasos 2 y 3)</div>
              <div class="arch-block-desc">
                Campo táctil de entrada numérica con foco automático para el código de la obra (ej: <code>OBJ-408</code>).
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--gold-primary);">
              <div class="arch-block-title" style="color: var(--gold-light);">Plaqueta de Verificación Visual (Paso 4)</div>
              <div class="arch-block-desc">
                Despliega sin ambigüedad: <strong>Título de la Obra, Sala Asignada y Ubicación Física dentro de la Sala</strong>.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--cyan-marine);">
              <div class="arch-block-title" style="color: var(--cyan-marine);">Tipificación y Confirmación (Pasos 7 a 12)</div>
              <div class="arch-block-desc">
                Selector táctil con tipos reglamentarios (Deterioro natural, provocado, caída accidental), hora del servidor y confirmación final.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ====================================================== -->
    <!-- SLIDE 12: DCD EXPANSIVO (JUAN TARDITTI)                -->
    <!-- ====================================================== -->
    <div class="slide" id="slide-12" data-topic="2.9 Clases del Dominio">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
          <div>
            <span class="chapter-tag">Capítulo 2.9 &bull; Vista Interna Orientada a Objetos &bull; Juan Tarditti</span>
            <h1 class="slide-title">Diagrama de Clases del Dominio (DCD)</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Arquitectura estática de soporte para la gestión de incidentes y rondas.</p>
          </div>
          <button class="btn-header" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
            <span>🔍</span> Super Zoom Modal HD
          </button>
        </div>

        <div class="expansive-diagram-layout">
          <!-- Big Diagram Viewport with Toolbar Presets -->
          <div class="expansive-viewport-card">
            <div class="expansive-toolbar">
              <span style="font-size: 11px; font-weight: 700; color: var(--gold-light); text-transform: uppercase;">
                🎯 Enfoque por Clúster de Clases:
              </span>
              <div class="preset-pill-group">
                <button class="preset-btn active" id="btn-dcd-all" onclick="focusDcd('all', this)">🔍 Ver Todo</button>
                <button class="preset-btn" id="btn-dcd-inc" onclick="focusDcd('incidente', this)">⚡ Incidente & Tipo (1)</button>
                <button class="preset-btn" id="btn-dcd-sala" onclick="focusDcd('sala', this)">🏛️ Sala & Guardias (1..*)</button>
                <button class="preset-btn" id="btn-dcd-obra" onclick="focusDcd('obra', this)">🎨 Obra & Estado</button>
              </div>
            </div>

            <div class="expansive-canvas" id="dcd-canvas">
              <img id="slide-dcd-img" src="{b64_dcd}" alt="Diagrama de Clases">
              <div class="gallery-frame-badge">💡 Haz click en los clústeres para ampliar clases</div>
            </div>
          </div>

          <!-- Right Column: Classes and Encapsulation -->
          <div style="display: flex; flex-direction: column; justify-content: space-between;">
            <div class="arch-block">
              <div class="arch-block-title">Entidades Centrales del Dominio</div>
              <div class="arch-block-desc">
                &bull; <strong>Incidente:</strong> Instancia transaccional con fecha, hora y tipología.<br>
                &bull; <strong>TipoIncidente:</strong> Clasificador tipológico.<br>
                &bull; <strong>ObraDeArte:</strong> Entidad patrimonial con puntero a Estado.<br>
                &bull; <strong>Sala, Guardia & SalaXGuardia:</strong> Modelo de asignación temporal.
              </div>
            </div>

            <div class="arch-block" style="border-left-color: var(--cyan-marine);">
              <div class="arch-block-title" style="color: var(--cyan-marine);">Encapsulamiento y Métodos de Negocio</div>
              <div class="arch-block-desc">
                Operaciones completas: <code>buscarObraPorCodigo()</code>, <code>actualizarEstado("Inactivo")</code>, <code>registrarIncidente()</code>.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 13: MULTIPLICIDADES DCD -->
    <div class="slide" id="slide-13" data-topic="2.9 Multiplicidades">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <span class="chapter-tag">Capítulo 2.9 &bull; Integridad Estructural del DCD &bull; Juan Tarditti</span>
        <h1 class="slide-title">Multiplicidades e Integridad en el Diagrama de Clases</h1>
        <p class="slide-subtitle">Resolución exhaustiva de las observaciones de cátedra sobre asociaciones del modelo.</p>

        <div class="grid-2-even">
          <div class="plaque-gold">
            <div class="plaque-gold-header">
              <span class="plaque-gold-title">Asociación 1</span>
              <span class="badge-gold">Incidente &rarr; (1) TipoIncidente</span>
            </div>
            <div style="font-size: 13.5px; color: var(--gold-light); font-weight: 700; margin-bottom: 6px;">
              Multiplicidad Unívoca Obligatoria
            </div>
            <div class="arch-block-desc">
              Cada objeto de la clase <code>Incidente</code> está inexcusablemente asociado a <strong>exactamente un (1)</strong> <code>TipoIncidente</code>. No se admiten siniestros anónimos; esto garantiza la integridad requerida para los reportes estadísticos y el cómputo de patrones.
            </div>
          </div>

          <div class="plaque-gold">
            <div class="plaque-gold-header">
              <span class="plaque-gold-title">Asociación 2</span>
              <span class="badge-gold">Sala &rarr; (1..*) SalaXGuardia</span>
            </div>
            <div style="font-size: 13.5px; color: var(--gold-light); font-weight: 700; margin-bottom: 6px;">
              Historial Temporal de Rondas
            </div>
            <div class="arch-block-desc">
              La relación muchos a muchos entre <code>Sala</code> y <code>Guardia</code> está descompuesta mediante la clase asociativa <code>SalaXGuardia</code>. Una sala tiene a lo largo del tiempo <strong>múltiples (1..*) asignaciones</strong>, preservando qué guardia estuvo a cargo en cada turno.
            </div>
          </div>
        </div>

        <div class="arch-block" style="margin-top: 14px; border-left-color: var(--gold-primary);">
          <div class="arch-block-title" style="color: var(--gold-light);">Patrón de Transición de Estado de la Obra</div>
          <div class="arch-block-desc">
            Al ejecutarse el método <code>registrarIncidente()</code>, el controlador de caso de uso invoca <code>obra.setEstado("Inactivo")</code>. La pieza queda inhabilitada de inmediato para exhibición hasta que la curaduría autorice su derivación a depósito o taller.
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 14: CONSOLA INTERACTIVA DE TRAZABILIDAD -->
    <div class="slide" id="slide-14" data-topic="Trazabilidad N a M">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <div>
            <span class="chapter-tag">Trazabilidad de Punta a Punta &bull; Kevin Pereyra &bull; Tobias Molina</span>
            <h1 class="slide-title">Consola Interactiva de Trazabilidad N a M</h1>
            <p class="slide-subtitle" style="margin-bottom: 0;">Selecciona un requerimiento para explorar su correspondencia analítica con Casos de Uso, Reglas y Clases.</p>
          </div>
          <span class="badge-gold">Matriz Dinámica</span>
        </div>

        <div class="trace-console">
          <div>
            <div class="trace-filters">
              <span class="trace-filter-pill active" onclick="filterTrace('todos', this)">Todos</span>
              <span class="trace-filter-pill" onclick="filterTrace('rondas', this)">Vigilancia & Incidentes</span>
              <span class="trace-filter-pill" onclick="filterTrace('obras', this)">Obras & Depósito</span>
              <span class="trace-filter-pill" onclick="filterTrace('visitas', this)">Visitas & Guías</span>
            </div>

            <div class="trace-rf-list" id="trace-rf-container"></div>
          </div>

          <div class="trace-impact-dossier">
            <div class="trace-impact-header">
              <div>
                <span class="chapter-tag" id="trace-cat-tag">Vigilancia & Incidentes</span>
                <div style="font-family: var(--font-display); font-size: 16px; font-weight: 700; color: var(--gold-light);" id="trace-rf-title">
                  RF-35: Registrar incidente
                </div>
              </div>
              <span class="badge-gold" id="trace-mapping-badge">Mapeo N a M</span>
            </div>

            <div>
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 4px;">
                Casos de Uso Vinculados:
              </div>
              <div class="trace-pill-group" id="trace-cu-group">
                <span class="pill-cu">CU-15 Registrar incidente</span>
                <span class="pill-cu">CU-16 Registrar revisión de la sala</span>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
              <div>
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 4px;">
                  Regla de Negocio:
                </div>
                <div class="trace-pill-group" id="trace-rule-group">
                  <span class="pill-rule">RN2: Registro Inmediato</span>
                </div>
              </div>

              <div>
                <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 4px;">
                  Interfaz / Pantalla:
                </div>
                <div style="font-size: 12.5px; color: var(--cyan-marine); font-weight: 600;" id="trace-ui-label">
                  Módulo Web Tablet (Reporte)
                </div>
              </div>
            </div>

            <div>
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 4px;">
                Clases del Dominio Impactadas:
              </div>
              <div class="trace-pill-group" id="trace-class-group">
                <span class="pill-class">Incidente</span>
                <span class="pill-class">TipoIncidente</span>
                <span class="pill-class">ObraDeArte</span>
                <span class="pill-class">SalaXGuardia</span>
              </div>
            </div>

            <div class="arch-block" style="margin-bottom: 0; border-left-color: var(--gold-primary);">
              <div class="arch-block-title" style="color: var(--gold-light);">Justificación de Consistencia para la Cátedra:</div>
              <div class="arch-block-desc" id="trace-justification">
                El requerimiento se satisface transaccionalmente en el CU-15 cuando el guardia reporta el daño en sala, alterando el estado de la obra en memoria y persistiéndolo con sello temporal del servidor.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 15: CONCLUSIONES & CIERRE -->
    <div class="slide" id="slide-15" data-topic="Síntesis & Cierre">
      <div class="museum-card gold-edge">
        <div class="corner-tl"></div><div class="corner-tr"></div><div class="corner-bl"></div><div class="corner-br"></div>
        <span class="chapter-tag">Evaluación Final &bull; Grupo 6 &bull; ASI 2K10</span>
        <h1 class="slide-title">Conclusiones y Síntesis de Consistencia Metodológica</h1>
        <p class="slide-subtitle">Alineación estricta entre las necesidades del negocio, el modelo BPMN, los Casos de Uso y las Clases.</p>

        <div class="grid-2-even" style="margin-bottom: 18px;">
          <div class="arch-block">
            <div class="arch-block-title">Fortalezas del Análisis Realizado</div>
            <div class="arch-block-desc">
              &bull; <strong>Trazabilidad Rigurosa:</strong> Cada elemento modelado responde a una regla de negocio explícita (RN1 y RN2).<br>
              &bull; <strong>Sin Ambigüedad:</strong> El Paso 4 del CU-15 documenta con precisión los atributos visualizados por el guardia.<br>
              &bull; <strong>Consistencia Estructural:</strong> Multiplicidades unívocas en <code>TipoIncidente</code> y asociativas en <code>SalaXGuardia</code>.
            </div>
          </div>

          <div class="arch-block" style="border-left-color: var(--gold-primary);">
            <div class="arch-block-title" style="color: var(--gold-light);">Impacto en la Operatoria Museológica</div>
            <div class="arch-block-desc">
              La digitalización de rondas en tablets reduce el tiempo de detección de siniestros, preserva la bitácora inmutable de incidentes y asegura la custodia de piezas durante el ciclo de restauración.
            </div>
          </div>
        </div>

        <div style="background: rgba(10, 21, 38, 0.9); border: 1px solid var(--gold-muted); border-radius: 10px; padding: 22px; text-align: center;">
          <h2 style="font-family: var(--font-display); font-size: 20px; color: var(--gold-light); margin-bottom: 6px;">
            ¡Muchas Gracias por su Atención!
          </h2>
          <p style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 14px;">
            Quedamos a disposición de los profesores y del ayudante de cátedra para preguntas.
          </p>
          <div style="display: flex; gap: 8px; justify-content: center;">
            <span class="badge-gold">UTN FRC</span>
            <span class="badge-gold">Cátedra ASI 2K10</span>
            <span class="badge-gold">Grupo 6</span>
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Bottom Control Bar -->
  <footer>
    <button class="nav-btn-v2" id="btn-prev" onclick="prevSlide()">
      <span>&larr;</span> Anterior
    </button>

    <div style="display: flex; align-items: center; gap: 16px;">
      <div class="dots-strip" id="dots-container"></div>
      <div class="counter-label" id="slide-counter">Slide 1 de 15</div>
    </div>

    <button class="nav-btn-v2" id="btn-next" onclick="nextSlide()">
      Siguiente <span>&rarr;</span>
    </button>
  </footer>

  <!-- Pan & Zoom Modal -->
  <div class="zoom-modal" id="zoom-modal">
    <div class="modal-bar">
      <div class="modal-title-text">
        <span class="badge-gold">Visor de Alta Definición</span>
        <span id="modal-diagram-title">Diagrama</span>
      </div>
      <div class="modal-tools">
        <button class="tool-btn-v2" onclick="zoomIn()" title="Acercar (Zoom In)">+</button>
        <button class="tool-btn-v2" onclick="zoomOut()" title="Alejar (Zoom Out)">&minus;</button>
        <span class="zoom-scale-text" id="zoom-level">100%</span>
        <button class="tool-btn-v2" onclick="resetZoom()" title="Restablecer">↺</button>
        <button class="tool-btn-v2" onclick="closeZoomModal()" style="color: var(--rose-marine); font-weight: 800;" title="Cerrar (Esc)">&times;</button>
      </div>
    </div>

    <div class="modal-viewport" id="modal-viewport">
      <div class="zoomable-content" id="zoomable-content">
        <img id="modal-img" src="" alt="Diagrama">
      </div>
      <div class="modal-hint-pill">
        💡 Rueda del mouse para <strong>Zoom</strong> &bull; Arrastra con click para <strong>Pan</strong> &bull; Tecla <strong>Esc</strong> para cerrar
      </div>
    </div>
  </div>

  <script>
    const assets = {{
      b64_mapa: "{b64_mapa}",
      b64_bpmn_desc: "{b64_bpmn_desc}",
      b64_bpmn_oper: "{b64_bpmn_oper}",
      b64_dcu: "{b64_dcu}",
      b64_proto: "{b64_proto}",
      b64_dcd: "{b64_dcd}"
    }};

    let currentSlide = 1;
    const totalSlides = 15;

    function buildDots() {{
      const container = document.getElementById('dots-container');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {{
        const dot = document.createElement('div');
        dot.className = 'dot-v2' + (i === currentSlide ? ' active' : '');
        dot.title = 'Slide ' + i;
        dot.onclick = () => goToSlide(i);
        container.appendChild(dot);
      }}
    }}

    function updateSlide() {{
      for (let i = 1; i <= totalSlides; i++) {{
        const el = document.getElementById('slide-' + i);
        if (el) {{
          if (i === currentSlide) {{
            el.classList.add('active');
            const topic = el.getAttribute('data-topic') || '';
            document.getElementById('slide-topic-badge').innerText = topic;
          }} else {{
            el.classList.remove('active');
          }}
        }}
      }}

      const pct = (currentSlide / totalSlides) * 100;
      document.getElementById('progress-bar').style.width = pct + '%';
      document.getElementById('slide-counter').innerText = 'Slide ' + currentSlide + ' de ' + totalSlides;

      document.getElementById('btn-prev').disabled = (currentSlide === 1);
      document.getElementById('btn-next').disabled = (currentSlide === totalSlides);

      const dots = document.querySelectorAll('.dot-v2');
      dots.forEach((d, idx) => {{
        if (idx + 1 === currentSlide) {{
          d.classList.add('active');
        }} else {{
          d.classList.remove('active');
        }}
      }});
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) {{
        currentSlide++;
        updateSlide();
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        currentSlide--;
        updateSlide();
      }}
    }}

    function goToSlide(n) {{
      if (n >= 1 && n <= totalSlides) {{
        currentSlide = n;
        updateSlide();
      }}
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    // ==========================================
    // REQUERIMIENTOS ACCORDION CONTROLLER
    // ==========================================
    function toggleReqCard(id) {{
      const card = document.getElementById(id);
      if (card) {{
        card.classList.toggle('open');
      }}
    }}

    function toggleAllReqs(open) {{
      document.querySelectorAll('.req-card').forEach(c => {{
        if (open) c.classList.add('open');
        else c.classList.remove('open');
      }});
    }}

    function searchReqs() {{
      const term = document.getElementById('req-search').value.toLowerCase().trim();
      document.querySelectorAll('.req-card').forEach(card => {{
        const rows = card.querySelectorAll('.req-item-row');
        let cardMatches = false;
        rows.forEach(r => {{
          const txt = r.innerText.toLowerCase();
          if (term === '' || txt.includes(term)) {{
            r.style.display = 'flex';
            cardMatches = true;
          }} else {{
            r.style.display = 'none';
          }}
        }});
        if (term !== '' && cardMatches) {{
          card.classList.add('open');
        }}
      }});
    }}

    // ==========================================
    // EXPANSIVE DCU PRESET FOCUS
    // ==========================================
    function focusDcu(quadrant, btnEl) {{
      const img = document.getElementById('slide-dcu-img');
      if (!img) return;
      document.querySelectorAll('#slide-8 .preset-btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');

      img.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      if (quadrant === 'all') {{
        img.style.transform = 'translate(0px, 0px) scale(1)';
      }} else if (quadrant === 'obras') {{
        img.style.transform = 'translate(20%, 30%) scale(2.3)';
      }} else if (quadrant === 'incidentes') {{
        img.style.transform = 'translate(22%, -6%) scale(2.4)';
      }} else if (quadrant === 'entradas') {{
        img.style.transform = 'translate(20%, -36%) scale(2.4)';
      }} else if (quadrant === 'admin') {{
        img.style.transform = 'translate(-24%, 2%) scale(1.9)';
      }}
    }}

    // ==========================================
    // EXPANSIVE DCD PRESET FOCUS
    // ==========================================
    function focusDcd(cluster, btnEl) {{
      const img = document.getElementById('slide-dcd-img');
      if (!img) return;
      document.querySelectorAll('#slide-12 .preset-btn').forEach(b => b.classList.remove('active'));
      if (btnEl) btnEl.classList.add('active');

      img.style.transition = 'transform 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
      if (cluster === 'all') {{
        img.style.transform = 'translate(0px, 0px) scale(1)';
      }} else if (cluster === 'incidente') {{
        img.style.transform = 'translate(14%, -18%) scale(2.2)';
      }} else if (cluster === 'sala') {{
        img.style.transform = 'translate(-20%, -18%) scale(2.2)';
      }} else if (cluster === 'obra') {{
        img.style.transform = 'translate(0%, 26%) scale(2.1)';
      }}
    }}

    // ==========================================
    // PAN & ZOOM MODAL IMPLEMENTATION
    // ==========================================
    let scale = 1;
    let translateX = 0;
    let translateY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    const modal = document.getElementById('zoom-modal');
    const viewport = document.getElementById('modal-viewport');
    const content = document.getElementById('zoomable-content');
    const modalImg = document.getElementById('modal-img');
    const modalTitle = document.getElementById('modal-diagram-title');
    const zoomDisplay = document.getElementById('zoom-level');

    function applyTransform() {{
      content.style.transform = `translate(${{translateX}}px, ${{translateY}}px) scale(${{scale}})`;
      zoomDisplay.innerText = Math.round(scale * 100) + '%';
    }}

    function openZoomModal(assetKey, title) {{
      if (assets[assetKey]) {{
        modalImg.src = assets[assetKey];
        modalTitle.innerText = title;
        modal.classList.add('active');
        resetZoom();
      }}
    }}

    function closeZoomModal() {{
      modal.classList.remove('active');
    }}

    function zoomIn() {{
      scale = Math.min(scale * 1.3, 5);
      applyTransform();
    }}

    function zoomOut() {{
      scale = Math.max(scale / 1.3, 0.4);
      applyTransform();
    }}

    function resetZoom() {{
      scale = 1;
      translateX = 0;
      translateY = 0;
      applyTransform();
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY > 0 ? 0.85 : 1.18;
      scale = Math.min(Math.max(scale * delta, 0.4), 6);
      applyTransform();
    }}, {{ passive: false }});

    viewport.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;
      isDragging = true;
      viewport.classList.add('dragging');
      startX = e.clientX - translateX;
      startY = e.clientY - translateY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      translateX = e.clientX - startX;
      translateY = e.clientY - startY;
      applyTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
      viewport.classList.remove('dragging');
    }});

    window.addEventListener('keydown', (e) => {{
      if (modal.classList.contains('active')) {{
        if (e.key === 'Escape') closeZoomModal();
        else if (e.key === '+' || e.key === '=') zoomIn();
        else if (e.key === '-' || e.key === '_') zoomOut();
        else if (e.key === '0' || e.key === 'r') resetZoom();
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        goToSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        goToSlide(totalSlides);
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }}
    }});

    // ==========================================
    // CU-15 INTERACTIVE STEP DATA & CONTROLLER
    // ==========================================
    const cu15Steps = [
      {{
        num: 1,
        title: "Paso 1: Solicitud de Reporte",
        actor: "Encargado de Vigilancia",
        actorClass: "actor-guardia",
        desc: "El Encargado de Vigilancia ingresa a la opción 'Reportar incidente' desde la interfaz táctil de la tablet durante el recorrido por la sala.",
        data: "Precondición activa: Guardia autenticado en el Módulo Web de Soporte y sala de ronda seleccionada."
      }},
      {{
        num: 2,
        title: "Paso 2: Solicitud de Código de Obra",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema despliega el campo de entrada táctil y solicita al guardia que ingrese o escanee el código de identificación de la pieza involucrada.",
        data: "Control de foco: input de código habilitado con teclado numérico."
      }},
      {{
        num: 3,
        title: "Paso 3: Ingreso del Código",
        actor: "Encargado de Vigilancia",
        actorClass: "actor-guardia",
        desc: "El guardia ingresa el código de inventario de la obra afectada (ejemplo: 'OBJ-408').",
        data: "Parámetro enviado: codigoObra = 'OBJ-408'."
      }},
      {{
        num: 4,
        title: "Paso 4: Búsqueda y Despliegue de Datos",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema busca la obra por el código ingresado y muestra de forma explícita sus datos de identificación para certificación visual.",
        data: "DATOS MOSTRADOS SIN AMBIGÜEDAD (Exigencia de Cátedra):\\n• Título de la Obra: 'Fósil de Smilodon Populator'\\n• Sala Asignada: 'Sala C - Paleontología'\\n• Ubicación Física: 'Vitrina Central, Sector Norte'\\n• Estado actual: 'En Exhibición'"
      }},
      {{
        num: 5,
        title: "Paso 5: Solicitud de Confirmación de Pieza",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema solicita al guardia que corrobore visualmente si la pieza hallada en la base de datos se corresponde con la obra dañada frente a él.",
        data: "Interfaz: Botones táctiles 'Confirmar Pieza' y 'Cancelar'."
      }},
      {{
        num: 6,
        title: "Paso 6: Confirmación del Objeto",
        actor: "Encargado de Vigilancia",
        actorClass: "actor-guardia",
        desc: "El guardia verifica los datos en pantalla y confirma que el objeto es el correcto.",
        data: "Evento: objetoConfirmado = true."
      }},
      {{
        num: 7,
        title: "Paso 7: Solicitud de Tipo de Incidente",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema despliega el listado tipológico normalizado: Deterioro natural, Deterioro provocado o Caída accidental.",
        data: "Catálogo recuperado de la clase TipoIncidente."
      }},
      {{
        num: 8,
        title: "Paso 8: Selección de Tipología",
        actor: "Encargado de Vigilancia",
        actorClass: "actor-guardia",
        desc: "El guardia selecciona el tipo de daño constatado en la sala (ejemplo: 'Caída accidental').",
        data: "Selección: idTipoIncidente = 3 ('Caída accidental')."
      }},
      {{
        num: 9,
        title: "Paso 9: Pantalla de Revisión Final",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema muestra el resumen consolidado del incidente: sala/ubicación, obra involucrada, tipo de daño seleccionado, hora actual del servidor y nuevo estado previsto.",
        data: "Resumen pre-grabación: Hora servidor = '15:42:18' & Nuevo Estado = 'Inactivo'."
      }},
      {{
        num: 10,
        title: "Paso 10: Solicitud de Confirmación Final",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema solicita la confirmación definitiva para impactar la bitácora electrónica y bloquear la pieza.",
        data: "Diálogo modal: '¿Confirma el registro del incidente patrimonial?'"
      }},
      {{
        num: 11,
        title: "Paso 11: Confirmación Final",
        actor: "Encargado de Vigilancia",
        actorClass: "actor-guardia",
        desc: "El guardia confirma el registro final del incidente.",
        data: "Confirmación aprobada por el guardia."
      }},
      {{
        num: 12,
        title: "Paso 12: Registro Persistente de Incidente",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema instancia el objeto Incidente vinculado a la sala, la obra, el TipoIncidente (multiplicidad 1) y la hora actual provista por el servidor.",
        data: "Persistencia en base de datos: Incidente registrado con id correlativo."
      }},
      {{
        num: 13,
        title: "Paso 13: Inactivación de la Obra",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "El sistema actualiza el estado de la obra a 'Inactivo', retirándola de los catálogos de exhibición pública para su posterior peritaje.",
        data: "Invocación orientada a objetos: obra.setEstado('Inactivo')."
      }},
      {{
        num: 14,
        title: "Paso 14: Fin del Caso de Uso",
        actor: "Sistema Central",
        actorClass: "actor-sistema",
        desc: "Se emite el mensaje de éxito en la tablet del guardia y se retorna al menú de ronda de vigilancia.",
        data: "Postcondición de Éxito cumplida satisfactoriamente."
      }}
    ];

    let currentStepIdx = 0;

    function renderStepsList() {{
      const container = document.getElementById('steps-container');
      container.innerHTML = '';
      cu15Steps.forEach((s, idx) => {{
        const item = document.createElement('div');
        item.className = 'step-item-card' + (idx === currentStepIdx ? ' active' : '');
        item.onclick = () => selectStep(idx);
        item.innerHTML = `
          <div class="step-badge-num">P${{s.num}}</div>
          <div class="step-summary-text">${{s.title}}</div>
        `;
        container.appendChild(item);
      }});
    }}

    function selectStep(idx) {{
      currentStepIdx = idx;
      const s = cu15Steps[idx];
      document.getElementById('detail-step-title').innerText = s.title;
      const actorTag = document.getElementById('detail-step-actor');
      actorTag.innerText = s.actor;
      actorTag.className = 'step-actor-tag ' + s.actorClass;
      document.getElementById('detail-step-desc').innerText = s.desc;
      document.getElementById('detail-step-data').innerText = s.data;
      document.getElementById('step-progress-label').innerText = `Paso ${{s.num}} de ${{cu15Steps.length}}`;

      renderStepsList();
    }}

    function nextStep() {{
      if (currentStepIdx < cu15Steps.length - 1) {{
        selectStep(currentStepIdx + 1);
      }}
    }}

    function prevStep() {{
      if (currentStepIdx > 0) {{
        selectStep(currentStepIdx - 1);
      }}
    }}

    function showNormalCourse() {{
      selectStep(0);
    }}

    function showAltCourses() {{
      document.getElementById('detail-step-title').innerText = "Cursos Alternativos Formales";
      const actorTag = document.getElementById('detail-step-actor');
      actorTag.innerText = "Excepciones de Flujo";
      actorTag.className = "step-actor-tag actor-sistema";
      document.getElementById('detail-step-desc').innerText = 
        "• A1 (Paso 11): El guardia cancela la confirmación final del registro. Se aborta la operación y no se persiste ningún cambio en la obra.\\n" +
        "• A2 (Paso 4): El sistema busca el código ingresado pero no lo encuentra en la base de datos de obras. Emite mensaje de error y solicita el reingreso de un código válido.\\n" +
        "• A3 (Paso 6): El guardia no confirma la pieza mostrada al constatar que difiere físicamente. Se cancela el caso de uso preventivamente.";
      document.getElementById('detail-step-data').innerText = "Postcondición de Fracaso: La obra permanece en su estado previo y la sala mantiene su estado sin alteración.";
      document.getElementById('step-progress-label').innerText = "Cursos A1, A2 y A3";
    }}

    // ==========================================
    // TRACEABILITY MATRIX DATA & CONTROLLER
    // ==========================================
    const traceData = [
      {{
        id: "RF-35",
        cat: "rondas",
        catName: "Vigilancia & Incidentes",
        name: "Registrar incidente en sala",
        cus: ["CU-15 Registrar incidente", "CU-16 Registrar revisión de la sala"],
        mapping: "N a M (Extensión Condicional)",
        rule: "RN2: Registro Inmediato",
        ui: "Tablet Móvil - Pantalla de Reporte",
        classes: ["Incidente", "TipoIncidente", "ObraDeArte", "SalaXGuardia"],
        just: "El guardia registra el incidente en la tablet en el momento del hallazgo. Se modela como extensión condicional (<<extend>>) sobre la revisión de sala; no todo chequeo genera un incidente."
      }},
      {{
        id: "RF-36",
        cat: "rondas",
        catName: "Vigilancia & Incidentes",
        name: "Consultar incidentes registrados",
        cus: ["CU-18 Consultar incidente", "CU-23 Emitir historial de incidentes"],
        mapping: "N a M (Requerimiento Transversal)",
        rule: "Auditoría Interna",
        ui: "Módulo Web - Panel de Supervisión",
        classes: ["Incidente", "Empleado", "Sala"],
        just: "Un único requerimiento de consulta se desdobla en casos de uso de inspección interactiva para el guardia y de consolidación histórica para el supervisor."
      }},
      {{
        id: "RF-32",
        cat: "rondas",
        catName: "Vigilancia & Incidentes",
        name: "Generar planificación de rondas",
        cus: ["CU-13 Generar planificación de rondas"],
        mapping: "1 a 1 Transaccional",
        rule: "Seguridad Operativa",
        ui: "Módulo Web - Asignación de Turnos",
        classes: ["PlanificacionRonda", "Sala", "Guardia", "SalaXGuardia"],
        just: "Genera la asignación temporal entre salas y guardias para un turno específico, poblando las instancias de la clase asociativa SalaXGuardia."
      }},
      {{
        id: "RF-34",
        cat: "rondas",
        catName: "Vigilancia & Incidentes",
        name: "Registrar revisión de sala",
        cus: ["CU-16 Registrar revisión de la sala"],
        mapping: "1 a N (Caso Base)",
        rule: "Control Continuo",
        ui: "Tablet Móvil - Plano Interactivo",
        classes: ["Sala", "SalaXGuardia", "Guardia"],
        just: "Caso de uso base ejecutado obligatoriamente por el guardia al ingresar a cada sala, actualizando el conteo de salas verificadas en la ronda."
      }},
      {{
        id: "RF-40",
        cat: "obras",
        catName: "Obras & Depósito",
        name: "Registrar obra a restaurar",
        cus: ["CU-4 Registrar obra a restaurar"],
        mapping: "1 a 1 Transaccional",
        rule: "Custodia Patrimonial",
        ui: "Módulo Web - Derivación a Taller",
        classes: ["ObraDeArte", "Restauracion", "Estado"],
        just: "Cambia el estado de la obra dañada para su traslado a los talleres de conservación tras el dictamen pericial del curador."
      }},
      {{
        id: "RF-41",
        cat: "obras",
        catName: "Obras & Depósito",
        name: "Registrar reingreso de obra restaurada",
        cus: ["CU-2 Registrar reingreso de obra"],
        mapping: "1 a 1 con Regla de Negocio",
        rule: "RN1: Reingreso Obligatorio a Depósito",
        ui: "Módulo Web - Control de Depósito",
        classes: ["ObraDeArte", "Deposito", "Restauracion"],
        just: "Aplica de forma estricta la RN1: toda obra restaurada debe ingresar obligatoriamente al depósito antes de definir cualquier nuevo destino."
      }},
      {{
        id: "RF-01",
        cat: "obras",
        catName: "Obras & Depósito",
        name: "Registrar ingreso de obra nueva",
        cus: ["CU-1 Registrar ingreso de obra"],
        mapping: "1 a 1 Transaccional",
        rule: "Catalogación Inicial",
        ui: "Módulo Web - Alta de Patrimonio",
        classes: ["ObraDeArte", "TipoObra", "TipoMaterial", "Estilo"],
        just: "Alta inicial en el inventario institucional con asignación de código unívoco, dimensiones, técnica y estado inicial."
      }},
      {{
        id: "RF-28",
        cat: "visitas",
        catName: "Visitas & Guías",
        name: "Consultar agenda de guías",
        cus: ["CU-12 Consultar agenda de guías", "CU-11 Registrar contratación de servicio de guía"],
        mapping: "N a M (Inclusión Mandatoria)",
        rule: "Coordinación de Personal",
        ui: "Módulo Web - Calendario de Guías",
        classes: ["Guia", "AgendaGuia", "Turno"],
        just: "El CU-11 incluye obligatoriamente (<<include>>) la consulta de agenda del CU-12 para garantizar la disponibilidad horaria del profesional."
      }},
      {{
        id: "RF-29",
        cat: "visitas",
        catName: "Visitas & Guías",
        name: "Registrar venta de entrada",
        cus: ["CU-10 Registrar venta de entrada", "CU-11 Registrar contratación de servicio de guía"],
        mapping: "N a M (Extensión Opcional)",
        rule: "Recaudación y Aforo",
        ui: "Módulo Web - Boletería",
        classes: ["Entrada", "Venta", "Tarifa"],
        just: "La venta de entrada es el caso base. La contratación de guía es una extensión facultativa solicitada a discreción por el visitante."
      }}
    ];

    let currentTraceCat = 'todos';

    function renderTraceList() {{
      const container = document.getElementById('trace-rf-container');
      container.innerHTML = '';
      const filtered = traceData.filter(d => currentTraceCat === 'todos' || d.cat === currentTraceCat);
      filtered.forEach((d, idx) => {{
        const item = document.createElement('div');
        item.className = 'trace-rf-item' + (idx === 0 ? ' active' : '');
        item.onclick = () => selectTrace(d, item);
        item.innerHTML = `
          <span class="trace-rf-code">${{d.id}}</span>
          <span class="trace-rf-name">${{d.name}}</span>
          <span class="badge-gold" style="font-size: 10px; padding: 2px 6px;">${{d.catName.split(' ')[0]}}</span>
        `;
        container.appendChild(item);
      }});
      if (filtered.length > 0) selectTrace(filtered[0], container.firstChild);
    }}

    function filterTrace(cat, pillEl) {{
      currentTraceCat = cat;
      document.querySelectorAll('.trace-filter-pill').forEach(p => p.classList.remove('active'));
      pillEl.classList.add('active');
      renderTraceList();
    }}

    function selectTrace(d, itemEl) {{
      document.querySelectorAll('.trace-rf-item').forEach(i => i.classList.remove('active'));
      if (itemEl) itemEl.classList.add('active');

      document.getElementById('trace-cat-tag').innerText = d.catName;
      document.getElementById('trace-rf-title').innerText = `${{d.id}}: ${{d.name}}`;
      document.getElementById('trace-mapping-badge').innerText = d.mapping;

      const cuGroup = document.getElementById('trace-cu-group');
      cuGroup.innerHTML = d.cus.map(c => `<span class="pill-cu">${{c}}</span>`).join('');

      const ruleGroup = document.getElementById('trace-rule-group');
      ruleGroup.innerHTML = `<span class="pill-rule">${{d.rule}}</span>`;

      document.getElementById('trace-ui-label').innerText = d.ui;

      const classGroup = document.getElementById('trace-class-group');
      classGroup.innerHTML = d.classes.map(c => `<span class="pill-class">${{c}}</span>`).join('');

      document.getElementById('trace-justification').innerText = d.just;
    }}

    // Initialization
    buildDots();
    updateSlide();
    renderStepsList();
    selectStep(0);
    renderTraceList();
  </script>
</body>
</html>
'''

with open("presentacion.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated presentation generated: presentacion.html ({len(html_content)} bytes).")
