import re

def enhance_dock(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target = """    if (dockHotspot) {
      dockHotspot.addEventListener('mouseenter', showMacDock);
      dockHotspot.addEventListener('mouseleave', hideMacDockWithDelay);
    }
    if (macDock) {
      macDock.addEventListener('mouseenter', showMacDock);
      macDock.addEventListener('mouseleave', hideMacDockWithDelay);"""

    replacement = """    if (dockHotspot) {
      dockHotspot.addEventListener('mouseenter', showMacDock);
      dockHotspot.addEventListener('mouseleave', hideMacDockWithDelay);
    }
    if (macDock) {
      macDock.addEventListener('mouseenter', showMacDock);
      macDock.addEventListener('mouseleave', hideMacDockWithDelay);
    }

    // Direct cursor tracking: trigger dock when pointer is within 60px of screen bottom
    document.addEventListener('mousemove', (e) => {
      if (e.clientY >= window.innerHeight - 60) {
        showMacDock();
      }
    });

    if (macDock) {"""

    if target in content and "document.addEventListener('mousemove', (e) => {\n      if (e.clientY >= window.innerHeight - 60)" not in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[{filepath}] Enhanced dock with mousemove bottom tracking!")
    else:
        print(f"[{filepath}] Already enhanced or target not found.")

enhance_dock('index.html')
enhance_dock('presentacion.html')
