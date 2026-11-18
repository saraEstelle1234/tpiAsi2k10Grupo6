# -*- coding: utf-8 -*-
"""
generate_v5_pure_navy_deck.py
Compila presentacion.html con estética 100% azul marino oscuro (navy) minimalista y elegante:
- Fondo azul marino oscuro unificado en las 14 slides, con ritmo sutil de tonos.
- Tarjetas y marcos de diagramas adaptados a sus colores nativos para eliminar márgenes negros (DCU y DCD en #121212, Mapa en #2E2E2E, BPMN en blanco).
- SVGs vectoriales elegantes y sutiles en TODAS las slides para que ninguna quede con texto aburrido.
- Cero información inventada / cero chamuyo: 100% fiel al enunciado y TPI.
- Observaciones generales del sistema a la derecha de los diagramas, limpias y claras.
- Header counter '01 / 14' tabular-nums prolijo.
- Dock estilo macOS (resorte, fisheye, tooltips, click hop, manija táctil, auto-hide tras 600ms).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_editorial_html import (
    b64_mapa, b64_bpmn_desc, b64_bpmn_oper, b64_dcu, b64_proto, b64_dcd
)

def build_presentation():
    output_path = "presentacion.html"
    print(f"Generating {output_path} with pure minimal navy aesthetic and custom SVGs...")

    # Shared UI SVGs
    svg_arrow_left = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
    svg_arrow_right = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
    svg_expand = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>'
    svg_close = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18M6 6l12 12"/></svg>'
    svg_plus = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>'
    svg_minus = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/></svg>'
    svg_fit = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/></svg>'
    svg_grid = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/></svg>'
    svg_fullscreen = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3m0 8v3a2 2 0 0 0 2 2h3m8 0h3a2 2 0 0 0 2-2v-3m0-8V5a2 2 0 0 0-2-2h-3"/></svg>'
    svg_help = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
    svg_eye = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
    svg_check = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>'
    svg_asterisk = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M4.93 4.93l14.14 14.14M2 12h20M4.93 19.07l14.14-14.14"/></svg>'

    # Curated Aesthetic SVGs for slides without main diagrams
    svg_museum_arch = '''
    <svg width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8 56h48M12 56V26M24 56V26M40 56V26M52 56V26"/>
      <path d="M6 26h52L32 10 6 26z"/>
      <circle cx="32" cy="19" r="3" fill="#2F6BFF"/>
    </svg>
    '''

    svg_rules_gear = '''
    <svg width="60" height="60" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="12" y="8" width="40" height="48" rx="8" stroke="#FFFFFF" stroke-width="1.8"/>
      <line x1="20" y1="20" x2="44" y2="20" stroke="#2F6BFF" stroke-width="2"/>
      <line x1="20" y1="28" x2="38" y2="28" stroke="#2F6BFF" stroke-width="2"/>
      <line x1="20" y1="36" x2="32" y2="36" stroke="#2F6BFF" stroke-width="2"/>
      <circle cx="44" cy="44" r="10" fill="#11233F" stroke="#2F6BFF" stroke-width="2"/>
      <path d="M41 44l2 2 4-4" stroke="#2F6BFF" stroke-width="2"/>
    </svg>
    '''

    svg_req_matrix = '''
    <svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="10" y="10" width="18" height="18" rx="4" fill="rgba(47,107,255,0.12)"/>
      <rect x="36" y="10" width="18" height="18" rx="4" fill="rgba(47,107,255,0.12)"/>
      <rect x="10" y="36" width="18" height="18" rx="4" fill="rgba(47,107,255,0.12)"/>
      <rect x="36" y="36" width="18" height="18" rx="4" fill="rgba(47,107,255,0.25)" stroke="#FFFFFF"/>
      <path d="M28 19h8M19 28v8M45 28v8M28 45h8" stroke="#8E9EB5" stroke-dasharray="2 2"/>
    </svg>
    '''

    svg_actor_uml = '''
    <svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="20" cy="18" r="8"/>
      <path d="M20 26v16M10 32h20M14 50l6-8 6 8"/>
      <path d="M34 24h18M34 32h12M34 40h16" stroke="#8E9EB5" stroke-width="1.8"/>
      <polygon points="52,24 46,20 46,28" fill="#2F6BFF"/>
    </svg>
    '''

    svg_stepper_flow = '''
    <svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="16" cy="18" r="6" fill="#2F6BFF"/>
      <circle cx="16" cy="34" r="6" fill="rgba(47,107,255,0.3)"/>
      <circle cx="16" cy="50" r="6" fill="rgba(47,107,255,0.1)"/>
      <line x1="16" y1="24" x2="16" y2="28" stroke="#2F6BFF" stroke-width="2"/>
      <line x1="16" y1="40" x2="16" y2="44" stroke="#2F6BFF" stroke-width="2"/>
      <line x1="28" y1="18" x2="52" y2="18" stroke="#FFFFFF" stroke-width="2"/>
      <line x1="28" y1="34" x2="46" y2="34" stroke="#8E9EB5" stroke-width="1.8"/>
      <line x1="28" y1="50" x2="40" y2="50" stroke="#8E9EB5" stroke-width="1.8"/>
    </svg>
    '''

    svg_multiplicity_uml = '''
    <svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="8" y="16" width="20" height="32" rx="4" stroke="#FFFFFF" stroke-width="1.8"/>
      <rect x="36" y="16" width="20" height="32" rx="4" stroke="#2F6BFF" stroke-width="2"/>
      <line x1="28" y1="32" x2="36" y2="32" stroke="#2F6BFF" stroke-width="2"/>
      <text x="14" y="28" font-size="9" fill="#FFF" font-family="monospace" font-weight="bold">1</text>
      <text x="42" y="28" font-size="9" fill="#2F6BFF" font-family="monospace" font-weight="bold">1..*</text>
    </svg>
    '''

    with open(output_path, "w", encoding="utf-8") as out:
        out.write('''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Defensa TPI ASI 2K10 - Museo de Historia Natural</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
/* Pure Navy Minimalist System */
:root {
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
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Manrope', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background-color: var(--navy-deep);
  color: var(--text-light);
  overflow-x: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Header */
header {
  height: 64px;
  padding: 0 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-dark);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  background: rgba(10, 22, 40, 0.92);
}

.header-left {
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  gap: 10px;
}

.header-left::before {
  content: "";
  display: block;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--blue-accent);
  box-shadow: 0 0 10px var(--blue-accent);
}

.header-center {
  font-size: 13px;
  color: var(--text-light-secondary);
  font-weight: 600;
}

.header-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

/* Tabular Slide Counter Box */
.header-counter-box {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 5px 14px;
  border-radius: 999px;
  white-space: nowrap;
}

.counter-current {
  font-family: 'Manrope', -apple-system, sans-serif;
  font-size: 14px;
  font-weight: 800;
  color: #FFFFFF;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}

.counter-divider {
  width: 1px;
  height: 12px;
  background: rgba(255, 255, 255, 0.22);
}

.counter-total {
  font-family: 'Manrope', -apple-system, sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: #8E9EB5;
  font-variant-numeric: tabular-nums;
}

/* Header Progress Line */
.header-progress-line {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2.5px;
  background: var(--blue-accent);
  transition: width 0.35s ease;
  z-index: 101;
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
  font-size: clamp(32px, 4vw, 54px);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.08;
  margin-bottom: 8px;
  color: #FFFFFF;
}

.editorial-subtitle {
  font-size: 15.5px;
  line-height: 1.55;
  color: var(--text-light-secondary);
  margin-bottom: 22px;
  max-width: 920px;
}

/* Cards (Navy System) */
.card-dark {
  background: var(--navy-card);
  border: 1px solid var(--navy-card-border);
  border-radius: 24px;
  padding: 24px 28px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.35);
  position: relative;
  transition: all 0.25s ease;
  color: var(--text-light);
}

.card-dark:hover {
  transform: translateY(-2px);
  border-color: rgba(255, 255, 255, 0.18);
}

/* Buttons */
.btn-primary {
  min-height: 54px;
  padding: 0 30px;
  border-radius: 999px;
  background: var(--blue-accent);
  color: #FFFFFF;
  font-size: 15.5px;
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

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.16);
  transform: translateY(-1px);
}

.btn-secondary:active {
  transform: scale(0.97);
}

/* Seamless Diagram Frames (Matches diagram canvas to eliminate black margins) */
.diagram-frame-clean {
  border-radius: 24px;
  padding: 16px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  border: 1px solid rgba(255, 255, 255, 0.12);
}

/* Backgrounds tailored to native image backgrounds */
.frame-dark-canvas { background: #121212; }
.frame-white-canvas { background: #FFFFFF; }
.frame-mapa-canvas { background: #2E2E2E; }
.frame-proto-canvas { background: #1C3150; }

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
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}

.frame-white-canvas .diagram-action-bar {
  border-top-color: rgba(10, 22, 40, 0.08);
}

/* ========================================================
   macOS STYLE DOCK SYSTEM (SPRING + FISHEYE + AUTO-HIDE)
   ======================================================== */
.dock-hotspot {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 80px;
  z-index: 998;
  pointer-events: auto;
}

.dock-touch-handle {
  display: none;
  position: fixed;
  bottom: 8px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 997;
  background: rgba(10, 22, 40, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 999px;
  padding: 4px 16px;
  cursor: pointer;
  backdrop-filter: blur(8px);
}

.touch-bar {
  display: block;
  width: 34px;
  height: 4px;
  border-radius: 2px;
  background: #FFFFFF;
}

@media (pointer: coarse) {
  .dock-touch-handle {
    display: block;
  }
}

.mac-dock-container {
  position: fixed;
  bottom: 18px;
  left: 50%;
  transform: translateX(-50%) translateY(140%);
  z-index: 1000;
  height: 68px;
  background: rgba(10, 22, 40, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 999px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  opacity: 0;
  pointer-events: none;
  transition: transform 0.5s var(--ease-spring), opacity 0.3s ease;
}

.mac-dock-container.visible {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
  pointer-events: auto;
}

@media (prefers-reduced-motion: reduce) {
  .mac-dock-container {
    transition: opacity 0.2s ease, transform 0.2s ease !important;
  }
}

.dock-item-wrapper {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dock-icon-btn {
  width: 48px;
  height: 48px;
  min-width: 48px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.15s var(--ease-smooth), background 0.2s ease, box-shadow 0.2s ease;
  transform-origin: bottom center;
}

.dock-icon-btn svg {
  width: 22px;
  height: 22px;
  stroke: currentColor;
  stroke-width: 2.2;
  fill: none;
  transition: transform 0.15s ease;
}

.dock-icon-btn.btn-accent {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  box-shadow: 0 4px 16px rgba(47, 107, 255, 0.4);
}

.dock-icon-btn.btn-accent:hover {
  background: #1A54E1;
  box-shadow: 0 6px 20px rgba(47, 107, 255, 0.6);
}

/* Floating Tooltip Label */
.dock-tooltip {
  position: absolute;
  bottom: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: rgba(10, 22, 40, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  font-size: 12px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: 6px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  transition: opacity 0.18s ease, transform 0.18s ease;
  z-index: 1002;
}

.dock-item-wrapper:hover .dock-tooltip {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* macOS dock jump on click */
@keyframes mac-dock-jump {
  0% { transform: translateY(0) scale(1.15); }
  35% { transform: translateY(-16px) scale(1.22); }
  65% { transform: translateY(0) scale(1.1); }
  85% { transform: translateY(-6px) scale(1.15); }
  100% { transform: translateY(0) scale(1.15); }
}

.dock-icon-btn.mac-jumping {
  animation: mac-dock-jump 0.48s ease;
}

.dock-divider-mac {
  width: 1px;
  height: 32px;
  background: rgba(255, 255, 255, 0.15);
  margin: 0 2px;
}

.dock-counter-badge {
  font-family: 'Manrope', -apple-system, sans-serif;
  font-size: 13.5px;
  font-weight: 800;
  color: #FFFFFF;
  padding: 7px 13px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  font-variant-numeric: tabular-nums;
  letter-spacing: 0.02em;
  white-space: nowrap;
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
  background: rgba(47, 107, 255, 0.16);
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
  background: #182E54 !important;
  border-color: var(--blue-accent) !important;
  box-shadow: 0 14px 40px rgba(47, 107, 255, 0.3) !important;
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
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 13.5px;
  line-height: 1.55;
  color: var(--text-light-secondary);
}

.expandable-card.expanded .card-extra-content {
  display: block;
}

/* Fullscreen Zoom Modal */
.zoom-fullscreen-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 22, 40, 0.94);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  z-index: 2000;
  display: flex;
  flex-direction: column;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.zoom-fullscreen-modal.active {
  opacity: 1;
  visibility: visible;
}

.zoom-modal-top {
  height: 64px;
  padding: 0 32px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(10, 22, 40, 0.8);
}

.zoom-modal-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 16px;
  font-weight: 700;
  color: #FFFFFF;
}

.zoom-viewport-stage {
  flex: 1;
  overflow: hidden;
  position: relative;
  cursor: grab;
  display: flex;
  align-items: center;
  justify-content: center;
}

.zoom-viewport-stage:active {
  cursor: grabbing;
}

.zoom-stage-content {
  transform-origin: center center;
  transition: transform 0.08s linear;
  display: flex;
  align-items: center;
  justify-content: center;
}

.zoom-stage-content img {
  max-width: 90vw;
  max-height: 82vh;
  object-fit: contain;
  border-radius: 8px;
  background: #FFFFFF;
  padding: 8px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7);
}

.zoom-controls-floating {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(10, 22, 40, 0.92);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 999px;
  padding: 8px 16px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(20px);
}

.zoom-btn {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
  border-radius: 999px;
  padding: 6px 14px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}

.zoom-btn:hover {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
}

/* Overview Modal */
.overview-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(10, 22, 40, 0.96);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  z-index: 2000;
  display: flex;
  flex-direction: column;
  padding: 40px 60px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  overflow-y: auto;
}

.overview-modal.active {
  opacity: 1;
  visibility: visible;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  max-width: 1400px;
  margin: 30px auto 0 auto;
  width: 100%;
}

.overview-card-item {
  background: var(--navy-card);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.overview-card-item:hover {
  border-color: var(--blue-accent);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(47, 107, 255, 0.25);
}

.overview-card-item.current {
  border-color: var(--blue-accent);
  background: #192F56;
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
  -webkit-backdrop-filter: blur(16px);
  z-index: 2100;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.tutorial-modal.active {
  opacity: 1;
  visibility: visible;
}

.tutorial-card-body {
  background: #0E1F3A;
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 28px;
  padding: 36px 40px;
  max-width: 580px;
  width: 90%;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.6);
}


/* ========================================================
   TPI SECTION 2.3 NATIVE TABLE (SLIDE 4)
   ======================================================== */
.tpi-table-container {
  width: 100%;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(14, 31, 58, 0.7);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.tpi-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.tpi-table-main-header {
  background: linear-gradient(90deg, #183359 0%, #112440 100%);
  color: #FFFFFF;
  font-size: 15px;
  font-weight: 800;
  padding: 13px 20px;
  border-bottom: 2px solid var(--blue-accent);
  letter-spacing: -0.01em;
}

.tpi-col-label {
  width: 22%;
  padding: 11px 16px;
  font-size: 13px;
  font-weight: 700;
  color: #93C5FD;
  background: rgba(15, 30, 54, 0.9);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-col-content {
  width: 78%;
  padding: 11px 18px;
  font-size: 13px;
  line-height: 1.55;
  color: var(--text-light);
  background: rgba(10, 22, 40, 0.55);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-col-subtable-cell {
  width: 78%;
  padding: 0;
  background: rgba(10, 22, 40, 0.55);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}

.tpi-subtable {
  width: 100%;
  border-collapse: collapse;
}

.tpi-subtable th {
  background: rgba(255, 255, 255, 0.04);
  color: #CBD5E1;
  font-size: 11.5px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 8px 14px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.tpi-subtable th:last-child {
  border-right: none;
}

.tpi-subtable td {
  padding: 8px 14px;
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--text-light);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.tpi-subtable td:last-child {
  border-right: none;
}

.tpi-subtable tr:last-child td {
  border-bottom: none;
}

/* ========================================================
   TRACEABILITY EXPANDED MATRIX (SLIDE 14)
   ======================================================== */
.trace-module-pills {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.trace-module-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--text-light-secondary);
  padding: 8px 14px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.trace-module-btn:hover {
  background: rgba(47, 107, 255, 0.15);
  border-color: var(--blue-accent);
  color: #FFF;
}

.trace-module-btn.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFF;
  box-shadow: 0 4px 14px rgba(47, 107, 255, 0.35);
}


/* ========================================================
   REQUERIMIENTOS FUNCIONALES ACCORDION (SLIDE 7)
   ======================================================== */
.rf-group {
  background: rgba(14, 31, 58, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}

.rf-group[open] {
  border-color: var(--blue-accent);
  background: rgba(20, 42, 78, 0.75);
}

.rf-summary {
  padding: 12px 18px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
  font-weight: 700;
  color: #FFFFFF;
  user-select: none;
}

.rf-summary::-webkit-details-marker {
  display: none;
}

.rf-summary::after {
  content: '▼';
  font-size: 10px;
  color: var(--blue-accent);
  transition: transform 0.2s ease;
}

.rf-group[open] .rf-summary::after {
  transform: rotate(180deg);
}

.rf-badge {
  font-size: 11px;
  font-weight: 700;
  background: rgba(47, 107, 255, 0.2);
  color: #93C5FD;
  padding: 3px 8px;
  border-radius: 999px;
  margin-left: 8px;
}

.rf-body {
  padding: 8px 18px 14px 18px;
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  font-size: 13px;
  line-height: 1.6;
  color: var(--text-light);
}

.rf-item {
  padding: 6px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.rf-item:last-child {
  border-bottom: none;
}

.rf-num {
  font-weight: 700;
  color: var(--blue-accent);
  font-family: monospace;
  font-size: 12px;
  flex-shrink: 0;
}

/* ========================================================
   CU-15 FORMAL TEMPLATE (SLIDE 10)
   ======================================================== */
.cu-template-container {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(14, 31, 58, 0.75);
}

.cu-step-row {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 6px;
  font-size: 13px;
  line-height: 1.45;
  color: var(--text-light);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

.cu-step-row:hover {
  background: rgba(47, 107, 255, 0.1);
}

.cu-step-num {
  font-weight: 800;
  color: #93C5FD;
  font-size: 12px;
  min-width: 22px;
  text-align: right;
  flex-shrink: 0;
}

/* Presets focus bar for DCU & DCD */
.preset-focus-bar {
  display: flex;
  gap: 8px;
  background: rgba(255, 255, 255, 0.06);
  padding: 6px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.preset-btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: #FFFFFF;
  border-radius: 8px;
  padding: 6px 14px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
}

.preset-btn:hover, .preset-btn.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

/* Traceability Console (Slide 14) */
.trace-matrix-console {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 20px;
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 20px;
  padding: 24px;
}

.trace-rf-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 480px;
  overflow-y: auto;
  padding-right: 6px;
}

.trace-rf-item {
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 13.5px;
}

.trace-rf-item:hover, .trace-rf-item.active {
  background: var(--blue-accent);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

.trace-impact-dossier {
  background: #0B172B;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
  </style>
</head>
<body>

  <!-- Top Header with Tabular Number Counter -->
  <header>
    <div class="header-left">Museo de Historia Natural</div>
    <div class="header-center">TPI ASI 2K10 &bull; Grupo 6 &bull; Año 2026</div>
    <div class="header-right">
      <div class="header-counter-box">
        <span class="counter-current" id="header-cur-num">01</span>
        <span class="counter-divider"></span>
        <span class="counter-total">15</span>
      </div>
    </div>
    <div class="header-progress-line" id="header-progress-line" style="width: 6.67%;"></div>
  </header>

  <main>
''')

        # ========================================================
        # SLIDE 1: PORTADA & EQUIPO (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 1: PORTADA & EQUIPO -->
    <div class="slide active" id="slide-1" data-topic="01 · Portada y Equipo">
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
          Caso: Museo de Historia Natural &bull; Cátedra de Análisis de Sistemas &bull; Curso 2K10 &bull; Año 2026
        </p>

        <div style="display: flex; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="nextSlideAction()">
            Comenzar presentación {svg_arrow_right}
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()">
            {svg_grid} Ver los 15 slides
          </button>
        </div>
      </div>

      <!-- 9 Members Grid (Identical cards, no special borders) -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 423269</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Dominio bajo estudio y Objetivo general de la organización</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419166</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Procesos de Negocio y Mapa de Procesos</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 403382</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Descripción de Proceso y Reglas de Negocio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Jastrzebski, Emiliano</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 402760</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Modelado BPMN a Nivel Descriptivo y Operativo</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419749</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Requerimientos Funcionales y No Funcionales (RF y RNF)</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 408990</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Casos de Uso</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 410975</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Descripción del Caso de Uso: Registrar Incidente</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 400212</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Clases del Dominio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 418201</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Trazabilidad de Requerimientos y Cierre</div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 2: DOMINIO & OBJETIVOS (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide" id="slide-2" data-topic="02 · Dominio y Objetivos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">02 &bull; Dominio y Objetivos</div>
          <h1 class="giant-title">Dominio bajo Estudio</h1>
          <p class="editorial-subtitle">
            Museo de Historia Natural &bull; Contexto institucional y objetivos de la organización
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_museum_arch}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Organización y Operatoria del Dominio</div>
          <div style="font-size: 14.5px; line-height: 1.6; color: var(--text-light);">
            El Museo de Historia Natural de la ciudad expone obras de artistas locales, nacionales e internacionales. El público asiste a ver las obras abonando una entrada en caja, pudiendo solicitar con arancel adicional el servicio de guía. Las obras ingresan por compra, donación o préstamo, registrándose autor, estilo, tipo de obra, dimensiones, material, valuación y fecha, asignándose un número de identificación.
          </div>
        </div>
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Salas Temáticas y Rondas de Vigilancia</div>
          <div style="font-size: 14.5px; line-height: 1.6; color: var(--text-light);">
            El museo está organizado en salas temáticas, con especial atracción en los objetos animados, cuyo comportamiento ante luz, sonido y temperatura depende de su material. El guardia realiza rondas de vigilancia basadas en una planificación diaria que prioriza las salas con más incidentes, registrando cada sala como 'Sin novedades' o con 'Observación pendiente' si detecta un incidente de forma inmediata.
          </div>
        </div>
      </div>

      <!-- 3 Expandable Objective Cards Strictly from TPI -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">01</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Objetivo General de la Organización</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas, preservando las obras con un sistema de gestión de incidentes.
          </div>
          <div class="card-extra-content">
            Definido textualmente en la Sección 1.1 del TPI: sostener la exposición de arte como proceso esencial y financiar las actividades mediante el cobro de entradas y servicios de guía, asegurando la conservación integral del patrimonio.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">02</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Objetivo del Proceso de Vigilancia</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Gestionar incidentes y restauración de obras mediante las rondas de vigilancia del guardia, registrando en el Módulo Web.
          </div>
          <div class="card-extra-content">
            Definido en la plantilla de proceso (Sección 2.3): permitir que los supervisores tomen medidas en relación a la obra, tales como envío a restauración, registro de baja de obra o refuerzo de vigilancia en sectores conflictivos.
          </div>
        </div>

        <div class="card-dark expandable-card reveal-item revealed" onclick="toggleExpandCard(this)">
          <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div style="font-size: 38px; font-weight: 800; color: var(--blue-accent); line-height: 1;">03</div>
            <div class="expand-circle-btn">{svg_plus}</div>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Regla de Reingreso Obligatorio a Depósito</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); line-height: 1.45;">
            Luego de restauradas las obras reingresan al depósito del museo y quedan disponibles para lo que se las requiera.
          </div>
          <div class="card-extra-content">
            Texto textual del enunciado y TPI: Aún si las obras no pueden restaurarse son ingresadas nuevamente al depósito para luego decidir el momento para retirarla del museo, es decir, darle de baja. Ninguna pieza retorna directamente a sala de exhibición.
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 3: MAPA DE PROCESOS (THEME: DARK - MATCHED CANVAS)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 3: MAPA DE PROCESOS -->
    <div class="slide" id="slide-3" data-topic="03 · Mapa de Procesos">
      <div class="breadcrumb-tag">03 &bull; Vista Externa Organizacional</div>
      <h1 class="giant-title">Mapa de Procesos</h1>
      <p class="editorial-subtitle">
        Identificación y clasificación de procesos según Sección 2.1 y 2.2 del Trabajo Práctico Integrador
      </p>

      <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px; align-items: center;">
        <div class="diagram-frame-clean frame-mapa-canvas reveal-item revealed">
          <img src="{b64_mapa}" class="diagram-preview-img" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')" alt="Mapa de Procesos">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Mapa de Procesos &bull; Vista Externa</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_mapa', 'Mapa de Procesos de Negocio')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- Right Column Vertically Centered with exact TPI Section 2.1 lists -->
        <div style="display: flex; flex-direction: column; justify-content: center; gap: 16px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Procesos Estratégicos</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; Planificar la programación de exposiciones<br>
              &bull; Planificar visitas guiadas<br>
              &bull; Definir precios de guía<br>
              &bull; Definir precios de entrada
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #FFFFFF;">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Proceso Esencial</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; <strong>Exponer obras de arte</strong>
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--text-light-secondary);">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 6px;">Procesos de Soporte</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; Gestionar ingreso de obras artísticas<br>
              &bull; Gestionar incidentes y restauración de obras<br>
              &bull; Administrar RRHH
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 4: PROCESO CRÍTICO & REGLAS (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 4: PLANTILLA DE PROCESO -->
    <div class="slide" id="slide-4" data-topic="04 · Plantilla de Proceso">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">04 &bull; Proceso de Soporte</div>
          <h1 class="giant-title">Plantilla de Proceso</h1>
          <p class="editorial-subtitle">
            Proceso de Negocio: Gestionar incidentes y restauración de obras (Sección 2.3 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_rules_gear}
        </div>
      </div>

      <div class="tpi-table-container reveal-item revealed">
        <table class="tpi-table">
          <thead>
            <tr>
              <th colspan="2" class="tpi-table-main-header">
                Proceso de Negocio: Gestionar incidentes y restauración de obras
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="tpi-col-label">Objetivo</td>
              <td class="tpi-col-content">
                Gestionar incidentes y restauración de obras mediante las rondas de vigilancia realizadas por el guardia, registrando los incidentes en el Módulo Web para que los supervisores tomen medidas en relación a la obra, envío a restauración, registro de baja de obra, etc.
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Cliente del Proceso</td>
              <td class="tpi-col-content">
                Proceso: “Exponer obras de artes” (esencial).
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Producto del Proceso</td>
              <td class="tpi-col-content">
                Informe generado con todos los incidentes ocurridos, y obra enviada a reparación.
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Proveedores del proceso e insumos que brinda cada uno</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Proveedor</th>
                      <th style="width: 50%;">Insumo</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Proceso: Gestionar ingreso de obras artísticas.</td>
                      <td>Obra dañada</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Obra registrada en Módulo Web</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Recursos del proceso</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Recursos Humanos</th>
                      <th style="width: 50%;">Recursos Tecnológicos - Hardware</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Guardia del Museo</td>
                      <td>Modulo Web de Soporte</td>
                    </tr>
                    <tr>
                      <td>Supervisor</td>
                      <td>PC</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Formularios, registros e información del proceso</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 50%;">Formularios</th>
                      <th style="width: 50%;">Registros e información</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Informe</td>
                      <td>Incidente</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Informe</td>
                    </tr>
                    <tr>
                      <td>&mdash;</td>
                      <td>Planificación de ronda de vigilancia</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td class="tpi-col-label">Reglas de Negocio</td>
              <td class="tpi-col-subtable-cell">
                <table class="tpi-subtable">
                  <thead>
                    <tr>
                      <th style="width: 8%;">ID</th>
                      <th style="width: 32%;">Regla de negocio</th>
                      <th style="width: 60%;">Descripción</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">1.</td>
                      <td style="font-weight: 600; color: #FFF;">Reingreso obligatorio a deposito</td>
                      <td>Toda obra enviada a restauración, se haya podido reparar con exito o no, debe ingresar obligatoriamente al depósito del museo antes de definir su destino final o su baja</td>
                    </tr>
                    <tr>
                      <td style="text-align: center; font-weight: 700; color: var(--blue-accent);">2.</td>
                      <td style="font-weight: 600; color: #FFF;">Registro inmediato de incidente</td>
                      <td>El guardia debe registrar el incidente de la obra de forma inmediata, indicando detalles del incidente.</td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
<!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Descriptivo</h1>
      <p class="editorial-subtitle">
        Modelado a Nivel 1 del proceso de rondas de vigilancia (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: stretch;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="display: flex; flex-direction: column;">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1" style="flex: 1; object-fit: contain;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; Vista General</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 26px 24px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Nivel 1 &bull; Alcance de Negocio</div>
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción del Modelo Descriptivo</h3>
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              Modela el flujo global de negocio de punta a punta entre los actores clave: <strong>Guardia del Museo</strong>, <strong>Módulo Web</strong> y <strong>Supervisor</strong>, prescindiendo del detalle de software para brindar una perspectiva ejecutiva del proceso de vigilancia y respuesta.
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">1. Ronda y Verificación Física</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia recorre las salas asignadas según la planificación y constata visualmente el estado de las obras expuestas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">2. Detección y Registro Inmediato</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  Al detectar cualquier anomalía, el guardia accede al Módulo Web y registra el incidente en el momento exacto (Regla de Negocio 2).
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">3. Evaluación y Decisión del Supervisor</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El supervisor analiza el incidente consolidado en el sistema y define el curso de acción: traslado a restauración externa o baja de la obra.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Regla Fundamental de Integridad</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Toda obra restaurada reingresa obligatoriamente al depósito del museo antes de definir cualquier nuevo destino o exhibición (RN-1).
            </div>
          </div>
        </div>
      </div>
    </div>
<!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Compuerta exclusiva, bifurcación ante incidentes y eventos del flujo (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 20px;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="max-height: 480px;">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="max-height: 380px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')" alt="BPMN Nivel 2">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Compuertas y Flujos</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Compuerta Exclusiva: Bifurcación en Sala</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              &bull; <strong>Camino Normal:</strong> Si todo está en orden, registra la sala con 'Sin novedades'.<br>
              &bull; <strong>Camino de Anomalía:</strong> Si detecta daño o anomalía, registra la sala con 'Observación pendiente' y ejecuta el registro del incidente.
            </div>
          </div>
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Consolidación de Datos y Cierre de Ronda</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Al completar el recorrido por todas las salas asignadas, el sistema consolida automáticamente el informe diario con el resumen de siniestros para análisis de supervisión.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 7: REQUERIMIENTOS (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 7: REQUERIMIENTOS FUNCIONALES -->
    <div class="slide" id="slide-7" data-topic="07 · Requerimientos Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">07 &bull; Especificación de Requerimientos</div>
          <h1 class="giant-title">Requerimientos Funcionales</h1>
          <p class="editorial-subtitle">
            Catálogo estructurado por paquetes funcionales del sistema (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="display: flex; gap: 10px; align-items: center; padding-top: 10px;">
          <button class="btn-secondary" onclick="expandAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Expandir todos
          </button>
          <button class="btn-secondary" onclick="collapseAllRf()" style="min-height: 40px; padding: 0 16px; font-size: 13px;">
            Colapsar todos
          </button>
        </div>
      </div>

      <div style="margin-bottom: 14px;">
        <input type="text" id="rf-search-input" class="search-input" placeholder="🔍 Filtrar requerimientos por palabra clave (ej: obra, sala, incidente, ronda, informe)..." oninput="filterRequirements()" style="width: 100%; height: 46px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0 18px; color: #FFF; font-size: 14px;">
      </div>

      <!-- 15 Global Bold Categories from TPI in 2 Scrollable Columns -->
      <div id="rf-accordion-list" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-height: 520px; overflow-y: auto; padding-right: 6px;">
        
        <!-- 1. Administrar Obras de Arte -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Administrar Obras de Arte <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 1.</span> Registrar ingreso de obra</div>
            <div class="rf-item"><span class="rf-num">RF 2.</span> Consultar obra</div>
            <div class="rf-item"><span class="rf-num">RF 3.</span> Registrar baja de obra</div>
          </div>
        </details>

        <!-- 2. Administrar Tipos de Obra -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Obra <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 4.</span> Registrar tipo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 5.</span> Consultar tipo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 6.</span> Registrar baja de tipo de obra</div>
          </div>
        </details>

        <!-- 3. Administrar Tipos de Material -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Material <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 7.</span> Registrar tipo de material</div>
            <div class="rf-item"><span class="rf-num">RF 8.</span> Consultar tipo de material</div>
            <div class="rf-item"><span class="rf-num">RF 9.</span> Registrar baja de tipo de material</div>
          </div>
        </details>

        <!-- 4. Administrar Salas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Salas <span class="rf-badge">4 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 10.</span> Registrar sala</div>
            <div class="rf-item"><span class="rf-num">RF 11.</span> Consultar sala</div>
            <div class="rf-item"><span class="rf-num">RF 12.</span> Modificar sala</div>
            <div class="rf-item"><span class="rf-num">RF 13.</span> Registrar baja de sala</div>
          </div>
        </details>

        <!-- 5. Administrar Guías -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Guías <span class="rf-badge">4 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 14.</span> Registrar guía</div>
            <div class="rf-item"><span class="rf-num">RF 15.</span> Consultar guía</div>
            <div class="rf-item"><span class="rf-num">RF 16.</span> Registrar modificación de guía</div>
            <div class="rf-item"><span class="rf-num">RF 17.</span> Registrar baja de guía</div>
          </div>
        </details>

        <!-- 6. Administrar Estilos de Obra -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Estilos de Obra <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 18.</span> Registrar estilo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 19.</span> Consultar estilo de obra</div>
            <div class="rf-item"><span class="rf-num">RF 20.</span> Registrar baja de estilo de obra</div>
          </div>
        </details>

        <!-- 7. Administrar Tipos de Incidentes -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Tipos de Incidentes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 21.</span> Registrar tipo de incidente</div>
            <div class="rf-item"><span class="rf-num">RF 22.</span> Consultar tipo de incidente</div>
            <div class="rf-item"><span class="rf-num">RF 23.</span> Registrar baja de tipo de incidente</div>
          </div>
        </details>

        <!-- 8. Gestionar Exposiciones -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Exposiciones <span class="rf-badge">2 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 24.</span> Registrar programación de exposiciones</div>
            <div class="rf-item"><span class="rf-num">RF 25.</span> Consultar programación de exposiciones</div>
          </div>
        </details>

        <!-- 9. Gestionar Visitas Guiadas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Visitas Guiadas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 26.</span> Registrar planificación de visitas guiadas</div>
            <div class="rf-item"><span class="rf-num">RF 27.</span> Consultar planificación de visitas guiadas</div>
            <div class="rf-item"><span class="rf-num">RF 28.</span> Consultar agenda de guías</div>
          </div>
        </details>

        <!-- 10. Gestionar Venta de Entradas -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Gestionar Venta de Entradas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 29.</span> Registrar venta de entrada</div>
            <div class="rf-item"><span class="rf-num">RF 30.</span> Registrar contratación de servicio adicional de guía</div>
            <div class="rf-item"><span class="rf-num">RF 31.</span> Consultar venta de entrada</div>
          </div>
        </details>

        <!-- 11. Gestionar Planificación y Rondas de Vigilancia -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Planificación y Rondas <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 32.</span> Generar planificación de rondas de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 33.</span> Consultar planificación de rondas de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 34.</span> Registrar revisión de sala</div>
          </div>
        </details>

        <!-- 12. Gestionar Incidentes -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Incidentes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 35.</span> Registrar incidente</div>
            <div class="rf-item"><span class="rf-num">RF 36.</span> Consultar incidentes</div>
            <div class="rf-item"><span class="rf-num">RF 37.</span> Registrar seguimiento de resolución de incidente</div>
          </div>
        </details>

        <!-- 13. Gestionar Restauración -->
        <details class="rf-group" open>
          <summary class="rf-summary">
            <span>Gestionar Restauración <span class="rf-badge">2 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 40.</span> Registrar obra a restaurar</div>
            <div class="rf-item"><span class="rf-num">RF 41.</span> Registrar reingreso de obra</div>
          </div>
        </details>

        <!-- 14. Generar Informes y Reportes -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Generar Informes y Reportes <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 42.</span> Generar informe diario de vigilancia</div>
            <div class="rf-item"><span class="rf-num">RF 43.</span> Generar reporte de patrones de incidentes</div>
            <div class="rf-item"><span class="rf-num">RF 44.</span> Emitir historial de incidentes</div>
          </div>
        </details>

        <!-- 15. Administrar Sesión -->
        <details class="rf-group">
          <summary class="rf-summary">
            <span>Administrar Sesión <span class="rf-badge">3 RFs</span></span>
          </summary>
          <div class="rf-body">
            <div class="rf-item"><span class="rf-num">RF 45.</span> Iniciar sesión</div>
            <div class="rf-item"><span class="rf-num">RF 46.</span> Cerrar sesión</div>
            <div class="rf-item"><span class="rf-num">RF 47.</span> Modificar contraseña</div>
          </div>
        </details>

      </div>
    </div>

    <!-- SLIDE 8: REQUERIMIENTOS NO FUNCIONALES -->
    <div class="slide" id="slide-8" data-topic="08 · Requerimientos No Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
        <div>
          <div class="breadcrumb-tag">08 &bull; Restricciones de Calidad y Arquitectura</div>
          <h1 class="giant-title">Requerimientos No Funcionales</h1>
          <p class="editorial-subtitle">
            Criterios de calidad, arquitectura y restricciones técnicas del sistema (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;">
        
        <div class="card-dark reveal-item revealed" style="border-top: 3px solid var(--blue-accent); padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Arquitectura &bull; Acceso Web Ubicuo</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 1 &bull; Módulo Web de Soporte</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #60A5FA; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Usabilidad &bull; Terminal Táctil para Guardias</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 2 &bull; Interfaz Móvil para Rondas</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #38BDF8; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Rendimiento &bull; Transacciones Críticas</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 3 &bull; Tiempos de Respuesta &lt; 2s</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            El sistema procesará las consultas de salas y registros de incidentes en menos de 2 segundos en condiciones normales de carga, asegurando fluidez operativa durante la ronda.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #818CF8; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Seguridad &bull; Control de Acceso por Rol</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 4 &bull; Autenticación y RBAC</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Autenticación obligatoria con perfiles diferenciados (Guardia, Supervisor, Encargado, Administrador), contraseñas robustas y sesiones cifradas HTTPS para salvaguardar la integridad de los datos.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #A78BFA; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Disponibilidad &bull; Operatividad 24/7</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 5 &bull; Confiabilidad y Persistencia ACID</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Disponibilidad continua con base de datos relacional que garantiza atomicidad, consistencia, aislamiento y durabilidad (ACID) en cada actualización del inventario patrimonial.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-top: 3px solid #F472B6; padding: 22px 20px;">
          <div style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; margin-bottom: 6px;">Auditoría &bull; Registro Inmutable de Eventos</div>
          <div style="font-size: 17px; font-weight: 800; color: #FFFFFF; margin-bottom: 10px;">RNF 6 &bull; Trazabilidad y Marcas de Tiempo</div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
            Captura automática e inalterable de fecha, hora de servidor y usuario responsable en cada transacción de vigilancia, sustentando los informes diarios y reportes de patrones.
          </div>
        </div>

      </div>
    </div>

    <!-- SLIDE 9: DCU GENERAL (AMPLIADO Y SECTORIZADO POR ACTOR) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.55fr 0.45fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px;">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Sectorizar por Actor:</span>
            <button class="preset-btn active" onclick="setDiagramPreset('dcu-img', 1, 0, 0)">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.3, -20, -22)">Guardia (CU-14 / CU-15)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.0, 18, -16)">Supervisor</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.1, -20, 22)">Ingreso y Obras</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 1.9, 20, 20)">Administrador</button>
          </div>

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column;">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center;">
              <img id="dcu-img" src="{b64_dcu}" class="diagram-preview-img" style="max-height: 100%; width: 100%; object-fit: contain; transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1); cursor: zoom-in;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #CBD5E1;">42 Casos de Uso &bull; Fondo nativo sin bordes negros</span>
              <button class="btn-primary" style="min-height: 40px; padding: 0 18px; font-size: 13px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar a pantalla completa {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- UN SOLO CUADRO EXPLICATIVO GENERAL -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 10px;">Límites y Concepción</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Concepción General del Diagrama</h3>
            
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 16px;">
              El modelo define el límite completo del software mediante <strong>42 Casos de Uso</strong> numerados de forma unívoca y continua, satisfaciendo el proceso sustantivo (<em>Exponer obras de arte</em>) y el proceso de soporte crítico bajo estudio (<em>Gestionar incidentes y restauración</em>).
            </p>

            <div style="display: flex; flex-direction: column; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">8 Actores del Sistema</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  7 roles humanos con accesos diferenciados y 1 temporizador de software (<em>Administrador Web</em>) que dispara la planificación de rondas.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #60A5FA; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Separación Operativa / Gerencial</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El guardia opera en terminal móvil (revisión y reporte), mientras que supervisores y administradores gestionan el catálogo patrimonial e informes.
                </div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #38BDF8; padding: 10px 14px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Centralidad de la Vigilancia</div>
                <div style="font-size: 13px; color: var(--text-light); margin-top: 3px; line-height: 1.45;">
                  El <strong>CU-15 (Registrar incidente)</strong> constituye el núcleo de integración entre la detección en sala y la custodia patrimonial.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(47, 107, 255, 0.08); border: 1px solid rgba(47, 107, 255, 0.25); border-radius: 8px; padding: 10px 14px; margin-top: 14px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #93C5FD; text-transform: uppercase;">Navegación Interactiva</div>
            <div style="font-size: 12.5px; color: var(--text-light); margin-top: 2px;">
              Utilizá los botones superiores para enfocar la sección de cada actor o hacé clic en el diagrama para explorar con zoom libre.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: PLANTILLA CU-15 (ESTILO PLANTILLA ORIGINAL SECCIÓN 2.8) -->
    <div class="slide" id="slide-10" data-topic="10 · Plantilla de Caso de Uso">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">10 &bull; Especificación Formal de Caso de Uso</div>
          <h1 class="giant-title">Plantilla de Caso de Uso</h1>
          <p class="editorial-subtitle">
            Descripción formal: Registrar Incidente (CU-15 &bull; Sección 2.8 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
        </div>
      </div>

      <!-- Header Metadata Bar matching TPI Section 2.8 -->
      <div class="card-dark reveal-item revealed" style="margin-bottom: 14px; padding: 14px 20px;">
        <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; font-size: 13px;">
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">ID Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;">CU-15</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Nombre Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;">Registrar incidente</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Actor Principal</span>
            <strong style="color: #FFF; font-size: 14px;">Encargado de vigilancia (EV)</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Actor Secundario</span>
            <strong style="color: #CBD5E1; font-size: 14px;">&mdash;</strong>
          </div>
          <div>
            <span style="color: #93C5FD; font-size: 11px; font-weight: 700; text-transform: uppercase; display: block;">Tipo de Caso de Uso</span>
            <strong style="color: #FFF; font-size: 14px;"><span style="color: var(--blue-accent);">[X]</span> Concreto &nbsp; [ ] Abstracto</strong>
          </div>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 16px;">
        <!-- Left Column: Objetivo, Pre-Condición, Cursos Alternativos, Post-Condiciones -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
          
          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Objetivo</div>
            <div style="font-size: 13px; line-height: 1.5; color: var(--text-light);">
              Registrar incidente en una sala del museo, indicando la pieza involucrada y el tipo de incidente con la hora.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 4px;">Pre-Condición</div>
            <div style="font-size: 13px; line-height: 1.5; color: var(--text-light);">
              Usuario logueado en el Módulo Web de Soporte y sala seleccionada.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #F59E0B; text-transform: uppercase; margin-bottom: 6px;">Cursos Alternativos</div>
            <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              <div><strong style="color: #FCD34D;">A1 (Paso 11):</strong> El EV no confirma el registro del incidente. Se cancela el caso de uso.</div>
              <div><strong style="color: #FCD34D;">A2 (Paso 4):</strong> El sistema busca el código del objeto pero no lo encuentra, y solicita que se ingrese otro código.</div>
              <div><strong style="color: #FCD34D;">A3 (Paso 6):</strong> El EV no confirma el objeto encontrado. Se cancela el caso de uso.</div>
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 18px;">
            <div style="font-size: 11.5px; font-weight: 700; color: #10B981; text-transform: uppercase; margin-bottom: 6px;">Post-Condiciones</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              <div style="margin-bottom: 4px;"><strong style="color: #6EE7B7;">Éxito:</strong> El sistema registró con éxito el incidente en una sala, con la pieza, el tipo de incidente, hora y registra el objeto con estado “Inactivo”. Incidente registrado exitosamente.</div>
              <div><strong style="color: #F87171;">Fracaso:</strong> El CU se cancela cuando: (A1) El EV no confirmó el registro; (A2) El EV cancela en cualquier momento; (A3) El EV no confirmó el objeto encontrado.</div>
            </div>
          </div>

        </div>

        <!-- Right Column: Curso Normal (14 Pasos) -->
        <div class="card-dark reveal-item revealed" style="padding: 16px 20px; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 8px; margin-bottom: 10px;">
            <span style="font-size: 13px; font-weight: 700; color: #FFF; text-transform: uppercase;">Curso Normal (Flujo Principal)</span>
            <span style="font-size: 11px; font-weight: 700; background: rgba(47,107,255,0.2); color: #93C5FD; padding: 3px 8px; border-radius: 999px;">14 Pasos Secuenciales</span>
          </div>

          <div style="max-height: 440px; overflow-y: auto; padding-right: 6px; display: flex; flex-direction: column;">
            <div class="cu-step-row"><span class="cu-step-num">1.</span> <span>El EV ingresa a la opción <em>Reportar incidente</em>.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">2.</span> <span>El sistema solicita que ingrese el código del objeto.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">3.</span> <span>El EV ingresa el código del objeto.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">4.</span> <span>El sistema busca la obra por el código ingresado y muestra sus datos: título/nombre de la obra, sala asignada y ubicación física dentro de la sala. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A2 si no existe]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">5.</span> <span>El sistema solicita que se confirme que el objeto encontrado es el correcto.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">6.</span> <span>El EV confirma el objeto encontrado. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A3 si no confirma]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">7.</span> <span>El sistema solicita que se seleccione el tipo de incidente entre Deterioro natural, Deterioro provocado y Caída accidental.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">8.</span> <span>El EV selecciona el tipo de incidente.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">9.</span> <span>El sistema muestra los datos del incidente para su revisión final: sala/ubicación, obra involucrada, tipo de incidente seleccionado, hora actual del registro y el nuevo estado de la obra.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">10.</span> <span>El sistema solicita que se confirme el registro del incidente.</span></div>
            <div class="cu-step-row" style="background: rgba(245, 158, 11, 0.08);"><span class="cu-step-num" style="color: #FCD34D;">11.</span> <span>El EV confirma el registro del incidente. <em style="color: #FCD34D; font-size: 11px;">[Ramifica A1 si cancela]</em></span></div>
            <div class="cu-step-row"><span class="cu-step-num">12.</span> <span>El sistema registra el incidente en una sala del museo, con la pieza involucrada, el tipo de incidente, la hora (que se obtiene de la hora actual).</span></div>
            <div class="cu-step-row" style="background: rgba(16, 185, 129, 0.08);"><span class="cu-step-num" style="color: #6EE7B7;">13.</span> <span>El sistema registra el objeto con estado <strong>“Inactivo”</strong>.</span></div>
            <div class="cu-step-row"><span class="cu-step-num">14.</span> <span>Fin del caso de uso.</span></div>
          </div>
        </div>
      </div>
    </div>
<!-- SLIDE 11: PROTOTIPO DE PANTALLA -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo UI</div>
      <h1 class="giant-title">Prototipo de Interfaz</h1>
      <p class="editorial-subtitle">
        Interfaz táctil para tablet de guardia y correspondencia con la plantilla (Sección 2.8 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px; align-items: center;">
        <div class="diagram-frame-clean frame-proto-canvas reveal-item revealed">
          <img src="{b64_proto}" class="diagram-preview-img" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')" alt="Prototipo Tablet">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Pantalla Táctil &bull; Tablet de Guardia</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_proto', 'Prototipo de Pantalla en Tablet')">
              Ampliar pantalla {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">1. Búsqueda y Validación (Pasos 2 a 4)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Campo numérico para ingresar el código de la pieza y visualización inmediata del nombre, sala y ubicación física.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">2. Tipificación del Siniestro (Pasos 7 y 8)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Selector desplegable con los tipos reglamentarios (Deterioro provocado, Caída accidental, Deterioro natural) y caja de texto para observaciones.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 6px;">3. Confirmación Segura (Pasos 9 a 14)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Botón de confirmación con diálogo modal que previene registros involuntarios antes de impactar en la base de datos.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 12: DIAGRAMA DE CLASES (THEME: DARK - MATCHED CANVAS #121212)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 12: DIAGRAMA DE CLASES -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="preset-focus-bar">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Enfoque rápido:</span>
            <button class="preset-btn active" onclick="setDiagramPreset('dcd-img', 1, 0, 0)">Ver Todo</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcd-img', 1.9, 15, -20)">Incidente & Tipo</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcd-img', 1.9, -20, 20)">Sala & Guardias</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcd-img', 2.0, 15, 20)">Obra & Estado</button>
          </div>

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="flex: 1;">
            <div style="overflow: hidden; height: 420px; display: flex; align-items: center; justify-content: center; position: relative;">
              <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="max-height: 420px; transition: transform 0.4s ease;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Diagrama de Clases &bull; Entidades y Métodos</span>
              <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
                Ampliar diagrama {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px; justify-content: center;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Clases Intervinientes</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              &bull; <strong>Incidente:</strong> Entidad transaccional con fecha, hora del servidor y descripción.<br>
              &bull; <strong>TipoIncidente:</strong> Clasificación normalizada del evento de daño.<br>
              &bull; <strong>Obra / ObjetoAnimado:</strong> Pieza patrimonial con atributo de estado y método <code>registrarIncidente()</code>.<br>
              &bull; <strong>Sala y SalaXGuardia:</strong> Modelo de asignación y registro histórico de rondas.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Consistencia con la Plantilla</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Cada método y mensaje documentado en la plantilla formal del CU-15 cuenta con su correspondiente soporte en las responsabilidades de las clases del modelo.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 13: MULTIPLICIDADES (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 13: MULTIPLICIDADES -->
    <div class="slide" id="slide-13" data-topic="13 · Multiplicidades y Asociaciones">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Modelo de Dominio</div>
          <h1 class="giant-title">Multiplicidades y Asociaciones</h1>
          <p class="editorial-subtitle">
            Relaciones estructurales, multiplicidades y reglas del dominio (Sección 2.10 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_multiplicity_uml}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 8px;">1. Multiplicidad Incidente &rarr; TipoIncidente</div>
          <div style="font-size: 17px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Multiplicidad 1 Obligatoria</div>
          <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
            Todo incidente registrado debe asociarse obligatoriamente a exactamente <strong>un (1)</strong> TipoIncidente. No se permiten incidentes anónimos o sin tipificar en la base de datos, garantizando la integridad de las estadísticas y los patrones de supervisión.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="border-left: 4px solid #FFFFFF;">
          <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 8px;">2. Multiplicidad Sala &rarr; SalaXGuardia</div>
          <div style="font-size: 17px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Multiplicidad 1..* (Uno a Muchos)</div>
          <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
            Cada sala del museo se vincula a <strong>uno o más (1..*)</strong> registros en la clase asociativa SalaXGuardia. Esto preserva el histórico de todas las rondas realizadas por los distintos guardias a lo largo de los días y turnos de vigilancia.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="grid-column: 1 / -1; border-left: 4px solid var(--text-light-secondary);">
          <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 8px;">3. Transición de Estado y Encapsulamiento de la Obra</div>
          <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
            Al crearse un Incidente, el mensaje <code>registrarIncidente()</code> en la clase Obra delega en su estado interno la transición al estado <strong>'Inactivo'</strong>. De esta manera, el sistema bloquea automáticamente la obra para exhibición o visitas guiadas, garantizando el aislamiento y resguardo de la pieza dañada hasta su envío a depósito o taller.
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 14: TRAZABILIDAD & CIERRE (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 14: TRAZABILIDAD -->
    <div class="slide" id="slide-14" data-topic="14 · Trazabilidad">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">14 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Mapeo integral: Reglas de Negocio &rarr; BPMN &rarr; Requerimientos &rarr; Casos de Uso &rarr; Clases del Dominio
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#2F6BFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"/>
            <circle cx="6" cy="12" r="3"/>
            <circle cx="18" cy="19" r="3"/>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
          </svg>
        </div>
      </div>

      <!-- Conceptual Explanation of Traceability in ASI -->
      <div class="card-dark reveal-item revealed" style="margin-bottom: 20px; padding: 22px 26px; border-left: 4px solid var(--blue-accent);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-size: 15px; font-weight: 800; color: #FFF;">El Concepto de Trazabilidad en Análisis de Sistemas</span>
          <span style="font-size: 11px; font-weight: 700; background: rgba(47,107,255,0.18); color: #93C5FD; padding: 4px 10px; border-radius: 999px;">FUNDAMENTO METODOLÓGICO</span>
        </div>
        <div style="font-size: 13.5px; line-height: 1.6; color: var(--text-light);">
          La <strong>trazabilidad</strong> es la propiedad que permite relacionar bidireccionalmente cada elemento del sistema de información con los objetivos de negocio que le dieron origen (<em>forward & backward traceability</em>).
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 12px; font-size: 13px; line-height: 1.5; color: var(--text-light-secondary);">
          <div style="background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px;">
            <strong style="color: #FFF;">Relación N a M (Muchos a Muchos):</strong> Un requerimiento puede materializarse en múltiples casos de uso (ej. gestión de obras dividida en alta, consulta, reparación y baja), mientras que un caso de uso complejo puede dar cumplimiento simultáneo a varios requerimientos funcionales (ej. CU-15 registra el hecho, captura fecha/hora y asocia la obra).
          </div>
          <div style="background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px;">
            <strong style="color: #FFF;">Requerimientos sin Caso de Uso interactivo:</strong> Ciertos requerimientos no originan un CU con actor porque corresponden a <em>reglas de dominio/integridad referencial</em> garantizadas directamente en el Diagrama de Clases (ej. RN-1 reingreso a depósito), o a <em>requerimientos no funcionales transversales</em> (seguridad, rendimiento).
          </div>
        </div>
      </div>

      <!-- Interactive 8-Module Trace Matrix -->
      <div class="trace-matrix-console reveal-item revealed">
        <div style="width: 32%;">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 10px;">Seleccionar Módulo del Sistema:</div>
          <div class="trace-rf-list" style="max-height: 380px; overflow-y: auto;">
            <div class="trace-rf-item active" onclick="selectTraceModule(this, 'mod-incidentes')">
              <strong>Módulo 6</strong> &bull; Gestión de Incidentes
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-rondas')">
              <strong>Módulo 5</strong> &bull; Planificación y Rondas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-obras')">
              <strong>Módulo 1</strong> &bull; Obras y Catálogo
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-maestros')">
              <strong>Módulo 2</strong> &bull; Parámetros Maestros
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-exposiciones')">
              <strong>Módulo 3</strong> &bull; Exposiciones y Visitas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-entradas')">
              <strong>Módulo 4</strong> &bull; Venta de Entradas
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-informes')">
              <strong>Módulo 7</strong> &bull; Informes y Reportes
            </div>
            <div class="trace-rf-item" onclick="selectTraceModule(this, 'mod-seguridad')">
              <strong>Módulo 8</strong> &bull; Seguridad y Reglas de Negocio
            </div>
          </div>
        </div>

        <div class="trace-impact-dossier" id="trace-dossier-content" style="width: 68%;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 14px;">
            <span style="font-size: 16px; font-weight: 800; color: #FFF;" id="trace-mod-title">Módulo 6: Gestión de Incidentes</span>
            <span style="font-size: 11px; font-weight: 700; background: var(--blue-accent); color: #FFF; padding: 4px 10px; border-radius: 4px;" id="trace-mod-badge">PROCESO DE SOPORTE CRÍTICO</span>
          </div>

          <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13.5px;">
            <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Requerimientos Funcionales Incluidos</span>
              <span id="trace-rfs" style="color: var(--text-light); line-height: 1.5; margin-top: 4px; display: block;">
                <strong>RF-37:</strong> Registrar incidente &bull; <strong>RF-38:</strong> Consultar incidentes &bull; <strong>RF-39:</strong> Registrar seguimiento de resolución de incidente.
              </span>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #60A5FA; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Casos de Uso Asociados</span>
                <span id="trace-cus" style="color: #FFF; font-weight: 600; line-height: 1.5; margin-top: 4px; display: block;">
                  CU-15 Registrar incidente<br>CU-17 Consultar incidente<br>CU-23 Registrar seguimiento
                </span>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 12px 14px; border-radius: 8px;">
                <span style="color: #38BDF8; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Actores y Clases DCD</span>
                <span id="trace-actors" style="color: var(--text-light); line-height: 1.5; margin-top: 4px; display: block;">
                  <strong>Actores:</strong> Guardia del Museo, Supervisor.<br><strong>Clases:</strong> Incidente, TipoIncidente, Obra, Guardia, Supervisor.
                </span>
              </div>
            </div>

            <div style="background: rgba(47,107,255,0.08); border-left: 3px solid var(--blue-accent); padding: 10px 14px; border-radius: 0 8px 8px 0;">
              <span style="color: #93C5FD; font-weight: 700; display: block; font-size: 11.5px; text-transform: uppercase;">Justificación Analítica de Trazabilidad</span>
              <span id="trace-rationale" style="color: var(--text-light); font-size: 12.5px; line-height: 1.5; margin-top: 4px; display: block;">
                Conexión directa con la Regla de Negocio 2 (inmediatez de registro) y la compuerta de anomalía del BPMN Operativo. El CU-15 materializa en pantalla táctil la captura del daño, garantizando que el incidente quede disponible al supervisor para la toma de medidas.
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 15: CIERRE & AGRADECIMIENTO -->
    <div class="slide" id="slide-15" data-topic="15 · Cierre y Agradecimiento">
      <div class="card-dark" style="margin-bottom: 24px; position: relative; overflow: hidden; padding: 38px 44px; text-align: center;">
        <div style="position: absolute; right: -40px; top: -40px; opacity: 0.08; pointer-events: none;">
          <svg width="340" height="340" viewBox="0 0 200 200" fill="none">
            <circle cx="100" cy="100" r="90" stroke="#2F6BFF" stroke-width="12"/>
            <path d="M40 100 L85 145 L160 65" stroke="#2F6BFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <div class="breadcrumb-tag" style="display: inline-flex; margin-bottom: 12px;">
          {svg_check} Defensa Oral Finalizada &bull; Trabajo Práctico Integrador
        </div>
        <h1 class="giant-title" style="margin-bottom: 8px; font-size: 48px;">¡Muchas Gracias!</h1>
        <p class="editorial-subtitle" style="max-width: 680px; margin: 0 auto 24px auto; font-size: 15px;">
          Sistema de Gestión y Vigilancia Museológica &bull; Grupo 6 &bull; Curso 2K10 &bull; Cátedra de Análisis de Sistemas de Información &bull; UTN - FRC 2026
        </p>

        <div style="display: flex; justify-content: center; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="goToSlide(1)" style="min-height: 48px; padding: 0 24px; font-size: 14px;">
            Volver al inicio ↺
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()" style="min-height: 48px; padding: 0 22px; font-size: 14px;">
            {svg_grid} Ver las 15 slides
          </button>
        </div>
      </div>

      <!-- 9 Members Grid (Balanced 3x3) -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Abad, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 423269</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Dominio bajo estudio y Objetivos de la organización</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Cufre, Agustín</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419166</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Procesos de Negocio y Mapa de Procesos</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Marcuzzi, Tomas</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 403382</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Proceso y Reglas de Negocio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Jastrzebski, Emiliano</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 402760</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Modelado BPMN a Nivel Descriptivo y Operativo</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Molina, Tobias</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 419749</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Requerimientos Funcionales y No Funcionales (RF y RNF)</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Thomas Rapp, Francisco</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 408990</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Casos de Uso</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Moyano, Lucas Uriel</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 410975</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Plantilla de Caso de Uso: Registrar Incidente</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Tarditti, Juan Sebastián</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 400212</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Diagrama de Clases del Dominio</div>
        </div>

        <div class="card-dark" style="padding: 18px 20px;">
          <div style="font-size: 15px; font-weight: 700; color: #FFF;">Pereyra, Kevin</div>
          <div style="font-size: 12px; color: var(--text-light-secondary); font-family: monospace;">Legajo: 418201</div>
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Trazabilidad de Requerimientos y Cierre</div>
        </div>
      </div>
    </div>

''')

        # ========================================================
        # macOS STYLE DOCK CONTAINER (SPRING + FISHEYE)
        # ========================================================
        out.write(f'''
  <!-- Hotspot trigger zone at bottom (80px height) -->
  <div class="dock-hotspot" id="dock-hotspot"></div>

  <!-- Touch screen toggle handle -->
  <button class="dock-touch-handle" id="dock-touch-handle" onclick="toggleDockTouch()" title="Abrir controles">
    <span class="touch-bar"></span>
  </button>

  <!-- macOS Dock Container (Hidden by default, spring slide up) -->
  <div class="mac-dock-container" id="mac-dock">
    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" id="dock-btn-prev" onclick="handleDockClick(this, prevSlideAction)" aria-label="Slide anterior">
        {svg_arrow_left}
      </button>
      <div class="dock-tooltip">Anterior (←)</div>
    </div>

    <div class="dock-counter-badge" id="dock-counter-text">01 / 15</div>

    <div class="dock-item-wrapper">
      <button class="dock-icon-btn btn-accent" id="dock-btn-next" onclick="handleDockClick(this, nextSlideAction)" aria-label="Avanzar">
        {svg_arrow_right}
      </button>
      <div class="dock-tooltip">Siguiente (→ o Espacio)</div>
    </div>

    <div class="dock-divider-mac"></div>

    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" onclick="handleDockClick(this, openOverviewModal)" aria-label="Vista general">
        {svg_grid}
      </button>
      <div class="dock-tooltip">Vista general (O)</div>
    </div>

    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" onclick="handleDockClick(this, toggleFullscreen)" aria-label="Pantalla completa">
        {svg_fullscreen}
      </button>
      <div class="dock-tooltip">Pantalla completa (F)</div>
    </div>

    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" onclick="handleDockClick(this, revealAllInCurrentSlide)" aria-label="Mostrar todo">
        {svg_eye}
      </button>
      <div class="dock-tooltip">Mostrar todo (A)</div>
    </div>

    <div class="dock-item-wrapper">
      <button class="dock-icon-btn" onclick="handleDockClick(this, openTutorialModal)" aria-label="Ayuda">
        {svg_help}
      </button>
      <div class="dock-tooltip">Ayuda (?)</div>
    </div>
  </div>
''')

        # ========================================================
        # MODALS: FULLSCREEN ZOOM, OVERVIEW GRID, TUTORIAL
        # ========================================================
        out.write(f'''
  <!-- Fullscreen Zoom Modal with Pan & Wheel -->
  <div class="zoom-fullscreen-modal" id="zoom-fullscreen-modal">
    <div class="zoom-modal-top">
      <div class="zoom-modal-title">
        <span style="font-size: 11px; font-weight: 800; background: var(--blue-accent); color: #FFF; padding: 4px 10px; border-radius: 999px;">HD</span>
        <span id="zoom-modal-title-text">Diagrama en Alta Resolución</span>
      </div>
      <button class="btn-secondary" onclick="closeZoomModal()" style="border-color: rgba(255,255,255,0.25);" title="Cerrar (Esc)">
        Cerrar {svg_close}
      </button>
    </div>

    <div class="zoom-viewport-stage" id="zoom-stage">
      <div class="zoom-stage-content" id="zoom-stage-content">
        <img id="zoom-modal-img" src="" alt="Diagrama">
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
      <button class="zoom-btn" onclick="closeZoomModal()" style="background: rgba(255,255,255,0.18);" title="Cerrar (Esc)">
        {svg_close} Cerrar
      </button>
    </div>
  </div>

  <!-- Overview Grid Modal (14 Slides) -->
  <div class="overview-modal" id="overview-modal">
    <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin: 0 auto; width: 100%;">
      <div>
        <div class="breadcrumb-tag">Navegación Rápida</div>
        <h2 style="font-size: 26px; font-weight: 800; color: #FFF;">Vista General de la Presentación &bull; 14 Slides</h2>
      </div>
      <button class="btn-primary" onclick="closeOverviewModal()">
        Cerrar vista {svg_close}
      </button>
    </div>
    <div class="overview-grid" id="overview-grid-container"></div>
  </div>

  <!-- Onboarding Mini-Tutorial Modal -->
  <div class="tutorial-modal" id="tutorial-modal">
    <div class="tutorial-card-body">
      <div class="breadcrumb-tag">Instrucciones de Uso</div>
      <h3 style="font-size: 24px; font-weight: 800; color: #FFF; margin-bottom: 14px;">Cómo Navegar la Presentación</h3>
      <div style="display: flex; flex-direction: column; gap: 14px; margin-bottom: 24px; font-size: 14px; line-height: 1.5; color: var(--text-light);">
        <div style="display: flex; gap: 12px; align-items: flex-start;">
          <div style="background: var(--blue-accent); color: #FFF; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; flex-shrink: 0;">1</div>
          <div><strong>Avanzar paso a paso:</strong> Usá las flechas del teclado (<code>&rarr;</code>, <code>&larr;</code>), la barra espaciadora o el botón flotante inferior. El botón <strong>Mostrar todo</strong> (o tecla <code>A</code>) revela todo el contenido del slide.</div>
        </div>
        <div style="display: flex; gap: 12px; align-items: flex-start;">
          <div style="background: var(--blue-accent); color: #FFF; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; flex-shrink: 0;">2</div>
          <div><strong>Explorar diagramas:</strong> Hacé click en cualquier diagrama o en el botón <strong>Ampliar diagrama ↗</strong> para abrir el visor con zoom por rueda y arrastre con mouse.</div>
        </div>
        <div style="display: flex; gap: 12px; align-items: flex-start;">
          <div style="background: var(--blue-accent); color: #FFF; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; flex-shrink: 0;">3</div>
          <div><strong>Dock estilo macOS:</strong> Mové el cursor hacia el borde inferior de la pantalla para desplegar la barra de controles flotante con efecto fisheye y resorte.</div>
        </div>
      </div>
      <button class="btn-primary" style="width: 100%;" onclick="closeTutorialModal()">
        Entendido {svg_check}
      </button>
    </div>
  </div>
''')

        # ========================================================
        # JAVASCRIPT SYSTEM
        # ========================================================
        out.write(f'''
  </main>

  <script>
    // Embedded image assets dictionary
    const diagramAssets = {{
      b64_mapa: "{b64_mapa}",
      b64_bpmn_desc: "{b64_bpmn_desc}",
      b64_bpmn_oper: "{b64_bpmn_oper}",
      b64_dcu: "{b64_dcu}",
      b64_proto: "{b64_proto}",
      b64_dcd: "{b64_dcd}"
    }};

    // Slide state (1 to 14)
    let currentSlide = 1;
    const totalSlides = 15;

    const slideTitles = [
      "01 · Portada y Equipo",
      "02 · Dominio bajo Estudio",
      "03 · Mapa de Procesos",
      "04 · Plantilla de Proceso",
      "05 · BPMN Nivel Descriptivo",
      "06 · BPMN Nivel Operativo",
      "07 · Requerimientos Funcionales",
      "08 · Requerimientos No Funcionales",
      "09 · Diagrama de Casos de Uso",
      "10 · Plantilla de Caso de Uso",
      "11 · Prototipo de Interfaz",
      "12 · Diagrama de Clases",
      "13 · Multiplicidades y Asociaciones",
      "14 · Trazabilidad de Requerimientos",
      "15 · Cierre y Agradecimiento"
    ];

    const headerCurNum = document.getElementById('header-cur-num');
    const headerProgressLine = document.getElementById('header-progress-line');
    const dockCounterText = document.getElementById('dock-counter-text');

    function updateSlide() {{
      for (let i = 1; i <= totalSlides; i++) {{
        const el = document.getElementById('slide-' + i);
        if (el) {{
          if (i === currentSlide) {{
            el.classList.add('active');
          }} else {{
            el.classList.remove('active');
          }}
        }}
      }}

      // Header and Dock Counter Formats
      const numStr = (currentSlide < 10 ? '0' : '') + currentSlide;
      if (headerCurNum) headerCurNum.textContent = numStr;
      if (dockCounterText) dockCounterText.textContent = `${{numStr}} / ${{totalSlides}}`;

      const progressPct = (currentSlide / totalSlides) * 100;
      if (headerProgressLine) headerProgressLine.style.width = `${{progressPct}}%`;

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

    // Expandable cards toggle
    function toggleExpandCard(cardEl) {{
      const isExpanded = cardEl.classList.contains('expanded');
      const siblings = cardEl.parentElement.querySelectorAll('.expandable-card');
      siblings.forEach(s => s.classList.remove('expanded'));
      if (!isExpanded) {{
        cardEl.classList.add('expanded');
      }}
    }}

    // Diagram Preset focus (DCU & DCD)
    function setDiagramPreset(imgId, scale, tx, ty) {{
      const img = document.getElementById(imgId);
      if (img) {{
        img.style.transform = `scale(${{scale}}) translate(${{tx}}%, ${{ty}}%)`;
      }}
      const btns = event.target.parentElement.querySelectorAll('.preset-btn');
      btns.forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
    }}

    // ========================================================
    // macOS DOCK LOGIC (SPRING SLIDE + FISHEYE MAGNIFICATION)
    // ========================================================
    const macDock = document.getElementById('mac-dock');
    const dockHotspot = document.getElementById('dock-hotspot');
    const dockIcons = document.querySelectorAll('.dock-icon-btn');
    let dockHideTimer = null;

    function showMacDock() {{
      if (dockHideTimer) clearTimeout(dockHideTimer);
      macDock.classList.add('visible');
    }}

    function hideMacDockWithDelay() {{
      if (dockHideTimer) clearTimeout(dockHideTimer);
      dockHideTimer = setTimeout(() => {{
        macDock.classList.remove('visible');
      }}, 600);
    }}

    dockHotspot.addEventListener('mouseenter', showMacDock);
    dockHotspot.addEventListener('mouseleave', hideMacDockWithDelay);
    macDock.addEventListener('mouseenter', showMacDock);
    macDock.addEventListener('mouseleave', hideMacDockWithDelay);

    // Fisheye magnification on mousemove
    macDock.addEventListener('mousemove', (e) => {{
      const mouseX = e.clientX;
      dockIcons.forEach(icon => {{
        const rect = icon.getBoundingClientRect();
        const iconCenterX = rect.left + rect.width / 2;
        const dist = Math.abs(mouseX - iconCenterX);
        const maxDist = 90;

        if (dist < maxDist) {{
          const factor = 1 - (dist / maxDist);
          const scale = 1 + factor * 0.36; // Up to 1.36x
          const translateY = -(factor * 6);
          icon.style.transform = `scale(${{scale}}) translateY(${{translateY}}px)`;
        }} else {{
          icon.style.transform = 'scale(1) translateY(0)';
        }}
      }});
    }});

    macDock.addEventListener('mouseleave', () => {{
      dockIcons.forEach(icon => {{
        icon.style.transform = 'scale(1) translateY(0)';
      }});
    }});

    // macOS click hop/bounce
    function handleDockClick(btn, actionFn) {{
      btn.classList.add('mac-jumping');
      setTimeout(() => btn.classList.remove('mac-jumping'), 480);
      if (actionFn) actionFn();
    }}

    function toggleDockTouch() {{
      macDock.classList.toggle('visible');
    }}

    // ========================================================
    // ZOOM MODAL WITH PAN & WHEEL
    // ========================================================
    const zoomModal = document.getElementById('zoom-fullscreen-modal');
    const zoomModalImg = document.getElementById('zoom-modal-img');
    const zoomModalTitle = document.getElementById('zoom-modal-title-text');
    const zoomStage = document.getElementById('zoom-stage');
    const zoomStageContent = document.getElementById('zoom-stage-content');
    const zoomLevelText = document.getElementById('zoom-level-text');

    let currentZoom = 1;
    let panX = 0, panY = 0;
    let isDragging = false;
    let startX = 0, startY = 0;

    function applyZoomTransform() {{
      zoomStageContent.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{currentZoom}})`;
      zoomLevelText.textContent = `${{Math.round(currentZoom * 100)}}%`;
    }}

    function openZoomModal(assetKey, title) {{
      const assetSrc = diagramAssets[assetKey] || assetKey;
      zoomModalImg.src = assetSrc;
      zoomModalTitle.textContent = title;
      currentZoom = 1;
      panX = 0;
      panY = 0;
      applyZoomTransform();
      zoomModal.classList.add('active');
    }}

    function closeZoomModal() {{
      zoomModal.classList.remove('active');
    }}

    function modalZoomIn() {{
      currentZoom = Math.min(currentZoom + 0.25, 4.0);
      applyZoomTransform();
    }}

    function modalZoomOut() {{
      currentZoom = Math.max(currentZoom - 0.25, 0.5);
      applyZoomTransform();
    }}

    function modalResetZoom() {{
      currentZoom = 1;
      panX = 0;
      panY = 0;
      applyZoomTransform();
    }}

    zoomStage.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY * -0.0015;
      currentZoom = Math.min(Math.max(0.5, currentZoom + delta), 4.0);
      applyZoomTransform();
    }}, {{ passive: false }});

    zoomStage.addEventListener('mousedown', (e) => {{
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyZoomTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
    }});

    zoomStage.addEventListener('dblclick', () => {{
      if (currentZoom === 1) {{
        currentZoom = 2.0;
      }} else {{
        modalResetZoom();
      }}
      applyZoomTransform();
    }});

    // ========================================================
    // OVERVIEW GRID MODAL (14 SLIDES)
    // ========================================================
    const overviewModal = document.getElementById('overview-modal');
    const overviewGrid = document.getElementById('overview-grid-container');

    function buildOverviewGrid() {{
      overviewGrid.innerHTML = '';
      slideTitles.forEach((title, idx) => {{
        const card = document.createElement('div');
        const num = idx + 1;
        card.className = 'overview-card-item' + (num === currentSlide ? ' current' : '');
        card.innerHTML = `
          <div style="font-size: 11px; font-weight: 700; color: var(--blue-accent);">SLIDE ${{String(num).padStart(2, '0')}}</div>
          <div style="font-size: 14.5px; font-weight: 700; color: #FFF;">${{title.split(' · ')[1] || title}}</div>
        `;
        card.onclick = () => {{
          goToSlide(num);
          closeOverviewModal();
        }};
        overviewGrid.appendChild(card);
      }});
    }}

    function openOverviewModal() {{
      buildOverviewGrid();
      overviewModal.classList.add('active');
    }}

    function closeOverviewModal() {{
      overviewModal.classList.remove('active');
    }}

    // ========================================================
    // ONBOARDING MINI-TUTORIAL MODAL
    // ========================================================
    const tutorialModal = document.getElementById('tutorial-modal');
    function openTutorialModal() {{
      tutorialModal.classList.add('active');
    }}

    function closeTutorialModal() {{
      tutorialModal.classList.remove('active');
    }}

    // ========================================================
    // FULLSCREEN TOGGLE
    // ========================================================
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // ========================================================
    // KEYBOARD NAVIGATION
    // ========================================================
    window.addEventListener('keydown', (e) => {{
      if (zoomModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeZoomModal();
        return;
      }}
      if (overviewModal.classList.contains('active')) {{
        if (e.key === 'Escape' || e.key.toLowerCase() === 'o') closeOverviewModal();
        return;
      }}
      if (tutorialModal.classList.contains('active')) {{
        if (e.key === 'Escape') closeTutorialModal();
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ') {{
        e.preventDefault();
        nextSlideAction();
      }} else if (e.key === 'ArrowLeft') {{
        e.preventDefault();
        prevSlideAction();
      }} else if (e.key.toLowerCase() === 'o') {{
        openOverviewModal();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }} else if (e.key.toLowerCase() === 'a') {{
        revealAllInCurrentSlide();
      }} else if (e.key === '?' || e.key.toLowerCase() === 'h') {{
        openTutorialModal();
      }}
    }});

    // ========================================================
    // TRACEABILITY MATRIX DATA INTERACTION (SLIDE 14)
    // ========================================================
    
    // ========================================================
    // EXPANDED TRACEABILITY MODULES CONTROLLER
    // ========================================================
    const traceModulesData = {{
      'mod-incidentes': {{
        title: 'Módulo 6: Gestión de Incidentes',
        badge: 'PROCESO DE SOPORTE CRÍTICO',
        rfs: '<strong>RF-37:</strong> Registrar incidente &bull; <strong>RF-38:</strong> Consultar incidentes &bull; <strong>RF-39:</strong> Registrar seguimiento de resolución de incidente.',
        cus: 'CU-15 Registrar incidente<br>CU-17 Consultar incidente<br>CU-23 Registrar seguimiento de resolución',
        actors: '<strong>Actores:</strong> Guardia del Museo, Supervisor.<br><strong>Clases:</strong> Incidente, TipoIncidente, Obra, Guardia, Supervisor.',
        rationale: 'Conexión directa con la Regla de Negocio 2 (inmediatez de registro) y la compuerta de anomalía del BPMN Operativo. El CU-15 materializa en pantalla táctil la captura del daño, garantizando que el incidente quede disponible al supervisor para la toma de medidas.'
      }},
      'mod-rondas': {{
        title: 'Módulo 5: Planificación y Rondas de Vigilancia',
        badge: 'PREVENCIÓN Y PATRULLAJE',
        rfs: '<strong>RF-34:</strong> Generar planificación de rondas &bull; <strong>RF-35:</strong> Consultar planificación &bull; <strong>RF-36:</strong> Registrar revisión de sala.',
        cus: 'CU-12 Generar planificación de rondas<br>CU-13 Consultar planificación ronda<br>CU-14 Registrar revisión de la sala',
        actors: '<strong>Actores:</strong> Supervisor, Guardia del Museo.<br><strong>Clases:</strong> PlanificacionRonda, Guardia, Sala, AsignacionRonda.',
        rationale: 'Establece la base física preventiva donde el guardia patrulla periódicamente las salas del museo. Cumplimentar la revisión de sala es la precondición operativa para la eventual detección de obras dañadas.'
      }},
      'mod-obras': {{
        title: 'Módulo 1: Obras de Arte y Catálogo',
        badge: 'NÚCLEO PATRIMONIAL',
        rfs: '<strong>RF-01:</strong> Registrar ingreso de obra &bull; <strong>RF-02:</strong> Registrar reingreso a depósito &bull; <strong>RF-03:</strong> Consultar obra &bull; <strong>RF-04:</strong> Registrar baja de obra &bull; <strong>RF-39:</strong> Registrar obra a restaurar.',
        cus: 'CU-01 Registrar ingreso de obra<br>CU-02 Registrar reingreso de obra<br>CU-03 Consultar obra<br>CU-04 Registrar obra a restaurar<br>CU-42 Registrar baja de obra',
        actors: '<strong>Actores:</strong> Supervisor, Encargado de Museo.<br><strong>Clases:</strong> Obra, EstadoObra, Deposito, Artista, Estilo, TipoMaterial.',
        rationale: 'Gestiona el ciclo de vida del inventario patrimonial. Garantiza el cumplimiento de la RN-1 (reingreso obligatorio a depósito luego de cualquier envío a restauración, previo a su reasignación o baja).'
      }},
      'mod-maestros': {{
        title: 'Módulo 2: Parámetros Maestros y Tablas de Soporte',
        badge: 'CONFIGURACIÓN Y CONSISTENCIA',
        rfs: '<strong>RF-05..RF-24:</strong> Registrar, consultar, modificar y dar de baja Tipos de Obra, Tipos de Material, Salas, Guías, Estilos y Tipos de Incidentes.',
        cus: 'CU-08..CU-10 Materiales &bull; CU-11..14 / CU-24..27 Salas<br>CU-15..18 / CU-35..38 Guías &bull; CU-19..21 / CU-39..41 Estilos<br>CU-22..24 / CU-31..34 Tipos de Incidente',
        actors: '<strong>Actores:</strong> Administrador del Sistema, Supervisor.<br><strong>Clases:</strong> TipoObra, TipoMaterial, Sala, Guia, Estilo, TipoIncidente.',
        rationale: 'Provee los datos normalizados indispensables para la consistencia transaccional del sistema. Evita ambigüedades en la tipificación de incidentes, clasificación artística y ubicación en salas.'
      }},
      'mod-exposiciones': {{
        title: 'Módulo 3: Gestión de Exposiciones y Visitas',
        badge: 'PROCESO CLAVE ESENCIAL',
        rfs: '<strong>RF-25..RF-30:</strong> Registrar y consultar programación de exposiciones, planificar visitas guiadas, generar invitaciones y consultar agenda de guías.',
        cus: 'CU-05 Registrar programación exposiciones<br>CU-06 Consultar exposiciones<br>CU-07 Consultar visitas guiadas<br>CU-08 Registrar planificación visitas<br>CU-11 Consultar agenda de guías',
        actors: '<strong>Actores:</strong> Encargado de Museo, Guía, Visitante.<br><strong>Clases:</strong> Exposicion, ObraEnExposicion, VisitaGuiada, Guia, Sala.',
        rationale: 'Satisface el proceso de negocio sustantivo del museo ("Exponer obras de arte"). Cada exposición vincula temporalmente obras con salas específicas, delimitando el alcance de patrullaje de los guardias.'
      }},
      'mod-entradas': {{
        title: 'Módulo 4: Gestión de Venta de Entradas',
        badge: 'CONTROL DE AFORO Y RECAUDACIÓN',
        rfs: '<strong>RF-31:</strong> Registrar venta de entrada &bull; <strong>RF-32:</strong> Contratación de servicio de guía &bull; <strong>RF-33:</strong> Consultar venta de entrada.',
        cus: 'CU-09 Registrar venta de entrada<br>CU-10 Registrar servicio adicional de guía<br>CU-32 Consultar venta de entrada',
        actors: '<strong>Actores:</strong> Empleado de Boletería, Visitante.<br><strong>Clases:</strong> Entrada, Tarifa, DetalleVenta, Visitante.',
        rationale: 'Regula el ingreso de público y financiamiento operativo del museo, permitiendo calcular el volumen de aforo por sala para ajustar las frecuencias de rondas de vigilancia.'
      }},
      'mod-informes': {{
        title: 'Módulo 7: Informes y Reportes Gerenciales',
        badge: 'INTELIGENCIA Y CONTROL',
        rfs: '<strong>RF-40:</strong> Generar informe diario &bull; <strong>RF-41:</strong> Reporte de patrones &bull; <strong>RF-42:</strong> Consultar informe &bull; <strong>RF-43:</strong> Emitir historial.',
        cus: 'CU-18/19 Patrones de incidentes<br>CU-20/21 Informe diario de vigilancia<br>CU-22 Emitir historial de incidentes',
        actors: '<strong>Actores:</strong> Director del Museo, Supervisor.<br><strong>Clases:</strong> InformeDiario, Incidente, Sala, Obra.',
        rationale: 'Consolida los eventos registrados por los guardias en auditorías periódicas que permiten al Director y Supervisores evaluar medidas de prevención y zonas de mayor riesgo en el edificio.'
      }},
      'mod-seguridad': {{
        title: 'Módulo 8: Seguridad y Reglas de Dominio',
        badge: 'INTEGRIDAD TRANSVERSAL',
        rfs: '<strong>RF-44:</strong> Iniciar sesión &bull; <strong>RF-45:</strong> Cerrar sesión &bull; <strong>RF-46:</strong> Modificar contraseña &bull; <strong>RN-1:</strong> Reingreso a depósito &bull; <strong>RN-2:</strong> Registro inmediato.',
        cus: 'Transversal por Módulo Web (Autenticación y Sesión)<br>Restricciones de Integridad en Clases (RN-1 y RN-2)',
        actors: '<strong>Actores:</strong> Todos los roles autenticados.<br><strong>Clases:</strong> Usuario, Rol, Sesion, Obra, Incidente.',
        rationale: 'Requerimientos que NO poseen un caso de uso independiente con actor final porque se gestionan mediante el middleware de seguridad del Módulo Web o mediante restricciones del dominio de persistencia.'
      }}
    }};

    function selectTraceModule(el, modKey) {{
      document.querySelectorAll('.trace-rf-list .trace-rf-item').forEach(item => item.classList.remove('active'));
      el.classList.add('active');

      const data = traceModulesData[modKey];
      if (!data) return;

      document.getElementById('trace-mod-title').innerText = data.title;
      document.getElementById('trace-mod-badge').innerText = data.badge;
      document.getElementById('trace-rfs').innerHTML = data.rfs;
      document.getElementById('trace-cus').innerHTML = data.cus;
      document.getElementById('trace-actors').innerHTML = data.actors;
      document.getElementById('trace-rationale').innerText = data.rationale;
    }}

    // Filter requirements in Slide 7
    
    // ========================================================
    // REQUERIMIENTOS FUNCIONALES EXPAND / COLLAPSE
    // ========================================================
    function expandAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = true);
    }}

    function collapseAllRf() {{
      document.querySelectorAll('#rf-accordion-list .rf-group').forEach(g => g.open = false);
    }}

    function filterRequirements() {{
      const query = document.getElementById('rf-search-input').value.toLowerCase();
      const groups = document.querySelectorAll('#rf-accordion-list .rf-group');
      groups.forEach(g => {{
        const text = g.innerText.toLowerCase();
        if (text.includes(query)) {{
          g.style.display = 'block';
          if (query.length > 1) g.open = true;
        }} else {{
          g.style.display = 'none';
        }}
      }});
    }}

    // Initialize View
    updateSlide();
  </script>
</body>
</html>
''')
    print("Pure Navy Compilation completed successfully!")

if __name__ == '__main__':
    build_presentation()
