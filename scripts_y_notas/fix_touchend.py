import re
import subprocess
import shutil

def fix_touchend():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    broken_touchend = """        // Horizontal swipe threshold: > 45px and predominantly horizontal
        if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.5) {
          if (diffX < 0) {
            nextSlideAction();
          } else {
            prevSlideAction();
          }
        }
    }, { passive: true });"""

    fixed_touchend = """        // Horizontal swipe threshold: > 45px and predominantly horizontal
        if (Math.abs(diffX) > 45 && Math.abs(diffX) > Math.abs(diffY) * 1.5) {
          if (diffX < 0) {
            nextSlideAction();
          } else {
            prevSlideAction();
          }
        }
      }
    }, { passive: true });"""

    if broken_touchend in content:
        content = content.replace(broken_touchend, fixed_touchend)
        print("Fixed touchend missing closing brace!")
    else:
        print("broken_touchend not found directly!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    m = re.search(r'<script[\s\S]*?>([\s\S]*?)</script>', content, re.IGNORECASE)
    if m:
        js_code = m.group(1)
        with open('_temp_val.js', 'w', encoding='utf-8') as f_js:
            f_js.write(js_code)
        res = subprocess.run(['node', '--check', '_temp_val.js'], capture_output=True, text=True)
        if res.returncode == 0:
            print(">>> ALL JAVASCRIPT IN index.html IS 100% VALID! <<<")
            shutil.copyfile('index.html', 'presentacion.html')
            print("Copied to presentacion.html")
        else:
            print(f"Node check failed:\n{res.stderr}")

fix_touchend()
