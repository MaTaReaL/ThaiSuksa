# -*- coding: utf-8 -*-
import subprocess
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ARTIFACT_DIR = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

board_file = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
with open(board_file, "r", encoding="utf-8") as f:
    board_html = f.read()

# We want to capture around y=17400 to 18600.
# We shift the #board element up by 17300px using CSS transform
offset_html = board_html.replace(
    '<div id="board" style="',
    '<div id="board" style="transform: translateY(-17300px); transform-origin: top left; '
)

wrapper_file = os.path.join(HERE, "temp_row15_offset.html")
with open(wrapper_file, "w", encoding="utf-8") as f:
    f.write(offset_html)

wrapper_url = 'file:///' + wrapper_file.replace('\\', '/')
out_wires_png = os.path.join(ARTIFACT_DIR, "row15_animals_prototype_board_wires.png")

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2700,1250",
    f"--screenshot={out_wires_png}",
    wrapper_url
]
print("Capturing Row 15 board wires with offset...")
subprocess.run(cmd, check=True)
print("Saved Row 15 board wires screenshot:", out_wires_png)

if os.path.exists(wrapper_file):
    os.remove(wrapper_file)
