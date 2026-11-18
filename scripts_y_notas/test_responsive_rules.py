# Test responsive CSS rules
responsive_css = """
    /* ========================================================
       PERFECT RESPONSIVE ENGINE (DESKTOP, TABLET, MOBILE)
       ======================================================== */

    /* Fluid Typography and Global Overflow Control */
    html, body {
      overflow-x: hidden;
      width: 100%;
      max-width: 100%;
    }

    /* Universal Responsive Image Scaling */
    img {
      max-width: 100%;
      height: auto;
    }

    /* Table Responsive Wrapper */
    .table-responsive-wrapper {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin-bottom: 12px;
      border-radius: 8px;
    }

    /* Large Desktops / TVs (>= 1600px) */
    @media (min-width: 1600px) {
      main {
        max-width: 1560px;
        padding: 32px 56px 120px 56px;
      }
    }

    /* Laptops & Standard Monitors (1025px - 1440px) */
    @media (max-width: 1440px) {
      main {
        padding: 20px 36px 110px 36px;
      }
      .giant-title {
        font-size: clamp(28px, 3.5vw, 48px);
      }
    }

    /* Tablets & Small Laptops (<= 1024px) */
    @media (max-width: 1024px) {
      header {
        padding: 12px 24px;
      }
      main {
        padding: 16px 20px 105px 20px;
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

      /* Responsive Diagram Frame Heights (no overflow, no clipping) */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {
        height: clamp(340px, 52vh, 580px) !important;
      }

      /* DCU column centering on tablet */
      #slide-9 [style*="grid-template-columns: 620px 1fr"] > div:first-child {
        max-width: 680px;
        margin: 0 auto;
        width: 100%;
      }
    }

    /* Tablets Portrait & Large Mobiles (<= 860px) */
    @media (max-width: 860px) {
      /* Stack 2-column layouts */
      [style*="grid-template-columns: 1fr 1fr"],
      [style*="grid-template-columns: 1.15fr 0.85fr"] {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }

      /* Header center label hide to avoid collision */
      .header-center {
        display: none !important;
      }

      /* Reduce card padding slightly for better space */
      .card-dark {
        padding: 18px 20px !important;
        border-radius: 16px !important;
      }

      /* Slide 1 Hero Header */
      #slide-1 .card-dark:first-child {
        padding: 24px 22px !important;
      }

      /* Team grids become 2 columns */
      [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
      }

      /* Slide 14 Split */
      #slide-14 [style*="grid-template-columns: 0.95fr 1.05fr"] {
        grid-template-columns: 1fr !important;
      }
    }

    /* Mobile Phones (<= 640px) */
    @media (max-width: 640px) {
      header {
        padding: 10px 14px;
      }
      .header-left {
        font-size: 12px;
      }
      .header-counter-box {
        padding: 4px 10px;
        font-size: 12px;
      }

      main {
        padding: 12px 12px 95px 12px;
      }

      .giant-title {
        font-size: clamp(24px, 6.5vw, 36px) !important;
        margin-bottom: 6px;
      }
      .editorial-subtitle {
        font-size: 13.5px !important;
        line-height: 1.45;
        margin-bottom: 14px !important;
      }

      /* All remaining grids stack to 1 column */
      [style*="grid-template-columns: repeat(3, 1fr)"],
      [style*="grid-template-columns: repeat(2, 1fr)"],
      #slide-6 [style*="grid-template-columns: repeat(3, 1fr)"],
      #slide-14 [style*="grid-template-columns: repeat(3, 1fr)"] {
        grid-template-columns: 1fr !important;
        gap: 10px !important;
      }

      /* Slide 14 - Professors grid */
      #slide-14 [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
        gap: 6px !important;
      }

      /* Slide 9 Preset buttons on mobile */
      .preset-focus-bar {
        gap: 4px !important;
      }
      .preset-btn {
        padding: 4px 8px !important;
        font-size: 11px !important;
      }

      /* Buttons become mobile-friendly */
      .btn-primary, .btn-secondary {
        min-height: 42px !important;
        padding: 0 16px !important;
        font-size: 13px !important;
      }

      /* Compact Dock for Mobile */
      .mac-dock-container {
        height: 54px !important;
        bottom: 10px !important;
        padding: 0 10px !important;
        gap: 8px !important;
        max-width: calc(100vw - 20px) !important;
      }
      .dock-icon-btn {
        width: 38px !important;
        height: 38px !important;
        min-width: 38px !important;
        border-radius: 10px !important;
      }
      .dock-icon-btn svg {
        width: 18px !important;
        height: 18px !important;
      }
      .dock-counter-badge {
        font-size: 11px !important;
        padding: 3px 6px !important;
      }
      .dock-divider-mac {
        height: 22px !important;
        margin: 0 1px !important;
      }
      .dock-tooltip {
        display: none !important; /* Hide hover tooltips on mobile to avoid sticking */
      }

      /* Zoom Modal Toolbar Mobile */
      .zoom-modal-toolbar {
        top: 12px !important;
        max-width: calc(100vw - 24px) !important;
        padding: 6px 10px !important;
        gap: 6px !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
      }
      .zoom-btn {
        min-height: 34px !important;
        padding: 0 10px !important;
        font-size: 12px !important;
      }

      /* Overview modal cards on mobile */
      .overview-grid {
        grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)) !important;
        gap: 10px !important;
        padding: 14px !important;
      }

      /* Mobile Diagram Frame Heights */
      .diagram-frame-clean,
      .card-dark[style*="height: 750px"],
      .diagram-frame-clean[style*="height: 740px"],
      .diagram-frame-clean[style*="height: 620px"],
      .diagram-frame-clean[style*="height: 520px"],
      .diagram-frame-clean[style*="height: 480px"] {
        height: clamp(280px, 45vh, 420px) !important;
      }
    }

    /* Small Mobile Phones (<= 380px) */
    @media (max-width: 380px) {
      .header-left span {
        display: none; /* Show only icon on micro screens */
      }
      .mac-dock-container {
        gap: 5px !important;
        padding: 0 6px !important;
      }
      .dock-icon-btn {
        width: 34px !important;
        height: 34px !important;
        min-width: 34px !important;
      }
    }
"""
print("Responsive CSS rules constructed successfully!")
