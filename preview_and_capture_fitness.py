# -*- coding: utf-8 -*-
import subprocess
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARTIFACT_DIR = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Import screens
sys.path.insert(0, HERE)
from generate_thai_suksa_flow import (
    s59b_fitness_membership_pass,
    s59c_fitness_subscription_wallet,
    s59d_fitness_news_and_classes,
    s59e_fitness_holiday_calendar,
    CSS
)

# 1. Build 4-screen side-by-side preview HTML
preview_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>University Fitness Center Suite (S59B - S59E)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {CSS}
    body {{
      background: #0B1120;
      padding: 40px;
      display: flex;
      flex-direction: row;
      gap: 30px;
      justify-content: center;
      align-items: flex-start;
      min-width: 1900px;
    }}
    .preview-col {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }}
    .col-title {{
      color: #38BDF8;
      font: 700 14px 'IBM Plex Sans Thai', sans-serif;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 6px 16px;
      border-radius: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
  </style>
</head>
<body>
  <div class="preview-col">
    <div class="col-title">59B. บัตรสมาชิกฟิตเนส & สแกนเข้าใช้บริการ</div>
    {s59b_fitness_membership_pass()}
  </div>
  <div class="preview-col">
    <div class="col-title">59C. สมัครและชำระค่าสมาชิกรายเดือนผ่านกระเป๋าเงิน</div>
    {s59c_fitness_subscription_wallet()}
  </div>
  <div class="preview-col">
    <div class="col-title">59D. ศูนย์ข่าวสารและประกาศฟิตเนสมหาวิทยาลัย</div>
    {s59d_fitness_news_and_classes()}
  </div>
  <div class="preview-col">
    <div class="col-title">59E. ปฏิทินวันทำการและตารางวันหยุดฟิตเนส</div>
    {s59e_fitness_holiday_calendar()}
  </div>
</body>
</html>
'''

preview_file = os.path.join(HERE, "fitness_preview.html")
with open(preview_file, "w", encoding="utf-8") as f:
    f.write(preview_html)

out_suite_png = os.path.join(ARTIFACT_DIR, "fitness_and_membership_suite.png")

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2050,1150",
    f"--screenshot={out_suite_png}",
    'file:///' + preview_file.replace('\\', '/')
]
print("Capturing Fitness Suite screens...")
subprocess.run(cmd, check=True)
print("Saved suite screenshot:", out_suite_png)

# 2. Render Row 14 prototype board wires crop
# In the prototype board:
# r = 13 (Row 14). y = 220 + 13 * (956 + 280) = 220 + 13 * 1236 = 220 + 16068 = 16288px!
# We can shift #board up by 16000px and capture cols 2..7!
board_file = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
with open(board_file, "r", encoding="utf-8") as f:
    board_html = f.read()

shifted_html = board_html.replace(
    '<div id="board" style="',
    '<div id="board" style="transform: translate(-1200px, -16050px); transform-origin: top left; '
)

offset_board_file = os.path.join(HERE, "temp_row14_fitness_offset.html")
with open(offset_board_file, "w", encoding="utf-8") as f:
    f.write(shifted_html)

out_wires_png = os.path.join(ARTIFACT_DIR, "row14_fitness_prototype_board_wires.png")
cmd2 = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=3000,1250",
    f"--screenshot={out_wires_png}",
    'file:///' + offset_board_file.replace('\\', '/')
]
print("Capturing Row 14 Fitness board wires with offset...")
subprocess.run(cmd2, check=True)
print("Saved Row 14 board wires screenshot:", out_wires_png)

# Cleanup temp offset file
if os.path.exists(offset_board_file):
    os.remove(offset_board_file)

print("Fitness visual verification artifacts complete!")
