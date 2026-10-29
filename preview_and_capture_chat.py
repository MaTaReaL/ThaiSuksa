# -*- coding: utf-8 -*-
import subprocess
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
from generate_thai_suksa_flow import (
    s36_community, s36b_campus_messenger, s36c_chat_room_and_customizer, s36d_voip_group_calling
)
from kit import CSS, C

screens = [
    ("S36", "36. กระดานชุมชน", s36_community()),
    ("S36B", "36B. ศูนย์ข้อความและแชทนักศึกษา", s36b_campus_messenger()),
    ("S36C", "36C. ห้องแชทและการปรับแต่งธีม", s36c_chat_room_and_customizer()),
    ("S36D", "36D. ระบบโทรเสียงและวิดีโอกลุ่ม", s36d_voip_group_calling())
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
  width: 1840px;
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

preview_path = os.path.join(HERE, "preview_chat.html")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
preview_url = 'file:///' + preview_path.replace('\\', '/')
artifact_dir = r'C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5'
out_screens = os.path.join(artifact_dir, 'chat_and_voip_suite.png')

# 1. Capture preview screens
cmd1 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=1820,980',
    f'--screenshot={out_screens}',
    preview_url
]
print("Capturing Chat & VoIP Calling preview...")
subprocess.run(cmd1, check=True)
print("Saved Chat preview:", out_screens)

# 2. Capture full board crop for Row 9 wires
board_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
board_url = 'file:///' + board_path.replace('\\', '/')
temp_board = os.path.join(HERE, "temp_board_chat.png")
out_crop = os.path.join(artifact_dir, 'row9_chat_prototype_board_wires.png')

cmd2 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=8200,16500',
    f'--screenshot={temp_board}',
    board_url
]
print("Rendering full board for Row 9 chat wires crop...")
subprocess.run(cmd2, check=True)

im = Image.open(temp_board)
# Crop around row 9: y = 9950 to 11350, x = 60 to 2800
box = (60, 9950, 2800, 11350)
cropped = im.crop(box)
cropped.save(out_crop)
print("Saved Row 9 board wires crop:", out_crop)

# Clean up
if os.path.exists(temp_board):
    os.remove(temp_board)
if os.path.exists(preview_path):
    os.remove(preview_path)

print("Chat & VoIP Calling visual verification complete!")
