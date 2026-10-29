# -*- coding: utf-8 -*-
import subprocess
import os
import re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ARTIFACT_DIR = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

from generate_thai_suksa_flow import (
    s55_emergency_sos_directory,
    s55b_emergency_contacts_and_alerts,
    s56_iphone_home_screen_widget,
    s56b_widget_gallery_and_sizes
)
from kit import CSS, C

screens = [
    ("S55", "55. ศูนย์เบอร์โทรฉุกเฉิน & SOS", s55_emergency_sos_directory()),
    ("S55B", "55B. จัดการผู้ติดต่อฉุกเฉิน & แจ้งเตือนภัย", s55b_emergency_contacts_and_alerts()),
    ("S56", "56. หน้าจอโฮมจำลอง iPhone & วิดเจ็ต", s56_iphone_home_screen_widget()),
    ("S56B", "56B. คลังวิดเจ็ตฉุกเฉินหลากขนาด iOS", s56b_widget_gallery_and_sizes())
]

screens_html = ""
for idx, (sid, title, content) in enumerate(screens):
    # strip existing scr wrapper positioning
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

preview_file = os.path.join(HERE, "emergency_preview.html")
with open(preview_file, "w", encoding="utf-8") as f:
    f.write(preview_html)

out_preview_png = os.path.join(ARTIFACT_DIR, "emergency_calling_and_ios_widgets_suite.png")

# 1. Render 4-screen suite
cmd = [
    CHROME_PATH,
    "--headless",
    "--disable-gpu",
    "--window-size=2100,1100",
    f"--screenshot={out_preview_png}",
    preview_file
]
subprocess.run(cmd, check=True)
print("Saved suite screenshot:", out_preview_png)

# 2. Crop Row 13 with connections from full board
full_board_file = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
temp_full_png = os.path.join(HERE, "temp_board_full.png")

cmd2 = [
    CHROME_PATH,
    "--headless",
    "--disable-gpu",
    "--window-size=4800,3200",
    f"--screenshot={temp_full_png}",
    full_board_file
]
subprocess.run(cmd2, check=True)

if os.path.exists(temp_full_png):
    Image.MAX_IMAGE_PIXELS = None
    im = Image.open(temp_full_png)
    w, h = im.size
    print(f"Full board capture size: {w}x{h}")
    # Row 13 is at the bottom of the board
    crop_box = (0, max(0, h - 1400), min(w, 3600), h)
    cropped = im.crop(crop_box)
    out_wires_png = os.path.join(ARTIFACT_DIR, "row13_emergency_prototype_board_wires.png")
    cropped.save(out_wires_png)
    print("Saved wires crop screenshot:", out_wires_png)
    try:
        os.remove(temp_full_png)
    except:
        pass
