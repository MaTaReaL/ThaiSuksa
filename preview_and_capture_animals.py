# -*- coding: utf-8 -*-
import subprocess
import os
import re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ARTIFACT_DIR = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

import sys
sys.path.insert(0, HERE)
from generate_thai_suksa_flow import (
    s61_campus_animal_wiki,
    s62_animal_details_and_health,
    s63_contribute_animal_sighting,
    s64_animal_radar_and_welfare
)
from kit import CSS, C

screens = [
    ("S61", "61. สารานุกรมสัตว์และวิกิชุมชนมหาวิทยาลัย", s61_campus_animal_wiki()),
    ("S62", "62. ข้อมูลสัตว์ประจำวิทยาเขตและประวัติสุขภาพ", s62_animal_details_and_health()),
    ("S63", "63. ร่วมแบ่งปันข้อมูลและรายงานพิกัดพบสัตว์", s63_contribute_animal_sighting()),
    ("S64", "64. แผนที่เรดาร์และสวัสดิภาพสัตว์ในวิทยาเขต", s64_animal_radar_and_welfare())
]

screens_html = ""
for idx, (sid, title, content) in enumerate(screens):
    clean_content = re.sub(r'<div\s+class=[\'"]scr[\'"][^>]*>', '<div class="scr" style="position:relative;margin:0;flex-shrink:0;">', content, count=1)
    screens_html += f"""
    <div style="display:flex;flex-direction:column;gap:12px;align-items:center;">
      <div style="background:{C['blue']};color:#fff;padding:6px 14px;border-radius:10px;font-size:13px;font-weight:700;letter-spacing:0.3px;box-shadow:0 4px 12px rgba(36,107,253,0.25);">
        {title}
      </div>
      {clean_content}
    </div>
    """

preview_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{CSS}
body {{
  margin: 0;
  padding: 40px;
  background: #0B1120;
  display: flex;
  gap: 36px;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  justify-content: center;
  align-items: flex-start;
  min-height: 100vh;
}}
</style>
</head>
<body>
{screens_html}
</body>
</html>"""

preview_file = os.path.join(HERE, "animals_preview.html")
preview_url = 'file:///' + preview_file.replace('\\', '/')
with open(preview_file, "w", encoding="utf-8") as f:
    f.write(preview_html)

out_preview_png = os.path.join(ARTIFACT_DIR, "campus_animals_wiki_suite.png")

# 1. Render 4-screen suite
cmd1 = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2000,1100",
    f"--screenshot={out_preview_png}",
    preview_url
]
print("Capturing Campus Animal Wiki screens suite...")
subprocess.run(cmd1, check=True)
print("Saved suite screenshot:", out_preview_png)

# 2. Render Row 15 from complete flow board
board_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
board_url = 'file:///' + board_path.replace('\\', '/')
temp_board_png = os.path.join(HERE, "temp_board_animals.png")
out_wires_png = os.path.join(ARTIFACT_DIR, "row15_animals_prototype_board_wires.png")

cmd2 = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=8200,20500",
    f"--screenshot={temp_board_png}",
    board_url
]
print("Rendering full board for Row 15 animal wiki wires crop...")
subprocess.run(cmd2, check=True)

if os.path.exists(temp_board_png):
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(temp_board_png)
    print("Full board size:", im.size)
    # Row 15 is around y=17350 to 18750, cols 0..3 (x=60 to 2800)
    box = (60, 17350, 2800, 18750)
    cropped = im.crop(box)
    cropped.save(out_wires_png)
    print("Saved Row 15 board wires crop:", out_wires_png)
    try:
        os.remove(temp_board_png)
    except:
        pass

print("Animal Wiki visual verification artifacts complete!")
