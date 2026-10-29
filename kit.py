"""Common building blocks (CSS, icons, status bar, nav...) for the THAI SUKSA (ไทยศึกษา) flow board."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 440, 956  # iPhone 16 Pro Max

C = dict(blue="#246BFD", navy="#101C36", cyan="#58D6FF", green="#16A675",
         amber="#E9A23B", red="#DC4545", bg="#F5F7FB", line="#E5EAF2", sub="#64748B")

USER = dict(
    app_name="ไทยศึกษา", app_name_en="THAI SUKSA",
    th="ธนพล กิจบำรุง", th_full="นายธนพล กิจบำรุง", en="Thanapol Kitbumrung",
    sid="670610452", fac="คณะศึกษาศาสตร์", major="สาขาวิชาเทคโนโลยีการศึกษา",
    uni="มหาวิทยาลัยศิลปากร", uni_en="Silpakorn University", uni_s="ม.ศิลปากร",
    email="kitbumrung_t@silpakorn.edu", year="ชั้นปีที่ 3",
    campus="วิทยาเขตพระราชวังสนามจันทร์",
)

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#DDE3EE;font-family:'IBM Plex Sans Thai','Inter',sans-serif;color:#101C36}
#board{position:relative;background:#DDE3EE}
.scr{position:absolute;width:440px;height:956px;overflow:hidden;background:#F5F7FB;display:flex;flex-direction:column;font-family:'IBM Plex Sans Thai','Inter',sans-serif;color:#101C36;box-shadow:0 20px 50px rgba(16,28,54,.18);z-index:20}
.lbl{position:absolute;font:600 18px 'Inter','IBM Plex Sans Thai';color:#101C36;white-space:nowrap;z-index:25}
.lbl small{font-weight:500;font-size:14px;color:#64748B;margin-left:8px}
.rowtitle{position:absolute;font:700 28px 'IBM Plex Sans Thai','Inter';color:#101C36;white-space:nowrap;z-index:25}
.sb{width:100% !important;box-sizing:border-box;height:54px;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 32px 0 36px;position:relative;font:600 16px 'Inter';z-index:40}
.island{position:absolute;left:50%;transform:translateX(-50%);top:11px;width:126px;height:37px;border-radius:20px;background:#000;z-index:45;pointer-events:none}
.hi{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:140px;height:5px;border-radius:3px;z-index:45;pointer-events:none}
.bar{height:60px;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 20px;gap:12px}
.ib{width:44px;height:44px;flex:none;border-radius:14px;background:#fff;border:1px solid #E5EAF2;display:flex;align-items:center;justify-content:center;position:relative}
.ttl{font-size:18px;font-weight:600;text-align:center;flex:1}
.body{flex:1;padding:4px 20px 0;display:flex;flex-direction:column;gap:14px;overflow-y:auto;overflow-x:hidden}
.h1{font-size:26px;font-weight:700;line-height:1.3}
.h2{font-size:20px;font-weight:600;line-height:1.35}
.h3{font-size:16px;font-weight:600;line-height:1.4}
.p{font-size:14px;line-height:1.6;color:#64748B}
.cap{font-size:12px;color:#64748B;line-height:1.5}
.btn{height:52px;flex:none;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:8px;font-size:15px;font-weight:600;padding:0 18px;white-space:nowrap}
.bp{background:#246BFD;color:#fff}
.bn{background:#101C36;color:#fff}
.bs{background:#fff;color:#101C36;border:1px solid #E5EAF2}
.bt{background:#EAF1FF;color:#246BFD}
.bd{background:#DC4545;color:#fff}
.bo{background:#fff;color:#DC4545;border:1px solid #F5C2C2}
.card{background:#fff;border:1px solid #E5EAF2;border-radius:16px;padding:16px;flex:none}
.chips{display:flex;gap:8px;overflow:hidden;flex:none}
.chip{height:36px;flex:none;padding:0 14px;border-radius:18px;display:flex;align-items:center;gap:6px;font-size:13px;font-weight:500;border:1px solid #E5EAF2;background:#fff;color:#64748B;white-space:nowrap}
.chip.on{background:#101C36;color:#fff;border-color:#101C36}
.badge{display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 10px;border-radius:12px;font-size:12px;font-weight:600;white-space:nowrap;flex:none}
.b-blue{background:#EAF1FF;color:#246BFD}.b-green{background:#E3F6EF;color:#0F7F59}.b-amber{background:#FDF1DF;color:#A86A12}.b-red{background:#FBE5E5;color:#B42F2F}.b-grey{background:#EEF1F6;color:#475569}.b-navy{background:#101C36;color:#fff}
.field{height:52px;flex:none;border-radius:12px;background:#fff;border:1px solid #E5EAF2;display:flex;align-items:center;gap:10px;padding:0 14px;font-size:15px;color:#101C36}
.field.ph{color:#94A3B8}.field.focus{border:2px solid #246BFD;box-shadow:0 0 0 4px rgba(36,107,253,.12)}.field.err{border:2px solid #DC4545}.field.lock{background:#F1F4F9;color:#64748B}
.lab{font-size:13px;font-weight:600;margin-bottom:6px;display:flex;justify-content:space-between}
.row{display:flex;align-items:center}
.col{display:flex;flex-direction:column}
.sec{display:flex;justify-content:space-between;align-items:center;font-size:16px;font-weight:600;flex:none}
.link{color:#246BFD;font-size:13px;font-weight:600;white-space:nowrap}
.nav{position:absolute;left:0;right:0;bottom:0;height:92px;background:#fff;border-top:1px solid #E5EAF2;display:flex;justify-content:space-around;padding-top:10px}
.nav .it{width:72px;height:50px;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:11px;font-weight:500;color:#94A3B8}
.nav .it.on{color:#246BFD;font-weight:700}
.dim{position:absolute;left:0;top:0;width:440px;height:956px;background:rgba(16,28,54,.55)}
.sheet{position:absolute;left:0;right:0;bottom:0;background:#fff;border-radius:28px 28px 0 0;padding:10px 20px 40px;display:flex;flex-direction:column;gap:16px}
.handle{width:44px;height:5px;border-radius:3px;background:#D5DBE5;margin:0 auto}
.modal{position:absolute;left:28px;width:384px;background:#fff;border-radius:24px;padding:28px 24px 24px;display:flex;flex-direction:column;align-items:center;gap:14px;text-align:center}
.circle{border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}
.tile{border-radius:16px;display:flex;align-items:center;justify-content:center;flex:none}
.sep{height:1px;background:#E5EAF2;flex:none}
.li{display:flex;align-items:center;gap:12px;min-height:56px}
.grow{flex:1;min-width:0}
.seg{display:flex;background:#E9EDF4;border-radius:14px;padding:4px;flex:none}
.seg div{flex:1;height:40px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:600;color:#64748B}
.seg .on{background:#fff;color:#101C36;box-shadow:0 1px 3px rgba(16,28,54,.12)}
.tg{width:48px;height:28px;border-radius:14px;background:#CBD3DF;position:relative;flex:none}
.tg::after{content:'';position:absolute;left:3px;top:3px;width:22px;height:22px;border-radius:50%;background:#fff}
.tg.on{background:#246BFD}.tg.on::after{left:23px}
.shadow{box-shadow:0 10px 30px rgba(16,28,54,.10)}
"""

# --- icons (24x24 stroke) -------------------------------------------------
ICONS = {
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "calendar": '<rect x="3" y="4.5" width="18" height="17" rx="3"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/>',
    "star": '<path d="M12 2.8l2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/>',
    "bell": '<path d="M6 8.5a6 6 0 0 1 12 0c0 6.5 2.5 8.5 2.5 8.5h-17S6 15 6 8.5"/><path d="M10.2 20.5a2 2 0 0 0 3.6 0"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h11"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20.5 20.5-4.2-4.2"/>',
    "right": '<path d="m9 18 6-6-6-6"/>',
    "left": '<path d="m15 18-6-6 6-6"/>',
    "down": '<path d="m6 9 6 6 6-6"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "pin": '<path d="M12 21.5s-7.5-6.4-7.5-12.3a7.5 7.5 0 0 1 15 0c0 5.9-7.5 12.3-7.5 12.3z"/><circle cx="12" cy="9.2" r="2.6"/>',
    "bookmark": '<path d="M6.5 3.5h11v17.5l-5.5-3.8-5.5 3.8z"/>',
    "share": '<circle cx="18" cy="5" r="2.8"/><circle cx="6" cy="12" r="2.8"/><circle cx="18" cy="19" r="2.8"/><path d="m8.5 13.4 7 4.2M15.5 6.4l-7 4.2"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "layers": '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "paperclip": '<path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/>',
    "expand": '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>',
    "qr": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><path d="M14 14h3v3h-3zM18 18h3v3h-3zM14 20.5h2M20.5 14v2"/>',
    "settings": '<path d="M4 6.5h9M17 6.5h3M4 12h3M11 12h9M4 17.5h11M19 17.5h1"/><circle cx="15" cy="6.5" r="2"/><circle cx="9" cy="12" r="2"/><circle cx="17" cy="17.5" r="2"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.6 9.2a2.5 2.5 0 1 1 3.4 2.3c-.6.3-1 .9-1 1.6v.6"/><path d="M12 17.2h.01"/>',
    "logout": '<path d="M9 21H5.5A2.5 2.5 0 0 1 3 18.5v-13A2.5 2.5 0 0 1 5.5 3H9"/><path d="m16 17 5-5-5-5M21 12H9"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "bus": '<rect x="4" y="3" width="16" height="15" rx="3.5"/><path d="M4 11h16M8 21v-3M16 21v-3"/><circle cx="8" cy="14.5" r="1"/><circle cx="16" cy="14.5" r="1"/>',
    "door": '<path d="M3.5 21h17M6 21V4.5A1.5 1.5 0 0 1 7.5 3h9A1.5 1.5 0 0 1 18 4.5V21"/><circle cx="14.5" cy="12" r="1"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="4"/><path d="M12 8V4.5M9.5 4h5"/><circle cx="9" cy="14" r="1.3"/><circle cx="15" cy="14" r="1.3"/>',
    "file": '<path d="M14 3H6.5A2.5 2.5 0 0 0 4 5.5v13A2.5 2.5 0 0 0 6.5 21h11a2.5 2.5 0 0 0 2.5-2.5V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    "send": '<path d="M21.5 2.5 11 13"/><path d="M21.5 2.5 15 21.5l-4-8.5-8.5-4z"/>',
    "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7.5a4 4 0 0 1 8 0V11"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "nav": '<path d="M3 11 21 3l-8 18-2-8z"/>',
    "walk": '<circle cx="13" cy="4.5" r="2"/><path d="m9 21 2.5-6.5L14 17v4M8 12.5l2.5-4.5 3.5 1 2 3.5M10.5 8 7 9.5"/>',
    "filter": '<path d="M3 5h18l-7 8.5v5.5l-4 2v-7.5z"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
    "camera": '<path d="M4 7.5h3l2-3h6l2 3h3a1 1 0 0 1 1 1V19a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8.5a1 1 0 0 1 1-1z"/><circle cx="12" cy="13.5" r="3.8"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.6h.01"/>',
    "alert": '<path d="M12 3.5 2.5 20.5h19z"/><path d="M12 10v5M12 17.8h.01"/>',
    "building": '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2M10.5 21v-3h3v3"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14.2c2.2.6 3.5 2.8 3.5 5.8"/>',
    "grid": '<rect x="3" y="3" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="2"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="2"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="2"/>',
    "news": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M7 8.5h10M7 12h10M7 15.5h6"/>',
    "id": '<rect x="2.5" y="5" width="19" height="14" rx="2.5"/><circle cx="8.5" cy="11" r="2.3"/><path d="M5 16.3c.6-1.5 2-2.3 3.5-2.3s2.9.8 3.5 2.3M14.5 9.5h4.5M14.5 13h3.5"/>',
    "phone": '<path d="M5 3.5h3.5l2 5-2.5 1.6a11 11 0 0 0 5.9 5.9l1.6-2.5 5 2v3.5a2 2 0 0 1-2 2A17 17 0 0 1 3 5.5a2 2 0 0 1 2-2z"/>',
    "spark": '<path d="M12 3l1.9 4.9L19 9.8l-5.1 1.9L12 16.6l-1.9-4.9L5 9.8l5.1-1.9z"/><path d="M19 15.5l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>',
    "target": '<circle cx="12" cy="12" r="7.5"/><circle cx="12" cy="12" r="2.8"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22"/>',
    "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15.5H6.5A2.5 2.5 0 0 0 4 21z"/><path d="M4 21V5.5"/>',
    "swap": '<path d="M7 4 3 8l4 4M3 8h14M17 20l4-4-4-4M21 16H7"/>',
    "download": '<path d="M12 3.5v11.5M7 10l5 5 5-5M5 20.5h14"/>',
    "food": '<path d="M4 9h13v4.5A5.5 5.5 0 0 1 11.5 19h-2A5.5 5.5 0 0 1 4 13.5z"/><path d="M17 10.5h1.5a2.5 2.5 0 0 1 0 5H17M8 3.5v2.5M12 3.5v2.5"/>',
    "parking": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M9.5 17V7h3.5a3 3 0 0 1 0 6H9.5"/>',
    "shield": '<path d="M12 3 4.5 6v6c0 4.8 3.3 7.8 7.5 9 4.2-1.2 7.5-4.2 7.5-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "tv": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8"/>',
    "board": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M7 20l2-4M17 20l-2-4"/>',
    "plug": '<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0zM12 17v4"/>',
    "wifi": '<path d="M2 8.5a15 15 0 0 1 20 0M5 12a10 10 0 0 1 14 0M8.5 15.5a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1"/>',
    "lift": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="m9 9 2-2 2 2M9 15l2 2 2-2"/>',
    "access": '<circle cx="12" cy="4.5" r="2"/><path d="M8 9h8M12 9v5l-3 6M12 14l3 6"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 9"/>',
    "dots": '<circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="19" cy="12" r="1.3"/>',
    "refresh": '<path d="M20 11a8 8 0 1 0-2.3 5.7M20 4v7h-7"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "type": '<path d="M4 7V5h16v2M12 5v14M9 19h6"/>',
    "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h14a1 1 0 0 1 1 1v3M2 7v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2z"/><circle cx="17.5" cy="14" r="1.5"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/>',
    "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2M7 12h10"/>',
    "receipt": '<path d="M4 2v20l3-2 3 2 3-2 3 2 4-2V2l-4 2-3-2-3 2-3-2zM8 8h8M8 12h8M8 16h5"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18M7 6h2M7 10h2"/>',
    "gift": '<rect x="3" y="8" width="18" height="14" rx="2"/><path d="M12 8v14M3 13h18M12 8c-2.5 0-4-2-4-3.5a2.5 2.5 0 0 1 5 0V8zM12 8c2.5 0 4-2 4-3.5a2.5 2.5 0 0 0-5 0V8z"/>',
    "discord": '<path d="M18.5 5.5A15.5 15.5 0 0 0 14.5 4a12 12 0 0 0-.6 1.3 14.5 14.5 0 0 0-3.8 0A12 12 0 0 0 9.5 4 15.5 15.5 0 0 0 5.5 5.5C3 9.3 2.3 13 2.6 16.7a15.7 15.7 0 0 0 4.8 2.4c.4-.6.8-1.2 1.1-1.8a10.2 10.2 0 0 1-1.6-.8l.4-.3c3.1 1.4 6.5 1.4 9.6 0l.4.3a10.2 10.2 0 0 1-1.6.8c.3.6.7 1.2 1.1 1.8a15.7 15.7 0 0 0 4.8-2.4c.4-4.3-.7-8-3.1-11.2zM8.5 14c-.8 0-1.5-.7-1.5-1.6s.7-1.6 1.5-1.6 1.5.7 1.5 1.6-.7 1.6-1.5 1.6zm7 0c-.8 0-1.5-.7-1.5-1.6s.7-1.6 1.5-1.6 1.5.7 1.5 1.6-.7 1.6-1.5 1.6z"/>',
    "bed": '<path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20M6 8v9"/>',
    "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9C2.1 11.2 2 11.6 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
    "bike": '<circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "briefcase": '<rect width="20" height="14" x="2" y="7" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "money": '<rect width="20" height="12" x="2" y="6" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "play": '<polygon points="5 3 19 12 5 21 5 3"/>',
    "video": '<path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2" ry="2"/>',
    "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "flame": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 3z"/>',
    "radio": '<circle cx="12" cy="12" r="2"/><path d="M16.2 7.8a6 6 0 0 1 0 8.4M7.8 7.8a6 6 0 0 0 0 8.4M19.1 4.9a10 10 0 0 1 0 14.2M4.9 4.9a10 10 0 0 0 0 14.2"/>',
    "volume": '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07M19.07 4.93a10 10 0 0 1 0 14.14"/>',
}


def ic(name, s=22, c="currentColor", w=2, fill="none"):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="{fill}" stroke="{c}" '
            f'stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" style="flex:none">{ICONS[name]}</svg>')


import base64

_B64_CACHE = {}

def get_b64_uri(name):
    if name in _B64_CACHE:
        return _B64_CACHE[name]
    for folder in ["assets_opt", "assets"]:
        p = os.path.join(HERE, folder, name)
        if os.path.exists(p):
            if name.endswith(".svg"):
                mime = "image/svg+xml"
            elif name.endswith(".png"):
                mime = "image/png"
            else:
                mime = "image/jpeg"
            with open(p, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            uri = f"data:{mime};base64,{b64}"
            _B64_CACHE[name] = uri
            return uri
    return None

def asset(name):
    return (os.path.exists(os.path.join(HERE, "assets_opt", name)) or 
            os.path.exists(os.path.join(HERE, "assets", name)))

def img(name, style, fallback="linear-gradient(135deg,#DCE7FF,#BFE9FB)"):
    uri = get_b64_uri(name)
    if uri:
        return f'<img src="{uri}" style="object-fit:cover;display:block;flex:none;{style}">'
    return f'<div style="background:{fallback};flex:none;{style}"></div>'

def avatar(s=44, ring=None):
    b = f"border:3px solid {ring};" if ring else ""
    return img("profile.jpg", f"width:{s}px;height:{s}px;border-radius:50%;object-position:50% 20%;margin:0 auto;{b}")

def sb(dark=False):
    c = "#fff" if dark else C["navy"]
    sig = (f'<svg width="19" height="12" viewBox="0 0 19 12" fill="{c}"><rect x="0" y="8" width="3.2" height="4" rx="1"/>'
           f'<rect x="5.2" y="5.5" width="3.2" height="6.5" rx="1"/><rect x="10.4" y="3" width="3.2" height="9" rx="1"/>'
           f'<rect x="15.6" y="0" width="3.2" height="12" rx="1"/></svg>')
    wifi = (f'<svg width="17" height="12" viewBox="0 0 17 12" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round">'
            f'<path d="M1.5 4.5a10 10 0 0 1 14 0M4 7.6a6.4 6.4 0 0 1 9 0"/><circle cx="8.5" cy="10.5" r="1.1" fill="{c}" stroke="none"/></svg>')
    bat = (f'<svg width="28" height="13" viewBox="0 0 28 13"><rect x=".5" y=".5" width="24" height="12" rx="3.8" fill="none" stroke="{c}" opacity=".4"/>'
           f'<rect x="2.5" y="2.5" width="20" height="8" rx="2.2" fill="{c}"/><rect x="26" y="4.5" width="1.6" height="4" rx=".8" fill="{c}" opacity=".5"/></svg>')
    return (f'<div class="sb" style="width:100%;color:{c};">'
            f'<span style="font-weight:600;font-size:16px;letter-spacing:-0.2px;">9:41</span>'
            f'<div class="island"></div>'
            f'<div class="row" style="gap:6px;align-items:center;">{sig}{wifi}{bat}</div>'
            f'</div>')

def hi(dark=False):
    return f'<div class="hi" style="background:{"#fff" if dark else C["navy"]}"></div>'

def bar(title="", back=True, back_target="S07", right="", left=None):
    if left is None:
        left = f'<div class="ib" data-go="{back_target}" style="cursor:pointer;">{ic("left")}</div>' if back else '<div style="width:44px"></div>'
    if not right:
        right = '<div style="width:44px"></div>'
    return f'<div class="bar">{left}<div class="ttl">{title}</div>{right}</div>'

NAV_ITEMS = [
    ("home", "หน้าหลัก", "S07"),
    ("calendar", "ตารางเรียน", "S12"),
    ("map", "แผนที่", "S21"),
    ("star", "กิจกรรม", "S18"),
    ("user", "โปรไฟล์", "S10")
]

def nav(active, link=True):
    out = '<div class="nav">'
    for i, (icn, label, go) in enumerate(NAV_ITEMS):
        on = " on" if i == active else ""
        attr = f' data-go="{go}" style="cursor:pointer;"' if (link and i != active) else ""
        out += f'<div class="it{on}"{attr}>{ic(icn, 24, w=2.2 if on else 1.9)}<span>{label}</span></div>'
    return out + hi() + "</div>"


def uni(abbr, color, s=44, r=12, fs=None):
    fs = fs or (15 if len(abbr) <= 3 else 12)
    return (f'<div class="tile" style="width:{s}px;height:{s}px;border-radius:{r}px;background:{color};'
            f'color:#fff;font:700 {fs}px Inter">{abbr}</div>')


def uni_seal(name, s=44):
    for folder in ["assets_opt", "assets"]:
        for ext in [".svg", ".png"]:
            p = os.path.join(HERE, folder, "unis", f"{name}{ext}")
            if os.path.exists(p):
                return img(f"unis/{name}{ext}", f"width:{s}px;height:{s}px;object-fit:contain;")
    return uni(name[:2].upper(), C["navy"], s=s)


def badge(text, kind="blue", icon=None):
    i = ic(icon, 14, w=2.4) if icon else ""
    return f'<span class="badge b-{kind}">{i}{text}</span>'


def btn(text, kind="bp", go=None, icon=None, style="", ov=False, label=None):
    a = f' data-go="{go}"' if go else ""
    if label:
        a += f' data-label="{label}"'
    i = ic(icon, 20) if icon else ""
    return f'<div class="btn {kind}"{a} style="{style}">{i}{text}</div>'


def field(text, icon=None, cls="", right="", style=""):
    i = ic(icon, 20, "#94A3B8") if icon else ""
    return f'<div class="field {cls}" style="{style}">{i}<span class="grow" style="white-space:nowrap;overflow:hidden">{text}</span>{right}</div>'


def labeled(label, inner, extra=""):
    return f'<div class="col"><div class="lab"><span>{label}</span>{extra}</div>{inner}</div>'


def screen_bg_hint():
    """Very light skeleton of an underlying screen, used behind popups."""
    return ('<div style="position:absolute;left:20px;top:80px;right:20px;display:flex;flex-direction:column;gap:16px;opacity:.9">'
            '<div style="height:44px;border-radius:14px;background:#fff"></div>'
            '<div style="height:150px;border-radius:24px;background:#fff"></div>'
            '<div style="height:90px;border-radius:16px;background:#fff"></div>'
            '<div style="height:90px;border-radius:16px;background:#fff"></div>'
            '<div style="height:220px;border-radius:16px;background:#fff"></div></div>')


def qr_svg(size=200, seed="THAISUKSA-670610452", color="#101C36"):
    """Real QR if `qrcode` is installed, else a deterministic QR-like pattern."""
    try:
        import qrcode
        q = qrcode.QRCode(border=0)
        q.add_data(seed)
        q.make(fit=True)
        m = q.get_matrix()
    except Exception:
        import random
        rnd = random.Random(seed)
        n = 25
        m = [[rnd.random() < 0.48 for _ in range(n)] for _ in range(n)]
        for (ox, oy) in [(0, 0), (n - 7, 0), (0, n - 7)]:
            for y in range(7):
                for x in range(7):
                    edge = x in (0, 6) or y in (0, 6)
                    core = 2 <= x <= 4 and 2 <= y <= 4
                    m[oy + y][ox + x] = edge or core
                if ox + 7 < n:
                    m[oy + y][ox + 7 if ox == 0 else ox - 1] = False
    n = len(m)
    cell = size / n
    rects = "".join(
        f'<rect x="{x*cell:.2f}" y="{y*cell:.2f}" width="{cell+0.3:.2f}" height="{cell+0.3:.2f}"/>'
        for y in range(n) for x in range(n) if m[y][x])
    return f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" fill="{color}" style="flex:none">{rects}</svg>'
