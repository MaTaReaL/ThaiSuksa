# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_DIR = r"c:\งานมหาลัย\งานFigma\ไทยศึกษา\assets"
base_phone_path = os.path.join(ASSETS_DIR, "iphone_user_reference_phone.png")
# Always reload fresh from user upload to be 100% clean
orig_upload = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5\.user_uploaded\media_1792015951451_0a1fd8c3.jpg"
im_full = Image.open(orig_upload).convert("RGBA")
# Crop phone: left 126, top 77, right 549, bottom 1023
im = im_full.crop((126, 77, 549, 1023))
w, h = im.size

# Fonts
font_bold_10 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 10)
font_bold_11 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 11)
font_title_9 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 9)
font_large_sos = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
font_thai_9 = ImageFont.truetype("C:/Windows/Fonts/leelawad.ttf", 9)
font_thai_b9 = ImageFont.truetype("C:/Windows/Fonts/leelawdb.ttf", 9)
font_thai_10 = ImageFont.truetype("C:/Windows/Fonts/leelawad.ttf", 10)
font_thai_b10 = ImageFont.truetype("C:/Windows/Fonts/leelawdb.ttf", 10)

# ===========================================================================
# 1. Clean Left 2x2 Widget (Campus Emergency & SOS)
# ===========================================================================
widget_w, widget_h = 160, 160
r = 28

# First, paint a completely opaque rounded rectangle directly on `im` to wipe out the weather widget!
draw_im = ImageDraw.Draw(im)
draw_im.rounded_rectangle([34, 86, 34 + widget_w, 86 + widget_h], radius=r, fill=(24, 36, 48, 255))

# Create RGB widget (no alpha transparency issues!)
lw = Image.new("RGB", (widget_w, widget_h), (24, 36, 48))
lw_draw = ImageDraw.Draw(lw)

# Opaque vertical gradient
for y in range(widget_h):
    ratio = y / widget_h
    r_col = int(34 - 14 * ratio)
    g_col = int(48 - 18 * ratio)
    b_col = int(62 - 20 * ratio)
    lw_draw.line([(0, y), (widget_w, y)], fill=(r_col, g_col, b_col))

# Left Column (width 42px) with lighter slate tint
left_col_w = 42
for y in range(widget_h):
    ratio = y / widget_h
    r_col = int(48 - 12 * ratio)
    g_col = int(66 - 18 * ratio)
    b_col = int(82 - 20 * ratio)
    lw_draw.line([(0, y), (left_col_w, y)], fill=(r_col, g_col, b_col))

# Divider line
lw_draw.line([(left_col_w, 2), (left_col_w, widget_h - 2)], fill=(75, 95, 115), width=1)

# Left Column Content:
# 1. Red SOS Pill
sos_badge_y = 18
lw_draw.rounded_rectangle([5, sos_badge_y, left_col_w - 5, sos_badge_y + 19], radius=6, fill=(225, 29, 72))
lw_draw.text((11, sos_badge_y + 3), "SOS", font=font_bold_10, fill=(255, 255, 255))

# Divider
lw_draw.line([(8, 54), (left_col_w - 8, 54)], fill=(60, 80, 100), width=1)

# 2. GPS Live Dot & Text
gps_y = 68
lw_draw.ellipse([8, gps_y + 3, 14, gps_y + 9], fill=(16, 185, 129))
lw_draw.text((18, gps_y), "GPS", font=font_bold_10, fill=(203, 213, 225))

# Divider
lw_draw.line([(8, 102), (left_col_w - 8, 102)], fill=(60, 80, 100), width=1)

# 3. 24H active text
h24_y = 116
lw_draw.text((11, h24_y), "24H", font=font_bold_10, fill=(148, 163, 184))

# Right Column Content:
# Title
lw_draw.text((50, 14), "SILPAKORN SAFETY", font=font_title_9, fill=(148, 163, 184))

# Glowing Red Circular SOS Button (Centered in right col)
center_x = left_col_w + (widget_w - left_col_w) // 2
center_y = 64
sos_radius = 26

# Subtle ambient red ring
lw_draw.ellipse([center_x - sos_radius - 4, center_y - sos_radius - 4, center_x + sos_radius + 4, center_y + sos_radius + 4], fill=(85, 30, 40))
# Solid red button
lw_draw.ellipse([center_x - sos_radius, center_y - sos_radius, center_x + sos_radius, center_y + sos_radius], fill=(225, 29, 72), outline=(254, 202, 202), width=2)
lw_draw.text((center_x - 20, center_y - 16), "SOS", font=font_large_sos, fill=(255, 255, 255))

# Security Guard Phone & Status
lw_draw.text((50, 101), "รปภ. 081-999-9999", font=font_thai_b10, fill=(254, 226, 226))

# Status with green dot
lw_draw.ellipse([50, 122, 56, 128], fill=(16, 185, 129))
lw_draw.text((60, 118), "สถานะ: ปลอดภัย", font=font_thai_10, fill=(167, 243, 208))

# Location
lw_draw.text((50, 134), "อาคาร 3 ชั้น 4 (พิกัดสด)", font=font_thai_9, fill=(148, 163, 184))

# Outline highlight
lw_draw.rounded_rectangle([0, 0, widget_w - 1, widget_h - 1], radius=r, outline=(70, 95, 120), width=1)

# Mask and paste onto im
lw_rgba = lw.convert("RGBA")
mask = Image.new("L", (widget_w, widget_h), 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, widget_w, widget_h], radius=r, fill=255)
im.paste(lw_rgba, (34, 86), mask)
print("Pasted 100% clean Left Widget (no bleed)!")

# ===========================================================================
# 2. Clean Right 2x2 Widget (October 2026 Academic Calendar)
# ===========================================================================
rw = Image.new("RGB", (widget_w, widget_h), (24, 36, 48))
rw_draw = ImageDraw.Draw(rw)

# Opaque vertical gradient
for y in range(widget_h):
    ratio = y / widget_h
    r_col = int(30 - 12 * ratio)
    g_col = int(44 - 16 * ratio)
    b_col = int(58 - 18 * ratio)
    rw_draw.line([(0, y), (widget_w, y)], fill=(r_col, g_col, b_col))

# Month & Year
rw_draw.text((16, 14), "OCTOBER", font=font_bold_10, fill=(241, 245, 249))
rw_draw.text((118, 14), "2026", font=font_bold_10, fill=(148, 163, 184))

# Days row
days = ["S", "M", "T", "W", "T", "F", "S"]
col_spacing = 19
start_x = 18
start_y = 34
for i, d in enumerate(days):
    rw_draw.text((start_x + i * col_spacing, start_y), d, font=font_title_9, fill=(148, 163, 184))

# Dates grid
cal_matrix = [
    ["", "", "", "", "1", "2", "3"],
    ["4", "5", "6", "7", "8", "9", "10"],
    ["11", "12", "13", "14", "15", "16", "17"],
    ["18", "19", "20", "21", "22", "23", "24"],
    ["25", "26", "27", "28", "29", "30", "31"]
]

y_step = 19
for row_idx, row in enumerate(cal_matrix):
    curr_y = start_y + 18 + row_idx * y_step
    for col_idx, date_str in enumerate(row):
        if not date_str:
            continue
        cx = start_x + col_idx * col_spacing
        if date_str == "15": # Today in red rounded rect
            rw_draw.rounded_rectangle([cx - 4, curr_y - 2, cx + 16, curr_y + 15], radius=4, fill=(225, 29, 72))
            rw_draw.text((cx, curr_y), date_str, font=font_title_9, fill=(255, 255, 255))
        elif date_str in ["23", "30"]:
            rw_draw.text((cx, curr_y), date_str, font=font_title_9, fill=(56, 189, 248))
        else:
            rw_draw.text((cx, curr_y), date_str, font=font_title_9, fill=(226, 232, 240))

rw_draw.rounded_rectangle([0, 0, widget_w - 1, widget_h - 1], radius=r, outline=(70, 95, 120), width=1)

rw_rgba = rw.convert("RGBA")
im.paste(rw_rgba, (229, 86), mask)
print("Pasted 100% clean Right Widget (no bleed)!")

# ===========================================================================
# 3. Clean University App Icon covering Find My (x=315, y=276, 68x68)
# ===========================================================================
icon_w = 68
ai_icon = Image.new("RGB", (icon_w, icon_w), (16, 28, 54))
ai_draw = ImageDraw.Draw(ai_icon)

# Base dark squircle
ai_draw.rounded_rectangle([0, 0, icon_w - 1, icon_w - 1], radius=16, fill=(16, 28, 54), outline=(70, 90, 120), width=1)
# University emblem
ai_draw.text((14, 14), "🎓", font=ImageFont.truetype("C:/Windows/Fonts/seguiemj.ttf", 28), fill=(255, 255, 255))
ai_draw.text((15, 47), "SU APP", font=font_bold_10, fill=(251, 191, 36))

# Red notification badge 1
bx = icon_w - 11
by = 11
ai_draw.ellipse([bx - 9, by - 9, bx + 9, by + 9], fill=(239, 68, 68), outline=(255, 255, 255), width=2)
ai_draw.text((bx - 3, by - 6), "1", font=font_bold_10, fill=(255, 255, 255))

icon_rgba = ai_icon.convert("RGBA")
icon_mask = Image.new("L", (icon_w, icon_w), 0)
ImageDraw.Draw(icon_mask).rounded_rectangle([0, 0, icon_w, icon_w], radius=16, fill=255)

# First erase background under Find My with matching dark slate
draw_im = ImageDraw.Draw(im)
draw_im.rounded_rectangle([314, 276, 314 + icon_w, 276 + icon_w], radius=16, fill=(24, 38, 50, 255))
im.paste(icon_rgba, (314, 276), icon_mask)
print("Pasted 100% clean Thai Suksa App Icon!")

# Save to assets & brain
out_2x2 = os.path.join(ASSETS_DIR, "iphone_home_screen_2x2.png")
im.save(out_2x2)

brain_dir = r"C:\Users\Thanapol Kitbumrung\.gemini\antigravity\brain\9b343bfc-8fa8-4784-a37c-4b1a71c98ad5"
im.save(os.path.join(brain_dir, "iphone_home_screen_2x2.png"))
print("Saved perfect iPhone home screen composite!")
