"""Download official logos and seals for Thai universities from Wikipedia / Wikimedia Commons."""
import os
import json
import urllib.request
import urllib.parse
import re
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DEST_DIR = os.path.join(HERE, "assets", "unis")
DEST_OPT_DIR = os.path.join(HERE, "assets_opt", "unis")
os.makedirs(DEST_DIR, exist_ok=True)
os.makedirs(DEST_OPT_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'ThaiSuksaEducationApp/1.0 (https://silpakorn.edu; kitbumrung_t@silpakorn.edu)'
}

UNIVERSITIES = [
    # Slug, Page Title, Short Abbr, Brand Color, Fallback English, Campus
    ("cmu", "มหาวิทยาลัยเชียงใหม่", "CMU", "#8B5CF6", "Chiang Mai University", "อำเภอเมือง เชียงใหม่"),
    ("kku", "มหาวิทยาลัยขอนแก่น", "KKU", "#B45309", "Khon Kaen University", "อำเภอเมือง ขอนแก่น"),
    ("psu", "มหาวิทยาลัยสงขลานครินทร์", "PSU", "#0284C7", "Prince of Songkla University", "หาดใหญ่ / ปัตตานี"),
    ("kmitl", "สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง", "KMITL", "#EA580C", "King Mongkut's Institute of Technology Ladkrabang", "เขตลาดกระบัง กรุงเทพฯ"),
    ("kmutt", "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี", "KMUTT", "#DC2626", "King Mongkut's University of Technology Thonburi", "บางมด / บางขุนเทียน"),
    ("kmutnb", "มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ", "KMUTNB", "#C2410C", "King Mongkut's University of Technology North Bangkok", "เขตบางซื่อ กรุงเทพฯ"),
    ("swu", "มหาวิทยาลัยศรีนครินทรวิโรฒ", "SWU", "#BE123C", "Srinakharinwirot University", "ประสานมิตร / องครักษ์"),
    ("buu", "มหาวิทยาลัยบูรพา", "BUU", "#D97706", "Burapha University", "บางแสน ชลบุรี"),
    ("mfu", "มหาวิทยาลัยแม่ฟ้าหลวง", "MFU", "#B91C1C", "Mae Fah Luang University", "อำเภอเมือง เชียงราย"),
    ("nu", "มหาวิทยาลัยนเรศวร", "NU", "#7C3AED", "Naresuan University", "อำเภอเมือง พิษณุโลก"),
    ("up", "มหาวิทยาลัยพะเยา", "UP", "#9333EA", "University of Phayao", "อำเภอเมือง พะเยา"),
    ("ru", "มหาวิทยาลัยรามคำแหง", "RU", "#1D4ED8", "Ramkhamhaeng University", "หัวหมาก / บางนา"),
    ("stou", "มหาวิทยาลัยสุโขทัยธรรมาธิราช", "STOU", "#047857", "Sukhothai Thammathirat Open University", "ปากเกร็ด นนทบุรี"),
    ("sut", "มหาวิทยาลัยเทคโนโลยีสุรนารี", "SUT", "#C2410C", "Suranaree University of Technology", "อำเภอเมือง นครราชสีมา"),
    ("wu", "มหาวิทยาลัยวลัยลักษณ์", "WU", "#D97706", "Walailak University", "ท่าศาลา นครศรีธรรมราช"),
    ("mju", "มหาวิทยาลัยแม่โจ้", "MJU", "#15803D", "Maejo University", "สันทราย เชียงใหม่"),
    ("msu", "มหาวิทยาลัยมหาสารคาม", "MSU", "#CA8A04", "Mahasarakham University", "กันทรวิชัย มหาสารคาม"),
    ("ubu", "มหาวิทยาลัยอุบลราชธานี", "UBU", "#B45309", "Ubon Ratchathani University", "วารินชำราบ อุบลราชธานี"),
    ("tsu", "มหาวิทยาลัยทักษิณ", "TSU", "#4338CA", "Thaksin University", "อำเภอเมือง สงขลา / พัทลุง"),
    ("sdu", "มหาวิทยาลัยสวนดุสิต", "SDU", "#0369A1", "Suan Dusit University", "เขตดุสิต กรุงเทพฯ"),
    ("nmu", "มหาวิทยาลัยนวมินทราธิราช", "NMU", "#0E7490", "Navamindradhiraj University", "เขตดุสิต กรุงเทพฯ"),

    # Rajabhat Universities
    ("ssru", "มหาวิทยาลัยราชภัฏสวนสุนันทา", "SSRU", "#0284C7", "Suan Sunandha Rajabhat University", "เขตดุสิต กรุงเทพฯ"),
    ("bsru", "มหาวิทยาลัยราชภัฏบ้านสมเด็จเจ้าพระยา", "BSRU", "#475569", "Bansomdejchaopraya Rajabhat University", "เขตธนบุรี กรุงเทพฯ"),
    ("cru", "มหาวิทยาลัยราชภัฏจันทรเกษม", "CRU", "#CA8A04", "Chandrakasem Rajabhat University", "เขตจตุจักร กรุงเทพฯ"),
    ("pnru", "มหาวิทยาลัยราชภัฏพระนคร", "PNRU", "#15803D", "Phranakhon Rajabhat University", "เขตบางเขน กรุงเทพฯ"),
    ("dru", "มหาวิทยาลัยราชภัฏธนบุรี", "DRU", "#4338CA", "Dhonburi Rajabhat University", "เขตธนบุรี กรุงเทพฯ"),
    ("cmru", "มหาวิทยาลัยราชภัฏเชียงใหม่", "CMRU", "#B45309", "Chiang Mai Rajabhat University", "อำเภอเมือง เชียงใหม่"),
    ("nrru", "มหาวิทยาลัยราชภัฏนครราชสีมา", "NRRU", "#B91C1C", "Nakhon Ratchasima Rajabhat University", "อำเภอเมือง นครราชสีมา"),
    ("npru", "มหาวิทยาลัยราชภัฏนครปฐม", "NPRU", "#047857", "Nakhon Pathom Rajabhat University", "อำเภอเมือง นครปฐม"),
    ("vru", "มหาวิทยาลัยราชภัฏวไลยอลงกรณ์ ในพระบรมราชูปถัมภ์", "VRU", "#1D4ED8", "Valaya Alongkorn Rajabhat University", "คลองหลวง ปทุมธานี"),
    ("sru", "มหาวิทยาลัยราชภัฏสุราษฎร์ธานี", "SRU", "#D97706", "Surat Thani Rajabhat University", "อำเภอเมือง สุราษฎร์ธานี"),

    # Rajamangala Universities (All 9 RMUTs)
    ("rmutt", "มหาวิทยาลัยเทคโนโลยีราชมงคลธัญบุรี", "RMUTT", "#0284C7", "RMUT Thanyaburi", "คลองหก ปทุมธานี"),
    ("rmutk", "มหาวิทยาลัยเทคโนโลยีราชมงคลกรุงเทพ", "RMUTK", "#15803D", "RMUT Krungthep", "เขตสาทร กรุงเทพฯ"),
    ("rmutp", "มหาวิทยาลัยเทคโนโลยีราชมงคลพระนคร", "RMUTP", "#7C3AED", "RMUT Phra Nakhon", "เขตดุสิต กรุงเทพฯ"),
    ("rmutr", "มหาวิทยาลัยเทคโนโลยีราชมงคลรัตนโกสินทร์", "RMUTR", "#DC2626", "RMUT Rattanakosin", "ศาลายา นครปฐม"),
    ("rmutto", "มหาวิทยาลัยเทคโนโลยีราชมงคลตะวันออก", "RMUTTO", "#EA580C", "RMUT Tawan-ok", "บางพระ ชลบุรี"),
    ("rmutsb", "มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ", "RMUTSB", "#CA8A04", "RMUT Suvarnabhumi", "พระนครศรีอยุธยา"),
    ("rmutl", "มหาวิทยาลัยเทคโนโลยีราชมงคลล้านนา", "RMUTL", "#B45309", "RMUT Lanna", "อำเภอเมือง เชียงใหม่"),
    ("rmuti", "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน", "RMUTI", "#B91C1C", "RMUT Isan", "อำเภอเมือง นครราชสีมา"),
    ("rmuts", "มหาวิทยาลัยเทคโนโลยีราชมงคลศรีวิชัย", "RMUTS", "#047857", "RMUT Srivijaya", "อำเภอเมือง สงขลา"),

    # Private Universities
    ("bu", "มหาวิทยาลัยกรุงเทพ", "BU", "#DC2626", "Bangkok University", "วิทยาเขตรังสิต / กล้วยน้ำไท"),
    ("rsu", "มหาวิทยาลัยรังสิต", "RSU", "#0284C7", "Rangsit University", "เมืองเอก ปทุมธานี"),
    ("utcc", "มหาวิทยาลัยหอการค้าไทย", "UTCC", "#1D4ED8", "University of the Thai Chamber of Commerce", "เขตดินแดง กรุงเทพฯ"),
    ("au", "มหาวิทยาลัยอัสสัมชัญ", "AU", "#B91C1C", "Assumption University (ABAC)", "สุวรรณภูมิ / หัวหมาก"),
    ("spu", "มหาวิทยาลัยศรีปทุม", "SPU", "#EA580C", "Sripatum University", "เขตจตุจักร กรุงเทพฯ"),
    ("dpu", "มหาวิทยาลัยธุรกิจบัณฑิตย์", "DPU", "#7C3AED", "Dhurakij Pundit University", "เขตหลักสี่ กรุงเทพฯ"),
    ("kbu", "มหาวิทยาลัยเกษมบัณฑิต", "KBU", "#047857", "Kasem Bundit University", "พัฒนาการ / ร่มเกล้า"),
    ("pyu", "มหาวิทยาลัยพายัพ", "PYU", "#0284C7", "Payap University", "อำเภอเมือง เชียงใหม่"),
    ("hcu", "มหาวิทยาลัยหัวเฉียวเฉลิมพระเกียรติ", "HCU", "#CA8A04", "Huachiew Chalermprakiet University", "บางพลี สมุทรปราการ"),
    ("tni", "สถาบันเทคโนโลยีไทย-ญี่ปุ่น", "TNI", "#B91C1C", "Thai-Nichi Institute of Technology", "พัฒนาการ กรุงเทพฯ"),
]

def get_page_image_url(page_title):
    # Try pageimages first
    url = f"https://th.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(page_title)}&prop=pageimages&pithumbsize=200&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            d = json.loads(r.read().decode('utf-8'))
            pages = d.get('query', {}).get('pages', {})
            for pid in pages:
                src = pages[pid].get('thumbnail', {}).get('source')
                if src:
                    return src
    except Exception:
        pass

    # Try parsing infobox wikitext
    url = f"https://th.wikipedia.org/w/api.php?action=parse&page={urllib.parse.quote(page_title)}&prop=wikitext&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=8) as r:
            d = json.loads(r.read().decode('utf-8'))
            wt = d.get('parse', {}).get('wikitext', {}).get('*', '')
            m = re.search(r'(?:logo|image|seal|ตรา|สัญลักษณ์)\s*=\s*([^|\n}]+)', wt, re.I)
            if m:
                raw = m.group(1).strip()
                raw = re.sub(r'\[\[(?:ไฟล์|File):', '', raw, flags=re.I)
                file_title = raw.split('|')[0].strip('[] ')
                if file_title:
                    furl = f"https://th.wikipedia.org/w/api.php?action=query&titles=File:{urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=200&format=json"
                    req2 = urllib.request.Request(furl, headers=HEADERS)
                    with urllib.request.urlopen(req2, timeout=8) as r2:
                        d2 = json.loads(r2.read().decode('utf-8'))
                        for pid in d2.get('query', {}).get('pages', {}):
                            info = d2['query']['pages'][pid].get('imageinfo', [{}])[0]
                            return info.get('thumburl') or info.get('url')
    except Exception:
        pass

    return None

def download_file(url, out_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=12) as r, open(out_path, 'wb') as f:
        f.write(r.read())

print(f"Starting logo fetch for {len(UNIVERSITIES)} universities...")

success_count = 0
for slug, page_title, abbr, col, en, campus in UNIVERSITIES:
    dest_file = os.path.join(DEST_DIR, f"{slug}.png")
    dest_opt_file = os.path.join(DEST_OPT_DIR, f"{slug}.png")

    if os.path.exists(dest_file) and os.path.getsize(dest_file) > 2000:
        print(f"[{slug}] already exists ({os.path.getsize(dest_file)} bytes)")
        if not os.path.exists(dest_opt_file):
            import shutil
            shutil.copyfile(dest_file, dest_opt_file)
        success_count += 1
        continue

    time.sleep(0.4)
    img_url = get_page_image_url(page_title)
    if img_url:
        try:
            download_file(img_url, dest_file)
            import shutil
            shutil.copyfile(dest_file, dest_opt_file)
            size = os.path.getsize(dest_file)
            print(f"[{slug}] Downloaded successfully: {size} bytes from {img_url[:60]}...")
            success_count += 1
        except Exception as e:
            print(f"[{slug}] Download failed: {e}")
    else:
        print(f"[{slug}] No URL found for '{page_title}'")

print(f"\nDone! Downloaded/Confirmed {success_count}/{len(UNIVERSITIES)} logos.")
