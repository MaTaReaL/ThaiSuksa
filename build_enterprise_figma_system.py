"""Build the complete Enterprise Multi-Page Figma System for THAI SUKSA (ไทยศึกษา) Smart Campus.

Generates:
- figma_pages/00_Cover_Specs.html (Page 00: Cover & Architecture Specs)
- figma_pages/01_Design_System_Master.html (Page 01: ❖ Main Components ตัวแม่)
- figma_pages/02_Page_Auth_Flow.html (Page 02: ◇ Instance S01-S06)
- figma_pages/03_Page_Home_Profile.html (Page 03: ◇ Instance S07-S11)
- figma_pages/04_Page_Academic_Schedule.html (Page 04: ◇ Instance S12-S15)
- figma_pages/05_Page_News_Activities.html (Page 05: ◇ Instance S16-S20)
- figma_pages/06_Page_Map_Transit.html (Page 06: ◇ Instance S21-S24)
- figma_pages/07_Page_Booking_AI_Services.html (Page 07: ◇ Instance S25-S28)
- figma_pages/08_Page_Camplus_Wallet.html (Page 08: ◇ Instance S29-S31)
- figma_pages/09_Page_Master_Board.html (Page 99: Master 31-Screen Board)
"""
import os
import re
import kit
import generate_nexora_flow as flow

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "figma_pages")
os.makedirs(OUT_DIR, exist_ok=True)

C = kit.C
USER = kit.USER
CSS = kit.CSS
ic = kit.ic
img = kit.img
avatar = kit.avatar
sb = kit.sb
hi = kit.hi
bar = kit.bar
nav = kit.nav
uni = kit.uni
badge = kit.badge
btn = kit.btn
field = kit.field
labeled = kit.labeled
qr_svg = kit.qr_svg

def page_html_shell(title, content, width=1920, height=1080, bg="#DDE3EE", is_board=False):
    return f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {CSS}
    @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
    body {{
      background: {bg};
      margin: 0;
      padding: 0;
      font-family: 'IBM Plex Sans Thai', 'Inter', sans-serif;
      color: #101C36;
    }}
    .page-canvas {{
      position: relative;
      width: {width}px;
      min-height: {height}px;
      margin: 0 auto;
      background: {bg};
      overflow: hidden;
    }}
    .component-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 8px;
      font: 700 12px 'Inter', 'IBM Plex Sans Thai';
      letter-spacing: 0.5px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.12);
      flex: none;
    }}
    .badge-master {{
      background: #7C3AED;
      color: #FFFFFF;
      border: 1px solid #A78BFA;
    }}
    .badge-instance {{
      background: #2563EB;
      color: #FFFFFF;
      border: 1px solid #93C5FD;
    }}
    .screen-header-card {{
      position: absolute;
      width: 440px;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 16px;
      padding: 12px 18px;
      box-shadow: 0 4px 15px rgba(16,28,54,0.06);
      box-sizing: border-box;
      z-index: 25;
    }}
    .floating-toolbar {{
      position: fixed;
      top: 20px;
      right: 30px;
      z-index: 9999;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(16, 28, 54, 0.95);
      backdrop-filter: blur(12px);
      padding: 8px 18px;
      border-radius: 40px;
      border: 1.5px solid rgba(88,214,255,0.4);
      box-shadow: 0 14px 35px rgba(0,0,0,0.35);
      color: #fff;
    }}
    .tb-btn {{
      background: #246BFD;
      color: #fff;
      border: none;
      padding: 8px 16px;
      border-radius: 20px;
      font: 700 13px 'IBM Plex Sans Thai','Inter';
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all .2s;
    }}
    .tb-btn:hover {{
      background: #1A54CE;
      transform: translateY(-1px);
    }}
  </style>
</head>
<body>

  <div class="floating-toolbar">
    <div style="font-size:13px;font-weight:700;display:flex;align-items:center;gap:6px;">
      <span style="color:#58D6FF;">✦</span>
      <span>{title}</span>
    </div>
    <button class="tb-btn" onclick="toggleWires()">
      <span>⚡</span>
      <span id="wireToggleText">ซ่อน/แสดง เส้น Prototype Wire</span>
    </button>
  </div>

  <div class="page-canvas">
    {content}
  </div>

  <script>
    function toggleWires() {{
      var svg = document.getElementById('svgConnectors');
      var txt = document.getElementById('wireToggleText');
      if (!svg) return;
      if (svg.style.display === 'none') {{
        svg.style.display = 'block';
        txt.innerText = 'ซ่อนเส้น Prototype Wire';
      }} else {{
        svg.style.display = 'none';
        txt.innerText = 'แสดงเส้น Prototype Wire';
      }}
    }}
  </script>
</body>
</html>
'''

def render_wires_svg(connections, screen_positions, width, height):
    svg_paths = ""
    svg_labels = ""

    for item in connections:
        from_id, to_id, label, from_dir, to_dir = item[:5]
        if from_id not in screen_positions or to_id not in screen_positions:
            continue
        fx, fy = screen_positions[from_id]
        tx, ty = screen_positions[to_id]

        if from_dir == "right":
            x1, y1 = fx + 440, fy + 480
        elif from_dir == "left":
            x1, y1 = fx, fy + 480
        elif from_dir == "bottom":
            x1, y1 = fx + 220, fy + 956
        else: # top
            x1, y1 = fx + 220, fy

        if to_dir == "left":
            x2, y2 = tx, ty + 480
        elif to_dir == "right":
            x2, y2 = tx + 440, ty + 480
        elif to_dir == "top":
            x2, y2 = tx + 220, ty
        else: # bottom
            x2, y2 = tx + 220, ty + 956

        dx = x2 - x1
        dy = y2 - y1

        if from_dir == "bottom" and to_dir == "bottom":
            loop_offset = 100 + abs(fx - tx) * 0.04
            cx1, cy1 = x1, y1 + loop_offset
            cx2, cy2 = x2, y2 + loop_offset
        elif from_dir == "top" and to_dir == "top":
            loop_offset = 100 + abs(fx - tx) * 0.04
            cx1, cy1 = x1, y1 - loop_offset
            cx2, cy2 = x2, y2 - loop_offset
        elif from_dir in ("left", "right") and to_dir in ("left", "right"):
            cx1 = x1 + dx * 0.5
            cy1 = y1
            cx2 = x1 + dx * 0.5
            cy2 = y2
        elif from_dir in ("top", "bottom") and to_dir in ("top", "bottom"):
            cx1 = x1
            cy1 = y1 + dy * 0.5
            cx2 = x2
            cy2 = y1 + dy * 0.5
        else:
            cx1 = x1 + (dx * 0.6 if from_dir == "right" else -dx * 0.6)
            cy1 = y1
            cx2 = x2
            cy2 = y2 - (dy * 0.6 if to_dir == "top" else -dy * 0.6)

        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        path_d = f"M {x1} {y1} C {cx1} {cy1}, {cx2} {cy2}, {x2} {y2}"

        lbl_w = max(140, len(label) * 9 + 40)
        svg_paths += f'''
        <g class="connector-wire-item">
          <path d="{path_d}" fill="none" stroke="#FFFFFF" stroke-width="6" opacity="0.9" />
          <path d="{path_d}" fill="none" stroke="{C['blue']}" stroke-width="3.5" stroke-dasharray="8,6" marker-end="url(#wireArrow)" />
          <circle cx="{x1}" cy="{y1}" r="6" fill="{C['blue']}" stroke="#FFFFFF" stroke-width="2" />
        </g>
        '''

        svg_labels += f'''
        <g transform="translate({mid_x},{mid_y})" class="connector-label-item">
          <rect x="{-lbl_w//2}" y="-14" width="{lbl_w}" height="28" rx="14" fill="{C['navy']}" stroke="{C['cyan']}" stroke-width="1.5" />
          <text x="0" y="4" font-family="'IBM Plex Sans Thai','Inter',sans-serif" font-size="11" font-weight="600" fill="#FFFFFF" text-anchor="middle">{label}</text>
        </g>
        '''

    return f'''
    <!-- PROTOTYPE_FLOW_WIRES Layer (Select and Delete in Figma when wiring is completed) -->
    <svg id="svgConnectors" width="{width}" height="{height}" style="position:absolute;top:0;left:0;pointer-events:none;z-index:10;">
      <defs>
        <marker id="wireArrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="{C['blue']}" />
        </marker>
      </defs>
      {svg_paths}
      {svg_labels}
    </svg>
    '''

def inject_screen_pos(html, s_id, x, y):
    m = re.search(r'<div\s+([^>]*class=[\'"]scr[\'"][^>]*)>', html)
    if not m:
        return html
    attrs = m.group(1)
    style_m = re.search(r'style=[\'"]([^\'"]*)[\'"]', attrs)
    if style_m:
        old_style = style_m.group(1).rstrip(';')
        new_style = f"left:{x}px;top:{y}px;{old_style};"
        new_attrs = attrs[:style_m.start()] + f'style="{new_style}"' + attrs[style_m.end():]
    else:
        new_attrs = attrs + f' style="left:{x}px;top:{y}px;"'
    if 'id=' not in new_attrs:
        new_attrs = f'id="{s_id}" ' + new_attrs
    return html[:m.start()] + f'<div {new_attrs}>' + html[m.end():]

# ---------------------------------------------------------------------------
# Build Page 00: Cover & Specifications
# ---------------------------------------------------------------------------
def build_page_00():
    title = "00 — Project Cover & Architecture Specs"
    content = f'''
    <div style="padding:80px 100px;background:radial-gradient(circle at top right,#1A365D 0%,#0B1528 60%,#050B14 100%);min-height:100vh;color:#fff;box-sizing:border-box;">
      
      <!-- Top Brand Header -->
      <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.12);padding-bottom:30px;margin-bottom:50px;">
        <div style="display:flex;align-items:center;gap:18px;">
          {img("thai_suksa_logo.png", "width:72px;height:72px;border-radius:18px;object-fit:cover;box-shadow:0 10px 25px rgba(0,0,0,0.4);")}
          <div>
            <div style="font:800 34px 'IBM Plex Sans Thai','Inter';letter-spacing:1px;color:#fff;">ไทยศึกษา (THAI SUKSA)</div>
            <div style="font:600 13px 'Inter';letter-spacing:2px;color:{C['cyan']};">CENTRAL HIGHER EDUCATION OPERATING SYSTEM</div>
          </div>
        </div>
        <div style="display:flex;gap:12px;align-items:center;">
          <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.18);padding:8px 16px;border-radius:24px;font-size:13px;color:#E2E8F0;">
            กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (MHESI)
          </div>
          <div style="background:{C['blue']};color:#fff;padding:8px 16px;border-radius:24px;font-size:13px;font-weight:700;">
            v2.5 Enterprise Production
          </div>
        </div>
      </div>

      <!-- Main Title Hero -->
      <div style="margin-bottom:60px;">
        <div style="font:700 16px 'Inter';color:{C['cyan']};text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">Official Design System & Prototype Architecture</div>
        <div style="font:800 48px 'IBM Plex Sans Thai','Inter';line-height:1.2;margin-bottom:18px;max-width:1100px;">
          ระบบสารสนเทศชีวิตนักศึกษาอัจฉริยะแห่งชาติ<br>
          <span style="background:linear-gradient(90deg,#58D6FF,#246BFD);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">รองรับ 65+ มหาวิทยาลัยทั่วประเทศไทย</span>
        </div>
        <div style="font:400 17px 'IBM Plex Sans Thai';color:#94A3B8;max-width:850px;line-height:1.7;">
          แพลตฟอร์มกลางระดับประเทศ เชื่อมต่อบริการการศึกษา การเดินทาง สิ่งอำนวยความสะดวก ปัญญาประดิษฐ์ (AI Copilot) และสวัสดิการค่าครองชีพนักศึกษา <strong>โครงการ Camplus (฿3,000/เดือน)</strong> ภายใต้กรอบมาตรฐานความปลอดภัยระดับสูงสุด
        </div>
      </div>

      <!-- 4 Pillars Grid -->
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:30px;margin-bottom:60px;">
        
        <!-- Box 1: Persona & Test Account -->
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:32px;">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
            <div style="width:40px;height:40px;border-radius:12px;background:rgba(36,107,253,0.2);display:flex;align-items:center;justify-content:center;color:{C['cyan']};">
              {ic('user', 22, C['cyan'])}
            </div>
            <div>
              <div style="font:700 18px 'IBM Plex Sans Thai';color:#fff;">ข้อมูลนักศึกษา & บัญชีทดสอบระบบ</div>
              <div style="font:400 12px 'Inter';color:#94A3B8;">Student Persona & Official Credentials</div>
            </div>
          </div>
          <div style="display:flex;gap:20px;align-items:center;margin-bottom:20px;padding:16px;background:rgba(255,255,255,0.03);border-radius:16px;">
            {avatar(64, C['cyan'])}
            <div>
              <div style="font:700 18px 'IBM Plex Sans Thai';color:#fff;">{USER['th_full']}</div>
              <div style="font:500 13px 'Inter';color:{C['cyan']};">{USER['en']}</div>
              <div style="font:600 14px 'Inter';color:#E2E8F0;margin-top:4px;">รหัสนักศึกษา: {USER['sid']}</div>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:13px;">
            <div><span style="color:#64748B;">คณะ:</span> <span style="color:#E2E8F0;font-weight:600;">{USER['fac']}</span></div>
            <div><span style="color:#64748B;">สาขา:</span> <span style="color:#E2E8F0;font-weight:600;">{USER['major']}</span></div>
            <div><span style="color:#64748B;">มหาวิทยาลัย:</span> <span style="color:#E2E8F0;font-weight:600;">{USER['uni']}</span></div>
            <div><span style="color:#64748B;">วิทยาเขต:</span> <span style="color:#E2E8F0;font-weight:600;">{USER['campus']}</span></div>
            <div><span style="color:#64748B;">อีเมลสถาบัน:</span> <span style="color:#E2E8F0;font-weight:600;">{USER['email']}</span></div>
            <div><span style="color:#64748B;">สถานะ:</span> <span style="color:#10B981;font-weight:700;">กำลังศึกษา ({USER['year']})</span></div>
          </div>
        </div>

        <!-- Box 2: Camplus Welfare System -->
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:32px;">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
            <div style="width:40px;height:40px;border-radius:12px;background:rgba(22,166,117,0.2);display:flex;align-items:center;justify-content:center;color:#10B981;">
              {ic('wallet', 22, '#10B981')}
            </div>
            <div>
              <div style="font:700 18px 'IBM Plex Sans Thai';color:#fff;">ระบบสวัสดิการ โครงการ Camplus</div>
              <div style="font:400 12px 'Inter';color:#94A3B8;">National Student Living Stipend Project</div>
            </div>
          </div>
          <div style="padding:20px;background:linear-gradient(135deg,rgba(16,185,129,0.15),rgba(36,107,253,0.15));border-radius:18px;border:1px solid rgba(88,214,255,0.25);margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <div>
                <div style="font:600 12px 'Inter';color:#A7F3D0;text-transform:uppercase;">Monthly Allowance Quota</div>
                <div style="font:800 32px 'Inter';color:#FFFFFF;margin-top:4px;">฿ 3,000<span style="font-size:16px;color:#A7F3D0;font-weight:500;">.00 / เดือน</span></div>
              </div>
              <div style="background:#10B981;color:#fff;padding:6px 14px;border-radius:20px;font:700 12px 'IBM Plex Sans Thai';">สวัสดิการแจกฟรี</div>
            </div>
            <div style="font:400 13px 'IBM Plex Sans Thai';color:#CBD5E1;margin-top:12px;line-height:1.6;">
              โครงการสนับสนุนค่าครองชีพนักศึกษาระดับอุดมศึกษา แจกงบอัตโนมัติทุกวันที่ 1 ของเดือน ใช้จ่ายซื้ออาหาร อุปกรณ์การศึกษา และผลิตภัณฑ์ภายในมหาวิทยาลัย
            </div>
          </div>
          <div style="display:flex;gap:10px;font-size:12px;color:#94A3B8;">
            <div style="display:flex;align-items:center;gap:6px;"><span>✓</span> QR Dynamic Payment</div>
            <div style="display:flex;align-items:center;gap:6px;"><span>✓</span> Zero Transaction Fee</div>
            <div style="display:flex;align-items:center;gap:6px;"><span>✓</span> MHESI e-Tax Receipt</div>
          </div>
        </div>

        <!-- Box 3: Technical Specifications -->
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:32px;">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
            <div style="width:40px;height:40px;border-radius:12px;background:rgba(88,214,255,0.2);display:flex;align-items:center;justify-content:center;color:{C['cyan']};">
              {ic('phone', 22, C['cyan'])}
            </div>
            <div>
              <div style="font:700 18px 'IBM Plex Sans Thai';color:#fff;">สเปกการออกแบบ (Hardware & Viewport)</div>
              <div style="font:400 12px 'Inter';color:#94A3B8;">Device Geometry & Display Standards</div>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;font-size:14px;">
            <div style="padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;">
              <div style="color:#64748B;font-size:12px;">Target Hardware</div>
              <div style="color:#FFFFFF;font-weight:700;margin-top:2px;">Apple iPhone 16 Pro Max</div>
            </div>
            <div style="padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;">
              <div style="color:#64748B;font-size:12px;">Canvas Viewport</div>
              <div style="color:#FFFFFF;font-weight:700;margin-top:2px;">440 × 956 px (3x Retina)</div>
            </div>
            <div style="padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;">
              <div style="color:#64748B;font-size:12px;">Corner Radius</div>
              <div style="color:#FFFFFF;font-weight:700;margin-top:2px;">55 px (Curved Display)</div>
            </div>
            <div style="padding:14px;background:rgba(255,255,255,0.03);border-radius:12px;">
              <div style="color:#64748B;font-size:12px;">Interactive Notch</div>
              <div style="color:#FFFFFF;font-weight:700;margin-top:2px;">Dynamic Island (126×37px)</div>
            </div>
          </div>
        </div>

        <!-- Box 4: Enterprise Figma Architecture -->
        <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:32px;">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:20px;">
            <div style="width:40px;height:40px;border-radius:12px;background:rgba(124,58,237,0.2);display:flex;align-items:center;justify-content:center;color:#A78BFA;">
              {ic('grid', 22, '#A78BFA')}
            </div>
            <div>
              <div style="font:700 18px 'IBM Plex Sans Thai';color:#fff;">มาตรฐานระบบ Multi-Page สำหรับ Figma</div>
              <div style="font:400 12px 'Inter';color:#94A3B8;">Enterprise Page Organization Hierarchy</div>
            </div>
          </div>
          <div style="display:flex;flex-direction:column;gap:10px;font-size:13px;">
            <div style="display:flex;align-items:center;gap:10px;">
              <span class="component-badge badge-master">❖ Main Component (ตัวแม่)</span>
              <span style="color:#CBD5E1;">รวบรวมในหน้า <code>01 — Design System</code> สำหรับเป็นคลังกลาง</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px;">
              <span class="component-badge badge-instance">◇ Instance (ตัวลูก)</span>
              <span style="color:#CBD5E1;">นำไปประกอบในหน้า User Flows (หน้า 02–08)</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px;">
              <span style="background:#0F172A;border:1px solid #58D6FF;color:#58D6FF;padding:4px 10px;border-radius:6px;font:700 11px Inter;">PROTOTYPE_FLOW_WIRES</span>
              <span style="color:#CBD5E1;">Layer เส้นเชื่อมตัวอย่าง พร้อมปุ่มซ่อน/แสดง และเลือกลบได้ทันที</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Page Directory Table -->
      <div style="background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);border-radius:24px;padding:32px;">
        <div style="font:700 20px 'IBM Plex Sans Thai';color:#fff;margin-bottom:18px;">
          สารบัญโครงสร้างไฟล์และหน้าใน Figma (Enterprise Page Directory)
        </div>
        <table style="width:100%;border-collapse:collapse;font-size:14px;color:#CBD5E1;">
          <thead>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.15);text-align:left;color:#94A3B8;font-size:12px;text-transform:uppercase;">
              <th style="padding:12px;">ลำดับหน้า</th>
              <th style="padding:12px;">ชื่อหน้าใน Figma</th>
              <th style="padding:12px;">หมวดหมู่ฟังก์ชัน</th>
              <th style="padding:12px;">จำนวนจอ</th>
              <th style="padding:12px;">ประเภท Component</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 00</td>
              <td style="padding:12px;font-weight:600;color:#fff;">00_Cover_Specs.html</td>
              <td style="padding:12px;">Cover Page & System Technical Architecture</td>
              <td style="padding:12px;">1 Spec Frame</td>
              <td style="padding:12px;"><span style="color:#94A3B8;">Documentation</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 01</td>
              <td style="padding:12px;font-weight:600;color:#fff;">01_Design_System_Master.html</td>
              <td style="padding:12px;">❖ Master Design System (Tokens, Atoms, Cards, Bars, Camplus)</td>
              <td style="padding:12px;">24+ Components</td>
              <td style="padding:12px;"><span class="component-badge badge-master">❖ Main Component</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 02</td>
              <td style="padding:12px;font-weight:600;color:#fff;">02_Page_Auth_Flow.html</td>
              <td style="padding:12px;">🔐 Central Onboarding & Multi-University SSO (S01–S06)</td>
              <td style="padding:12px;">6 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 03</td>
              <td style="padding:12px;font-weight:600;color:#fff;">03_Page_Home_Profile.html</td>
              <td style="padding:12px;">🏠 Main Dashboard, Hamburger Drawer & Digital ID (S07–S11)</td>
              <td style="padding:12px;">5 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 04</td>
              <td style="padding:12px;font-weight:600;color:#fff;">04_Page_Academic_Schedule.html</td>
              <td style="padding:12px;">📚 Weekly Timetable, Course Syllabus & Exams (S12–S15)</td>
              <td style="padding:12px;">4 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 05</td>
              <td style="padding:12px;font-weight:600;color:#fff;">05_Page_News_Activities.html</td>
              <td style="padding:12px;">📢 University News, Student Clubs & Event QR Tickets (S16–S20)</td>
              <td style="padding:12px;">5 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 06</td>
              <td style="padding:12px;font-weight:600;color:#fff;">06_Page_Map_Transit.html</td>
              <td style="padding:12px;">🗺️ Interactive Campus Map & Live EV Shuttle Tracker (S21–S24)</td>
              <td style="padding:12px;">4 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 07</td>
              <td style="padding:12px;font-weight:600;color:#fff;">07_Page_Booking_AI_Services.html</td>
              <td style="padding:12px;">🤖 Study Room Booking, ไทยศึกษา AI Copilot & e-Petitions (S25–S28)</td>
              <td style="padding:12px;">4 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 08</td>
              <td style="padding:12px;font-weight:600;color:#fff;">08_Page_Camplus_Wallet.html</td>
              <td style="padding:12px;">💳 Camplus Welfare Wallet (฿3,000/mo), Scan & Pay & e-Slip (S29–S31)</td>
              <td style="padding:12px;">3 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Instance</span></td>
            </tr>
            <tr>
              <td style="padding:12px;font-weight:700;color:{C['cyan']};">Page 99</td>
              <td style="padding:12px;font-weight:600;color:#fff;">09_Page_Master_Board.html</td>
              <td style="padding:12px;">🌐 Consolidated Executive Master Board (All 31 Screens + Full Wires)</td>
              <td style="padding:12px;">31 Screens</td>
              <td style="padding:12px;"><span class="component-badge badge-instance">◇ Full Flow</span></td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
    '''
    return page_html_shell(title, content, width=1920, height=1280, bg="#0B1528")

# ---------------------------------------------------------------------------
# Build Page 01: Design System Master Components (ตัวแม่)
# ---------------------------------------------------------------------------
def build_page_01():
    title = "01 — ❖ Master Design System (คลัง Component ตัวแม่)"
    
    # We construct comprehensive, pixel-perfect master components
    content = f'''
    <div style="padding:80px 100px;background:#F1F5F9;min-height:100vh;color:#101C36;box-sizing:border-box;">
      
      <!-- Design System Header -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:50px;box-shadow:0 8px 30px rgba(16,28,54,0.06);">
        <div style="display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
              <span class="component-badge badge-master">❖ Master Component Library</span>
              <span style="font:700 13px 'Inter';color:#7C3AED;">Single Source of Truth</span>
            </div>
            <div style="font:800 36px 'IBM Plex Sans Thai','Inter';color:#101C36;">
              ไทยศึกษา Master UI Components (ตัวแม่ทั้งหมด)
            </div>
            <div style="font:400 15px 'IBM Plex Sans Thai';color:#64748B;margin-top:6px;max-width:850px;">
              ชิ้นส่วน UI ทั้งหมดในหน้านี้ได้รับการกำหนดเป็น <strong>[ ❖ Main Component (ตัวแม่) ]</strong> ตามมาตรฐานสากล เมื่อนำเข้า Figma สามารถกด <code>Ctrl+Alt+K</code> (หรือ <code>Cmd+Option+K</code>) เพื่อ Publish เข้าสู่ Team Library ได้ทันที
            </div>
          </div>
          <div style="text-align:right;">
            <div style="font:800 24px 'Inter';color:{C['blue']};">30+ Components</div>
            <div style="font:500 13px 'Inter';color:#94A3B8;">Tokens • Atoms • Organisms</div>
          </div>
        </div>
      </div>

      <!-- Section 1: Brand Identity & Logo Master System (คลังโลโก้ตัวแม่ 4 เวอร์ชั่น) -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:40px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">1. Brand Identity & Logo Master System (คลังโลโก้ตัวแม่ 4 เวอร์ชั่น)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">Multi-Context High-Legibility Assets • ไดคัดพื้นหลังโปร่งใส 100% • สลับใช้อัตโนมัติตามค่าความสว่างพื้นผิว (Light vs Dark Surfaces)</div>
          </div>
          <span class="component-badge badge-master">❖ Logo Master Assets</span>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
          
          <!-- Logo V1: Light Surface Full Logo -->
          <div style="background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:18px;padding:20px;display:flex;flex-direction:column;align-items:center;text-align:center;">
            <div style="width:100%;height:160px;background:#FFFFFF;border-radius:14px;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px;padding:12px;">
              {img("logo_v1_light_full.png", "max-width:130px;max-height:130px;object-fit:contain;")}
            </div>
            <span class="component-badge badge-master" style="margin-bottom:6px;">❖ Logo / V1 Light Full</span>
            <div style="font:700 14px 'IBM Plex Sans Thai';color:#101C36;">เวอร์ชั่น 1: สำหรับพื้นผิวสว่าง (Light)</div>
            <div style="font:400 12px 'IBM Plex Sans Thai';color:#64748B;margin-top:4px;line-height:1.4;">
              ตราสัญลักษณ์ยอดปรางค์ + ตัวอักษร "ไทยศึกษา" สีกรมท่า คมชัดสูงสุดบนพื้นหลังสีขาวหรือสีอ่อน (เช่น หน้า Onboarding, หน้าบัตรนักศึกษา, ฟอร์มลงทะเบียน)
            </div>
            <div style="margin-top:10px;font:600 11px Inter;color:#246BFD;background:#EAF1FF;padding:4px 10px;border-radius:10px;">assets/logo_v1_light_full.png</div>
          </div>

          <!-- Logo V2: Dark Surface Full Logo -->
          <div style="background:#0F172A;border:1.5px solid #1E293B;border-radius:18px;padding:20px;display:flex;flex-direction:column;align-items:center;text-align:center;">
            <div style="width:100%;height:160px;background:#101C36;border-radius:14px;border:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;margin-bottom:14px;padding:12px;">
              {img("logo_v2_dark_full.png", "max-width:130px;max-height:130px;object-fit:contain;filter:drop-shadow(0 8px 20px rgba(36,107,253,0.45));")}
            </div>
            <span class="component-badge badge-master" style="margin-bottom:6px;background:rgba(255,255,255,0.1);color:#58D6FF;border-color:rgba(88,214,255,0.3);">❖ Logo / V2 Dark Full</span>
            <div style="font:700 14px 'IBM Plex Sans Thai';color:#FFFFFF;">เวอร์ชั่น 2: สำหรับพื้นผิวมืด (Dark)</div>
            <div style="font:400 12px 'IBM Plex Sans Thai';color:#94A3B8;margin-top:4px;line-height:1.4;">
              ตราสัญลักษณ์ยอดปรางค์เรืองแสง + ตัวอักษรสีขาวสว่างและช่อชัยพฤกษ์สีทอง คมชัดบนพื้นหลัง Midnight Navy (เช่น Splash S01, Cover Specs, Drawer Menu Header)
            </div>
            <div style="margin-top:10px;font:600 11px Inter;color:#58D6FF;background:rgba(88,214,255,0.12);padding:4px 10px;border-radius:10px;">assets/logo_v2_dark_full.png</div>
          </div>

          <!-- Logo V3: App Icon Squircle Light -->
          <div style="background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:18px;padding:20px;display:flex;flex-direction:column;align-items:center;text-align:center;">
            <div style="width:100%;height:160px;background:#FFFFFF;border-radius:14px;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
              {img("logo_v3_icon_light.png", "width:110px;height:110px;object-fit:contain;filter:drop-shadow(0 10px 20px rgba(16,28,54,0.12));")}
            </div>
            <span class="component-badge badge-master" style="margin-bottom:6px;">❖ Icon / V3 Light Squircle</span>
            <div style="font:700 14px 'IBM Plex Sans Thai';color:#101C36;">เวอร์ชั่น 3: App Icon ขาว (Light)</div>
            <div style="font:400 12px 'IBM Plex Sans Thai';color:#64748B;margin-top:4px;line-height:1.4;">
              ไอคอน Squircle ขอบมนสีขาว ใช้บน App Store, Light Home Launcher, การแจ้งเตือนระบบแบบการ์ดสว่าง
            </div>
            <div style="margin-top:10px;font:600 11px Inter;color:#246BFD;background:#EAF1FF;padding:4px 10px;border-radius:10px;">assets/logo_v3_icon_light.png</div>
          </div>

          <!-- Logo V4: App Icon Squircle Dark -->
          <div style="background:#0F172A;border:1.5px solid #1E293B;border-radius:18px;padding:20px;display:flex;flex-direction:column;align-items:center;text-align:center;">
            <div style="width:100%;height:160px;background:#101C36;border-radius:14px;border:1px solid rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;margin-bottom:14px;">
              {img("logo_v4_icon_dark.png", "width:110px;height:110px;object-fit:contain;filter:drop-shadow(0 10px 20px rgba(36,107,253,0.35));")}
            </div>
            <span class="component-badge badge-master" style="margin-bottom:6px;background:rgba(255,255,255,0.1);color:#58D6FF;border-color:rgba(88,214,255,0.3);">❖ Icon / V4 Dark Squircle</span>
            <div style="font:700 14px 'IBM Plex Sans Thai';color:#FFFFFF;">เวอร์ชั่น 4: App Icon กรมท่า (Dark)</div>
            <div style="font:400 12px 'IBM Plex Sans Thai';color:#94A3B8;margin-top:4px;line-height:1.4;">
              ไอคอน Squircle สีกรมท่าเรืองแสง ใช้บน Dark Mode Launcher, Student ID Smart Card, Apple Wallet Pass, Security Badges
            </div>
            <div style="margin-top:10px;font:600 11px Inter;color:#58D6FF;background:rgba(88,214,255,0.12);padding:4px 10px;border-radius:10px;">assets/logo_v4_icon_dark.png</div>
          </div>

        </div>
      </div>

      <!-- Section 2: Color Tokens -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:40px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">2. Design Color Tokens (ชุดสีหลัก)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">Semantic Brand & System Color Scales</div>
          </div>
          <span class="component-badge badge-master">❖ Token Styles</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(6,1fr);gap:18px;">
          <div style="background:{C['blue']};color:#fff;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Electric Blue</div>
            <div>
              <div style="font:800 16px 'Inter';">{C['blue']}</div>
              <div style="font:500 11px 'Inter';opacity:0.8;">Primary Brand</div>
            </div>
          </div>
          <div style="background:{C['navy']};color:#fff;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Midnight Navy</div>
            <div>
              <div style="font:800 16px 'Inter';">{C['navy']}</div>
              <div style="font:500 11px 'Inter';opacity:0.8;">Dark Surface / Text</div>
            </div>
          </div>
          <div style="background:{C['cyan']};color:#101C36;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Cyan Accent</div>
            <div>
              <div style="font:800 16px 'Inter';">{C['cyan']}</div>
              <div style="font:500 11px 'Inter';opacity:0.8;">Action / Highlight</div>
            </div>
          </div>
          <div style="background:#10B981;color:#fff;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Camplus Green</div>
            <div>
              <div style="font:800 16px 'Inter';">#10B981</div>
              <div style="font:500 11px 'Inter';opacity:0.8;">Welfare / Success</div>
            </div>
          </div>
          <div style="background:#EF4444;color:#fff;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Danger Red</div>
            <div>
              <div style="font:800 16px 'Inter';">#EF4444</div>
              <div style="font:500 11px 'Inter';opacity:0.8;">Alert / Error</div>
            </div>
          </div>
          <div style="background:#F5F7FB;color:#101C36;border:1px solid #CBD5E1;border-radius:16px;padding:20px;height:120px;display:flex;flex-direction:column;justify-content:space-between;">
            <div style="font:700 14px 'Inter';">Canvas Light</div>
            <div>
              <div style="font:800 16px 'Inter';">#F5F7FB</div>
              <div style="font:500 11px 'Inter';color:#64748B;">Background</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Section 3: Buttons & Interactive Controls -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:40px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">3. Buttons & Interactive Controls (ปุ่มตัวแม่)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">Primary, Navy, Outline, Soft Tint, Chips & Segmented Tabs</div>
          </div>
          <span class="component-badge badge-master">❖ Button Components</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px;align-items:center;">
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Btn / Primary Solid</div>
            <div class="btn bp" style="width:100%;">
              <span>ยืนยันการดำเนินการ</span>
              {ic('right', 18, '#fff')}
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Btn / Midnight Navy</div>
            <div class="btn bn" style="width:100%;">
              {ic('lock', 18, '#fff')}
              <span>เข้าสู่ระบบผ่าน SSO</span>
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Btn / Soft Tint</div>
            <div class="btn bt" style="width:100%;">
              {ic('calendar', 18, C['blue'])}
              <span>ดูตารางเรียนทั้งหมด</span>
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Btn / Outline Secondary</div>
            <div class="btn bs" style="width:100%;">
              {ic('swap', 18, C['navy'])}
              <span>เปลี่ยนสถาบัน</span>
            </div>
          </div>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:24px;padding-top:24px;border-top:1px solid #E2E8F0;">
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Segmented Control (Tabs)</div>
            <div class="seg">
              <div class="on">สัปดาห์นี้</div>
              <div>ตารางสอบ</div>
              <div>ปฏิทิน</div>
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Filter Chips (Active & Default)</div>
            <div class="chips">
              <div class="chip on">{ic('building', 14, '#fff')} อาคารเรียน</div>
              <div class="chip">{ic('food', 14, '#64748B')} โรงอาหาร</div>
              <div class="chip">{ic('bus', 14, '#64748B')} รถราง EV</div>
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Status Badges & Pills</div>
            <div style="display:flex;gap:8px;flex-wrap:wrap;">
              <span class="badge b-blue">MHESI Verified</span>
              <span class="badge b-green">โครงการ Camplus</span>
              <span class="badge b-amber">กำลังตรวจสอบ</span>
              <span class="badge b-red">ปิดรับสมัคร</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Section 4: Forms & Input Fields -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:40px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">4. Form Elements & Search Inputs (ช่องกรอกตัวแม่)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">Text fields, Search, Password toggles & University Picker</div>
          </div>
          <span class="component-badge badge-master">❖ Input Components</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Field / Search with Icon</div>
            <div class="field">
              {ic('search', 20, '#94A3B8')}
              <input type="text" placeholder="ค้นหารายวิชา, ห้องเรียน, ร้านค้า..." style="border:none;outline:none;width:100%;font:500 14px 'IBM Plex Sans Thai';background:transparent;" value="อาคารเรียนรวม 1">
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Field / University Selector</div>
            <div class="field" style="justify-content:space-between;cursor:pointer;">
              <div style="display:flex;align-items:center;gap:10px;">
                {img("thai_suksa_logo.png", "width:24px;height:24px;border-radius:6px;object-fit:cover;")}
                <span style="font:600 14px 'IBM Plex Sans Thai';color:#101C36;">มหาวิทยาลัยศิลปากร</span>
              </div>
              {ic('down', 18, '#64748B')}
            </div>
          </div>
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Field / Password with Eye Toggle</div>
            <div class="field" style="justify-content:space-between;">
              <div style="display:flex;align-items:center;gap:10px;">
                {ic('lock', 20, '#94A3B8')}
                <span style="font:600 15px 'Inter';letter-spacing:2px;color:#101C36;">••••••••••••</span>
              </div>
              {ic('eye', 20, '#64748B')}
            </div>
          </div>
        </div>
      </div>

      <!-- Section 5: Camplus Welfare & Digital Wallet Components -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;margin-bottom:40px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">5. Camplus Welfare & Financial Components (ตัวแม่ระบบกระเป๋าเงิน & โครงการ Camplus)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">Allowance Cards, Payment Source Tile, History Row & Digital e-Slip</div>
          </div>
          <span class="component-badge badge-master">❖ Camplus Master Components</span>
        </div>
        
        <div style="display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:24px;align-items:start;">
          
          <!-- Camplus Quota Card -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / Camplus Allowance Card</div>
            <div style="background:linear-gradient(135deg,#101C36 0%,#1E3A8A 100%);border-radius:22px;padding:24px;color:#fff;box-shadow:0 12px 30px rgba(16,28,54,0.25);">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
                <div style="display:flex;align-items:center;gap:8px;">
                  <span style="width:10px;height:10px;border-radius:50%;background:#10B981;box-shadow:0 0 8px #10B981;"></span>
                  <span style="font:700 12px 'Inter';letter-spacing:1px;color:#A7F3D0;">โครงการ CAMPLUS STIPEND</span>
                </div>
                <span class="badge b-green" style="font-size:11px;">กระทรวง อว.</span>
              </div>
              <div style="font:800 32px 'Inter';color:#FFFFFF;margin-bottom:4px;">฿ 2,450<span style="font-size:16px;color:#94A3B8;font-weight:500;"> / 3,000.00</span></div>
              <div style="font:400 12px 'IBM Plex Sans Thai';color:#94A3B8;margin-bottom:14px;">ยอดสวัสดิการคงเหลือประจำเดือน • รีเซ็ตทุกวันที่ 1</div>
              <div style="width:100%;height:8px;border-radius:4px;background:rgba(255,255,255,0.15);overflow:hidden;">
                <div style="width:81%;height:100%;background:linear-gradient(90deg,#10B981,#58D6FF);border-radius:4px;"></div>
              </div>
            </div>
          </div>

          <!-- Payment Selector Tile -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / Payment Source Selector</div>
            <div style="display:flex;flex-direction:column;gap:12px;">
              <div style="border:2px solid {C['blue']};background:#F0F5FF;border-radius:16px;padding:14px;display:flex;align-items:center;justify-content:space-between;">
                <div style="display:flex;align-items:center;gap:12px;">
                  <div style="width:40px;height:40px;border-radius:10px;background:#101C36;display:flex;align-items:center;justify-content:center;color:#10B981;">
                    {ic('wallet', 20, '#10B981')}
                  </div>
                  <div>
                    <div style="font:700 14px 'IBM Plex Sans Thai';color:#101C36;">โครงการ Camplus</div>
                    <div style="font:500 12px 'Inter';color:#10B981;">คงเหลือ ฿ 2,450.00</div>
                  </div>
                </div>
                <div style="width:20px;height:20px;border-radius:50%;background:{C['blue']};display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;">✓</div>
              </div>

              <div style="border:1px solid #CBD5E1;background:#FFFFFF;border-radius:16px;padding:14px;display:flex;align-items:center;justify-content:space-between;">
                <div style="display:flex;align-items:center;gap:12px;">
                  <div style="width:40px;height:40px;border-radius:10px;background:#F1F5F9;display:flex;align-items:center;justify-content:center;color:#64748B;">
                    {ic('card', 20, '#64748B')}
                  </div>
                  <div>
                    <div style="font:700 14px 'IBM Plex Sans Thai';color:#101C36;">บัญชีส่วนตัว / พร้อมเพย์</div>
                    <div style="font:500 12px 'Inter';color:#64748B;">คงเหลือ ฿ 1,840.50</div>
                  </div>
                </div>
                <div style="width:20px;height:20px;border-radius:50%;border:1px solid #CBD5E1;"></div>
              </div>
            </div>
          </div>

          <!-- Transaction Row Item -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / Transaction Row</div>
            <div style="background:#FFFFFF;border:1px solid #E2E8F0;border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:10px;">
              <div style="display:flex;align-items:center;justify-content:space-between;">
                <div style="display:flex;align-items:center;gap:10px;">
                  <div style="width:36px;height:36px;border-radius:10px;background:#F0FDF4;display:flex;align-items:center;justify-content:center;color:#10B981;">
                    {ic('food', 18, '#10B981')}
                  </div>
                  <div>
                    <div style="font:600 13px 'IBM Plex Sans Thai';color:#101C36;">โรงอาหารกลาง สระแก้ว</div>
                    <div style="font:400 11px 'Inter';color:#94A3B8;">วันนี้ • 12:15 น. (Camplus)</div>
                  </div>
                </div>
                <div style="font:700 14px 'Inter';color:#10B981;">- ฿ 50.00</div>
              </div>
              <div style="height:1px;background:#F1F5F9;"></div>
              <div style="display:flex;align-items:center;justify-content:space-between;">
                <div style="display:flex;align-items:center;gap:10px;">
                  <div style="width:36px;height:36px;border-radius:10px;background:#EFF6FF;display:flex;align-items:center;justify-content:center;color:{C['blue']};">
                    {ic('book', 18, C['blue'])}
                  </div>
                  <div>
                    <div style="font:600 13px 'IBM Plex Sans Thai';color:#101C36;">ศูนย์หนังสือศิลปากร</div>
                    <div style="font:400 11px 'Inter';color:#94A3B8;">เมื่อวาน • 15:40 น. (Camplus)</div>
                  </div>
                </div>
                <div style="font:700 14px 'Inter';color:#10B981;">- ฿ 240.00</div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- Section 6: Organisms, Bars & Campus Cards -->
      <div style="background:#FFFFFF;border:1px solid #CBD5E1;border-radius:24px;padding:36px;box-shadow:0 6px 20px rgba(16,28,54,0.04);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:24px;">
          <div>
            <div style="font:700 22px 'IBM Plex Sans Thai';color:#101C36;">6. Organisms, Navigation Bars & Campus Cards (การ์ด & แถบนำทางตัวแม่)</div>
            <div style="font:400 13px 'Inter';color:#64748B;">iOS Status Bar, Bottom Nav, Course Card, Digital ID & AI Assistant Bubble</div>
          </div>
          <span class="component-badge badge-master">❖ Organism Components</span>
        </div>
        
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">
          
          <!-- Course Card -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / Course Timetable Card</div>
            <div class="card" style="box-shadow:0 4px 15px rgba(16,28,54,0.05);">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span class="badge b-blue">08:30 - 11:30 น.</span>
                <span style="font:600 12px 'Inter';color:#64748B;">3(2-2-5) หน่วยกิต</span>
              </div>
              <div style="font:700 16px 'IBM Plex Sans Thai';color:#101C36;">084312 นวัตกรรมการเรียนรู้ดิจิทัล</div>
              <div style="font:400 13px 'IBM Plex Sans Thai';color:#64748B;margin-top:4px;">
                {ic('pin', 14, '#64748B')} ห้อง ศษ.402 • อาคารศึกษาศาสตร์ 1
              </div>
              <div style="margin-top:12px;display:flex;justify-content:space-between;align-items:center;padding-top:10px;border-top:1px solid #F1F5F9;">
                <span style="font:500 12px 'IBM Plex Sans Thai';color:#64748B;">อ.ดร. นันทิยา กิตติวงศ์</span>
                <span style="font:600 12px 'IBM Plex Sans Thai';color:{C['blue']};">เช็กอินแล้ว ✓</span>
              </div>
            </div>
          </div>

          <!-- Digital ID Mini Card -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / Student Digital ID Badge</div>
            <div style="background:linear-gradient(135deg,#101C36,#1E3A8A);border-radius:18px;padding:18px;color:#fff;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                <div style="display:flex;align-items:center;gap:8px;">
                  {img("thai_suksa_logo.png", "width:20px;height:20px;border-radius:5px;object-fit:cover;")}
                  <span style="font:700 11px 'Inter';color:#58D6FF;">SILPAKORN DIGITAL ID</span>
                </div>
                <span style="font:700 11px 'Inter';color:#A7F3D0;">VERIFIED</span>
              </div>
              <div style="display:flex;gap:12px;align-items:center;">
                {avatar(44, '#58D6FF')}
                <div>
                  <div style="font:700 14px 'IBM Plex Sans Thai';">{USER['th_full']}</div>
                  <div style="font:600 12px 'Inter';color:#CBD5E1;">ID: {USER['sid']}</div>
                </div>
              </div>
            </div>
          </div>

          <!-- AI Assistant Chat Bubble -->
          <div>
            <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:8px;">❖ Component / ไทยศึกษา AI Bubble</div>
            <div style="display:flex;flex-direction:column;gap:8px;">
              <div style="background:{C['blue']};color:#fff;border-radius:16px 16px 4px 16px;padding:12px 16px;align-self:flex-end;max-width:85%;font-size:13px;">
                สอบถามหน่อย วันนี้มีห้องอ่านหนังสือว่างที่ตึกไหนบ้าง?
              </div>
              <div style="background:#F1F5F9;border:1px solid #E2E8F0;border-radius:16px 16px 16px 4px;padding:12px 16px;align-self:flex-start;max-width:90%;font-size:13px;display:flex;gap:10px;">
                <div style="width:24px;height:24px;border-radius:50%;background:#101C36;display:flex;align-items:center;justify-content:center;color:#58D6FF;flex:none;">
                  {ic('spark', 14, '#58D6FF')}
                </div>
                <div>
                  <div style="font-weight:700;color:{C['blue']};font-size:11px;margin-bottom:2px;">ไทยศึกษา AI COPILOT</div>
                  <div>ขณะนี้ที่ <strong>หอสมุดพระราชวังสนามจันทร์ ชั้น 3</strong> มี Co-working Space ว่าง 4 ห้อง สามารถกดจองผ่านแอปได้ทันทีครับ!</div>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Floating Bottom Navigation Component Full Width -->
        <div style="margin-top:30px;padding-top:24px;border-top:1px solid #E2E8F0;">
          <div style="font:600 12px 'Inter';color:#64748B;margin-bottom:12px;">❖ Organism / Floating Bottom Navigation Bar (5 Primary Tabs)</div>
          <div style="position:relative;height:92px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:24px;display:flex;justify-content:space-around;align-items:center;box-shadow:0 10px 25px rgba(16,28,54,0.06);max-width:440px;">
            <div class="it on" style="display:flex;flex-direction:column;align-items:center;gap:4px;color:{C['blue']};font:700 11px 'IBM Plex Sans Thai';">
              {ic('home', 22, C['blue'])}
              <span>หน้าหลัก</span>
            </div>
            <div class="it" style="display:flex;flex-direction:column;align-items:center;gap:4px;color:#94A3B8;font:500 11px 'IBM Plex Sans Thai';">
              {ic('calendar', 22, '#94A3B8')}
              <span>ตารางเรียน</span>
            </div>
            <div class="it" style="display:flex;flex-direction:column;align-items:center;gap:4px;color:#94A3B8;font:500 11px 'IBM Plex Sans Thai';">
              {ic('star', 22, '#94A3B8')}
              <span>กิจกรรม</span>
            </div>
            <div class="it" style="display:flex;flex-direction:column;align-items:center;gap:4px;color:#94A3B8;font:500 11px 'IBM Plex Sans Thai';">
              {ic('wallet', 22, '#94A3B8')}
              <span>กระเป๋าเงิน</span>
            </div>
            <div class="it" style="display:flex;flex-direction:column;align-items:center;gap:4px;color:#94A3B8;font:500 11px 'IBM Plex Sans Thai';">
              {ic('user', 22, '#94A3B8')}
              <span>โปรไฟล์</span>
            </div>
          </div>
        </div>

      </div>

    </div>
    '''
    return page_html_shell(title, content, width=2200, height=2200, bg="#F1F5F9")

# ---------------------------------------------------------------------------
# Flow Page Generator Helper
# ---------------------------------------------------------------------------
def build_flow_page(page_num, page_title, page_category, screens_meta, connections):
    """
    screens_meta: list of dicts:
      [
        {"id": "S01", "name": "Splash Screen", "desc": "หน้าแรกเปิดแอป แสดงอัตลักษณ์ ไทยศึกษา & MHESI", "builder": flow.s01_splash},
        ...
      ]
    """
    num_screens = len(screens_meta)
    col_w = 440
    col_gap = 140
    pad_x = 100
    pad_y = 150
    
    total_w = pad_x * 2 + num_screens * col_w + (num_screens - 1) * col_gap
    total_h = pad_y * 2 + 956 + 100 # ample vertical room

    screen_positions = {}
    screens_html = ""

    for i, meta in enumerate(screens_meta):
        s_id = meta["id"]
        s_name = meta["name"]
        s_desc = meta["desc"]
        builder_fn = meta["builder"]

        x = pad_x + i * (col_w + col_gap)
        y = pad_y

        screen_positions[s_id] = (x, y)

        # Header card above the screen
        header_card = f'''
        <div class="screen-header-card" style="left:{x}px;top:{y - 95}px;">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:4px;">
            <div style="font:700 17px 'Inter','IBM Plex Sans Thai';color:#101C36;">{s_id} — {s_name}</div>
            <span class="component-badge badge-instance">◇ Instance (ตัวลูก)</span>
          </div>
          <div style="font:400 12px 'IBM Plex Sans Thai';color:#64748B;">{s_desc} • iPhone 16 Pro Max</div>
        </div>
        '''

        raw_scr = builder_fn()
        positioned_scr = inject_screen_pos(raw_scr, s_id, x, y)

        screens_html += header_card + "\n" + positioned_scr + "\n"

    # Render wires
    wires_svg = render_wires_svg(connections, screen_positions, total_w, total_h)

    banner = f'''
    <div style="position:absolute;left:{pad_x}px;top:40px;right:{pad_x}px;display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px solid #CBD5E1;padding-bottom:20px;">
      <div style="display:flex;align-items:center;gap:16px;">
        <div style="width:52px;height:52px;border-radius:14px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(0,0,0,0.06);">
          {img("thai_suksa_logo.png", "width:40px;height:40px;border-radius:10px;object-fit:cover;")}
        </div>
        <div>
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
            <span style="background:{C['navy']};color:{C['cyan']};padding:4px 10px;border-radius:6px;font:700 12px 'Inter';">PAGE {page_num:02d}</span>
            <span style="font:700 12px 'Inter';color:{C['blue']};">ไทยศึกษา • {page_category}</span>
          </div>
          <div style="font:800 28px 'IBM Plex Sans Thai','Inter';color:#101C36;">{page_title}</div>
        </div>
      </div>
      <div style="display:flex;gap:12px;align-items:center;">
        <span class="component-badge badge-instance">◇ All Screens are Instances (ตัวลูก)</span>
        <div style="background:#FFFFFF;border:1px solid #CBD5E1;padding:6px 14px;border-radius:20px;font:600 12px 'Inter';color:#64748B;">
          {num_screens} Screens Flow
        </div>
      </div>
    </div>
    '''

    full_content = banner + "\n" + screens_html + "\n" + wires_svg
    return page_html_shell(f"Page {page_num:02d} — {page_title}", full_content, width=total_w, height=total_h, bg="#DDE3EE")

# ---------------------------------------------------------------------------
# Flow Pages Definitions (02 to 08)
# ---------------------------------------------------------------------------

def build_page_02():
    title = "Central Onboarding & Multi-University SSO Flow"
    category = "AUTHENTICATION & IDENTITY"
    screens = [
        {"id": "S01", "name": "Splash Screen", "desc": "หน้าแรกเปิดแอป แสดงอัตลักษณ์ ไทยศึกษา & MHESI", "builder": flow.s01_splash},
        {"id": "S02", "name": "Welcome Onboarding", "desc": "แนะนำระบบสารสนเทศกลางและโครงการของกระทรวง อว.", "builder": flow.s02_welcome},
        {"id": "S03", "name": "Select University", "desc": "เลือกสถาบันการศึกษาจาก 65+ มหาวิทยาลัยทั่วประเทศ", "builder": flow.s03_select_university},
        {"id": "S04", "name": "Central SSO Login", "desc": "เข้าสู่ระบบกลางด้วยบัญชีสถาบันและตัวสลับมหาลัย", "builder": flow.s04_login},
        {"id": "S05", "name": "New Registration", "desc": "ลงทะเบียนนักศึกษาใหม่และยืนยันข้อมูลบัตรประชาชน", "builder": flow.s05_registration},
        {"id": "S06", "name": "Forgot Password & OTP", "desc": "กู้คืนรหัสผ่านด้วย SMS OTP และอีเมลสถาบัน", "builder": flow.s06_forgot_password},
    ]
    connections = [
        ("S01", "S02", "On Load / Auto Transition", "right", "left"),
        ("S02", "S03", "Get Started -> เลือกมหาวิทยาลัย", "right", "left"),
        ("S03", "S04", "เลือกศิลปากร -> เข้าสู่ระบบ", "right", "left"),
        ("S04", "S05", "คลิกลงทะเบียนใหม่", "bottom", "bottom"),
        ("S05", "S04", "ยืนยันข้อมูล -> กลับมาเข้าสู่ระบบ", "bottom", "bottom"),
        ("S04", "S06", "คลิกลืมรหัสผ่าน", "bottom", "bottom"),
        ("S06", "S04", "ตั้งรหัสใหม่ -> กลับมาเข้าสู่ระบบ", "bottom", "bottom"),
    ]
    return build_flow_page(2, title, category, screens, connections)

def build_page_03():
    title = "Main Dashboard, Navigation & Student Identity"
    category = "CORE HUB & PROFILE"
    screens = [
        {"id": "S07", "name": "Home Dashboard", "desc": "แดชบอร์ดหลัก วิดเจ็ตกระเป๋า Camplus และทางลัด", "builder": flow.s07_home},
        {"id": "S08", "name": "Hamburger Menu Drawer", "desc": "เมนูแบบแฮมเบอร์เกอร์ รวมลิงก์ทุกบริการในแอป", "builder": flow.s08_hamburger_drawer},
        {"id": "S09", "name": "Notifications Center", "desc": "ศูนย์แจ้งเตือนคลาสเรียน สวัสดิการ และข่าวประกาศ", "builder": flow.s09_notifications},
        {"id": "S10", "name": "Student Profile", "desc": "ข้อมูลนักศึกษา นายธนพล กิจบำรุง 670610452", "builder": flow.s10_profile},
        {"id": "S11", "name": "Digital Student ID", "desc": "บัตรนักศึกษาดิจิทัลทางการ พร้อม Dynamic Barcode/QR", "builder": flow.s11_digital_id},
    ]
    connections = [
        ("S07", "S08", "กดปุ่มแฮมเบอร์เกอร์ -> เปิด Drawer", "right", "left"),
        ("S08", "S07", "กดปิด / แตะพื้นที่นอก -> กลับ Dashboard", "left", "right"),
        ("S07", "S09", "กดไอคอนกระดิ่ง -> เปิดการแจ้งเตือน", "bottom", "bottom"),
        ("S07", "S10", "แตะรูปโปรไฟล์ -> ดูโปรไฟล์นักศึกษา", "bottom", "bottom"),
        ("S10", "S11", "แตะการ์ดบัตร -> ขยายเต็มจอ Digital ID", "right", "left"),
    ]
    return build_flow_page(3, title, category, screens, connections)

def build_page_04():
    title = "Academic Life, Timetable & Schedule"
    category = "ACADEMIC SERVICES"
    screens = [
        {"id": "S12", "name": "Weekly Timetable", "desc": "ตารางเรียนรายสัปดาห์ แสดงห้องเรียนและหน่วยกิต", "builder": flow.s12_schedule},
        {"id": "S13", "name": "Class Details Sheet", "desc": "รายละเอียดวิชา แผนการสอน และปุ่มนำทางไปห้อง", "builder": flow.s13_class_details},
        {"id": "S14", "name": "Exam Schedule", "desc": "ตารางสอบกลางภาคและปลายภาค พร้อมเลขที่นั่งสอบ", "builder": flow.s14_exam_schedule},
        {"id": "S15", "name": "Academic Calendar", "desc": "ปฏิทินการศึกษาและเครื่องมือบันทึกกิจกรรมส่วนตัว", "builder": flow.s15_calendar},
    ]
    connections = [
        ("S12", "S13", "คลิกการ์ดวิชา -> เปิด Bottom Sheet", "right", "left"),
        ("S12", "S14", "สลับแท็บ -> ตารางสอบกลางภาค/ปลายภาค", "bottom", "bottom"),
        ("S14", "S12", "สลับแท็บ -> กลับตารางเรียน", "bottom", "bottom"),
        ("S12", "S15", "สลับแท็บ -> ปฏิทินการศึกษา", "bottom", "bottom"),
    ]
    return build_flow_page(4, title, category, screens, connections)

def build_page_05():
    title = "Campus News, Community & Event Tickets"
    category = "COMMUNITY & ACTIVITIES"
    screens = [
        {"id": "S16", "name": "News Feed", "desc": "ข่าวสารกลางจากกระทรวง อว. และ มหาวิทยาลัย", "builder": flow.s16_news_feed},
        {"id": "S17", "name": "News Article Details", "desc": "เนื้อหาข่าวฉบับเต็ม ลิงก์แนบ และแกลเลอรีภาพ", "builder": flow.s17_news_details},
        {"id": "S18", "name": "Activities & Clubs", "desc": "รวมกิจกรรม ชมรมนักศึกษา และการสะสมชั่วโมงกิจกรรม", "builder": flow.s18_activities},
        {"id": "S19", "name": "Activity Details", "desc": "รายละเอียดกิจกรรม กำหนดการ และโควตาที่เปิดรับ", "builder": flow.s19_activity_details},
        {"id": "S20", "name": "Registration Confirm", "desc": "Modal ยืนยันการลงทะเบียน พร้อมรับ QR Code ตั๋วเข้างาน", "builder": flow.s20_registration_confirm},
    ]
    connections = [
        ("S16", "S17", "คลิกการ์ดข่าว -> อ่านเนื้อหาเต็ม", "right", "left"),
        ("S18", "S19", "คลิกการ์ดกิจกรรม -> ดูเงื่อนไข", "right", "left"),
        ("S19", "S20", "กดลงทะเบียน -> Modal สำเร็จ & QR", "right", "left"),
        ("S20", "S18", "เสร็จสิ้น -> บันทึกประวัติและกลับหน้ารวม", "bottom", "bottom"),
    ]
    return build_flow_page(5, title, category, screens, connections)

def build_page_06():
    title = "Smart Campus Map & Live EV Shuttle Transit"
    category = "MAP & MOBILITY"
    screens = [
        {"id": "S21", "name": "Interactive Campus Map", "desc": "แผนที่มหาวิทยาลัย ตัวกรองตึก อาคาร และสิ่งอำนวยความสะดวก", "builder": flow.s21_campus_map},
        {"id": "S22", "name": "Building Details", "desc": "ข้อมูลอาคาร ชั้น ห้องเรียน และลิฟต์สำหรับผู้พิการ", "builder": flow.s22_place_details},
        {"id": "S23", "name": "Directions & Routing", "desc": "ระบบนำทางเดินเท้า ปั่นจักรยาน พร้อมระยะทางและเวลา", "builder": flow.s23_directions},
        {"id": "S24", "name": "Smart EV Shuttle Tracker", "desc": "ระบบติดตามรถรางไฟฟ้าอัจฉริยะแบบ Real-Time GPS", "builder": flow.s24_smart_transit},
    ]
    connections = [
        ("S21", "S22", "แตะหมุดอาคาร -> ดูรายละเอียด", "right", "left"),
        ("S22", "S23", "กดปุ่มนำทาง -> เปิดแผนที่เส้นทาง", "right", "left"),
        ("S21", "S24", "แตะปุ่มรถราง -> เปิดแทร็กเกอร์ EV GPS", "bottom", "bottom"),
        ("S24", "S21", "ปิดแทร็กเกอร์ -> กลับแผนที่หลัก", "bottom", "bottom"),
    ]
    return build_flow_page(6, title, category, screens, connections)

def build_page_07():
    title = "Smart Facility Booking, Fleet Rental & e-Services"
    category = "SMART SPACE & STUDENT SERVICES"
    screens = [
        {"id": "S25", "name": "Space & Room Booking", "desc": "จองห้องศึกษาเดี่ยว/กลุ่ม Co-working Space หอสมุด", "builder": flow.s25_room_booking},
        {"id": "S26", "name": "Booking Pass & QR", "desc": "บัตรผ่านเข้าห้องอัจฉริยะ ปปลดล็อกด้วย Smart QR Code", "builder": flow.s26_booking_confirm},
        {"id": "S27", "name": "Fleet & Equipment Rental", "desc": "ยืมจักรยาน Smart EV, iPads แล็บ และรถตู้สถาบัน", "builder": flow.s27_fleet_rental},
        {"id": "S28", "name": "Student e-Services", "desc": "ศูนย์ยื่นคำร้องออนไลน์ ใบรับรอง และบริการการศึกษา", "builder": flow.s28_student_services},
    ]
    connections = [
        ("S25", "S26", "เลือกช่วงเวลา & ยืนยัน -> รับ QR Smart Pass", "right", "left"),
        ("S26", "S25", "เสร็จสิ้น -> บันทึกประวัติการจอง", "bottom", "bottom"),
        ("S27", "S26", "สแกนยืมอุปกรณ์ -> รับ QR ปลดล็อก", "left", "right"),
        ("S28", "S25", "ยื่นคำร้องขอใช้พื้นที่ -> ระบบจอง", "bottom", "bottom"),
    ]
    return build_flow_page(7, title, category, screens, connections)

def build_page_08():
    title = "Welfare, Finance, Student Loan & Campus Living Hub"
    category = "WELFARE, TUITION & LIVING"
    screens = [
        {"id": "S29", "name": "Camplus Wallet Hub", "desc": "กระเป๋าเงินสวัสดิการ ฿3,000/เดือน และยอดเงินส่วนตัว", "builder": flow.s29_wallet},
        {"id": "S30", "name": "Scan to Pay & Food Pay", "desc": "สแกน QR จ่ายเงินโรงอาหาร พร้อมเลือกกระเป๋า Camplus หรือ พร้อมเพย์", "builder": flow.s30_scan_pay},
        {"id": "S31", "name": "Official Digital e-Slip", "desc": "สลิปและใบเสร็จดิจิทัลทางการ ตรวจสอบย้อนหลังได้", "builder": flow.s31_payment_slip},
        {"id": "S32", "name": "Tuition Fee Payment", "desc": "ชำระค่าลงทะเบียน 18,500 ฿ พร้อมเพย์ & ดาวน์โหลดใบเสร็จ", "builder": flow.s32_tuition_pay},
        {"id": "S33", "name": "Student Loan e-Portal", "desc": "ระบบกองทุนเงินกู้ยืม กยศ. ดิจิทัล & ติดตามค่าครองชีพ", "builder": flow.s33_student_loan},
        {"id": "S34", "name": "Volunteer Hours Tracker", "desc": "สะสมชั่วโมงจิตอาสา 36/36 ชม. & ขอ e-Certificate อว.", "builder": flow.s34_volunteer_hours},
        {"id": "S35", "name": "Dormitory Life & Utility Pay", "desc": "หอพักทับแก้ว 3 ห้อง 412 & บิลค่าน้ำค่าไฟ 3,186 ฿", "builder": flow.s35_dormitory},
    ]
    connections = [
        ("S29", "S30", "กดปุ่มสแกนจ่าย QR หรือระบุยอดเงิน", "right", "left"),
        ("S30", "S31", "เลือกกระเป๋า Camplus -> ยืนยันชำระเงิน -> รับสลิป", "right", "left"),
        ("S31", "S29", "เสร็จสิ้น -> อัปเดตยอดเงินคงเหลือในกระเป๋า", "bottom", "bottom"),
        ("S32", "S31", "ชำระค่าเทอมสำเร็จ -> ออกใบเสร็จดิจิทัล", "left", "right"),
        ("S32", "S33", "นักศึกษากู้ยืม -> เช็กสิทธิ กยศ.", "right", "left"),
        ("S33", "S34", "ตรวจเกณฑ์ กยศ. -> ตรวจชั่วโมงจิตอาสา", "right", "left"),
        ("S35", "S30", "กดชำระค่าน้ำไฟ -> สแกนจ่าย", "left", "right"),
    ]
    return build_flow_page(8, title, category, screens, connections)

def build_page_09():
    title = "Community Forum, Discord Matrix & AI Campus Copilot"
    category = "COMMUNITY & AI COPILOT"
    screens = [
        {"id": "S36", "name": "Community Forum", "desc": "กระดานสนทนานักศึกษา ถามตอบ ติวสอบ และรีวิวชีวิตในมอ", "builder": flow.s36_community},
        {"id": "S37", "name": "Discord Matrix Lounge", "desc": "ห้องแชต & สนทนาเสียงแยกคณะ/สาขา/รวมมหาลัยทั่วประเทศ", "builder": flow.s37_discord_matrix},
        {"id": "S38", "name": "AI Campus Copilot", "desc": "ผู้ช่วยปัญญาประดิษฐ์ตอบคำถาม ค้นหาห้องเรียน และพยากรณ์เกรด", "builder": flow.s38_ai_assistant},
    ]
    connections = [
        ("S36", "S37", "เปิดห้องสนทนาเสียง Discord Lounge", "right", "left"),
        ("S37", "S36", "ออกจากห้องเสียง -> กลับบอร์ดชุมชน", "left", "right"),
        ("S38", "S36", "AI แนะนำกระทู้ติวที่น่าสนใจ", "left", "right"),
    ]
    return build_flow_page(9, title, category, screens, connections)

# ---------------------------------------------------------------------------
# Build Page 10: Master Board (Consolidated Overview S01-S38)
# ---------------------------------------------------------------------------
def build_page_10():
    """Outputs the complete 38-screen master flow board with the verified layout."""
    flow_file = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
    if os.path.exists(flow_file):
        with open(flow_file, "r", encoding="utf-8") as f:
            return f.read()
    else:
        flow.generate_board()
        with open(flow_file, "r", encoding="utf-8") as f:
            return f.read()

# ---------------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("THAI SUKSA (ไทยศึกษา) ENTERPRISE MULTI-PAGE FIGMA BUILDER")
    print("=" * 60)

    pages = [
        ("00_Cover_Specs.html", build_page_00),
        ("01_Design_System_Master.html", build_page_01),
        ("02_Page_Auth_Flow.html", build_page_02),
        ("03_Page_Home_Profile.html", build_page_03),
        ("04_Page_Academic_Schedule.html", build_page_04),
        ("05_Page_News_Activities.html", build_page_05),
        ("06_Page_Map_Transit.html", build_page_06),
        ("07_Page_Booking_Fleet_Services.html", build_page_07),
        ("08_Page_Welfare_Living.html", build_page_08),
        ("09_Page_Community_AI.html", build_page_09),
        ("10_Page_Master_Board.html", build_page_10),
    ]

    for fname, func in pages:
        out_path = os.path.join(OUT_DIR, fname)
        print(f"Generating {fname}...")
        html = func()
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f" -> Saved {fname} ({len(html):,} bytes)")

    print("=" * 60)
    print("ALL 11 FIGMA PAGES GENERATED SUCCESSFULLY!")
    print(f"Output folder: {OUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
