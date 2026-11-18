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
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
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
  padding: 14px 20px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 16px;
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
  grid-template-columns: 400px 1fr;
  gap: 24px;
  background: var(--navy-card);
  border: 1px solid var(--border-dark);
  border-radius: 20px;
  padding: 24px 28px;
  min-height: 560px;
}

.trace-rf-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-height: 520px;
  overflow-y: auto;
  overflow-x: hidden;
  padding-right: 8px;
  scrollbar-width: thin;
  scrollbar-color: rgba(45, 127, 249, 0.4) transparent;
}

.trace-rf-list::-webkit-scrollbar {
  width: 6px;
}
.trace-rf-list::-webkit-scrollbar-thumb {
  background: rgba(45, 127, 249, 0.4);
  border-radius: 4px;
}

.trace-rf-item {
  padding: 14px 18px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 15px;
}

.trace-rf-item:hover, .trace-rf-item.active {
  background: rgba(45, 127, 249, 0.22);
  border-color: var(--blue-accent);
  color: #FFFFFF;
}

.trace-impact-dossier {
  background: #0B172B;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  padding: 24px 28px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  gap: 14px;
  min-height: 520px;
  overflow: visible;
}

    /* --- IDEA 2: TRACE PIPELINE (SLIDE 13) --- */
    .trace-pipeline-container {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      padding: 12px 16px;
      margin-bottom: 14px;
    }
    .pipeline-node {
      flex: 1;
      border-radius: 8px;
      padding: 9px 12px;
      text-align: center;
      transition: all 0.3s ease;
    }
    .pipeline-arrow {
      color: #60A5FA;
      display: flex;
      align-items: center;
      justify-content: center;
      animation: pulseArrow 2s infinite ease-in-out;
    }
    @keyframes pulseArrow {
      0%, 100% { opacity: 0.6; transform: translateX(0); }
      50% { opacity: 1; transform: translateX(3px); }
    }


    /* ========================================================
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
        <span class="counter-total">14</span>
      </div>
    </div>
    <div class="header-progress-line" id="header-progress-line" style="width: 7.14%;"></div>
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
            {svg_grid} Ver los 14 slides
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

      <!-- 3 Clean Objective Cards Strictly from TPI Section 1.1 & 2.1 -->
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #60A5FA; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 1.1 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Objetivo de la Organización</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            Exponer obras de artistas locales, nacionales e internacionales al público mediante el cobro de entradas, preservando las obras con un sistema de gestión de incidentes.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 2.1 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Proceso Esencial</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            <strong>Exponer obras de arte:</strong> Proceso central de la organización y cliente receptor de las obras protegidas por el sistema de vigilancia.
          </div>
        </div>

        <div class="card-dark reveal-item revealed" style="padding: 22px 20px;">
          <div style="font-size: 12px; font-weight: 800; color: #818CF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">Sección 2.3 del TPI</div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 8px;">Objetivo del Proceso Bajo Estudio</div>
          <div style="font-size: 13.5px; color: var(--text-light); line-height: 1.55;">
            Gestionar incidentes y restauración de obras mediante las rondas de vigilancia del guardia, registrando en el Módulo Web para que los supervisores tomen medidas.
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
            <tr>
              <td class="tpi-col-label">Observaciones</td>
              <td class="tpi-col-content" style="color: var(--text-light-secondary); font-style: italic;">
                &mdash; (No aplica)
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

      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
        <!-- Diagrama a tamaño maximizado en marco blanco limpio -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 620px; display: flex; flex-direction: column; border-radius: 14px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo (4 Carriles)')" alt="BPMN Nivel 1 Descriptivo" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; 4 Carriles Formalizados</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo (4 Carriles)')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- Síntesis en 4 carriles (sin cuadritos negros) -->
        <div class="card-dark reveal-item revealed" style="padding: 24px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Nivel 1 &bull; Alcance Global</div>
            <h3 style="font-size: 18px; font-weight: 800; color: #FFF; margin-bottom: 10px; letter-spacing: -0.01em;">Estructura en 4 Carriles</h3>
            <p style="font-size: 12.5px; line-height: 1.55; color: var(--text-light); margin-bottom: 16px;">
              El modelo formaliza la interacción y responsabilidades entre los cuatro roles del proceso (Sección 2.5 del TPI):
            </p>

            <div style="display: flex; flex-direction: column; gap: 13px; padding-left: 2px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">1. Guardia del museo</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Ronda presencial, consulta de planificación y reporte in situ de novedades en sala.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">2. Admin de sistema</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Tipificación del daño (accidental, provocado, natural) y acciones sugeridas de mitigación.
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">3. Encargado de supervisión</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Evaluación consolidada del informe y determinación de derivación a restauración o baja.
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 12px;">
                <div style="font-size: 12.5px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">4. Encargado de restauración</div>
                <div style="font-size: 12px; color: var(--text-light); line-height: 1.45;">
                  Intervención técnica en taller y reingreso obligatorio a depósito conforme a la Regla 1.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 11.5px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Clic en el diagrama o en 'Ampliar' para navegarlo con zoom libre en alta resolución.</em>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: BPMN OPERATIVO (NUEVO DIAGRAMA CORREGIDO CON 4 CARRILES) -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN</div>
      <h1 class="giant-title">BPMN Nivel Operativo</h1>
      <p class="editorial-subtitle">
        Flujo de control, 4 carriles, alimentación de datos y estados del proceso (Sección 2.6 del TPI)
      </p>

      <div style="display: flex; flex-direction: column; gap: 14px;">
        <!-- Diagrama a tamaño máximo horizontal en marco blanco limpio sin bordes negros -->
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed" style="height: 520px; display: flex; flex-direction: column; border-radius: 14px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
          <img src="{b64_bpmn_oper}" class="diagram-preview-img" style="flex: 1; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')" alt="BPMN Nivel 2 Corregido">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 2 Operativo &bull; Versión Oficial Corregida (1682 &times; 798 px)</span>
            <button class="btn-primary" style="min-height: 38px; padding: 0 16px; font-size: 13px;" onclick="openZoomModal('b64_bpmn_oper', 'BPMN Nivel 2 Operativo (Versión Corregida 4 Carriles)')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <!-- 3 Puntos concretos que explican cómo se plantearon las correcciones del profesor -->
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px;">
          
          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #2D7FF9;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">1. Alimentación y Almacenes</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              La tarea <em>Registrar incidente</em> se alimenta de los almacenes maestros de <strong>Incidente</strong>, <strong>Salas</strong> y <strong>Obras</strong>, asociando las acciones sugeridas de acuerdo al tipo de daño.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #60A5FA;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">2. Estados Explícitos</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              Cada actividad explicita su estado: sala en <strong>'Incidente activo'</strong> o <strong>'Sin novedades'</strong>; y la obra pasa a <strong>'Inactivo'</strong> ante daño y retorna a <strong>'Activo'</strong> tras su resolución.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="padding: 14px 16px; border-left: 3px solid #38BDF8;">
            <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; margin-bottom: 4px;">3. 4 Carriles y Restauración</div>
            <div style="font-size: 12.5px; line-height: 1.45; color: var(--text-light);">
              Separación formal en 4 carriles: <em>Guardia del museo</em>, <em>Admin de sistema</em>, <em>Encargado de supervisión</em> y <em>Encargado de restauración</em>, con la actividad <strong>'Restaurar obra'</strong>.
            </div>
          </div>

        </div>
      </div>
    </div>
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

      <!-- 15 Global Bold Categories from TPI in 2 Independent Separate Columns -->
      <div id="rf-accordion-list" style="display: flex; gap: 18px; max-height: 520px; overflow-y: auto; padding-right: 6px; align-items: flex-start;">
        
        <!-- Columna Izquierda (Grupos 1 a 8) -->
        <div class="rf-col" id="rf-col-left" style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
          
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

        </div>

        <!-- Columna Derecha (Grupos 9 a 15) -->
        <div class="rf-col" id="rf-col-right" style="flex: 1; display: flex; flex-direction: column; gap: 10px;">
          
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
          <details class="rf-group">
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
          <details class="rf-group">
            <summary class="rf-summary">
              <span>Gestionar Incidentes <span class="rf-badge">3 RFs</span></span>
            </summary>
            <div class="rf-body">
              <div class="rf-item"><span class="rf-num">RF 35.</span> Registrar incidente (CU-15)</div>
              <div class="rf-item"><span class="rf-num">RF 36.</span> Consultar incidentes</div>
              <div class="rf-item"><span class="rf-num">RF 37.</span> Registrar seguimiento de resolución de incidente</div>
            </div>
          </details>

          <!-- 13. Gestionar Restauración -->
          <details class="rf-group">
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
    </div>

    <!-- SLIDE 8: REQUERIMIENTOS NO FUNCIONALES (ESTRICTAMENTE 2 SEGÚN TPI) -->
    <div class="slide" id="slide-8" data-topic="08 · Requerimientos No Funcionales">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px;">
        <div>
          <div class="breadcrumb-tag">08 &bull; Restricciones de Calidad y Arquitectura</div>
          <h1 class="giant-title">Requerimientos No Funcionales</h1>
          <p class="editorial-subtitle">
            Criterios de arquitectura técnica y soporte operativo especificados formalmente en la Sección 2.4 del TPI
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 6px;">
          <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
          </svg>
        </div>
      </div>

      <!-- 2 Clean, Generous Editorial Cards Side-by-Side (Exactly 2 RNFs from TPI) -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 20px;">
        
        <!-- RNF 1: Módulo Web de Soporte -->
        <div class="card-dark reveal-item revealed" style="border-top: 4px solid var(--blue-accent); padding: 32px 28px; background: rgba(14, 31, 58, 0.75); border-radius: 14px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #93C5FD; background: rgba(45, 127, 249, 0.16); border: 1px solid rgba(45, 127, 249, 0.32); padding: 5px 12px; border-radius: 6px; text-transform: uppercase;">
                Arquitectura &bull; Acceso Web Ubicuo
              </span>
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>

            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.01em;">
              RNF 1 &bull; Módulo Web de Soporte
            </div>

            <div style="font-size: 15px; line-height: 1.7; color: #F1F5F9; background: rgba(255,255,255,0.04); border-left: 3px solid #2D7FF9; padding: 18px 20px; border-radius: 0 10px 10px 0; margin-bottom: 22px;">
              "El sistema deberá implementarse bajo una <strong>arquitectura web cliente-servidor</strong> accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo."
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 18px;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Arquitectura Web Cliente-Servidor:</strong> Servicios centralizados y persistencia relacional.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Navegadores Modernos:</strong> Acceso universal sin dependencias de plugins o runtime local.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #60A5FA; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Zero-Install:</strong> Mantenimiento centralizado con cero sobrecarga en terminales del museo.</span>
            </div>
          </div>
        </div>

        <!-- RNF 2: Interfaz móvil para rondas -->
        <div class="card-dark reveal-item revealed" style="border-top: 4px solid #38BDF8; padding: 32px 28px; background: rgba(14, 31, 58, 0.75); border-radius: 14px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
              <span style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; color: #38BDF8; background: rgba(56, 189, 248, 0.16); border: 1px solid rgba(56, 189, 248, 0.32); padding: 5px 12px; border-radius: 6px; text-transform: uppercase;">
                Usabilidad &bull; Terminal Táctil para Guardias
              </span>
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="4" y="2" width="16" height="20" rx="2" ry="2"/>
                <line x1="12" y1="18" x2="12.01" y2="18"/>
              </svg>
            </div>

            <div style="font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.01em;">
              RNF 2 &bull; Interfaz móvil para rondas
            </div>

            <div style="font-size: 15px; line-height: 1.7; color: #F1F5F9; background: rgba(255,255,255,0.04); border-left: 3px solid #38BDF8; padding: 18px 20px; border-radius: 0 10px 10px 0; margin-bottom: 22px;">
              "La aplicación deberá contar con una <strong>interfaz responsiva y táctil adaptada para tablets</strong>, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia."
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 18px;">
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #CBD5E1;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Interfaz Táctil en Tablet:</strong> Ergonomía y botones de alto contraste para rondas en movimiento.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #38BDF8; font-weight: bold; font-size: 14px;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Plano Interactivo:</strong> Navegación espacial de salas para selección y verificación visual in situ.</span>
            </div>
            <div style="display: flex; gap: 10px; align-items: center; font-size: 13.5px; color: #38BDF8; font-weight: bold; font-size: 14px;">
              <span style="color: #38BDF8; font-weight: bold; font-size: 14px;">✔</span>
              <span><strong>Reporte Inmediato:</strong> Registro en caliente que alimenta al instante la base de datos (RN-2).</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Reference Bar -->
      <div style="padding: 14px 22px; background: rgba(14, 31, 58, 0.55); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          <span style="font-size: 13px; color: #94A3B8;">
            <strong style="color: #60A5FA;">Fidelidad al TPI:</strong> La Sección 2.4 define formalmente estos dos requerimientos no funcionales como condicionantes rectores de despliegue y usabilidad.
          </span>
        </div>
        <span style="font-size: 11px; font-weight: 700; color: #93C5FD; background: rgba(45, 127, 249, 0.15); border: 1px solid rgba(45, 127, 249, 0.3); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">
          Sección 2.4 &bull; 2 RNFs Formales
        </span>
      </div>

    </div>

    <!-- SLIDE 9: DCU GENERAL (MAXIMIZADO ALTO, SIN BANDAS NEGRAS, SIN CUADRITOS NEGROS) -->
    <div class="slide" id="slide-9" data-topic="09 · Casos de Uso">
      <div class="breadcrumb-tag">09 &bull; Frontera del Software</div>
      <h1 class="giant-title">Diagrama de Casos de Uso</h1>
      <p class="editorial-subtitle">
        Vista panorámica de los 42 Casos de Uso del sistema (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 620px 1fr; gap: 24px; align-items: stretch;">
        <!-- Columna Izquierda: Diagrama en proporción vertical exacta (sin bandas negras) -->
        <div style="display: flex; flex-direction: column;">
          <!-- Presets Sectorizados por Actor -->
          <div class="preset-focus-bar" style="margin-bottom: 10px; display: flex; flex-wrap: wrap; gap: 6px;">
            <span style="font-size: 11.5px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 2px;">Sectorizar:</span>
            <button class="preset-btn active" onclick="setDcuSector('all', this)" style="padding: 4px 10px; font-size: 11.5px;">Ver Todo (42 CUs)</button>
            <button class="preset-btn" onclick="setDcuSector('guardia', this)" style="padding: 4px 10px; font-size: 11.5px;">Guardia</button>
            <button class="preset-btn" onclick="setDcuSector('supervisor', this)" style="padding: 4px 10px; font-size: 11.5px;">Supervisor</button>
            <button class="preset-btn" onclick="setDcuSector('ingreso', this)" style="padding: 4px 10px; font-size: 11.5px;">Ingreso</button>
            <button class="preset-btn" onclick="setDcuSector('admin', this)" style="padding: 4px 10px; font-size: 11.5px;">Admin</button>
          </div>

          <!-- Marco del diagrama: Proporción vertical ajustada a 0.868 para eliminar bandas laterales -->
          <div class="card-dark reveal-item revealed" style="height: 750px; padding: 10px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 16px; box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45); border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; background: #121212; border-radius: 10px; width: 100%; height: 100%;">
              <img id="dcu-img" src="{b64_dcu}" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in; transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1);" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
              <span style="font-size: 12px; font-weight: 600; color: #CBD5E1;">42 CUs &bull; Clic para zoom interactivo</span>
              <button class="btn-primary" style="min-height: 34px; padding: 0 14px; font-size: 12px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (42 CUs)')">
                Ampliar {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <!-- Columna Derecha: Explicación limpia, continua y elegante (SIN CUADRITOS NEGROS) -->
        <div class="card-dark reveal-item revealed" style="padding: 28px 28px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Frontera del Software &bull; Sección 2.7</div>
            <h3 style="font-size: 20px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Organización de los 42 Casos de Uso</h3>
            <p style="font-size: 13.5px; line-height: 1.6; color: var(--text-light); margin-bottom: 20px;">
              El modelo delimita taxativamente las funciones del software mediante 42 casos de uso numerados de forma unívoca, estructurados según los cuatro actores clave del dominio:
            </p>

            <div style="display: flex; flex-direction: column; gap: 16px; padding-left: 4px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Guardia de Vigilancia (CU 13 al CU 17)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Rondas presenciales y reporte in situ con tablet táctil: <strong>CU-14 (Revisar sala)</strong> y <strong>CU-15 (Registrar incidente)</strong> como nexo operativo principal.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Supervisor de Seguridad (CU 18 al CU 23)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Análisis y control: seguimiento de novedades no resueltas, análisis de patrones de recurrencia y definición del plan de acción (taller de restauración o baja).
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Ingreso y Ciclo de Obras (CU 01 al CU 04)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Gestión patrimonial: ingreso de obras, derivación a restauración externa y cumplimiento riguroso de la <strong>Regla de Negocio 1</strong> (reingreso obligatorio a depósito).
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 14px;">
                <div style="font-size: 13.5px; font-weight: 800; color: #93C5FD; margin-bottom: 3px;">
                  Administración y Catálogos (CU 24 al CU 42)
                </div>
                <div style="font-size: 13px; color: var(--text-light); line-height: 1.5;">
                  Mantenimiento de tablas maestras: salas, materiales, tipos de daño, guías, tarifas y administración de accesos del sistema.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 10px; padding: 12px 14px; margin-top: 20px;">
            <div style="font-size: 12.5px; color: #93C5FD; line-height: 1.45;">
              💡 <em>Usá los botones de la barra superior para enfocar automáticamente cada sector por actor, o hacé clic sobre el diagrama para navegarlo con zoom libre.</em>
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
<!-- SLIDE 11: PROTOTIPO DE PANTALLA (CLEAN MOCKUP) -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo UI</div>
      <h1 class="giant-title">Prototipo de Interfaz</h1>
      <p class="editorial-subtitle">
        Interfaz táctil para tablet de guardia y correspondencia con la plantilla (Sección 2.8 y 2.9 del TPI)
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
            <div style="font-size: 12px; font-weight: 700; color: #38BDF8; text-transform: uppercase; margin-bottom: 6px;">3. Confirmación y Registro (Pasos 9 a 12)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El sistema solicita confirmación del incidente, el guardia confirma y la obra pasa a estado 'Inactivo' con registro de hora del servidor.
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
    <!-- SLIDE 12: DIAGRAMA DE CLASES (MAXIMIZADO AL MÁXIMO, SIN TIRA INFERIOR, SIN CUADRITOS NEGROS) -->
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases">
      <div class="breadcrumb-tag">12 &bull; Modelo de Dominio</div>
      <h1 class="giant-title">Diagrama de Clases</h1>
      <p class="editorial-subtitle">
        Diagrama de Clases del Dominio completo (Sección 2.10 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1fr 280px; gap: 20px; align-items: stretch;">
        <!-- Columna Izquierda: Diagrama de clases maximizado en alto y ancho (~1060px x 740px) -->
        <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="height: 740px; display: flex; flex-direction: column; padding: 10px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 16px 44px rgba(0, 0, 0, 0.45);">
          <div style="flex: 1; overflow: hidden; position: relative; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; background: #121212; border-radius: 10px;">
            <img id="dcd-img" src="{b64_dcd}" class="diagram-preview-img" style="height: 100%; width: 100%; object-fit: contain; cursor: zoom-in;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')" alt="DCD General">
          </div>
          <div class="diagram-action-bar" style="margin-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
            <span style="font-size: 12.5px; font-weight: 600; color: #CBD5E1;">Clases, Atributos y Métodos &bull; Visualización de Dominio</span>
            <button class="btn-primary" style="min-height: 36px; padding: 0 16px; font-size: 12.5px;" onclick="openZoomModal('b64_dcd', 'Diagrama de Clases del Dominio')">
              Ampliar {svg_expand}
            </button>
          </div>
        </div>

        <!-- Columna Derecha: Síntesis conceptual continua y limpia (SIN CUADRITOS NEGROS) -->
        <div class="card-dark reveal-item revealed" style="padding: 26px 22px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div class="breadcrumb-tag" style="margin-bottom: 8px;">Modelo de Dominio</div>
            <h3 style="font-size: 19px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.01em;">Lógica Estructural</h3>
            <p style="font-size: 13px; line-height: 1.55; color: var(--text-light); margin-bottom: 18px;">
              Entidades y relaciones estructurales especificadas en la Sección 2.10 del TPI:
            </p>

            <div style="display: flex; flex-direction: column; gap: 15px; padding-left: 2px;">
              <div style="border-left: 3px solid var(--blue-accent); padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Gestión de Incidentes</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La entidad <code>Incidente</code> documenta fecha, hora y descripción, vinculada a su <code>TipoIncidente</code> y a la <code>Obra</code> afectada.
                </div>
              </div>

              <div style="border-left: 3px solid #60A5FA; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Obra y Estados</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  <code>Obra</code> encapsula autor, estilo, dimensiones y material (para sugerir acciones inmediatas), transicionando a <em>'Inactivo'</em> ante daño.
                </div>
              </div>

              <div style="border-left: 3px solid #38BDF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Vigilancia y Rondas</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  La relación entre <code>Guardia</code> y <code>Sala</code> se asienta mediante la clase asociativa <code>SalaXGuardia</code>, auditando fecha y hora de ronda.
                </div>
              </div>

              <div style="border-left: 3px solid #818CF8; padding-left: 12px;">
                <div style="font-size: 13px; font-weight: 800; color: #93C5FD; margin-bottom: 2px;">Depósito (Regla 1)</div>
                <div style="font-size: 12.5px; color: var(--text-light); line-height: 1.45;">
                  Toda obra derivada a <code>Restaurador</code> debe ingresar obligatoriamente a la clase <code>Deposito</code> antes de reasignarse.
                </div>
              </div>
            </div>
          </div>

          <div style="background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; padding: 10px 12px; margin-top: 14px;">
            <div style="font-size: 12px; color: #93C5FD; line-height: 1.4;">
              💡 <em>Hacé clic en el diagrama o en 'Ampliar' para explorar todas las clases, atributos y métodos en alta resolución.</em>
            </div>
          </div>
        </div>
      </div>
    </div>
<!-- SLIDE 13: TRAZABILIDAD (AMPLIADA, LEGIBLE Y SIN CHAMUYO) -->
    <div class="slide" id="slide-13" data-topic="13 · Trazabilidad de Requerimientos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 14px;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Trazabilidad de Requerimientos</div>
          <h1 class="giant-title">Trazabilidad de Requerimientos</h1>
          <p class="editorial-subtitle">
            Correspondencia: Requerimiento Funcional (RF) &rarr; Caso(s) de Uso Asociado(s) &rarr; Clases del Dominio (DCD)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 6px;">
          <svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="18" cy="5" r="3"/>
            <circle cx="6" cy="12" r="3"/>
            <circle cx="18" cy="19" r="3"/>
            <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/>
            <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/>
          </svg>
        </div>
      </div>

      <!-- Filter Controls Bar -->
      <div style="display: flex; gap: 14px; align-items: center; margin-bottom: 14px;">
        <input type="text" id="trace-search-input" class="search-input" placeholder="🔍 Filtrar trazabilidad (ej: RF-35, obra, sala, ronda, incidente)..." oninput="filterTraceMatrix()" style="flex: 1; height: 44px; background: rgba(10, 22, 40, 0.7); border: 1px solid rgba(255,255,255,0.15); border-radius: 10px; padding: 0 18px; color: #FFF; font-size: 14px;">
        
        <div class="trace-module-pills" style="margin-bottom: 0; display: flex; gap: 8px;">
          <button class="trace-module-btn active" onclick="filterTraceModule(this, 'ALL')">Todos (34)</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'INCIDENTES')">Incidentes y Rondas</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'OBRAS')">Obras y Depósito</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'MAESTROS')">Salas y Maestros</button>
          <button class="trace-module-btn" onclick="filterTraceModule(this, 'REPORTES')">Informes</button>
        </div>
      </div>

      <!-- Interactive Trace Matrix Console -->
      <div class="trace-matrix-console reveal-item revealed" style="margin-bottom: 0;">
        <!-- Left Column: Requerimientos Funcionales -->
        <div style="display: flex; flex-direction: column;">
          <div style="font-size: 12px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 10px;">
            Requerimientos Funcionales del Sistema:
          </div>
          <div class="trace-rf-list" id="trace-items-container">
            <!-- Dynamically populated items -->
          </div>
        </div>

        <!-- Right Column: Detail Dossier of Selected Trace Link -->
        <div class="trace-impact-dossier" id="trace-dossier-panel">
          <div>
            <!-- Header of Selected RF -->
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 14px; margin-bottom: 16px;">
              <div>
                <span style="font-size: 12.5px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.05em;" id="td-rf-code">REQUERIMIENTO FUNCIONAL RF-35</span>
                <div style="font-size: 22px; font-weight: 800; color: #FFF; margin-top: 3px;" id="td-rf-name">Registrar incidente</div>
              </div>
              <span style="font-size: 13.5px; font-weight: 800; background: var(--blue-accent); color: #FFF; padding: 6px 14px; border-radius: 8px;" id="td-cu-badge">CU-15</span>
            </div>

            <!-- IDEA 2: DYNAMIC TRACE PIPELINE (3 CONNECTED NODES) -->
            <div class="trace-pipeline-container">
              <div class="pipeline-node" style="background: rgba(45, 127, 249, 0.12); border: 1.5px solid #2D7FF9;">
                <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase;">1. Requerimiento (RF)</div>
                <div id="pipe-rf" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">RF-35: Registrar incidente</div>
              </div>

              <div class="pipeline-arrow">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </div>

              <div class="pipeline-node" style="background: rgba(56, 189, 248, 0.12); border: 1.5px solid #38BDF8;">
                <div style="font-size: 11px; font-weight: 800; color: #7DD3FC; text-transform: uppercase;">2. Caso de Uso (DCU)</div>
                <div id="pipe-cu" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">CU-15 (Guardia)</div>
              </div>

              <div class="pipeline-arrow">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </div>

              <div class="pipeline-node" style="background: rgba(129, 140, 248, 0.12); border: 1.5px solid #818CF8;">
                <div style="font-size: 11px; font-weight: 800; color: #C7D2FE; text-transform: uppercase;">3. Clases Dominio (DCD)</div>
                <div id="pipe-dcd" style="font-size: 13.5px; font-weight: 700; color: #FFFFFF; margin-top: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Incidente &bull; Obra</div>
              </div>
            </div>

            <!-- Concept clarification note on traceability -->
            <div style="font-size: 13px; color: #94A3B8; background: rgba(255,255,255,0.03); padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.07); margin-bottom: 14px;">
              💡 <strong>Correspondencia en ASI:</strong> Cada requerimiento funcional se concreta a través de uno o más Casos de Uso del sistema, los cuales interactúan con las clases del dominio para capturar y persistir los datos.
            </div>
            <!-- 3 Clean Structured Cards -->
            <div style="display: flex; flex-direction: column; gap: 14px;">
              
              <!-- Card 1: Caso de Uso Asociado -->
              <div style="background: rgba(255,255,255,0.035); border-left: 3px solid #2D7FF9; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #60A5FA; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Caso de Uso Asociado (DCU)</span>
                <span id="td-cu-info" style="color: #FFF; font-weight: 700; font-size: 15px;">CU-15: Registrar incidente &bull; Actor: Encargado de vigilancia</span>
              </div>

              <!-- Card 2: Clases del Dominio Afectadas -->
              <div style="background: rgba(255,255,255,0.035); border-left: 3px solid #38BDF8; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #38BDF8; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Clases del Dominio Afectadas (DCD)</span>
                <span id="td-dcd-info" style="color: #E2E8F0; font-size: 14.5px; line-height: 1.55;">
                  <strong>Clases:</strong> <code>Incidente</code>, <code>TipoIncidente</code>, <code>Obra</code>, <code>Estado</code>.<br>
                  <strong>Método invocado:</strong> <code>obra.registrarIncidente()</code> actualiza puntero a Estado 'Inactivo'.
                </span>
              </div>

              <!-- Card 3: Justificación Concreta -->
              <div style="background: rgba(45,127,249,0.08); border-left: 3px solid #60A5FA; padding: 14px 18px; border-radius: 0 10px 10px 0;">
                <span style="color: #93C5FD; font-weight: 800; display: block; font-size: 12px; text-transform: uppercase; margin-bottom: 4px; letter-spacing: 0.04em;">Explicación de la Trazabilidad</span>
                <span id="td-rationale" style="color: #CBD5E1; font-size: 14px; line-height: 1.55;">
                  El requerimiento define el registro del daño. El CU-15 materializa el flujo en pantalla, y el DCD persiste el hecho en la entidad Incidente vinculada a TipoIncidente y a la Obra.
                </span>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 14: CIERRE & AGRADECIMIENTO (ESTÉTICO, INSTITUCIONAL Y COMPACTO) -->
    <div class="slide" id="slide-14" data-topic="14 · Cierre y Agradecimiento">
      
      <!-- Top Hero Header -->
      <div class="card-dark" style="margin-bottom: 18px; position: relative; overflow: hidden; padding: 32px 36px; text-align: center;">
        <div style="position: absolute; right: -30px; top: -30px; opacity: 0.06; pointer-events: none;">
          <svg width="280" height="280" viewBox="0 0 200 200" fill="none">
            <circle cx="100" cy="100" r="90" stroke="#2F6BFF" stroke-width="12"/>
            <path d="M40 100 L85 145 L160 65" stroke="#2F6BFF" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>

        <div class="breadcrumb-tag" style="display: inline-flex; margin-bottom: 10px;">
          {svg_check} Defensa Oral Finalizada &bull; Trabajo Práctico Integrador
        </div>
        <h1 class="giant-title" style="margin-bottom: 8px; font-size: 56px; letter-spacing: -0.02em;">¡Muchas Gracias!</h1>
        <p class="editorial-subtitle" style="max-width: 720px; margin: 0 auto 18px auto; font-size: 15px;">
          Sistema de Gestión y Vigilancia Museológica &bull; Museo de Historia Natural
        </p>

        <div style="display: flex; justify-content: center; align-items: center; gap: 14px;">
          <button class="btn-primary" onclick="goToSlide(1)" style="min-height: 44px; padding: 0 22px; font-size: 13.5px;">
            Volver al inicio ↺
          </button>
          <button class="btn-secondary" onclick="openOverviewModal()" style="min-height: 44px; padding: 0 20px; font-size: 13.5px;">
            {svg_grid} Ver los 14 slides
          </button>
        </div>
      </div>

      <!-- Main Split: Institutional & Professors (Left) vs Compact Team Members (Right) -->
      <div style="display: grid; grid-template-columns: 0.95fr 1.05fr; gap: 18px;">
        
        <!-- Columna Izquierda: Cátedra, Comisión y Docentes -->
        <div class="card-dark" style="padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 16px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 14px;">
              <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(45, 127, 249, 0.15); border: 1px solid rgba(45, 127, 249, 0.35); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                  <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
                </svg>
              </div>
              <div>
                <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.06em;">Marco Académico</div>
                <div style="font-size: 16px; font-weight: 800; color: #FFFFFF;">UTN &bull; Facultad Regional Córdoba</div>
                <div style="font-size: 12px; color: var(--text-light-secondary);">Ingeniería en Sistemas de Información</div>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 16px;">
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px 12px;">
                <span style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; display: block;">Cátedra</span>
                <strong style="font-size: 13.5px; color: #FFF;">Análisis de Sistemas (ASI)</strong>
              </div>
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 10px 12px;">
                <span style="font-size: 11px; font-weight: 700; color: #93C5FD; text-transform: uppercase; display: block;">Comisión y Ciclo</span>
                <strong style="font-size: 13.5px; color: #FFF;">Curso 2K10 &bull; Año 2026</strong>
              </div>
            </div>

            <!-- Docentes Evaluadores -->
            <div>
              <div style="font-size: 11px; font-weight: 800; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">
                Equipo Docente Evaluador:
              </div>
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid var(--blue-accent);">
                  Ing. Cattaneo, Marcela F.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #60A5FA;">
                  Ing. Turanzas, Susana B.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #38BDF8;">
                  Ing. Sanchez, Claudia E.
                </div>
                <div style="font-size: 13px; color: #E2E8F0; background: rgba(255,255,255,0.025); padding: 8px 12px; border-radius: 6px; border-left: 2px solid #818CF8;">
                  Padilla, Tomas Lautaro
                </div>
              </div>
            </div>
          </div>

          <div style="margin-top: 14px; padding: 10px 14px; background: rgba(45, 127, 249, 0.08); border: 1px solid rgba(45, 127, 249, 0.2); border-radius: 8px; font-size: 12px; color: #93C5FD;">
            🎓 <em>Agradecemos a la cátedra por el acompañamiento y las devoluciones formativas durante el ciclo lectivo.</em>
          </div>
        </div>

        <!-- Columna Derecha: 9 Integrantes (Compacto, Prolijo y Elegante) -->
        <div class="card-dark" style="padding: 24px 26px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 12px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2D7FF9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                  <circle cx="9" cy="7" r="4"/>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
                <span style="font-size: 15px; font-weight: 800; color: #FFFFFF;">Equipo de Trabajo &bull; Grupo 6</span>
              </div>
              <span style="font-size: 11px; font-weight: 800; background: rgba(45, 127, 249, 0.2); color: #93C5FD; border: 1px solid rgba(45, 127, 249, 0.35); padding: 3px 10px; border-radius: 12px;">
                9 Integrantes
              </span>
            </div>

            <!-- 3x3 Compact Member Grid -->
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
              
              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Tarditti, Juan S.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 400212</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Thomas Rapp, F.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 408990</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Abad, Francisco</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 423269</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Molina, Tobias</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419749</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Moyano, Lucas U.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 410975</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Pereyra, Kevin</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 418201</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Marcuzzi, Tomas</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 403382</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Cufre, Agustín</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 419166</div>
              </div>

              <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 10px 10px;">
                <div style="font-size: 12.5px; font-weight: 700; color: #FFF; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Jastrzebski, E.</div>
                <div style="font-size: 11px; color: #60A5FA; font-family: monospace; margin-top: 2px;">Leg. 402760</div>
              </div>

            </div>
          </div>

          <div style="margin-top: 14px; padding: 10px 14px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; text-align: center; font-size: 12px; color: var(--text-light-secondary);">
            Quedamos a total disposición de la mesa evaluadora para responder a sus preguntas.
          </div>
        </div>

      </div>
    </div>

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

    <div class="dock-counter-badge" id="dock-counter-text">01 / 14</div>

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
    const totalSlides = 14;

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
      "13 · Trazabilidad de Requerimientos",
      "14 · Cierre y Agradecimiento"
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
        renderTraceMatrixItems();
    initExclusiveAccordion();
    updateSlide();
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 1) {{
        currentSlide--;
        renderTraceMatrixItems();
    initExclusiveAccordion();
    updateSlide();
      }}
    }}

    function goToSlide(n) {{
      if (n >= 1 && n <= totalSlides) {{
        currentSlide = n;
        renderTraceMatrixItems();
    initExclusiveAccordion();
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

    // ========================================================
    // PRECISE DCU SECTOR ZOOM (MATHEMATICALLY CENTERED)
    // ========================================================
    function setDcuSector(sector, btn) {{
      const img = document.getElementById('dcu-img');
      if (!img) return;
      if (btn) {{
        const btns = btn.parentElement.querySelectorAll('.preset-btn');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }}
      if (sector === 'guardia') {{
        // Guardia de vigilancia: act_vigilancia (CU 13, 14, 15, 16, 17)
        img.style.transformOrigin = '19% 62%';
        img.style.transform = 'scale(2.5)';
      }} else if (sector === 'supervisor') {{
        // Supervisor: act_seguridad (CU 18, 19, 20, 21, 22, 23)
        img.style.transformOrigin = '19% 86%';
        img.style.transform = 'scale(2.4)';
      }} else if (sector === 'ingreso') {{
        // Responsable de ingreso de obra: act_obras (CU 1, 2, 3, 4)
        img.style.transformOrigin = '19% 11%';
        img.style.transform = 'scale(2.4)';
      }} else if (sector === 'admin') {{
        // Admin de sistema: act_admin_sist (CU 24..42 Tablas Maestras)
        img.style.transformOrigin = '74% 18%';
        img.style.transform = 'scale(2.3)';
      }} else {{
        // Ver Todo (42 CUs)
        img.style.transformOrigin = 'center center';
        img.style.transform = 'scale(1)';
      }}
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
    
    // ========================================================
    // COMPREHENSIVE TRACEABILITY MATRIX (RF <-> CU <-> DCD)
    // ========================================================
    const fullTraceData = [
      {{
        rf: 'RF-01',
        name: 'Registrar ingreso de obra',
        cat: 'OBRAS',
        cu: 'CU-01 Registrar ingreso de obra',
        actor: 'Responsable de ingreso de obra',
        dcd: 'Obra, Autor, Estilo, Material, TipoObra, TipoIngreso',
        methods: 'obra.crear(), autor.asociar(), estilo.vincular()',
        rationale: 'Da de alta la obra en el inventario patrimonial. El CU-01 captura los datos y el DCD persiste la entidad Obra asociada a sus catálogos maestros de clasificación.'
      }},
      {{
        rf: 'RF-02',
        name: 'Consultar obra',
        cat: 'OBRAS',
        cu: 'CU-03 Consultar obra',
        actor: 'Responsable de ingreso, Supervisor',
        dcd: 'Obra, Estado, Sala, Exposicion',
        methods: 'obra.getDatos(), obra.getEstadoActual()',
        rationale: 'Permite consultar la ficha técnica y localización de cualquier obra. En el DCD se materializa mediante las asociaciones de Obra con Estado y Sala.'
      }},
      {{
        rf: 'RF-03',
        name: 'Registrar baja de obra',
        cat: 'OBRAS',
        cu: 'CU-42 Registrar baja de obra',
        actor: 'Admin de sistema, Supervisor',
        dcd: 'Obra, Estado',
        methods: 'obra.darDeBaja(), estado.transicionar("Baja")',
        rationale: 'Formaliza la salida del catálogo de una obra irrecuperable o dada de baja. Actualiza el puntero de Estado en el DCD para auditoría histórica.'
      }},
      {{
        rf: 'RF-04',
        name: 'Registrar tipo de obra',
        cat: 'MAESTROS',
        cu: 'CU-05 / Parámetros Maestros',
        actor: 'Admin de sistema',
        dcd: 'TipoObra',
        methods: 'tipoObra.crear()',
        rationale: 'Parametriza los tipos (escultura, pintura, objeto animado). En el DCD alimenta la clasificación consumida por la entidad Obra.'
      }},
      {{
        rf: 'RF-07',
        name: 'Registrar tipo de material',
        cat: 'MAESTROS',
        cu: 'CU-28 Registrar tipo de material',
        actor: 'Admin de sistema',
        dcd: 'Material',
        methods: 'material.crear()',
        rationale: 'Normaliza los materiales artísticos (óleo, lienzo, bronce). El DCD vincula Material con Obra para calibrar protocolos de conservación.'
      }},
      {{
        rf: 'RF-10',
        name: 'Registrar sala',
        cat: 'MAESTROS',
        cu: 'CU-24 Registrar sala nueva',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.crear()',
        rationale: 'Da de alta espacios de exhibición física. En el DCD la Sala es el contenedor espacial de las Obras y el destino de las Rondas.'
      }},
      {{
        rf: 'RF-11',
        name: 'Consultar sala',
        cat: 'MAESTROS',
        cu: 'CU-27 Consultar salas',
        actor: 'Admin de sistema, Supervisor',
        dcd: 'Sala, Obra',
        methods: 'sala.getObrasExpuestas()',
        rationale: 'Permite inspeccionar la ocupación y obras activas en sala. En el DCD navega la relación Sala-Obra (1 a 1..*).'
      }},
      {{
        rf: 'RF-12',
        name: 'Modificar sala',
        cat: 'MAESTROS',
        cu: 'CU-25 Modificar sala',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.modificarDatos()',
        rationale: 'Actualiza nombre, capacidad o aforo. Modifica los atributos de la entidad Sala en el DCD.'
      }},
      {{
        rf: 'RF-13',
        name: 'Registrar baja de sala',
        cat: 'MAESTROS',
        cu: 'CU-26 Registrar baja de sala',
        actor: 'Admin de sistema',
        dcd: 'Sala',
        methods: 'sala.darDeBaja()',
        rationale: 'Inhabilita una sala por reformas. Valida que no contenga obras activas antes de persistir la baja en el DCD.'
      }},
      {{
        rf: 'RF-14',
        name: 'Registrar guía',
        cat: 'MAESTROS',
        cu: 'CU-35 Registrar alta de guía',
        actor: 'Admin de sistema',
        dcd: 'Guia',
        methods: 'guia.crear()',
        rationale: 'Incorpora personal al cuerpo de guías. Persiste datos de contacto e idiomas en la entidad Guia del DCD.'
      }},
      {{
        rf: 'RF-15',
        name: 'Consultar guía',
        cat: 'MAESTROS',
        cu: 'CU-38 Consultar guía',
        actor: 'Admin de sistema, Encargado',
        dcd: 'Guia, VisitaGuiada',
        methods: 'guia.getAgenda()',
        rationale: 'Permite revisar la carga horaria y recorridos asignados a un guía en el DCD.'
      }},
      {{
        rf: 'RF-18',
        name: 'Registrar estilo de obra',
        cat: 'MAESTROS',
        cu: 'CU-39 Registrar estilo de obra',
        actor: 'Admin de sistema',
        dcd: 'Estilo',
        methods: 'estilo.crear()',
        rationale: 'Estandariza corrientes históricas (barroco, cubismo, renacentista) asociadas a las Obras en el DCD.'
      }},
      {{
        rf: 'RF-19',
        name: 'Consultar estilo de obra',
        cat: 'MAESTROS',
        cu: 'CU-41 Consultar estilo de obra',
        actor: 'Admin de sistema',
        dcd: 'Estilo',
        methods: 'estilo.listar()',
        rationale: 'Provee el catálogo consumido durante el alta de obras y curaduría de muestras.'
      }},
      {{
        rf: 'RF-21',
        name: 'Registrar tipo de incidente',
        cat: 'MAESTROS',
        cu: 'CU-31 Registrar tipo de incidente',
        actor: 'Admin de sistema',
        dcd: 'TipoIncidente',
        methods: 'tipoIncidente.crear()',
        rationale: 'Define las tipologías de daño (deterioro natural, provocado, caída accidental). En el DCD es mandatorio para Incidente (1 a 1).'
      }},
      {{
        rf: 'RF-22',
        name: 'Consultar tipo de incidente',
        cat: 'MAESTROS',
        cu: 'CU-34 Consultar tipo de incidente',
        actor: 'Admin de sistema, Guardia',
        dcd: 'TipoIncidente',
        methods: 'tipoIncidente.listarActivos()',
        rationale: 'Suministra las opciones mostradas en el selector del formulario táctil del CU-15 en tablet.'
      }},
      {{
        rf: 'RF-24',
        name: 'Registrar programación de exposiciones',
        cat: 'MAESTROS',
        cu: 'CU-05 Registrar programación de exposiciones',
        actor: 'Administrador del museo',
        dcd: 'Exposicion, Obra, Sala',
        methods: 'exposicion.planificar(), obra.asignarSala()',
        rationale: 'Cronograma de muestras artísticas. Asocia obras a salas específicas durante un período determinado en el DCD.'
      }},
      {{
        rf: 'RF-25',
        name: 'Consultar programación de exposiciones',
        cat: 'MAESTROS',
        cu: 'CU-06 Consultar exposiciones',
        actor: 'Administrador del museo, Público',
        dcd: 'Exposicion, Sala',
        methods: 'exposicion.listarVigentes()',
        rationale: 'Permite consultar cartelera y salas asignadas. En el DCD consulta la entidad Exposicion.'
      }},
      {{
        rf: 'RF-26',
        name: 'Registrar planificación de visitas guiadas',
        cat: 'MAESTROS',
        cu: 'CU-08 Registrar planificación de visitas',
        actor: 'Administrador del museo',
        dcd: 'VisitaGuiada, Guia, Sala',
        methods: 'visita.crear(), guia.asignar()',
        rationale: 'Agenda recorridos pedagógicos coordinando guía y salas en el DCD.'
      }},
      {{
        rf: 'RF-27',
        name: 'Consultar planificación de visitas guiadas',
        cat: 'MAESTROS',
        cu: 'CU-07 Consultar visitas guiadas',
        actor: 'Administrador del museo',
        dcd: 'VisitaGuiada',
        methods: 'visita.listarPorFecha()',
        rationale: 'Control de aforo y visitas confirmadas para evitar superposiciones con las rondas de guardia.'
      }},
      {{
        rf: 'RF-28',
        name: 'Consultar agenda de guías',
        cat: 'MAESTROS',
        cu: 'CU-11 Consultar agenda de guías',
        actor: 'Administrador del museo, Guía',
        dcd: 'Guia, VisitaGuiada',
        methods: 'guia.getDisponibilidad()',
        rationale: 'Verifica disponibilidad del personal para asignación de nuevos recorridos en el DCD.'
      }},
      {{
        rf: 'RF-29',
        name: 'Registrar venta de entrada',
        cat: 'MAESTROS',
        cu: 'CU-09 Registrar venta de entrada',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada, Tarifa, Visitante',
        methods: 'entrada.emitir(), tarifa.calcular()',
        rationale: 'Regula el ingreso de público y cobro de tarifas. Persiste la venta en la entidad Entrada del DCD.'
      }},
      {{
        rf: 'RF-30',
        name: 'Contratar servicio adicional de guía',
        cat: 'MAESTROS',
        cu: 'CU-10 Registrar servicio adicional de guía',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada, Guia',
        methods: 'entrada.agregarServicioGuia()',
        rationale: 'Adiciona el guiado profesional a la entrada del visitante en el DCD.'
      }},
      {{
        rf: 'RF-31',
        name: 'Consultar venta de entrada',
        cat: 'MAESTROS',
        cu: 'CU-32 Consultar venta de entrada',
        actor: 'Responsable de atención al cliente',
        dcd: 'Entrada',
        methods: 'entrada.getDetalle()',
        rationale: 'Auditoría de recaudación y cantidad de personas que ingresaron a las salas del museo.'
      }},
      {{
        rf: 'RF-32',
        name: 'Generar planificación de rondas de vigilancia',
        cat: 'INCIDENTES',
        cu: 'CU-12 Generar planificación de rondas',
        actor: 'Administrador web (Automático)',
        dcd: 'Guardia, Sala, SalaXGuardia',
        methods: 'guardia.asignarRonda(), salaXGuardia.crear()',
        rationale: 'Disparador automático del sistema que programa el cronograma de inspección y genera las instancias de SalaXGuardia en el DCD.'
      }},
      {{
        rf: 'RF-33',
        name: 'Consultar planificación de rondas de vigilancia',
        cat: 'INCIDENTES',
        cu: 'CU-13 Consultar planificación ronda',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'Guardia, SalaXGuardia, Sala',
        methods: 'guardia.getRondasTurno()',
        rationale: 'Permite al guardia consultar en su tablet las salas asignadas para su turno de patrullaje.'
      }},
      {{
        rf: 'RF-34',
        name: 'Registrar revisión de sala',
        cat: 'INCIDENTES',
        cu: 'CU-14 Registrar revisión de la sala',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'SalaXGuardia, Guardia, Sala',
        methods: 'salaXGuardia.marcarVerificada(), salaXGuardia.setFin()',
        rationale: 'Certifica la inspección presencial del guardia en la sala, estampando marca de tiempo en la clase asociativa SalaXGuardia.'
      }},
      {{
        rf: 'RF-35',
        name: 'Registrar incidente',
        cat: 'INCIDENTES',
        cu: 'CU-15 Registrar incidente',
        actor: 'Encargado de vigilancia (EV)',
        dcd: 'Incidente, TipoIncidente, Obra, Estado',
        methods: 'incidente.crear(), obra.registrarIncidente(), estado.setInactivo()',
        rationale: 'Núcleo del proceso de soporte (RN-2). El CU-15 persiste la entidad Incidente vinculada obligatoriamente a TipoIncidente y actualiza la Obra a estado Inactivo.'
      }},
      {{
        rf: 'RF-36',
        name: 'Consultar incidentes',
        cat: 'INCIDENTES',
        cu: 'CU-17 Consultar incidente',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra, TipoIncidente',
        methods: 'incidente.listarPendientes(), obra.getHistorial()',
        rationale: 'Permite al supervisor examinar las denuncias cargadas por los guardias para decidir derivación a talleres o bajas.'
      }},
      {{
        rf: 'RF-37',
        name: 'Registrar seguimiento de resolución de incidente',
        cat: 'INCIDENTES',
        cu: 'CU-23 Registrar seguimiento',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra',
        methods: 'incidente.actualizarResolucion()',
        rationale: 'Rastrea el informe de peritaje y los avances de la restauración de piezas afectadas.'
      }},
      {{
        rf: 'RF-40',
        name: 'Registrar obra a restaurar',
        cat: 'OBRAS',
        cu: 'CU-04 Registrar obra a restaurar',
        actor: 'Responsable de ingreso, Supervisor',
        dcd: 'Obra, Estado',
        methods: 'obra.enviarARestauracion(), estado.transicionar("En Restauración")',
        rationale: 'Documenta la salida de la pieza dañada hacia el taller especializado, transicionando su Estado en el DCD.'
      }},
      {{
        rf: 'RF-41',
        name: 'Registrar reingreso de obra al depósito',
        cat: 'OBRAS',
        cu: 'CU-02 Registrar reingreso de obra',
        actor: 'Responsable de ingreso de obra',
        dcd: 'Obra, Estado',
        methods: 'obra.registrarReingreso(), estado.transicionar("En Depósito")',
        rationale: 'Cumplimiento estricto de la Regla de Negocio 1: toda obra reparada debe reingresar indefectiblemente al depósito institucional.'
      }},
      {{
        rf: 'RF-42',
        name: 'Generar informe diario de vigilancia',
        cat: 'REPORTES',
        cu: 'CU-20 Generar informe diario de vigilancia',
        actor: 'Encargado de supervisión, Director',
        dcd: 'Incidente, SalaXGuardia, Guardia',
        methods: 'informe.consolidarTurno()',
        rationale: 'Consolida las rondas concluidas y los incidentes registrados en el día para auditoría directiva.'
      }},
      {{
        rf: 'RF-43',
        name: 'Generar reporte de patrones de incidentes',
        cat: 'REPORTES',
        cu: 'CU-18 Generar patrones de incidentes',
        actor: 'Encargado de supervisión, Director',
        dcd: 'Incidente, TipoIncidente, Sala',
        methods: 'reporte.calcularEstadisticas()',
        rationale: 'Análisis de correlación entre tipologías de incidentes y salas de mayor recurrencia para prevención de daños.'
      }},
      {{
        rf: 'RF-44',
        name: 'Emitir historial de incidentes',
        cat: 'REPORTES',
        cu: 'CU-22 Emitir historial de incidentes',
        actor: 'Encargado de supervisión',
        dcd: 'Incidente, Obra',
        methods: 'obra.getHistorialIncidentes()',
        rationale: 'Emite la hoja de vida pericial de una obra, vinculando todos los incidentes sufridos a lo largo de su custodia.'
      }}
    ];

    let currentTraceFilter = 'ALL';

    function renderTraceMatrixItems() {{
      const container = document.getElementById('trace-items-container');
      if (!container) return;
      container.innerHTML = '';

      const query = document.getElementById('trace-search-input')?.value.toLowerCase() || '';

      const filtered = fullTraceData.filter(item => {{
        const matchesCat = (currentTraceFilter === 'ALL' || item.cat === currentTraceFilter);
        const text = (item.rf + ' ' + item.name + ' ' + item.cu + ' ' + item.dcd + ' ' + item.rationale).toLowerCase();
        const matchesQuery = query === '' || text.includes(query);
        return matchesCat && matchesQuery;
      }});

      if (filtered.length === 0) {{
        container.innerHTML = '<div style="color: var(--text-light-secondary); padding: 16px; font-size: 13px;">No se encontraron requerimientos para este filtro.</div>';
        return;
      }}

      filtered.forEach((item, index) => {{
        const div = document.createElement('div');
        div.className = 'trace-rf-item' + (index === 0 ? ' active' : '');
        div.onclick = () => selectTraceDetail(div, item);
        div.innerHTML = `
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
            <strong style="color: #60A5FA; font-size: 14px; font-weight: 800; letter-spacing: 0.03em;">${{item.rf}}</strong>
            <span style="font-size: 12px; font-weight: 800; background: rgba(45, 127, 249, 0.22); color: #93C5FD; border: 1px solid rgba(45, 127, 249, 0.35); padding: 3px 8px; border-radius: 6px;">${{item.cu.split(' ')[0]}}</span>
          </div>
          <div style="font-size: 15px; color: #FFFFFF; font-weight: 600; line-height: 1.35;">${{item.name}}</div>
        `;
        container.appendChild(div);

        if (index === 0) {{
          updateTraceDossier(item);
        }}
      }});
    }}

    function selectTraceDetail(element, item) {{
      document.querySelectorAll('#trace-items-container .trace-rf-item').forEach(el => el.classList.remove('active'));
      element.classList.add('active');
      updateTraceDossier(item);
    }}

    function updateTraceDossier(item) {{
      document.getElementById('td-rf-code').innerText = 'REQUERIMIENTO FUNCIONAL ' + item.rf;
      document.getElementById('td-rf-name').innerText = item.name;
      document.getElementById('td-cu-badge').innerText = item.cu.split(' ')[0];
      document.getElementById('td-cu-info').innerHTML = `<strong>${{item.cu}}</strong> &bull; Actor: ${{item.actor}}`;
      document.getElementById('td-dcd-info').innerHTML = `<strong>Clases DCD:</strong> ${{item.dcd}}<br><strong>Métodos / Lógica:</strong> <code>${{item.methods}}</code>`;
      document.getElementById('td-rationale').innerText = item.rationale;

      // Update Dynamic Pipeline Nodes (Idea 2)
      const pipeRf = document.getElementById('pipe-rf');
      const pipeCu = document.getElementById('pipe-cu');
      const pipeDcd = document.getElementById('pipe-dcd');
      if (pipeRf) pipeRf.innerText = item.rf + ': ' + item.name;
      if (pipeCu) pipeCu.innerText = item.cu.split(' ')[0] + ' (' + item.actor + ')';
      if (pipeDcd) pipeDcd.innerText = item.dcd.replace(/<[^>]+>/g, '').split(',').slice(0, 2).join(', ');
    }}

    function filterTraceModule(btn, cat) {{
      document.querySelectorAll('.trace-module-pills .trace-module-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentTraceFilter = cat;
      renderTraceMatrixItems();
    }}

    function filterTraceMatrix() {{
      renderTraceMatrixItems();
    }}

    // ========================================================
    // REQUERIMIENTOS FUNCIONALES EXPAND / COLLAPSE
    // ========================================================
    let rfExclusiveMode = true;

    function initExclusiveAccordion() {{
      const allGroups = document.querySelectorAll('.rf-group');
      allGroups.forEach(group => {{
        const summary = group.querySelector('.rf-summary');
        if (!summary) return;
        summary.addEventListener('click', function(e) {{
          if (!rfExclusiveMode) return;
          // If group is currently closed, opening it will close all others
          const willOpen = !group.open;
          if (willOpen) {{
            allGroups.forEach(other => {{
              if (other !== group) other.open = false;
            }});
          }}
        }});
      }});
    }}

    function expandAllRf() {{
      rfExclusiveMode = false;
      document.querySelectorAll('.rf-group').forEach(g => {{
        g.style.display = 'block';
        g.open = true;
      }});
      setTimeout(() => {{ rfExclusiveMode = true; }}, 300);
    }}

    function collapseAllRf() {{
      document.querySelectorAll('.rf-group').forEach(g => {{
        g.open = false;
      }});
    }}

    function filterRequirements() {{
      const query = document.getElementById('rf-search-input').value.toLowerCase().trim();
      const groups = document.querySelectorAll('.rf-group');
      if (!query) {{
        groups.forEach(g => {{
          g.style.display = 'block';
        }});
        return;
      }}
      rfExclusiveMode = false;
      groups.forEach(g => {{
        const text = g.innerText.toLowerCase();
        if (text.includes(query)) {{
          g.style.display = 'block';
          g.open = true;
        }} else {{
          g.style.display = 'none';
          g.open = false;
        }}
      }});
      setTimeout(() => {{ rfExclusiveMode = true; }}, 300);
    }}

    // Initialize View
    renderTraceMatrixItems();
    initExclusiveAccordion();
    updateSlide();

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
  </script>
</body>
</html>
''')
    print("Pure Navy Compilation completed successfully!")

if __name__ == '__main__':
    build_presentation()
