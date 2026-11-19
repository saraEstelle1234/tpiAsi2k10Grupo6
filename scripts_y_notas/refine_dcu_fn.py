import re
import subprocess
import shutil

def refine_set_dcu_sector(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_fn = """        function setDcuSector(sector, btn) {
      const img = document.getElementById('dcu-img');
      if (!img) return;
      if (btn) {
        const btns = btn.parentElement.querySelectorAll('.tour-btn, .preset-btn');
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      }
      
      const key = (sector === 'guardia') ? 'vigilancia' : ((sector === 'supervisor') ? 'supervision' : sector);
      const data = DCU_ACTOR_STEPS[key] || DCU_ACTOR_STEPS['all'];
      
      img.style.transform = data.transform;
      const tagEl = document.getElementById('dcu-tour-tag');
      const titleEl = document.getElementById('dcu-tour-title');
      const descEl = document.getElementById('dcu-tour-desc');
      if (tagEl) tagEl.innerText = data.tag;
      if (titleEl) titleEl.innerText = data.title;
      if (descEl) descEl.innerText = data.desc;
    }"""

    new_fn = """    function setDcuSector(sector, btn) {
      const img = document.getElementById('dcu-img');
      if (!img) return;
      
      const key = (sector === 'guardia') ? 'vigilancia' : ((sector === 'supervisor') ? 'supervision' : sector);
      
      const tourBar = document.getElementById('dcu-tour-bar');
      if (tourBar) {
        const btns = tourBar.querySelectorAll('.tour-btn');
        btns.forEach(b => b.classList.remove('active'));
        if (btn) {
          btn.classList.add('active');
        } else {
          btns.forEach(b => {
            const attr = b.getAttribute('onclick') || '';
            if (attr.includes("'" + key + "'") || attr.includes('"' + key + '"')) {
              b.classList.add('active');
            }
          });
        }
      }
      
      const data = DCU_ACTOR_STEPS[key] || DCU_ACTOR_STEPS['all'];
      
      img.style.transform = data.transform;
      const tagEl = document.getElementById('dcu-tour-tag');
      const titleEl = document.getElementById('dcu-tour-title');
      const descEl = document.getElementById('dcu-tour-desc');
      if (tagEl) tagEl.innerText = data.tag;
      if (titleEl) titleEl.innerText = data.title;
      if (descEl) descEl.innerText = data.desc;
    }"""

    if old_fn in content:
        content = content.replace(old_fn, new_fn)
        print(f"[{filepath}] Updated setDcuSector function!")
    else:
        print(f"[{filepath}] Regex replacing setDcuSector...")
        content = re.sub(
            r'function setDcuSector\([\s\S]*?if \(descEl\) descEl\.innerText = data\.desc;\s*\}',
            new_fn.strip(),
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

refine_set_dcu_sector('index.html')
refine_set_dcu_sector('presentacion.html')

res = subprocess.run(['node', 'scripts_y_notas/test_dom_run.js'], capture_output=True, text=True)
print("DOM test output:", res.stdout, res.stderr)
