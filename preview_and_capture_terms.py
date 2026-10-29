# -*- coding: utf-8 -*-
import subprocess
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
from generate_thai_suksa_flow import (
    s01_splash, s02_welcome, s02b_terms_and_conditions,
    s05_thaid_registration, s03_select_university, s04b_sso_webview,
    s05b_social_linking, s04_login
)
from kit import CSS, C

screens = [
    ("S01", "01. สแปลชสกรีน", s01_splash()),
    ("S02", "02. ยินดีต้อนรับ", s02_welcome()),
    ("S02B", "02B. ข้อกำหนดและเงื่อนไขการใช้งาน", s02b_terms_and_conditions()),
    ("S05", "05. ยืนยันตัวตน ThaID", s05_thaid_registration()),
    ("S03", "03. เลือกสถาบันการศึกษา", s03_select_university()),
    ("S04B", "04B. เข้าสู่ระบบ SSO สถาบัน", s04b_sso_webview()),
    ("S05B", "05B. เชื่อมต่อบัญชีโซเชียล", s05b_social_linking()),
    ("S04", "04. เข้าสู่ระบบ", s04_login())
]

screens_html = ""
for i, (sid, title, content) in enumerate(screens):
    x = 40 + i * 440
    screens_html += f'''
    <div style="position:absolute;left:{x}px;top:40px;">
      <div style="margin-bottom:8px;font:700 13px 'IBM Plex Sans Thai';color:{C['navy']};display:flex;align-items:center;gap:6px;">
        <span style="background:{C['blue']};color:#fff;padding:2px 8px;border-radius:6px;font-size:11px;">{sid}</span>
        {title}
      </div>
      <div style="position:relative;width:400px;height:844px;box-shadow:0 14px 40px rgba(0,0,0,0.15);border-radius:44px;overflow:hidden;border:4px solid #1E293B;">
        {content}
      </div>
    </div>
    '''

html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
{CSS}
body {{
  background: #0B1120;
  width: 3600px;
  height: 980px;
  margin: 0;
  padding: 0;
  overflow: hidden;
}}
</style>
</head>
<body>
  {screens_html}
</body>
</html>'''

preview_path = os.path.join(HERE, "preview_terms.html")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
preview_url = 'file:///' + preview_path.replace('\\', '/')
artifact_dir = r'C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5'
out_screens = os.path.join(artifact_dir, 'row1_terms_and_onboarding_suite.png')

# 1. Capture preview screens
cmd1 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=3580,980',
    f'--screenshot={out_screens}',
    preview_url
]
print("Capturing Row 1 with Terms & Conditions preview...")
subprocess.run(cmd1, check=True)
print("Saved Row 1 Terms preview:", out_screens)

# 2. Capture full board crop for Row 1 wires
board_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
board_url = 'file:///' + board_path.replace('\\', '/')
temp_board = os.path.join(HERE, "temp_board_terms.png")
out_crop = os.path.join(artifact_dir, 'row1_terms_prototype_board_wires.png')

cmd2 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=5600,15400',
    f'--screenshot={temp_board}',
    board_url
]
print("Rendering full board for Row 1 wires crop...")
subprocess.run(cmd2, check=True)

im = Image.open(temp_board)
# Crop around row 1: y = 80 to 1350, x = 60 to 5400
box = (60, 80, 5400, 1350)
cropped = im.crop(box)
cropped.save(out_crop)
print("Saved Row 1 board wires crop:", out_crop)

# Clean up
if os.path.exists(temp_board):
    os.remove(temp_board)
if os.path.exists(preview_path):
    os.remove(preview_path)

print("Row 1 Terms & Conditions visual verification complete!")
