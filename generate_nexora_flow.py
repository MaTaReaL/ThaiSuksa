"""Generate the complete THAI SUKSA (ไทยศึกษา) 31-screen prototype board with visual connector arrows."""
import os
import json
import re
from kit import (
    W, H, C, USER, CSS, ICONS, ic, img, avatar, sb, hi, bar, nav, uni, uni_seal, badge,
    btn, field, labeled, screen_bg_hint, qr_svg
)

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Screen Builders
# ---------------------------------------------------------------------------

def s01_splash():
    """01. Splash Screen (Master Institutional Brand Launch)"""
    return f"""
    <div class="scr" data-go="S02" style="background:radial-gradient(ellipse at 50% 25%, #132247 0%, #0A1128 55%, #060A17 100%) !important;color:#FFFFFF !important;cursor:pointer;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:space-between;width:100%;height:100%;">
      {sb(dark=True)}

      <!-- Ambient Lighting & Architectural Constellation Overlay -->
      <div style="position:absolute;top:-100px;left:50%;transform:translateX(-50%);width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(36,107,253,0.25) 0%,rgba(10,17,40,0) 70%);pointer-events:none;"></div>
      <div style="position:absolute;top:180px;left:50%;transform:translateX(-50%);width:260px;height:260px;border-radius:50%;background:radial-gradient(circle,rgba(245,158,11,0.14) 0%,rgba(10,17,40,0) 70%);pointer-events:none;"></div>

      <!-- Top Accreditation Pill -->
      <div style="position:relative;z-index:2;margin-top:20px;display:flex;justify-content:center;width:100%;">
        <div style="display:flex;align-items:center;gap:8px;padding:6px 14px;border-radius:20px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);backdrop-filter:blur(12px);">
          <div style="width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 8px #10B981;"></div>
          <span style="font:600 11px 'Inter','IBM Plex Sans Thai';color:#E2E8F0;letter-spacing:.4px;">MHESI DIGITAL PLATFORM • กระทรวง อว.</span>
        </div>
      </div>

      <!-- Center Hero: Master Logo in Glassmorphic Halo Frame -->
      <div style="position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 24px;width:100%;">
        
        <!-- Outer Halo Frame for Logo -->
        <div style="position:relative;width:176px;height:176px;display:flex;align-items:center;justify-content:center;margin-bottom:24px;">
          <!-- Ambient Aura Glow Behind Squircle -->
          <div style="position:absolute;inset:-12px;border-radius:48px;background:linear-gradient(135deg,rgba(36,107,253,0.45),rgba(88,214,255,0.25),rgba(245,158,11,0.3));filter:blur(18px);opacity:0.8;"></div>
          
          <!-- Glassmorphic Border Frame -->
          <div style="position:absolute;inset:0;border-radius:44px;background:rgba(255,255,255,0.08);border:1.5px solid rgba(255,255,255,0.24);box-shadow:0 28px 65px rgba(0,0,0,0.7),inset 0 1px 2px rgba(255,255,255,0.4);backdrop-filter:blur(20px);"></div>
          
          <!-- Untouched 1024x1024 Squircle Icon -->
          <div style="position:relative;z-index:3;width:164px;height:164px;border-radius:40px;overflow:hidden;display:flex;align-items:center;justify-content:center;box-shadow:0 12px 28px rgba(0,0,0,0.3);">
            {img("thai_suksa_logo.png", "width:100%;height:100%;object-fit:cover;")}
          </div>
        </div>

        <!-- Typography & Positioning -->
        <div style="display:flex;flex-direction:column;align-items:center;gap:6px;">
          <div style="font:800 12px 'Plus Jakarta Sans',Inter;letter-spacing:3.5px;color:{C['cyan']};text-transform:uppercase;">
            NATIONAL SMART CAMPUS PLATFORM
          </div>
          <div style="font:700 22px 'IBM Plex Sans Thai',sans-serif;color:#FFFFFF;letter-spacing:.4px;margin-top:2px;">
            ระบบนิเวศการศึกษาและชีวิตมหาวิทยาลัย
          </div>
          <div style="font:400 13px 'IBM Plex Sans Thai',sans-serif;color:#94A3B8;max-width:320px;line-height:1.5;margin-top:4px;">
            เชื่อมต่อข้อมูลนักศึกษา ตารางเรียน สวัสดิการ และบริการครบวงจรในแอปเดียว
          </div>
        </div>

        <!-- Sleek Quick Start CTA Button -->
        <div style="margin-top:26px;width:100%;display:flex;flex-direction:column;align-items:center;">
          <div class="btn bp" data-go="S02" style="cursor:pointer;width:270px;height:50px;border-radius:25px;background:linear-gradient(135deg,#246BFD 0%,#1D4ED8 100%);box-shadow:0 12px 28px rgba(36,107,253,0.5),inset 0 1px 1px rgba(255,255,255,0.3);display:flex;align-items:center;justify-content:center;gap:10px;font-weight:700;font-size:15px;color:#fff;">
            <span>เข้าสู่ระบบ / เริ่มต้นใช้งาน</span>
            {ic("right", 18, "#fff")}
          </div>
          <div style="font-size:11px;color:#64748B;margin-top:10px;">แตะส่วนใดก็ได้บนหน้าจอเพื่อข้าม</div>
        </div>

      </div>

      <!-- Bottom Institutional Footer -->
      <div style="position:relative;z-index:2;margin-bottom:28px;display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;width:100%;">
        <!-- Sleek Hairline Gradient Progress Bar -->
        <div style="width:130px;height:3px;background:rgba(255,255,255,0.12);border-radius:10px;overflow:hidden;position:relative;">
          <div style="width:65%;height:100%;background:linear-gradient(90deg,#246BFD,#58D6FF,#F59E0B);border-radius:10px;"></div>
        </div>
        
        <div style="font-size:11px;color:#64748B;line-height:1.4;">
          กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (อว.)<br>
          <span style="font-size:10px;color:#475569;">มหาวิทยาลัยศิลปากร • Version 3.0 Enterprise</span>
        </div>
      </div>

      {hi(dark=True)}
    </div>
    """

def s02_welcome():
    """02. Welcome / Onboarding"""
    return f'''
    <div class="scr" style="background:#fff;">
      {sb()}
      <div class="bar" style="justify-content:space-between;">
        <div class="row" style="gap:10px;">
          {img("thai_suksa_logo.png", "width:34px;height:34px;border-radius:9px;object-fit:contain;box-shadow:0 2px 8px rgba(0,0,0,0.12);")}
          <span style="font:800 20px 'IBM Plex Sans Thai',Inter;color:{C['navy']};letter-spacing:.5px;">ไทยศึกษา</span>
        </div>
        <div class="badge b-blue" style="font-size:12px;padding:4px 12px;border-radius:20px;">TH | EN</div>
      </div>
      <div class="body" style="padding:0 24px 24px;justify-content:space-between;text-align:center;">
        <div style="margin-top:10px;">
          <div style="width:100%;height:320px;border-radius:28px;overflow:hidden;background:#F1F5F9;display:flex;align-items:center;justify-content:center;">
            {img("onboarding_hero.jpg", "width:100%;height:100%;object-fit:cover;")}
          </div>
        </div>
        <div>
          <div class="badge b-navy" style="margin-bottom:12px;font-size:11px;">
            {ic("shield", 14, C['cyan'])} ศูนย์กลางข้อมูลนักศึกษาทุกมหาวิทยาลัย (อว.)
          </div>
          <div class="h1" style="font-size:27px;color:{C['navy']};">Your Campus Life,<br>Unified in One Tap</div>
          <p class="p" style="margin-top:10px;font-size:14px;padding:0 10px;">
            เชื่อมโยงตารางเรียน แผนที่ รถรับส่ง การจองห้องสอบ คำร้อง และ AI ผู้ช่วย เข้ากับทุกสถาบันอุดมศึกษาทั่วประเทศ
          </p>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;">
          {btn("เข้าสู่ระบบ (Sign In)", "bp", go="S04", icon="right")}
          {btn("ลงทะเบียนใหม่ด้วย Thai ID (ThaID)", "bs", go="S05")}
        </div>
      </div>
      {hi()}
    </div>
    '''

ALL_UNIVERSITIES = [('public', 'silpakorn', 'SU', '#0F7F59', 'มหาวิทยาลัยศิลปากร', 'Silpakorn University', 'วิทยาเขตพระราชวังสนามจันทร์ / วังท่าพระ / เพชรบุรี', True), ('public', 'chula', 'CU', '#E11D48', 'จุฬาลงกรณ์มหาวิทยาลัย', 'Chulalongkorn University', 'เขตปทุมวัน กรุงเทพมหานคร', False), ('public', 'thammasat', 'TU', '#F59E0B', 'มหาวิทยาลัยธรรมศาสตร์', 'Thammasat University', 'ศูนย์รังสิต / ท่าพระจันทร์ / พัทยา / ลำปาง', False), ('public', 'kasetsart', 'KU', '#16A34A', 'มหาวิทยาลัยเกษตรศาสตร์', 'Kasetsart University', 'วิทยาเขตบางเขน / กำแพงแสน / ศรีราชา / สกลนคร', False), ('public', 'mahidol', 'MU', '#0284C7', 'มหาวิทยาลัยมหิดล', 'Mahidol University', 'ศาลายา นครปฐม / พญาไท / บางกอกน้อย / กาญจนบุรี', False), ('public', 'cmu', 'CMU', '#8B5CF6', 'มหาวิทยาลัยเชียงใหม่', 'Chiang Mai University', 'อำเภอเมือง เชียงใหม่', False), ('public', 'kku', 'KKU', '#B45309', 'มหาวิทยาลัยขอนแก่น', 'Khon Kaen University', 'อำเภอเมือง ขอนแก่น / วิทยาเขตหนองคาย', False), ('public', 'psu', 'PSU', '#0284C7', 'มหาวิทยาลัยสงขลานครินทร์', 'Prince of Songkla University', 'หาดใหญ่ / ปัตตานี / ภูเก็ต / สุราษฎร์ธานี / ตรัง', False), ('public', 'kmitl', 'KMITL', '#EA580C', 'สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง', 'KMITL', 'เขตลาดกระบัง กรุงเทพฯ / วิทยาเขตชุมพร', False), ('public', 'kmutt', 'KMUTT', '#DC2626', 'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี', 'KMUTT', 'บางมด / บางขุนเทียน / ราชบุรี', False), ('public', 'kmutnb', 'KMUTNB', '#C2410C', 'มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ', 'KMUTNB', 'เขตบางซื่อ กรุงเทพฯ / ปราจีนบุรี / ระยอง', False), ('public', 'swu', 'SWU', '#BE123C', 'มหาวิทยาลัยศรีนครินทรวิโรฒ', 'Srinakharinwirot University', 'ประสานมิตร กรุงเทพฯ / องครักษ์ นครนายก', False), ('public', 'buu', 'BUU', '#D97706', 'มหาวิทยาลัยบูรพา', 'Burapha University', 'บางแสน ชลบุรี / จันทบุรี / สระแก้ว', False), ('public', 'mfu', 'MFU', '#B91C1C', 'มหาวิทยาลัยแม่ฟ้าหลวง', 'Mae Fah Luang University', 'อำเภอเมือง เชียงราย', False), ('public', 'nu', 'NU', '#7C3AED', 'มหาวิทยาลัยนเรศวร', 'Naresuan University', 'อำเภอเมือง พิษณุโลก', False), ('public', 'up', 'UP', '#9333EA', 'มหาวิทยาลัยพะเยา', 'University of Phayao', 'อำเภอเมือง พะเยา', False), ('public', 'ru', 'RU', '#1D4ED8', 'มหาวิทยาลัยรามคำแหง', 'Ramkhamhaeng University', 'หัวหมาก / บางนา / สาขาวิทยบริการทั่วประเทศ', False), ('public', 'stou', 'STOU', '#047857', 'มหาวิทยาลัยสุโขทัยธรรมาธิราช', 'Sukhothai Thammathirat Open University', 'ปากเกร็ด นนทบุรี', False), ('public', 'sut', 'SUT', '#C2410C', 'มหาวิทยาลัยเทคโนโลยีสุรนารี', 'Suranaree University of Technology', 'อำเภอเมือง นครราชสีมา', False), ('public', 'wu', 'WU', '#D97706', 'มหาวิทยาลัยวลัยลักษณ์', 'Walailak University', 'ท่าศาลา นครศรีธรรมราช', False), ('public', 'mju', 'MJU', '#15803D', 'มหาวิทยาลัยแม่โจ้', 'Maejo University', 'สันทราย เชียงใหม่ / แพร่ / ชุมพร', False), ('public', 'msu', 'MSU', '#CA8A04', 'มหาวิทยาลัยมหาสารคาม', 'Mahasarakham University', 'กันทรวิชัย มหาสารคาม', False), ('public', 'ubu', 'UBU', '#B45309', 'มหาวิทยาลัยอุบลราชธานี', 'Ubon Ratchathani University', 'วารินชำราบ อุบลราชธานี', False), ('public', 'tsu', 'TSU', '#4338CA', 'มหาวิทยาลัยทักษิณ', 'Thaksin University', 'อำเภอเมือง สงขลา / พัทลุง', False), ('public', 'sdu', 'SDU', '#0369A1', 'มหาวิทยาลัยสวนดุสิต', 'Suan Dusit University', 'เขตดุสิต กรุงเทพฯ / สุพรรณบุรี / ลำปาง', False), ('public', 'nmu', 'NMU', '#0E7490', 'มหาวิทยาลัยนวมินทราธิราช', 'Navamindradhiraj University', 'เขตดุสิต กรุงเทพฯ (วชิรพยาบาล)', False), ('rmut', 'rmutt', 'RMUTT', '#0284C7', 'มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี', 'RMUT Thanyaburi', 'คลองหก ปทุมธานี', False), ('rmut', 'rmutk', 'RMUTK', '#15803D', 'มหาวิทยาลัยเทคโนโลยีราชมงคลกรุงเทพ', 'RMUT Krungthep', 'เขตสาทร กรุงเทพฯ (บพิตรพิมุข)', False), ('rmut', 'rmutp', 'RMUTP', '#7C3AED', 'มหาวิทยาลัยเทคโนโลยีราชมงคลพระนคร', 'RMUT Phra Nakhon', 'เขตดุสิต กรุงเทพฯ (พณิชยการพระนคร)', False), ('rmut', 'rmutr', 'RMUTR', '#DC2626', 'มหาวิทยาลัยเทคโนโลยีราชมงคลรัตนโกสินทร์', 'RMUT Rattanakosin', 'ศาลายา นครปฐม / วังไกลกังวล', False), ('rmut', 'rmutto', 'RMUTTO', '#EA580C', 'มหาวิทยาลัยเทคโนโลยีราชมงคลตะวันออก', 'RMUT Tawan-ok', 'บางพระ ชลบุรี / จักรพงษภูวนารถ', False), ('rmut', 'rmutsb', 'RMUTSB', '#CA8A04', 'มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ', 'RMUT Suvarnabhumi', 'หันตรา พระนครศรีอยุธยา / นนทบุรี', False), ('rmut', 'rmutl', 'RMUTL', '#B45309', 'มหาวิทยาลัยเทคโนโลยีราชมงคลล้านนา', 'RMUT Lanna', 'อำเภอเมือง เชียงใหม่ / ภาคพายัพ', False), ('rmut', 'rmuti', 'RMUTI', '#B91C1C', 'มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน', 'RMUT Isan', 'อำเภอเมือง นครราชสีมา / ขอนแก่น / สุรินทร์', False), ('rmut', 'rmuts', 'RMUTS', '#047857', 'มหาวิทยาลัยเทคโนโลยีราชมงคลศรีวิชัย', 'RMUT Srivijaya', 'อำเภอเมือง สงขลา / ตรัง / นครศรีฯ', False), ('rajabhat', 'ssru', 'SSRU', '#0284C7', 'มหาวิทยาลัยราชภัฏสวนสุนันทา', 'Suan Sunandha Rajabhat University', 'เขตดุสิต กรุงเทพฯ / นครปฐม', False), ('rajabhat', 'bsru', 'BSRU', '#475569', 'มหาวิทยาลัยราชภัฏบ้านสมเด็จเจ้าพระยา', 'Bansomdejchaopraya Rajabhat Univ.', 'เขตธนบุรี กรุงเทพฯ', False), ('rajabhat', 'cru', 'CRU', '#CA8A04', 'มหาวิทยาลัยราชภัฏจันทรเกษม', 'Chandrakasem Rajabhat University', 'เขตจตุจักร กรุงเทพฯ / ชัยนาท', False), ('rajabhat', 'pnru', 'PNRU', '#15803D', 'มหาวิทยาลัยราชภัฏพระนคร', 'Phranakhon Rajabhat University', 'เขตบางเขน กรุงเทพฯ', False), ('rajabhat', 'dru', 'DRU', '#4338CA', 'มหาวิทยาลัยราชภัฏธนบุรี', 'Dhonburi Rajabhat University', 'เขตธนบุรี กรุงเทพฯ / สมุทรปราการ', False), ('rajabhat', 'cmru', 'CMRU', '#B45309', 'มหาวิทยาลัยราชภัฏเชียงใหม่', 'Chiang Mai Rajabhat University', 'อำเภอเมือง เชียงใหม่ / แม่ริม', False), ('rajabhat', 'nrru', 'NRRU', '#B91C1C', 'มหาวิทยาลัยราชภัฏนครราชสีมา', 'Nakhon Ratchasima Rajabhat Univ.', 'อำเภอเมือง นครราชสีมา', False), ('rajabhat', 'npru', 'NPRU', '#047857', 'มหาวิทยาลัยราชภัฏนครปฐม', 'Nakhon Pathom Rajabhat University', 'อำเภอเมือง นครปฐม', False), ('rajabhat', 'vru', 'VRU', '#1D4ED8', 'มหาวิทยาลัยราชภัฏวไลยอลงกรณ์ ในพระบรมราชูปถัมภ์', 'Valaya Alongkorn Rajabhat Univ.', 'คลองหลวง ปทุมธานี / สระแก้ว', False), ('rajabhat', 'sru', 'SRU', '#D97706', 'มหาวิทยาลัยราชภัฏสุราษฎร์ธานี', 'Surat Thani Rajabhat University', 'อำเภอเมือง สุราษฎร์ธานี', False), ('private', 'bu', 'BU', '#DC2626', 'มหาวิทยาลัยกรุงเทพ', 'Bangkok University', 'วิทยาเขตรังสิต ปทุมธานี / กล้วยน้ำไท', False), ('private', 'rsu', 'RSU', '#0284C7', 'มหาวิทยาลัยรังสิต', 'Rangsit University', 'เมืองเอก ปทุมธานี', False), ('private', 'utcc', 'UTCC', '#1D4ED8', 'มหาวิทยาลัยหอการค้าไทย', 'Univ. of the Thai Chamber of Commerce', 'เขตดินแดง กรุงเทพฯ', False), ('private', 'au', 'AU', '#B91C1C', 'มหาวิทยาลัยอัสสัมชัญ (ABAC)', 'Assumption University', 'สุวรรณภูมิ สมุทรปราการ / หัวหมาก', False), ('private', 'spu', 'SPU', '#EA580C', 'มหาวิทยาลัยศรีปทุม', 'Sripatum University', 'เขตจตุจักร กรุงเทพฯ / ชลบุรี / ขอนแก่น', False), ('private', 'dpu', 'DPU', '#7C3AED', 'มหาวิทยาลัยธุรกิจบัณฑิตย์', 'Dhurakij Pundit University', 'เขตหลักสี่ กรุงเทพฯ', False), ('private', 'kbu', 'KBU', '#047857', 'มหาวิทยาลัยเกษมบัณฑิต', 'Kasem Bundit University', 'พัฒนาการ / ร่มเกล้า กรุงเทพฯ', False), ('private', 'pyu', 'PYU', '#0284C7', 'มหาวิทยาลัยพายัพ', 'Payap University', 'อำเภอเมือง เชียงใหม่', False), ('private', 'hcu', 'HCU', '#CA8A04', 'มหาวิทยาลัยหัวเฉียวเฉลิมพระเกียรติ', 'Huachiew Chalermprakiet Univ.', 'บางพลี สมุทรปราการ', False), ('private', 'tni', 'TNI', '#B91C1C', 'สถาบันเทคโนโลยีไทย-ญี่ปุ่น', 'Thai-Nichi Institute of Technology', 'พัฒนาการ กรุงเทพฯ', False)]

def s03_select_university():
    """03. Select University (National Central Portal — 55+ Universities with Real Logos)"""
    categories = [
        ("public", "มหาวิทยาลัยรัฐและในกำกับของรัฐ", "26 สถาบันทั่วประเทศ", "🏛️"),
        ("rmut", "กลุ่มมหาวิทยาลัยเทคโนโลยีราชมงคล (มทร.)", "9 แห่งทั่วประเทศ (ครบทุกแห่ง)", "⚙️"),
        ("rajabhat", "กลุ่มมหาวิทยาลัยราชภัฏ (มรภ.)", "10 แห่งตัวแทนภูมิภาคและ กทม.", "🎓"),
        ("private", "มหาวิทยาลัยเอกชนและสถาบันชั้นนำ", "10 สถาบันมาตรฐานสากล", "✨"),
    ]

    rendered_categories = ""
    for cat_id, cat_title, cat_badge, cat_icon in categories:
        unis_in_cat = [u for u in ALL_UNIVERSITIES if u[0] == cat_id]
        cat_cards = ""
        for cat, slug, abbr, col, th_name, en_name, campus, active in unis_in_cat:
            border = f"border:2px solid {C['blue']};background:#F8FAFF;" if active else "border:1px solid #E5EAF2;background:#fff;"
            chk = f'<div style="width:22px;height:22px;border-radius:50%;background:{C["blue"]};color:#fff;display:flex;align-items:center;justify-content:center;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>' if active else '<div style="width:20px;height:20px;border-radius:50%;border:2px solid #CBD5E1;"></div>'
            cat_cards += f"""
            <div class="uni-card card" data-cat="{cat}" data-slug="{slug}" data-abbr="{abbr}" data-th="{th_name}" data-en="{en_name}" data-campus="{campus}" data-col="{col}" style="padding:14px 16px;{border}display:flex;align-items:center;gap:14px;cursor:pointer;transition:all 0.18s ease;margin-bottom:10px;">
              <div style="width:50px;height:50px;border-radius:14px;background:#fff;border:1px solid #E2E8F0;padding:4px;display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 2px 6px rgba(16,28,54,0.06);">
                {uni_seal(slug, s=42)}
              </div>
              <div style="flex:1;min-width:0;">
                <div class="row" style="gap:8px;align-items:center;">
                  <span class="uni-th" style="font-weight:700;font-size:14px;color:{C['navy']};line-height:1.3;">{th_name}</span>
                  <span class="badge b-blue" style="font-size:10px;padding:1px 6px;height:18px;">{abbr}</span>
                </div>
                <div class="uni-en" style="font-size:12px;color:#64748B;margin-top:2px;">{en_name}</div>
                <div class="uni-campus" style="font-size:11px;color:#94A3B8;margin-top:2px;">{campus}</div>
              </div>
              <div class="uni-chk">{chk}</div>
            </div>
            """

        rendered_categories += f"""
        <div class="uni-sec-header sec" data-sec-cat="{cat_id}" style="margin-top:16px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;">
          <div class="row" style="gap:8px;">
            <span style="font-size:16px;">{cat_icon}</span>
            <span style="font-weight:700;font-size:15px;color:{C['navy']};">{cat_title}</span>
          </div>
          <span class="badge b-blue" style="font-size:11px;">{cat_badge}</span>
        </div>
        <div class="uni-sec-group" data-sec-cat="{cat_id}">
          {cat_cards}
        </div>
        """

    return f"""
    <div class="scr" style="background:#F5F7FB;display:flex;flex-direction:column;transition:height 0.3s ease;">
      {sb()}
      {bar("เลือกสถาบันการศึกษา (2/4)", back=True, back_target="S05", right=f'<div class="ib" onclick="toggleS03Expand()" title="ขยาย/ย่อเฟรมเต็มความยาว" style="cursor:pointer;color:{C["blue"]};">{ic("expand", 18, C["blue"])}</div>')}
      
      <!-- Top Sticky Controls -->
      <div style="padding:0 20px;display:flex;flex-direction:column;gap:10px;flex:none;margin-bottom:10px;">
        <div style="background:#EFF6FF;border:1px solid #DBEAFE;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;">
          {ic("shield", 20, C['blue'])}
          <div style="font-size:12px;color:#1E40AF;line-height:1.4;">
            <strong>ระบบกลางกระทรวง อว.</strong> เชื่อมต่อฐานข้อมูล 55+ สถาบันทั่วประเทศไทย
          </div>
        </div>

        <div style="position:relative;display:flex;align-items:center;background:#fff;border:1.5px solid #E2E8F0;border-radius:14px;padding:0 14px;height:46px;box-shadow:0 2px 6px rgba(16,28,54,0.04);">
          <div style="margin-right:10px;display:flex;align-items:center;color:#94A3B8;">{ic("search", 18, "#94A3B8")}</div>
          <input id="uni_search_input" type="text" placeholder="ค้นหาชื่อมหาวิทยาลัย ตัวย่อ (SU, CU...) หรือจังหวัด" style="border:none;outline:none;background:transparent;width:100%;font:500 13px 'IBM Plex Sans Thai',Inter;color:{C['navy']};">
          <div id="uni_count_badge" class="badge b-blue" style="font-size:11px;margin-left:8px;">55 แห่ง</div>
        </div>

        <div class="chips" style="gap:8px;overflow-x:auto;padding-bottom:2px;flex:none;">
          <div class="uni-chip chip on" data-filter="all" style="cursor:pointer;">ทั้งหมด (55)</div>
          <div class="uni-chip chip" data-filter="public" style="cursor:pointer;">ม.รัฐ/ในกำกับ (26)</div>
          <div class="uni-chip chip" data-filter="rmut" style="cursor:pointer;">มทร. (9)</div>
          <div class="uni-chip chip" data-filter="rajabhat" style="cursor:pointer;">มรภ. (10)</div>
          <div class="uni-chip chip" data-filter="private" style="cursor:pointer;">ม.เอกชน (10)</div>
        </div>
      </div>

      <!-- Main Scrollable Directory Body -->
      <div id="uni_scroll_body" class="body" style="padding:0 20px 16px;gap:6px;flex:1;overflow-y:auto;overflow-x:hidden;">
        {rendered_categories}
      </div>

      <!-- Bottom Confirmation Action Bar -->
      <div class="uni-confirm-bar" style="background:#fff;border-top:1px solid #E5EAF2;padding:12px 20px;display:flex;flex-direction:column;gap:8px;flex:none;box-shadow:0 -6px 20px rgba(16,28,54,0.06);z-index:40;">
        <div style="display:flex;align-items:center;justify-content:space-between;">
          <div style="font-size:12px;color:#64748B;">สถาบันที่เลือก:</div>
          <div id="uni_selected_label" style="font-weight:700;font-size:13px;color:#246BFD;">มหาวิทยาลัยศิลปากร (SU)</div>
        </div>
        <div id="uni_confirm_btn" class="btn bp" data-go="S04B" style="cursor:pointer;width:100%;font-weight:700;display:flex;align-items:center;justify-content:center;gap:10px;height:48px;">
          <span id="uni_btn_text">ยืนยันและดำเนินการต่อ (Continue with SU)</span>
          {ic("right", 18, "#fff")}
        </div>
      </div>

      {hi()}
    </div>
    """

def s04_login():
    """04. Login (University SSO & Platform Logins)"""
    return f"""
    <div class="scr" style="background:#F8FAFC;">
      {sb()}
      {bar("เข้าสู่ระบบ", back=True, back_target="S02")}
      <div class="body" style="padding:0 24px 24px;gap:13px;overflow-y:auto;">
        
        <!-- Selected University Pill with Quick SSO Button -->
        <div id="login_uni_pill" class="card" style="padding:14px 16px;background:#fff;border:1.5px solid #E2E8F0;box-shadow:0 3px 10px rgba(16,28,54,0.04);display:flex;flex-direction:column;gap:12px;">
          <div style="display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <div id="login_uni_seal" style="width:42px;height:42px;border-radius:12px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;padding:2px;flex:none;box-shadow:0 2px 6px rgba(0,0,0,0.04);">
                {uni_seal("silpakorn", s=38)}
              </div>
              <div>
                <div id="login_uni_name" style="font-weight:700;font-size:13.5px;color:{C['navy']};">{USER['uni']}</div>
                <div id="login_uni_campus" style="font-size:11px;color:#64748B;">{USER['campus']}</div>
              </div>
            </div>
            <span class="badge b-green" style="font-size:10px;padding:2px 8px;">เชื่อมต่อแล้ว</span>
          </div>
          
          <!-- SU-NET SSO Primary Button -->
          <div data-go="S04B" class="btn" style="background:linear-gradient(135deg, #00C48C 0%, #009E6F 100%);color:#fff;font-weight:700;font-size:13.5px;height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:10px;cursor:pointer;box-shadow:0 4px 14px rgba(0,196,140,0.28);transition:transform 0.15s ease;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            <span id="login_sso_btn_text">เข้าใช้งานด้วย SU-NET SSO (Single Sign-On)</span>
          </div>
        </div>

        <!-- Social / Platform Logins Section -->
        <div style="margin-top:2px;">
          <div class="row" style="margin:2px 0 10px;">
            <div class="sep" style="flex:1;"></div>
            <span style="padding:0 10px;font-size:12px;font-weight:600;color:#64748B;">หรือเข้าสู่ระบบด้วยแพลตฟอร์มที่เชื่อมต่อไว้</span>
            <div class="sep" style="flex:1;"></div>
          </div>

          <!-- Platform Login Buttons Grid -->
          <div style="display:flex;flex-direction:column;gap:8px;">
            
            <!-- Google Login Button -->
            <div class="btn" data-go="S07" data-platform="Google" style="background:#fff;border:1.5px solid #E2E8F0;color:#1E293B;font-weight:600;font-size:13.5px;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;cursor:pointer;box-shadow:0 2px 6px rgba(16,28,54,0.03);">
              <div class="row" style="gap:12px;">
                <svg width="20" height="20" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.33 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.14-1.55.38-2.27V6.58H1.25C.45 8.16 0 9.94 0 12s.45 3.84 1.25 5.42l4.03-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.33 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>
                <span>ดำเนินการต่อด้วย Google</span>
              </div>
              <span class="badge b-blue" style="font-size:10px;padding:2px 8px;">เชื่อมต่อแล้ว</span>
            </div>

            <!-- Facebook Login Button -->
            <div class="btn" data-go="S07" data-platform="Facebook" style="background:#fff;border:1.5px solid #E2E8F0;color:#1E293B;font-weight:600;font-size:13.5px;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;cursor:pointer;box-shadow:0 2px 6px rgba(16,28,54,0.03);">
              <div class="row" style="gap:12px;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                <span>เข้าสู่ระบบด้วย Facebook</span>
              </div>
              <span style="color:#94A3B8;">{ic("right", 16, "#94A3B8")}</span>
            </div>

            <!-- 3-Column Platforms: X, TikTok, Discord -->
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;">
              
              <!-- X (Twitter) -->
              <div class="btn" data-go="S07" data-platform="X" style="background:#fff;border:1.5px solid #E2E8F0;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;box-shadow:0 2px 6px rgba(16,28,54,0.03);">
                <svg width="17" height="17" viewBox="0 0 24 24" fill="#000"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                <span style="font-weight:600;font-size:12.5px;color:#1E293B;">X</span>
              </div>

              <!-- TikTok -->
              <div class="btn" data-go="S07" data-platform="TikTok" style="background:#fff;border:1.5px solid #E2E8F0;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;box-shadow:0 2px 6px rgba(16,28,54,0.03);">
                <svg width="17" height="17" viewBox="0 0 24 24" fill="#000"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.29 0 .58.04.85.12V9.4a6.33 6.33 0 0 0-1-.08A6.34 6.34 0 0 0 3 15.66a6.34 6.34 0 0 0 10.82 4.47V10.8a8.28 8.28 0 0 0 5.77 2.28v-3.45a4.84 4.84 0 0 1 0-2.94z"/></svg>
                <span style="font-weight:600;font-size:12.5px;color:#1E293B;">TikTok</span>
              </div>

              <!-- Discord -->
              <div class="btn" data-go="S07" data-platform="Discord" style="background:#fff;border:1.5px solid #E2E8F0;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;gap:6px;cursor:pointer;box-shadow:0 2px 6px rgba(16,28,54,0.03);">
                <svg width="17" height="17" viewBox="0 0 24 24" fill="#5865F2"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
                <span style="font-weight:600;font-size:12.5px;color:#1E293B;">Discord</span>
              </div>
            </div>

          </div>
        </div>

        <!-- Traditional Student ID Login Form -->
        <div style="margin-top:2px;">
          <div class="row" style="margin:2px 0 10px;">
            <div class="sep" style="flex:1;"></div>
            <span style="padding:0 10px;font-size:12px;font-weight:600;color:#64748B;">หรือเข้าด้วยรหัสนักศึกษา</span>
            <div class="sep" style="flex:1;"></div>
          </div>

          <div style="display:flex;flex-direction:column;gap:10px;">
            {labeled("รหัสนักศึกษา / อีเมลมหาวิทยาลัย", field(USER['sid'], icon="user"))}
            {labeled("รหัสผ่าน (Password)", field("••••••••••••••", icon="lock", right=ic("eye", 18, "#94A3B8")), extra='<span class="link" data-go="S06" style="cursor:pointer;">ลืมรหัสผ่าน?</span>')}

            <div class="row" style="justify-content:space-between;margin:2px 0;">
              <label class="row" style="gap:8px;font-size:13px;color:{C['navy']};cursor:pointer;">
                <input type="checkbox" checked style="accent-color:{C['blue']};width:16px;height:16px;">
                <span>จดจำการเข้าสู่ระบบ</span>
              </label>
            </div>

            {btn("เข้าสู่ระบบ (Sign In)", "bp", go="S07", icon="right")}
          </div>
        </div>

        <!-- Mandatory Thai ID Registration Link -->
        <div style="margin-top:auto;padding-top:10px;text-align:center;">
          <div style="font-size:13px;color:#64748B;">
            ยังไม่มีบัญชีนักศึกษา? 
            <span class="link" data-go="S05" style="cursor:pointer;font-weight:700;color:{C['blue']};">ลงทะเบียนใหม่ด้วย Thai ID</span>
          </div>
        </div>

      </div>
      {hi()}
    </div>
    """

def s04b_sso_webview():
    """04B. University SSO Webview (Exact SU-NET SSO Replica from User Screenshot)"""
    return f"""
    <div class="scr" style="background:#FFFFFF;display:flex;flex-direction:column;">
      {sb()}
      
      <!-- Mock Browser Address Bar Header (Matching URL from user screenshot) -->
      <div style="background:#1E293B;padding:8px 16px;display:flex;align-items:center;justify-content:space-between;color:#fff;flex:none;gap:10px;">
        <div class="row" style="gap:8px;align-items:center;flex:1;min-width:0;">
          <div data-go="S04" style="cursor:pointer;color:#94A3B8;display:flex;align-items:center;">
            {ic("left", 18, "#fff")}
          </div>
          <!-- Browser Address Bar -->
          <div style="background:#0F172A;border-radius:18px;padding:5px 12px;display:flex;align-items:center;gap:6px;flex:1;min-width:0;border:1px solid #334155;">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#00C48C" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span style="font-size:11px;color:#CBD5E1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-family:monospace;">sso.su.ac.th/nidp/app/login?id=505&sid=0</span>
          </div>
        </div>
        <div class="row" style="gap:10px;color:#94A3B8;">
          <span style="font-size:10.5px;background:#334155;padding:2px 6px;border-radius:6px;color:#38BDF8;font-weight:600;">SSL 256</span>
        </div>
      </div>

      <!-- Main SSO Body (100% exact replica of screenshot) -->
      <div class="body" style="padding:24px 26px 20px;display:flex;flex-direction:column;align-items:center;background:#FFFFFF;flex:1;overflow-y:auto;text-align:center;">
        
        <!-- Large Authentic Silpakorn Ganesha Circular Seal -->
        <div id="sso_uni_seal" style="width:160px;height:160px;border-radius:50%;background:#FFFFFF;display:flex;align-items:center;justify-content:center;margin-bottom:12px;flex:none;">
          {uni_seal("silpakorn", s=155)}
        </div>

        <!-- SU-NET Title (Exact green serif/display font from screenshot) -->
        <div id="sso_uni_title" style="font:800 34px 'Inter',serif;color:#00B074;letter-spacing:1px;margin-top:2px;line-height:1.1;">
          SU-NET
        </div>
        
        <!-- Single Sign On (SSO) Subtitle (Light grey serif font from screenshot) -->
        <div style="font-family:'Times New Roman',Georgia,serif;font-size:16px;color:#B0B0B0;margin-top:6px;margin-bottom:26px;letter-spacing:0.3px;">
          Single Sign On (SSO)
        </div>

        <!-- Input 1: username/ชื่อผู้ใช้งาน (Exact pill with green border & user icon) -->
        <div style="width:100%;max-width:340px;height:52px;border-radius:9999px;border:2px solid #00C48C;background:#FFFFFF;box-shadow:0 3px 12px rgba(0,196,140,0.12);display:flex;align-items:center;padding:0 20px;gap:12px;margin-bottom:16px;box-sizing:border-box;">
          <div style="color:#00C48C;display:flex;align-items:center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00C48C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          </div>
          <input type="text" value="{USER['sid']}" placeholder="username/ชื่อผู้ใช้งาน" style="border:none;outline:none;background:transparent;width:100%;font:500 15px 'IBM Plex Sans Thai',Inter;color:#1E293B;">
        </div>

        <!-- Input 2: password/รหัสผ่าน (Exact pill with green border & padlock icon) -->
        <div style="width:100%;max-width:340px;height:52px;border-radius:9999px;border:2px solid #00C48C;background:#FFFFFF;box-shadow:0 3px 12px rgba(0,196,140,0.12);display:flex;align-items:center;padding:0 20px;gap:12px;margin-bottom:24px;box-sizing:border-box;">
          <div style="color:#00C48C;display:flex;align-items:center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00C48C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path d="M8 11V7.5a4 4 0 0 1 8 0V11"/></svg>
          </div>
          <input type="password" value="••••••••••••" placeholder="password/รหัสผ่าน" style="border:none;outline:none;background:transparent;width:100%;font:500 15px 'IBM Plex Sans Thai',Inter;color:#1E293B;">
        </div>

        <!-- Submit Button: เข้าสู่ระบบ/Login (Exact solid vibrant green pill from screenshot) -->
        <div id="sso_submit_btn" data-go="S05B" style="width:100%;max-width:340px;height:52px;border-radius:9999px;background:#00C48C;box-shadow:0 6px 18px rgba(0,196,140,0.38);display:flex;align-items:center;justify-content:center;cursor:pointer;color:#FFFFFF;font:700 18px 'IBM Plex Sans Thai',sans-serif;letter-spacing:.3px;transition:all 0.2s ease;">
          เข้าสู่ระบบ/Login
        </div>

        <!-- Footer Text (Exact 2 lines from screenshot) -->
        <div style="margin-top:auto;padding-top:32px;padding-bottom:8px;text-align:center;">
          <div id="sso_footer_th" style="font-size:11.5px;color:#8E8E93;line-height:1.5;">สำนักดิจิทัลเทคโนโลยี มหาวิทยาลัยศิลปากร</div>
          <div id="sso_footer_en" style="font-size:11px;color:#8E8E93;margin-top:2px;">Bureau of Digital Technology, Silpakorn University</div>
        </div>

      </div>
      {hi()}
    </div>
    """

def s05_thaid_registration():
    """05. Register - Step 1: Thai ID (ThaID D.DOPA Mandatory Identity Verification)"""
    return f"""
    <div class="scr" style="background:#F8FAFC;">
      {sb()}
      {bar("ลงทะเบียนใหม่ (1/4)", back=True, back_target="S02")}
      <div class="body" style="padding:0 24px 24px;gap:14px;overflow-y:auto;">
        
        <!-- Stepper Progress Bar -->
        <div style="display:flex;align-items:center;justify-content:space-between;padding:0 4px;margin-bottom:2px;">
          <div style="display:flex;align-items:center;gap:6px;">
            <div style="width:24px;height:24px;border-radius:50%;background:{C['blue']};color:#fff;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center;">1</div>
            <span style="font-weight:700;font-size:12px;color:{C['blue']};">Thai ID</span>
          </div>
          <div style="flex:1;height:2px;background:#CBD5E1;margin:0 6px;"></div>
          <div style="display:flex;align-items:center;gap:6px;">
            <div style="width:24px;height:24px;border-radius:50%;background:#E2E8F0;color:#64748B;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center;">2</div>
            <span style="font-weight:500;font-size:12px;color:#64748B;">เลือกสถาบัน</span>
          </div>
          <div style="flex:1;height:2px;background:#CBD5E1;margin:0 6px;"></div>
          <div style="display:flex;align-items:center;gap:6px;">
            <div style="width:24px;height:24px;border-radius:50%;background:#E2E8F0;color:#64748B;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center;">3</div>
            <span style="font-weight:500;font-size:12px;color:#64748B;">SSO มหาลัย</span>
          </div>
        </div>

        <!-- Official ThaID Accreditation Banner -->
        <div class="card" style="background:linear-gradient(135deg, #0A2540 0%, #001E3C 100%);color:#fff;padding:16px;border-radius:18px;border:1px solid #1E3A5F;box-shadow:0 8px 24px rgba(10,37,64,0.18);">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px;">
            <div style="width:44px;height:44px;border-radius:12px;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;flex:none;border:1px solid rgba(255,255,255,0.2);">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            </div>
            <div>
              <div style="font-weight:800;font-size:16px;color:#fff;letter-spacing:.3px;">ThaID (ไทยดี)</div>
              <div style="font-size:11px;color:#94A3B8;">ระบบพิสูจน์และยืนยันตัวตนทางดิจิทัล กรมการปกครอง</div>
            </div>
          </div>
          <div style="font-size:12px;color:#E2E8F0;line-height:1.5;">
            ตามเกณฑ์กระทรวง อว. นักศึกษาทุกคนต้องยืนยันตัวตนด้วยบัตรประชาชนดิจิทัล ThaID เป็นหลักก่อนสร้างบัญชี เพื่อความปลอดภัยและรับรองสิทธิประโยชน์นักศึกษา
          </div>
        </div>

        <!-- Verified Digital Identity Card -->
        <div class="card" style="background:#fff;border:1.5px solid #22C55E;padding:16px;border-radius:18px;box-shadow:0 4px 14px rgba(34,197,94,0.08);">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
            <span class="badge b-green" style="font-size:11px;padding:3px 10px;">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="margin-right:4px;"><polyline points="20 6 9 17 4 12"/></svg>
              ยืนยันตัวตนผ่านแล้ว (IAL 2.3)
            </span>
            <span style="font-size:11px;color:#64748B;">ฐานข้อมูลทะเบียนราษฎร์</span>
          </div>

          <div style="display:flex;gap:14px;align-items:center;">
            <div style="width:64px;height:78px;border-radius:10px;background:#F1F5F9;border:1px solid #CBD5E1;overflow:hidden;flex:none;display:flex;align-items:center;justify-content:center;">
              {avatar(64)}
            </div>
            <div style="flex:1;min-width:0;">
              <div style="font-size:11px;color:#64748B;">เลขประจำตัวประชาชน 13 หลัก</div>
              <div style="font-weight:700;font-size:15px;color:#1E293B;font-family:monospace;letter-spacing:1px;">1-7399-00284-51-2</div>
              <div style="font-size:11px;color:#64748B;margin-top:6px;">ชื่อ-นามสกุล (ภาษาไทย)</div>
              <div style="font-weight:700;font-size:14px;color:{C['navy']};">{USER['th_full']}</div>
              <div style="font-size:11px;color:#64748B;">Mr. Thanapol Kitbumrung</div>
            </div>
          </div>

          <div class="sep" style="margin:12px 0 10px;"></div>
          
          <div style="display:flex;justify-content:space-between;font-size:11.5px;color:#64748B;">
            <span>สถานะบัตร: <strong style="color:#16A34A;">ปกติ (Active)</strong></span>
            <span>ความน่าเชื่อถือ: <strong>ระดับสูง (DOPA Certified)</strong></span>
          </div>
        </div>

        <!-- Next Action Button -> Go to Step 2: Select University -->
        <div style="margin-top:auto;display:flex;flex-direction:column;gap:10px;">
          <div class="btn bp" data-go="S03" style="width:100%;height:48px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;cursor:pointer;">
            <span>ถัดไป: เลือกสถาบันการศึกษา (Select University)</span>
            {ic("right", 18, "#fff")}
          </div>
          <div style="text-align:center;">
            <span class="link" data-go="S04" style="font-size:12.5px;color:#64748B;cursor:pointer;">มีบัญชีอยู่แล้ว? เข้าสู่ระบบ</span>
          </div>
        </div>

      </div>
      {hi()}
    </div>
    """

def s05b_social_linking():
    """05B. Register - Step 4: Link Social Platforms (Optional & Skappable)"""
    return f"""
    <div class="scr" style="background:#F8FAFC;">
      {sb()}
      {bar("เชื่อมต่อแพลตฟอร์ม (4/4)", back=True, back_target="S04B")}
      <div class="body" style="padding:0 24px 24px;gap:13px;overflow-y:auto;">
        
        <!-- Header Info -->
        <div style="text-align:center;padding:8px 0 2px;">
          <div style="width:56px;height:56px;border-radius:18px;background:#EFF6FF;color:{C['blue']};margin:0 auto 8px;display:flex;align-items:center;justify-content:center;">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{C['blue']}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
          </div>
          <div class="h2" style="font-size:19px;color:{C['navy']};">เชื่อมต่อแพลตฟอร์มโซเชียล</div>
          <p class="cap" style="margin-top:3px;font-size:12px;color:#64748B;line-height:1.5;">
            ผูกบัญชีเพื่อความสะดวกในการเข้าสู่ระบบด้วย 1 คลิกในครั้งต่อไป (หรือกดข้ามได้หากไม่ต้องการเชื่อมต่อ)
          </p>
        </div>

        <!-- Success Toast of Thai ID & SSO -->
        <div style="background:#ECFDF5;border:1px solid #A7F3D0;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;">
          <div style="color:#10B981;flex:none;">{ic("check", 18, "#10B981")}</div>
          <div style="font-size:12px;color:#065F46;line-height:1.4;">
            <strong>ยืนยันตัวตนสำเร็จ:</strong> ผูก Thai ID และ SU-NET SSO (มหาวิทยาลัยศิลปากร) เรียบร้อยแล้ว
          </div>
        </div>

        <!-- Social Platform Toggle Cards -->
        <div style="display:flex;flex-direction:column;gap:8px;">
          
          <!-- 1. Google (Connected by default) -->
          <div class="card" style="padding:11px 16px;background:#fff;border:1.5px solid #246BFD;display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <svg width="22" height="22" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.82-2.4 3.68v3.05h3.88c2.27-2.09 3.66-5.17 3.66-9.17z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.05c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.25v3.15C3.26 21.36 7.33 24 12 24z"/><path fill="#FBBC05" d="M5.28 14.27c-.25-.72-.38-1.49-.38-2.27s.14-1.55.38-2.27V6.58H1.25C.45 8.16 0 9.94 0 12s.45 3.84 1.25 5.42l4.03-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.33 0 3.26 2.64 1.25 6.58l4.03 3.15c.95-2.83 3.6-4.98 6.72-4.98z"/></svg>
              <div>
                <div style="font-weight:700;font-size:13px;color:#1E293B;">Google Account</div>
                <div style="font-size:11px;color:#64748B;">thanapol.k@gmail.com</div>
              </div>
            </div>
            <span class="badge b-blue" style="font-size:10px;padding:3px 8px;">เชื่อมต่อแล้ว</span>
          </div>

          <!-- 2. Facebook -->
          <div class="card" style="padding:11px 16px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              <div>
                <div style="font-weight:700;font-size:13px;color:#1E293B;">Facebook</div>
                <div style="font-size:11px;color:#94A3B8;">แตะเพื่อเชื่อมต่อบัญชี</div>
              </div>
            </div>
            <button class="btn" style="background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;font-size:11px;font-weight:600;padding:4px 10px;border-radius:10px;cursor:pointer;">เชื่อมต่อ</button>
          </div>

          <!-- 3. X (Twitter) -->
          <div class="card" style="padding:11px 16px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="#000"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
              <div>
                <div style="font-weight:700;font-size:13px;color:#1E293B;">X (Twitter)</div>
                <div style="font-size:11px;color:#94A3B8;">แตะเพื่อเชื่อมต่อบัญชี</div>
              </div>
            </div>
            <button class="btn" style="background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;font-size:11px;font-weight:600;padding:4px 10px;border-radius:10px;cursor:pointer;">เชื่อมต่อ</button>
          </div>

          <!-- 4. TikTok -->
          <div class="card" style="padding:11px 16px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="#000"><path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-5.2 1.74 2.89 2.89 0 0 1 2.31-4.64c.29 0 .58.04.85.12V9.4a6.33 6.33 0 0 0-1-.08A6.34 6.34 0 0 0 3 15.66a6.34 6.34 0 0 0 10.82 4.47V10.8a8.28 8.28 0 0 0 5.77 2.28v-3.45a4.84 4.84 0 0 1 0-2.94z"/></svg>
              <div>
                <div style="font-weight:700;font-size:13px;color:#1E293B;">TikTok</div>
                <div style="font-size:11px;color:#94A3B8;">แตะเพื่อเชื่อมต่อบัญชี</div>
              </div>
            </div>
            <button class="btn" style="background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;font-size:11px;font-weight:600;padding:4px 10px;border-radius:10px;cursor:pointer;">เชื่อมต่อ</button>
          </div>

          <!-- 5. Discord -->
          <div class="card" style="padding:11px 16px;background:#fff;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="#5865F2"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
              <div>
                <div style="font-weight:700;font-size:13px;color:#1E293B;">Discord</div>
                <div style="font-size:11px;color:#94A3B8;">แตะเพื่อเชื่อมต่อบัญชี</div>
              </div>
            </div>
            <button class="btn" style="background:#F1F5F9;border:1px solid #CBD5E1;color:#475569;font-size:11px;font-weight:600;padding:4px 10px;border-radius:10px;cursor:pointer;">เชื่อมต่อ</button>
          </div>

        </div>

        <!-- Action CTAs: Save vs Skip -->
        <div style="margin-top:auto;display:flex;flex-direction:column;gap:10px;padding-top:8px;">
          <!-- Save & Continue to Login -->
          <div class="btn bp" data-go="S04" style="width:100%;height:48px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;cursor:pointer;">
            <span>บันทึกและไปหน้าเข้าสู่ระบบ (Complete Setup)</span>
            {ic("check", 18, "#fff")}
          </div>
          
          <!-- Explicit Skip Option as Requested -->
          <div class="btn" data-go="S04" style="width:100%;height:44px;font-weight:600;font-size:13px;color:#64748B;background:#fff;border:1.5px solid #CBD5E1;display:flex;align-items:center;justify-content:center;cursor:pointer;border-radius:14px;">
            ข้ามขั้นตอนนี้ (Skip for Now)
          </div>
        </div>

      </div>
      {hi()}
    </div>
    """

def s06_forgot_password():
    """06. Forgot Password & OTP Reset"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("รีเซ็ตรหัสผ่าน")}
      <div class="body" style="padding:0 24px 24px;gap:20px;">
        <div style="text-align:center;padding:20px 0 10px;">
          <div style="width:72px;height:72px;border-radius:24px;background:#EFF6FF;color:{C['blue']};margin:0 auto 16px;display:flex;align-items:center;justify-content:center;">
            {ic("lock", 34, C['blue'])}
          </div>
          <div class="h1" style="font-size:24px;">ลืมรหัสผ่าน?</div>
          <p class="p" style="margin-top:6px;font-size:13px;padding:0 12px;">
            กรอกอีเมลสถาบัน ระบบจะส่งรหัสยืนยัน OTP 6 หลักเพื่อตั้งรหัสผ่านใหม่
          </p>
        </div>

        {labeled("อีเมลมหาวิทยาลัย", field(USER['email'], icon="mail"))}
        {btn("ส่งรหัสยืนยัน OTP (Send OTP)", "bp", go="S04", icon="send")}

        <!-- Demo Success State Card -->
        <div class="card" style="background:#ECFDF5;border:1px solid #A7F3D0;display:flex;gap:12px;align-items:flex-start;">
          <div style="color:{C['green']};margin-top:2px;">{ic("check", 20, C['green'])}</div>
          <div>
            <div style="font-weight:700;font-size:13px;color:#065F46;">ระบบได้ส่งรหัส OTP ไปยังอีเมลแล้ว</div>
            <div style="font-size:12px;color:#047857;margin-top:2px;">กรุณาตรวจสอบกล่องข้อความที่ {USER['email']}</div>
          </div>
        </div>

        <div style="margin-top:auto;text-align:center;">
          <span class="link" data-go="S04">← กลับสู่หน้าเข้าสู่ระบบ</span>
        </div>
      </div>
      {hi()}
    </div>
    '''

def s07_home():
    """07. Home Dashboard (The central hub)"""
    return f"""
    <div class="scr">
      {sb()}
      <!-- Top App Bar -->
      <div class="bar" style="justify-content:space-between;padding:0 20px;">
        <div class="row" style="gap:12px;">
          <div class="ib" data-go="S08" style="background:#fff;border:1px solid #E5EAF2;cursor:pointer;">
            {ic("menu", 22, C['navy'])}
          </div>
          <div class="row" style="gap:10px;cursor:pointer;" data-go="S10">
            {avatar(44, ring=C['blue'])}
            <div style="text-align:left;">
              <div style="font-size:11px;color:#64748B;">ยินดีต้อนรับ 👋</div>
              <div style="font-weight:700;font-size:15px;color:{C['navy']};">{USER['th']}</div>
            </div>
          </div>
        </div>
        <div class="row" style="gap:8px;">
          <div class="ib" data-go="S09" style="cursor:pointer;position:relative;">
            {ic("bell", 20, C['navy'])}
            <span style="position:absolute;top:9px;right:9px;width:8px;height:8px;border-radius:50%;background:{C['red']};"></span>
          </div>
          <div class="ib" data-go="S11" style="cursor:pointer;background:#EFF6FF;border-color:#DBEAFE;color:{C['blue']};">
            {ic("qr", 20, C['blue'])}
          </div>
        </div>
      </div>

      <!-- Scrollable Dashboard Content -->
      <div class="body" style="padding:0 20px 120px;gap:14px;overflow-y:auto;">
        <!-- University Badge Strip -->
        <div class="row" style="justify-content:space-between;background:#fff;border:1px solid #E5EAF2;border-radius:14px;padding:10px 14px;">
          <div class="row" style="gap:10px;">
            {uni_seal("silpakorn", s=30)}
            <span style="font-size:12px;font-weight:700;color:{C['navy']};">{USER['uni']}</span>
            <span class="badge b-green" style="font-size:10px;height:20px;">{USER['fac']}</span>
          </div>
          <span class="link" style="font-size:11px;" data-go="S08">เมนู อว.</span>
        </div>

        <!-- Camplus Digital Wallet & Living Allowance Card (งบ 3,000 ฿/เดือน) -->
        <div class="card" style="background:linear-gradient(135deg,#0D1B3E 0%,#163268 50%,#246BFD 100%);color:#fff;border:none;box-shadow:0 12px 28px rgba(36,107,253,.28);padding:14px 16px;cursor:pointer;position:relative;overflow:hidden;" data-go="S29">
          <div style="position:absolute;right:-20px;top:-20px;width:100px;height:100px;border-radius:50%;background:radial-gradient(circle,rgba(88,214,255,0.2) 0%,transparent 70%);pointer-events:none;"></div>
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div class="row" style="gap:8px;">
              {ic("wallet", 18, C['cyan'])}
              <span style="font-size:12px;color:{C['cyan']};font-weight:700;letter-spacing:.5px;">CAMPLUS WALLET • ค่าครองชีพ</span>
            </div>
            <span class="badge b-green" style="font-size:10px;padding:2px 8px;">รับสิทธิ์ ฿3,000/ด.</span>
          </div>
          <div class="row" style="justify-content:space-between;align-items:flex-end;margin-top:10px;">
            <div>
              <div style="font-size:11px;color:#CBD5E1;">ยอดเงินคงเหลือใช้จ่ายในมอ</div>
              <div style="font:800 24px 'Inter';color:#fff;letter-spacing:.5px;">฿ 2,420.00</div>
            </div>
            <div class="row" style="gap:6px;">
              <div style="padding:6px 12px;border-radius:10px;background:rgba(255,255,255,0.18);backdrop-filter:blur(10px);font-size:11px;font-weight:700;color:#fff;display:flex;align-items:center;gap:4px;" data-go="S30">
                {ic("scan", 14, "#fff")} สแกนจ่าย
              </div>
            </div>
          </div>
        </div>

        <!-- Next Class Card -->
        <div class="card" style="border-left:4px solid {C['blue']};padding:14px 16px;cursor:pointer;" data-go="S13">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <span class="badge b-blue" style="font-size:10px;">วิชาถัดไป • 09:00 - 12:00 น.</span>
            <span style="font-size:11px;color:{C['blue']};font-weight:600;">อีก 25 นาที →</span>
          </div>
          <div style="font-weight:700;font-size:15px;color:{C['navy']};margin-top:6px;">462301 สื่อนวัตกรรมการเรียนรู้</div>
          <div class="row" style="gap:14px;margin-top:6px;font-size:12px;color:#64748B;">
            <span class="row" style="gap:4px;">{ic("pin", 14, C['blue'])} อาคารศึกษา 3 (ED-304)</span>
            <span class="row" style="gap:4px;">{ic("user", 14, "#64748B")} อ.ดร.กิตติศักดิ์</span>
          </div>
        </div>

        <!-- 8-Quick Action Grid -->
        <div class="sec"><span>บริการด่วนสำหรับนักศึกษา (Smart Actions)</span></div>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
          <!-- 1. Schedule -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S12">
            <div style="width:40px;height:40px;border-radius:12px;background:#EFF6FF;color:{C['blue']};margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("calendar", 20, C['blue'])}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">ตารางเรียน</div>
          </div>
          <!-- 2. Map -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S21">
            <div style="width:40px;height:40px;border-radius:12px;background:#F0FDF4;color:{C['green']};margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("map", 20, C['green'])}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">แผนที่ ม.</div>
          </div>
          <!-- 3. Room Booking -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S25">
            <div style="width:40px;height:40px;border-radius:12px;background:#FEF3C7;color:{C['amber']};margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("door", 20, C['amber'])}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">จองห้องติว</div>
          </div>
          <!-- 4. Fleet Rental -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S27">
            <div style="width:40px;height:40px;border-radius:12px;background:#F5F3FF;color:#7C3AED;margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("bike", 20, "#7C3AED")}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">ยืมรถ/ของ</div>
          </div>
          <!-- 5. Tuition -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S32">
            <div style="width:40px;height:40px;border-radius:12px;background:#FFF1F2;color:#E11D48;margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("receipt", 20, "#E11D48")}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">จ่ายค่าเทอม</div>
          </div>
          <!-- 6. Student Loan กยศ. -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S33">
            <div style="width:40px;height:40px;border-radius:12px;background:#ECFDF5;color:#059669;margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("shield", 20, "#059669")}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">ทุน กยศ.</div>
          </div>
          <!-- 7. Dormitory -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S35">
            <div style="width:40px;height:40px;border-radius:12px;background:#F1F5F9;color:{C['navy']};margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("bed", 20, C['navy'])}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">หอพักนักศึกษา</div>
          </div>
          <!-- 8. AI Copilot -->
          <div class="card" style="padding:10px 4px;text-align:center;cursor:pointer;" data-go="S38">
            <div style="width:40px;height:40px;border-radius:12px;background:#ECFEFF;color:{C['cyan']};margin:0 auto 4px;display:flex;align-items:center;justify-content:center;">
              {ic("bot", 20, "#0891B2")}
            </div>
            <div style="font-weight:700;font-size:11px;color:{C['navy']};">AI Copilot</div>
          </div>
        </div>

        <!-- Welfare & Community Highlights -->
        <div class="sec"><span>ชุมชนและการใช้ชีวิต (Campus Life & Social)</span></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <!-- Community Forum -->
          <div class="card" style="padding:12px;cursor:pointer;background:#fff;" data-go="S36">
            <div class="row" style="gap:8px;">
              <div style="width:32px;height:32px;border-radius:8px;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;">
                {ic("users", 16, C['blue'])}
              </div>
              <div style="font-weight:700;font-size:12px;color:{C['navy']};">กระดานชุมชน</div>
            </div>
            <div style="font-size:11px;color:#64748B;margin-top:6px;">กระทู้ถามตอบ ติวสอบ รีวิว</div>
          </div>
          <!-- Discord Matrix -->
          <div class="card" style="padding:12px;cursor:pointer;background:#fff;" data-go="S37">
            <div class="row" style="gap:8px;">
              <div style="width:32px;height:32px;border-radius:8px;background:#F5F3FF;color:#5865F2;display:flex;align-items:center;justify-content:center;">
                {ic("discord", 16, "#5865F2")}
              </div>
              <div style="font-weight:700;font-size:12px;color:{C['navy']};">Discord Lounge</div>
            </div>
            <div style="font-size:11px;color:#22C55E;margin-top:6px;">● กำลังคุยเสียง 4 คน</div>
          </div>
        </div>

        <!-- Volunteer Progress Bar Pill -->
        <div class="card" style="padding:12px 14px;background:#F0FDF4;border-color:#BBF7D0;cursor:pointer;" data-go="S34">
          <div class="row" style="justify-content:space-between;align-items:center;">
            <div class="row" style="gap:10px;">
              {ic("heart", 18, C['green'])}
              <div>
                <span style="font-weight:700;font-size:12px;color:#166534;">ชั่วโมงจิตอาสา กยศ.</span>
                <span style="font-size:11px;color:#64748B;"> (36/36 ชม.)</span>
              </div>
            </div>
            <span class="badge b-green" style="font-size:10px;">ครบ 100% →</span>
          </div>
        </div>

        <!-- Upcoming Deadlines -->
        <div>
          <div class="sec"><span>งานและกำหนดส่งสัปดาห์นี้</span><span class="link" data-go="S15">ดูปฏิทิน</span></div>
          <div class="card" style="margin-top:8px;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;" data-go="S15">
            <div class="row" style="gap:12px;">
              <div style="width:10px;height:10px;border-radius:50%;background:{C['red']};"></div>
              <div>
                <div style="font-weight:700;font-size:13px;color:{C['navy']};">ส่งรายงานโครงงานเทคโนโลยีการศึกษา</div>
                <div style="font-size:11px;color:#64748B;">ครบกำหนดวันนี้ 23:59 น. • วิชา 462301</div>
              </div>
            </div>
            <span class="badge b-red">Due Today</span>
          </div>
        </div>

        <!-- Featured News / Activities -->
        <div style="padding-bottom:100px;">
          <div class="sec"><span>ข่าวด่วน & กิจกรรมแนะนำ</span><span class="link" data-go="S18">ทั้งหมด</span></div>
          <div class="card" style="margin-top:8px;padding:0;overflow:hidden;cursor:pointer;" data-go="S19">
            <div style="width:100%;height:130px;background:#E2E8F0;">
              {img("event_hackathon.jpg", "width:100%;height:130px;object-fit:cover;")}
            </div>
            <div style="padding:12px 14px;">
              <div class="badge b-blue" style="font-size:10px;">เปิดรับสมัคร • เหลือ 15 ที่นั่ง</div>
              <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-top:6px;">ไทยศึกษา Smart Campus Hackathon 2026</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">ชิงทุนการศึกษา 150,000 บาท ณ หอสมุดกลาง</div>
            </div>
          </div>
        </div>
      </div>
      {nav(0, link=True)}
    </div>
    """

def s08_hamburger_drawer():
    """08. Hamburger Menu Drawer (Overlay on Home)"""
    menu_items = [
        ("wallet", "กระเป๋าเงินดิจิทัล & โครงการ Camplus", "S29", "฿ 2,420"),
        ("id", "บัตรประจำตัวนักศึกษาดิจิทัล", "S11", "เปิดบัตร"),
        ("calendar", "ตารางเรียนและตารางสอบ", "S12", ""),
        ("receipt", "ชำระค่าลงทะเบียน & ค่าเทอม", "S32", "ภาค 2/69"),
        ("shield", "ระบบกองทุนเงินกู้ยืม กยศ. ดิจิทัล", "S33", "อนุมัติ"),
        ("heart", "บันทึกชั่วโมงจิตอาสา (36 ชม.)", "S34", "ครบ 100%"),
        ("bed", "จัดการหอพัก & ค่าน้ำค่าไฟ", "S35", "รอชำระ"),
        ("bike", "ยืม-คืนยานพาหนะ & อุปกรณ์แล็บ", "S27", "ฟรี 2 ชม."),
        ("map", "แผนที่วิทยาเขต & รถรางไฟฟ้า", "S21", ""),
        ("door", "ระบบจองห้องติวและ Co-working", "S25", ""),
        ("users", "กระดานสนทนานักศึกษา (Community)", "S36", ""),
        ("discord", "ไทยศึกษา Discord Lounge", "S37", "สด 4 คน"),
        ("bot", "ไทยศึกษา AI Campus Copilot", "S38", "ใหม่"),
        ("file", "คำร้องออนไลน์ & เอกสารการศึกษา", "S28", "2 รายการ"),
        ("star", "กิจกรรมและชมรมของฉัน", "S18", ""),
        ("settings", "การตั้งค่าบัญชี & ความเป็นส่วนตัว", "S10", ""),
    ]
    menu_html = ""
    for icon_name, label, go_target, tag in menu_items:
        badge_html = f'<span class="badge b-blue" style="font-size:10px;">{tag}</span>' if tag else ""
        menu_html += f"""
        <div class="row" style="justify-content:space-between;padding:11px 0;cursor:pointer;border-bottom:1px solid #F1F5F9;" data-go="{go_target}">
          <div class="row" style="gap:14px;">
            <div style="width:34px;height:34px;border-radius:10px;background:#F8FAFC;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;color:{C['navy']};">
              {ic(icon_name, 18, C['navy'])}
            </div>
            <span style="font-size:14px;font-weight:600;color:{C['navy']};">{label}</span>
          </div>
          <div class="row" style="gap:8px;">
            {badge_html}
            {ic("right", 16, "#94A3B8")}
          </div>
        </div>
        """

    return f"""
    <div class="scr" style="background:rgba(16,28,54,0.55);">
      <!-- Underlying Screen Hint -->
      {screen_bg_hint()}
      <!-- Left Drawer Frame -->
      <div style="position:absolute;left:0;top:0;bottom:0;width:360px;background:#fff;display:flex;flex-direction:column;box-shadow:10px 0 40px rgba(0,0,0,0.3);z-index:50;">
        {sb()}
        <!-- Drawer Header -->
        <div style="background:linear-gradient(135deg,#101C36 0%,#1E293B 100%);padding:20px;color:#fff;">
          <div class="row" style="justify-content:space-between;">
            <div class="row" style="gap:10px;">
              {img("thai_suksa_logo.png", "width:34px;height:34px;border-radius:9px;object-fit:contain;box-shadow:0 3px 10px rgba(0,0,0,0.3);")}
              <span style="font:800 18px 'IBM Plex Sans Thai',Inter;color:#fff;letter-spacing:1px;">ไทยศึกษา</span>
            </div>
            <div class="ib" data-go="S07" style="width:32px;height:32px;border-radius:8px;background:rgba(255,255,255,0.1);border:none;color:#fff;cursor:pointer;">
              {ic("x", 18, "#fff")}
            </div>
          </div>

          <!-- User Card -->
          <div class="row" style="gap:14px;margin-top:16px;">
            {avatar(56, ring=C['cyan'])}
            <div>
              <div style="font-weight:700;font-size:16px;color:#fff;">{USER['th']}</div>
              <div style="font-size:12px;color:{C['cyan']};">{USER['sid']}</div>
              <div style="font-size:11px;color:#94A3B8;margin-top:2px;">{USER['fac']}</div>
            </div>
          </div>

          <!-- Active University & Switcher -->
          <div class="card" style="margin-top:14px;padding:8px 12px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:space-between;">
            <div class="row" style="gap:8px;">
              {uni_seal("silpakorn", s=26)}
              <span style="font-size:12px;color:#fff;font-weight:600;">{USER['uni']}</span>
            </div>
            <span class="link" style="color:{C['cyan']};font-size:11px;cursor:pointer;" data-go="S03">สลับสถาบัน</span>
          </div>
        </div>

        <!-- Menu List -->
        <div style="flex:1;overflow-y:auto;padding:10px 20px;">
          {menu_html}
        </div>

        <!-- Drawer Footer -->
        <div style="padding:16px 20px 30px;border-top:1px solid #E5EAF2;background:#F8FAFC;">
          <div class="row" style="justify-content:space-between;margin-bottom:12px;">
            <span style="font-size:12px;color:#64748B;">กระทรวงการอุดมศึกษาฯ (อว.)</span>
            <span class="badge b-blue" style="font-size:10px;">v3.0.0</span>
          </div>
          <div class="row" style="gap:8px;color:{C['red']};cursor:pointer;font-weight:600;font-size:13px;" data-go="S04">
            {ic("logout", 18, C['red'])}
            <span>ออกจากระบบ (Logout)</span>
          </div>
        </div>
      </div>
      {hi()}
    </div>
    """

def s09_notifications():
    """09. Notifications Center"""
    items = [
        ("📚", "เตือนตารางเรียน: สื่อนวัตกรรมการเรียนรู้", "วิชา 462301 กำลังจะเริ่มในอีก 20 นาที ณ อาคารศึกษา 3 ห้อง ED-304", "10 นาทีที่แล้ว", "b-blue", True),
        ("✅", "คำร้องขอหนังสือรับรองสถานภาพ ได้รับการอนุมัติแล้ว", "เจ้าหน้าที่สำนักทะเบียนได้ลงนามอิเล็กทรอนิกส์แล้ว ดาวน์โหลด PDF ได้ทันที", "1 ชม. ที่แล้ว", "b-green", True),
        ("🎉", "เปิดรับสมัคร: Smart Campus Hackathon 2026", "ชิงทุนการศึกษา 150,000 บาท สมัครได้ถึง 20 ต.ค. นี้", "เมื่อวานนี้", "b-amber", False),
        ("💳", "บัตรนักศึกษาดิจิทัลอัปเดตรหัสความปลอดภัยแล้ว", "QR Code สำหรับแตะเข้าหอสมุดกลางอัปเดตรอบใหม่", "2 วันที่แล้ว", "b-grey", False),
    ]
    cards = ""
    for emo, title, desc, time_str, badge_style, unread in items:
        dot = f'<span style="width:8px;height:8px;border-radius:50%;background:{C["blue"]};flex:none;"></span>' if unread else ""
        bg = "#F8FAFF" if unread else "#fff"
        cards += f'''
        <div class="card" style="padding:14px;background:{bg};display:flex;gap:12px;cursor:pointer;" data-go="S13">
          <div style="font-size:22px;margin-top:2px;">{emo}</div>
          <div style="flex:1;">
            <div class="row" style="justify-content:space-between;">
              <span style="font-weight:700;font-size:14px;color:{C['navy']};">{title}</span>
              {dot}
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;line-height:1.4;">{desc}</div>
            <div style="font-size:11px;color:#94A3B8;margin-top:6px;">{time_str}</div>
          </div>
        </div>
        '''

    return f'''
    <div class="scr">
      {sb()}
      {bar("การแจ้งเตือน", back=True, right=f'<span class="link" style="font-size:12px;">อ่านหมดแล้ว</span>')}
      <div class="body" style="padding:0 20px 24px;gap:12px;">
        <div class="chips">
          <div class="chip on">ทั้งหมด (4)</div>
          <div class="chip">การเรียน</div>
          <div class="chip">คำร้อง & อนุมัติ</div>
          <div class="chip">กิจกรรม</div>
          <div class="chip">ระบบ อว.</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:10px;overflow-y:auto;">
          {cards}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s10_profile():
    """10. Student Profile & Settings (Ultra-Luxury Institutional UX/UI)"""
    return f'''
    <div class="scr" style="background:#F5F7FB;">
      {sb()}
      {bar("ข้อมูลส่วนตัวนักศึกษา", back=True, back_target="S07", right=f'<div class="ib" data-go="S09" style="cursor:pointer;">{ic("bell", 20, C["navy"])}</div>')}
      
      <div class="body" style="padding:0 20px 120px;gap:16px;overflow-y:auto;">
        
        <!-- Master Profile Hero Card with Banner & Overlapping Centered Avatar -->
        <div class="card" style="padding:0;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 8px 24px rgba(16,28,54,0.06);border:1px solid #E2E8F0;">
          
          <!-- Institutional Gradient Banner Header -->
          <div style="height:96px;background:linear-gradient(135deg,#0A1E3F 0%,#132E5E 50%,#246BFD 100%);position:relative;padding:14px 18px;display:flex;align-items:flex-start;justify-content:space-between;">
            <div style="display:flex;align-items:center;gap:8px;">
              <div style="width:28px;height:28px;border-radius:8px;background:rgba(255,255,255,0.15);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;padding:2px;">
                {uni_seal("silpakorn", s=24)}
              </div>
              <span style="font-weight:700;font-size:12px;color:#fff;letter-spacing:.3px;">มหาวิทยาลัยศิลปากร</span>
            </div>
            <span class="badge" style="background:rgba(255,255,255,0.18);color:#fff;font-size:10px;padding:3px 10px;backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.25);">
              อว. PASSPORT
            </span>
          </div>

          <!-- Overlapping Centered Profile Photo & Details Container -->
          <div style="padding:0 20px 22px;text-align:center;position:relative;">
            
            <!-- Perfectly Centered Avatar with Glow & Badges -->
            <div style="margin-top:-50px;display:flex;justify-content:center;align-items:center;margin-bottom:12px;">
              <div style="position:relative;width:96px;height:96px;margin:0 auto;">
                
                <!-- Ambient Glow Ring -->
                <div style="position:absolute;inset:-3px;border-radius:50%;background:linear-gradient(135deg,#246BFD,#58D6FF);opacity:0.6;filter:blur(6px);"></div>
                
                <!-- Main Avatar Circle Frame -->
                <div style="position:relative;width:96px;height:96px;border-radius:50%;border:4px solid #FFFFFF;box-shadow:0 10px 25px rgba(16,28,54,0.18);overflow:hidden;background:#fff;display:flex;align-items:center;justify-content:center;">
                  {img("profile.jpg", "width:100%;height:100%;object-position:50% 20%;object-fit:cover;display:block;")}
                </div>

                <!-- Verified Checkmark Badge at bottom-right corner -->
                <div style="position:absolute;bottom:0px;right:0px;width:28px;height:28px;border-radius:50%;background:#10B981;border:2.5px solid #FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,0.15);" title="ยืนยันตัวตนเรียบร้อย">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
                </div>

                <!-- Camera / Edit Badge at top-right corner -->
                <div style="position:absolute;top:0px;right:-4px;width:26px;height:26px;border-radius:50%;background:#EFF6FF;border:2px solid #FFFFFF;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 6px rgba(0,0,0,0.1);cursor:pointer;" title="เปลี่ยนรูปโปรไฟล์">
                  {ic("camera", 13, C['blue'])}
                </div>

              </div>
            </div>

            <!-- Student Name -->
            <div style="font-weight:800;font-size:20px;color:{C['navy']};letter-spacing:.3px;">
              {USER['th_full']}
            </div>

            <!-- Student ID Pill with Copy Action -->
            <div style="display:inline-flex;align-items:center;gap:6px;background:#EFF6FF;border:1px solid #DBEAFE;border-radius:20px;padding:3px 12px;margin-top:6px;cursor:pointer;">
              <span style="font-size:12px;color:#64748B;">รหัสนักศึกษา:</span>
              <span style="font-family:monospace;font-weight:700;font-size:13px;color:{C['blue']};">{USER['sid']}</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="{C['blue']}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            </div>

            <!-- Faculty & Major Line -->
            <div style="font-size:13px;color:#475569;margin-top:8px;font-weight:500;">
              {USER['fac']} • {USER['major']}
            </div>

            <!-- Active Status Chip -->
            <div style="display:inline-flex;align-items:center;gap:6px;background:#ECFDF5;border:1px solid #A7F3D0;border-radius:20px;padding:3px 12px;margin-top:8px;">
              <div style="width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 6px #10B981;"></div>
              <span style="font-weight:600;font-size:11.5px;color:#065F46;">สถานะ: กำลังศึกษาปกติ (Active Student)</span>
            </div>

            <!-- 3 Modern KPI Stats Pills -->
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:16px;">
              
              <!-- Stat 1: Institution -->
              <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:16px;padding:10px 6px;">
                <div style="font-size:11px;color:#64748B;">สถาบัน</div>
                <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:2px;">{USER['uni_s']}</div>
                <div style="font-size:10px;color:#94A3B8;">สนามจันทร์</div>
              </div>

              <!-- Stat 2: Year -->
              <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:16px;padding:10px 6px;">
                <div style="font-size:11px;color:#64748B;">ระดับชั้นปี</div>
                <div style="font-weight:700;font-size:13px;color:{C['navy']};margin-top:2px;">{USER['year']}</div>
                <div style="font-size:10px;color:#94A3B8;">รหัส 67</div>
              </div>

              <!-- Stat 3: GPAX -->
              <div style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:16px;padding:10px 6px;">
                <div style="font-size:11px;color:#B45309;">เกรดเฉลี่ย</div>
                <div style="font-weight:800;font-size:14px;color:#B45309;margin-top:2px;">3.72</div>
                <div style="font-size:10px;color:#D97706;font-weight:600;">เกียรตินิยม</div>
              </div>

            </div>

          </div>

        </div>

        <!-- Digital Student ID Hero Card (Interactive Virtual Card Banner) -->
        <div class="card" data-go="S11" style="cursor:pointer;background:linear-gradient(135deg,#0F172A 0%,#1E293B 100%);color:#fff;padding:18px 20px;border-radius:22px;border:1.5px solid rgba(88,214,255,0.3);box-shadow:0 12px 30px rgba(15,23,42,0.22);display:flex;flex-direction:column;gap:12px;position:relative;overflow:hidden;">
          <div style="position:absolute;top:-20px;right:-20px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(36,107,253,0.3) 0%,rgba(0,0,0,0) 70%);pointer-events:none;"></div>
          
          <div style="display:flex;align-items:center;justify-content:space-between;position:relative;z-index:2;">
            <div class="row" style="gap:10px;">
              <!-- Hologram Chip Icon -->
              <div style="width:36px;height:26px;border-radius:6px;background:linear-gradient(135deg,#F59E0B,#D97706);border:1px solid rgba(255,255,255,0.4);display:flex;align-items:center;justify-content:center;">
                <div style="width:16px;height:12px;border:1px solid rgba(0,0,0,0.2);border-radius:2px;"></div>
              </div>
              <div>
                <div style="font-weight:700;font-size:13.5px;color:#F8FAFC;">บัตรนักศึกษาดิจิทัล (Digital ID)</div>
                <div style="font-size:11px;color:#94A3B8;">แตะเพื่อเปิดแสดงบัตรและบาร์โค้ดห้องสมุด</div>
              </div>
            </div>
            <!-- NFC Contactless Icon -->
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{C['cyan']}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0"/><path d="M4 6a9 9 0 0 1 16 0"/><path d="M8 10a3 3 0 0 1 6 0"/><line x1="12" y1="14" x2="12" y2="14.01"/></svg>
          </div>

          <!-- Bottom Card Preview Row -->
          <div style="display:flex;align-items:center;justify-content:space-between;position:relative;z-index:2;padding-top:8px;border-top:1px solid rgba(255,255,255,0.1);">
            <div style="font-family:monospace;font-size:13px;letter-spacing:1.5px;color:#E2E8F0;">
              •••• •••• •••• 0452
            </div>
            <div style="display:flex;align-items:center;gap:6px;color:{C['cyan']};font-size:12px;font-weight:700;">
              <span>เปิดบัตรสแกน</span>
              {ic("right", 14, C['cyan'])}
            </div>
          </div>
        </div>

        <!-- Academic Details Card (อว. Student Passport) -->
        <div class="card" style="padding:16px 18px;border-radius:22px;background:#fff;border:1px solid #E2E8F0;box-shadow:0 4px 16px rgba(16,28,54,0.04);">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;">
            <div style="font-weight:700;font-size:14.5px;color:{C['navy']};display:flex;align-items:center;gap:8px;">
              {ic("book", 18, C['blue'])}
              <span>ข้อมูลการศึกษา (Student Passport)</span>
            </div>
            <span class="badge b-blue" style="font-size:10px;padding:2px 8px;">อว. Verified</span>
          </div>

          <!-- Graduation Progress Bar -->
          <div style="background:#F8FAFC;border:1px solid #E2E8F0;border-radius:14px;padding:12px 14px;margin-bottom:14px;">
            <div style="display:flex;justify-content:space-between;font-size:12px;color:#475569;margin-bottom:6px;">
              <span>ความก้าวหน้าหลักสูตร:</span>
              <strong style="color:{C['blue']};">94 / 136 หน่วยกิต (69.1%)</strong>
            </div>
            <div style="width:100%;height:8px;border-radius:10px;background:#E2E8F0;overflow:hidden;">
              <div style="width:69.1%;height:100%;background:linear-gradient(90deg,#246BFD,#58D6FF);border-radius:10px;"></div>
            </div>
          </div>

          <div style="display:flex;flex-direction:column;gap:10px;font-size:13px;">
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#64748B;">วิทยาเขตศึกษา:</span>
              <span style="font-weight:600;color:{C['navy']};">{USER['campus']}</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#64748B;">อาจารย์ที่ปรึกษา:</span>
              <span style="font-weight:600;color:{C['navy']};">ผศ.ดร.กมลวรรณ สุขุมินทร์</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#64748B;">ชั่วโมงจิตอาสาสะสม:</span>
              <span style="font-weight:700;color:#16A34A;">36 / 36 ชั่วโมง (ครบตามเกณฑ์)</span>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:center;">
              <span style="color:#64748B;">สถานะกองทุน กยศ.:</span>
              <span style="font-weight:600;color:{C['navy']};">ผู้กู้ยืมต่อเนื่อง (ปกติ)</span>
            </div>
          </div>
        </div>

        <!-- Account Settings & Navigation List -->
        <div class="card" style="padding:4px 18px;border-radius:22px;background:#fff;border:1px solid #E2E8F0;box-shadow:0 4px 16px rgba(16,28,54,0.04);">
          
          <!-- Switch University -->
          <div class="row" style="justify-content:space-between;padding:14px 0;border-bottom:1px solid #F1F5F9;cursor:pointer;" data-go="S03">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#EFF6FF;display:flex;align-items:center;justify-content:center;color:{C['blue']};">
                {ic("building", 18, C['blue'])}
              </div>
              <div>
                <div style="font-size:13.5px;font-weight:600;color:{C['navy']};">สลับสถาบันการศึกษา (Switch University)</div>
                <div style="font-size:11px;color:#64748B;">ปัจจุบัน: มหาวิทยาลัยศิลปากร (SU)</div>
              </div>
            </div>
            {ic("right", 16, "#94A3B8")}
          </div>

          <!-- Linked Platforms -->
          <div class="row" style="justify-content:space-between;padding:14px 0;border-bottom:1px solid #F1F5F9;cursor:pointer;" data-go="S05B">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#ECFDF5;display:flex;align-items:center;justify-content:center;color:#10B981;">
                {ic("shield", 18, "#10B981")}
              </div>
              <div>
                <div style="font-size:13.5px;font-weight:600;color:{C['navy']};">บัญชีและแพลตฟอร์มที่เชื่อมต่อ</div>
                <div style="font-size:11px;color:#64748B;">ThaID, Google, SU-NET SSO</div>
              </div>
            </div>
            <span class="badge b-green" style="font-size:10px;">ผูกแล้ว</span>
          </div>

          <!-- Language -->
          <div class="row" style="justify-content:space-between;padding:14px 0;border-bottom:1px solid #F1F5F9;">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#F8FAFC;display:flex;align-items:center;justify-content:center;color:#64748B;">
                {ic("globe", 18, "#64748B")}
              </div>
              <span style="font-size:13.5px;font-weight:600;color:{C['navy']};">ภาษาของแอปพลิเคชัน (Language)</span>
            </div>
            <span class="badge b-blue" style="font-size:11px;font-weight:600;">ไทย (TH)</span>
          </div>

          <!-- Notification Settings -->
          <div class="row" style="justify-content:space-between;padding:14px 0;border-bottom:1px solid #F1F5F9;cursor:pointer;" data-go="S09">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#FFFBEB;display:flex;align-items:center;justify-content:center;color:#D97706;">
                {ic("bell", 18, "#D97706")}
              </div>
              <span style="font-size:13.5px;font-weight:600;color:{C['navy']};">การตั้งค่าการแจ้งเตือน (Notifications)</span>
            </div>
            {ic("right", 16, "#94A3B8")}
          </div>

          <!-- Log Out -->
          <div class="row" style="justify-content:space-between;padding:14px 0;cursor:pointer;color:{C['red']};" data-go="S04">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#FEF2F2;display:flex;align-items:center;justify-content:center;color:{C['red']};">
                {ic("logout", 18, C['red'])}
              </div>
              <span style="font-size:13.5px;font-weight:700;">ออกจากระบบ (Log Out)</span>
            </div>
            {ic("right", 16, C['red'])}
          </div>

        </div>

      </div>
      {nav(4, link=True)}
    </div>
    '''

def s11_digital_id():
    """11. Digital Student ID (Official Silpakorn / National Student Pass)"""
    return f'''
    <div class="scr" style="background:#0F172A;color:#fff;">
      {sb(dark=True)}
      {bar("บัตรประจำตัวนักศึกษา", back=True, right='<span class="badge b-green">Active</span>')}
      <div class="body" style="padding:0 24px 30px;justify-content:space-between;text-align:center;">
        <div style="font-size:12px;color:{C['cyan']};letter-spacing:1px;font-weight:600;">
          กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม (อว.)
        </div>

        <!-- Realistic Smart Card -->
        <div style="background:linear-gradient(135deg,#1E293B 0%,#0F172A 100%);border:1.5px solid rgba(88,214,255,0.4);border-radius:28px;padding:24px;text-align:left;position:relative;box-shadow:0 25px 60px rgba(0,0,0,0.6);">
          <div class="row" style="justify-content:space-between;">
            <div class="row" style="gap:10px;">
              {uni("SU", "#0F7F59", s=36, r=10, fs=13)}
              <div>
                <div style="font-weight:800;font-size:15px;color:#fff;">{USER['uni']}</div>
                <div style="font-size:11px;color:{C['cyan']};">{USER['uni_en']}</div>
              </div>
            </div>
            {img("thai_suksa_logo.png", "width:38px;height:38px;border-radius:10px;object-fit:contain;box-shadow:0 4px 12px rgba(0,0,0,0.4);")}
          </div>

          <div class="row" style="gap:18px;margin-top:22px;">
            <div style="width:84px;height:108px;border-radius:16px;overflow:hidden;border:2.5px solid {C['cyan']};box-shadow:0 6px 18px rgba(0,0,0,0.4);flex:none;">
              {img("profile.jpg", "width:100%;height:100%;object-fit:cover;object-position:50% 25%;")}
            </div>
            <div>
              <div style="font-size:17px;font-weight:800;color:#fff;">{USER['th_full']}</div>
              <div style="font-size:13px;color:#CBD5E1;margin-top:1px;">{USER['en']}</div>
              <div style="font:700 15px Inter;color:{C['cyan']};margin-top:6px;">{USER['sid']}</div>
              <div style="font-size:12px;color:#94A3B8;margin-top:2px;">{USER['fac']}</div>
              <div style="font-size:11px;color:#94A3B8;">{USER['major']}</div>
            </div>
          </div>

          <div class="row" style="justify-content:space-between;margin-top:22px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.1);font-size:11px;color:#94A3B8;">
            <span>ออกบัตร: 08/2567</span>
            <span>หมดอายุ: 31 พ.ค. 2571</span>
            <span style="color:{C['green']};font-weight:700;">● ปกติ (ACTIVE)</span>
          </div>
        </div>

        <!-- Dynamic Security QR Code Card -->
        <div style="background:#fff;border-radius:24px;padding:20px;color:{C['navy']};box-shadow:0 12px 30px rgba(0,0,0,0.3);">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};">สแกนเข้าหอสมุด / ประตูอาคารเรียน</div>
          <div style="margin:14px auto 8px;display:flex;justify-content:center;">
            {qr_svg(160, seed=USER['sid'])}
          </div>
          <div class="row" style="justify-content:center;gap:6px;font-size:12px;color:#64748B;">
            {ic("refresh", 14, C['blue'])} รหัสอัปเดตอัตโนมัติทุก 30 วินาที
          </div>
        </div>

        {btn("แสดงแบบเต็มจอ / เพิ่มลง Apple Wallet", "bp", go="S07", icon="qr")}
      </div>
      {hi(dark=True)}
    </div>
    '''

def s12_schedule():
    """12. Weekly Schedule Timetable"""
    classes = [
        ("09:00 - 12:00 น.", "462301 สื่อนวัตกรรมการเรียนรู้", "อาคารศึกษา 3 ห้อง ED-304", "อ.ดร.กมลวรรณ", "b-blue", True),
        ("13:00 - 16:00 น.", "462303 การออกแบบกราฟิกเพื่อการศึกษา", "อาคารศูนย์คอมพิวเตอร์ Lab 2", "ผศ.วิภาดา", "b-green", False),
        ("16:30 - 18:30 น.", "01204213 ขั้นตอนวิธีและการเขียนโปรแกรม", "อาคารเรียนรวม SC ห้อง 2101", "ผศ.ดร.สมชาย", "b-amber", False),
    ]
    cards = ""
    for time_str, name, room, inst, col, active in classes:
        border_col = C['blue'] if active else C['line']
        cards += f'''
        <div class="card" style="padding:14px 16px;border-left:5px solid {C['blue'] if col=='b-blue' else (C['green'] if col=='b-green' else C['amber'])};cursor:pointer;" data-go="S13">
          <div class="row" style="justify-content:space-between;">
            <span class="badge {col}">{time_str}</span>
            <span style="font-size:12px;color:#64748B;">3 หน่วยกิต</span>
          </div>
          <div style="font-weight:700;font-size:15px;color:{C['navy']};margin-top:8px;">{name}</div>
          <div class="row" style="justify-content:space-between;margin-top:10px;font-size:12px;color:#64748B;">
            <span class="row" style="gap:6px;">{ic("pin", 14, C['blue'])} {room}</span>
            <span class="row" style="gap:6px;">{ic("user", 14, C['blue'])} {inst}</span>
          </div>
        </div>
        '''

    return f'''
    <div class="scr">
      {sb()}
      <div class="bar">
        <div class="ib" data-go="S07">{ic("left")}</div>
        <div class="ttl">ตารางเรียนและตารางสอบ</div>
        <div class="ib" data-go="S15">{ic("calendar")}</div>
      </div>
      <div class="body" style="padding:0 20px;gap:14px;">
        <!-- Day / Exam Switcher -->
        <div class="seg">
          <div class="on">ตารางเรียนรายสัปดาห์</div>
          <div data-go="S14">ตารางสอบกลางภาค/ปลายภาค</div>
        </div>

        <!-- Horizontal Week Strip -->
        <div style="display:flex;gap:8px;overflow-x:auto;">
          <div class="card" style="flex:1;text-align:center;padding:10px 4px;background:{C['blue']};color:#fff;border-color:{C['blue']};">
            <div style="font-size:11px;opacity:.9;">จันทร์</div>
            <div style="font:700 17px Inter;margin-top:2px;">12</div>
            <div style="font-size:9px;opacity:.8;margin-top:2px;">● 3 วิชา</div>
          </div>
          <div class="card" style="flex:1;text-align:center;padding:10px 4px;">
            <div style="font-size:11px;color:#64748B;">อังคาร</div>
            <div style="font:700 17px Inter;margin-top:2px;">13</div>
            <div style="font-size:9px;color:#94A3B8;margin-top:2px;">2 วิชา</div>
          </div>
          <div class="card" style="flex:1;text-align:center;padding:10px 4px;">
            <div style="font-size:11px;color:#64748B;">พุธ</div>
            <div style="font:700 17px Inter;margin-top:2px;">14</div>
            <div style="font-size:9px;color:#94A3B8;margin-top:2px;">1 วิชา</div>
          </div>
          <div class="card" style="flex:1;text-align:center;padding:10px 4px;">
            <div style="font-size:11px;color:#64748B;">พฤหัส</div>
            <div style="font:700 17px Inter;margin-top:2px;">15</div>
            <div style="font-size:9px;color:#94A3B8;margin-top:2px;">2 วิชา</div>
          </div>
          <div class="card" style="flex:1;text-align:center;padding:10px 4px;">
            <div style="font-size:11px;color:#64748B;">ศุกร์</div>
            <div style="font:700 17px Inter;margin-top:2px;">16</div>
            <div style="font-size:9px;color:#94A3B8;margin-top:2px;">ว่าง</div>
          </div>
        </div>

        <!-- Class Cards -->
        <div style="display:flex;flex-direction:column;gap:12px;overflow-y:auto;padding-bottom:100px;">
          {cards}
        </div>
      </div>
      {nav(1, link=True)}
    </div>
    '''

def s13_class_details():
    """13. Class Details Modal / Sheet"""
    return f'''
    <div class="scr" style="background:rgba(16,28,54,0.5);">
      {screen_bg_hint()}
      <div class="sheet" style="height:620px;">
        <div class="handle"></div>
        <div class="row" style="justify-content:space-between;margin-top:4px;">
          <span class="badge b-blue">วิชาเอกบังคับ • 3 หน่วยกิต</span>
          <div class="ib" data-go="S12" style="width:32px;height:32px;cursor:pointer;">{ic("x", 18)}</div>
        </div>

        <div>
          <div class="h1" style="font-size:22px;color:{C['navy']};">462301 สื่อนวัตกรรมการเรียนรู้</div>
          <div style="font-size:13px;color:#64748B;margin-top:2px;">Educational Media and Technology Innovation</div>
        </div>

        <div class="card" style="background:#F8FAFC;padding:14px;display:flex;flex-direction:column;gap:10px;font-size:13px;">
          <div class="row" style="justify-content:space-between;">
            <span style="color:#64748B;">เวลาเรียน:</span>
            <span style="font-weight:700;color:{C['navy']};">วันจันทร์ 09:00 - 12:00 น.</span>
          </div>
          <div class="row" style="justify-content:space-between;">
            <span style="color:#64748B;">สถานที่:</span>
            <span style="font-weight:700;color:{C['blue']};">อาคารศึกษา 3 ห้อง ED-304 (ชั้น 3)</span>
          </div>
          <div class="row" style="justify-content:space-between;">
            <span style="color:#64748B;">อาจารย์ผู้สอน:</span>
            <span style="font-weight:700;color:{C['navy']};">ผศ.ดร.กมลวรรณ สุขุมินทร์</span>
          </div>
          <div class="row" style="justify-content:space-between;">
            <span style="color:#64748B;">คณะที่เปิดสอน:</span>
            <span style="font-weight:600;">{USER['fac']} ม.ศิลปากร</span>
          </div>
        </div>

        <div class="row" style="gap:10px;">
          {btn("นำทางไปยังห้อง ED-304", "bp", go="S23", icon="nav", style="flex:1;")}
          {btn("เพิ่มแจ้งเตือน", "bs", go="S15", icon="clock", style="flex:1;")}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s14_exam_schedule():
    """14. Exam Schedule"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ตารางสอบกลางภาค / ปลายภาค")}
      <div class="body" style="padding:0 20px 24px;gap:14px;">
        <div class="seg">
          <div data-go="S12">ตารางเรียน</div>
          <div class="on">ตารางสอบ (Exams)</div>
        </div>

        <!-- Exam Countdown Hero -->
        <div class="card" style="background:linear-gradient(135deg,#DC2626,#991B1B);color:#fff;border:none;">
          <div class="badge" style="background:rgba(255,255,255,0.2);color:#fff;">สอบวิชาถัดไป</div>
          <div style="font:800 28px Inter;margin-top:8px;">อีก 4 วัน 16 ชั่วโมง</div>
          <div style="font-size:13px;opacity:.9;margin-top:2px;">462301 สื่อนวัตกรรมการเรียนรู้ • กลางภาค</div>
        </div>

        <div class="sec"><span>กำหนดการสอบภาคเรียนที่ 1/2569</span></div>
        <div style="display:flex;flex-direction:column;gap:10px;overflow-y:auto;">
          <div class="card" style="padding:14px;">
            <div class="row" style="justify-content:space-between;">
              <span class="badge b-red">19 ต.ค. 2569 • 09:00 - 12:00</span>
              <span class="badge b-amber">ที่นั่ง A-24</span>
            </div>
            <div style="font-weight:700;font-size:15px;color:{C['navy']};margin-top:8px;">462301 สื่อนวัตกรรมการเรียนรู้</div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;">ห้องสอบ ED-304 อาคารศึกษา 3</div>
          </div>

          <div class="card" style="padding:14px;">
            <div class="row" style="justify-content:space-between;">
              <span class="badge b-blue">22 ต.ค. 2569 • 13:00 - 16:00</span>
              <span class="badge b-grey">ที่นั่ง B-12</span>
            </div>
            <div style="font-weight:700;font-size:15px;color:{C['navy']};margin-top:8px;">462303 การออกแบบกราฟิกเพื่อการศึกษา</div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;">ห้องสอบ Lab 2 ศูนย์คอมพิวเตอร์</div>
          </div>
        </div>
      </div>
      {hi()}
    </div>
    '''

def s15_calendar():
    """15. Calendar & Add Event Modal"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ปฏิทินและบันทึกกิจกรรม", right='<div class="ib" data-go="S12">' + ic("calendar") + '</div>')}
      <div class="body" style="padding:0 20px 24px;gap:14px;">
        <!-- Calendar Widget -->
        <div class="card" style="padding:16px;">
          <div class="row" style="justify-content:space-between;margin-bottom:12px;">
            <span style="font-weight:700;font-size:16px;color:{C['navy']};">ตุลาคม 2569</span>
            <div class="row" style="gap:6px;">
              <div class="ib" style="width:32px;height:32px;">{ic("left", 14)}</div>
              <div class="ib" style="width:32px;height:32px;">{ic("right", 14)}</div>
            </div>
          </div>
          <!-- Days of week -->
          <div style="display:grid;grid-template-columns:repeat(7,1fr);text-align:center;font-size:12px;font-weight:600;color:#94A3B8;margin-bottom:8px;">
            <span>อา</span><span>จ</span><span>อ</span><span>พ</span><span>พฤ</span><span>ศ</span><span>ส</span>
          </div>
          <!-- Sample Grid -->
          <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center;font:600 13px Inter;">
            <span style="color:#CBD5E1;padding:8px 0;">28</span><span style="color:#CBD5E1;padding:8px 0;">29</span><span style="color:#CBD5E1;padding:8px 0;">30</span>
            <span style="padding:8px 0;">1</span><span style="padding:8px 0;">2</span><span style="padding:8px 0;">3</span><span style="padding:8px 0;">4</span>
            <span style="padding:8px 0;">5</span><span style="padding:8px 0;">6</span><span style="padding:8px 0;">7</span><span style="padding:8px 0;">8</span><span style="padding:8px 0;">9</span><span style="padding:8px 0;">10</span><span style="padding:8px 0;">11</span>
            <span style="padding:8px 0;background:{C['blue']};color:#fff;border-radius:10px;">12</span>
            <span style="padding:8px 0;">13</span><span style="padding:8px 0;">14</span><span style="padding:8px 0;">15</span><span style="padding:8px 0;">16</span><span style="padding:8px 0;">17</span><span style="padding:8px 0;">18</span>
          </div>
        </div>

        <div class="sec"><span>กำหนดการวันที่ 12 ต.ค.</span><span class="badge b-blue">+ เพิ่มนัดหมาย</span></div>
        <div style="display:flex;flex-direction:column;gap:8px;">
          <div class="card" style="padding:12px 14px;border-left:4px solid {C['blue']};">
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">09:00 - 12:00 | เรียนวิชาสื่อนวัตกรรม ED-304</div>
            <div style="font-size:11px;color:#64748B;">คณะศึกษาศาสตร์ ม.ศิลปากร</div>
          </div>
          <div class="card" style="padding:12px 14px;border-left:4px solid {C['amber']};">
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">14:00 - 16:00 | นัดติวกลุ่มโครงงานเทคโนฯ</div>
            <div style="font-size:11px;color:#64748B;">ห้องติวกลุ่ม 4B หอสมุดกลาง</div>
          </div>
        </div>
      </div>
      {hi()}
    </div>
    '''

def s16_news_feed():
    """16. News Feed"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ข่าวสาร & ประกาศสถาบัน")}
      <div class="body" style="padding:0 20px;gap:12px;overflow-y:auto;">
        {field("ค้นหาข่าวสาร หรือประกาศด่วน...", icon="search")}
        <div class="chips">
          <div class="chip on">ทั้งหมด</div>
          <div class="chip">ข่าวสถาบัน (SU)</div>
          <div class="chip">ทุนการศึกษา อว.</div>
          <div class="chip">วิชาการ & วิจัย</div>
        </div>

        <!-- Featured Card -->
        <div class="card" style="padding:0;overflow:hidden;cursor:pointer;" data-go="S17">
          <div style="width:100%;height:160px;background:#E2E8F0;">
            {img("news_banner.jpg", "width:100%;height:160px;object-fit:cover;")}
          </div>
          <div style="padding:14px;">
            <div class="row" style="justify-content:space-between;">
              <span class="badge b-blue">ประกาศทางการ • อว.</span>
              <span style="font-size:11px;color:#94A3B8;">10 ต.ค. 2569</span>
            </div>
            <div style="font-weight:700;font-size:15px;color:{C['navy']};margin-top:6px;">
              เปิดรับสมัครทุนวิจัยและนวัตกรรมดิจิทัลสำหรับนักศึกษา ประจำปี 2569
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;">
              กระทรวง อว. จัดสรรทุนสนับสนุนโครงการพัฒนานวัตกรรมอัจฉริยะ สูงสุดโครงการละ 50,000 บาท
            </div>
          </div>
        </div>
      </div>
      {nav(0, link=True)}
    </div>
    '''

def s17_news_details():
    """17. News Details"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("รายละเอียดข่าวสาร", back=True, right='<div class="ib">' + ic("share") + '</div>')}
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        <div style="width:100%;height:200px;border-radius:20px;overflow:hidden;background:#E2E8F0;">
          {img("news_banner.jpg", "width:100%;height:200px;object-fit:cover;")}
        </div>
        <div>
          <span class="badge b-blue">สำนักส่งเสริมและบริการวิชาการ • อว.</span>
          <div class="h1" style="font-size:22px;color:{C['navy']};margin-top:8px;line-height:1.35;">
            เปิดรับสมัครทุนวิจัยและนวัตกรรมดิจิทัลสำหรับนักศึกษา ประจำปี 2569
          </div>
          <div style="font-size:12px;color:#94A3B8;margin-top:6px;">เผยแพร่เมื่อ 10 ต.ค. 2569 • มีผู้เข้าชม 1,420 ครั้ง</div>
        </div>
        <p class="p" style="font-size:14px;color:#334155;line-height:1.7;">
          กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม ร่วมกับสถาบันอุดมศึกษาทั่วประเทศ เปิดรับข้อเสนอโครงการพัฒนานวัตกรรมดิจิทัลและแอปพลิเคชันเพื่อชุมชน นิสิตนักศึกษาสามารถส่งโครงงานร่วมกันข้ามสถาบันได้ โดยส่งเอกสารผ่านระบบ ไทยศึกษา ภายใน 30 พ.ย. 2569
        </p>
        <div class="card" style="background:#F8FAFC;padding:12px 14px;">
          <div style="font-weight:700;font-size:13px;color:{C['navy']};">เอกสารแนบดาวน์โหลด:</div>
          <div class="row" style="gap:8px;margin-top:6px;color:{C['blue']};font-size:12px;font-weight:600;">
            {ic("file", 16, C['blue'])} ประกาศทุนวิจัย_2569.pdf (1.4 MB)
          </div>
        </div>
        {btn("แชร์ข่าวสารนี้ (Share)", "bp", go="S16", icon="share")}
      </div>
      {hi()}
    </div>
    '''

def s18_activities():
    """18. Activities & Clubs Directory"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("กิจกรรมและชมรม")}
      <div class="body" style="padding:0 20px;gap:12px;overflow-y:auto;">
        {field("ค้นหากิจกรรม, เวิร์กช็อป, ชั่วโมงจิตอาสา...", icon="search")}
        <div class="chips">
          <div class="chip on">ทั้งหมด</div>
          <div class="chip">เวิร์กช็อป & แข่งขัน</div>
          <div class="chip">ชั่วโมงกิจกรรม</div>
          <div class="chip">กีฬา & นันทนาการ</div>
        </div>

        <!-- Featured Activity Card -->
        <div class="card" style="padding:0;overflow:hidden;cursor:pointer;" data-go="S19">
          <div style="width:100%;height:150px;background:#E2E8F0;">
            {img("event_hackathon.jpg", "width:100%;height:150px;object-fit:cover;")}
          </div>
          <div style="padding:14px;">
            <div class="row" style="justify-content:space-between;">
              <span class="badge b-green">สะสม 6 ชั่วโมงกิจกรรม</span>
              <span style="font-size:11px;color:{C['red']};font-weight:700;">เหลือ 15 ที่นั่ง!</span>
            </div>
            <div style="font-weight:700;font-size:16px;color:{C['navy']};margin-top:6px;">ไทยศึกษา Smart Campus Hackathon 2026</div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;">
              25 ต.ค. 2569 • 09:00 - 18:00 น. ณ Co-working ชั้น 2 หอสมุดกลาง
            </div>
          </div>
        </div>
      </div>
      {nav(3, link=True)}
    </div>
    '''

def s19_activity_details():
    """19. Activity Details"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("รายละเอียดกิจกรรม", back=True)}
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        <div style="width:100%;height:200px;border-radius:20px;overflow:hidden;background:#E2E8F0;">
          {img("event_hackathon.jpg", "width:100%;height:200px;object-fit:cover;")}
        </div>
        <div>
          <span class="badge b-green">ได้รับชั่วโมงกิจกรรมพัฒนานักศึกษา 6 ชม.</span>
          <div class="h1" style="font-size:22px;color:{C['navy']};margin-top:8px;">
            ไทยศึกษา Smart Campus Hackathon 2026
          </div>
          <div style="font-size:13px;color:#64748B;margin-top:4px;">จัดโดย สภานิสิตนักศึกษา ร่วมกับ กระทรวง อว.</div>
        </div>

        <div class="card" style="background:#F8FAFC;padding:14px;display:flex;flex-direction:column;gap:8px;font-size:13px;">
          <div>📅 วันที่: 25 ตุลาคม 2569 (09:00 - 18:00 น.)</div>
          <div>📍 สถานที่: Co-working Space หอสมุดกลาง ชั้น 2 ม.ศิลปากร</div>
          <div>👥 จำนวนที่รับ: 50 คน (คงเหลือ 15 ที่นั่ง)</div>
          <div>🏆 รางวัล: ทุนการศึกษาและใบประกาศนียบัตรรับรองจาก อว.</div>
        </div>

        {btn("ลงทะเบียนเข้าร่วมกิจกรรม (Register Now)", "bp", go="S20", icon="check")}
      </div>
      {hi()}
    </div>
    '''

def s20_registration_confirm():
    """20. Registration Confirmation Modal (Center Dialog)"""
    return f'''
    <div class="scr" style="background:rgba(16,28,54,0.55);">
      {screen_bg_hint()}
      <div class="modal" style="top:220px;">
        <div style="width:72px;height:72px;border-radius:50%;background:#ECFDF5;color:{C['green']};display:flex;align-items:center;justify-content:center;margin:0 auto;">
          {ic("check", 36, C['green'])}
        </div>
        <div class="h1" style="font-size:22px;color:{C['navy']};">ลงทะเบียนสำเร็จ!</div>
        <div style="font-size:13px;color:#64748B;">รหัสบัตรกิจกรรม: #TS-2569-8812</div>

        <div class="card" style="background:#F8FAFC;text-align:left;width:100%;padding:12px;font-size:12px;margin:8px 0;">
          <div style="font-weight:700;color:{C['navy']};">ไทยศึกษา Hackathon 2026</div>
          <div style="color:#64748B;margin-top:2px;">ผู้เข้าร่วม: {USER['th_full']}</div>
          <div style="color:#64748B;">25 ต.ค. 2569 • Co-working ชั้น 2 หอสมุดกลาง</div>
        </div>

        <div style="display:flex;flex-direction:column;gap:8px;width:100%;">
          {btn("บันทึกลงปฏิทินส่วนตัว (Add to Calendar)", "bp", go="S15", icon="calendar")}
          {btn("กลับสู่หน้ารวมกิจกรรม", "bs", go="S18")}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s21_campus_map():
    """21. Campus Map & Navigation Overview"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("แผนที่วิทยาเขต & สถานที่", right='<div class="ib" data-go="S24">' + ic("bus") + '</div>')}
      <div class="body" style="padding:0 20px;gap:12px;">
        {field("ค้นหาอาคารเรียน, โรงอาหาร, จุดจอดรถ...", icon="search")}
        <div class="chips">
          <div class="chip on">ทั้งหมด</div>
          <div class="chip">อาคารเรียน</div>
          <div class="chip">โรงอาหาร & ร้านค้า</div>
          <div class="chip">หอสมุดกลาง</div>
          <div class="chip">ป้ายรถราง EV</div>
        </div>

        <!-- Campus Map Canvas -->
        <div style="flex:1;border-radius:24px;overflow:hidden;position:relative;border:1px solid #E2E8F0;background:#E5E7EB;cursor:pointer;" data-go="S22">
          {img("campus_map.jpg", "width:100%;height:100%;object-fit:cover;")}
          <!-- Pin on Map -->
          <div style="position:absolute;top:40%;left:48%;transform:translate(-50%,-100%);text-align:center;">
            <div style="background:{C['navy']};color:#fff;padding:4px 10px;border-radius:12px;font-size:11px;font-weight:700;box-shadow:0 4px 12px rgba(0,0,0,0.3);white-space:nowrap;">
              📍 อาคารศูนย์เรียนรวม SC
            </div>
            <div style="width:14px;height:14px;background:{C['blue']};border:3px solid #fff;border-radius:50%;margin:2px auto 0;"></div>
          </div>

          <div style="position:absolute;bottom:16px;right:16px;background:#fff;border-radius:14px;padding:8px 12px;box-shadow:0 4px 12px rgba(0,0,0,0.15);font-size:12px;font-weight:600;" data-go="S24">
            🚌 รถรางสายสีเขียว (อีก 3 นาที)
          </div>
        </div>

        <!-- Selected Location Preview Drawer -->
        <div class="card" style="padding:14px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;" data-go="S22">
          <div>
            <div style="font-weight:700;font-size:15px;color:{C['navy']};">อาคารศูนย์เรียนรวม SC</div>
            <div style="font-size:12px;color:#64748B;">ห่างจากคุณ 320 เมตร • เดินประมาณ 4 นาที</div>
          </div>
          {btn("ดูรายละเอียด", "bp", go="S22", style="height:40px;font-size:13px;padding:0 14px;")}
        </div>
      </div>
      {nav(2, link=True)}
    </div>
    '''

def s22_place_details():
    """22. Place & Building Details"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("รายละเอียดอาคาร", back=True, right='<div class="ib">' + ic("bookmark") + '</div>')}
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        <div style="width:100%;height:200px;border-radius:20px;overflow:hidden;background:#E2E8F0;">
          {img("building.jpg", "width:100%;height:200px;object-fit:cover;")}
        </div>
        <div>
          <div class="row" style="justify-content:space-between;">
            <div class="h1" style="font-size:22px;color:{C['navy']};">อาคารศูนย์เรียนรวม (SC Building)</div>
            <span class="badge b-green">เปิดบริการ</span>
          </div>
          <div style="font-size:12px;color:#64748B;margin-top:2px;">{USER['uni']} • พระราชวังสนามจันทร์</div>
        </div>

        <div class="card" style="background:#F8FAFC;padding:14px;display:flex;flex-direction:column;gap:8px;font-size:13px;">
          <div>🕒 เวลาเปิดทำการ: จันทร์ - ศุกร์ (07:30 - 20:30 น.)</div>
          <div>📶 สิ่งอำนวยความสะดวก: Wi-Fi อว., ทางลาดผู้พิการ, ลิฟต์โดยสาร 4 ตัว</div>
          <div>🏢 ข้อมูลชั้น: ชั้น 1 โรงอาหารกลาง • ชั้น 2-3 ห้องบรรยาย SC-201 ถึง 310</div>
        </div>

        <div class="row" style="gap:10px;">
          {btn("นำทางไปยังตึกนี้ (Directions)", "bp", go="S23", icon="nav", style="flex:1;")}
          {btn("ดูตารางรถรางผ่านตึกนี้", "bs", go="S24", icon="bus", style="flex:1;")}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s23_directions():
    """23. Step-by-Step Directions"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("เส้นทางการเดินทาง", back=True)}
      <div class="body" style="padding:0 20px 24px;gap:14px;">
        <div class="card" style="padding:14px;background:#F8FAFC;">
          <div class="row" style="gap:10px;"><span style="color:{C['green']};">🟢</span><span style="font-size:13px;">จุดเริ่มต้น: หน้าหอสมุดกลาง ม.ศิลปากร</span></div>
          <div style="height:14px;border-left:2px dashed #CBD5E1;margin-left:8px;"></div>
          <div class="row" style="gap:10px;"><span style="color:{C['red']};">🔴</span><span style="font-size:13px;font-weight:700;">ปลายทาง: อาคารเรียนรวม SC (ห้อง 2101)</span></div>
        </div>

        <div class="row" style="gap:10px;">
          <div class="btn bp" style="flex:1;height:44px;font-size:13px;">🚶 เดินเท้า 4 นาที (320 ม.)</div>
          <div class="btn bs" style="flex:1;height:44px;font-size:13px;" data-go="S24">🚌 รถราง EV 2 นาที</div>
        </div>

        <div class="card" style="padding:16px;display:flex;flex-direction:column;gap:12px;font-size:13px;">
          <div style="font-weight:700;color:{C['navy']};">ขั้นตอนการเดินเท้า:</div>
          <div class="row" style="gap:10px;">
            <span style="width:22px;height:22px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11px;">1</span>
            <span>เดินออกจากประตูทิศตะวันตกของหอสมุด มุ่งหน้าสู่วงเวียนสระแก้ว (120 ม.)</span>
          </div>
          <div class="row" style="gap:10px;">
            <span style="width:22px;height:22px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11px;">2</span>
            <span>เลี้ยวขวาผ่านหน้าคณะศึกษาศาสตร์ ข้ามทางม้าลาย (80 ม.)</span>
          </div>
          <div class="row" style="gap:10px;">
            <span style="width:22px;height:22px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:11px;">3</span>
            <span>ถึงอาคารศูนย์เรียนรวม SC ประตูด้านหน้า ลิฟต์อยู่ฝั่งซ้ายมือ</span>
          </div>
        </div>

        <div style="margin-top:auto;">
          {btn("เริ่มการนำทางเสมือนจริง (Start Navigation)", "bp", go="S21", icon="nav")}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s24_smart_transit():
    """24. Smart Shuttle Bus Tracker"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("รถรางไฟฟ้ามหาวิทยาลัย (EV Transit)", back=True)}
      <div class="body" style="padding:0 20px;gap:12px;overflow-y:auto;">
        <div class="card" style="background:linear-gradient(135deg,#059669,#047857);color:#fff;border:none;">
          <div class="row" style="justify-content:space-between;">
            <span class="badge" style="background:rgba(255,255,255,0.2);color:#fff;">สายสีเขียว (Green Line)</span>
            <span style="font-size:12px;">กำลังวิ่ง 3 คัน</span>
          </div>
          <div style="font:700 20px Inter;margin-top:8px;">ป้ายหอสมุดกลาง (Central Library)</div>
          <div style="font-size:13px;opacity:.9;margin-top:2px;">รถคันถัดไปจะมาถึงในอีก: <strong>3 นาที (180 เมตร)</strong></div>
        </div>

        <div class="sec"><span>สถานะรถทุกสายในวิทยาเขต</span></div>
        <div class="card" style="padding:12px 14px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-weight:700;font-size:14px;color:{C['navy']};">สาย 1: หน้าประตูใหญ่ ➔ หอสมุด ➔ ตึก SC</div>
            <div style="font-size:12px;color:#64748B;">ที่นั่งว่างปานกลาง • ค่าโดยสาร: ฟรีสำหรับนักศึกษา</div>
          </div>
          <span class="badge b-green">3 นาที</span>
        </div>

        <div class="card" style="padding:12px 14px;display:flex;justify-content:space-between;align-items:center;">
          <div>
            <div style="font-weight:700;font-size:14px;color:{C['navy']};">สาย 2: ศูนย์อาหาร ➔ หอพักนักศึกษา ➔ สนามกีฬา</div>
            <div style="font-size:12px;color:#64748B;">แน่นมาก • รถคันต่อไป 09:15 น.</div>
          </div>
          <span class="badge b-amber">8 นาที</span>
        </div>
      </div>
      {nav(2, link=True)}
    </div>
    '''

def s25_room_booking():
    """25. Room & Space Booking"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("จองห้องและพื้นที่การเรียนรู้", back=True)}
      <div class="body" style="padding:0 20px;gap:12px;overflow-y:auto;">
        <div class="chips">
          <div class="chip on">ห้องติวกลุ่ม (Study Pod)</div>
          <div class="chip">Co-working Space</div>
          <div class="chip">แล็บคอมพิวเตอร์</div>
          <div class="chip">ห้องซ้อมนำเสนอ</div>
        </div>

        <!-- Room 1 -->
        <div class="card" style="padding:0;overflow:hidden;cursor:pointer;" data-go="S26">
          <div style="width:100%;height:140px;background:#E2E8F0;">
            {img("study_room.jpg", "width:100%;height:140px;object-fit:cover;")}
          </div>
          <div style="padding:14px;">
            <div class="row" style="justify-content:space-between;">
              <div style="font-weight:700;font-size:16px;color:{C['navy']};">ห้องติวกลุ่ม 4B (Group Study 4B)</div>
              <span class="badge b-green">ว่าง</span>
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:2px;">หอสมุดกลาง ชั้น 4 • ความจุ 4-6 ที่นั่ง</div>
            <div style="font-size:12px;color:#64748B;margin-top:6px;">
              สิ่งอำนวยความสะดวก: Smart TV 55", ปลั๊กไฟ 6 จุด, กระดานกระจก ไวไฟความเร็วสูง
            </div>
            <div style="margin-top:12px;">
              {btn("เลือกช่วงเวลาและจองห้อง (Select Slot)", "bp", go="S26", style="height:42px;font-size:13px;")}
            </div>
          </div>
        </div>
      </div>
      {nav(0, link=True)}
    </div>
    '''

def s26_booking_confirm():
    """26. Booking Confirmation Modal & QR Check-in"""
    return f'''
    <div class="scr" style="background:rgba(16,28,54,0.55);">
      {screen_bg_hint()}
      <div class="modal" style="top:180px;">
        <div style="width:68px;height:68px;border-radius:50%;background:#ECFDF5;color:{C['green']};display:flex;align-items:center;justify-content:center;">
          {ic("check", 34, C['green'])}
        </div>
        <div class="h1" style="font-size:22px;color:{C['navy']};">จองห้องสำเร็จเรียบร้อย!</div>
        <div style="font-size:12px;color:#64748B;">รหัสการจอง: #BK-2569-4419</div>

        <!-- Ticket Card -->
        <div class="card" style="background:#F8FAFC;text-align:left;width:100%;padding:14px;font-size:13px;">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};">ห้องติวกลุ่ม 4B (Group Study)</div>
          <div style="color:#64748B;margin-top:2px;">📍 หอสมุดกลาง ชั้น 4 ม.ศิลปากร</div>
          <div style="color:#64748B;margin-top:2px;">📅 วันนี้ (12 ต.ค. 2569) เวลา 13:00 - 15:00 น.</div>
          <div style="color:#64748B;margin-top:2px;">👤 ผู้จอง: {USER['th_full']}</div>
          <div class="sep" style="margin:10px 0;"></div>
          <div style="text-align:center;">
            <div style="font-size:11px;color:#64748B;margin-bottom:6px;">สแกน QR หน้าห้องเพื่อปลดล็อกประตู:</div>
            <div style="display:flex;justify-content:center;">{qr_svg(120, seed="ROOM-4B-BK4419")}</div>
          </div>
        </div>

        <div style="display:flex;flex-direction:column;gap:8px;width:100%;">
          {btn("บันทึกการจองลงปฏิทิน", "bp", go="S15", icon="calendar")}
          {btn("ปิดหน้าต่าง (กลับสู่หน้าหลัก)", "bs", go="S07")}
        </div>
      </div>
      {hi()}
    </div>
    '''

def s27_fleet_rental():
    """27. Fleet & Equipment Rental (ยืม-คืนยานพาหนะ & อุปกรณ์แล็บ)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ยืม-คืนยานพาหนะ & อุปกรณ์", back=True, back_target="S07")}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Banner Intro -->
        <div class="card" style="background:#EFF6FF;border-color:#DBEAFE;padding:12px 14px;display:flex;align-items:center;gap:12px;">
          <div style="width:38px;height:38px;border-radius:10px;background:#DBEAFE;display:flex;align-items:center;justify-content:center;color:{C['blue']};">
            {ic("bike", 22, C['blue'])}
          </div>
          <div>
            <div style="font-weight:700;font-size:13px;color:{C['blue']};">ระบบยืมคืนอัจฉริยะ Smart Campus</div>
            <div style="font-size:11px;color:#1E40AF;margin-top:2px;">สแกนปลดล็อกด้วย Digital ID • ใช้งานฟรีตามโควตานักศึกษา</div>
          </div>
        </div>

        <!-- Filter Chips -->
        <div class="chips">
          <div class="chip on">ทั้งหมด (All)</div>
          <div class="chip">จักรยานไฟฟ้า Smart EV</div>
          <div class="chip">อุปกรณ์แล็บ (iPads/กล้อง)</div>
          <div class="chip">รถตู้รับส่งสถาบัน</div>
        </div>

        <!-- Item 1: Smart EV Bike -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div class="row" style="gap:12px;">
              <div style="width:48px;height:48px;border-radius:14px;background:#F0FDF4;display:flex;align-items:center;justify-content:center;color:{C['green']};">
                {ic("bike", 26, C['green'])}
              </div>
              <div>
                <div style="font-weight:700;font-size:14px;color:{C['navy']};">Smart EV Bike #SU-042</div>
                <div style="font-size:12px;color:#64748B;margin-top:1px;">จุดจอด: หน้าหอสมุดกลาง วังสนามจันทร์</div>
                <div class="row" style="gap:8px;margin-top:6px;">
                  <span class="badge b-green">● แบตเตอรี่ 88% (วิ่งได้ 32 กม.)</span>
                  <span class="badge b-blue">ฟรี 2 ชม. แรก</span>
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;display:flex;align-items:center;justify-content:space-between;">
            <div style="font-size:11px;color:#64748B;">ค่าบริการส่วนเกิน: ฿ 10 / ชม.</div>
            {btn("สแกนปลดล็อก NFC / QR", "bp", go="S26", icon="qr", style="height:36px;font-size:12px;padding:0 14px;")}
          </div>
        </div>

        <!-- Item 2: Lab iPad Pro M2 -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div class="row" style="gap:12px;">
              <div style="width:48px;height:48px;border-radius:14px;background:#F5F3FF;display:flex;align-items:center;justify-content:center;color:#7C3AED;">
                {ic("tv", 26, "#7C3AED")}
              </div>
              <div>
                <div style="font-weight:700;font-size:14px;color:{C['navy']};">Apple iPad Pro 11\" M2 + Pencil 2</div>
                <div style="font-size:12px;color:#64748B;margin-top:1px;">แล็บเทคโนโลยีการศึกษา ED-302</div>
                <div class="row" style="gap:8px;margin-top:6px;">
                  <span class="badge b-blue">ยืมเพื่อการศึกษา 3 วัน</span>
                  <span class="badge b-green">พร้อมใช้งาน 4 เครื่อง</span>
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;display:flex;align-items:center;justify-content:space-between;">
            <div style="font-size:11px;color:#64748B;">ติดตั้ง Procreate, GoodNotes, Canva Pro</div>
            {btn("จองคิวรับเครื่อง", "bp", go="S26", style="height:36px;font-size:12px;padding:0 14px;")}
          </div>
        </div>

        <!-- Item 3: Campus Shuttle Van -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div class="row" style="gap:12px;">
              <div style="width:48px;height:48px;border-radius:14px;background:#FFFBEB;display:flex;align-items:center;justify-content:center;color:{C['amber']};">
                {ic("car", 26, C['amber'])}
              </div>
              <div>
                <div style="font-weight:700;font-size:14px;color:{C['navy']};">รถตู้รับส่ง วังสนามจันทร์ ⇄ วังท่าพระ</div>
                <div style="font-size:12px;color:#64748B;margin-top:1px;">รอบเวลาวันนี้: 16:30 น. (ที่นั่งว่าง 4/14)</div>
                <div class="row" style="gap:8px;margin-top:6px;">
                  <span class="badge b-amber">เดินทางระหว่างวิทยาเขต</span>
                  <span class="badge b-green">ฟรีสำหรับนักศึกษา</span>
                </div>
              </div>
            </div>
          </div>
          <div style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;display:flex;align-items:center;justify-content:space-between;">
            <div style="font-size:11px;color:#64748B;">จุดขึ้นรถ: หน้าอาคารศิลป์ พีระศรี 3</div>
            {btn("สำรองที่นั่งด่วน", "bp", go="S26", style="height:36px;font-size:12px;padding:0 14px;")}
          </div>
        </div>
      </div>
      {nav(0, link=True)}
    </div>
    '''

def s28_student_services():
    """28. Student Services (e-Request / คำร้องทางการ)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("บริการคำร้องนักศึกษา (e-Services)", back=True)}
      <div class="body" style="padding:0 20px;gap:14px;overflow-y:auto;">
        <div class="card" style="background:#EFF6FF;border-color:#DBEAFE;padding:12px 14px;">
          <div style="font-weight:700;font-size:13px;color:{C['blue']};">ระบบคำร้องออนไลน์ส่วนกลาง (อว. e-Services)</div>
          <div style="font-size:11px;color:#1E40AF;margin-top:2px;">ยื่นคำร้อง ติดตามสถานะ และรับเอกสารดิจิทัลผ่านแอปได้โดยตรง</div>
        </div>

        <div class="sec"><span>ยื่นคำร้องรายการใหม่</span></div>
        <div class="card" style="padding:14px;cursor:pointer;" data-go="S07">
          <div class="row" style="justify-content:space-between;">
            <div>
              <div style="font-weight:700;font-size:14px;color:{C['navy']};">คำร้องขอใบรายงานผลการศึกษา (Transcript)</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">ฉบับดิจิทัลพร้อมลายมือชื่ออิเล็กทรอนิกส์</div>
            </div>
            <span class="link">ยื่นเรื่อง →</span>
          </div>
        </div>

        <div class="card" style="padding:14px;cursor:pointer;" data-go="S07">
          <div class="row" style="justify-content:space-between;">
            <div>
              <div style="font-weight:700;font-size:14px;color:{C['navy']};">หนังสือรับรองสถานภาพนักศึกษา</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">ภาษาไทย / ภาษาอังกฤษ สำหรับขอวีซ่าหรือสมัครงาน</div>
            </div>
            <span class="link">ยื่นเรื่อง →</span>
          </div>
        </div>

        <div class="sec" style="margin-top:6px;"><span>สถานะคำร้องของฉัน (My Petitions)</span></div>
        <div class="card" style="padding:14px;border-left:4px solid {C['green']};">
          <div class="row" style="justify-content:space-between;">
            <span style="font-weight:700;font-size:13px;color:{C['navy']};">ขอหนังสือรับรองสถานภาพ (ฉบับภาษาอังกฤษ)</span>
            <span class="badge b-green">อนุมัติแล้ว</span>
          </div>
          <div style="font-size:11px;color:#64748B;margin-top:4px;">ยื่นเมื่อ 11 ต.ค. 2569 • เลขที่ #REQ-2569-8812</div>
          <div class="row" style="margin-top:10px;justify-content:space-between;">
            <span style="font-size:12px;color:{C['blue']};font-weight:600;">ดาวน์โหลดเอกสาร PDF (มีตราประทับ อว.)</span>
            {ic("download", 16, C['blue'])}
          </div>
        </div>
      </div>
      {nav(4, link=True)}
    </div>
    '''

def s29_wallet():
    """29. กระเป๋าเงินดิจิทัล & โครงการ Camplus (Campus Wallet)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("กระเป๋าเงินดิจิทัล & Camplus", back=True, back_target="S07", right=f'<div class="ib" data-go="S31" style="cursor:pointer;">{ic("receipt", 20, C["navy"])}</div>')}
      <div class="body" style="padding:0 20px;gap:14px;overflow-y:auto;">
        
        <!-- Camplus Hero Card (Living Welfare 3,000 THB/month) -->
        <div class="card" style="background:linear-gradient(135deg,#0D1B3E 0%,#163268 50%,#246BFD 100%);color:#fff;border:none;box-shadow:0 16px 36px rgba(36,107,253,.32);position:relative;overflow:hidden;padding:18px 20px;">
          <div style="position:absolute;right:-25px;top:-25px;width:140px;height:140px;border-radius:50%;background:radial-gradient(circle,rgba(88,214,255,0.25) 0%,transparent 70%);pointer-events:none;"></div>
          <div style="position:absolute;left:-30px;bottom:-30px;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(36,107,253,0.3) 0%,transparent 70%);pointer-events:none;"></div>

          <div class="row" style="justify-content:space-between;position:relative;z-index:2;">
            <div class="row" style="gap:8px;">
              <span style="font-size:18px;">✨</span>
              <div>
                <div style="font-weight:800;font-size:15px;color:#fff;letter-spacing:.3px;">โครงการ Camplus</div>
                <div style="font-size:11px;color:{C['cyan']};">เงินอุดหนุนค่าครองชีพนักศึกษา ม.ศิลปากร</div>
              </div>
            </div>
            <span class="badge" style="background:rgba(88,214,255,0.2);color:{C['cyan']};border:1px solid rgba(88,214,255,0.4);font-size:11px;">
              โควตา ฿3,000 / ด.
            </span>
          </div>

          <div style="margin-top:16px;position:relative;z-index:2;">
            <div style="font-size:12px;color:#CBD5E1;">ยอดเงินคงเหลือในกระเป๋า Camplus</div>
            <div class="row" style="align-items:baseline;gap:8px;margin-top:4px;">
              <span style="font:800 34px 'Inter';color:#fff;letter-spacing:.5px;">฿ 2,420.00</span>
              <span style="font-size:12px;color:#94A3B8;">/ 3,000.00 บาท</span>
            </div>
          </div>

          <!-- Quota Progress Bar -->
          <div style="margin-top:14px;position:relative;z-index:2;">
            <div class="row" style="justify-content:space-between;font-size:11px;color:#CBD5E1;margin-bottom:6px;">
              <span>ใช้ไปแล้ว ฿580.00 (19%)</span>
              <span style="color:{C['cyan']};">เหลือใช้ได้อีก ฿2,420.00</span>
            </div>
            <div style="width:100%;height:8px;border-radius:4px;background:rgba(255,255,255,0.15);overflow:hidden;">
              <div style="width:81%;height:100%;border-radius:4px;background:linear-gradient(90deg,#58D6FF,#246BFD);"></div>
            </div>
          </div>

          <div class="row" style="justify-content:space-between;margin-top:14px;padding-top:12px;border-top:1px solid rgba(255,255,255,0.12);font-size:11px;color:#94A3B8;position:relative;z-index:2;">
            <span>ตัดรอบใหม่: 1 พ.ย. 2569 (รีเซ็ตเป็น ฿3,000)</span>
            <span style="color:#6EE7B7;font-weight:600;">● สิทธิ์ปกติ</span>
          </div>
        </div>

        <!-- 4 Primary Action Tiles -->
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;">
          <div class="card" style="padding:12px 6px;text-align:center;cursor:pointer;background:#EFF6FF;border-color:#BFDBFE;" data-go="S30">
            <div style="width:44px;height:44px;border-radius:14px;background:#246BFD;color:#fff;margin:0 auto 6px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(36,107,253,0.3);">
              {ic("scan", 22, "#fff")}
            </div>
            <div style="font-weight:700;font-size:12px;color:{C['navy']};">สแกนจ่าย</div>
          </div>
          <div class="card" style="padding:12px 6px;text-align:center;cursor:pointer;">
            <div style="width:44px;height:44px;border-radius:14px;background:#F1F5F9;color:{C['navy']};margin:0 auto 6px;display:flex;align-items:center;justify-content:center;">
              {ic("qr", 22, C['navy'])}
            </div>
            <div style="font-weight:700;font-size:12px;color:{C['navy']};">QR ของฉัน</div>
          </div>
          <div class="card" style="padding:12px 6px;text-align:center;cursor:pointer;">
            <div style="width:44px;height:44px;border-radius:14px;background:#ECFDF5;color:{C['green']};margin:0 auto 6px;display:flex;align-items:center;justify-content:center;">
              {ic("plus", 22, C['green'])}
            </div>
            <div style="font-weight:700;font-size:12px;color:{C['navy']};">เติมเงิน</div>
          </div>
          <div class="card" style="padding:12px 6px;text-align:center;cursor:pointer;" data-go="S21">
            <div style="width:44px;height:44px;border-radius:14px;background:#FEF3C7;color:{C['amber']};margin:0 auto 6px;display:flex;align-items:center;justify-content:center;">
              {ic("food", 22, C['amber'])}
            </div>
            <div style="font-weight:700;font-size:12px;color:{C['navy']};">ร้านร่วมรายการ</div>
          </div>
        </div>

        <!-- Personal Balance Sub-Wallet -->
        <div class="card" style="padding:14px 16px;background:#fff;display:flex;align-items:center;justify-content:space-between;">
          <div class="row" style="gap:12px;">
            <div style="width:40px;height:40px;border-radius:12px;background:#F8FAFC;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;color:{C['navy']};">
              {ic("wallet", 22, C['navy'])}
            </div>
            <div>
              <div style="font-size:11px;color:#64748B;">กระเป๋าเงินสดส่วนตัว (Personal Wallet)</div>
              <div style="font:700 16px 'Inter';color:{C['navy']};">฿ 450.00</div>
            </div>
          </div>
          <button style="border:1px solid #E2E8F0;background:#F8FAFC;color:{C['blue']};font-size:12px;font-weight:700;padding:6px 12px;border-radius:10px;cursor:pointer;">
            + เติมเงิน
          </button>
        </div>

        <!-- Participating Stores & Services Banner -->
        <div class="card" style="padding:14px 16px;background:linear-gradient(135deg,#F0FDF4 0%,#E6F9EF 100%);border:1px solid #BBF7D0;">
          <div class="row" style="justify-content:space-between;">
            <div class="row" style="gap:8px;">
              <span class="badge b-green">สิทธิประโยชน์ Camplus</span>
              <span style="font-size:12px;font-weight:700;color:#0F7F59;">ใช้ได้ทุกร้านใน ม.ศิลปากร</span>
            </div>
            <span class="link" data-go="S21">ดูแผนที่ร้าน</span>
          </div>
          <div style="font-size:12px;color:#166534;margin-top:8px;line-height:1.5;">
            ครอบคลุมโรงอาหารสระแก้ว/เพชรรัตน, ศูนย์หนังสือ, ร้านสะดวกซื้อ, รถราง EV และร้านกาแฟทุกคณะ
          </div>
        </div>

        <!-- Recent Transactions -->
        <div>
          <div class="sec"><span>ประวัติการใช้จ่ายล่าสุด</span><span class="link" data-go="S31">ดูสลิป</span></div>
          <div style="display:flex;flex-direction:column;gap:10px;margin-top:10px;">
            <div class="card" style="padding:12px 14px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;" data-go="S31">
              <div class="row" style="gap:12px;">
                <div style="width:38px;height:38px;border-radius:10px;background:#FEE2E2;color:#DC2626;display:flex;align-items:center;justify-content:center;">
                  {ic("food", 20, "#DC2626")}
                </div>
                <div>
                  <div style="font-weight:700;font-size:13px;color:{C['navy']};">โรงอาหารเพชรรัตน — ร้านป้าพร</div>
                  <div style="font-size:11px;color:#64748B;">วันนี้ 12:45 น. • ข้าวกะเพราหมูกรอบ</div>
                </div>
              </div>
              <div style="text-align:right;">
                <div style="font:700 14px 'Inter';color:#DC2626;">-฿65.00</div>
                <span class="badge b-blue" style="font-size:9px;padding:1px 6px;">Camplus</span>
              </div>
            </div>

            <div class="card" style="padding:12px 14px;display:flex;align-items:center;justify-content:space-between;">
              <div class="row" style="gap:12px;">
                <div style="width:38px;height:38px;border-radius:10px;background:#FEE2E2;color:#DC2626;display:flex;align-items:center;justify-content:center;">
                  {ic("book", 20, "#DC2626")}
                </div>
                <div>
                  <div style="font-weight:700;font-size:13px;color:{C['navy']};">ศูนย์หนังสือ ม.ศิลปากร</div>
                  <div style="font-size:11px;color:#64748B;">เมื่อวาน 16:20 น. • สมุดและปากกาไฮไลท์</div>
                </div>
              </div>
              <div style="text-align:right;">
                <div style="font:700 14px 'Inter';color:#DC2626;">-฿120.00</div>
                <span class="badge b-blue" style="font-size:9px;padding:1px 6px;">Camplus</span>
              </div>
            </div>

            <div class="card" style="padding:12px 14px;display:flex;align-items:center;justify-content:space-between;">
              <div class="row" style="gap:12px;">
                <div style="width:38px;height:38px;border-radius:10px;background:#ECFDF5;color:#16A675;display:flex;align-items:center;justify-content:center;">
                  {ic("gift", 20, "#16A675")}
                </div>
                <div>
                  <div style="font-weight:700;font-size:13px;color:{C['navy']};">มหาวิทยาลัยศิลปากร (อว.)</div>
                  <div style="font-size:11px;color:#64748B;">1 ต.ค. 2569 • เงินอุดหนุน Camplus ประจำเดือน</div>
                </div>
              </div>
              <div style="text-align:right;">
                <div style="font:700 14px 'Inter';color:#16A675;">+฿3,000.00</div>
                <span class="badge b-green" style="font-size:9px;padding:1px 6px;">งบสวัสดิการ</span>
              </div>
            </div>
          </div>
        </div>

      </div>
      {nav(0, link=True)}
    </div>
    '''

def s30_scan_pay():
    """30. สแกนจ่ายเงิน & เลือกกระเป๋า Camplus (QR Scanner & Payment Drawer)"""
    return f'''
    <div class="scr" style="background:#0F172A;color:#fff;">
      {sb(dark=True)}
      <!-- Top Scanner Bar -->
      <div class="bar" style="justify-content:space-between;color:#fff;">
        <div class="ib" data-go="S29" style="background:rgba(255,255,255,0.15);border:none;color:#fff;cursor:pointer;">
          {ic("left", 20, "#fff")}
        </div>
        <div class="ttl" style="color:#fff;">สแกนคิวอาร์ชำระเงิน</div>
        <div class="ib" style="background:rgba(255,255,255,0.15);border:none;color:#fff;cursor:pointer;">
          {ic("sun", 20, "#fff")}
        </div>
      </div>

      <!-- Camera Viewfinder Simulation -->
      <div style="flex:1;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;">
        <!-- Scanner Frame -->
        <div style="width:260px;height:260px;position:relative;display:flex;align-items:center;justify-content:center;">
          <!-- 4 Corner Brackets -->
          <div style="position:absolute;left:0;top:0;width:36px;height:36px;border-top:4px solid {C['cyan']};border-left:4px solid {C['cyan']};border-radius:12px 0 0 0;"></div>
          <div style="position:absolute;right:0;top:0;width:36px;height:36px;border-top:4px solid {C['cyan']};border-right:4px solid {C['cyan']};border-radius:0 12px 0 0;"></div>
          <div style="position:absolute;left:0;bottom:0;width:36px;height:36px;border-bottom:4px solid {C['cyan']};border-left:4px solid {C['cyan']};border-radius:0 0 0 12px;"></div>
          <div style="position:absolute;right:0;bottom:0;width:36px;height:36px;border-bottom:4px solid {C['cyan']};border-right:4px solid {C['cyan']};border-radius:0 0 12px 0;"></div>

          <!-- Laser Scan Line -->
          <div style="position:absolute;left:10px;right:10px;top:50%;height:2px;background:linear-gradient(90deg,transparent,#58D6FF,#246BFD,transparent);box-shadow:0 0 12px #58D6FF;"></div>

          <!-- Dummy QR Code in Viewfinder -->
          <div style="opacity:0.65;">
            {qr_svg(180, seed="SU-MERCHANT-FOOD-014", color="#FFFFFF")}
          </div>
        </div>

        <div style="font-size:13px;color:#94A3B8;margin-top:16px;text-align:center;">
          ส่องกล้องตรงไปยังคิวอาร์ร้านค้าภายในมหาวิทยาลัย
        </div>
      </div>

      <!-- Bottom Detected Payment Sheet -->
      <div style="background:#fff;border-radius:28px 28px 0 0;padding:20px 24px 30px;color:{C['navy']};box-shadow:0 -10px 40px rgba(0,0,0,0.5);">
        <div class="handle" style="margin-bottom:14px;"></div>

        <!-- Detected Merchant Header -->
        <div class="row" style="justify-content:space-between;align-items:center;">
          <div class="row" style="gap:12px;">
            <div style="width:44px;height:44px;border-radius:14px;background:#EFF6FF;display:flex;align-items:center;justify-content:center;color:{C['blue']};">
              {ic("food", 22, C['blue'])}
            </div>
            <div>
              <div style="font-weight:700;font-size:15px;color:{C['navy']};">โรงอาหารเพชรรัตน — ร้านป้าพร</div>
              <div style="font-size:11px;color:#64748B;">รหัสร้านค้า: SU-FOOD-014 • วังสนามจันทร์</div>
            </div>
          </div>
          <span class="badge b-green" style="font-size:11px;">✓ รับ Camplus</span>
        </div>

        <!-- Amount Box -->
        <div style="margin-top:16px;background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:16px;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;">
          <div>
            <div style="font-size:11px;color:#64748B;">ยอดที่ต้องชำระ (Amount)</div>
            <div style="font:800 28px 'Inter';color:{C['navy']};">฿ 65.00</div>
          </div>
          <div style="text-align:right;">
            <span style="font-size:12px;color:#64748B;">ข้าวกะเพราหมูกรอบ</span>
          </div>
        </div>

        <!-- Payment Source Selection -->
        <div style="margin-top:16px;">
          <div style="font-size:13px;font-weight:700;color:{C['navy']};margin-bottom:8px;">เลือกแหล่งเงินที่จะชำระ:</div>
          
          <!-- Option 1: Camplus (Default Checked) -->
          <div class="card" style="padding:12px 14px;border:2px solid {C['blue']};background:#EFF6FF;margin-bottom:8px;cursor:pointer;">
            <div class="row" style="justify-content:space-between;">
              <div class="row" style="gap:10px;">
                <div style="width:20px;height:20px;border-radius:50%;background:{C['blue']};color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;">
                  ✓
                </div>
                <div>
                  <div class="row" style="gap:6px;">
                    <span style="font-weight:700;font-size:13px;color:{C['navy']};">งบค่าครองชีพ Camplus</span>
                    <span class="badge b-blue" style="font-size:10px;height:18px;">แนะนำ</span>
                  </div>
                  <div style="font-size:11px;color:#64748B;margin-top:2px;">คงเหลือ ฿ 2,420.00 (หลังหักเหลือ ฿ 2,355.00)</div>
                </div>
              </div>
              <span style="font:700 13px 'Inter';color:{C['blue']};">-฿65.00</span>
            </div>
          </div>

          <!-- Option 2: Personal Balance -->
          <div class="card" style="padding:12px 14px;border:1px solid #E2E8F0;cursor:pointer;">
            <div class="row" style="justify-content:space-between;">
              <div class="row" style="gap:10px;">
                <div style="width:20px;height:20px;border-radius:50%;border:2px solid #CBD5E1;"></div>
                <div>
                  <div style="font-weight:600;font-size:13px;color:{C['navy']};">กระเป๋าเงินสดส่วนตัว (Personal Wallet)</div>
                  <div style="font-size:11px;color:#64748B;margin-top:2px;">คงเหลือ ฿ 450.00</div>
                </div>
              </div>
              <span style="font:600 13px 'Inter';color:#64748B;">-฿65.00</span>
            </div>
          </div>
        </div>

        <div style="margin-top:20px;">
          {btn("ยืนยันการชำระเงิน (Confirm Pay ฿65.00)", "bp", go="S31", icon="check")}
        </div>
      </div>
      {hi(dark=True)}
    </div>
    '''

def s31_payment_slip():
    """31. สลิปชำระเงินดิจิทัล (Digital e-Slip & Confirmation)"""
    return f'''
    <div class="scr" style="background:#F1F5F9;">
      {sb()}
      {bar("ทำรายการสำเร็จ", back=True, back_target="S29", right=f'<div class="ib" style="cursor:pointer;">{ic("share", 18, C["navy"])}</div>')}
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        
        <!-- Digital e-Slip Receipt Card -->
        <div class="card" style="background:#fff;border-radius:24px;padding:24px 20px;box-shadow:0 12px 30px rgba(0,0,0,0.08);position:relative;">
          <!-- Success Stamp / Checkmark -->
          <div style="text-align:center;">
            <div style="width:60px;height:60px;border-radius:50%;background:#ECFDF5;border:3px solid #10B981;color:#10B981;margin:0 auto 10px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 20px rgba(16,185,129,0.25);">
              {ic("check", 32, "#10B981", w=3)}
            </div>
            <div style="font-weight:800;font-size:20px;color:{C['navy']};">ชำระเงินสำเร็จ</div>
            <div style="font-size:12px;color:#64748B;margin-top:2px;">14 ตุลาคม 2569 • 12:45 น.</div>
            <div style="font:800 32px 'Inter';color:{C['blue']};margin-top:12px;">฿ 65.00</div>
          </div>

          <!-- Perforated Ticket Divider -->
          <div style="position:relative;margin:20px -20px;">
            <div class="sep" style="border-top:2px dashed #CBD5E1;background:none;height:0;"></div>
            <div style="position:absolute;left:-10px;top:-10px;width:20px;height:20px;border-radius:50%;background:#F1F5F9;"></div>
            <div style="position:absolute;right:-10px;top:-10px;width:20px;height:20px;border-radius:50%;background:#F1F5F9;"></div>
          </div>

          <!-- Slip Details -->
          <div style="display:flex;flex-direction:column;gap:10px;font-size:13px;">
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ชำระจาก:</span>
              <span class="badge b-blue" style="font-size:11px;">✨ โครงการ Camplus</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ร้านค้าปลายทาง:</span>
              <span style="font-weight:700;color:{C['navy']};">ร้านป้าพรอาหารตามสั่ง (ร้าน 14)</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">สถานที่:</span>
              <span style="color:{C['navy']};">โรงอาหารเพชรรัตน ม.ศิลปากร</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ผู้ชำระ:</span>
              <span style="font-weight:600;color:{C['navy']};">{USER['th_full']}</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">รหัสนักศึกษา:</span>
              <span style="font:600 13px 'Inter';color:{C['navy']};">{USER['sid']}</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">คณะ/สาขา:</span>
              <span style="color:{C['navy']};">{USER['fac']}</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">รหัสอ้างอิง:</span>
              <span style="font:600 12px 'Inter';color:#64748B;">TXN-SU-20261014-9842</span>
            </div>

            <div class="sep" style="margin:6px 0;"></div>

            <!-- Remaining Camplus Quota Box -->
            <div class="card" style="padding:10px 14px;background:#F0FDF4;border:1px solid #BBF7D0;">
              <div class="row" style="justify-content:space-between;">
                <span style="font-size:12px;color:#166534;">ยอดคงเหลืองบ Camplus เดือนนี้:</span>
                <span style="font:800 15px 'Inter';color:#15803D;">฿ 2,355.00</span>
              </div>
              <div style="font-size:10px;color:#16A34A;margin-top:2px;">
                (ใช้ไปแล้ว ฿645.00 จากโควตาทั้งหมด ฿3,000.00)
              </div>
            </div>

            <!-- Slip Barcode & QR Verification -->
            <div style="margin-top:10px;text-align:center;">
              <div style="margin:0 auto;display:flex;justify-content:center;">
                {qr_svg(100, seed="TXN-SU-20261014-9842", color="#101C36")}
              </div>
              <div style="font-size:11px;color:#94A3B8;margin-top:6px;">
                สแกนตรวจสอบความถูกต้องผ่านระบบ e-Receipt อว.
              </div>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div style="display:flex;flex-direction:column;gap:10px;margin-top:8px;">
          {btn("เสร็จสิ้น (กลับหน้ากระเป๋าเงิน Camplus)", "bp", go="S29", icon="wallet")}
          {btn("กลับสู่หน้าหลัก (Home Dashboard)", "bs", go="S07", icon="home")}
        </div>

      </div>
      {hi()}
    </div>
    '''



def s32_tuition_pay():
    """32. Tuition Fee Payment & Official e-Receipt (ชำระค่าลงทะเบียน & ค่าธรรมเนียม)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ชำระค่าลงทะเบียน & ค่าธรรมเนียม", back=True, back_target="S07", right=f'<div class="ib" data-go="S31" style="cursor:pointer;">{ic("receipt", 20, C["navy"])}</div>')}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Invoice Header Card -->
        <div class="card" style="background:linear-gradient(135deg,#101C36 0%,#1E293B 100%);color:#fff;border:none;padding:18px 20px;box-shadow:0 12px 28px rgba(16,28,54,0.35);">
          <div class="row" style="justify-content:space-between;">
            <div>
              <div style="font-size:12px;color:{C['cyan']};letter-spacing:.5px;">ภาคการศึกษาที่ 2/2569</div>
              <div style="font-weight:800;font-size:18px;color:#fff;margin-top:2px;">{USER['fac']}</div>
              <div style="font-size:12px;color:#94A3B8;">{USER['uni']} (วังสนามจันทร์)</div>
            </div>
            <span class="badge b-amber" style="height:24px;">รอการชำระเงิน</span>
          </div>

          <div style="margin-top:16px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.12);display:flex;justify-content:space-between;align-items:flex-end;">
            <div>
              <div style="font-size:11px;color:#94A3B8;">ยอดชำระสุทธิ (Total Due)</div>
              <div style="font:800 28px 'Inter';color:#fff;">฿ 18,500.00</div>
            </div>
            <div style="font-size:11px;color:#FCA5A5;font-weight:600;">ครบกำหนด 31 ต.ค. 69</div>
          </div>
        </div>

        <!-- Breakdown Details -->
        <div class="card" style="padding:16px;">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-bottom:12px;">รายการแจกแจงค่าธรรมเนียมการศึกษา</div>
          <div class="col" style="gap:10px;font-size:13px;">
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ค่าบำรุงมหาวิทยาลัยศิลปากร</span>
              <span style="font-weight:600;color:{C['navy']};">฿ 8,500.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ค่าหน่วยกิตศึกษาศาสตร์ (21 หน่วยกิต @ 400฿)</span>
              <span style="font-weight:600;color:{C['navy']};">฿ 8,400.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ค่าบำรุงแล็บเทคโนโลยีการศึกษา ED-Lab</span>
              <span style="font-weight:600;color:{C['navy']};">฿ 1,200.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ค่าประกันอุบัติเหตุ & สวัสดิการสุขภาพนักศึกษา</span>
              <span style="font-weight:600;color:{C['navy']};">฿ 400.00</span>
            </div>
            <div class="sep" style="margin:4px 0;"></div>
            <div class="row" style="justify-content:space-between;font-weight:700;">
              <span style="color:{C['navy']};">รวมทั้งสิ้น (Total Amount)</span>
              <span style="color:{C['blue']};font-size:16px;">฿ 18,500.00</span>
            </div>
          </div>
        </div>

        <!-- QR PromptPay Box -->
        <div class="card" style="text-align:center;padding:20px 16px;background:#F8FAFC;">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};">สแกนชำระด้วย QR PromptPay</div>
          <div style="font-size:12px;color:#64748B;margin-top:2px;">รองรับทุกแอปธนาคารไทย (Mobile Banking)</div>
          
          <div style="margin:16px auto;display:flex;justify-content:center;">
            <div style="padding:14px;background:#fff;border-radius:18px;border:1px solid #E2E8F0;box-shadow:0 8px 20px rgba(0,0,0,0.06);">
              {qr_svg(160, seed="PROMPTPAY-SU-TUITION-670610452-18500", color="#101C36")}
            </div>
          </div>

          <div style="font-size:11px;color:#64748B;">
            Ref 1: <strong>670610452</strong> • Ref 2: <strong>256902</strong>
          </div>

          <div class="row" style="gap:10px;margin-top:14px;">
            {btn("บันทึกรูป QR ลงเครื่อง", "bn", icon="download", style="flex:1;height:42px;font-size:12px;")}
            {btn("ตรวจสอบสถานะชำระ", "bp", go="S31", style="flex:1;height:42px;font-size:12px;")}
          </div>
        </div>

        <!-- Student Loan Hook -->
        <div class="card" style="padding:12px 16px;background:#F0FDF4;border-color:#BBF7D0;display:flex;align-items:center;justify-content:space-between;cursor:pointer;" data-go="S33">
          <div class="row" style="gap:10px;">
            {ic("check", 20, C['green'])}
            <div style="font-size:12px;color:#166534;">
              นักศึกษาผู้กู้ กยศ. ยอดนี้คุ้มครองตามสัญญาเงินกู้
            </div>
          </div>
          <span class="link" style="color:{C['green']};">ตรวจสิทธิ กยศ. →</span>
        </div>
      </div>
      {nav(4, link=True)}
    </div>
    '''

def s33_student_loan():
    """33. Student Loan e-Portal (ระบบกองทุนเงินกู้ยืม กยศ. ดิจิทัล)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ระบบกองทุน กยศ. ดิจิทัล", back=True, back_target="S07")}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Status Hero Card -->
        <div class="card" style="background:linear-gradient(135deg,#047857 0%,#065F46 100%);color:#fff;border:none;padding:18px 20px;box-shadow:0 12px 28px rgba(4,120,87,0.3);">
          <div class="row" style="justify-content:space-between;">
            <div>
              <div style="font-size:12px;color:#A7F3D0;">กองทุนเงินให้กู้ยืมเพื่อการศึกษา (กยศ.)</div>
              <div style="font-weight:800;font-size:18px;color:#fff;margin-top:2px;">สถานะ: อนุมัติสัญญากู้ยืมแล้ว</div>
            </div>
            <span class="badge b-green" style="background:#ECFDF5;color:#047857;font-weight:700;">Active 2/2569</span>
          </div>

          <div style="margin-top:16px;display:grid;grid-template-columns:1fr 1fr;gap:12px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.2);">
            <div>
              <div style="font-size:11px;color:#A7F3D0;">วงเงินค่าเทอมที่คุ้มครอง</div>
              <div style="font:700 18px 'Inter';color:#fff;margin-top:2px;">฿ 18,500.00</div>
            </div>
            <div>
              <div style="font-size:11px;color:#A7F3D0;">ค่าครองชีพรายเดือน</div>
              <div style="font:700 18px 'Inter';color:#fff;margin-top:2px;">฿ 3,000.00 / ด.</div>
            </div>
          </div>
        </div>

        <!-- 4-Step Loan Progress Tracker -->
        <div class="card" style="padding:16px;">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-bottom:14px;">ขั้นตอนการกู้ยืมประจำภาคเรียน 2/2569</div>
          
          <div class="col" style="gap:14px;">
            <!-- Step 1 -->
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="width:26px;height:26px;border-radius:50%;background:#ECFDF5;color:{C['green']};display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px;">
                {ic("check", 16, C['green'], w=2.6)}
              </div>
              <div style="flex:1;">
                <div style="font-weight:700;font-size:13px;color:{C['navy']};">1. ยื่นแบบยืนยันการกู้ยืมประจำปี</div>
                <div style="font-size:11px;color:#64748B;">ผ่านการรับรองโดยคณะศึกษาศาสตร์ (15 ก.ค. 2569)</div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="width:26px;height:26px;border-radius:50%;background:#ECFDF5;color:{C['green']};display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px;">
                {ic("check", 16, C['green'], w=2.6)}
              </div>
              <div style="flex:1;">
                <div style="font-weight:700;font-size:13px;color:{C['navy']};">2. บันทึกกรอบวงเงินค่าเล่าเรียน</div>
                <div style="font-size:11px;color:#64748B;">ยอด ฿ 18,500 ส่งต่อฝ่ายการเงิน ม.ศิลปากร เรียบร้อย</div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="width:26px;height:26px;border-radius:50%;background:#ECFDF5;color:{C['green']};display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px;">
                {ic("check", 16, C['green'], w=2.6)}
              </div>
              <div style="flex:1;">
                <div style="font-weight:700;font-size:13px;color:{C['navy']};">3. ลงนามสัญญากู้ยืมอิเล็กทรอนิกส์ (e-Signature)</div>
                <div style="font-size:11px;color:#64748B;">ยืนยันตัวตนดิจิทัลผ่าน ThaiID และ มหาวิทยาลัย</div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="row" style="gap:12px;align-items:flex-start;">
              <div style="width:26px;height:26px;border-radius:50%;background:#EFF6FF;color:{C['blue']};display:flex;align-items:center;justify-content:center;flex:none;margin-top:2px;">
                <span style="font:700 12px 'Inter';">4</span>
              </div>
              <div style="flex:1;">
                <div style="font-weight:700;font-size:13px;color:{C['blue']};">4. โอนเงินค่าครองชีพรายเดือน (3,000 ฿/ด.)</div>
                <div style="font-size:11px;color:#64748B;">กำลังดำเนินการโอนรอบถัดไป 25 ต.ค. 2569</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Monthly Allowance Transfer Schedule -->
        <div class="card" style="padding:16px;">
          <div class="row" style="justify-content:space-between;margin-bottom:10px;">
            <div style="font-weight:700;font-size:14px;color:{C['navy']};">ประวัติการโอนค่าครองชีพ (รอบปัจจุบัน)</div>
            <span style="font-size:11px;color:{C['blue']};font-weight:600;">บัญชี ธ.กรุงไทย</span>
          </div>

          <div class="col" style="gap:10px;font-size:13px;">
            <div class="row" style="justify-content:space-between;">
              <div>
                <div style="font-weight:600;color:{C['navy']};">งวดเดือน สิงหาคม 2569</div>
                <div style="font-size:11px;color:#64748B;">โอนสำเร็จ • 25 ส.ค. 69</div>
              </div>
              <span class="badge b-green">฿ 3,000.00 ✓</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <div>
                <div style="font-weight:600;color:{C['navy']};">งวดเดือน กันยายน 2569</div>
                <div style="font-size:11px;color:#64748B;">โอนสำเร็จ • 25 ก.ย. 69</div>
              </div>
              <span class="badge b-green">฿ 3,000.00 ✓</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <div>
                <div style="font-weight:600;color:{C['blue']};">งวดเดือน ตุลาคม 2569 (ถัดไป)</div>
                <div style="font-size:11px;color:#64748B;">กำหนดโอน • 25 ต.ค. 69 (อีก 11 วัน)</div>
              </div>
              <span class="badge b-blue">รอโอน ฿ 3,000</span>
            </div>
          </div>
        </div>

        <!-- Volunteer Hours Link -->
        <div class="card" style="padding:14px;background:#F8FAFC;cursor:pointer;" data-go="S34">
          <div class="row" style="justify-content:space-between;">
            <div class="row" style="gap:12px;">
              <div style="width:36px;height:36px;border-radius:10px;background:#ECFDF5;display:flex;align-items:center;justify-content:center;color:{C['green']};">
                {ic("heart", 20, C['green'])}
              </div>
              <div>
                <div style="font-weight:700;font-size:13px;color:{C['navy']};">ชั่วโมงจิตอาสาสะสม กยศ.</div>
                <div style="font-size:11px;color:#64748B;">สะสมครบ 36 / 36 ชม. แล้ว (เกณฑ์ผ่าน 100%)</div>
              </div>
            </div>
            <span class="link">ดูประวัติ →</span>
          </div>
        </div>
      </div>
      {nav(4, link=True)}
    </div>
    '''

def s34_volunteer_hours():
    """34. Volunteer Hours Tracker (บันทึกชั่วโมงจิตอาสา & กิจกรรมพัฒนานิสิต)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("ชั่วโมงจิตอาสา & กิจกรรมสะสม", back=True, back_target="S07")}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Hero Progress Card -->
        <div class="card" style="background:linear-gradient(135deg,#059669 0%,#10B981 100%);color:#fff;border:none;padding:20px;box-shadow:0 12px 28px rgba(16,185,129,0.3);text-align:center;">
          <div style="font-size:12px;color:#D1FAE5;font-weight:600;letter-spacing:.5px;">เกณฑ์สะสมประจำปีการศึกษา 2569</div>
          <div style="font:800 42px 'Inter';color:#fff;margin:6px 0;">36 / 36 <span style="font-size:18px;font-weight:500;">ชม.</span></div>
          <div style="display:inline-block;padding:4px 14px;background:rgba(255,255,255,0.22);border-radius:20px;font-size:12px;font-weight:700;">
            ✓ บรรลุเกณฑ์สมบูรณ์ (100% Completed)
          </div>
          
          <div style="margin-top:16px;background:rgba(0,0,0,0.15);border-radius:10px;height:10px;overflow:hidden;">
            <div style="width:100%;height:100%;background:#FCD34D;"></div>
          </div>
          <div style="font-size:11px;color:#D1FAE5;margin-top:8px;">
            สะสมเกินเกณฑ์: +6 ชั่วโมง (รวมทั้งสิ้น 42 ชั่วโมง)
          </div>
        </div>

        <!-- Certificate Download Button -->
        <div class="card" style="padding:14px;border:1px dashed {C['blue']};background:#F8FAFF;cursor:pointer;">
          <div class="row" style="justify-content:space-between;">
            <div class="row" style="gap:10px;">
              {ic("download", 20, C['blue'])}
              <div>
                <div style="font-weight:700;font-size:13px;color:{C['blue']};">ดาวน์โหลดเอกสารรับรองดิจิทัล (e-Certificate)</div>
                <div style="font-size:11px;color:#64748B;">ลงนามดิจิทัลมาตรฐาน อว. สำหรับยื่น กยศ. และขอทุน</div>
              </div>
            </div>
            <span class="badge b-blue">PDF</span>
          </div>
        </div>

        <!-- Activities Log -->
        <div class="sec"><span>รายการกิจกรรมที่ผ่านการอนุมัติ (4 รายการ)</span></div>

        <!-- Event 1 -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">อาสาพัฒนาห้องสมุดดิจิทัล รร.วัดพระปฐมเจดีย์</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">4 ต.ค. 2569 • รับรองโดย คณะศึกษาศาสตร์</div>
            </div>
            <span class="badge b-green">+8 ชั่วโมง</span>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">พี่เลี้ยงค่ายนวัตกรรม EdTech Camp 2026</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">20-21 ก.ย. 2569 • รับรองโดย สาขาเทคโนโลยีการศึกษา</div>
            </div>
            <span class="badge b-green">+16 ชั่วโมง</span>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">บริจาคโลหิต สภากาชาดไทย (จุดบริการสนามจันทร์)</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">12 ส.ค. 2569 • รับรองโดย กองกิจการนักศึกษา</div>
            </div>
            <span class="badge b-green">+6 ชั่วโมง</span>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="card" style="padding:14px;">
          <div class="row" style="justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">จิตอาสาฟื้นฟูทัศนียภาพสระแก้ว พระราชวังสนามจันทร์</div>
              <div style="font-size:11px;color:#64748B;margin-top:2px;">28 ก.ค. 2569 • รับรองโดย มหาวิทยาลัยศิลปากร</div>
            </div>
            <span class="badge b-green">+6 ชั่วโมง</span>
          </div>
        </div>

        <!-- Add New Log Button -->
        <div style="margin-top:8px;">
          {btn("ยื่นหลักฐานเข้าร่วมกิจกรรมจิตอาสาใหม่ (+)", "bp", go="S28")}
        </div>
      </div>
      {nav(4, link=True)}
    </div>
    '''

def s35_dormitory():
    """35. Dormitory Life & Utility Pay (จัดการหอพัก & บิลค่าน้ำค่าไฟ)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("หอพักนักศึกษา & ค่าสาธารณูปโภค", back=True, back_target="S07")}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Residence Overview Card -->
        <div class="card" style="background:linear-gradient(135deg,#1E293B 0%,#0F172A 100%);color:#fff;border:none;padding:18px 20px;box-shadow:0 12px 28px rgba(0,0,0,0.3);">
          <div class="row" style="justify-content:space-between;">
            <div>
              <div style="font-size:11px;color:{C['cyan']};letter-spacing:.5px;">หอพักในมหาวิทยาลัยศิลปากร</div>
              <div style="font-weight:800;font-size:18px;color:#fff;margin-top:2px;">หอพักทับแก้ว 3</div>
              <div style="font-size:12px;color:#94A3B8;">ชั้น 4 • ห้องพัก 412 (เตียง A)</div>
            </div>
            <div style="width:44px;height:44px;border-radius:14px;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;color:{C['cyan']};">
              {ic("bed", 24, C['cyan'])}
            </div>
          </div>

          <div class="row" style="gap:12px;margin-top:16px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.12);">
            <div class="badge b-green">● กำลังเข้าพัก (Active)</div>
            <div class="badge b-blue">ห้องปรับอากาศ 2 คน</div>
            <div class="badge b-grey">เพื่อนร่วมห้อง: กานต์ ก.</div>
          </div>
        </div>

        <!-- Monthly Bill Breakdown Card -->
        <div class="card" style="padding:16px;">
          <div class="row" style="justify-content:space-between;align-items:center;margin-bottom:12px;">
            <div style="font-weight:700;font-size:14px;color:{C['navy']};">ใบแจ้งหนี้ประจำงวด ตุลาคม 2569</div>
            <span class="badge b-amber">รอชำระ (Due 25 ต.ค.)</span>
          </div>

          <div class="col" style="gap:10px;font-size:13px;">
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">ค่าเช่าห้องพักรายเดือน (รวมส่วนกลาง)</span>
              <span style="font-weight:600;color:{C['navy']};">฿ 2,400.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <div>
                <span style="color:#64748B;">ค่าน้ำประปา</span>
                <span style="font-size:11px;color:#94A3B8;"> (312 ➔ 324 | 12 หน่วย × 18฿)</span>
              </div>
              <span style="font-weight:600;color:{C['navy']};">฿ 216.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <div>
                <span style="color:#64748B;">ค่าไฟฟ้า</span>
                <span style="font-size:11px;color:#94A3B8;"> (1,480 ➔ 1,575 | 95 หน่วย × 6฿)</span>
              </div>
              <span style="font-weight:600;color:{C['navy']};">฿ 570.00</span>
            </div>
            <div class="row" style="justify-content:space-between;">
              <span style="color:#64748B;">อินเทอร์เน็ต Wi-Fi หอพักความเร็วสูง</span>
              <span style="font-weight:600;color:{C['green']};">ฟรี (สวัสดิการ ม.)</span>
            </div>
            <div class="sep" style="margin:4px 0;"></div>
            <div class="row" style="justify-content:space-between;font-weight:700;">
              <span style="color:{C['navy']};">ยอดสุทธิที่ต้องชำระ</span>
              <span style="color:{C['blue']};font-size:18px;font-family:'Inter';">฿ 3,186.00</span>
            </div>
          </div>

          <div style="margin-top:16px;">
            {btn("ชำระด้วยกระเป๋า Camplus / PromptPay", "bp", go="S30", icon="qr", style="height:46px;")}
          </div>
        </div>

        <!-- Quick Dorm Services -->
        <div class="sec"><span>บริการพิเศษสำหรับชาวหอพัก</span></div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <div class="card" style="padding:12px;cursor:pointer;" data-go="S28">
            <div style="font-size:20px;margin-bottom:4px;">🔧</div>
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">แจ้งซ่อมบำรุง</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">แอร์ ไฟดับ ก๊อกน้ำชำรุด</div>
          </div>
          <div class="card" style="padding:12px;cursor:pointer;" data-go="S28">
            <div style="font-size:20px;margin-bottom:4px;">🌙</div>
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">ขอเข้าหอหลังเที่ยงคืน</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">e-Pass ขออนุมัติออนไลน์</div>
          </div>
          <div class="card" style="padding:12px;cursor:pointer;" data-go="S09">
            <div style="font-size:20px;margin-bottom:4px;">📦</div>
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">พัสดุมาถึง</div>
            <div style="font-size:11px;color:{C['green']};margin-top:2px;">มี 1 กล่องรอรับที่ป้อม</div>
          </div>
          <div class="card" style="padding:12px;cursor:pointer;" data-go="S25">
            <div style="font-size:20px;margin-bottom:4px;">🧺</div>
            <div style="font-weight:700;font-size:13px;color:{C['navy']};">เครื่องซักผ้า Smart</div>
            <div style="font-size:11px;color:#64748B;margin-top:2px;">เครื่อง 3 ชั้น 1 ว่างอยู่</div>
          </div>
        </div>
      </div>
      {nav(4, link=True)}
    </div>
    '''

def s36_community():
    """36. Community Forum (กระดานสนทนานักศึกษา & ชุมชนสถาบัน)"""
    return f'''
    <div class="scr">
      {sb()}
      {bar("กระดานสนทนานักศึกษา (Community)", back=True, back_target="S07", right=f'<div class="ib" data-go="S37" style="cursor:pointer;">{ic("discord", 20, "#5865F2")}</div>')}
      <div class="body" style="padding:0 20px 100px;gap:14px;overflow-y:auto;">
        <!-- Filter Category Chips -->
        <div class="chips">
          <div class="chip on">ทั้งหมด (All)</div>
          <div class="chip">คณะศึกษาศาสตร์</div>
          <div class="chip">หาเพื่อนติว/อ่านหนังสือ</div>
          <div class="chip">รีวิวหอพัก/ของกิน</div>
          <div class="chip">แจกสรุปแนวข้อสอบ</div>
        </div>

        <!-- Post 1 -->
        <div class="card" style="padding:14px;cursor:pointer;" data-go="S37">
          <div class="row" style="gap:10px;">
            {avatar(36, ring=C['blue'])}
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">{USER['th']} (คุณ)</div>
              <div style="font-size:11px;color:#64748B;">เทคโนโลยีการศึกษา ปี 3 • 2 ชม. ที่แล้ว</div>
            </div>
          </div>
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-top:10px;line-height:1.4;">
            [วิชา 462301] สื่อนวัตกรรม อาจารย์ให้ทำโปรเจกต์เดี่ยวหรือกลุ่มครับ? แล้วสอบกลางภาคเป็นปรนัยหรืออัตนัย?
          </div>
          <div class="row" style="gap:8px;margin-top:8px;">
            <span class="badge b-blue">#เทคโนการศึกษา</span>
            <span class="badge b-grey">#สอบกลางภาค</span>
          </div>
          <div class="row" style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;justify-content:space-between;font-size:12px;color:#64748B;">
            <div class="row" style="gap:14px;">
              <span class="row" style="gap:4px;">{ic("heart", 14, C['red'])} 34</span>
              <span class="row" style="gap:4px;">💬 18 ความคิดเห็น</span>
            </div>
            <span style="color:{C['blue']};font-weight:600;">ตอบกระทู้ →</span>
          </div>
        </div>

        <!-- Post 2 -->
        <div class="card" style="padding:14px;cursor:pointer;" data-go="S37">
          <div class="row" style="gap:10px;">
            <div style="width:36px;height:36px;border-radius:50%;background:#FCE7F3;display:flex;align-items:center;justify-content:center;color:#BE185D;font-weight:700;font-size:13px;">
              รด
            </div>
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">รินดา ใจดี</div>
              <div style="font-size:11px;color:#64748B;">คณะอักษรศาสตร์ ปี 2 • 4 ชม. ที่แล้ว</div>
            </div>
          </div>
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-top:10px;line-height:1.4;">
            รีวิวข้าวกะเพราหมูกรอบร้านป้าพร โรงอาหารเพชรรัตน วันนี้จ่ายด้วยกระเป๋า Camplus ได้ส่วนลดเงินอุดหนุนอีก 5 บาท คุ้มมากก 🍛
          </div>
          <div class="row" style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;justify-content:space-between;font-size:12px;color:#64748B;">
            <div class="row" style="gap:14px;">
              <span class="row" style="gap:4px;">{ic("heart", 14, C['red'])} 89</span>
              <span class="row" style="gap:4px;">💬 45 ความคิดเห็น</span>
            </div>
            <span style="color:{C['blue']};font-weight:600;">ตอบกระทู้ →</span>
          </div>
        </div>

        <!-- Post 3 -->
        <div class="card" style="padding:14px;cursor:pointer;" data-go="S37">
          <div class="row" style="gap:10px;">
            <div style="width:36px;height:36px;border-radius:50%;background:#FEF3C7;display:flex;align-items:center;justify-content:center;color:#B45309;font-weight:700;font-size:13px;">
              พพ
            </div>
            <div>
              <div style="font-weight:700;font-size:13px;color:{C['navy']};">พีรพล ส.</div>
              <div style="font-size:11px;color:#64748B;">คณะวิทยาศาสตร์ ปี 4 • 6 ชม. ที่แล้ว</div>
            </div>
          </div>
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-top:10px;line-height:1.4;">
            หาเพื่อนหารค่า Grab ไปสถานีรถไฟนครปฐม วันศุกร์นี้ 15:30 น. หน้าตึกศึกษา 3 ทักแชตด่วนครับ 🚗
          </div>
          <div class="row" style="margin-top:12px;padding-top:10px;border-top:1px solid #F1F5F9;justify-content:space-between;font-size:12px;color:#64748B;">
            <div class="row" style="gap:14px;">
              <span class="row" style="gap:4px;">{ic("heart", 14, C['red'])} 12</span>
              <span class="row" style="gap:4px;">💬 7 ความคิดเห็น</span>
            </div>
            <span style="color:{C['blue']};font-weight:600;">ตอบกระทู้ →</span>
          </div>
        </div>
      </div>

      <!-- Floating New Post Button -->
      <div style="position:absolute;right:24px;bottom:90px;z-index:20;">
        <div style="width:54px;height:54px;border-radius:50%;background:{C['blue']};color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 25px rgba(36,107,253,0.45);cursor:pointer;" data-go="S37">
          {ic("plus", 26, "#fff", w=2.5)}
        </div>
      </div>
      {nav(0, link=True)}
    </div>
    '''

def s37_discord_matrix():
    """37. Thai Suksa Discord-like Matrix Lounge (ห้องสนทนาเสียง & แชตรวมมหาลัย)"""
    return f'''
    <div class="scr" style="background:#1E1F22;color:#DBDEE1;">
      {sb(dark=True)}
      <!-- Top Discord Header Bar -->
      <div class="bar" style="background:#2B2D31;border-bottom:1px solid #1F2023;color:#F2F3F5;justify-content:space-between;">
        <div class="row" style="gap:10px;">
          <div class="ib" data-go="S07" style="background:transparent;border:none;color:#DBDEE1;cursor:pointer;">
            {ic("left", 20, "#DBDEE1")}
          </div>
          <span style="font-weight:700;font-size:15px;color:#F2F3F5;"># 💬-ห้องแชตรวม-edtech-ปี3</span>
        </div>
        <div class="row" style="gap:10px;">
          {ic("users", 20, "#DBDEE1")}
          {ic("search", 20, "#DBDEE1")}
        </div>
      </div>

      <!-- Main Discord Layout: Left Server Rail + Channels Body -->
      <div style="flex:1;display:flex;overflow:hidden;">
        <!-- Server Rail (Left 60px) -->
        <div style="width:62px;background:#1E1F22;padding:12px 0;display:flex;flex-direction:column;align-items:center;gap:10px;border-right:1px solid #2B2D31;">
          <!-- Server 1: Thai Suksa National -->
          <div style="width:44px;height:44px;border-radius:14px;background:#5865F2;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;">
            <div style="position:absolute;left:-8px;width:4px;height:24px;background:#fff;border-radius:0 4px 4px 0;"></div>
            {img("thai_suksa_logo.png", "width:40px;height:40px;border-radius:12px;object-fit:cover;")}
          </div>

          <!-- Server 2: Silpakorn Official -->
          <div style="width:44px;height:44px;border-radius:22px;background:#2B2D31;display:flex;align-items:center;justify-content:center;cursor:pointer;">
            {uni_seal("silpakorn", s=34)}
          </div>

          <!-- Server 3: Faculty of Education -->
          <div style="width:44px;height:44px;border-radius:22px;background:#2B2D31;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#22C55E;font-weight:700;font-size:13px;">
            ED
          </div>

          <!-- Add Server -->
          <div style="width:44px;height:44px;border-radius:22px;background:#2B2D31;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#22C55E;">
            {ic("plus", 20, "#22C55E")}
          </div>
        </div>

        <!-- Channels & Chat Area -->
        <div style="flex:1;background:#2B2D31;display:flex;flex-direction:column;overflow-y:auto;padding:12px 14px;">
          <!-- Category: Text Channels -->
          <div style="font-size:11px;font-weight:700;color:#949BA4;letter-spacing:.5px;margin-bottom:6px;">TEXT CHANNELS</div>
          
          <div style="padding:8px 10px;border-radius:6px;background:rgba(255,255,255,0.06);color:#F2F3F5;font-size:13px;font-weight:600;display:flex;align-items:center;gap:8px;margin-bottom:4px;cursor:pointer;">
            <span style="color:#949BA4;">#</span> 💬-ห้องแชตรวม-edtech-ปี3
          </div>
          <div style="padding:8px 10px;border-radius:6px;color:#949BA4;font-size:13px;display:flex;align-items:center;gap:8px;margin-bottom:4px;cursor:pointer;">
            <span>#</span> 📣-ประกาศด่วน-คณะ
          </div>
          <div style="padding:8px 10px;border-radius:6px;color:#949BA4;font-size:13px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;">
            <span>#</span> 📚-แชร์ชีทสรุป-แนวข้อสอบ
          </div>

          <!-- Category: Voice Channels -->
          <div style="font-size:11px;font-weight:700;color:#949BA4;letter-spacing:.5px;margin-bottom:6px;">VOICE CHANNELS (ห้องเสียงสด)</div>
          
          <!-- Active Voice Channel 1 -->
          <div style="background:#1F2023;border-radius:8px;padding:10px 12px;margin-bottom:8px;">
            <div class="row" style="justify-content:space-between;color:#23A55A;font-weight:700;font-size:13px;">
              <div class="row" style="gap:6px;">
                <span>🔊</span> ห้องติววิจัยการศึกษา
              </div>
              <span class="badge b-green" style="font-size:10px;background:#23A55A;color:#fff;">4 คน</span>
            </div>

            <!-- Participants List -->
            <div style="margin-top:8px;display:flex;flex-direction:column;gap:6px;padding-left:14px;">
              <div class="row" style="gap:8px;font-size:12px;color:#F2F3F5;">
                <div style="width:8px;height:8px;border-radius:50%;background:#23A55A;"></div>
                <span>{USER['th_full']} (คุณ) 🎙️</span>
              </div>
              <div class="row" style="gap:8px;font-size:12px;color:#949BA4;">
                <div style="width:8px;height:8px;border-radius:50%;background:#23A55A;"></div>
                <span>กานต์ กิจเกษม</span>
              </div>
              <div class="row" style="gap:8px;font-size:12px;color:#949BA4;">
                <div style="width:8px;height:8px;border-radius:50%;background:#23A55A;"></div>
                <span>รินดา ใจดี</span>
              </div>
              <div class="row" style="gap:8px;font-size:12px;color:#949BA4;">
                <div style="width:8px;height:8px;border-radius:50%;background:#23A55A;"></div>
                <span>พีรพล สุขสมบัติ</span>
              </div>
            </div>
          </div>

          <!-- Voice Channel 2 -->
          <div style="padding:8px 10px;border-radius:6px;color:#949BA4;font-size:13px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;">
            <div class="row" style="gap:6px;">
              <span>🔊</span> Lounge หน้าหอพัก 3
            </div>
            <span style="font-size:11px;">2 คน</span>
          </div>
        </div>
      </div>

      <!-- Discord Bottom Connected Voice Banner -->
      <div style="background:#111214;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid #1F2023;">
        <div class="row" style="gap:10px;">
          <div style="width:36px;height:36px;border-radius:50%;background:#23A55A;display:flex;align-items:center;justify-content:center;color:#fff;">
            {ic("mic", 18, "#fff")}
          </div>
          <div>
            <div style="font-size:12px;font-weight:700;color:#23A55A;">เชื่อมต่อเสียงอยู่: ห้องติววิจัย</div>
            <div style="font-size:11px;color:#949BA4;">RTC Connected / Ping 18ms</div>
          </div>
        </div>

        <div class="row" style="gap:8px;">
          <div style="width:34px;height:34px;border-radius:8px;background:#2B2D31;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#DBDEE1;">
            {ic("settings", 16, "#DBDEE1")}
          </div>
          <div style="width:34px;height:34px;border-radius:8px;background:#DA373C;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff;" data-go="S36">
            ✕
          </div>
        </div>
      </div>
      {hi()}
    </div>
    '''

def s38_ai_assistant():
    """38. ไทยศึกษา AI Campus Copilot (AI ผู้ช่วยอัจฉริยะประจำชีวิตในมอ)"""
    return f'''
    <div class="scr">
      {sb()}
      <div class="bar" style="background:#fff;justify-content:space-between;">
        <div class="ib" data-go="S07" style="cursor:pointer;">{ic("left")}</div>
        <div class="row" style="gap:10px;">
          <div style="width:36px;height:36px;border-radius:12px;overflow:hidden;">
            {img("ai_avatar.jpg", "width:100%;height:100%;object-fit:cover;")}
          </div>
          <div style="text-align:left;">
            <div style="font-weight:700;font-size:14px;color:{C['navy']};">ไทยศึกษา AI Copilot</div>
            <div style="font-size:11px;color:{C['green']};">● พร้อมตอบคำถามชีวิตในมอ</div>
          </div>
        </div>
        <div class="ib" data-go="S08" style="cursor:pointer;">{ic("menu")}</div>
      </div>

      <div class="body" style="padding:10px 20px;gap:12px;overflow-y:auto;display:flex;flex-direction:column;justify-content:space-between;">
        <!-- Chat Flow -->
        <div style="display:flex;flex-direction:column;gap:12px;">
          <!-- AI Message 1 -->
          <div class="row" style="gap:10px;align-items:flex-start;">
            <div style="width:32px;height:32px;border-radius:10px;overflow:hidden;flex:none;">
              {img("ai_avatar.jpg", "width:100%;height:100%;object-fit:cover;")}
            </div>
            <div class="card" style="max-width:82%;padding:12px 14px;background:#fff;border-radius:4px 18px 18px 18px;font-size:13px;line-height:1.5;">
              สวัสดีครับคุณ{USER['th']}! ผมคือ AI ผู้ช่วยประจำสถาบัน มีอะไรให้ผมช่วยแนะนำเกี่ยวกับวิชาเรียน ห้องสอบ ทุน กยศ. หรือการยื่นคำร้องไหมครับ?
            </div>
          </div>

          <!-- User Message -->
          <div class="row" style="justify-content:flex-end;">
            <div class="card" style="max-width:80%;padding:12px 14px;background:{C['blue']};color:#fff;border-radius:18px 4px 18px 18px;font-size:13px;line-height:1.5;">
              วิชาเรียนถัดไปของฉันวันนี้เรียนห้องไหน และเดินไปยังไง?
            </div>
          </div>

          <!-- AI Message 2 with Action Card -->
          <div class="row" style="gap:10px;align-items:flex-start;">
            <div style="width:32px;height:32px;border-radius:10px;overflow:hidden;flex:none;">
              {img("ai_avatar.jpg", "width:100%;height:100%;object-fit:cover;")}
            </div>
            <div class="card" style="max-width:85%;padding:14px;background:#fff;border-radius:4px 18px 18px 18px;font-size:13px;line-height:1.5;">
              <div>วิชาถัดไปคือ <strong>462301 สื่อนวัตกรรมการเรียนรู้</strong> ครับ</div>
              <div style="margin-top:6px;color:#64748B;">📍 อาคารศึกษา 3 ห้อง ED-304 (09:00 - 12:00 น.)</div>
              <div style="margin-top:10px;">
                {btn("เปิดแผนที่นำทางไปตึกนี้", "bp", go="S23", icon="nav", style="height:38px;font-size:12px;padding:0 12px;")}
              </div>
            </div>
          </div>

          <!-- AI Message 3: GPA & Financial Insight -->
          <div class="row" style="gap:10px;align-items:flex-start;">
            <div style="width:32px;height:32px;border-radius:10px;overflow:hidden;flex:none;">
              {img("ai_avatar.jpg", "width:100%;height:100%;object-fit:cover;")}
            </div>
            <div class="card" style="max-width:85%;padding:14px;background:#F0FDF4;border-color:#BBF7D0;border-radius:4px 18px 18px 18px;font-size:13px;line-height:1.5;">
              <div style="font-weight:700;color:{C['green']};">💡 แจ้งเตือนสวัสดิการ & ทุน</div>
              <div style="margin-top:4px;color:#166534;">
                ยอดเงินค่าครองชีพ กยศ. ประจำงวดเดือนนี้ (฿ 3,000) มีกำหนดโอนเข้าบัญชีในวันที่ <strong>25 ต.ค. 69</strong> และชั่วโมงจิตอาสาของคุณครบ 36 ชม. แล้วครับ!
              </div>
              <div class="row" style="gap:8px;margin-top:10px;">
                {btn("ตรวจยอด กยศ.", "bp", go="S33", style="height:32px;font-size:11px;padding:0 10px;background:#059669;")}
                {btn("ดูกระเป๋า Camplus", "bn", go="S29", style="height:32px;font-size:11px;padding:0 10px;")}
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Prompt Chips & Input -->
        <div style="margin-top:auto;display:flex;flex-direction:column;gap:8px;padding-bottom:12px;">
          <div class="chips">
            <div class="chip">ขอหนังสือรับรองทำอย่างไร?</div>
            <div class="chip">หอสมุดปิดกี่โมง?</div>
            <div class="chip">รถรางรอบถัดไป</div>
            <div class="chip">ค่าเทอมเทอมนี้เท่าไหร่?</div>
          </div>
          <div class="row" style="gap:8px;">
            {field("พิมพ์คำถามเรื่องการเรียน สถาบัน หรือทุน...", icon=None, style="flex:1;")}
            <div class="btn bp" style="width:52px;height:52px;padding:0;border-radius:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;">
              {ic("send", 20, "#fff")}
            </div>
          </div>
        </div>
      </div>
      {hi()}
    </div>
    '''

# ---------------------------------------------------------------------------
# Board Layout & SVG Connector Generator
# ---------------------------------------------------------------------------

SCREENS = [
                # Row 1: Auth, Thai ID Verification & Central SSO (Cols 0..7)
    ("S01", "01. Splash Screen", s01_splash, 0, 0, "ระบบเข้าสู่ระบบและเครือข่ายสถาบัน (Authentication & Central University Portal)"),
    ("S02", "02. Welcome / Onboarding", s02_welcome, 0, 1, ""),
    ("S05", "05. ยืนยันตัวตนด้วย Thai ID", s05_thaid_registration, 0, 2, ""),
    ("S03", "03. เลือกมหาวิทยาลัย (55+ แห่ง)", s03_select_university, 0, 3, ""),
    ("S04B", "04B. มหาวิทยาลัย SSO Webview (SU-NET SSO)", s04b_sso_webview, 0, 4, ""),
    ("S05B", "05B. เชื่อมต่อบัญชีโซเชียล", s05b_social_linking, 0, 5, ""),
    ("S04", "04. เข้าสู่ระบบ (Login & Social Platforms)", s04_login, 0, 6, ""),
    ("S06", "06. ลืมรหัสผ่าน & OTP", s06_forgot_password, 0, 7, ""),




    # Row 2: Home, Drawer & Profile (Cols 0..4)
    ("S07", "07. หน้าหลัก (Home Dashboard)", s07_home, 1, 0, "หน้าหลัก, เมนูระบบ และข้อมูลส่วนตัว (Home, Drawer & Profile)"),
    ("S08", "08. Hamburger Menu Drawer [Overlay]", s08_hamburger_drawer, 1, 1, ""),
    ("S09", "09. การแจ้งเตือน (Notifications)", s09_notifications, 1, 2, ""),
    ("S10", "10. โปรไฟล์นักศึกษา (Student Profile)", s10_profile, 1, 3, ""),
    ("S11", "11. บัตรนักศึกษาดิจิทัล (Digital ID)", s11_digital_id, 1, 4, ""),

    # Row 3: Schedule, Details & Calendar (Cols 0..3)
    ("S12", "12. ตารางเรียนรายสัปดาห์ (Schedule)", s12_schedule, 2, 0, "วิชาการ, ตารางเรียน และตารางสอบ (Academics, Schedule & Exams)"),
    ("S13", "13. รายละเอียดวิชาเรียน [Bottom Sheet]", s13_class_details, 2, 1, ""),
    ("S14", "14. ตารางสอบ (Exam Schedule)", s14_exam_schedule, 2, 2, ""),
    ("S15", "15. ปฏิทิน & เพิ่มกิจกรรม (Calendar)", s15_calendar, 2, 3, ""),

    # Row 4: News & Activities (Cols 0..4)
    ("S16", "16. ข่าวสาร & ประกาศ (News Feed)", s16_news_feed, 3, 0, "ข่าวสารและกิจกรรมมหาวิทยาลัย (News & Campus Activities)"),
    ("S17", "17. รายละเอียดข่าวสาร (News Details)", s17_news_details, 3, 1, ""),
    ("S18", "18. กิจกรรมและชมรม (Activities & Clubs)", s18_activities, 3, 2, ""),
    ("S19", "19. รายละเอียดกิจกรรม (Event Details)", s19_activity_details, 3, 3, ""),
    ("S20", "20. ยืนยันการลงทะเบียน [Modal Popup]", s20_registration_confirm, 3, 4, ""),

    # Row 5: Campus Map & Navigation (Cols 0..3)
    ("S21", "21. แผนที่วิทยาเขต (Campus Map)", s21_campus_map, 4, 0, "แผนที่และการเดินทางอัจฉริยะ (Campus Map, Navigation & Live EV Tram)"),
    ("S22", "22. รายละเอียดอาคารเรียน (Building Info)", s22_place_details, 4, 1, ""),
    ("S23", "23. เส้นทางการเดินทาง (Directions)", s23_directions, 4, 2, ""),
    ("S24", "24. รถรางไฟฟ้าสด (Live EV Tram)", s24_smart_transit, 4, 3, ""),

    # Row 6: Smart Space, Fleet & Services (Cols 0..3)
    ("S25", "25. จองห้องติว & พื้นที่ (Room Booking)", s25_room_booking, 5, 0, "ระบบจองพื้นที่, ยานพาหนะ และบริการคำร้อง (Smart Space, Fleet Rental & e-Petitions)"),
    ("S26", "26. ตั๋วการจอง & QR เข้าห้อง [Modal]", s26_booking_confirm, 5, 1, ""),
    ("S27", "27. ยืม-คืนยานพาหนะ & อุปกรณ์ (Fleet Rental)", s27_fleet_rental, 5, 2, ""),
    ("S28", "28. คำร้องออนไลน์ (Student e-Services)", s28_student_services, 5, 3, ""),

    # Row 7: Welfare, Finance & Living (Cols 0..6)
    ("S29", "29. กระเป๋าเงินดิจิทัล (Campus Wallet)", s29_wallet, 6, 0, "สวัสดิการ, การเงิน และการใช้ชีวิตในมอ (Welfare, Finance & Campus Living)"),
    ("S30", "30. สแกนจ่ายเงินโรงอาหาร (QR Pay)", s30_scan_pay, 6, 1, ""),
    ("S31", "31. สลิปชำระเงินดิจิทัล (e-Receipt Slip)", s31_payment_slip, 6, 2, ""),
    ("S32", "32. ชำระค่าลงทะเบียน & ค่าเทอม (Tuition Pay)", s32_tuition_pay, 6, 3, ""),
    ("S33", "33. ระบบกองทุน กยศ. ดิจิทัล (Student Loan)", s33_student_loan, 6, 4, ""),
    ("S34", "34. ชั่วโมงจิตอาสาสะสม (Volunteer Tracker)", s34_volunteer_hours, 6, 5, ""),
    ("S35", "35. หอพักนักศึกษา & บิลค่าน้ำไฟ (Dormitory)", s35_dormitory, 6, 6, ""),

    # Row 8: Community & AI Assistant (Cols 0..2)
    ("S36", "36. กระดานสนทนานักศึกษา (Community Forum)", s36_community, 7, 0, "สังคมนักศึกษา, ห้องสนทนาเสียง และ AI ผู้ช่วย (Community, Discord Lounge & AI Copilot)"),
    ("S37", "37. ไทยศึกษา Discord Lounge (Matrix Voice)", s37_discord_matrix, 7, 1, ""),
    ("S38", "38. ไทยศึกษา AI Campus Copilot (AI Assistant)", s38_ai_assistant, 7, 2, ""),
]

# Grid Spacing
COL_W = 440
COL_GAP = 140
ROW_H = 956
ROW_GAP = 280
ORIGIN_X = 120
ORIGIN_Y = 220

def get_screen_coords(col, row):
    x = ORIGIN_X + col * (COL_W + COL_GAP)
    y = ORIGIN_Y + row * (ROW_H + ROW_GAP)
    return x, y

def inject_screen_pos(html, s_id, x, y):
    """Safely inject left/top position and id without creating duplicate style attributes."""
    m = re.search(r'<div\s+([^>]*class=[\'"]scr[\'"][^>]*)>', html)
    if not m:
        return html
    attrs = m.group(1)
    
    # Check if style attribute exists
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

def generate_board():
    screen_positions = {}
    screens_html = ""
    row_headers_html = ""

    for s_id, title, func, r, c, section_title in SCREENS:
        x, y = get_screen_coords(c, r)
        screen_positions[s_id] = (x, y)

        if section_title:
            row_headers_html += f'''
            <div class="rowtitle" style="left:{ORIGIN_X}px;top:{y - 100}px;">
              <span style="color:{C['blue']};margin-right:12px;">#</span>{section_title}
            </div>
            '''

        # Label above screen
        label_html = f'''
        <div class="lbl" style="left:{x}px;top:{y - 46}px;">
          <span style="background:{C['blue']};color:#fff;padding:2px 8px;border-radius:6px;font-size:12px;font-weight:700;margin-right:8px;">{s_id}</span>
          {title}
        </div>
        '''

        # Render screen content and safely inject position
        content = func()
        screen_wrapped = inject_screen_pos(content, s_id, x, y)
        screens_html += label_html + "\n" + screen_wrapped + "\n"

    # -----------------------------------------------------------------------
    # Connections / Prototype Flow Arrows
    # -----------------------------------------------------------------------
        connections = [
                                # Auth & Registration Flow
        ("S01", "S02", "On Load / Auto", "right", "left"),
        ("S02", "S04", "เข้าสู่ระบบ", "right", "left"),
        ("S02", "S05", "ลงทะเบียนใหม่ด้วย Thai ID", "right", "left"),
        ("S05", "S03", "ยืนยัน ThaID -> เลือกสถาบัน", "right", "left"),
        ("S03", "S04B", "เลือกสถาบัน -> SU-NET SSO", "right", "left"),
        ("S04B", "S05B", "SSO สำเร็จ -> เชื่อมต่อโซเชียล", "right", "left"),
        ("S05B", "S04", "เสร็จสิ้น / ข้าม -> ไปหน้า Login", "right", "left"),
        ("S04", "S04B", "เข้าสู่ระบบด้วย SU-NET SSO", "left", "right"),
        ("S04", "S07", "เข้าสู่ระบบสำเร็จ -> หน้าหลัก", "bottom", "top"),
        ("S04", "S06", "ลืมรหัสผ่าน", "right", "left"),

        # Home & Drawer Flow
        ("S07", "S08", "เปิดแฮมเบอร์เกอร์เมนู", "right", "left"),
        ("S07", "S09", "เปิดการแจ้งเตือน", "right", "left"),
        ("S07", "S10", "ดูโปรไฟล์นักศึกษา", "right", "left"),
        ("S07", "S11", "เปิดบัตรนักศึกษา Digital ID", "right", "left"),
        ("S07", "S13", "คลิกวิชาถัดไป -> รายละเอียด", "bottom", "top"),
        ("S07", "S12", "ปุ่มลัดตารางเรียน", "bottom", "top"),
        ("S07", "S21", "ปุ่มลัดแผนที่", "bottom", "top"),
        ("S07", "S25", "ปุ่มลัดจองห้อง", "bottom", "top"),
        ("S07", "S27", "ปุ่มลัดยืมรถ/อุปกรณ์", "bottom", "top"),
        ("S07", "S29", "ปุ่มลัดกระเป๋าเงิน Camplus", "bottom", "top"),
        ("S07", "S32", "ปุ่มลัดจ่ายค่าเทอม", "bottom", "top"),
        ("S07", "S33", "ปุ่มลัดตรวจ กยศ.", "bottom", "top"),
        ("S07", "S35", "ปุ่มลัดหอพักนักศึกษา", "bottom", "top"),
        ("S07", "S36", "ปุ่มลัดกระดานชุมชน", "bottom", "top"),
        ("S07", "S38", "ปุ่มลัด AI Copilot", "bottom", "top"),

        # Schedule Flow
        ("S12", "S13", "คลิกการ์ดวิชา -> เปิด Sheet", "right", "left"),
        ("S12", "S14", "สลับแท็บตารางสอบ", "right", "left"),
        ("S12", "S15", "เปิดปฏิทิน & เพิ่มนัด", "right", "left"),
        ("S13", "S23", "กดนำทาง -> เปิดแผนที่เส้นทาง", "bottom", "top"),

        # News & Activities Flow
        ("S16", "S17", "คลิกข่าว -> อ่านรายละเอียด", "right", "left"),
        ("S18", "S19", "คลิกกิจกรรม -> ดูเงื่อนไข", "right", "left"),
        ("S19", "S20", "กดลงทะเบียน -> Modal สำเร็จ", "right", "left"),
        ("S20", "S15", "บันทึกกิจกรรมลงปฏิทิน", "top", "bottom"),

        # Campus Map & Transit Flow
        ("S21", "S22", "แตะหมุดตึก -> ดูรายละเอียด", "right", "left"),
        ("S22", "S23", "กดนำทาง -> แผนที่เส้นทาง", "right", "left"),
        ("S21", "S24", "เปิดแทร็กเกอร์รถราง EV", "right", "left"),

        # Space Booking & Fleet Flow
        ("S25", "S26", "เลือกช่วงเวลา -> Modal สำเร็จ & QR", "right", "left"),
        ("S27", "S26", "สแกนยืมรถ/อุปกรณ์ -> Access QR", "left", "right"),
        ("S28", "S07", "ส่งคำร้องสำเร็จ -> กลับหน้าหลัก", "bottom", "top"),

        # Welfare, Finance & Living Flow
        ("S29", "S30", "แตะสแกนคิวอาร์ -> เปิดกล้อง", "right", "left"),
        ("S30", "S31", "ยืนยันยอดเงิน -> สลิปดิจิทัล", "right", "left"),
        ("S31", "S29", "เสร็จสิ้น -> กลับกระเป๋าเงิน", "bottom", "bottom"),
        ("S32", "S31", "ชำระค่าเทอม -> ออกใบเสร็จ", "left", "right"),
        ("S32", "S33", "นักศึกษากู้ยืม -> เช็กสิทธิ กยศ.", "right", "left"),
        ("S33", "S34", "ตรวจเกณฑ์ กยศ. -> ชั่วโมงจิตอาสา", "right", "left"),
        ("S34", "S28", "ยื่นหลักฐานจิตอาสา -> คำร้อง", "bottom", "top"),
        ("S35", "S30", "กดชำระค่าน้ำไฟ -> สแกนจ่าย", "left", "right"),

        # Community & AI Flow
        ("S36", "S37", "เข้าสู่ Discord Lounge", "right", "left"),
        ("S37", "S36", "ออกจากห้องเสียง -> กลับบอร์ด", "left", "right"),
        ("S38", "S23", "AI แนะนำห้องเรียน -> นำทาง", "bottom", "top"),
        ("S38", "S33", "AI แจ้งเตือนทุน -> ตรวจ กยศ.", "bottom", "top"),
    ]

    svg_paths = ""
    svg_labels = ""

    for from_id, to_id, label, from_dir, to_dir in connections:
        if from_id not in screen_positions or to_id not in screen_positions:
            continue
        fx, fy = screen_positions[from_id]
        tx, ty = screen_positions[to_id]

        # anchor calculations
        if from_dir == "right":
            x1, y1 = fx + COL_W, fy + 480
        elif from_dir == "left":
            x1, y1 = fx, fy + 480
        elif from_dir == "bottom":
            x1, y1 = fx + COL_W // 2, fy + ROW_H
        else: # top
            x1, y1 = fx + COL_W // 2, fy

        if to_dir == "left":
            x2, y2 = tx, ty + 480
        elif to_dir == "right":
            x2, y2 = tx + COL_W, ty + 480
        elif to_dir == "top":
            x2, y2 = tx + COL_W // 2, ty
        else: # bottom
            x2, y2 = tx + COL_W // 2, ty + ROW_H

        dx = x2 - x1
        dy = y2 - y1

        # Bezier control points
        if from_dir in ("left", "right") and to_dir in ("left", "right"):
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
        svg_paths += f'''
        <g class="connector-group">
          <!-- Outer glow for visibility -->
          <path d="{path_d}" fill="none" stroke="#FFFFFF" stroke-width="6" opacity="0.9" />
          <!-- Main connector wire -->
          <path d="{path_d}" fill="none" stroke="{C['blue']}" stroke-width="3.5" stroke-dasharray="8,6" marker-end="url(#arrowhead)" />
          <!-- Source anchor dot -->
          <circle cx="{x1}" cy="{y1}" r="6" fill="{C['blue']}" stroke="#FFFFFF" stroke-width="2" />
        </g>
        '''

        svg_labels += f'''
        <g transform="translate({mid_x},{mid_y})">
          <rect x="-90" y="-14" width="180" height="28" rx="14" fill="{C['navy']}" stroke="{C['cyan']}" stroke-width="1.5" />
          <text x="0" y="4" font-family="'IBM Plex Sans Thai','Inter',sans-serif" font-size="11" font-weight="600" fill="#FFFFFF" text-anchor="middle">{label}</text>
        </g>
        '''

    max_c = max(c for _, _, _, _, c, _ in SCREENS)
    max_r = max(r for _, _, _, r, _, _ in SCREENS)
    total_w = ORIGIN_X + (max_c + 1) * (COL_W + COL_GAP) + 100
    total_h = ORIGIN_Y + (max_r + 1) * (ROW_H + ROW_GAP) + 200

    board_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>ไทยศึกษา (THAI SUKSA) — Complete 38-Screen Master Prototype Flow Board</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {CSS}
    @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
    @keyframes pulseTarget {{
      0% {{ box-shadow: 0 0 0 0 rgba(36,107,253,0.8); }}
      50% {{ box-shadow: 0 0 0 16px rgba(88,214,255,0.6), 0 25px 60px rgba(16,28,54,0.3); }}
      100% {{ box-shadow: 0 20px 50px rgba(16,28,54,.18); }}
    }}
    .pulse-target {{
      animation: pulseTarget 1.6s ease-out;
      z-index: 60 !important;
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
      padding: 8px 14px;
      border-radius: 40px;
      border: 1.5px solid rgba(88,214,255,0.4);
      box-shadow: 0 14px 35px rgba(0,0,0,0.35);
      font-family: 'IBM Plex Sans Thai','Inter',sans-serif;
    }}
    .tb-select {{
      background: rgba(255,255,255,0.1);
      color: #fff;
      border: 1px solid rgba(255,255,255,0.2);
      padding: 8px 14px;
      border-radius: 20px;
      font: 600 13px 'IBM Plex Sans Thai','Inter';
      outline: none;
      cursor: pointer;
    }}
    .tb-select option {{
      background: #101C36;
      color: #fff;
    }}
    .tb-btn {{
      background: {C['blue']};
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
    [data-go] {{
      cursor: pointer;
      transition: transform 0.15s ease, filter 0.15s ease;
    }}
    [data-go]:hover {{
      filter: brightness(1.05);
    }}
    [data-go]:active {{
      transform: scale(0.97);
    }}
  </style>
</head>
<body>

  <!-- Floating Navigation & Prototype Toolbar -->
  <div class="floating-toolbar">
    <div style="display:flex;align-items:center;gap:8px;color:#fff;font-size:13px;font-weight:700;">
      <span style="color:{C['cyan']};font-size:16px;">✦</span>
      <span>ไทยศึกษา Prototype</span>
    </div>
    
    <!-- Screen Jump Selector -->
    <select class="tb-select" onchange="jumpToScreen(this.value)">
      <option value="">-- ไปยังหน้าจอ (1-31) --</option>
      {"".join([f'<option value="{s_id}">{title}</option>' for s_id, title, _, _, _, _ in SCREENS])}
    </select>

    <!-- Wire Toggle Button -->
    <button class="tb-btn" onclick="toggleConnectors()">
      <span>⚡</span>
      <span id="toggleText">ซ่อนเส้นเชื่อม Wire</span>
    </button>
  </div>

  <div id="board" style="width:{total_w}px;height:{total_h}px;">

    <!-- Top Canvas Title Banner -->
    <div style="position:absolute;left:{ORIGIN_X}px;top:40px;display:flex;align-items:center;gap:20px;">
      <div style="width:64px;height:64px;border-radius:20px;background:#fff;border:1px solid #E5EAF2;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 25px rgba(0,0,0,0.1);">
        {img("thai_suksa_logo.png", "width:68px;height:68px;border-radius:18px;object-fit:cover;")}
      </div>
      <div>
        <div style="font:800 36px 'Inter','IBM Plex Sans Thai';color:{C['navy']};letter-spacing:.5px;">
          ไทยศึกษา (THAI SUKSA) — Smart Campus Master Flow Board
        </div>
        <div style="font-size:16px;color:#64748B;margin-top:4px;">
          มาตรฐาน iPhone 16 Pro Max (440 × 956 px) • 38 หน้าจอครบสมบูรณ์ระดับมืออาชีพ (ครอบคลุม 14 ฟังก์ชันหลักตามเกณฑ์อาจารย์ + 7 ระบบสวัสดิการและการใช้ชีวิตในมอ) • รองรับทุกมหาวิทยาลัยในสังกัดกระทรวง อว. • บัญชีตัวอย่าง: นายธนพล กิจบำรุง (670610452) ม.ศิลปากร
        </div>
      </div>
    </div>

    <!-- Row Section Titles -->
    {row_headers_html}

    <!-- 31 Screen Nodes -->
    {screens_html}

    <!-- SVG Connector Flow Layer -->
    <svg id="svgConnectors" width="{total_w}" height="{total_h}" style="position:absolute;top:0;left:0;pointer-events:none;z-index:10;">
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto">
          <polygon points="0 0, 8 4, 0 8" fill="{C['blue']}" />
        </marker>
      </defs>
      {svg_paths}
      {svg_labels}
    </svg>

  </div>

  <script>
    function toggleConnectors() {{
      var svg = document.getElementById('svgConnectors');
      var txt = document.getElementById('toggleText');
      if (svg.style.display === 'none') {{
        svg.style.display = 'block';
        txt.innerText = 'ซ่อนเส้นเชื่อม Wire';
      }} else {{
        svg.style.display = 'none';
        txt.innerText = 'แสดงเส้นเชื่อม Wire';
      }}
    }}

    function jumpToScreen(screenId) {{
      if (!screenId) return;
      var el = document.getElementById(screenId);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth', block: 'center', inline: 'center' }});
        el.classList.add('pulse-target');
        setTimeout(function() {{
          el.classList.remove('pulse-target');
        }}, 1800);
      }}
    }}

    // Bind all interactive elements with data-go
    
    
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
          var ssoBtnWrap = document.getElementById('login_sso_btn_wrap');
          if (ssoBtnWrap) {{
            ssoBtnWrap.innerHTML = '<div class="btn bn" data-go="S07" style="cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>เข้าใช้งานด้วย Single Sign-On (' + selectedAbbr + ' SSO)</div>';
          }}
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
          var ssoBtnWrap = document.getElementById('login_sso_btn_wrap');
          if (ssoBtnWrap) {{
            ssoBtnWrap.innerHTML = '<div class="btn bn" data-go="S07" style="cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>เข้าใช้งานด้วย Single Sign-On (' + selectedAbbr + ' SSO)</div>';
          }}
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
      document.body.addEventListener('click', function(e) {{
        var targetEl = e.target.closest('[data-go]');
        if (targetEl) {{
          var dest = targetEl.getAttribute('data-go');
          if (dest) {{
            jumpToScreen(dest);
          }}
        }}
      }});
    }});
  </script>

</body>
</html>
'''

    out_path = os.path.join(HERE, "ไทยศึกษา_complete_flow.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(board_html)

    

    print(f"Generated complete board with {len(SCREENS)} screens & {len(connections)} prototype connector wires!")
    print(f"Output saved to: {out_path} ({len(board_html)} bytes)")

if __name__ == "__main__":
    generate_board()
