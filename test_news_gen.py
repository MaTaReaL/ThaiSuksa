# Test news & activities generation
import json
import os
from kit import screen_bg_hint, C, USER, sb, hi, bar, nav, ic, img, btn, field, get_b64_uri, qr_svg

NEWS_ARTICLES = {
    "news_campus_1": {
        "id": "news_campus_1",
        "scope": "campus",
        "tag": "ทุนการศึกษา",
        "badge_color": "b-blue",
        "date": "14 ต.ค. 2569",
        "title": "ม.ศิลปากร เปิดรับสมัครทุนวิจัยและนวัตกรรมดิจิทัลสำหรับนักศึกษา ประจำปี 2569",
        "summary": "กองบริการการศึกษาจัดสรรทุนพัฒนานวัตกรรมอัจฉริยะ สูงสุดโครงการละ 50,000 บาท พร้อมสิทธิ์นำเสนอผลงานในงานประชุมวิชาการระดับชาติ",
        "photo": "campus_library.jpg",
        "author": "กองบริการการศึกษา สำนักงานอธิการบดี",
        "views": "2,840 ครั้ง",
        "read_time": "3 นาที",
        "paragraphs": [
            "มหาวิทยาลัยศิลปากร โดยกองบริการการศึกษาร่วมกับสำนักดิจิทัลเทคโนโลยี ประกาศเปิดรับข้อเสนอโครงการวิจัยและพัฒนานวัตกรรมดิจิทัลสำหรับนักศึกษาระดับปริญญาตรี ประจำปีการศึกษา 2569 เพื่อสนับสนุนการสร้างสรรค์ผลงานเทคโนโลยีที่ตอบโจทย์สังคม ชุมชน และสิ่งแวดล้อมอย่างยั่งยืน",
            "นักศึกษาที่ผ่านการคัดเลือกจะได้รับทุนสนับสนุนการพัฒนาต้นแบบ สูงสุดโครงการละ 50,000 บาท พร้อมพื้นที่ปฏิบัติการใน Co-working Space หอสมุดพระราชวังสนามจันทร์ และการให้คำปรึกษาจากผู้เชี่ยวชาญจากภาคอุตสาหกรรมเทคโนโลยี",
            "เปิดรับสมัครผ่านระบบไทยศึกษาตั้งแต่วันนี้ ถึง 30 พฤศจิกายน 2569 ประกาศผลรอบแรกวันที่ 15 ธันวาคม 2569",
        ],
        "attachments": [("ประกาศทุนวิจัยและนวัตกรรม_2569.pdf", "1.8 MB"), ("แบบฟอร์มข้อเสนอโครงการ.docx", "240 KB")]
    },
    "news_campus_2": {
        "id": "news_campus_2",
        "scope": "campus",
        "tag": "นิทรรศการศิลปะ",
        "badge_color": "b-green",
        "date": "12 ต.ค. 2569",
        "title": "นิทรรศการศิลปนิพนธ์สร้างสรรค์ 2569 ณ หอศิลปวัฒนธรรมเฉลิมพระเกียรติ 6 รอบฯ",
        "summary": "รวมผลงานออกแบบ สื่อการสอนดิจิทัล และศิลปะร่วมสมัยกว่า 200 ชิ้นงานจากนักศึกษาชั้นปีสุดท้าย ทุกวิทยาเขต",
        "photo": "campus_auditorium.jpg",
        "author": "สำนักส่งเสริมศิลปวัฒนธรรม ม.ศิลปากร",
        "views": "1,950 ครั้ง",
        "read_time": "2 นาที",
        "paragraphs": [
            "ขอเชิญคณาจารย์ นักศึกษา และประชาชนทั่วไป ร่วมชมนิทรรศการแสดงผลงานศิลปนิพนธ์ยอดเยี่ยม ประจำปีการศึกษา 2569 ภายใต้แนวคิด ศิลปะ นวัตกรรม และภูมิปัญญาสร้างสรรค์สู่อนาคต ณ ศูนย์ศิลปวัฒนธรรมเฉลิมพระเกียรติ 6 รอบพระชนมพรรษา มหาวิทยาลัยศิลปากร วิทยาเขตพระราชวังสนามจันทร์",
            "ภายในงานมีการจัดแสดงผลงานสื่อมัลติมีเดียเพื่อการศึกษา สื่อแอนิเมชัน ผลงานจิตรกรรม ประติมากรรม และการออกแบบผลิตภัณฑ์เพื่อชุมชน พร้อมเวทีเสวนาแลกเปลี่ยนมุมมองกับศิลปินและนักออกแบบแถวหน้าของเมืองไทย",
            "จัดแสดงระหว่างวันที่ 18 - 28 ตุลาคม 2569 เวลา 09:00 - 18:00 น. เข้าชมฟรีโดยไม่เสียค่าใช้จ่าย",
        ],
        "attachments": [("สูจิบัตรนิทรรศการศิลปนิพนธ์_2569.pdf", "4.2 MB")]
    },
    "news_campus_3": {
        "id": "news_campus_3",
        "scope": "campus",
        "tag": "กำหนดการสำคัญ",
        "badge_color": "b-amber",
        "date": "10 ต.ค. 2569",
        "title": "ประกาศปฏิทินการลงทะเบียนเรียน ภาคการศึกษาปลาย 2569 และการขอผ่อนผันค่าเทอม",
        "summary": "ตรวจสอบรายวิชาเปิดสอน แผนการลงทะเบียนล่วงหน้า และระบบอนุมัติคำร้องผ่อนผันค่าธรรมเนียมการศึกษาแบบออนไลน์",
        "photo": "building.jpg",
        "author": "งานทะเบียนและประมวลผลการศึกษา",
        "views": "5,320 ครั้ง",
        "read_time": "2 นาที",
        "paragraphs": [
            "กองบริการการศึกษา มหาวิทยาลัยศิลปากร แจ้งกำหนดการลงทะเบียนเรียนผ่านระบบออนไลน์สำหรับภาคการศึกษาปลาย ประจำปีการศึกษา 2569 โดยเริ่มเปิดให้ตรวจสอบรายวิชาเปิดสอนและตารางเรียนล่วงหน้าตั้งแต่วันที่ 20 ตุลาคม 2569",
            "สำหรับนักศึกษาที่มีความจำเป็นต้องขอผ่อนผันการชำระค่าธรรมเนียมการศึกษา สามารถยื่นคำร้องผ่านเมนู บริการคำร้องออนไลน์ ในแอปพลิเคชันไทยศึกษา ได้ทันทีโดยไม่ต้องเดินทางมายื่นเอกสารด้วยตนเอง",
        ],
        "attachments": [("ปฏิทินการศึกษา_ภาคปลาย_2569.pdf", "850 KB")]
    },
    "news_world_1": {
        "id": "news_world_1",
        "scope": "world",
        "tag": "เทคโนโลยีและ AI",
        "badge_color": "b-blue",
        "date": "14 ต.ค. 2569",
        "title": "AI ในการศึกษาระดับโลก: มหาวิทยาลัยชั้นนำปรับโฉมหลักสูตร มุ่งเน้นการคิดวิเคราะห์",
        "summary": "รายงานสากลชี้แนวโน้มสถาบันการศึกษาทั่วโลกเปลี่ยนจากการห้ามใช้ AI สู่การสอนประยุกต์ใช้เป็นเครื่องมือสร้างสรรค์และแก้ปัญหาจริง",
        "photo": "news_world_ai.jpg",
        "author": "ฝ่ายวิจัยเทคโนโลยีการศึกษาสากล",
        "views": "4,180 ครั้ง",
        "read_time": "4 นาที",
        "paragraphs": [
            "รายงานวิจัยล่าสุดจาก World Economic Forum และมหาวิทยาลัยชั้นนำระดับโลกเปิดเผยว่า วงการอุดมศึกษาทั่วโลกได้ก้าวผ่านยุคของการถกเถียงเรื่องการห้ามใช้ปัญญาประดิษฐ์ เข้าสู่ยุคของการบูรณาการ AI เข้ากับกระบวนการเรียนรู้และการวิจัยในทุกศาสตร์",
            "อาจารย์และนักศึกษาได้รับการส่งเสริมให้ใช้ AI ในฐานะคู่คิดวิเคราะห์ ช่วยระดมความคิด วิเคราะห์ชุดข้อมูลขนาดใหญ่ และจำลองสถานการณ์เสมือน โดยเกณฑ์การประเมินผลได้ปรับเปลี่ยนไปเน้นความลุ่มลึกของการคิดเชิงวิพากษ์ จริยธรรมการใช้ข้อมูล และการแก้ปัญหาในบริบทจริง",
            "สำหรับประเทศไทย สถาบันอุดมศึกษาหลายแห่งกำลังเร่งพัฒนาโครงสร้างพื้นฐานดิจิทัลและการรู้เท่าทันปัญญาประดิษฐ์ ให้นิสิตนักศึกษาทุกคนมีความพร้อมแข่งขันในเวทีสากล",
        ],
        "attachments": [("Global_EdTech_AI_Report_2026.pdf", "2.6 MB")]
    },
    "news_world_2": {
        "id": "news_world_2",
        "scope": "world",
        "tag": "ทุนเรียนต่อต่างประเทศ",
        "badge_color": "b-green",
        "date": "11 ต.ค. 2569",
        "title": "สหภาพยุโรปเปิดรับสมัครทุน Erasmus Mundus 2027 ทุนเต็มจำนวนเรียนต่อปริญญาโท",
        "summary": "เปิดโอกาสให้นักศึกษาไทยศึกษาต่อในมหาวิทยาลัยชั้นนำของยุโรปอย่างน้อย 2 ประเทศ ครอบคลุมค่าเล่าเรียนและค่าใช้จ่ายทั้งหมด",
        "photo": "news_world_erasmus.jpg",
        "author": "ฝ่ายความร่วมมือระหว่างประเทศ",
        "views": "3,620 ครั้ง",
        "read_time": "3 นาที",
        "paragraphs": [
            "คณะกรรมาธิการยุโรป ประกาศเปิดรับสมัครทุนการศึกษา Erasmus Mundus Joint Master Degrees สำหรับปีการศึกษา 2027 ซึ่งเป็นหนึ่งในทุนการศึกษาที่มีเกียรติและครอบคลุมค่าใช้จ่ายสมบูรณ์แบบที่สุดในโลก",
            "จุดเด่นของทุนนี้คือ ผู้รับทุนจะได้ศึกษาในสถาบันอุดมศึกษาชั้นนำอย่างน้อย 2 ประเทศในสหภาพยุโรป และได้รับปริญญาร่วม หรือปริญญาคู่ ทุนการศึกษาครอบคลุมค่าเล่าเรียน 100% ค่าตั๋วเครื่องบินไปกลับ ค่าประกันสุขภาพ และค่าครองชีพรายเดือนตลอดหลักสูตร 2 ปี",
            "นักศึกษาชั้นปีที่ 3 และปีที่ 4 ที่สนใจสามารถเริ่มเตรียมเอกสารผลการเรียน ผลทดสอบภาษาอังกฤษ และหนังสือแสดงเจตจำนง เพื่อยื่นสมัครได้ตั้งแต่เดือนพฤศจิกายนนี้",
        ],
        "attachments": [("Erasmus_Mundus_Guide_2027.pdf", "3.1 MB")]
    },
    "news_world_3": {
        "id": "news_world_3",
        "scope": "world",
        "tag": "ตลาดแรงงานโลก",
        "badge_color": "b-amber",
        "date": "08 ต.ค. 2569",
        "title": "10 ทักษะเกิดใหม่ที่ตลาดงานสากลต้องการสูงสุดในยุคเศรษฐกิจสีเขียวและดิจิทัล",
        "summary": "สรุปข้อมูลวิเคราะห์อาชีพแห่งอนาคต ชี้สายงานวิศวกรรมข้อมูล นวัตกรรมเพื่อความยั่งยืน และการออกแบบประสบการณ์ผู้ใช้มีอัตราเติบโตก้าวกระโดด",
        "photo": "study_room.jpg",
        "author": "ศูนย์พัฒนาศักยภาพอาชีพสู่สากล",
        "views": "6,490 ครั้ง",
        "read_time": "3 นาที",
        "paragraphs": [
            "ผลการสำรวจตลาดแรงงานระดับสากล Future of Jobs เผยข้อมูลความต้องการขององค์กรชั้นนำทั่วโลก พบว่ากลุ่มทักษะที่มีความต้องการสูงที่สุด ไม่ได้จำกัดอยู่เพียงแค่การเขียนโปรแกรม แต่เน้นการเชื่อมโยงเทคโนโลยีเข้ากับการแก้ปัญหาความยั่งยืน",
            "อาชีพที่มีอัตราเติบโตเร็วที่สุด 3 อันดับแรก ได้แก่ ผู้เชี่ยวชาญด้านปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง, ผู้เชี่ยวชาญด้านความยั่งยืนและสิ่งแวดล้อม, และนักออกแบบประสบการณ์ผู้ใช้ขั้นสูง",
            "นักศึกษาสามารถเริ่มสะสมทักษะเหล่านี้ผ่านการเรียนรู้เสริมและโครงงานนอกห้องเรียน เพื่อสร้างประวัติและผลงานที่โดดเด่นก่อนก้าวสู่โลกการทำงาน",
        ],
        "attachments": [("Global_Skills_Outlook_2026.pdf", "1.9 MB")]
    }
}

CAMPUS_ACTIVITIES = {
    "act_1": {
        "id": "act_1",
        "title": "ไทยศึกษา Smart Campus Hackathon 2026",
        "cat": "การแข่งขันและนวัตกรรม",
        "hours_gain": "สะสม 6 ชั่วโมงกิจกรรมวิชาการ",
        "photo": "event_hackathon.jpg",
        "date_display": "เสาร์ที่ 25 ต.ค. 2569 • 09:00 - 18:00 น.",
        "location": "Co-working Space ชั้น 2 หอสมุดพระราชวังสนามจันทร์",
        "remaining_seats": "เหลือ 15 ที่นั่ง (จาก 50 ที่นั่ง)",
        "organizer": "สภานิสิตนักศึกษา ร่วมกับ สำนักดิจิทัลเทคโนโลยี",
        "awards": "เงินรางวัลรวม 120,000 บาท พร้อมโล่รางวัลและใบประกาศนียบัตรดิจิทัล",
        "desc": "การประลองไอเดียสร้างสรรค์พัฒนานวัตกรรมสมาร์ทแคมปัสเพื่อยกระดับชีวิตนักศึกษาในรั้วมหาวิทยาลัย เปิดรับสมัครทีมละ 3-5 คน พร้อมเมนเทอร์ผู้เชี่ยวชาญคอยดูแลตลอดการแข่งขัน",
        "ticket_code": "TS-HACK-8812"
    },
    "act_2": {
        "id": "act_2",
        "title": "เทศกาลดนตรีในสวนและตลาดนัดศิลปะ พระราชวังสนามจันทร์",
        "cat": "ดนตรีและศิลปวัฒนธรรม",
        "hours_gain": "สะสม 3 ชั่วโมงกิจกรรมสุนทรียศาสตร์",
        "photo": "campus_ganesha.jpg",
        "date_display": "ศุกร์ที่ 18 ต.ค. 2569 • 16:30 - 21:00 น.",
        "location": "ลานพระพิฆเนศและริมสระแก้ว ม.ศิลปากร",
        "remaining_seats": "เปิดกว้างสำหรับทุกคน ไม่จำกัดที่นั่ง",
        "organizer": "ชมรมดนตรีสากลและสโมสรนักศึกษา ม.ศิลปากร",
        "awards": "รับเกียรติบัตรการเข้าร่วมกิจกรรมสุนทรียภาพทางศิลปะ",
        "desc": "เพลิดเพลินกับการแสดงดนตรีสดอะคูสติกริมสระแก้ว ชมนิทรรศการงานศิลปะทำมือ และเลือกซื้อสินค้าไอเดียสร้างสรรค์จากนักศึกษาท่ามกลางบรรยากาศร่มรื่นยามเย็น",
        "ticket_code": "TS-MUSIC-4091"
    },
    "act_3": {
        "id": "act_3",
        "title": "เวิร์กช็อป Generative AI for Educational Innovation",
        "cat": "สัมมนาและเวิร์กช็อป",
        "hours_gain": "สะสม 4 ชั่วโมงกิจกรรมวิชาการ",
        "photo": "news_world_ai.jpg",
        "date_display": "พุธที่ 22 ต.ค. 2569 • 13:00 - 17:00 น.",
        "location": "ห้องปฏิบัติการคอมพิวเตอร์ ED-204 คณะศึกษาศาสตร์",
        "remaining_seats": "เหลือ 8 ที่นั่ง (จาก 40 ที่นั่ง)",
        "organizer": "สาขาวิชาเทคโนโลยีการศึกษา คณะศึกษาศาสตร์",
        "awards": "ใบรับรองทักษะวิชาชีพดิจิทัล Google Cloud & Thai Suksa",
        "desc": "ฝึกปฏิบัติจริงการใช้ Generative AI ในการออกแบบสื่อการเรียนการสอน การสังเคราะห์แบบทดสอบอัตโนมัติ และการสร้างโมเดลสอนเสริมสำหรับผู้เรียนรายบุคคล",
        "ticket_code": "TS-EDTECH-3310"
    },
    "act_4": {
        "id": "act_4",
        "title": "จิตอาสาพัฒนาภูมิทัศน์และอนุรักษ์สระแก้ว พระราชวังสนามจันทร์",
        "cat": "จิตอาสา กยศ.",
        "hours_gain": "สะสม 8 ชั่วโมงจิตอาสา กยศ.",
        "photo": "building.jpg",
        "date_display": "อาทิตย์ที่ 26 ต.ค. 2569 • 08:30 - 16:30 น.",
        "location": "ศาลาริมสระแก้วและพื้นที่สวนรอบวิทยาเขต",
        "remaining_seats": "เหลือ 22 ที่นั่ง (จาก 80 ที่นั่ง)",
        "organizer": "กองกิจการนักศึกษาและชมรมอนุรักษ์ธรรมชาติ",
        "awards": "บันทึกชั่วโมงจิตอาสาลงระบบ กยศ. อัตโนมัติทันทีหลังจบกิจกรรม",
        "desc": "ร่วมแรงร่วมใจทำความสะอาดฟื้นฟูระบบนิเวศริมสระแก้ว ปลูกต้นไม้เพิ่มพื้นที่สีเขียวในมหาวิทยาลัย และบำรุงรักษาภูมิทัศน์ประวัติศาสตร์พระราชวังสนามจันทร์",
        "ticket_code": "TS-VOLUN-5519"
    }
}

print(f"Loaded {len(NEWS_ARTICLES)} news articles and {len(CAMPUS_ACTIVITIES)} activities.")


def s16_news_feed():
    """16. News Feed"""
    top_story = NEWS_ARTICLES["news_campus_1"]
    
    campus_cards_html = ""
    for nid, art in NEWS_ARTICLES.items():
        is_campus = (art["scope"] == "campus")
        scope_pill = f'<span class="badge b-blue" style="font-size:10.5px;padding:2px 8px;">ม.ศิลปากร</span>' if is_campus else f'<span class="badge b-navy" style="font-size:10.5px;padding:2px 8px;">ข่าวสารโลก</span>'
        
        campus_cards_html += f'''
        <div class="card news-card-item" data-nid="{nid}" data-scope="{art['scope']}" data-tag="{art['tag']}" onclick="openNewsArticle('{nid}')" data-go="S17" style="padding:12px;border-radius:18px;display:flex;gap:12px;cursor:pointer;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 2px 8px rgba(16,28,54,0.04);">
          <div style="width:88px;height:88px;border-radius:14px;overflow:hidden;flex:none;background:#F1F5F9;">
            {img(art['photo'], "width:88px;height:88px;object-fit:cover;")}
          </div>
          <div style="flex:1;min-width:0;display:flex;flex-direction:column;justify-content:space-between;">
            <div>
              <div style="display:flex;align-items:center;gap:6px;margin-bottom:4px;">
                {scope_pill}
                <span class="badge {art['badge_color']}" style="font-size:10.5px;padding:2px 8px;">{art['tag']}</span>
              </div>
              <div style="font-weight:700;font-size:13.5px;color:{C['navy']};line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">
                {art['title']}
              </div>
            </div>
            <div style="display:flex;align-items:center;gap:6px;font-size:11px;color:#94A3B8;margin-top:4px;">
              <span>{art['date']}</span>
              <span>•</span>
              <span>อ่าน {art['read_time']}</span>
            </div>
          </div>
        </div>
        '''

    return f'''
    <div class="scr">
      {sb()}
      {bar("ข่าวสารและประกาศ", right='<div class="ib" title="บันทึกที่อ่านแล้ว">' + ic("bookmark") + '</div>')}
      <div class="body" style="padding:0 20px 20px;gap:12px;overflow-y:auto;">
        
        <!-- Live Search Field -->
        <div style="position:relative;width:100%;flex:none;">
          <input type="text" id="news_search_input" placeholder="ค้นหาข่าวสาร ทุนการศึกษา นวัตกรรม..." style="width:100%;height:44px;border-radius:14px;background:#FFFFFF;border:1px solid #E2E8F0;padding:0 36px 0 42px;font-size:13px;font-family:'IBM Plex Sans Thai',sans-serif;outline:none;color:{C['navy']};box-shadow:0 2px 6px rgba(0,0,0,0.03);">
          <div style="position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#94A3B8;pointer-events:none;">{ic("search", 18)}</div>
          <div id="news_search_clear" onclick="clearNewsSearch()" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);color:#94A3B8;cursor:pointer;display:none;width:20px;height:20px;border-radius:50%;background:#F1F5F9;align-items:center;justify-content:center;">{ic("x", 12)}</div>
        </div>

        <!-- Scope Segment Switcher: Campus vs World -->
        <div class="seg" style="flex:none;">
          <div class="on news-scope-btn" data-scope="campus" onclick="switchNewsScope('campus')" style="cursor:pointer;">
            ข่าวภายในมหาวิทยาลัย
          </div>
          <div class="news-scope-btn" data-scope="world" onclick="switchNewsScope('world')" style="cursor:pointer;">
            ข่าวสารโลก
          </div>
        </div>

        <!-- Category Filter Chips -->
        <div class="chips" style="gap:6px;overflow-x:auto;padding-bottom:2px;flex:none;">
          <div class="chip on news-filter-chip" data-tag="all" onclick="filterNewsTag('all')">ทั้งหมด 6</div>
          <div class="chip news-filter-chip" data-tag="ทุนการศึกษา" onclick="filterNewsTag('ทุนการศึกษา')">ทุนการศึกษา</div>
          <div class="chip news-filter-chip" data-tag="เทคโนโลยีและ AI" onclick="filterNewsTag('เทคโนโลยีและ AI')">เทคโนโลยีและ AI</div>
          <div class="chip news-filter-chip" data-tag="นิทรรศการศิลปะ" onclick="filterNewsTag('นิทรรศการศิลปะ')">นิทรรศการ</div>
          <div class="chip news-filter-chip" data-tag="กำหนดการสำคัญ" onclick="filterNewsTag('กำหนดการสำคัญ')">กำหนดการ</div>
          <div class="chip news-filter-chip" data-tag="ตลาดแรงงานโลก" onclick="filterNewsTag('ตลาดแรงงานโลก')">ตลาดแรงงาน</div>
        </div>

        <!-- Featured Top Story Hero Card -->
        <div class="card shadow" onclick="openNewsArticle('{top_story['id']}')" data-go="S17" style="padding:0;overflow:hidden;cursor:pointer;border-radius:20px;border:1.5px solid #E2E8F0;flex:none;">
          <div style="width:100%;height:170px;position:relative;background:#E2E8F0;">
            {img(top_story['photo'], "width:100%;height:170px;object-fit:cover;")}
            <div style="position:absolute;top:12px;left:12px;background:rgba(16,28,54,0.85);backdrop-filter:blur(8px);color:#FFFFFF;font-size:11px;font-weight:600;padding:4px 10px;border-radius:12px;display:flex;align-items:center;gap:6px;">
              <span style="color:#F59E0B;">★</span>
              <span>ข่าวยอดนิยม • อ่าน {top_story['read_time']}</span>
            </div>
            <div style="position:absolute;bottom:10px;left:12px;background:#246BFD;color:#FFFFFF;font-size:11px;font-weight:700;padding:3px 10px;border-radius:10px;">
              {top_story['tag']}
            </div>
          </div>
          <div style="padding:14px;">
            <div style="font-weight:700;font-size:16px;color:{C['navy']};line-height:1.35;">
              {top_story['title']}
            </div>
            <div style="font-size:12.5px;color:#64748B;margin-top:6px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">
              {top_story['summary']}
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-top:10px;padding-top:8px;border-top:1px solid #F1F5F9;font-size:11.5px;color:#94A3B8;">
              <span>{top_story['author']}</span>
              <span>{top_story['date']}</span>
            </div>
          </div>
        </div>

        <!-- Section Title: News Stream -->
        <div class="sec" style="margin-top:4px;">
          <span style="font-size:14px;font-weight:700;color:{C['navy']};">ข่าวสารและประกาศล่าสุด</span>
          <span id="news_count_badge" style="font-size:11px;color:{C['blue']};font-weight:600;">ทั้งหมด 6 ข่าว</span>
        </div>

        <!-- News Cards List -->
        <div id="news_list_container" style="display:flex;flex-direction:column;gap:10px;">
          {campus_cards_html}
        </div>

      </div>
      {nav(0, link=True)}
    </div>
    '''

def s17_news_details():
    """17. News Details (Full Reader & Audio Assistant)"""
    art = NEWS_ARTICLES["news_campus_1"]
    
    paragraphs_html = ""
    for p_text in art["paragraphs"]:
        paragraphs_html += f'<p class="news-body-paragraph" style="font-size:14px;color:#334155;line-height:1.75;margin-bottom:12px;">{p_text}</p>'

    attachments_html = ""
    for fname, fsize in art["attachments"]:
        attachments_html += f'''
        <div style="display:flex;align-items:center;justify-content:space-between;background:#FFFFFF;border:1px solid #E2E8F0;padding:10px 12px;border-radius:12px;margin-top:6px;">
          <div style="display:flex;align-items:center;gap:8px;color:{C['navy']};font-size:12.5px;font-weight:600;">
            <div style="color:{C['blue']};">{ic("file", 18)}</div>
            <span>{fname}</span>
          </div>
          <span style="font-size:11px;color:#64748B;">{fsize}</span>
        </div>
        '''

    return f'''
    <div class="scr" style="position:relative;">
      <!-- Reading Progress Line -->
      <div id="news_read_progress" style="position:absolute;top:0;left:0;height:4px;width:65%;background:{C['blue']};z-index:100;border-radius:0 2px 2px 0;"></div>
      
      {sb()}
      {bar("อ่านข่าวสาร", back=True, right='<div class="row" style="gap:8px;"><div class="ib" id="btn_toggle_tts" onclick="toggleNewsTTS()" title="ฟังข่าวด้วยเสียง AI">' + ic("spark", 18, C['blue']) + '</div><div class="ib" title="แชร์">' + ic("share") + '</div></div>')}
      
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        
        <!-- Hero Article Image Banner -->
        <div id="news_detail_img_box" style="width:100%;height:200px;border-radius:20px;overflow:hidden;position:relative;background:#E2E8F0;box-shadow:0 8px 24px rgba(16,28,54,0.12);flex:none;">
          {img(art['photo'], "width:100%;height:200px;object-fit:cover;")}
          <div style="position:absolute;top:12px;left:12px;background:rgba(16,28,54,0.85);backdrop-filter:blur(8px);color:#FFFFFF;font-size:11px;font-weight:600;padding:4px 10px;border-radius:12px;">
            📸 ภาพประกอบข่าวจริง
          </div>
        </div>

        <!-- Category & Scope Tag Row -->
        <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;flex:none;">
          <div style="display:flex;align-items:center;gap:6px;">
            <span id="news_detail_scope" class="badge b-blue" style="font-size:11px;padding:2px 8px;">ม.ศิลปากร</span>
            <span id="news_detail_tag" class="badge {art['badge_color']}" style="font-size:11px;padding:2px 8px;">{art['tag']}</span>
          </div>
          <span style="font-size:11px;color:#94A3B8;">อ่าน {art['read_time']}</span>
        </div>

        <!-- Headline & Metadata -->
        <div style="flex:none;">
          <div id="news_detail_title" style="font-size:22px;font-weight:700;color:{C['navy']};line-height:1.35;">
            {art['title']}
          </div>
          <div style="display:flex;align-items:center;gap:8px;margin-top:8px;font-size:12px;color:#64748B;">
            <span id="news_detail_author" style="font-weight:600;color:{C['navy']};">{art['author']}</span>
            <span>•</span>
            <span id="news_detail_date">{art['date']}</span>
            <span>•</span>
            <span id="news_detail_views">{art['views']}</span>
          </div>
        </div>

        <!-- Interactive Article Toolbar: TTS Reader & Font Scaler -->
        <div class="card" style="padding:10px 14px;border-radius:14px;background:#F8FAFC;border:1px solid #EDF2F7;display:flex;align-items:center;justify-content:space-between;flex:none;">
          <!-- AI Voice Reader Button -->
          <div id="news_tts_bar" onclick="toggleNewsTTS()" style="display:flex;align-items:center;gap:8px;color:{C['blue']};font-size:12.5px;font-weight:600;cursor:pointer;">
            <span style="width:26px;height:26px;border-radius:50%;background:#EFF6FF;display:flex;align-items:center;justify-content:center;">{ic("spark", 15, C['blue'])}</span>
            <span id="news_tts_label">ฟังข่าวด้วยเสียง AI</span>
          </div>

          <!-- Font Size Adjustment Buttons -->
          <div style="display:flex;align-items:center;gap:6px;">
            <span style="font-size:11px;color:#94A3B8;margin-right:2px;">ขนาดตัวอักษร:</span>
            <div onclick="adjustNewsFontSize(-1)" style="width:28px;height:28px;border-radius:8px;background:#FFFFFF;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#64748B;cursor:pointer;">ก</div>
            <div onclick="adjustNewsFontSize(1)" style="width:28px;height:28px;border-radius:8px;background:#FFFFFF;border:1px solid #E2E8F0;display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:700;color:{C['blue']};cursor:pointer;">ก+</div>
          </div>
        </div>

        <!-- Key Takeaways Highlight Box -->
        <div class="card" style="padding:12px 14px;border-radius:14px;background:#EFF6FF;border-left:4px solid {C['blue']};flex:none;">
          <div style="font-weight:700;font-size:12.5px;color:{C['blue']};">สาระสำคัญโดยสรุป</div>
          <div id="news_detail_summary" style="font-size:13px;color:#1E3A8A;margin-top:4px;line-height:1.5;">
            {art['summary']}
          </div>
        </div>

        <!-- Article Body Paragraphs -->
        <div id="news_detail_paragraphs" style="flex:none;">
          {paragraphs_html}
        </div>

        <!-- Document Attachments Download Card -->
        <div class="card" style="padding:14px;background:#F8FAFC;border-radius:16px;flex:none;">
          <div style="font-weight:700;font-size:13px;color:{C['navy']};display:flex;align-items:center;justify-content:space-between;">
            <span>เอกสารแนบและแบบฟอร์ม</span>
            <span style="font-size:11px;color:{C['blue']};font-weight:600;">ดาวน์โหลดฟรี</span>
          </div>
          <div id="news_detail_attachments">
            {attachments_html}
          </div>
        </div>

        <!-- Bottom Action CTA -->
        <div style="display:flex;gap:8px;flex:none;margin-top:4px;">
          <div class="btn bp" data-go="S16" style="flex:1;height:46px;border-radius:14px;cursor:pointer;">
            {ic("left", 18, "#FFFFFF")}
            <span>กลับสู่หน้ารวมข่าวสาร</span>
          </div>
          <div class="btn bs" onclick="alert('คัดลอกลิงก์ข่าวสารเรียบร้อยแล้ว')" style="width:52px;height:46px;border-radius:14px;cursor:pointer;padding:0;">
            {ic("share", 18, C['navy'])}
          </div>
        </div>

      </div>
      {hi()}
    </div>
    '''

def s18_activities():
    """18. Activities & Clubs Directory"""
    featured = CAMPUS_ACTIVITIES["act_1"]

    act_cards_html = ""
    for aid, act in CAMPUS_ACTIVITIES.items():
        act_cards_html += f'''
        <div class="card activity-card-item" data-aid="{aid}" data-cat="{act['cat']}" onclick="openActivityDetails('{aid}')" data-go="S19" style="padding:14px;border-radius:18px;display:flex;flex-direction:column;gap:10px;cursor:pointer;background:#FFFFFF;border:1px solid #E2E8F0;box-shadow:0 2px 8px rgba(16,28,54,0.04);">
          <div style="width:100%;height:130px;border-radius:14px;overflow:hidden;position:relative;background:#F1F5F9;">
            {img(act['photo'], "width:100%;height:130px;object-fit:cover;")}
            <div style="position:absolute;top:10px;left:10px;background:#10B981;color:#FFFFFF;font-size:11px;font-weight:700;padding:3px 10px;border-radius:10px;">
              {act['hours_gain']}
            </div>
            <div style="position:absolute;bottom:8px;right:10px;background:rgba(16,28,54,0.85);backdrop-filter:blur(6px);color:#FFFFFF;font-size:11px;font-weight:600;padding:3px 8px;border-radius:8px;">
              {act['remaining_seats']}
            </div>
          </div>
          <div>
            <div style="font-weight:700;font-size:15px;color:{C['navy']};line-height:1.35;">
              {act['title']}
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:4px;display:flex;align-items:center;gap:6px;">
              <span>📅 {act['date_display']}</span>
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:2px;display:flex;align-items:center;gap:6px;">
              <span>📍 {act['location']}</span>
            </div>
          </div>
          <div style="display:flex;align-items:center;justify-content:space-between;padding-top:8px;border-top:1px solid #F1F5F9;">
            <span class="badge b-blue" style="font-size:11px;">{act['cat']}</span>
            <span style="font-size:12px;font-weight:700;color:{C['blue']};">ดูรายละเอียด & สมัคร →</span>
          </div>
        </div>
        '''

    return f'''
    <div class="scr">
      {sb()}
      {bar("กิจกรรมและชมรม", right='<div class="ib" title="ตั๋วการลงทะเบียนของฉัน" data-go="S20">' + ic("qr") + '</div>')}
      <div class="body" style="padding:0 20px 20px;gap:12px;overflow-y:auto;">
        
        <!-- Search Field -->
        <div style="position:relative;width:100%;flex:none;">
          <input type="text" id="act_search_input" placeholder="ค้นหากิจกรรม เวิร์กช็อป ชั่วโมงจิตอาสา..." style="width:100%;height:44px;border-radius:14px;background:#FFFFFF;border:1px solid #E2E8F0;padding:0 36px 0 42px;font-size:13px;font-family:'IBM Plex Sans Thai',sans-serif;outline:none;color:{C['navy']};box-shadow:0 2px 6px rgba(0,0,0,0.03);">
          <div style="position:absolute;left:14px;top:50%;transform:translateY(-50%);color:#94A3B8;pointer-events:none;">{ic("search", 18)}</div>
        </div>

        <!-- Filter Chips -->
        <div class="chips" style="gap:6px;overflow-x:auto;padding-bottom:2px;flex:none;">
          <div class="chip on act-filter-chip" data-cat="all" onclick="filterActCategory('all')">ทั้งหมด 4</div>
          <div class="chip act-filter-chip" data-cat="การแข่งขันและนวัตกรรม" onclick="filterActCategory('การแข่งขันและนวัตกรรม')">การแข่งขัน</div>
          <div class="chip act-filter-chip" data-cat="จิตอาสา กยศ." onclick="filterActCategory('จิตอาสา กยศ.')">จิตอาสา กยศ.</div>
          <div class="chip act-filter-chip" data-cat="ดนตรีและศิลปวัฒนธรรม" onclick="filterActCategory('ดนตรีและศิลปวัฒนธรรม')">ศิลปวัฒนธรรม</div>
          <div class="chip act-filter-chip" data-cat="สัมมนาและเวิร์กช็อป" onclick="filterActCategory('สัมมนาและเวิร์กช็อป')">เวิร์กช็อป</div>
        </div>

        <!-- Featured Activity Hero Card -->
        <div class="card shadow" onclick="openActivityDetails('{featured['id']}')" data-go="S19" style="padding:0;overflow:hidden;cursor:pointer;border-radius:20px;border:1.5px solid #E2E8F0;flex:none;">
          <div style="width:100%;height:160px;position:relative;background:#E2E8F0;">
            {img(featured['photo'], "width:100%;height:160px;object-fit:cover;")}
            <div style="position:absolute;top:12px;left:12px;background:#10B981;color:#FFFFFF;font-size:11px;font-weight:700;padding:4px 10px;border-radius:12px;">
              {featured['hours_gain']}
            </div>
            <div style="position:absolute;bottom:10px;right:12px;background:rgba(220,69,69,0.9);color:#FFFFFF;font-size:11px;font-weight:700;padding:3px 10px;border-radius:10px;">
              {featured['remaining_seats']}
            </div>
          </div>
          <div style="padding:14px;">
            <div style="font-weight:700;font-size:16px;color:{C['navy']};line-height:1.35;">
              {featured['title']}
            </div>
            <div style="font-size:12.5px;color:#64748B;margin-top:4px;">
              📅 {featured['date_display']}
            </div>
            <div style="font-size:12px;color:#64748B;margin-top:2px;">
              📍 {featured['location']}
            </div>
            <div style="margin-top:10px;display:flex;align-items:center;justify-content:space-between;border-top:1px solid #F1F5F9;padding-top:8px;">
              <span class="badge b-blue" style="font-size:11px;">{featured['organizer']}</span>
              <span style="font-size:12px;font-weight:700;color:{C['blue']};">แตะเพื่อดูรายละเอียด →</span>
            </div>
          </div>
        </div>

        <!-- Section Title -->
        <div class="sec" style="margin-top:4px;">
          <span style="font-size:14px;font-weight:700;color:{C['navy']};">กิจกรรมเปิดรับสมัครทั้งหมด</span>
          <span style="font-size:11px;color:{C['blue']};font-weight:600;">อัปเดตสัปดาห์นี้</span>
        </div>

        <!-- Activity Stream List -->
        <div id="act_list_container" style="display:flex;flex-direction:column;gap:10px;">
          {act_cards_html}
        </div>

      </div>
      {nav(3, link=True)}
    </div>
    '''

def s19_activity_details():
    """19. Activity Details & Registration"""
    act = CAMPUS_ACTIVITIES["act_1"]

    return f'''
    <div class="scr">
      {sb()}
      {bar("รายละเอียดกิจกรรม", back=True, right='<div class="ib" title="แชร์">' + ic("share") + '</div>')}
      <div class="body" style="padding:0 20px 24px;gap:14px;overflow-y:auto;">
        
        <!-- Hero Activity Image -->
        <div id="act_detail_img_box" style="width:100%;height:200px;border-radius:20px;overflow:hidden;position:relative;background:#E2E8F0;box-shadow:0 8px 24px rgba(16,28,54,0.12);flex:none;">
          {img(act['photo'], "width:100%;height:200px;object-fit:cover;")}
          <div id="act_detail_hours_badge" style="position:absolute;top:12px;left:12px;background:#10B981;color:#FFFFFF;font-size:11px;font-weight:700;padding:4px 10px;border-radius:12px;">
            {act['hours_gain']}
          </div>
        </div>

        <!-- Urgency Remaining Seats Bar -->
        <div class="card" style="padding:10px 14px;background:#FEF2F2;border:1px solid #FEE2E2;border-radius:14px;display:flex;flex-direction:column;gap:6px;flex:none;">
          <div style="display:flex;align-items:center;justify-content:space-between;font-size:12px;">
            <span style="font-weight:700;color:#DC4545;">สถานะที่นั่ง: เปิดรับ 50 ที่นั่ง</span>
            <span id="act_detail_seats_text" style="font-weight:700;color:#DC4545;">เหลือ 15 ที่นั่งสุดท้าย</span>
          </div>
          <!-- Progress Bar -->
          <div style="width:100%;height:6px;border-radius:3px;background:#FCA5A5;overflow:hidden;">
            <div id="act_detail_seat_progress" style="width:70%;height:100%;background:#DC4545;"></div>
          </div>
        </div>

        <!-- Title & Category -->
        <div style="flex:none;">
          <span id="act_detail_cat_badge" class="badge b-blue" style="font-size:11.5px;padding:3px 10px;">{act['cat']}</span>
          <div id="act_detail_title" style="font-size:22px;font-weight:700;color:{C['navy']};margin-top:6px;line-height:1.35;">
            {act['title']}
          </div>
          <div id="act_detail_organizer" style="font-size:13px;color:#64748B;margin-top:4px;">
            {act['organizer']}
          </div>
        </div>

        <!-- Key Information Grid -->
        <div class="card" style="background:#F8FAFC;padding:14px;border-radius:18px;display:flex;flex-direction:column;gap:10px;font-size:13px;flex:none;">
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:{C['blue']};font-size:16px;">📅</span>
            <div>
              <div style="font-weight:700;color:{C['navy']};">วันและเวลาจัดกิจกรรม</div>
              <div id="act_detail_date" style="color:#475569;margin-top:2px;">{act['date_display']}</div>
            </div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:{C['blue']};font-size:16px;">📍</span>
            <div>
              <div style="font-weight:700;color:{C['navy']};">สถานที่จัดกิจกรรม</div>
              <div id="act_detail_location" style="color:#475569;margin-top:2px;">{act['location']}</div>
            </div>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#F59E0B;font-size:16px;">🏆</span>
            <div>
              <div style="font-weight:700;color:{C['navy']};">รางวัลและสิทธิประโยชน์</div>
              <div id="act_detail_awards" style="color:#475569;margin-top:2px;">{act['awards']}</div>
            </div>
          </div>
        </div>

        <!-- Detailed Description -->
        <div class="card" style="padding:14px;border-radius:18px;flex:none;">
          <div style="font-weight:700;font-size:14px;color:{C['navy']};margin-bottom:6px;">เกี่ยวกับกิจกรรมนี้</div>
          <div id="act_detail_desc" style="font-size:13px;color:#334155;line-height:1.65;">
            {act['desc']}
          </div>
        </div>

        <!-- Action Registration Buttons -->
        <div style="display:flex;flex-direction:column;gap:8px;flex:none;margin-top:auto;">
          {btn("ลงทะเบียนเข้าร่วมกิจกรรม", "bp", go="S20", icon="check", style="height:50px;border-radius:16px;font-size:15px;")}
          {btn("สอบถามผู้จัดกิจกรรม", "bs", style="height:44px;border-radius:14px;font-size:13px;")}
        </div>

      </div>
      {hi()}
    </div>
    '''

def s20_registration_confirm():
    """20. Registration Confirmation Modal & Digital Event Ticket Pass"""
    act = CAMPUS_ACTIVITIES["act_1"]

    return f'''
    <div class="scr" style="background:rgba(10,17,40,0.65);backdrop-filter:blur(6px);">
      {screen_bg_hint()}
      <div class="modal" style="top:90px;width:396px;padding:24px 20px 20px;border-radius:26px;box-shadow:0 24px 60px rgba(0,0,0,0.35);">
        
        <!-- Success Icon -->
        <div style="width:64px;height:64px;border-radius:50%;background:#ECFDF5;color:#10B981;display:flex;align-items:center;justify-content:center;margin:0 auto 10px;box-shadow:0 6px 18px rgba(16,185,129,0.25);">
          {ic("check", 34, "#10B981")}
        </div>

        <div style="font-size:22px;font-weight:800;color:{C['navy']};letter-spacing:-0.2px;">
          ลงทะเบียนสำเร็จ!
        </div>
        <div style="font-size:12.5px;color:#64748B;margin-top:2px;">
          ระบบได้บันทึกรายชื่อและออกบัตรดิจิทัลเรียบร้อยแล้ว
        </div>

        <!-- Digital Perforated Ticket Pass -->
        <div style="width:100%;background:#F8FAFC;border:1.5px solid #E2E8F0;border-radius:20px;padding:16px;margin:14px 0 10px;position:relative;text-align:left;box-shadow:0 4px 14px rgba(0,0,0,0.03);">
          
          <!-- Event Header -->
          <div style="display:flex;align-items:flex-start;justify-content:space-between;gap:8px;">
            <div>
              <span class="badge b-green" style="font-size:10px;padding:2px 8px;margin-bottom:4px;">บัตรเข้าร่วมกิจกรรมดิจิทัล</span>
              <div id="ticket_act_title" style="font-size:14.5px;font-weight:700;color:{C['navy']};line-height:1.3;">
                {act['title']}
              </div>
            </div>
            <div style="text-align:right;flex:none;">
              <span style="font-size:10px;color:#94A3B8;">รหัสบัตร</span>
              <div id="ticket_code" style="font-family:monospace;font-weight:700;font-size:12px;color:{C['blue']};">
                {act['ticket_code']}
              </div>
            </div>
          </div>

          <!-- Perforated Divider Line with Cutout Notches -->
          <div style="position:relative;margin:12px -16px;border-top:2px dashed #CBD5E1;">
            <div style="position:absolute;left:-8px;top:-8px;width:16px;height:16px;border-radius:50%;background:#FFFFFF;border:1.5px solid #E2E8F0;"></div>
            <div style="position:absolute;right:-8px;top:-8px;width:16px;height:16px;border-radius:50%;background:#FFFFFF;border:1.5px solid #E2E8F0;"></div>
          </div>

          <!-- Attendee Profile & Date -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:11.5px;">
            <div>
              <span style="color:#94A3B8;">ชื่อผู้เข้าร่วม</span>
              <div style="font-weight:700;color:{C['navy']};">{USER['th_full']}</div>
            </div>
            <div>
              <span style="color:#94A3B8;">รหัสนักศึกษา</span>
              <div style="font-weight:700;color:{C['navy']};">{USER['sid']}</div>
            </div>
            <div>
              <span style="color:#94A3B8;">สังกัดคณะ</span>
              <div style="font-weight:600;color:#475569;">{USER['fac']}</div>
            </div>
            <div>
              <span style="color:#94A3B8;">ชั่วโมงกิจกรรม</span>
              <div style="font-weight:700;color:#0F7F59;">+6 ชั่วโมงวิชาการ</div>
            </div>
          </div>

          <!-- QR Code for Check-in -->
          <div style="margin-top:12px;padding-top:10px;border-top:1px solid #EDF2F7;display:flex;align-items:center;justify-content:space-between;">
            <div>
              <div style="font-size:11px;font-weight:700;color:{C['navy']};">สแกนเช็คอินหน้างาน</div>
              <div style="font-size:10px;color:#94A3B8;">ยื่น QR นี้แก่เจ้าหน้าที่หน้างาน</div>
            </div>
            <div style="width:54px;height:54px;background:#FFFFFF;border:1px solid #E2E8F0;border-radius:8px;display:flex;align-items:center;justify-content:center;padding:4px;">
              {qr_svg(46, "TS-HACK-8812-THANAPOL")}
            </div>
          </div>

        </div>

        <!-- 2 Action Buttons -->
        <div style="display:flex;flex-direction:column;gap:8px;width:100%;margin-top:4px;">
          {btn("บันทึกลงปฏิทินส่วนตัว", "bp", go="S15", icon="calendar", style="height:48px;border-radius:14px;font-size:14px;")}
          {btn("กลับสู่หน้ารวมกิจกรรม", "bs", go="S18", style="height:44px;border-radius:14px;font-size:13px;")}
        </div>

      </div>
      {hi()}
    </div>
    '''

print("s16:", len(s16_news_feed()))
print("s17:", len(s17_news_details()))
print("s18:", len(s18_activities()))
print("s19:", len(s19_activity_details()))
print("s20:", len(s20_registration_confirm()))
