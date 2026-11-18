# -*- coding: utf-8 -*-
"""
Full Generator for Minimalist Editorial Navy Presentation (presentacion.html)
"""
import sys, os
sys.path.append("scripts_y_notas")
from build_editorial_html import b64_mapa, b64_bpmn_desc, b64_bpmn_oper, b64_dcu, b64_proto, b64_dcd

svg_arrow_right = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
svg_arrow_left = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
svg_expand = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>'
svg_close = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18M6 6l12 12"/></svg>'
svg_grid = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>'
svg_fullscreen = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>'
svg_eye = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
svg_help = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
svg_plus = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'
svg_minus = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/></svg>'
svg_fit = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>'
svg_asterisk = '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L13.5 9L20 6L16 12L22 15L15 16L17 22L12 18L7 22L9 16L2 15L8 12L4 6L10.5 9L12 2Z"/></svg>'

with open("presentacion.html", "w", encoding="utf-8") as out:
    out.write('<!DOCTYPE html>\n<html lang="es">\n<head>\n')
    out.write('  <meta charset="UTF-8">\n')
    out.write('  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    out.write('  <title>Sistema de Gestión y Vigilancia Museológica – TPI ASI 2K10</title>\n')
    out.write('  <link rel="preconnect" href="https://fonts.googleapis.com">\n')
    out.write('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
    out.write('  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n')
    out.write('  <style>\n')
    
    # CSS
    out.write('''
:root {
  --navy-deep: #0A1628;
  --navy-card: #11233F;
  --navy-main: #1B3A6B;
  --blue-accent: #2F6BFF;
  --blue-accent-hover: #1E55E0;
  --blue-ice: #E8EEF7;
  --blue-ice-light: #F4F7FB;
  --bg-light: #F8FAFC;
  --text-dark: #0A1628;
  --text-secondary: #5B6B82;
  --text-light: #F8FAFC;
  --text-light-secondary: #9FB0C9;
  --border-light: rgba(27, 58, 107, 0.12);
  --border-dark: rgba(255, 255, 255, 0.12);
  --font-main: 'Manrope', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: var(--font-main);
  -webkit-font-smoothing: antialiased;
}

body {
  background-color: var(--navy-deep);
  color: var(--text-light);
  min-height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  transition: background-color 0.35s ease, color 0.35s ease;
  user-select: none;
}

body.theme-light {
  background-color: var(--bg-light);
  color: var(--text-dark);
}

/* Header */
header {
  height: 56px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-dark);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
  background: rgba(10, 22, 40, 0.9);
  transition: all 0.35s ease;
}

body.theme-light header {
  background: rgba(248, 250, 252, 0.92);
  border-bottom-color: var(--border-light);
}

.header-left {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

body.theme-light .header-left {
  color: var(--navy-deep);
}

.header-center {
  font-size: 13px;
  color: var(--text-light-secondary);
  font-weight: 600;
}

body.theme-light .header-center {
  color: var(--text-secondary);
}

.slide-num-pill {
  font-family: monospace;
  font-size: 13px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-light);
}

body.theme-light .slide-num-pill {
  background: var(--blue-ice);
  color: var(--navy-main);
}

/* Main Container */
main {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 24px 44px 110px 44px;
  max-width: 1480px;
  margin: 0 auto;
  width: 100%;
}

.slide {
  display: none;
  width: 100%;
  animation: slideFadeIn 0.4s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.slide.active {
  display: block;
}

@keyframes slideFadeIn {
  from { opacity: 0; transform: scale(0.985) translateY(12px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

/* Breadcrumb & Section tag */
.breadcrumb-tag {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--blue-accent);
  margin-bottom: 8px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

/* Typography */
.giant-title {
  font-size: clamp(32px, 4vw, 56px);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.08;
  margin-bottom: 8px;
}

body.theme-light .giant-title {
  color: var(--text-dark);
}

.editorial-subtitle {
  font-size: 15.5px;
  line-height: 1.55;
  color: var(--text-light-secondary);
  margin-bottom: 22px;
  max-width: 900px;
}

body.theme-light .editorial-subtitle {
  color: var(--text-secondary);
}

/* Cards */
.card-dark {
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 24px;
  padding: 24px 28px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
  position: relative;
  transition: all 0.25s ease;
}

.card-light {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 24px;
  padding: 24px 28px;
  box-shadow: 0 6px 24px rgba(10, 22, 40, 0.04);
  position: relative;
  color: var(--text-dark);
  transition: all 0.25s ease;
}

.card-dark:hover, .card-light:hover {
  transform: translateY(-2px);
}

/* Buttons */
.btn-primary {
  min-height: 56px;
  padding: 0 32px;
  border-radius: 999px;
  background: var(--blue-accent);
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 600;
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  box-shadow: 0 4px 16px rgba(47, 107, 255, 0.35);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  text-decoration: none;
}

.btn-primary:hover {
  background: var(--blue-accent-hover);
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(47, 107, 255, 0.45);
}

.btn-primary:active {
  transform: scale(0.97);
}

.btn-primary:focus-visible {
  outline: 2px solid var(--blue-accent);
  outline-offset: 3px;
}

.btn-secondary {
  min-height: 48px;
  padding: 0 22px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--text-light);
  border: 1px solid var(--border-dark);
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: all 0.2s ease;
}

body.theme-light .btn-secondary {
  background: var(--blue-ice);
  color: var(--navy-main);
  border-color: var(--border-light);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.16);
  transform: translateY(-1px);
}

body.theme-light .btn-secondary:hover {
  background: #d9e4f5;
}

.btn-secondary:active {
  transform: scale(0.97);
}

.btn-secondary:disabled {
  opacity: 0.3;
  cursor: not-allowed;
  transform: none !important;
}

/* Floating Bottom Dock */
.dock-container {
  position: fixed;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
  height: 64px;
  background: var(--navy-deep);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 999px;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 16px 48px rgba(10, 22, 40, 0.45);
  backdrop-filter: blur(16px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.dock-container.dimmed {
  opacity: 0.45;
}

.dock-container:hover {
  opacity: 1 !important;
}

.dock-counter {
  font-size: 15px;
  font-weight: 700;
  color: #FFFFFF;
  padding: 0 8px;
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.05em;
}

.dock-divider {
  width: 1px;
  height: 28px;
  background: rgba(255, 255, 255, 0.15);
}

/* Progressive Reveal Items */
.reveal-item {
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
}

.reveal-item.revealed {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

/* Expandable Content Cards */
.expandable-card {
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.expand-circle-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(47, 107, 255, 0.12);
  color: var(--blue-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.25s ease;
}

.expandable-card:hover .expand-circle-btn {
  background: var(--blue-accent);
  color: #FFFFFF;
  transform: scale(1.08);
}

.expandable-card.expanded {
  background: #FFFFFF !important;
  border-color: var(--blue-accent) !important;
  box-shadow: 0 12px 36px rgba(47, 107, 255, 0.2) !important;
  color: var(--navy-deep) !important;
}

.expandable-card.expanded .expand-circle-btn {
  background: var(--blue-accent);
  color: #FFFFFF;
  transform: rotate(45deg);
}

.card-extra-content {
  display: none;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid rgba(0, 0, 0, 0.08);
  font-size: 14px;
  line-height: 1.55;
  color: var(--text-secondary);
}

.expandable-card.expanded .card-extra-content {
  display: block;
}

/* Diagram Container & Framing */
.diagram-frame-clean {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 24px;
  padding: 16px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(10, 22, 40, 0.05);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.diagram-preview-img {
  width: 100%;
  height: auto;
  max-height: 480px;
  object-fit: contain;
  border-radius: 12px;
  cursor: pointer;
  display: block;
  transition: transform 0.3s ease;
}

.diagram-preview-img:hover {
  transform: scale(1.01);
}

.diagram-action-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 12px;
  padding-top: 10px;
  border-top: 1px solid rgba(27, 58, 107, 0.08);
}

/* Fullscreen Zoom Modal */
.zoom-fullscreen-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 22, 40, 0.94);
  backdrop-filter: blur(20px);
  z-index: 9999;
  display: none;
  flex-direction: column;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.zoom-fullscreen-modal.active {
  display: flex;
  opacity: 1;
}

.zoom-modal-top {
  height: 70px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.zoom-modal-title {
  font-size: 18px;
  font-weight: 700;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  gap: 12px;
}

.zoom-controls-floating {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--navy-deep);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 999px;
  padding: 8px 18px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
  z-index: 10001;
}

.zoom-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: #FFFFFF;
  height: 44px;
  padding: 0 16px;
  border-radius: 999px;
  font-size: 14px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.zoom-btn:hover {
  background: var(--blue-accent);
}

.zoom-viewport-stage {
  flex: 1;
  width: 100%;
  overflow: hidden;
  position: relative;
  cursor: grab;
  display: flex;
  align-items: center;
  justify-content: center;
}

.zoom-viewport-stage.dragging {
  cursor: grabbing;
}

.zoom-stage-content {
  position: absolute;
  transform-origin: center center;
  transition: transform 0.05s linear;
  will-change: transform;
}

.zoom-stage-content img {
  max-width: 90vw;
  max-height: 85vh;
  object-fit: contain;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
  border-radius: 12px;
  display: block;
  pointer-events: none;
}

/* Overview Grid Modal */
.overview-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 22, 40, 0.96);
  backdrop-filter: blur(20px);
  z-index: 9990;
  display: none;
  flex-direction: column;
  padding: 40px;
  opacity: 0;
  transition: opacity 0.3s ease;
  overflow-y: auto;
}

.overview-modal.active {
  display: flex;
  opacity: 1;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1400px;
  margin: 30px auto;
  width: 100%;
}

.overview-card-item {
  background: var(--navy-card);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 130px;
}

.overview-card-item:hover {
  background: rgba(47, 107, 255, 0.15);
  border-color: var(--blue-accent);
  transform: translateY(-2px);
}

.overview-card-item.current {
  border-color: var(--blue-accent);
  background: rgba(47, 107, 255, 0.2);
}

/* Onboarding Tutorial Modal */
.tutorial-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 22, 40, 0.85);
  backdrop-filter: blur(16px);
  z-index: 10050;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 24px;
}

.tutorial-modal.active {
  display: flex;
}

.tutorial-card-body {
  background: #FFFFFF;
  color: var(--navy-deep);
  border-radius: 28px;
  max-width: 580px;
  width: 100%;
  padding: 40px;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
}

/* Expansive Diagram Viewport */
.expansive-diagram-grid {
  display: grid;
  grid-template-columns: 1.35fr 0.65fr;
  gap: 24px;
  align-items: stretch;
}

.expansive-canvas-card {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(10, 22, 40, 0.05);
  display: flex;
  flex-direction: column;
}

.expansive-toolbar {
  height: 52px;
  padding: 0 20px;
  background: var(--blue-ice-light);
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.preset-pill-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.preset-btn {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  color: var(--navy-main);
  font-size: 12px;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 999px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.preset-btn:hover, .preset-btn.active {
  background: var(--blue-accent);
  color: #FFFFFF;
  border-color: var(--blue-accent);
}

.expansive-canvas {
  flex: 1;
  height: 540px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FAFCFF;
}

.expansive-canvas img {
  max-width: 95%;
  max-height: 95%;
  object-fit: contain;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  border-radius: 8px;
  user-select: none;
  pointer-events: none;
}

/* Accordion Requerimientos */
.req-accordion-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  max-height: 480px;
  overflow-y: auto;
  padding-right: 6px;
}

.req-accordion-grid::-webkit-scrollbar {
  width: 5px;
}
.req-accordion-grid::-webkit-scrollbar-thumb {
  background: var(--blue-ice);
  border-radius: 4px;
}

.req-card {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.2s ease;
}

.req-card-header {
  padding: 14px 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #FFFFFF;
  transition: background 0.2s ease;
}

.req-card-header:hover {
  background: var(--blue-ice-light);
}

.req-card-title {
  font-size: 13.5px;
  font-weight: 700;
  color: var(--navy-deep);
  display: flex;
  align-items: center;
  gap: 8px;
}

.req-card-body {
  display: none;
  padding: 14px 18px;
  background: #FAFCFF;
  border-top: 1px solid var(--border-light);
  flex-direction: column;
  gap: 6px;
}

.req-card.open .req-card-body {
  display: flex;
}

.req-card.open .req-card-arrow {
  transform: rotate(180deg);
}

.req-item-row {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--navy-deep);
  padding: 4px 0;
  border-bottom: 1px solid rgba(27, 58, 107, 0.05);
}

.req-code-badge {
  font-family: monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--blue-accent);
  background: var(--blue-ice);
  border: 1px solid rgba(47, 107, 255, 0.25);
  padding: 2px 6px;
  border-radius: 4px;
  min-width: 50px;
  text-align: center;
}

/* Step Explorer (CU-15) */
.step-explorer-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 20px;
  align-items: stretch;
}

.steps-list-container {
  max-height: 480px;
  overflow-y: auto;
  padding-right: 8px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.steps-list-container::-webkit-scrollbar {
  width: 5px;
}
.steps-list-container::-webkit-scrollbar-thumb {
  background: var(--blue-ice);
  border-radius: 4px;
}

.step-item-card {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 12px;
  padding: 12px 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.2s ease;
}

.step-item-card:hover {
  background: var(--blue-ice-light);
  border-color: var(--blue-accent);
}

.step-item-card.active {
  background: var(--blue-ice);
  border-color: var(--blue-accent);
  box-shadow: 0 4px 14px rgba(47, 107, 255, 0.15);
}

.step-badge-num {
  font-family: monospace;
  font-size: 11px;
  font-weight: 700;
  color: var(--blue-accent);
  background: #FFFFFF;
  border: 1px solid rgba(47, 107, 255, 0.3);
  padding: 3px 8px;
  border-radius: 6px;
  min-width: 32px;
  text-align: center;
}

.step-summary-text {
  font-size: 13px;
  font-weight: 600;
  color: var(--navy-deep);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex: 1;
}

.step-detail-viewer {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 20px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 6px 20px rgba(10, 22, 40, 0.04);
}

/* Traceability Console */
.trace-console-grid {
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  gap: 24px;
  align-items: stretch;
}

.trace-rf-list {
  max-height: 420px;
  overflow-y: auto;
  padding-right: 6px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.trace-rf-list::-webkit-scrollbar {
  width: 5px;
}
.trace-rf-list::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}

.trace-rf-item {
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 12px;
  padding: 12px 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.2s ease;
}

.trace-rf-item:hover {
  background: rgba(47, 107, 255, 0.15);
  border-color: var(--blue-accent);
}

.trace-rf-item.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

.trace-impact-dossier {
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 20px;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
''')
    out.write('  </style>\n</head>\n<body>\n')

    # Top Header
    out.write('''
  <header>
    <div class="header-left">Museo de Historia Natural</div>
    <div class="header-center">Grupo 6 &bull; ASI 2K10 &bull; TPI 2026</div>
    <div class="header-right">
      <span class="slide-num-pill" id="header-slide-num">01 / 14</span>
    </div>
  </header>
  <main>
''')

    # ========================================================
    # SLIDE 1: PORTADA & EQUIPO (THEME: DARK)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 1: PORTADA & EQUIPO -->
    <div class="slide active theme-dark" id="slide-1" data-topic="01 · Portada y Equipo" data-theme="dark">
      <div class="card-dark" style="margin-bottom: 24px; position: relative; overflow: hidden; padding: 40px 44px;">
        <div style="position: absolute; right: -40px; bottom: -40px; opacity: 0.12; pointer-events: none;">
          <svg width="340" height="340" viewBox="0 0 200 200" fill="none">
            <path d="M0 100 C 40 40, 160 160, 200 100" stroke="#2F6BFF" stroke-width="24" fill="none"/>
            <path d="M0 130 C 40 70, 160 190, 200 130" stroke="#2F6BFF" stroke-width="12" fill="none"/>
            <circle cx="160" cy="50" r="30" stroke="#2F6BFF" stroke-width="8"/>
          </svg>
        </div>

        <div class="breadcrumb-tag">
          {svg_asterisk} Trabajo Práctico Integrador &bull; Análisis de Sistemas de Información
        </div>
        <h1 class="giant-title">Sistema de Gestión y Vigilancia Museológica</h1>
        <p class="editorial-subtitle">
          Museo Provincial de Historia Natural &bull; Modelo Integral de Procesos de Negocio, Casos de Uso y Clases de Dominio.
        </p>

        <div style="display: flex; gap: 10px; margin-bottom: 24px; flex-wrap: wrap;">
          <span style="font-size: 12px; font-weight: 700; background: rgba(47, 107, 255, 0.18); color: var(--blue-accent); border: 1px solid rgba(47, 107, 255, 0.35); padding: 6px 14px; border-radius: 999px;">TPI 2026</span>
          <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #FFF; border: 1px solid rgba(255, 255, 255, 0.15); padding: 6px 14px; border-radius: 999px;">ASI 2K10</span>
          <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #FFF; border: 1px solid rgba(255, 255, 255, 0.15); padding: 6px 14px; border-radius: 999px;">UTN FRC</span>
          <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #FFF; border: 1px solid rgba(255, 255, 255, 0.15); padding: 6px 14px; border-radius: 999px;">Grupo 6</span>
        </div>

        <div style="display: flex; align-items: center; gap: 16px;">
          <button class="btn-primary" onclick="nextSlide()">
            Comenzar presentación {svg_arrow_right}
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()">
            {svg_grid} Ver los 14 slides
          </button>
        </div>
      </div>

      <!-- 9 Members Grid -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">01 &bull; DOMINIO</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 423269</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Dominio bajo estudio y Objetivos estratégicos</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">02 &bull; PROCESOS</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419166</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Mapa de Procesos de Negocio</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">03 &bull; REGLAS</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 403382</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Ficha Técnica y Reglas de Negocio (RN1 / RN2)</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">04 &bull; BPMN</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Jastrzebski, Emiliano</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 402760</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Modelado BPMN Descriptivo y Operativo</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">05 &bull; REQUERIMIENTOS</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419749</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Requerimientos y Trazabilidad N a M</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px; border-color: var(--blue-accent);">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">06 &bull; CASOS DE USO</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 408990</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Vista Externa: Diagrama de Casos de Uso (DCU)</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">07 &bull; PLANTILLA CU</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 410975</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Caso de Uso Esencial: CU-15 Registrar Incidente</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px; border-color: var(--blue-accent);">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">08 &bull; DOMINIO OO</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 400212</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Vista Interna: Diagrama de Clases del Dominio</div>
        </div>
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-family: monospace; font-size: 11px; font-weight: 700; color: var(--blue-accent); margin-bottom: 4px;">09 &bull; TRAZABILIDAD</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 418201</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 4px;">Prototipo Web Tablet y Trazabilidad Integral</div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 2: DOMINIO & OBJETIVOS (THEME: DARK)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide theme-dark" id="slide-2" data-topic="02 · Contexto y Objetivos" data-theme="dark">
      <div class="breadcrumb-tag">02 &bull; Contexto Organizacional</div>
      <h1 class="giant-title">Dominio bajo Estudio y Objetivos Estratégicos</h1>
      <p class="editorial-subtitle">
        Museo Provincial de Historia Natural: Custodia patrimonial, exhibición cultural y gestión de rondas.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Problemática Detectada</div>
          <div style="font-size: 15px; line-height: 1.6; color: var(--text-light);">
            El museo alberga colecciones históricas y biológicas insustituibles. La operatoria manual previa producía demoras críticas en la comunicación de incidentes de deterioro o caídas, falta de trazabilidad en las restauraciones y desajustes en las rondas de guardia.
          </div>
        </div>
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Misión Institucional</div>
          <div style="font-size: 15px; line-height: 1.6; color: var(--text-light);">
            Resguardar el patrimonio museológico mediante un estricto control de exhibición y rondas de seguridad activa, garantizando al mismo tiempo una experiencia de divulgación ágil para los visitantes.
          </div>
        </div>
      </div>

      <!-- 3 Expandable Objective Cards -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 42px; font-weight: 800; color: var(--blue-accent); line-height: 1;">01</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 17px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Tiempo Real en Sala</div>
          <div style="font-size: 14px; color: var(--text-light-secondary); line-height: 1.45;">
            Digitalizar el reporte de incidentes en el momento exacto del hallazgo.
          </div>
          <div class="card-extra-content">
            Dotar al personal de vigilancia de tablets táctiles para certificar el código de la pieza, sala y ubicación en muro, reduciendo a segundos la bitácora electrónica de siniestros.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 42px; font-weight: 800; color: var(--blue-accent); line-height: 1;">02</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 17px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Cadena de Custodia</div>
          <div style="font-size: 14px; color: var(--text-light-secondary); line-height: 1.45;">
            Garantizar el reingreso obligatorio a depósito previo a nueva disposición.
          </div>
          <div class="card-extra-content">
            Asegurar el cumplimiento estricto de la regla de negocio RN1: ninguna pieza restaurada puede volver a exhibición pública sin peritaje de depósito.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 42px; font-weight: 800; color: var(--blue-accent); line-height: 1;">03</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 17px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Control de Rondas y Guías</div>
          <div style="font-size: 14px; color: var(--text-light-secondary); line-height: 1.45;">
            Planificación dinámica de guardias y coordinación de agendas.
          </div>
          <div class="card-extra-content">
            Automatizar las hojas de ruta de los guardias por sala y turno, y coordinar de forma mandatoria las agendas de guías para visitas escolares y generales.
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 3: MAPA DE PROCESOS (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 3: MAPA DE PROCESOS -->
    <div class="slide theme-light" id="slide-3" data-topic="03 · Mapa de Procesos" data-theme="light">
      <div class="breadcrumb-tag">03 &bull; Vista Externa Organizacional</div>
      <h1 class="giant-title">Mapa de Procesos: Cadena de Valor del Museo</h1>
      <p class="editorial-subtitle">
        Clasificación de procesos: Estratégicos, Esenciales/Clave y de Soporte.
      </p>

      <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean reveal-item revealed">
          <img src="{b64_mapa}" class="diagram-preview-img" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')" alt="Mapa de Procesos">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: var(--text-secondary);">Cadena de Valor Completa</span>
            <button class="btn-primary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase; margin-bottom: 4px;">Procesos Estratégicos</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-secondary);">
              Planificación institucional, adquisición de piezas, convenios científicos y gestión de exposiciones temporales.
            </div>
          </div>

          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Procesos Clave / Esenciales</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-dark);">
              &bull; <strong>Exposición de Obras de Arte:</strong> Divulgación y atención.<br>
              &bull; <strong>Visitas Guiadas:</strong> Atención a contingentes escolares y público general.
            </div>
          </div>

          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--navy-deep);">
            <div style="font-size: 12px; font-weight: 700; color: var(--navy-deep); text-transform: uppercase; margin-bottom: 4px;">Proceso de Soporte Crítico</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-dark);">
              <strong>Realizar Ronda de Vigilancia y Gestión de Incidentes:</strong> Custodia activa en salas, verificación de condiciones de las obras y reporte inmediato de siniestros.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 4: PROCESO CRÍTICO & REGLAS (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 4: PROCESO CRÍTICO & REGLAS -->
    <div class="slide theme-light" id="slide-4" data-topic="04 · Proceso Crítico y Reglas" data-theme="light">
      <div class="breadcrumb-tag">04 &bull; Ficha Técnica &bull; Tomas Marcuzzi</div>
      <h1 class="giant-title">Descripción del Proceso Crítico: Vigilancia e Incidentes</h1>
      <p class="editorial-subtitle">
        Ficha técnica estructurada, formularios intervinientes y reglas de negocio determinantes.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Formularios y Documentos del Proceso</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-secondary);">
              &bull; <strong>Planificación de Ronda:</strong> Hoja de ruta asignada al guardia por sala y turno.<br>
              &bull; <strong>Registro de Incidente:</strong> Acta electrónica de tipificación de anomalía, pieza y hora.<br>
              &bull; <strong>Informe Diario de Vigilancia:</strong> Resumen consolidado emitido al cierre de guardia.
            </div>
          </div>

          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Listado de Actividades Formales</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-secondary);">
              1. Consultar planificación de rondas de vigilancia.<br>
              2. Inspección física de sala: bifurcación en compuerta.<br>
              3. Registro de sala con 'Observación pendiente' (camino del incidente).<br>
              4. Registro de sala con 'Sin novedades' (camino normal).<br>
              5. Generación de informe con salas recorridas y cierre.
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent); background: #FAFCFF;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;">Regla de Negocio 1 &bull; RN1</span>
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">MANDATORIA</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: var(--navy-deep); margin-bottom: 6px;">Reingreso Obligatorio a Depósito</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
              Toda obra enviada a restauración, se haya podido reparar con éxito o no, debe ingresar obligatoriamente al depósito del museo antes de definir su destino final o su baja formal. Ninguna pieza retorna directamente a sala de exhibición.
            </div>
          </div>

          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--navy-main); background: #FAFCFF;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase;">Regla de Negocio 2 &bull; RN2</span>
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--navy-main); padding: 3px 8px; border-radius: 4px;">INMEDIATEZ</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: var(--navy-deep); margin-bottom: 6px;">Registro Inmediato de Incidente</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
              El guardia debe registrar el incidente de la obra de forma inmediata ante el hallazgo en la sala, indicando obligatoriamente los datos exactos del siniestro, la pieza involucrada y la hora actual del servidor.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 5: BPMN DESCRIPTIVO (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide theme-light" id="slide-5" data-topic="05 · BPMN Descriptivo" data-theme="light">
      <div class="breadcrumb-tag">05 &bull; Vista Interna Macro &bull; Emiliano Jastrzebski</div>
      <h1 class="giant-title">BPMN Nivel 1: Visión Macro de la Vigilancia</h1>
      <p class="editorial-subtitle">
        Flujo general de punta a punta, límites de responsabilidad y carril de supervisión.
      </p>

      <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean reveal-item revealed">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')" alt="BPMN Descriptivo">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: var(--text-secondary);">Visión Gerencial Nivel 1</span>
            <button class="btn-primary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN a Nivel Descriptivo (Nivel 1)')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 12px;">
          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Objetivo del Nivel Descriptivo</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-secondary);">
              Brindar una perspectiva de negocio de alto nivel comprensible para la dirección del museo, estableciendo el inicio de la jornada, la verificación de salas y la emisión final del informe diario.
            </div>
          </div>

          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Carriles de Responsabilidad (Lanes)</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-dark);">
              &bull; <strong>Encargado de Vigilancia:</strong> Ejecuta la inspección de salas asignadas.<br>
              &bull; <strong>Sistema Central:</strong> Valida estados, persigue registros y emite informes.<br>
              &bull; <strong>Supervisor:</strong> Recibe el reporte diario y audita novedades.
            </div>
          </div>

          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase; margin-bottom: 4px;">Punto de Integración con Nivel 2</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-secondary);">
              La tarea central de revisión de sala se expande detalladamente en el nivel operativo mediante compuertas condicionales.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 6: BPMN OPERATIVO (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide theme-light" id="slide-6" data-topic="06 · BPMN Operativo" data-theme="light">
      <div class="breadcrumb-tag">06 &bull; Vista Interna Detallada &bull; Emiliano Jastrzebski</div>
      <h1 class="giant-title">BPMN Nivel 2: Lógica de Control y Compuerta XOR</h1>
      <p class="editorial-subtitle">
        Lógica de control en sala, compuerta exclusiva y bifurcación hacia el registro de incidentes.
      </p>

      <div class="diagram-frame-clean reveal-item revealed" style="margin-bottom: 20px;">
        <img src="{b64_bpmn_oper}" style="max-height: 280px; width: 100%; object-fit: contain; cursor: pointer;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')" alt="BPMN Operativo">
        <div class="diagram-action-bar">
          <span style="font-size: 13px; font-weight: 600; color: var(--text-secondary);">Flujo Operativo de Ronda y Bifurcación</span>
          <button class="btn-primary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN a Nivel Operativo (Nivel 2)')">
            Ampliar diagrama {svg_expand}
          </button>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--navy-main);">
          <div style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase; margin-bottom: 4px;">Camino Normal (Sin Novedades)</div>
          <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
            Si el guardia no constata anomalías en las piezas ni en las condiciones de la sala, registra el estado 'Sin novedades'. El sistema actualiza el registro de recorrido y habilita la inspección de la siguiente sala asignada en la planificación.
          </div>
        </div>

        <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Camino Alternativo (Anomalía Detectada)</div>
          <div style="font-size: 14px; line-height: 1.55; color: var(--text-dark);">
            Ante deterioro o caída, la sala pasa a 'Observación pendiente', disparando en forma inmediata la invocación del subproceso / caso de uso <strong>CU-15 Registrar incidente</strong> con identificación de la pieza, tipificación del daño y sellado de tiempo.
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 7: REQUERIMIENTOS (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 7: REQUERIMIENTOS -->
    <div class="slide theme-light" id="slide-7" data-topic="07 · Requerimientos" data-theme="light">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <div class="breadcrumb-tag">07 &bull; Catálogo Interactivo &bull; Tobias Molina</div>
          <h1 class="giant-title">Catálogo de Requerimientos y Consistencia N a M</h1>
          <p class="editorial-subtitle" style="margin-bottom: 14px;">
            45 Requerimientos Funcionales clasificados por módulo y 2 No Funcionales.
          </p>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
          <input type="text" id="req-search" placeholder="Buscar requerimiento..." style="padding: 10px 16px; border: 1px solid var(--border-light); border-radius: 999px; font-size: 13px; outline: none; width: 220px;" oninput="searchReqs()">
          <button class="btn-secondary" style="min-height: 40px; padding: 0 16px; font-size: 13px;" onclick="toggleAllReqs(true)">Expandir Todos</button>
          <button class="btn-secondary" style="min-height: 40px; padding: 0 16px; font-size: 13px;" onclick="toggleAllReqs(false)">Colapsar</button>
        </div>
      </div>

      <div class="req-accordion-grid" id="req-accordion-container">
        <!-- Module 1 -->
        <div class="req-card" id="req-card-1">
          <div class="req-card-header" onclick="toggleReqCard('req-card-1')">
            <span class="req-card-title">🖼️ Administrar Obras de Arte & Tipología</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">9 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
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

        <!-- Module 2 -->
        <div class="req-card" id="req-card-2">
          <div class="req-card-header" onclick="toggleReqCard('req-card-2')">
            <span class="req-card-title">🏛️ Administrar Salas de Exhibición</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">4 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
            </div>
          </div>
          <div class="req-card-body">
            <div class="req-item-row"><span class="req-code-badge">RF-10</span><span>Registrar sala</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-11</span><span>Consultar sala</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-12</span><span>Modificar sala</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-13</span><span>Registrar baja de sala</span></div>
          </div>
        </div>

        <!-- Module 3 -->
        <div class="req-card" id="req-card-3">
          <div class="req-card-header" onclick="toggleReqCard('req-card-3')">
            <span class="req-card-title">🎙️ Administrar Guías & Estilos de Obra</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">7 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
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

        <!-- Module 4 -->
        <div class="req-card" id="req-card-4">
          <div class="req-card-header" onclick="toggleReqCard('req-card-4')">
            <span class="req-card-title">⚠️ Tipos de Incidentes & Exposiciones</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">5 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
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

        <!-- Module 5 -->
        <div class="req-card" id="req-card-5">
          <div class="req-card-header" onclick="toggleReqCard('req-card-5')">
            <span class="req-card-title">🎟️ Visitas Guiadas & Venta de Entradas</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">6 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
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

        <!-- Module 6 -->
        <div class="req-card open" id="req-card-6" style="border-left: 3px solid var(--blue-accent);">
          <div class="req-card-header" onclick="toggleReqCard('req-card-6')">
            <span class="req-card-title" style="color: var(--blue-accent);">🛡️ Rondas e Incidentes (Proceso Crítico)</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-accent); color: #FFF; padding: 3px 8px; border-radius: 4px;">6 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
            </div>
          </div>
          <div class="req-card-body">
            <div class="req-item-row"><span class="req-code-badge">RF-32</span><span>Generar planificación de rondas de vigilancia</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-33</span><span>Consultar planificación de rondas de vigilancia</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-34</span><span>Registrar revisión de sala</span></div>
            <div class="req-item-row"><span class="req-code-badge" style="background: var(--blue-accent); color: #FFF;">RF-35</span><strong style="color: var(--blue-accent);">Registrar incidente (Disparador de CU-15)</strong></div>
            <div class="req-item-row"><span class="req-code-badge">RF-36</span><span>Consultar incidentes</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-37</span><span>Registrar seguimiento de resolución de incidente</span></div>
          </div>
        </div>

        <!-- Module 7 -->
        <div class="req-card" id="req-card-7">
          <div class="req-card-header" onclick="toggleReqCard('req-card-7')">
            <span class="req-card-title">🔄 Restauración, Informes & Sesión</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">7 RFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
            </div>
          </div>
          <div class="req-card-body">
            <div class="req-item-row"><span class="req-code-badge">RF-40</span><span>Registrar obra a restaurar</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-41</span><span>Registrar reingreso de obra (Aplica Regla RN1)</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-42</span><span>Generar informe diario de vigilancia</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-43</span><span>Generar reporte de patrones de incidentes</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-44</span><span>Emitir historial de incidentes</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-45</span><span>Iniciar sesión</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-46</span><span>Cerrar sesión</span></div>
            <div class="req-item-row"><span class="req-code-badge">RF-47</span><span>Modificar contraseña</span></div>
          </div>
        </div>

        <!-- Module 8 -->
        <div class="req-card" id="req-card-8">
          <div class="req-card-header" onclick="toggleReqCard('req-card-8')">
            <span class="req-card-title">📱 Requerimientos No Funcionales</span>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--navy-main); padding: 3px 8px; border-radius: 4px;">2 RNFs</span>
              <span class="req-card-arrow" style="font-size: 11px; color: var(--text-secondary); transition: transform 0.2s;">▼</span>
            </div>
          </div>
          <div class="req-card-body">
            <div class="req-item-row" style="flex-direction: column; align-items: flex-start; gap: 4px;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="req-code-badge">RNF-1</span>
                <strong>Módulo Web de Soporte</strong>
              </div>
              <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.4;">
                Arquitectura web cliente-servidor accesible desde navegadores modernos sin software cliente.
              </div>
            </div>
            <div class="req-item-row" style="flex-direction: column; align-items: flex-start; gap: 4px; border-bottom: none;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span class="req-code-badge">RNF-2</span>
                <strong>Interfaz Móvil para Rondas en Tablet</strong>
              </div>
              <div style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.4;">
                Interfaz responsiva y táctil adaptada para tablets de guardia en recorrido.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 8: DCU GENERAL (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 8: DCU GENERAL -->
    <div class="slide theme-light" id="slide-8" data-topic="08 · Casos de Uso" data-theme="light">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <div class="breadcrumb-tag">08 &bull; Vista Externa del Software &bull; Francisco Thomas Rapp</div>
          <h1 class="giant-title">Diagrama de Casos de Uso del Sistema (DCU)</h1>
          <p class="editorial-subtitle" style="margin-bottom: 12px;">
            Frontera del sistema, numeración continua correlativa del 1 al 42 y módulo de sesión 43 al 45.
          </p>
        </div>
        <button class="btn-primary" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso Completo')">
          Ampliar diagrama {svg_expand}
        </button>
      </div>

      <div class="expansive-diagram-grid">
        <div class="expansive-canvas-card">
          <div class="expansive-toolbar">
            <span style="font-size: 12px; font-weight: 700; color: var(--navy-deep); text-transform: uppercase;">
              Enfoque Rápido por Cuadrante:
            </span>
            <div class="preset-pill-group">
              <button class="preset-btn active" id="btn-dcu-all" onclick="focusDcu('all', this)">Ver Todo</button>
              <button class="preset-btn" id="btn-dcu-obras" onclick="focusDcu('obras', this)">Obras (1..9)</button>
              <button class="preset-btn" id="btn-dcu-incidentes" onclick="focusDcu('incidentes', this)">Rondas (13..24)</button>
              <button class="preset-btn" id="btn-dcu-entradas" onclick="focusDcu('entradas', this)">Entradas (10..12)</button>
              <button class="preset-btn" id="btn-dcu-admin" onclick="focusDcu('admin', this)">Admin (25..45)</button>
            </div>
          </div>
          <div class="expansive-canvas" id="dcu-canvas">
            <img id="slide-dcu-img" src="{b64_dcu}" alt="Diagrama de Casos de Uso">
          </div>
        </div>

        <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 12px;">
          <div class="card-light">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Consistencia Numérica 1..42</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
              Se unificó la secuencia correlativa del 1 al 42 en perfecta correspondencia con la especificación de objetivos de la cátedra, subsanando los desfases anteriores.
            </div>
          </div>

          <div class="card-light" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Núcleo Operativo del Guardia</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--navy-deep);">
              &bull; <strong>CU-13:</strong> Generar planificación de rondas<br>
              &bull; <strong>CU-14:</strong> Consultar planificación de rondas<br>
              &bull; <strong>CU-15:</strong> Registrar incidente (Caso de Estudio)<br>
              &bull; <strong>CU-16:</strong> Registrar revisión de la sala
            </div>
          </div>

          <div class="card-light">
            <div style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase; margin-bottom: 6px;">Frontera del Sistema (Boundary)</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
              Delimita estrictamente las transacciones dentro de la plataforma frente a los actores humanos y de soporte.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 9: ACTORES Y RELACIONES (THEME: DARK)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 9: ACTORES Y RELACIONES -->
    <div class="slide theme-dark" id="slide-9" data-topic="09 · Actores y Relaciones" data-theme="dark">
      <div class="breadcrumb-tag">09 &bull; Arquitectura de Casos de Uso &bull; Francisco Thomas Rapp</div>
      <h1 class="giant-title">Actores del Sistema y Dependencias UML</h1>
      <p class="editorial-subtitle">
        Fundamentación de los 8 actores y las relaciones formales «extend» e «include».
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 8px;">Actores Principales del Dominio</div>
          <div style="font-size: 14.5px; line-height: 1.6; color: var(--text-light-secondary);">
            &bull; <strong style="color:#FFF;">Responsable de Ingreso de Obras:</strong> Registra altas, reingresos y derivaciones a taller.<br>
            &bull; <strong style="color:#FFF;">Administrador del Museo:</strong> Planifica exhibiciones y autoriza bajas de piezas.<br>
            &bull; <strong style="color:#FFF;">Responsable de Atención al Cliente:</strong> Venta de entradas y contratación de guías.<br>
            &bull; <strong style="color:#FFF;">Encargado de Vigilancia (EV):</strong> Rondas, revisión de salas y reporte de siniestros.<br>
            &bull; <strong style="color:#FFF;">Encargado de Supervisión:</strong> Informes consolidados y patrones de incidentes.<br>
            &bull; <strong style="color:#FFF;">Admin del Sistema / Usuario:</strong> Parámetros de catálogos y seguridad de sesión.
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;">Relación &laquo;extend&raquo; (Condicional)</span>
              <span style="font-size: 11px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">CU-15 &rarr; CU-16</span>
            </div>
            <div style="font-size: 14.5px; line-height: 1.55; color: var(--text-light-secondary);">
              <strong style="color:#FFF;">Registrar incidente &rarr; Registrar revisión de la sala:</strong><br>
              El guardia siempre realiza la revisión de sala (caso base). La registración del incidente es una extensión condicional que únicamente se dispara cuando se constata un desperfecto físico en alguna obra.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-ice);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: var(--blue-ice); text-transform: uppercase;">Relación &laquo;include&raquo; (Mandatoria)</span>
              <span style="font-size: 11px; font-weight: 700; background: rgba(255, 255, 255, 0.1); color: var(--text-light); padding: 3px 8px; border-radius: 4px;">CU-11 &rarr; CU-12</span>
            </div>
            <div style="font-size: 14.5px; line-height: 1.55; color: var(--text-light-secondary);">
              <strong style="color:#FFF;">Contratar servicio de guía &rarr; Consultar agenda de guías:</strong><br>
              Es técnicamente imposible contratar un servicio de guía sin antes comprobar e incluir obligatoriamente la disponibilidad horaria del personal calificado.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 10: PLANTILLA CU-15 (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 10: PLANTILLA CU-15 -->
    <div class="slide theme-light" id="slide-10" data-topic="10 · Plantilla CU-15" data-theme="light">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <div class="breadcrumb-tag">10 &bull; Especificación Formal &bull; Lucas Moyano</div>
          <h1 class="giant-title">Especificación Interactiva: Registrar Incidente (CU-15)</h1>
          <p class="editorial-subtitle" style="margin-bottom: 12px;">
            Plantilla formal de 14 pasos, no ambigüedad en Paso 4 y cursos alternativos.
          </p>
        </div>
        <div style="display: flex; gap: 8px;">
          <button class="btn-primary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="showNormalCourse()">Curso Normal (14 Pasos)</button>
          <button class="btn-secondary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="showAltCourses()">Cursos Alternativos</button>
        </div>
      </div>

      <div class="step-explorer-grid">
        <div class="steps-list-container" id="steps-container"></div>

        <div class="step-detail-viewer">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border-light); padding-bottom: 12px; margin-bottom: 14px;">
              <div style="font-size: 18px; font-weight: 700; color: var(--navy-deep);" id="detail-step-title">Paso 1: Solicitud de Reporte</div>
              <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 4px 10px; border-radius: 999px;" id="detail-step-actor">Encargado de Vigilancia</span>
            </div>
            <div style="font-size: 15px; line-height: 1.6; color: var(--navy-deep); margin-bottom: 16px;" id="detail-step-desc">
              El Encargado de Vigilancia ingresa a la opción 'Reportar incidente' desde la interfaz táctil de la tablet durante el recorrido por la sala.
            </div>
            <div style="background: var(--blue-ice-light); border: 1px solid var(--border-light); border-radius: 12px; padding: 16px; margin-bottom: 16px;" id="detail-step-payload">
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--navy-main); margin-bottom: 6px;">Datos / Estado en este paso:</div>
              <div style="font-size: 13.5px; color: var(--navy-deep); line-height: 1.5;" id="detail-step-data">
                Precondición activa: Guardia autenticado en el Módulo Web de Soporte y sala de ronda seleccionada.
              </div>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid var(--border-light); padding-top: 14px;">
            <button class="btn-secondary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="prevStep()">Paso Anterior</button>
            <span style="font-size: 13px; font-weight: 700; color: var(--blue-accent); font-family: monospace;" id="step-progress-label">Paso 1 de 14</span>
            <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="nextStep()">Siguiente Paso</button>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 11: PROTOTIPO DE PANTALLA (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 11: PROTOTIPO DE PANTALLA -->
    <div class="slide theme-light" id="slide-11" data-topic="11 · Prototipo UI" data-theme="light">
      <div class="breadcrumb-tag">11 &bull; Interfaz de Usuario &bull; Kevin Pereyra</div>
      <h1 class="giant-title">Prototipo de Pantalla: Módulo Web en Tablet</h1>
      <p class="editorial-subtitle">
        Diseño ergonómico táctil para el guardia y correspondencia con los pasos del CU-15.
      </p>

      <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean reveal-item revealed">
          <img src="{b64_proto}" class="diagram-preview-img" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')" alt="Prototipo Tablet">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: var(--text-secondary);">Mockup Tablet Responsivo</span>
            <button class="btn-primary" style="min-height: 44px; padding: 0 20px; font-size: 14px;" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
              Ampliar mockup {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 12px;">
          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">1. Entrada Numérica Rápida (Pasos 2-3)</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-secondary);">
              Campo táctil de entrada numérica con foco automático para el código de la obra (ej: <code>OBJ-408</code>).
            </div>
          </div>

          <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">2. Verificación Visual sin Ambigüedad (Paso 4)</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--navy-deep);">
              Despliega de inmediato: <strong>Título de la Obra, Sala Asignada y Ubicación Física dentro de la Sala</strong>.
            </div>
          </div>

          <div class="card-light reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase; margin-bottom: 4px;">3. Tipificación y Sellado (Pasos 7-12)</div>
            <div style="font-size: 14px; line-height: 1.5; color: var(--text-secondary);">
              Selector táctil de daño (Deterioro natural, provocado, caída), hora del servidor y botones táctiles de confirmación.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 12: DIAGRAMA DE CLASES (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 12: DIAGRAMA DE CLASES -->
    <div class="slide theme-light" id="slide-12" data-topic="12 · Clases del Dominio" data-theme="light">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <div class="breadcrumb-tag">12 &bull; Vista Interna Orientada a Objetos &bull; Juan Tarditti</div>
          <h1 class="giant-title">Diagrama de Clases del Dominio (DCD)</h1>
          <p class="editorial-subtitle" style="margin-bottom: 12px;">
            Arquitectura estática orientada a objetos para la gestión de incidentes y rondas.
          </p>
        </div>
        <button class="btn-primary" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
          Ampliar diagrama {svg_expand}
        </button>
      </div>

      <div class="expansive-diagram-grid">
        <div class="expansive-canvas-card">
          <div class="expansive-toolbar">
            <span style="font-size: 12px; font-weight: 700; color: var(--navy-deep); text-transform: uppercase;">
              Enfoque por Clúster de Clases:
            </span>
            <div class="preset-pill-group">
              <button class="preset-btn active" id="btn-dcd-all" onclick="focusDcd('all', this)">Ver Todo</button>
              <button class="preset-btn" id="btn-dcd-inc" onclick="focusDcd('incidente', this)">Incidente & Tipo (1)</button>
              <button class="preset-btn" id="btn-dcd-sala" onclick="focusDcd('sala', this)">Sala & Guardias (1..*)</button>
              <button class="preset-btn" id="btn-dcd-obra" onclick="focusDcd('obra', this)">Obra & Estado</button>
            </div>
          </div>
          <div class="expansive-canvas" id="dcd-canvas">
            <img id="slide-dcd-img" src="{b64_dcd}" alt="Diagrama de Clases">
          </div>
        </div>

        <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 12px;">
          <div class="card-light">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Entidades Centrales del Dominio</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-secondary);">
              &bull; <strong>Incidente:</strong> Instancia transaccional con fecha, hora y tipología.<br>
              &bull; <strong>TipoIncidente:</strong> Clasificador tipológico.<br>
              &bull; <strong>ObraDeArte:</strong> Entidad patrimonial con puntero a Estado.<br>
              &bull; <strong>Sala, Guardia & SalaXGuardia:</strong> Modelo asociativo temporal.
            </div>
          </div>

          <div class="card-light" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Encapsulamiento y Métodos</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--navy-deep);">
              Operaciones completas modeladas:<br>
              <code>buscarObraPorCodigo()</code><br>
              <code>actualizarEstado("Inactivo")</code><br>
              <code>registrarIncidente()</code>
            </div>
          </div>
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 13: MULTIPLICIDADES (THEME: LIGHT)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 13: MULTIPLICIDADES -->
    <div class="slide theme-light" id="slide-13" data-topic="13 · Multiplicidades" data-theme="light">
      <div class="breadcrumb-tag">13 &bull; Integridad Estructural del DCD &bull; Juan Tarditti</div>
      <h1 class="giant-title">Multiplicidades y Consistencia en el DCD</h1>
      <p class="editorial-subtitle">
        Resolución exhaustiva de las observaciones de cátedra sobre asociaciones del modelo.
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 20px;">
        <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent); background: #FAFCFF;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;">Asociación 1</span>
            <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">Incidente &rarr; (1) TipoIncidente</span>
          </div>
          <div style="font-size: 17px; font-weight: 700; color: var(--navy-deep); margin-bottom: 6px;">Multiplicidad Unívoca Obligatoria</div>
          <div style="font-size: 14px; line-height: 1.6; color: var(--text-secondary);">
            Cada objeto de la clase <code>Incidente</code> está inexcusablemente asociado a <strong>exactamente un (1)</strong> <code>TipoIncidente</code>. No se admiten siniestros anónimos; esto garantiza la integridad requerida para los reportes estadísticos y el cómputo de patrones.
          </div>
        </div>

        <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--navy-main); background: #FAFCFF;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--navy-main); text-transform: uppercase;">Asociación 2</span>
            <span style="font-size: 11px; font-weight: 700; background: var(--blue-ice); color: var(--navy-main); padding: 3px 8px; border-radius: 4px;">Sala &rarr; (1..*) SalaXGuardia</span>
          </div>
          <div style="font-size: 17px; font-weight: 700; color: var(--navy-deep); margin-bottom: 6px;">Historial Temporal de Rondas</div>
          <div style="font-size: 14px; line-height: 1.6; color: var(--text-secondary);">
            La relación muchos a muchos entre <code>Sala</code> y <code>Guardia</code> está descompuesta mediante la clase asociativa <code>SalaXGuardia</code>. Una sala tiene a lo largo del tiempo <strong>múltiples (1..*) asignaciones</strong>, preservando qué guardia estuvo a cargo en cada turno.
          </div>
        </div>
      </div>

      <div class="card-light reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
        <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Patrón de Transición de Estado de la Obra</div>
        <div style="font-size: 14.5px; line-height: 1.6; color: var(--navy-deep);">
          Al ejecutarse el método <code>registrarIncidente()</code>, el controlador de caso de uso invoca <code>obra.setEstado("Inactivo")</code>. La pieza queda inhabilitada de inmediato para exhibición hasta que la curaduría autorice su derivación a depósito o taller.
        </div>
      </div>
    </div>
''')

    # ========================================================
    # SLIDE 14: TRAZABILIDAD & CIERRE (THEME: DARK)
    # ========================================================
    out.write(f'''
    <!-- SLIDE 14: TRAZABILIDAD & CIERRE -->
    <div class="slide theme-dark" id="slide-14" data-topic="14 · Trazabilidad y Cierre" data-theme="dark">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px;">
        <div>
          <div class="breadcrumb-tag">14 &bull; Trazabilidad de Punta a Punta &bull; Kevin Pereyra &bull; Tobias Molina</div>
          <h1 class="giant-title">Trazabilidad Integral N a M y Conclusión</h1>
          <p class="editorial-subtitle" style="margin-bottom: 14px;">
            Selecciona un requerimiento para explorar su correspondencia analítica con Casos de Uso, Reglas y Clases.
          </p>
        </div>
        <button class="btn-primary" onclick="goToSlide(1)">
          Volver al inicio {svg_arrow_right}
        </button>
      </div>

      <div class="trace-console-grid" style="margin-bottom: 24px;">
        <div>
          <div style="display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap;">
            <button class="btn-secondary" style="min-height: 36px; padding: 0 14px; font-size: 12px;" onclick="filterTrace('todos', this)">Todos</button>
            <button class="btn-secondary" style="min-height: 36px; padding: 0 14px; font-size: 12px;" onclick="filterTrace('rondas', this)">Vigilancia</button>
            <button class="btn-secondary" style="min-height: 36px; padding: 0 14px; font-size: 12px;" onclick="filterTrace('obras', this)">Obras</button>
            <button class="btn-secondary" style="min-height: 36px; padding: 0 14px; font-size: 12px;" onclick="filterTrace('visitas', this)">Visitas</button>
          </div>
          <div class="trace-rf-list" id="trace-rf-container"></div>
        </div>

        <div class="trace-impact-dossier">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-dark); padding-bottom: 10px;">
            <div>
              <div style="font-size: 11px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;" id="trace-cat-tag">Vigilancia & Incidentes</div>
              <div style="font-size: 17px; font-weight: 700; color: #FFF;" id="trace-rf-title">RF-35: Registrar incidente</div>
            </div>
            <span style="font-size: 11px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: var(--blue-accent); padding: 4px 10px; border-radius: 999px;" id="trace-mapping-badge">Mapeo N a M</span>
          </div>

          <div>
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-light-secondary); margin-bottom: 4px;">Casos de Uso Vinculados:</div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;" id="trace-cu-group">
              <span style="font-size: 11.5px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: #FFF; padding: 3px 8px; border-radius: 4px;">CU-15 Registrar incidente</span>
              <span style="font-size: 11.5px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: #FFF; padding: 3px 8px; border-radius: 4px;">CU-16 Registrar revisión de sala</span>
            </div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div>
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-light-secondary); margin-bottom: 4px;">Regla de Negocio:</div>
              <div style="font-size: 13px; font-weight: 600; color: #FFF;" id="trace-rule-group">RN2: Registro Inmediato</div>
            </div>
            <div>
              <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-light-secondary); margin-bottom: 4px;">Interfaz / Pantalla:</div>
              <div style="font-size: 13px; font-weight: 600; color: var(--blue-accent);" id="trace-ui-label">Módulo Web Tablet (Reporte)</div>
            </div>
          </div>

          <div>
            <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-light-secondary); margin-bottom: 4px;">Clases del Dominio Impactadas:</div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;" id="trace-class-group">
              <span style="font-size: 11.5px; font-family: monospace; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 3px 8px; border-radius: 4px;">Incidente</span>
              <span style="font-size: 11.5px; font-family: monospace; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 3px 8px; border-radius: 4px;">TipoIncidente</span>
              <span style="font-size: 11.5px; font-family: monospace; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 3px 8px; border-radius: 4px;">ObraDeArte</span>
            </div>
          </div>

          <div style="background: rgba(0, 0, 0, 0.25); border-left: 3px solid var(--blue-accent); border-radius: 8px; padding: 12px;">
            <div style="font-size: 11px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Justificación de Consistencia:</div>
            <div style="font-size: 13px; line-height: 1.5; color: var(--text-light);" id="trace-justification">
              El requerimiento se satisface transaccionalmente en el CU-15 cuando el guardia reporta el daño en sala, alterando el estado de la obra en memoria y persistiéndolo con sello temporal del servidor.
            </div>
          </div>
        </div>
      </div>

      <!-- Closing Banner -->
      <div class="card-dark" style="text-align: center; padding: 32px; border-color: var(--blue-accent);">
        <h2 style="font-size: 24px; font-weight: 700; color: #FFF; margin-bottom: 8px;">¡Muchas Gracias por su Atención!</h2>
        <p style="font-size: 15px; color: var(--text-light-secondary); margin-bottom: 16px;">
          Quedamos a disposición de los profesores y del ayudante de cátedra para preguntas.
        </p>
        <div style="display: flex; gap: 10px; justify-content: center;">
          <span style="font-size: 12px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: var(--blue-accent); padding: 4px 12px; border-radius: 999px;">UTN FRC</span>
          <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 4px 12px; border-radius: 999px;">ASI 2K10</span>
          <span style="font-size: 12px; font-weight: 700; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 4px 12px; border-radius: 999px;">Grupo 6</span>
        </div>
      </div>
    </div>
''')

    # Close main
    out.write('  </main>\n')

    # Floating Bottom Dock
    out.write(f'''
  <!-- Fixed Floating Bottom Dock -->
  <div class="dock-container" id="floating-dock">
    <button class="btn-secondary" id="dock-btn-prev" onclick="prevSlideAction()" title="Slide anterior (←)">
      {svg_arrow_left} Anterior
    </button>

    <div class="dock-counter" id="dock-counter-text">01 / 14</div>

    <button class="btn-primary" id="dock-btn-next" onclick="nextSlideAction()" title="Avanzar (→ o Espacio)">
      Siguiente {svg_arrow_right}
    </button>

    <div class="dock-divider"></div>

    <button class="btn-secondary" onclick="openOverviewModal()" title="Ver los 14 slides (O)">
      {svg_grid} Vista general
    </button>

    <button class="btn-secondary" onclick="toggleFullscreen()" title="Pantalla completa (F o F11)">
      {svg_fullscreen} Pantalla completa
    </button>

    <button class="btn-secondary" onclick="revealAllInCurrentSlide()" title="Mostrar todo en el slide actual (A)">
      {svg_eye} Mostrar todo
    </button>

    <button class="btn-secondary" style="padding: 0; width: 44px; min-width: 44px; border-radius: 50%; justify-content: center;" onclick="openTutorialModal()" title="Cómo usar la presentación (?)">
      {svg_help}
    </button>
  </div>
''')

    # Zoom Fullscreen Modal
    out.write(f'''
  <!-- Fullscreen Zoom Modal -->
  <div class="zoom-fullscreen-modal" id="zoom-fullscreen-modal">
    <div class="zoom-modal-top">
      <div class="zoom-modal-title">
        <span style="font-size: 12px; font-weight: 700; background: var(--blue-accent); color: #FFF; padding: 4px 10px; border-radius: 999px;">HD</span>
        <span id="zoom-modal-title-text">Diagrama en Alta Resolución</span>
      </div>
      <button class="btn-secondary" onclick="closeZoomModal()" style="border-color: rgba(255,255,255,0.3);" title="Cerrar (Esc)">
        Cerrar {svg_close}
      </button>
    </div>

    <div class="zoom-viewport-stage" id="zoom-stage">
      <div class="zoom-stage-content" id="zoom-stage-content">
        <img id="zoom-modal-img" src="" alt="Diagrama en Detalle">
      </div>
    </div>

    <div class="zoom-controls-floating">
      <button class="zoom-btn" onclick="modalZoomIn()" title="Acercar (+)">
        {svg_plus} Acercar
      </button>
      <button class="zoom-btn" onclick="modalZoomOut()" title="Alejar (−)">
        {svg_minus} Alejar
      </button>
      <span style="font-size: 13px; font-weight: 700; color: #FFF; min-width: 55px; text-align: center; font-family: monospace;" id="zoom-level-text">100%</span>
      <button class="zoom-btn" onclick="modalResetZoom()" title="Ajustar a pantalla">
        {svg_fit} Ajustar
      </button>
      <button class="zoom-btn" onclick="closeZoomModal()" style="background: rgba(255,255,255,0.15);" title="Cerrar (Esc)">
        {svg_close} Cerrar
      </button>
    </div>
  </div>
''')

    # Overview Grid Modal
    out.write(f'''
  <!-- Overview Grid Modal -->
  <div class="overview-modal" id="overview-modal">
    <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin: 0 auto; width: 100%;">
      <div>
        <div class="breadcrumb-tag">Navegación Rápida</div>
        <h2 style="font-size: 28px; font-weight: 700; color: #FFF;">Vista General de la Presentación &bull; 14 Slides</h2>
      </div>
      <button class="btn-primary" onclick="closeOverviewModal()">
        Cerrar vista {svg_close}
      </button>
    </div>
    <div class="overview-grid" id="overview-grid-container"></div>
  </div>
''')

    # Initial Onboarding Tutorial Modal
    out.write(f'''
  <!-- Onboarding Mini-Tutorial Modal -->
  <div class="tutorial-modal" id="tutorial-modal">
    <div class="tutorial-card-body">
      <div class="breadcrumb-tag">Guía Rápida de Uso</div>
      <h3 style="font-size: 24px; font-weight: 700; color: var(--navy-deep); margin-bottom: 12px;">Cómo navegar la defensa</h3>
      <p style="font-size: 15px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 24px;">
        Esta presentación interactiva está diseñada para explorarse con total fluidez mediante clics o atajos de teclado:
      </p>

      <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 28px;">
        <div style="display: flex; align-items: flex-start; gap: 14px;">
          <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--blue-accent); color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0;">1</div>
          <div style="font-size: 14.5px; line-height: 1.5; color: var(--navy-deep);">
            <strong>Avanzá a tu ritmo:</strong> Tocá el botón grande <span style="color: var(--blue-accent); font-weight: 700;">Siguiente →</span> o usá las flechas del teclado / barra espaciadora.
          </div>
        </div>

        <div style="display: flex; align-items: flex-start; gap: 14px;">
          <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--blue-accent); color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0;">2</div>
          <div style="font-size: 14.5px; line-height: 1.5; color: var(--navy-deep);">
            <strong>Abrir y Zoomear:</strong> Hacé click en cualquier tarjeta con <span style="color: var(--blue-accent); font-weight: 700;">+</span> para ver su detalle, o tocá <span style="color: var(--blue-accent); font-weight: 700;">Ampliar ↗</span> en un diagrama para hacer zoom interactivo.
          </div>
        </div>

        <div style="display: flex; align-items: flex-start; gap: 14px;">
          <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--blue-accent); color: #FFF; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0;">3</div>
          <div style="font-size: 14.5px; line-height: 1.5; color: var(--navy-deep);">
            <strong>Saltá a cualquier slide:</strong> Abrí la <span style="color: var(--blue-accent); font-weight: 700;">Vista general</span> en la barra inferior (o presioná la tecla <kbd>O</kbd>) para elegir cualquier diapositiva.
          </div>
        </div>
      </div>

      <button class="btn-primary" style="width: 100%;" onclick="closeTutorialModal()">
        Entendido, comenzar presentación {svg_arrow_right}
      </button>
    </div>
  </div>
''')

    # JavaScript Controller
    out.write(f'''
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
    const totalSlides = 14;

    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Contexto y Objetivos",
      "03 · Mapa de Procesos",
      "04 · Proceso Crítico y Reglas",
      "05 · BPMN Descriptivo",
      "06 · BPMN Operativo",
      "07 · Requerimientos",
      "08 · Casos de Uso",
      "09 · Actores y Relaciones",
      "10 · Plantilla CU-15",
      "11 · Prototipo UI",
      "12 · Clases del Dominio",
      "13 · Multiplicidades",
      "14 · Trazabilidad y Cierre"
    ];

    function updateSlide() {{
      for (let i = 1; i <= totalSlides; i++) {{
        const el = document.getElementById('slide-' + i);
        if (el) {{
          if (i === currentSlide) {{
            el.classList.add('active');
            const theme = el.getAttribute('data-theme') || 'dark';
            if (theme === 'light') {{
              document.body.classList.add('theme-light');
            }} else {{
              document.body.classList.remove('theme-light');
            }}
          }} else {{
            el.classList.remove('active');
          }}
        }}
      }}

      // Format slide string 01 / 14
      const formatted = (currentSlide < 10 ? '0' : '') + currentSlide + ' / ' + (totalSlides < 10 ? '0' : '') + totalSlides;
      document.getElementById('header-slide-num').innerText = formatted;
      document.getElementById('dock-counter-text').innerText = formatted;

      document.getElementById('dock-btn-prev').disabled = (currentSlide === 1);
      document.getElementById('dock-btn-next').disabled = (currentSlide === totalSlides);

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
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
        closeOverviewModal();
      }}
    }}

    // Progressive Reveal
    function nextSlideAction() {{
      const currentEl = document.getElementById('slide-' + currentSlide);
      if (currentEl) {{
        const unrevealed = currentEl.querySelectorAll('.reveal-item:not(.revealed)');
        if (unrevealed.length > 0) {{
          unrevealed[0].classList.add('revealed');
          return;
        }}
      }}
      nextSlide();
    }}

    function prevSlideAction() {{
      const currentEl = document.getElementById('slide-' + currentSlide);
      if (currentEl) {{
        const revealed = currentEl.querySelectorAll('.reveal-item.revealed');
        if (revealed.length > 0) {{
          revealed[revealed.length - 1].classList.remove('revealed');
          return;
        }}
      }}
      prevSlide();
    }}

    function revealAllInCurrentSlide() {{
      const currentEl = document.getElementById('slide-' + currentSlide);
      if (currentEl) {{
        currentEl.querySelectorAll('.reveal-item').forEach(el => el.classList.add('revealed'));
      }}
    }}

    // Fullscreen toggle
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    // Expandable cards
    function toggleExpandCard(cardEl) {{
      cardEl.classList.toggle('expanded');
    }}

    // Requerimientos Accordion
    function toggleReqCard(id) {{
      const c = document.getElementById(id);
      if (c) c.classList.toggle('open');
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

    // Expansive Presets Focus for DCU
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

    // Expansive Presets Focus for DCD
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

    // Fullscreen Zoom Modal Logic
    let modalScale = 1;
    let modalTranslateX = 0;
    let modalTranslateY = 0;
    let isModalDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;

    const zoomModal = document.getElementById('zoom-fullscreen-modal');
    const zoomStage = document.getElementById('zoom-stage');
    const zoomContent = document.getElementById('zoom-stage-content');
    const zoomImg = document.getElementById('zoom-modal-img');
    const zoomTitle = document.getElementById('zoom-modal-title-text');
    const zoomLevelText = document.getElementById('zoom-level-text');

    function applyModalTransform() {{
      zoomContent.style.transform = `translate(${{modalTranslateX}}px, ${{modalTranslateY}}px) scale(${{modalScale}})`;
      zoomLevelText.innerText = Math.round(modalScale * 100) + '%';
    }}

    function openZoomModal(assetKey, title) {{
      if (assets[assetKey]) {{
        zoomImg.src = assets[assetKey];
        zoomTitle.innerText = title;
        zoomModal.classList.add('active');
        modalResetZoom();
      }}
    }}

    function closeZoomModal() {{
      zoomModal.classList.remove('active');
    }}

    function modalZoomIn() {{
      modalScale = Math.min(modalScale * 1.3, 5);
      applyModalTransform();
    }}

    function modalZoomOut() {{
      modalScale = Math.max(modalScale / 1.3, 0.4);
      applyModalTransform();
    }}

    function modalResetZoom() {{
      modalScale = 1;
      modalTranslateX = 0;
      modalTranslateY = 0;
      applyModalTransform();
    }}

    zoomStage.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY > 0 ? 0.85 : 1.18;
      modalScale = Math.min(Math.max(modalScale * delta, 0.4), 6);
      applyModalTransform();
    }}, {{ passive: false }});

    zoomStage.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;
      isModalDragging = true;
      zoomStage.classList.add('dragging');
      dragStartX = e.clientX - modalTranslateX;
      dragStartY = e.clientY - modalTranslateY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isModalDragging) return;
      modalTranslateX = e.clientX - dragStartX;
      modalTranslateY = e.clientY - dragStartY;
      applyModalTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isModalDragging = false;
      zoomStage.classList.remove('dragging');
    }});

    // Double click to toggle 100% and 200%
    zoomStage.addEventListener('dblclick', () => {{
      if (modalScale > 1.2) {{
        modalResetZoom();
      }} else {{
        modalScale = 2;
        applyModalTransform();
      }}
    }});

    // Overview Grid Modal
    const overviewModal = document.getElementById('overview-modal');
    function openOverviewModal() {{
      buildOverviewGrid();
      overviewModal.classList.add('active');
    }}

    function closeOverviewModal() {{
      overviewModal.classList.remove('active');
    }}

    function buildOverviewGrid() {{
      const container = document.getElementById('overview-grid-container');
      container.innerHTML = '';
      slideTitles.forEach((title, idx) => {{
        const card = document.createElement('div');
        const num = idx + 1;
        card.className = 'overview-card-item' + (num === currentSlide ? ' current' : '');
        card.onclick = () => goToSlide(num);
        card.innerHTML = `
          <div style="font-family: monospace; font-size: 13px; font-weight: 700; color: var(--blue-accent);">SLIDE ${{num < 10 ? '0' : ''}}${{num}}</div>
          <div style="font-size: 15px; font-weight: 700; color: #FFF; line-height: 1.3;">${{title.split(' · ')[1] || title}}</div>
          <div style="font-size: 12px; color: var(--text-light-secondary);">${{num === currentSlide ? '● Actual' : 'Ir al slide →'}}</div>
        `;
        container.appendChild(card);
      }});
    }}

    // Tutorial Modal
    const tutorialModal = document.getElementById('tutorial-modal');
    function openTutorialModal() {{
      tutorialModal.classList.add('active');
    }}
    function closeTutorialModal() {{
      tutorialModal.classList.remove('active');
    }}

    // Auto-dimming Dock
    let dockTimeout;
    const dock = document.getElementById('floating-dock');
    function resetDockTimer() {{
      dock.classList.remove('dimmed');
      clearTimeout(dockTimeout);
      dockTimeout = setTimeout(() => {{
        dock.classList.add('dimmed');
      }}, 3500);
    }}
    window.addEventListener('mousemove', resetDockTimer);
    window.addEventListener('keydown', resetDockTimer);
    resetDockTimer();

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
      if (zoomModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeZoomModal();
        else if (e.key === '+' || e.key === '=') modalZoomIn();
        else if (e.key === '-' || e.key === '_') modalZoomOut();
        else if (e.key === '0' || e.key === 'r') modalResetZoom();
        return;
      }}

      if (overviewModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeOverviewModal();
        return;
      }}

      if (tutorialModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeTutorialModal();
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        nextSlideAction();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlideAction();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        goToSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        goToSlide(totalSlides);
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'o' || e.key === 'O') {{
        openOverviewModal();
      }} else if (e.key === 'a' || e.key === 'A') {{
        revealAllInCurrentSlide();
      }} else if (e.key === '?') {{
        openTutorialModal();
      }}
    }});

    // ==========================================
    // CU-15 STEP EXPLORER DATA & CONTROLLER
    // ==========================================
    const cu15Steps = [
      {{ num: 1, title: "Paso 1: Solicitud de Reporte", actor: "Encargado de Vigilancia", desc: "El Encargado de Vigilancia ingresa a la opción 'Reportar incidente' desde la interfaz táctil de la tablet durante el recorrido por la sala.", data: "Precondición activa: Guardia autenticado en el Módulo Web de Soporte y sala de ronda seleccionada." }},
      {{ num: 2, title: "Paso 2: Solicitud de Código de Obra", actor: "Sistema Central", desc: "El sistema despliega el campo de entrada táctil y solicita al guardia que ingrese o escanee el código de identificación de la pieza involucrada.", data: "Control de foco: input de código habilitado con teclado numérico." }},
      {{ num: 3, title: "Paso 3: Ingreso del Código", actor: "Encargado de Vigilancia", desc: "El guardia ingresa el código de inventario de la obra afectada (ejemplo: 'OBJ-408').", data: "Parámetro enviado: codigoObra = 'OBJ-408'." }},
      {{ num: 4, title: "Paso 4: Búsqueda y Despliegue de Datos", actor: "Sistema Central", desc: "El sistema busca la obra por el código ingresado y muestra de forma explícita sus datos de identificación para certificación visual.", data: "DATOS MOSTRADOS SIN AMBIGÜEDAD (Exigencia de Cátedra):\\n• Título de la Obra: 'Fósil de Smilodon Populator'\\n• Sala Asignada: 'Sala C - Paleontología'\\n• Ubicación Física: 'Vitrina Central, Sector Norte'\\n• Estado actual: 'En Exhibición'" }},
      {{ num: 5, title: "Paso 5: Solicitud de Confirmación", actor: "Sistema Central", desc: "El sistema solicita al guardia que corrobore visualmente si la pieza hallada en la base de datos se corresponde con la obra dañada frente a él.", data: "Interfaz: Botones táctiles 'Confirmar Pieza' y 'Cancelar'." }},
      {{ num: 6, title: "Paso 6: Confirmación del Objeto", actor: "Encargado de Vigilancia", desc: "El guardia verifica los datos en pantalla y confirma que el objeto es el correcto.", data: "Evento: objetoConfirmado = true." }},
      {{ num: 7, title: "Paso 7: Solicitud de Tipo de Incidente", actor: "Sistema Central", desc: "El sistema despliega el listado tipológico normalizado: Deterioro natural, Deterioro provocado o Caída accidental.", data: "Catálogo recuperado de la clase TipoIncidente." }},
      {{ num: 8, title: "Paso 8: Selección de Tipología", actor: "Encargado de Vigilancia", desc: "El guardia selecciona el tipo de daño constatado en la sala (ejemplo: 'Caída accidental').", data: "Selección: idTipoIncidente = 3 ('Caída accidental')." }},
      {{ num: 9, title: "Paso 9: Pantalla de Revisión Final", actor: "Sistema Central", desc: "El sistema muestra el resumen consolidado del incidente: sala/ubicación, obra involucrada, tipo de daño seleccionado, hora actual del servidor y nuevo estado previsto.", data: "Resumen pre-grabación: Hora servidor = '15:42:18' & Nuevo Estado = 'Inactivo'." }},
      {{ num: 10, title: "Paso 10: Solicitud de Confirmación Final", actor: "Sistema Central", desc: "El sistema solicita la confirmación definitiva para impactar la bitácora electrónica y bloquear la pieza.", data: "Diálogo modal: '¿Confirma el registro del incidente patrimonial?'" }},
      {{ num: 11, title: "Paso 11: Confirmación Final", actor: "Encargado de Vigilancia", desc: "El guardia confirma el registro final del incidente.", data: "Confirmación aprobada por el guardia." }},
      {{ num: 12, title: "Paso 12: Registro Persistente de Incidente", actor: "Sistema Central", desc: "El sistema instancia el objeto Incidente vinculado a la sala, la obra, el TipoIncidente (multiplicidad 1) y la hora actual provista por el servidor.", data: "Persistencia en base de datos: Incidente registrado con id correlativo." }},
      {{ num: 13, title: "Paso 13: Inactivación de la Obra", actor: "Sistema Central", desc: "El sistema actualiza el estado de la obra a 'Inactivo', retirándola de los catálogos de exhibición pública para su posterior peritaje.", data: "Invocación orientada a objetos: obra.setEstado('Inactivo')." }},
      {{ num: 14, title: "Paso 14: Fin del Caso de Uso", actor: "Sistema Central", desc: "Se emite el mensaje de éxito en la tablet del guardia y se retorna al menú de ronda de vigilancia.", data: "Postcondición de Éxito cumplida satisfactoriamente." }}
    ];

    let currentStepIdx = 0;

    function renderStepsList() {{
      const container = document.getElementById('steps-container');
      if (!container) return;
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
      document.getElementById('detail-step-actor').innerText = s.actor;
      document.getElementById('detail-step-desc').innerText = s.desc;
      document.getElementById('detail-step-data').innerText = s.data;
      document.getElementById('step-progress-label').innerText = `Paso ${{s.num}} de ${{cu15Steps.length}}`;
      renderStepsList();
    }}

    function nextStep() {{
      if (currentStepIdx < cu15Steps.length - 1) selectStep(currentStepIdx + 1);
    }}

    function prevStep() {{
      if (currentStepIdx > 0) selectStep(currentStepIdx - 1);
    }}

    function showNormalCourse() {{
      selectStep(0);
    }}

    function showAltCourses() {{
      document.getElementById('detail-step-title').innerText = "Cursos Alternativos Formales";
      document.getElementById('detail-step-actor').innerText = "Excepciones de Flujo";
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
      {{ id: "RF-35", cat: "rondas", catName: "Vigilancia & Incidentes", name: "Registrar incidente en sala", cus: ["CU-15 Registrar incidente", "CU-16 Registrar revisión de la sala"], mapping: "N a M (Extensión Condicional)", rule: "RN2: Registro Inmediato", ui: "Tablet Móvil - Pantalla de Reporte", classes: ["Incidente", "TipoIncidente", "ObraDeArte", "SalaXGuardia"], just: "El guardia registra el incidente en la tablet en el momento del hallazgo. Se modela como extensión condicional (<<extend>>) sobre la revisión de sala; no todo chequeo genera un incidente." }},
      {{ id: "RF-36", cat: "rondas", catName: "Vigilancia & Incidentes", name: "Consultar incidentes registrados", cus: ["CU-18 Consultar incidente", "CU-23 Emitir historial de incidentes"], mapping: "N a M (Requerimiento Transversal)", rule: "Auditoría Interna", ui: "Módulo Web - Panel de Supervisión", classes: ["Incidente", "Empleado", "Sala"], just: "Un único requerimiento de consulta se desdobla en casos de uso de inspección interactiva para el guardia y de consolidación histórica para el supervisor." }},
      {{ id: "RF-32", cat: "rondas", catName: "Vigilancia & Incidentes", name: "Generar planificación de rondas", cus: ["CU-13 Generar planificación de rondas"], mapping: "1 a 1 Transaccional", rule: "Seguridad Operativa", ui: "Módulo Web - Asignación de Turnos", classes: ["PlanificacionRonda", "Sala", "Guardia", "SalaXGuardia"], just: "Genera la asignación temporal entre salas y guardias para un turno específico, poblando las instancias de la clase asociativa SalaXGuardia." }},
      {{ id: "RF-34", cat: "rondas", catName: "Vigilancia & Incidentes", name: "Registrar revisión de sala", cus: ["CU-16 Registrar revisión de la sala"], mapping: "1 a N (Caso Base)", rule: "Control Continuo", ui: "Tablet Móvil - Plano Interactivo", classes: ["Sala", "SalaXGuardia", "Guardia"], just: "Caso de uso base ejecutado obligatoriamente por el guardia al ingresar a cada sala, actualizando el conteo de salas verificadas en la ronda." }},
      {{ id: "RF-40", cat: "obras", catName: "Obras & Depósito", name: "Registrar obra a restaurar", cus: ["CU-4 Registrar obra a restaurar"], mapping: "1 a 1 Transaccional", rule: "Custodia Patrimonial", ui: "Módulo Web - Derivación a Taller", classes: ["ObraDeArte", "Restauracion", "Estado"], just: "Cambia el estado de la obra dañada para su traslado a los talleres de conservación tras el dictamen pericial del curador." }},
      {{ id: "RF-41", cat: "obras", catName: "Obras & Depósito", name: "Registrar reingreso de obra restaurada", cus: ["CU-2 Registrar reingreso de obra"], mapping: "1 a 1 con Regla de Negocio", rule: "RN1: Reingreso Obligatorio a Depósito", ui: "Módulo Web - Control de Depósito", classes: ["ObraDeArte", "Deposito", "Restauracion"], just: "Aplica de forma estricta la RN1: toda obra restaurada debe ingresar obligatoriamente al depósito antes de definir cualquier nuevo destino." }},
      {{ id: "RF-01", cat: "obras", catName: "Obras & Depósito", name: "Registrar ingreso de obra nueva", cus: ["CU-1 Registrar ingreso de obra"], mapping: "1 a 1 Transaccional", rule: "Catalogación Inicial", ui: "Módulo Web - Alta de Patrimonio", classes: ["ObraDeArte", "TipoObra", "TipoMaterial", "Estilo"], just: "Alta inicial en el inventario institucional con asignación de código unívoco, dimensiones, técnica y estado inicial." }},
      {{ id: "RF-28", cat: "visitas", catName: "Visitas & Guías", name: "Consultar agenda de guías", cus: ["CU-12 Consultar agenda de guías", "CU-11 Registrar contratación de servicio de guía"], mapping: "N a M (Inclusión Mandatoria)", rule: "Coordinación de Personal", ui: "Módulo Web - Calendario de Guías", classes: ["Guia", "AgendaGuia", "Turno"], just: "El CU-11 incluye obligatoriamente (<<include>>) la consulta de agenda del CU-12 para garantizar la disponibilidad horaria del profesional." }},
      {{ id: "RF-29", cat: "visitas", catName: "Visitas & Guías", name: "Registrar venta de entrada", cus: ["CU-10 Registrar venta de entrada", "CU-11 Registrar contratación de servicio de guía"], mapping: "N a M (Extensión Opcional)", rule: "Recaudación y Aforo", ui: "Módulo Web - Boletería", classes: ["Entrada", "Venta", "Tarifa"], just: "La venta de entrada es el caso base. La contratación de guía es una extensión facultativa solicitada a discreción por el visitante." }}
    ];

    let currentTraceCat = 'todos';

    function renderTraceList() {{
      const container = document.getElementById('trace-rf-container');
      if (!container) return;
      container.innerHTML = '';
      const filtered = traceData.filter(d => currentTraceCat === 'todos' || d.cat === currentTraceCat);
      filtered.forEach((d, idx) => {{
        const item = document.createElement('div');
        item.className = 'trace-rf-item' + (idx === 0 ? ' active' : '');
        item.onclick = () => selectTrace(d, item);
        item.innerHTML = `
          <span style="font-family: monospace; font-size: 11.5px; font-weight: 700; color: var(--blue-accent);">${{d.id}}</span>
          <span style="font-size: 13px; color: #FFF; flex: 1; margin: 0 10px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${{d.name}}</span>
          <span style="font-size: 10px; font-weight: 700; background: rgba(255,255,255,0.1); color: var(--text-light-secondary); padding: 2px 6px; border-radius: 4px;">${{d.catName.split(' ')[0]}}</span>
        `;
        container.appendChild(item);
      }});
      if (filtered.length > 0) selectTrace(filtered[0], container.firstChild);
    }}

    function filterTrace(cat, pillEl) {{
      currentTraceCat = cat;
      document.querySelectorAll('#slide-14 .btn-secondary').forEach(p => p.classList.remove('active'));
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
      cuGroup.innerHTML = d.cus.map(c => `<span style="font-size: 11.5px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: #FFF; padding: 3px 8px; border-radius: 4px;">${{c}}</span>`).join('');

      document.getElementById('trace-rule-group').innerText = d.rule;
      document.getElementById('trace-ui-label').innerText = d.ui;

      const classGroup = document.getElementById('trace-class-group');
      classGroup.innerHTML = d.classes.map(c => `<span style="font-size: 11.5px; font-family: monospace; background: rgba(255, 255, 255, 0.08); color: #FFF; padding: 3px 8px; border-radius: 4px;">${{c}}</span>`).join('');

      document.getElementById('trace-justification').innerText = d.just;
    }}

    // Init
    updateSlide();
    renderStepsList();
    selectStep(0);
    renderTraceList();
  </script>
</body>
</html>
''')

print("Final clean presentacion.html successfully compiled!")
