# -*- coding: utf-8 -*-
import subprocess
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
from generate_thai_suksa_flow import (
    s07_home, s08_hamburger_drawer, s08b_credits_attribution,
    s09_notifications, s10_profile, s10b_account_privacy_settings, s11_digital_id
)
from kit import CSS, C

screens = [
    ("S07", "07. หน้าหลัก", s07_home()),
    ("S08", "08. เมนูหลัก", s08_hamburger_drawer()),
    ("S08B", "08B. เครดิตผู้จัดทำและผู้สนับสนุน", s08b_credits_attribution()),
    ("S09", "09. การแจ้งเตือน", s09_notifications()),
    ("S10", "10. โปรไฟล์นักศึกษา", s10_profile()),
    ("S10B", "10B. การตั้งค่าบัญชี & ความเป็นส่วนตัว", s10b_account_privacy_settings()),
    ("S11", "11. บัตรนักศึกษาดิจิทัล", s11_digital_id())
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
  width: 3160px;
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

preview_path = os.path.join(HERE, "preview_credits.html")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
preview_url = 'file:///' + preview_path.replace('\\', '/')
artifact_dir = r'C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5'
out_screens = os.path.join(artifact_dir, 'row3_with_credits_suite.png')

# 1. Capture preview screens
cmd1 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=3140,980',
    f'--screenshot={out_screens}',
    preview_url
]
print("Capturing Row 3 with Credits preview...")
subprocess.run(cmd1, check=True)
print("Saved Row 3 with Credits preview:", out_screens)

# 2. Capture full board crop for Row 3 wires
board_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
board_url = 'file:///' + board_path.replace('\\', '/')
temp_board = os.path.join(HERE, "temp_board_credits.png")
out_crop = os.path.join(artifact_dir, 'row3_credits_prototype_board_wires.png')

cmd2 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=3800,15400',
    f'--screenshot={temp_board}',
    board_url
]
print("Rendering full board for Row 3 wires crop...")
subprocess.run(cmd2, check=True)

im = Image.open(temp_board)
# Crop around row 3: y = 2550 to 3850, x = 60 to 3700
box = (60, 2550, 3700, 3850)
cropped = im.crop(box)
cropped.save(out_crop)
print("Saved Row 3 board wires crop:", out_crop)

# Clean up
if os.path.exists(temp_board):
    os.remove(temp_board)
if os.path.exists(preview_path):
    os.remove(preview_path)

print("Row 3 Credits visual verification complete!")
