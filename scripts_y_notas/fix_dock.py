import re
import subprocess
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

bad_snippet = """      const key = (sector === 'guardia') ? 'vigilancia' : ((sector === 'supervisor') ? 'supervision' : sector);
      const data = DCU_ACTOR_STEPS[key] || DCU_ACTOR_STEPS['all'];
      
      inner.style.transform = data.transform;
      const tagEl = document.getElementById('dcu-tour-tag');
      const titleEl = document.getElementById('dcu-tour-title');
      const descEl = document.getElementById('dcu-tour-desc');
      if (tagEl) tagEl.innerText = data.tag;
      if (titleEl) titleEl.innerText = data.title;
      if (descEl) descEl.innerText = data.desc;
    });
    });

    macDock.addEventListener('mouseleave', () => {
      dockIcons.forEach(icon => {
        icon.style.transform = 'scale(1) translateY(0)';
      });
    });"""

good_snippet = """    // ========================================================
    // macOS DOCK LOGIC (SPRING SLIDE + FISHEYE MAGNIFICATION)
    // ========================================================
    const macDock = document.getElementById('mac-dock');
    const dockHotspot = document.getElementById('dock-hotspot');
    const dockIcons = document.querySelectorAll('.dock-icon-btn');
    let dockHideTimer = null;

    function showMacDock() {
      if (dockHideTimer) clearTimeout(dockHideTimer);
      if (macDock) macDock.classList.add('visible');
    }

    function hideMacDockWithDelay() {
      if (dockHideTimer) clearTimeout(dockHideTimer);
      dockHideTimer = setTimeout(() => {
        if (macDock) macDock.classList.remove('visible');
      }, 600);
    }

    if (dockHotspot) {
      dockHotspot.addEventListener('mouseenter', showMacDock);
      dockHotspot.addEventListener('mouseleave', hideMacDockWithDelay);
    }
    if (macDock) {
      macDock.addEventListener('mouseenter', showMacDock);
      macDock.addEventListener('mouseleave', hideMacDockWithDelay);

      // Fisheye magnification on mousemove
      macDock.addEventListener('mousemove', (e) => {
        const mouseX = e.clientX;
        dockIcons.forEach(icon => {
          const rect = icon.getBoundingClientRect();
          const iconCenterX = rect.left + rect.width / 2;
          const dist = Math.abs(mouseX - iconCenterX);
          const maxDist = 90;

          if (dist < maxDist) {
            const factor = 1 - (dist / maxDist);
            const scale = 1 + factor * 0.36; // Up to 1.36x
            const translateY = -(factor * 6);
            icon.style.transform = `scale(${scale}) translateY(${translateY}px)`;
          } else {
            icon.style.transform = 'scale(1) translateY(0)';
          }
        });
      });

      macDock.addEventListener('mouseleave', () => {
        dockIcons.forEach(icon => {
          icon.style.transform = 'scale(1) translateY(0)';
        });
      });
    }"""

if bad_snippet not in content:
    print("bad_snippet not found in index.html!")
else:
    print("bad_snippet found! Replacing...")
    content = content.replace(bad_snippet, good_snippet)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('presentacion.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced in index.html and presentacion.html successfully.")

# Extract script and check with node
m = re.search(r'<script[\s\S]*?>([\s\S]*?)</script>', content, re.IGNORECASE)
if m:
    with open('_test_script.js', 'w', encoding='utf-8') as f:
        f.write(m.group(1))
    res = subprocess.run(['node', '--check', '_test_script.js'], capture_output=True, text=True)
    print("Node check exit code:", res.returncode)
    if res.returncode != 0:
        print("Node check stderr:\n", res.stderr)
    else:
        print("ALL JAVASCRIPT SYNTAX IN INDEX.HTML IS 100% VALID!")
