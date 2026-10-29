"""Generate interactive iPhone 16 Pro Max device simulator."""
import os
import re
from kit import C, USER, CSS, ICONS, ic, img, avatar, sb, hi, bar, nav, uni, badge, btn, field, labeled, screen_bg_hint, qr_svg
import generate_thai_suksa_flow as flow

HERE = os.path.dirname(os.path.abspath(__file__))

def generate_simulator():
    screens_dict = {}
    screens_rendered = ""
    screen_options = ""

    for s_id, title, func, r, c, sec in flow.SCREENS:
        content = func()
        # Preserve existing inline styles (background, color, etc.) and attributes (data-go) while adapting for simulator
        m = re.search(r'<div\s+([^>]*class=[\'"]scr[\'"][^>]*)>', content)
        if m:
            attrs = m.group(1)
            style_m = re.search(r'style=[\'"]([^\'"]*)[\'"]', attrs)
            orig_style = style_m.group(1).strip() if style_m else ""
            if orig_style and not orig_style.endswith(';'):
                orig_style += ';'
            attrs_clean = re.sub(r'style=[\'"][^\'"]*[\'\"]', '', attrs).strip()
            attrs_clean = re.sub(r'id=[\'"][^\'"]*[\'\"]', '', attrs_clean).strip()
            clean_style = re.sub(r'(?:min-)?height\s*:[^;]+;?', '', orig_style).strip()
            clean_style = re.sub(r'overflow\s*:[^;]+;?', '', clean_style).strip()
            clean_style = re.sub(r'display\s*:[^;]+;?', '', clean_style).strip()
            clean_style = re.sub(r'flex-direction\s*:[^;]+;?', '', clean_style).strip()
            sim_style = f"position:relative;width:100%;height:100%;display:none;flex-direction:column;overflow:hidden;{clean_style}"
            new_tag = f'<div id="sim_{s_id}" {attrs_clean} style="{sim_style}">'
            new_tag = re.sub(r'\s+', ' ', new_tag)
            content_clean = content[:m.start()] + new_tag + content[m.end():]
        else:
            content_clean = content
        screens_rendered += f"\n<!-- Screen {s_id}: {title} -->\n" + content_clean
        screen_options += f'<option value="{s_id}">{s_id} - {title}</option>\n'

    html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ไทยศึกษา (THAI SUKSA) — Interactive Mobile Device Simulator (iPhone 16 Pro Max)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {CSS}
    body {{
      background: linear-gradient(135deg, #0B132B 0%, #101C36 50%, #1C2D4F 100%);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 30px 20px;
      margin: 0;
      color: #fff;
    }}
    .sim-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 600px;
      margin-bottom: 20px;
      gap: 16px;
    }}
    .sim-title {{
      font-weight: 800;
      font-size: 22px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .sim-select {{
      background: rgba(255, 255, 255, 0.12);
      color: #fff;
      border: 1.5px solid rgba(88, 214, 255, 0.4);
      padding: 8px 14px;
      border-radius: 20px;
      font: 600 13px 'IBM Plex Sans Thai', 'Inter';
      outline: none;
      cursor: pointer;
    }}
    .sim-select option {{
      background: #101C36;
      color: #fff;
    }}
    /* iPhone 16 Pro Max Titanium Body Mockup */
    .iphone-case {{
      width: 468px;
      height: 984px;
      border-radius: 56px;
      background: #0B0E14;
      padding: 14px;
      box-sizing: border-box;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.6), 0 0 0 3px #2A364F, 0 0 0 6px #151D2C;
      position: relative;
      display: flex;
      flex-direction: column;
    }}
    .iphone-screen {{
      width: 440px;
      height: 956px;
      border-radius: 44px;
      overflow: hidden;
      background: #F5F7FB;
      position: relative;
      flex: none;
    }}
    .sim-controls {{
      margin-top: 20px;
      display: flex;
      align-items: center;
      gap: 14px;
      font-size: 13px;
      color: #94A3B8;
    }}
    .sim-btn {{
      background: rgba(255,255,255,0.1);
      border: 1px solid rgba(255,255,255,0.2);
      color: #fff;
      padding: 6px 14px;
      border-radius: 14px;
      cursor: pointer;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .sim-btn:hover {{
      background: #246BFD;
      border-color: #246BFD;
    }}
    [data-go] {{
      cursor: pointer;
    }}
    [data-go]:active {{
      opacity: 0.7;
    }}
  </style>
</head>
<body>

  <div class="sim-header">
    <div class="sim-title">
      <span style="color:{C['cyan']};">✦</span>
      <span>ไทยศึกษา Mobile Simulator</span>
    </div>
    <select id="screenSelect" class="sim-select" onchange="navigateTo(this.value, false)">
      {screen_options}
    </select>
  </div>

  <!-- iPhone 16 Pro Max Device -->
  <div class="iphone-case">
    <div class="iphone-screen">
      {screens_rendered}
    </div>
  </div>

  <div class="sim-controls">
    <button class="sim-btn" onclick="goBack()">← ย้อนกลับ (Back)</button>
    <button class="sim-btn" onclick="navigateTo('S07')">🏠 หน้าหลัก (Home)</button>
    <button class="sim-btn" onclick="navigateTo('S01')">🔄 เริ่มใหม่ (Restart)</button>
    <span>| คลิกทุกปุ่มบนหน้าจอเพื่อทดสอบการนำทางจริง</span>
  </div>

  <script>
    var currentScreen = 'S01';
    var navHistory = ['S01'];

    function showScreen(screenId) {{
      // hide all screens
      var all = document.querySelectorAll('.iphone-screen .scr');
      all.forEach(function(el) {{
        el.style.display = 'none';
      }});

      // show target screen
      var target = document.getElementById('sim_' + screenId);
      if (target) {{
        target.style.display = 'flex';
        currentScreen = screenId;
        document.getElementById('screenSelect').value = screenId;
      }}
    }}

    function navigateTo(screenId, pushHistory) {{
      if (pushHistory === undefined) pushHistory = true;
      if (pushHistory && currentScreen !== screenId) {{
        navHistory.push(screenId);
      }}
      showScreen(screenId);
    }}

    function goBack() {{
      if (navHistory.length > 1) {{
        navHistory.pop();
        var prev = navHistory[navHistory.length - 1];
        showScreen(prev);
      }} else {{
        navigateTo('S07');
      }}
    }}

    // Global click listener for interactive data-go elements
    
    
    // University selection, expand toggle & live search
    var isS03Expanded = false;
    function toggleS03Expand() {{
      var scr = document.getElementById('S03') || document.getElementById('scr_S03') || document.getElementById('sim_S03');
      var bodyEl = document.getElementById('uni_scroll_body');
      if (!scr) return;
      isS03Expanded = !isS03Expanded;
      if (isS03Expanded) {{
        scr.style.height = '5200px';
        scr.style.minHeight = '5200px';
        if (bodyEl) bodyEl.style.overflow = 'visible';
      }} else {{
        scr.style.height = '956px';
        scr.style.minHeight = '956px';
        if (bodyEl) bodyEl.style.overflow = 'auto';
      }}
    }}

    document.addEventListener('DOMContentLoaded', function() {{
      var selectedSlug = 'silpakorn';
      var selectedAbbr = 'SU';
      var selectedTh = 'มหาวิทยาลัยศิลปากร';
      var selectedCampus = 'วิทยาเขตพระราชวังสนามจันทร์ / วังท่าพระ';

      document.body.addEventListener('click', function(e) {{
        var card = e.target.closest('.uni-card');
        if (card) {{
          document.querySelectorAll('.uni-card').forEach(function(c) {{
            c.style.border = '1px solid #E5EAF2';
            c.style.background = '#fff';
            var chk = c.querySelector('.uni-chk');
            if (chk) chk.innerHTML = '<div style="width:20px;height:20px;border-radius:50%;border:2px solid #CBD5E1;"></div>';
          }});
          card.style.border = '2px solid #246BFD';
          card.style.background = '#F8FAFF';
          var activeChk = card.querySelector('.uni-chk');
          if (activeChk) {{
            activeChk.innerHTML = '<div style="width:22px;height:22px;border-radius:50%;background:#246BFD;color:#fff;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>';
          }}

          selectedSlug = card.getAttribute('data-slug');
          selectedAbbr = card.getAttribute('data-abbr');
          selectedTh = card.getAttribute('data-th');
          selectedCampus = card.getAttribute('data-campus');

          var labelEl = document.getElementById('uni_selected_label');
          if (labelEl) labelEl.innerText = selectedTh + ' (' + selectedAbbr + ')';
          var btnText = document.getElementById('uni_btn_text');
          if (btnText) btnText.innerText = 'ยืนยันและดำเนินการต่อ (Continue with ' + selectedAbbr + ')';

          // Update S04 Login Pill
          var pName = document.getElementById('login_uni_name');
          if (pName) pName.innerText = selectedTh;
          var pCampus = document.getElementById('login_uni_campus');
          if (pCampus) pCampus.innerText = selectedCampus;
          var pSeal = document.getElementById('login_uni_seal');
          var cardImg = card.querySelector('img, .tile');
          if (pSeal && cardImg) pSeal.innerHTML = cardImg.outerHTML;
          
          // Update S04B SSO Screen
          var ssoTitle = document.getElementById('sso_uni_title');
          if (ssoTitle) ssoTitle.innerText = selectedAbbr + '-NET';
          var ssoSeal = document.getElementById('sso_uni_seal');
          if (ssoSeal && cardImg) ssoSeal.innerHTML = cardImg.outerHTML;
          var ssoFooterTh = document.getElementById('sso_footer_th');
          if (ssoFooterTh) ssoFooterTh.innerText = 'สำนักดิจิทัลเทคโนโลยี ' + selectedTh;
          var ssoFooterEn = document.getElementById('sso_footer_en');
          if (ssoFooterEn) ssoFooterEn.innerText = 'Bureau of Digital Technology, ' + (card.getAttribute('data-en') || selectedTh);
          var ssoBtnText = document.getElementById('login_sso_btn_text');
          if (ssoBtnText) ssoBtnText.innerText = 'เข้าใช้งานด้วย ' + selectedAbbr + '-NET SSO (Single Sign-On)';
          return;
        }}

        var chip = e.target.closest('.uni-chip');
        if (chip) {{
          document.querySelectorAll('.uni-chip').forEach(function(ch) {{ ch.classList.remove('on'); }});
          chip.classList.add('on');
          var cat = chip.getAttribute('data-filter');
          document.querySelectorAll('.uni-card').forEach(function(c) {{
            if (cat === 'all' || c.getAttribute('data-cat') === cat) {{
              c.style.display = 'flex';
            }} else {{
              c.style.display = 'none';
            }}
          }});
          document.querySelectorAll('.uni-sec-header').forEach(function(sh) {{
            var sc = sh.getAttribute('data-sec-cat');
            if (cat === 'all' || sc === cat) {{
              sh.style.display = 'flex';
            }} else {{
              sh.style.display = 'none';
            }}
          }});
          document.querySelectorAll('.uni-sec-group').forEach(function(sg) {{
            var sc = sg.getAttribute('data-sec-cat');
            if (cat === 'all' || sc === cat) {{
              sg.style.display = 'block';
            }} else {{
              sg.style.display = 'none';
            }}
          }});
        }}
      }});

      var sInp = document.getElementById('uni_search_input');
      if (sInp) {{
        sInp.addEventListener('input', function(e) {{
          var q = e.target.value.toLowerCase().trim();
          var count = 0;
          document.querySelectorAll('.uni-card').forEach(function(c) {{
            var th = (c.getAttribute('data-th') || '').toLowerCase();
            var en = (c.getAttribute('data-en') || '').toLowerCase();
            var ab = (c.getAttribute('data-abbr') || '').toLowerCase();
            var cp = (c.getAttribute('data-campus') || '').toLowerCase();
            if (!q || th.indexOf(q) !== -1 || en.indexOf(q) !== -1 || ab.indexOf(q) !== -1 || cp.indexOf(q) !== -1) {{
              c.style.display = 'flex';
              count++;
            }} else {{
              c.style.display = 'none';
            }}
          }});
          var bd = document.getElementById('uni_count_badge');
          if (bd) bd.innerText = count + ' แห่ง';
        }});
      }}
    }});

    document.addEventListener('DOMContentLoaded', function() {{
      showScreen('S01');

      document.body.addEventListener('click', function(e) {{
        var socialConnectBtn = e.target.closest('#sim_S05B .card button');
        if (socialConnectBtn) {{
          socialConnectBtn.outerHTML = '<span class="badge b-blue" style="font-size:10px;padding:3px 8px;">เชื่อมต่อแล้ว</span>';
          return;
        }}

        var ssoSubmit = e.target.closest('#sso_submit_btn');
        if (ssoSubmit) {{
          if (navHistory.indexOf('S03') !== -1 || navHistory.indexOf('S05') !== -1) {{
            navigateTo('S05B', true);
          }} else {{
            navigateTo('S07', true);
          }}
          return;
        }}

        var btnGo = e.target.closest('[data-go]');
        if (btnGo) {{
          var dest = btnGo.getAttribute('data-go');
          if (dest) {{
            navigateTo(dest, true);
          }}
          return;
        }}

        var btnBack = e.target.closest('.ib[data-back="1"]');
        if (btnBack) {{
          goBack();
          return;
        }}
      }});
    }});
  </script>
</body>
</html>
'''

    out_path = os.path.join(HERE, "ไทยศึกษา.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated device simulator: {out_path} ({len(html)} bytes)")

    

if __name__ == "__main__":
    generate_simulator()
