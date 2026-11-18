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
  padding: 7px 14px;
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
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Requerimientos Funcionales y No Funcionales</div>
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
          <div style="font-size: 12.5px; color: var(--text-light-secondary); margin-top: 6px;">Prototipo de Interfaz y Trazabilidad de Requerimientos</div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 2: DOMINIO & OBJETIVOS (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 2: DOMINIO & OBJETIVOS -->
    <div class="slide" id="slide-2" data-topic="02 · Contexto y Objetivos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">02 &bull; Dominio bajo Estudio y Objetivos</div>
          <h1 class="giant-title">Dominio bajo Estudio y Objetivos de la Organización</h1>
          <p class="editorial-subtitle">
            Caso de Estudio: Museo de Historia Natural &bull; Sección 1.1 del Trabajo Práctico Integrador
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
      <h1 class="giant-title">Mapa de Procesos: Cadena de Valor del Museo</h1>
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
    <!-- SLIDE 4: PROCESO CRÍTICO & REGLAS -->
    <div class="slide" id="slide-4" data-topic="04 · Proceso Crítico y Reglas">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">04 &bull; Ficha Técnica y Reglas de Negocio</div>
          <h1 class="giant-title">Descripción del Proceso: Gestionar Incidentes y Restauración</h1>
          <p class="editorial-subtitle">
            Ficha técnica formal del proceso de soporte y reglas de negocio determinantes (Sección 2.3 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_rules_gear}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Formularios y Documentos del Proceso</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              &bull; <strong>Planificación de Ronda:</strong> Hoja de ruta generada al finalizar el día anterior que prioriza salas con más incidentes.<br>
              &bull; <strong>Registro de Incidente:</strong> Acta electrónica en Módulo Web que registra hora, pieza involucrada y tipo de siniestro.<br>
              &bull; <strong>Informe Diario de Vigilancia:</strong> Resumen consolidado de salas recorridas, incidentes y acciones realizadas.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Actividades Formales del Proceso</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              1. Visualizar en mapa la planificación de ronda de vigilancia.<br>
              2. Inspección física de sala en recorrido.<br>
              3. Registrar sala con 'Sin novedades' (si todo está en orden).<br>
              4. Registrar sala con 'Observación pendiente' y registrar incidente de forma inmediata.<br>
              5. Generar informe diario para supervisión y análisis de patrones.
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;">Regla de Negocio 1</span>
              <span style="font-size: 11px; font-weight: 700; background: rgba(47, 107, 255, 0.2); color: var(--blue-accent); padding: 3px 8px; border-radius: 4px;">MANDATORIA</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">Reingreso Obligatorio a Depósito</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-light-secondary);">
              Luego de restauradas las obras reingresan obligatoriamente al depósito del museo y quedan disponibles para lo que se las requiera. Aún si las obras no pueden restaurarse son ingresadas nuevamente al depósito para luego decidir el momento para retirarla del museo, es decir, darle de baja.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #FFFFFF;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase;">Regla de Negocio 2</span>
              <span style="font-size: 11px; font-weight: 700; background: rgba(255, 255, 255, 0.15); color: #FFFFFF; padding: 3px 8px; border-radius: 4px;">INMEDIATEZ</span>
            </div>
            <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">Registro Inmediato del Incidente</div>
            <div style="font-size: 14px; line-height: 1.55; color: var(--text-light-secondary);">
              El guardia debe registrar cada incidente de forma inmediata ante el hallazgo en la sala, indicando obligatoriamente la hora exacta, la pieza involucrada y el tipo de incidente detectado (deterioro provocado, caída accidental o deterioro natural).
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 5: BPMN DESCRIPTIVO (THEME: DARK - WHITE CANVAS)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 5: BPMN DESCRIPTIVO -->
    <div class="slide" id="slide-5" data-topic="05 · BPMN Descriptivo">
      <div class="breadcrumb-tag">05 &bull; Modelado BPMN Nivel 1 Descriptivo</div>
      <h1 class="giant-title">Modelado BPMN Nivel 1: Rondas de Vigilancia</h1>
      <p class="editorial-subtitle">
        Vista interna del proceso de negocio a nivel descriptivo (Sección 2.5 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: center;">
        <div class="diagram-frame-clean frame-white-canvas reveal-item revealed">
          <img src="{b64_bpmn_desc}" class="diagram-preview-img" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')" alt="BPMN Nivel 1">
          <div class="diagram-action-bar">
            <span style="font-size: 13px; font-weight: 600; color: #2B3B52;">BPMN Nivel 1 Descriptivo &bull; Vista General</span>
            <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_bpmn_desc', 'BPMN Nivel 1 Descriptivo')">
              Ampliar diagrama {svg_expand}
            </button>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Carril: Guardia de Vigilancia</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Inicia turno consultando el mapa de rondas, inspecciona cada sala físicamente y bifurca su acción según el estado de las obras exhibidas.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Carril: Módulo Web / Sistema</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Recibe las confirmaciones de sala, registra los incidentes con hora del servidor y consolida el informe diario al finalizar las rondas.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); text-transform: uppercase; margin-bottom: 6px;">Carril: Supervisor</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              Analiza los incidentes reportados, evalúa la seguridad, coordina derivaciones a taller y refuerza sectores conflictivos.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 6: BPMN OPERATIVO (THEME: DARK - WHITE CANVAS)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 6: BPMN OPERATIVO -->
    <div class="slide" id="slide-6" data-topic="06 · BPMN Operativo">
      <div class="breadcrumb-tag">06 &bull; Modelado BPMN Nivel 2 Operativo</div>
      <h1 class="giant-title">Modelado BPMN Nivel 2: Detalle Operativo</h1>
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
    <!-- SLIDE 7: REQUERIMIENTOS -->
    <div class="slide" id="slide-7" data-topic="07 · Requerimientos">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">07 &bull; Especificación de Requerimientos</div>
          <h1 class="giant-title">Especificación de Requerimientos y Trazabilidad</h1>
          <p class="editorial-subtitle">
            Catálogo de 45 Requerimientos Funcionales y 2 Requerimientos No Funcionales (Sección 2.4 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_req_matrix}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 24px;">
        <div class="card-dark reveal-item revealed" style="padding: 20px;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase;">Módulos del Catálogo (45 RFs)</div>
            <input type="text" id="rf-search-input" placeholder="Buscar por número o palabra..." style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #FFF; padding: 6px 12px; border-radius: 999px; font-size: 12px; outline: none;" onkeyup="filterRequirements()">
          </div>

          <div style="display: flex; flex-direction: column; gap: 8px; max-height: 440px; overflow-y: auto; padding-right: 6px;" id="rf-accordion-list">
            <details class="rf-group" open style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 10px 14px;">
              <summary style="cursor: pointer; font-weight: 700; font-size: 13.5px; color: #FFF; display: flex; justify-content: space-between;">
                <span>1. Gestión de Obras Artísticas (RF-01 a RF-11)</span>
                <span style="font-size: 11px; background: rgba(47,107,255,0.25); color: var(--blue-accent); padding: 2px 8px; border-radius: 999px;">11 RF</span>
              </summary>
              <div style="margin-top: 8px; font-size: 12.5px; color: var(--text-light-secondary); line-height: 1.5;">
                Registrar ingreso de obra (RF-01), estilo, tipo, autor, valuación, dimensiones, estado y registro de reingreso a depósito.
              </div>
            </details>

            <details class="rf-group" style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 10px 14px;">
              <summary style="cursor: pointer; font-weight: 700; font-size: 13.5px; color: #FFF; display: flex; justify-content: space-between;">
                <span>2. Exposiciones y Visitas Guiadas (RF-12 a RF-20)</span>
                <span style="font-size: 11px; background: rgba(47,107,255,0.25); color: var(--blue-accent); padding: 2px 8px; border-radius: 999px;">9 RF</span>
              </summary>
              <div style="margin-top: 8px; font-size: 12.5px; color: var(--text-light-secondary); line-height: 1.5;">
                Planificar exposiciones, definir tarifas de entrada y guía, y programar visitas para público y escuelas.
              </div>
            </details>

            <details class="rf-group" open style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 10px 14px;">
              <summary style="cursor: pointer; font-weight: 700; font-size: 13.5px; color: #FFF; display: flex; justify-content: space-between;">
                <span>3. Rondas de Vigilancia e Incidentes (RF-31 a RF-40)</span>
                <span style="font-size: 11px; background: var(--blue-accent); color: #FFF; padding: 2px 8px; border-radius: 999px;">10 RF</span>
              </summary>
              <div style="margin-top: 8px; font-size: 12.5px; color: var(--text-light); line-height: 1.5;">
                Visualizar mapa de rondas (RF-31), registrar sala sin novedades (RF-33), observación pendiente (RF-34), registrar incidente en sala (RF-35) y generar informe diario.
              </div>
            </details>

            <details class="rf-group" style="background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 10px 14px;">
              <summary style="cursor: pointer; font-weight: 700; font-size: 13.5px; color: #FFF; display: flex; justify-content: space-between;">
                <span>4. Administración y Seguridad (RF-41 a RF-45)</span>
                <span style="font-size: 11px; background: rgba(255,255,255,0.15); color: #FFF; padding: 2px 8px; border-radius: 999px;">5 RF</span>
              </summary>
              <div style="margin-top: 8px; font-size: 12.5px; color: var(--text-light-secondary); line-height: 1.5;">
                Gestión de salas, tipos de material, tipos de incidente, guías y control de acceso.
              </div>
            </details>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Trazabilidad N a M (Muchos a Muchos)</div>
            <div style="font-size: 14px; line-height: 1.6; color: var(--text-light);">
              La relación entre requerimientos y casos de uso no es 1 a 1:
              <br><br>
              &bull; <strong>Un requerimiento puede originar varios casos de uso:</strong> Por ejemplo, la necesidad de gestionar incidentes se desglosa en registrar, consultar patrones y emitir informes.<br>
              &bull; <strong>Un caso de uso cubre múltiples requerimientos:</strong> El CU-15 'Registrar incidente' satisface la búsqueda de la obra, tipificación del daño y actualización de estado.<br>
              &bull; <strong>Requerimientos que no requieren caso de uso:</strong> Reglas operativas o de integridad que se resuelven en la lógica de dominio o en la base de datos.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Requerimientos No Funcionales (RNF)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              &bull; <strong>RNF-01 (Seguridad y Autenticación):</strong> Acceso restringido por perfiles mediante usuario y contraseña.<br>
              &bull; <strong>RNF-02 (Disponibilidad y Concurrencia):</strong> Operatividad continua en tablets para el personal de vigilancia en salas.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 8: DCU GENERAL (THEME: DARK - MATCHED CANVAS #121212)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 8: DCU GENERAL -->
    <div class="slide" id="slide-8" data-topic="08 · Diagrama de Casos de Uso">
      <div class="breadcrumb-tag">08 &bull; Vista Externa del Sistema</div>
      <h1 class="giant-title">Diagrama de Casos de Uso (DCU General)</h1>
      <p class="editorial-subtitle">
        Modelo de Casos de Uso con numeración continua 1 al 42 (Sección 2.7 del TPI)
      </p>

      <div style="display: grid; grid-template-columns: 1.35fr 0.65fr; gap: 24px; align-items: stretch;">
        <div style="display: flex; flex-direction: column;">
          <div class="preset-focus-bar">
            <span style="font-size: 12px; font-weight: 700; color: var(--text-light-secondary); display: flex; align-items: center; margin-right: 4px;">Enfoque rápido:</span>
            <button class="preset-btn active" onclick="setDiagramPreset('dcu-img', 1, 0, 0)">Ver Todo</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 1.8, -10, 20)">Obras (1..4)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.0, -15, -25)">Rondas (13..24)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 2.2, 5, 0)">Entradas (10..12)</button>
            <button class="preset-btn" onclick="setDiagramPreset('dcu-img', 1.9, 25, 20)">Admin (25..43)</button>
          </div>

          <div class="diagram-frame-clean frame-dark-canvas reveal-item revealed" style="flex: 1;">
            <div style="overflow: hidden; height: 420px; display: flex; align-items: center; justify-content: center; position: relative;">
              <img id="dcu-img" src="{b64_dcu}" class="diagram-preview-img" style="max-height: 420px; transition: transform 0.4s ease;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (1..42)')" alt="DCU General">
            </div>
            <div class="diagram-action-bar">
              <span style="font-size: 13px; font-weight: 600; color: #8E9EB5;">Diagrama Completo &bull; Casos de Uso 1 al 42</span>
              <button class="btn-primary" style="min-height: 42px; padding: 0 18px; font-size: 13.5px;" onclick="openZoomModal('b64_dcu', 'Diagrama de Casos de Uso (1..42)')">
                Ampliar diagrama {svg_expand}
              </button>
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px; justify-content: center;">
          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Estructura del Diagrama</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              &bull; <strong>Numeración Continua:</strong> Casos de uso numerados secuencialmente del 1 al 42 sin saltos ni desfasajes.<br>
              &bull; <strong>Límite del Sistema:</strong> Encapsula todas las transacciones soportadas por la solución informática.<br>
              &bull; <strong>Trazabilidad Directa:</strong> Cada caso de uso responde a los requerimientos elicitados en la Sección 2.4.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Foco en Vigilancia (Casos 15 y 16)</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              El Encargado de Vigilancia ejecuta la revisión de la sala (CU-16), la cual se extiende condicionalmente mediante <strong>&laquo;extend&raquo;</strong> hacia 'Registrar incidente' (CU-15) sólo cuando se detecta un siniestro físico.
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
    <div class="slide" id="slide-9" data-topic="09 · Actores y Relaciones">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">09 &bull; Actores y Relaciones de Casos de Uso</div>
          <h1 class="giant-title">Arquitectura de Actores y Dependencias UML</h1>
          <p class="editorial-subtitle">
            Roles del sistema y relaciones de inclusión y extensión (Sección 2.7 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_actor_uml}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">
        <div class="card-dark reveal-item revealed">
          <div style="font-size: 13px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 12px;">Actores Identificados en el Negocio</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>1. Responsable de ingreso</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-1 a CU-4</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>2. Administrador del museo</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-5 a CU-8</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>3. Atención al cliente</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-10 a CU-12</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>4. Administrador web</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-13 a CU-14</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>5. Encargado vigilancia</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-15 a CU-18</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>6. Encargado supervisión</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-19 a CU-24</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>7. Admin de sistema</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-25 a CU-43</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 10px; font-size: 13px;">
              <strong>8. Usuario genérico</strong><br><span style="font-size: 11.5px; color: var(--text-light-secondary);">CU-44 a CU-46</span>
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Relación de Extensión &laquo;extend&raquo;</div>
            <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 6px;">CU-16 Revisar sala &rarr; CU-15 Registrar incidente</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light-secondary);">
              El caso base es la revisión habitual de la sala en la ronda. La extensión hacia el registro del incidente ocurre de manera opcional y condicionada: sólo se ejecuta cuando el guardia constata una anomalía física en alguna de las obras expuestas.
            </div>
          </div>

          <div class="card-dark reveal-item revealed" style="border-left: 4px solid #FFFFFF;">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Relación de Inclusión &laquo;include&raquo;</div>
            <div style="font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 6px;">CU-11 Registrar contratación &rarr; CU-12 Consultar agenda</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light-secondary);">
              Para contratar un servicio de guía para el visitante, el sistema ejecuta de manera mandatoria e incondicional la consulta de la agenda de guías para comprobar la disponibilidad horaria antes de autorizar el cobro adicional.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 10: PLANTILLA CU-15 (THEME: DARK)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 10: PLANTILLA CU-15 -->
    <div class="slide" id="slide-10" data-topic="10 · Plantilla Registrar Incidente">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">10 &bull; Especificación Formal de Caso de Uso</div>
          <h1 class="giant-title">Caso de Uso: Registrar Incidente (CU-15)</h1>
          <p class="editorial-subtitle">
            Plantilla formal de pasos y eliminación de ambigüedad en el Paso 4 (Sección 2.8 del TPI)
          </p>
        </div>
        <div style="opacity: 0.85; padding-top: 10px;">
          {svg_stepper_flow}
        </div>
      </div>

      <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px;">
        <div class="card-dark reveal-item revealed" style="padding: 20px;">
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 12px;">Flujo Principal de Pasos (1 al 14)</div>
          
          <div style="display: flex; flex-direction: column; gap: 8px; max-height: 420px; overflow-y: auto; padding-right: 6px;">
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 1:</strong> El guardia visualiza la sala y solicita registrar nuevo incidente.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 2:</strong> El sistema solicita el ingreso del número de identificación de la obra.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 3:</strong> El guardia ingresa el código de identificación de la obra dañada.
            </div>
            <div style="background: rgba(47,107,255,0.2); border: 1px solid var(--blue-accent); padding: 10px 14px; border-radius: 10px; font-size: 13px; color: #FFF;">
              <strong>Paso 4 (Detallado sin ambigüedad):</strong><br>
              El sistema busca la obra y despliega: <strong>Código de identificación</strong>, <strong>Título de la obra</strong>, <strong>Nombre de la sala actual</strong> y <strong>Ubicación física en muro/vitrina</strong>.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 5:</strong> El guardia constata que la obra mostrada en pantalla coincide con la pieza física.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 6:</strong> El guardia confirma la obra seleccionada.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 7:</strong> El sistema recupera y despliega los tipos de incidentes habilitados.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 8:</strong> El guardia selecciona el tipo de incidente e ingresa observaciones.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 9:</strong> El sistema solicita confirmación del registro del incidente.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 10:</strong> El guardia confirma la registración del siniestro.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 11:</strong> El sistema toma la fecha y hora del servidor y crea la instancia de Incidente.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 12:</strong> El sistema actualiza el estado de la obra a 'Inactivo'.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 13:</strong> El sistema actualiza el estado de la sala a 'Observación pendiente'.
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 8px 12px; border-radius: 8px; font-size: 12.5px;">
              <strong>Paso 14:</strong> El sistema muestra mensaje de confirmación y número de incidente generado.
            </div>
          </div>
        </div>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div class="card-dark reveal-item revealed" style="border-left: 4px solid var(--blue-accent);">
            <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 6px;">Corrección de Ambigüedad</div>
            <div style="font-size: 13.5px; line-height: 1.55; color: var(--text-light);">
              En cumplimiento estricto de las directivas de cátedra, se eliminó la redacción ambigua tipo 'mostrar datos' en el Paso 4, detallando los atributos explícitos que el sistema recupera y presenta en la tablet.
            </div>
          </div>

          <div class="card-dark reveal-item revealed">
            <div style="font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;">Cursos Alternativos</div>
            <div style="font-size: 13px; line-height: 1.55; color: var(--text-light-secondary);">
              &bull; <strong>A1 (Paso 4):</strong> Obra no encontrada en el catálogo. Vuelve al Paso 2.<br>
              &bull; <strong>A2 (Paso 6):</strong> La obra mostrada no coincide físicamente. Cancela y retorna.<br>
              &bull; <strong>A3 (Paso 10):</strong> El guardia desiste de confirmar el incidente. Cancela operación.
            </div>
          </div>
        </div>
      </div>
    </div>
''')

        # ========================================================
        # SLIDE 11: PROTOTIPO DE PANTALLA (THEME: DARK - MATCHED CANVAS)
        # ========================================================
        out.write(f'''
    <!-- SLIDE 11: PROTOTIPO DE PANTALLA -->
    <div class="slide" id="slide-11" data-topic="11 · Prototipo de Pantalla">
      <div class="breadcrumb-tag">11 &bull; Prototipo de Interfaz de Usuario</div>
      <h1 class="giant-title">Prototipo de Pantalla: Registrar Incidente</h1>
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
    <div class="slide" id="slide-12" data-topic="12 · Diagrama de Clases del Dominio">
      <div class="breadcrumb-tag">12 &bull; Vista Interna Orientada a Objetos</div>
      <h1 class="giant-title">Diagrama de Clases del Dominio (DCD General)</h1>
      <p class="editorial-subtitle">
        Modelo de Dominio para el caso de uso Registrar Incidente (Sección 2.9 del TPI)
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
    <div class="slide" id="slide-13" data-topic="13 · Multiplicidades e Integridad">
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <div class="breadcrumb-tag">13 &bull; Multiplicidades y Reglas de Integridad del Dominio</div>
          <h1 class="giant-title">Multiplicidades y Reglas Estructurales del DCD</h1>
          <p class="editorial-subtitle">
            Garantía de consistencia de datos y acoplamiento según directivas de cátedra (Sección 2.9 del TPI)
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
    <!-- SLIDE 14: TRAZABILIDAD & CIERRE -->
    <div class="slide" id="slide-14" data-topic="14 · Trazabilidad y Conclusiones">
      <div class="breadcrumb-tag">14 &bull; Trazabilidad Integral de Requerimientos</div>
      <h1 class="giant-title">Matriz de Trazabilidad Integral y Conclusiones</h1>
      <p class="editorial-subtitle">
        Camino completo del dato: Regla de Negocio &rarr; BPMN &rarr; Requerimiento &rarr; Caso de Uso &rarr; Clases de Dominio
      </p>

      <div class="trace-matrix-console reveal-item revealed" style="margin-bottom: 24px;">
        <div>
          <div style="font-size: 12px; font-weight: 700; color: var(--blue-accent); text-transform: uppercase; margin-bottom: 10px;">Seleccionar Requerimiento:</div>
          <div class="trace-rf-list">
            <div class="trace-rf-item active" onclick="selectTraceItem(this, 'RF-35')">
              <strong>RF-35</strong> &bull; Registrar Incidente
            </div>
            <div class="trace-rf-item" onclick="selectTraceItem(this, 'RF-02')">
              <strong>RF-02</strong> &bull; Registrar Reingreso a Depósito
            </div>
            <div class="trace-rf-item" onclick="selectTraceItem(this, 'RF-31')">
              <strong>RF-31</strong> &bull; Consultar Planificación de Rondas
            </div>
            <div class="trace-rf-item" onclick="selectTraceItem(this, 'RF-10')">
              <strong>RF-10</strong> &bull; Registrar Venta de Entrada
            </div>
          </div>
        </div>

        <div class="trace-impact-dossier" id="trace-dossier-content">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px;">
            <span style="font-size: 15px; font-weight: 800; color: #FFF;" id="trace-rf-title">RF-35: Registrar Incidente en Sala</span>
            <span style="font-size: 11px; font-weight: 700; background: var(--blue-accent); color: #FFF; padding: 3px 8px; border-radius: 4px;">TRAZABILIDAD COMPLETA</span>
          </div>

          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; font-size: 13px;">
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11px;">REGLA DE NEGOCIO</span>
              <span id="trace-rn">Regla de Negocio 2: Inmediatez de registro ante hallazgo en tablet.</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11px;">BPMN NIVEL 2</span>
              <span id="trace-bpmn">Compuerta XOR &rarr; Rama de anomalía y registro de incidente.</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11px;">CASO DE USO</span>
              <span id="trace-cu">CU-15 Registrar incidente (extiende a CU-16 de Revisar sala).</span>
            </div>
            <div style="background: rgba(255,255,255,0.04); padding: 10px; border-radius: 8px;">
              <span style="color: var(--blue-accent); font-weight: 700; display: block; font-size: 11px;">CLASES DEL DCD</span>
              <span id="trace-dcd">Incidente, TipoIncidente, ObjetoAnimado, Estado.</span>
            </div>
          </div>
        </div>
      </div>

      <div class="card-dark reveal-item revealed" style="display: flex; justify-content: space-between; align-items: center;">
        <div>
          <div style="font-size: 16px; font-weight: 700; color: #FFF;">Fin de la Defensa Oral &bull; Grupo 6 &bull; ASI 2K10</div>
          <div style="font-size: 13.5px; color: var(--text-light-secondary); margin-top: 2px;">
            Quedamos a disposición de la mesa evaluadora para las preguntas y devoluciones.
          </div>
        </div>
        <button class="btn-primary" onclick="goToSlide(1)">
          Volver al inicio {svg_arrow_right}
        </button>
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
      "07 · Requerimientos del Sistema",
      "08 · Diagrama de Casos de Uso",
      "09 · Actores y Casos de Uso",
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
    const traceData = {{
      'RF-35': {{
        title: 'RF-35: Registrar Incidente en Sala',
        rn: 'Regla de Negocio 2: Inmediatez de registro ante hallazgo en tablet.',
        bpmn: 'Compuerta XOR &rarr; Rama de anomalía y registro de incidente.',
        cu: 'CU-15 Registrar incidente (extiende a CU-16 de Revisar sala).',
        dcd: 'Incidente, TipoIncidente, ObjetoAnimado, Estado.'
      }},
      'RF-02': {{
        title: 'RF-02: Registrar Reingreso de Obra Restaurada a Depósito',
        rn: 'Regla de Negocio 1: Reingreso obligatorio a depósito antes de nueva disposición.',
        bpmn: 'Subproceso de restauración &rarr; Retorno y peritaje en depósito.',
        cu: 'CU-2 Registrar reingreso de obra.',
        dcd: 'Obra, Deposito, Empleado, EstadoObra.'
      }},
      'RF-31': {{
        title: 'RF-31: Consultar Planificación de Rondas de Vigilancia',
        rn: 'Priorización algorítmica de salas con mayor índice de siniestros.',
        bpmn: 'Evento de inicio de turno &rarr; Consulta de mapa en Módulo Web.',
        cu: 'CU-14 Consultar planificación ronda.',
        dcd: 'PlanificacionRonda, Guardia, Sala, SalaXGuardia.'
      }},
      'RF-10': {{
        title: 'RF-10: Registrar Venta de Entrada y Servicio de Guía',
        rn: 'Cobro de entrada general con arancel adicional por servicio de guía.',
        bpmn: 'Proceso esencial de Exposición &rarr; Caja de ingreso.',
        cu: 'CU-10 Registrar venta de entrada (incluye CU-12 Consultar agenda).',
        dcd: 'Entrada, Tarifa, Guia, AgendaGuia, DetalleVenta.'
      }}
    }};

    function selectTraceItem(el, rfCode) {{
      const items = el.parentElement.querySelectorAll('.trace-rf-item');
      items.forEach(it => it.classList.remove('active'));
      el.classList.add('active');

      const data = traceData[rfCode];
      if (data) {{
        document.getElementById('trace-rf-title').textContent = data.title;
        document.getElementById('trace-rn').textContent = data.rn;
        document.getElementById('trace-bpmn').innerHTML = data.bpmn;
        document.getElementById('trace-cu').textContent = data.cu;
        document.getElementById('trace-dcd').textContent = data.dcd;
      }}
    }}

    // Filter requirements in Slide 7
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
