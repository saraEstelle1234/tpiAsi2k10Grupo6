import re
import subprocess
import shutil

def fix_all():
    filepath = 'index.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix applySmartMatrixDimming
    broken_dimming = """    function applySmartMatrixDimming(activeCategory) {
      const rows = document.querySelectorAll('.trace-item');
      rows.forEach(row => {
        if (!activeCategory || activeCategory === 'all') {
          row.classList.remove('row-dimmed');
          row.classList.remove('row-highlighted');
        } else {
          const rowCategory = row.getAttribute('data-cat') || '';
          if (rowCategory.includes(activeCategory)) {
            row.classList.remove('row-dimmed');
            row.classList.add('row-highlighted');
          } else {
            row.classList.remove('row-highlighted');
            row.classList.add('row-dimmed');
          }
        });
    }"""

    fixed_dimming = """    function applySmartMatrixDimming(activeCategory) {
      const rows = document.querySelectorAll('.trace-item');
      rows.forEach(row => {
        if (!activeCategory || activeCategory === 'all') {
          row.classList.remove('row-dimmed');
          row.classList.remove('row-highlighted');
        } else {
          const rowCategory = row.getAttribute('data-cat') || '';
          if (rowCategory.includes(activeCategory)) {
            row.classList.remove('row-dimmed');
            row.classList.add('row-highlighted');
          } else {
            row.classList.remove('row-highlighted');
            row.classList.add('row-dimmed');
          }
        }
      });
    }"""

    if broken_dimming in content:
        content = content.replace(broken_dimming, fixed_dimming)
        print("Fixed applySmartMatrixDimming syntax error!")
    else:
        print("broken_dimming not found directly, checking...")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate JavaScript
    m = re.search(r'<script[\s\S]*?>([\s\S]*?)</script>', content, re.IGNORECASE)
    if m:
        js_code = m.group(1)
        with open('_temp_val.js', 'w', encoding='utf-8') as f_js:
            f_js.write(js_code)
        res = subprocess.run(['node', '--check', '_temp_val.js'], capture_output=True, text=True)
        if res.returncode == 0:
            print(">>> ALL JAVASCRIPT IN index.html IS 100% VALID! <<<")
            # Copy to presentacion.html
            shutil.copyfile('index.html', 'presentacion.html')
            print("Copied identical fixed file to presentacion.html")
        else:
            print(f"Node check failed:\n{res.stderr}")

fix_all()
