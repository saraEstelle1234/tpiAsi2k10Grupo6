# Let's see if pytesseract or easyocr or windows ocr can read text, or let's use powershell windows OCR script win_ocr.ps1
import subprocess

result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts_y_notas/win_ocr.ps1", "media_presentacion/page_7_img_0_26.png"], capture_output=True, text=True)
print("=== BPMN DESC OCR ===")
print(result.stdout[:1500])

result2 = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "scripts_y_notas/win_ocr.ps1", "media_presentacion/page_8_img_0_29.png"], capture_output=True, text=True)
print("=== BPMN OPER OCR ===")
print(result2.stdout[:1500])
