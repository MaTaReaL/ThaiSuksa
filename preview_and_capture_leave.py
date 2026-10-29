# -*- coding: utf-8 -*-
import subprocess
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
from generate_thai_suksa_flow import (
    s12_schedule, s13_class_details, s13b_leave_request,
    s13c_leave_status, s14_exam_schedule, s15_calendar
)
from kit import CSS, C

screens = [
    ("S12", "12. ตารางเรียน", s12_schedule()),
    ("S13", "13. รายละเอียดวิชา", s13_class_details()),
    ("S13B", "13B. ยื่นลาเรียนออนไลน์", s13b_leave_request()),
    ("S13C", "13C. สถานะคำร้องขอลาเรียน", s13c_leave_status()),
    ("S14", "14. ตารางสอบ", s14_exam_schedule()),
    ("S15", "15. ปฏิทินการศึกษา", s15_calendar())
]

screens_html = ""
for i, (sid, title, content) in enumerate(screens):
    x = 40 + i * 460
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
  width: 2850px;
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

preview_path = os.path.join(HERE, "preview_leave.html")
with open(preview_path, "w", encoding="utf-8") as f:
    f.write(html)

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
preview_url = 'file:///' + preview_path.replace('\\', '/')
artifact_dir = r'C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5'
out_screens = os.path.join(artifact_dir, 'row4_schedule_and_online_leave_suite.png')

# 1. Capture preview screens
cmd1 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=2820,980',
    f'--screenshot={out_screens}',
    preview_url
]
print("Capturing Row 4 Schedule & Leave preview...")
subprocess.run(cmd1, check=True)
print("Saved Row 4 Leave preview:", out_screens)

# 2. Capture full board crop for Row 4
board_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
board_url = 'file:///' + board_path.replace('\\', '/')
temp_board = os.path.join(HERE, "temp_board_leave.png")
out_crop = os.path.join(artifact_dir, 'row4_schedule_and_leave_prototype_board_wires.png')

# Row 4 is at y = 220 + 3 * (956 + 280) = 220 + 3708 = 3928
cmd2 = [
    chrome,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=3800,15400',
    f'--screenshot={temp_board}',
    board_url
]
print("Rendering full board for Row 4 wires crop...")
subprocess.run(cmd2, check=True)

im = Image.open(temp_board)
# Crop around row 4: y = 3800 to 5100, x = 80 to 3650
box = (80, 3800, 3650, 5100)
cropped = im.crop(box)
cropped.save(out_crop)
print("Saved Row 4 board wires crop:", out_crop)

# Clean up
if os.path.exists(temp_board):
    os.remove(temp_board)
if os.path.exists(preview_path):
    os.remove(preview_path)

print("Row 4 Leave visual verification complete!")
