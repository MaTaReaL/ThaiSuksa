# -*- coding: utf-8 -*-
import os

HERE = os.path.dirname(os.path.abspath(__file__))
target_file = os.path.join(HERE, "generate_thai_suksa_flow.py")
source_file = os.path.join(HERE, "test_leave.py")

with open(source_file, "r", encoding="utf-8") as f:
    source_content = f.read()

# Extract code from def s13b_leave_request(): to print("All Leave
start_idx = source_content.find("def s13b_leave_request():")
end_idx = source_content.find('print("All Leave')
assert start_idx != -1 and end_idx != -1, "Could not find slice in test_leave.py"
new_leave_code = source_content[start_idx:end_idx].strip()

with open(target_file, "r", encoding="utf-8") as f:
    target_content = f.read()

# 1. Insert s13b and s13c functions right after s13_class_details
s13_marker = "def s13_class_details():"
assert s13_marker in target_content, "s13_class_details marker not found"
s14_marker = "def s14_exam_schedule():"
assert s14_marker in target_content, "s14_exam_schedule marker not found"

idx_s14 = target_content.find(s14_marker)
target_content = target_content[:idx_s14] + new_leave_code + "\n\n" + target_content[idx_s14:]

# 2. Add "ยื่นลาเรียน" button into s13_class_details()
# Look for {btn("เพิ่มแจ้งเตือน", "bs", go="S15", icon="clock", style="flex:1;")}
btn_anchor = '{btn("เพิ่มแจ้งเตือน", "bs", go="S15", icon="clock", style="flex:1;")}'
assert btn_anchor in target_content, "btn_anchor in s13 not found"

updated_buttons = '''{btn("นำทาง", "bp", go="S23", icon="nav", style="flex:1;")}
          {btn("ยื่นลาเรียน", "bs", go="S13B", icon="receipt", style="flex:1;")}
          {btn("เตือน", "bs", go="S15", icon="clock", style="flex:0.8;")}'''

# Replace the two buttons with three buttons
old_btn_row = '''        <div class="row" style="gap:10px;">
          {btn("นำทางไปยังห้อง ED-304", "bp", go="S23", icon="nav", style="flex:1;")}
          {btn("เพิ่มแจ้งเตือน", "bs", go="S15", icon="clock", style="flex:1;")}
        </div>'''
assert old_btn_row in target_content, "old_btn_row not found"

new_btn_row = f'''        <div class="row" style="gap:8px;">
          {updated_buttons}
        </div>'''
target_content = target_content.replace(old_btn_row, new_btn_row)

# 3. Add quick "ยื่นลาเรียนออนไลน์" button in S12 Schedule top bar
# Find <div class="ib" data-go="S15">{ic("calendar")}</div> in s12_schedule
s12_bar_marker = '<div class="ib" data-go="S15">{ic("calendar")}</div>'
assert s12_bar_marker in target_content, "s12_bar_marker not found"

new_s12_bar = '''<div class="row" style="gap:6px;">
          <div class="ib" data-go="S13B" style="width:36px;height:36px;cursor:pointer;" title="ยื่นลาเรียนออนไลน์">{ic("receipt", 18, C['blue'])}</div>
          <div class="ib" data-go="S15" style="width:36px;height:36px;cursor:pointer;" title="ปฏิทิน">{ic("calendar", 18, C['navy'])}</div>
        </div>'''

target_content = target_content.replace(s12_bar_marker, new_s12_bar)

# 4. Add screens to SCREENS list in Row 4
row4_anchor = '    ("S13", "13. รายละเอียดวิชาเรียน", s13_class_details, 3, 1, ""),'
assert row4_anchor in target_content, "row4_anchor not found in SCREENS"

new_row4_screens = '''    ("S13", "13. รายละเอียดวิชาเรียน", s13_class_details, 3, 1, ""),
    ("S13B", "13B. ยื่นลาเรียนออนไลน์", s13b_leave_request, 3, 2, ""),
    ("S13C", "13C. สถานะคำร้องขอลาเรียน", s13c_leave_status, 3, 3, ""),
    ("S14", "14. ตารางสอบ", s14_exam_schedule, 3, 4, ""),
    ("S15", "15. ปฏิทินการศึกษา", s15_calendar, 3, 5, ""),'''

# Replace Row 4 lines in SCREENS
old_row4 = '''    ("S13", "13. รายละเอียดวิชาเรียน", s13_class_details, 3, 1, ""),
    ("S14", "14. ตารางสอบ", s14_exam_schedule, 3, 2, ""),
    ("S15", "15. ปฏิทินการศึกษา", s15_calendar, 3, 3, ""),'''
assert old_row4 in target_content, "old_row4 not found in SCREENS"

target_content = target_content.replace(old_row4, new_row4_screens)

# 5. Add connections in Schedule Flow
conn_target = '        ("S12", "S15", "เปิดปฏิทิน & เพิ่มนัด", "right", "left"),'
assert conn_target in target_content, "conn_target in Schedule Flow not found"

new_sched_conn = '''        ("S12", "S15", "เปิดปฏิทิน & เพิ่มนัด", "right", "left"),
        ("S12", "S13B", "ลัดยื่นเรื่องลาเรียน", "bottom", "top"),
        ("S13", "S13B", "กดลาเรียนจากวิชานี้", "right", "left"),
        ("S13B", "S13C", "ยื่นคำร้อง -> ดูสถานะ", "right", "left"),
        ("S13C", "S12", "เสร็จสิ้น -> กลับตารางเรียน", "bottom", "bottom"),'''

target_content = target_content.replace(conn_target, new_sched_conn)

with open(target_file, "w", encoding="utf-8") as f:
    f.write(target_content)

print("Successfully integrated Online Leave System into generate_thai_suksa_flow.py!")
