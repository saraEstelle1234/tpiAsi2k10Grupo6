import re
import subprocess

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix setBpmnTour extra brace
    bpmn_broken = """        function setBpmnTour(stepIdx, btn) {
      document.querySelectorAll('#bpmn-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('bpmn-img');
      const data = BPMN_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('bpmn-tour-tag');
        const titleEl = document.getElementById('bpmn-tour-title');
        const descEl = document.getElementById('bpmn-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }
    }"""
    
    bpmn_fixed = """    function setBpmnTour(stepIdx, btn) {
      document.querySelectorAll('#bpmn-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('bpmn-img');
      const data = BPMN_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('bpmn-tour-tag');
        const titleEl = document.getElementById('bpmn-tour-title');
        const descEl = document.getElementById('bpmn-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }"""

    if bpmn_broken in content:
        content = content.replace(bpmn_broken, bpmn_fixed)
        print(f"[{filepath}] Fixed bpmn extra brace")
    else:
        print(f"[{filepath}] bpmn_broken not matched directly, checking regex...")
        # fallback regex for setBpmnTour with double closing braces
        content = re.sub(
            r'(function setBpmnTour\([\s\S]*?if \(tagEl\)[\s\S]*?if \(descEl\)[\s\S]*?\}\s*\})\s*\}',
            r'\1',
            content
        )

    # 2. Fix setDcdTour extra brace
    dcd_broken = """        function setDcdTour(stepIdx, btn) {
      document.querySelectorAll('#dcd-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('dcd-img');
      const data = DCD_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('dcd-tour-tag');
        const titleEl = document.getElementById('dcd-tour-title');
        const descEl = document.getElementById('dcd-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }
    }"""

    dcd_fixed = """    function setDcdTour(stepIdx, btn) {
      document.querySelectorAll('#dcd-tour-bar .tour-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const img = document.getElementById('dcd-img');
      const data = DCD_TOUR_STEPS[stepIdx];
      if (img && data) {
        img.style.transform = data.transform;
        const tagEl = document.getElementById('dcd-tour-tag');
        const titleEl = document.getElementById('dcd-tour-title');
        const descEl = document.getElementById('dcd-tour-desc');
        if (tagEl) tagEl.innerText = data.tag;
        if (titleEl) titleEl.innerText = data.title;
        if (descEl) descEl.innerText = data.desc;
      }
    }"""

    if dcd_broken in content:
        content = content.replace(dcd_broken, dcd_fixed)
        print(f"[{filepath}] Fixed dcd extra brace")
    else:
        print(f"[{filepath}] dcd_broken not matched directly, checking regex...")
        content = re.sub(
            r'(function setDcdTour\([\s\S]*?if \(tagEl\)[\s\S]*?if \(descEl\)[\s\S]*?\}\s*\})\s*\}',
            r'\1',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate JavaScript
    m = re.search(r'<script[\s\S]*?>([\s\S]*?)</script>', content, re.IGNORECASE)
    if m:
        js_code = m.group(1)
        with open('_temp_val.js', 'w', encoding='utf-8') as f_js:
            f_js.write(js_code)
        res = subprocess.run(['node', '--check', '_temp_val.js'], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[{filepath}] JS SYNTAX VALIDATION: PASSED PERFECTLY!")
        else:
            print(f"[{filepath}] JS SYNTAX ERROR:\n{res.stderr}")
    else:
        print(f"[{filepath}] Warning: No script tag found")

fix_file('index.html')
fix_file('presentacion.html')
