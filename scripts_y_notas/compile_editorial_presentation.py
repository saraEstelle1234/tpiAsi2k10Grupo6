# -*- coding: utf-8 -*-
"""
Compiler script for presentacion.html
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
svg_asterisk = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2L13.5 9L20 6L16 12L22 15L15 16L17 22L12 18L7 22L9 16L2 15L8 12L4 6L10.5 9L12 2Z"/></svg>'

css_content = """
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
  transition: background-color 0.4s ease, color 0.4s ease;
  user-select: none;
}

body.theme-light {
  background-color: var(--bg-light);
  color: var(--text-dark);
}

/* Thin Header */
header {
  height: 60px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-dark);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
  background: rgba(10, 22, 40, 0.85);
  transition: all 0.4s ease;
}

body.theme-light header {
  background: rgba(248, 250, 252, 0.9);
  border-bottom-color: var(--border-light);
}

.header-project {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

body.theme-light .header-project {
  color: var(--navy-deep);
}

.header-center {
  font-size: 13px;
  color: var(--text-light-secondary);
  font-weight: 500;
}

body.theme-light .header-center {
  color: var(--text-secondary);
}

.header-right {
  display: flex;
  align-items: center;
  gap: 16px;
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
  padding: 32px 48px 120px 48px;
  max-width: 1520px;
  margin: 0 auto;
  width: 100%;
}

.slide {
  display: none;
  width: 100%;
  animation: slideIn 0.45s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}

.slide.active {
  display: block;
}

@keyframes slideIn {
  from { opacity: 0; transform: scale(0.98) translateY(10px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

/* Breadcrumb & Section tags */
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
  font-size: clamp(34px, 4.4vw, 62px);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.06;
  margin-bottom: 8px;
}

body.theme-light .giant-title {
  color: var(--text-dark);
}

.editorial-subtitle {
  font-size: 16px;
  line-height: 1.55;
  color: var(--text-light-secondary);
  margin-bottom: 24px;
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
  padding: 26px 30px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
  transition: all 0.25s ease;
  position: relative;
}

.card-light {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: 24px;
  padding: 26px 30px;
  box-shadow: 0 6px 24px rgba(10, 22, 40, 0.04);
  transition: all 0.25s ease;
  position: relative;
  color: var(--text-dark);
}

.card-light:hover, .card-dark:hover {
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
  box-shadow: 0 4px 18px rgba(47, 107, 255, 0.35);
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
  font-size: 14.5px;
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
"""

print("Writing full generator script...")
